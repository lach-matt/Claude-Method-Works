import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';

// Ψ_Z(t) plotted in 3D configuration space (n, ℓ, k) for H, He, and Fe simultaneously
//
// H  (Z=1):  ground 1s¹ = (1,0,1)  → Q1=(2,0,1)  Q2=(2,1,1)
// He (Z=2):  ground 1s² = (1,0,2)  → Q1=(2,0,2)  Q2=(2,1,2)
// Fe (Z=26): ground 3d⁶ = (3,2,6)  → Q1=(4,2,6)  Q2=(3,3,6)
//
// p0(t) = cos²(t),  p1=p2 = sin²(t)/2
// ⟨Q⟩(t) = Σ pᵢ·Qᵢ    σ²(t) = Σ pᵢ·|Qᵢ−⟨Q⟩|²

const OMEGA = 0.45;

const ATOMS = [
  {
    sym: 'H', label: 'H  (1s\u00b9)', Z: 1,
    Q0: [1,0,1], Q1: [2,0,1], Q2: [2,1,1],
    groundColor: 0x52e3c2, css: '#52E3C2',
    excite1Color: 0x7be8d4, excite2Color: 0xf6a150,
  },
  {
    sym: 'He', label: 'He (1s\u00b2)', Z: 2,
    Q0: [1,0,2], Q1: [2,0,2], Q2: [2,1,2],
    groundColor: 0xf6a150, css: '#F6A150',
    excite1Color: 0xfab87a, excite2Color: 0xffd166,
  },
  {
    sym: 'Fe', label: 'Fe (3d\u2076)', Z: 26,
    Q0: [3,2,6], Q1: [4,2,6], Q2: [3,3,6],
    groundColor: 0xb18cf2, css: '#B18CF2',
    excite1Color: 0xc9a9f5, excite2Color: 0xe8a0d0,
  },
];

const HIGHLIGHT_CSS = '#FFD166';
const HIGHLIGHT_HEX = 0xffd166;

// Map all (n,ℓ,k) coordinates into a shared 3D canvas
// Scale so the spread between H/He (n=1-2) and Fe (n=3-4) is visible
const SX = 2.0, SY = 2.4, SZ = 0.55;
function latticePos(n, l, k) {
  return [(n - 2.5) * SX, (l - 1.5) * SY, (k - 4.5) * SZ];
}

function makeLabelSprite(text, color, scaleX = 1.1, scaleY = 0.55) {
  const canvas = document.createElement('canvas');
  canvas.width = 256; canvas.height = 128;
  const ctx = canvas.getContext('2d');
  ctx.font = '600 50px Space Grotesk, sans-serif';
  ctx.fillStyle = color;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(text, 128, 68);
  const tex = new THREE.CanvasTexture(canvas);
  tex.minFilter = THREE.LinearFilter;
  const mat = new THREE.SpriteMaterial({ map: tex, transparent: true, depthTest: false });
  const sp = new THREE.Sprite(mat);
  sp.scale.set(scaleX, scaleY, 1);
  return sp;
}

function makeAxisLine(from, to, color, opacity = 0.4) {
  const geo = new THREE.BufferGeometry().setFromPoints([
    new THREE.Vector3(...from), new THREE.Vector3(...to),
  ]);
  return new THREE.Line(geo, new THREE.LineBasicMaterial({ color, transparent: true, opacity }));
}

function sig2(p0, ph, Q0, Q1, Q2) {
  const En = p0*Q0[0] + ph*Q1[0] + ph*Q2[0];
  const El = p0*Q0[1] + ph*Q1[1] + ph*Q2[1];
  const Ek = p0*Q0[2] + ph*Q1[2] + ph*Q2[2];
  return (
    p0*((Q0[0]-En)**2+(Q0[1]-El)**2+(Q0[2]-Ek)**2) +
    ph*((Q1[0]-En)**2+(Q1[1]-El)**2+(Q1[2]-Ek)**2) +
    ph*((Q2[0]-En)**2+(Q2[1]-El)**2+(Q2[2]-Ek)**2)
  );
}

function expectation(p0, ph, Q0, Q1, Q2) {
  return [
    p0*Q0[0]+ph*Q1[0]+ph*Q2[0],
    p0*Q0[1]+ph*Q1[1]+ph*Q2[1],
    p0*Q0[2]+ph*Q1[2]+ph*Q2[2],
  ];
}

export default function PsiThreeElements() {
  const mountRef = useRef(null);
  const readoutRef = useRef(null);
  const [playing, setPlaying] = useState(true);
  const playRef = useRef(true);
  const [activeAtom, setActiveAtom] = useState(null);
  useEffect(() => { playRef.current = playing; }, [playing]);

  useEffect(() => {
    const mount = mountRef.current;
    let W = mount.clientWidth, H = mount.clientHeight;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x070b14);
    const camera = new THREE.PerspectiveCamera(42, W / H, 0.1, 120);
    camera.position.set(0, 0, 18);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.setSize(W, H);
    mount.appendChild(renderer.domElement);

    scene.add(new THREE.AmbientLight(0xffffff, 0.92));
    const dl = new THREE.DirectionalLight(0xffffff, 0.65);
    dl.position.set(6, 8, 12); scene.add(dl);

    const group = new THREE.Group();
    scene.add(group);

    // ── Shared axis frame ────────────────────────────────────────────────
    const axisOrigin = latticePos(1, 0, 1);
    group.add(makeAxisLine(axisOrigin, latticePos(5, 0, 1), 0x52e3c2));
    group.add(makeAxisLine(axisOrigin, latticePos(1, 4, 1), 0xf6a150));
    group.add(makeAxisLine(axisOrigin, latticePos(1, 0, 10), 0xb18cf2));

    // axis labels
    const nLbl = makeLabelSprite('n (shell)', '#52E3C2');
    nLbl.position.set(...latticePos(5.6, 0, 1)); group.add(nLbl);
    const lLbl = makeLabelSprite('\u2113 (subshell)', '#F6A150');
    lLbl.position.set(...latticePos(1, 4.7, 1)); group.add(lLbl);
    const kLbl = makeLabelSprite('k (e\u207b count)', '#B18CF2');
    kLbl.position.set(...latticePos(1, 0, 11.2)); group.add(kLbl);

    // tick marks on n axis
    for (let n = 1; n <= 4; n++) {
      const lbl = makeLabelSprite(`${n}`, '#8B97AC', 0.4, 0.35);
      const p = latticePos(n, 0, 1);
      lbl.position.set(p[0], p[1] - 0.55, p[2]); group.add(lbl);
    }
    // tick marks on l axis
    for (let l = 0; l <= 3; l++) {
      const names = ['s','p','d','f'];
      const lbl = makeLabelSprite(names[l], '#8B97AC', 0.38, 0.32);
      const p = latticePos(1, l, 1);
      lbl.position.set(p[0] - 0.9, p[1], p[2]); group.add(lbl);
    }

    // ── Per-atom setup ────────────────────────────────────────────────────
    const sphereGeo = new THREE.SphereGeometry(1, 22, 22);
    const atomData = ATOMS.map((atom) => {
      const states = [atom.Q0, atom.Q1, atom.Q2];
      const colors = [atom.groundColor, atom.excite1Color, atom.excite2Color];

      // state nodes
      const nodeMeshes = states.map((Q, i) => {
        const mat = new THREE.MeshStandardMaterial({
          color: colors[i], transparent: true, opacity: 0.5, roughness: 0.3, metalness: 0.1,
        });
        const mesh = new THREE.Mesh(sphereGeo, mat);
        mesh.position.set(...latticePos(...Q));
        group.add(mesh);
        return mesh;
      });

      // node label on ground state
      const lbl = makeLabelSprite(atom.label, atom.css, 1.2, 0.45);
      lbl.position.set(
        latticePos(...atom.Q0)[0],
        latticePos(...atom.Q0)[1] + 0.9,
        latticePos(...atom.Q0)[2],
      );
      group.add(lbl);

      // neighbourhood edges
      [[0,1],[1,2]].forEach(([a,b]) => {
        const geo = new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(...latticePos(...states[a])),
          new THREE.Vector3(...latticePos(...states[b])),
        ]);
        group.add(new THREE.Line(geo, new THREE.LineBasicMaterial({
          color: atom.groundColor, transparent: true, opacity: 0.35,
        })));
      });

      // ⟨Q⟩ expectation marker
      const expMesh = new THREE.Mesh(
        new THREE.SphereGeometry(0.17, 14, 14),
        new THREE.MeshBasicMaterial({ color: atom.groundColor }),
      );
      const haloMesh = new THREE.Mesh(
        new THREE.SphereGeometry(0.32, 12, 12),
        new THREE.MeshBasicMaterial({ color: atom.groundColor, transparent: true, opacity: 0.2, wireframe: true }),
      );
      group.add(expMesh); group.add(haloMesh);

      // σ² variance sphere
      const varMesh = new THREE.Mesh(
        new THREE.SphereGeometry(1, 14, 14),
        new THREE.MeshBasicMaterial({ color: atom.groundColor, transparent: true, opacity: 0.07, depthWrite: false }),
      );
      group.add(varMesh);

      // trail
      const TRAIL = 52;
      const trailPts = Array.from({ length: TRAIL }, () => new THREE.Vector3(...latticePos(...atom.Q0)));
      const trailGeo = new THREE.BufferGeometry().setFromPoints(trailPts);
      const trailLine = new THREE.Line(trailGeo, new THREE.LineBasicMaterial({
        color: atom.groundColor, transparent: true, opacity: 0.4,
      }));
      group.add(trailLine);

      return { atom, nodeMeshes, expMesh, haloMesh, varMesh, trailPts, trailGeo, trailHead: 0 };
    });

    group.rotation.set(-0.3, 0.55, 0);

    // ── Drag ─────────────────────────────────────────────────────────────
    let isDragging = false, last = { x: 0, y: 0 };
    const el = renderer.domElement;
    el.style.touchAction = 'none';
    el.addEventListener('pointerdown', (e) => { isDragging = true; last = { x: e.clientX, y: e.clientY }; });
    el.addEventListener('pointermove', (e) => {
      if (!isDragging) return;
      group.rotation.y += (e.clientX - last.x) * 0.006;
      group.rotation.x = Math.max(-1.4, Math.min(1.4, group.rotation.x + (e.clientY - last.y) * 0.006));
      last = { x: e.clientX, y: e.clientY };
    });
    el.addEventListener('pointerup', () => { isDragging = false; });
    el.addEventListener('pointerleave', () => { isDragging = false; });
    el.addEventListener('wheel', (e) => {
      e.preventDefault();
      camera.position.z = Math.max(6, Math.min(30, camera.position.z + e.deltaY * 0.008));
    }, { passive: false });
    window.addEventListener('resize', () => {
      W = mount.clientWidth; H = mount.clientHeight;
      camera.aspect = W / H; camera.updateProjectionMatrix();
      renderer.setSize(W, H);
    });

    // ── Animation ─────────────────────────────────────────────────────────
    let raf, t = 0, lastMs = performance.now();
    function animate() {
      const now = performance.now();
      if (playRef.current) t += (now - lastMs) / 1000 * OMEGA;
      lastMs = now;

      const p0 = Math.cos(t) ** 2;
      const ph = Math.sin(t) ** 2 / 2;

      const readoutLines = [];

      atomData.forEach(({ atom, nodeMeshes, expMesh, haloMesh, varMesh, trailPts, trailGeo }, ai) => {
        const probs = [p0, ph, ph];
        const states = [atom.Q0, atom.Q1, atom.Q2];

        nodeMeshes.forEach((m, i) => {
          const r = 0.14 + 0.75 * Math.sqrt(probs[i]);
          m.scale.setScalar(r);
          m.material.opacity = 0.1 + 0.65 * probs[i];
        });

        const [En, El, Ek] = expectation(p0, ph, atom.Q0, atom.Q1, atom.Q2);
        const [ex, ey, ez] = latticePos(En, El, Ek);
        expMesh.position.set(ex, ey, ez);
        haloMesh.position.set(ex, ey, ez);

        const s2 = sig2(p0, ph, atom.Q0, atom.Q1, atom.Q2);
        const sigR = Math.sqrt(s2) * 0.65;
        varMesh.position.set(ex, ey, ez);
        varMesh.scale.setScalar(Math.max(0.01, sigR));
        varMesh.material.opacity = s2 > 0.01 ? 0.08 : 0;

        // trail update
        const head = atomData[ai].trailHead;
        trailPts[head].set(ex, ey, ez);
        atomData[ai].trailHead = (head + 1) % trailPts.length;
        const ordered = [];
        for (let i = 0; i < trailPts.length; i++)
          ordered.push(trailPts[(atomData[ai].trailHead + i) % trailPts.length]);
        trailGeo.setFromPoints(ordered);
        trailGeo.attributes.position.needsUpdate = true;

        readoutLines.push(
          `${atom.sym}: \u27e8n\u27e9=${En.toFixed(2)} \u27e8\u2113\u27e9=${El.toFixed(2)} \u27e8k\u27e9=${Ek.toFixed(2)}  \u03c3\u00b2=${s2.toFixed(3)}`
        );
      });

      if (readoutRef.current) {
        readoutRef.current.innerHTML = readoutLines.join('&nbsp;&nbsp;|&nbsp;&nbsp;');
      }

      renderer.render(scene, camera);
      raf = requestAnimationFrame(animate);
    }
    animate();

    return () => {
      cancelAnimationFrame(raf);
      mount.removeChild(renderer.domElement);
      renderer.dispose();
      sphereGeo.dispose();
    };
  }, []);

  return (
    <div style={{
      width: '100%', height: '100vh', background: '#070B14', color: '#E7ECF3',
      fontFamily: "'Inter', sans-serif", display: 'flex', flexDirection: 'column', overflow: 'hidden',
    }}>
      <style>{`@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;600&display=swap');`}</style>

      <div style={{ padding: '14px 18px 10px', borderBottom: '1px solid rgba(255,255,255,0.06)', flexShrink: 0 }}>
        <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: '17px' }}>
          \u03a8_Z(t) \u2014 H, He, Fe in shared configuration space
        </div>
        <div style={{ fontSize: '11px', color: '#8B97AC', marginTop: '3px', fontFamily: "'JetBrains Mono', monospace", lineHeight: 1.5 }}>
          axes: n \u00b7 \u2113 \u00b7 k &nbsp;|\&nbsp;
          <span style={{ color:'#52E3C2' }}>teal</span> = H &nbsp;
          <span style={{ color:'#F6A150' }}>orange</span> = He &nbsp;
          <span style={{ color:'#B18CF2' }}>purple</span> = Fe &nbsp;|\&nbsp;
          sphere size \u221d |c\u1d62|\u00b2 &nbsp;|\&nbsp; dot + trail = \u27e8Q\u27e9(t) &nbsp;|\&nbsp; haze = \u03c3\u00b2(t)
        </div>
      </div>

      <div ref={mountRef} style={{ flex: 1, minHeight: 0 }} />

      <div style={{
        padding: '10px 18px', borderTop: '1px solid rgba(255,255,255,0.06)', flexShrink: 0,
        minHeight: '48px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '10px',
      }}>
        <div ref={readoutRef} style={{
          fontSize: '10.5px', color: '#C7D0DD',
          fontFamily: "'JetBrains Mono', monospace", lineHeight: 1.6, flex: 1,
        }} />
        <button
          onClick={() => setPlaying(s => !s)}
          style={{
            background: playing ? 'rgba(255,209,102,0.12)' : 'rgba(255,255,255,0.08)',
            border: '1px solid rgba(255,209,102,0.35)', color: '#FFD166',
            borderRadius: '6px', padding: '6px 12px', fontSize: '11px',
            fontFamily: "'Inter', sans-serif", cursor: 'pointer', flexShrink: 0,
          }}
        >{playing ? 'Pause' : 'Play'}</button>
      </div>
    </div>
  );
}