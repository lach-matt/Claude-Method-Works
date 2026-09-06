import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';

// Ψ_Z(t) plotted in 3D configuration space (n, ℓ, k)
// Three-state hydrogen model:
//   |0⟩ = 1s = (n=1, ℓ=0, k=1)  ground state
//   |1⟩ = 2s = (n=2, ℓ=0, k=1)  n→n+1 shell excitation
//   |2⟩ = 2p = (n=2, ℓ=1, k=1)  subshell excitation
//
// c₀(t) = cos(t),  c₁(t) = c₂(t) = sin(t)/√2
// p_i(t) = |c_i(t)|²
// ⟨Q⟩(t) = Σ p_i · Q_i
// σ²(t)  = Σ p_i · |Q_i − ⟨Q⟩|²

const OMEGA = 0.5;
const HIGHLIGHT_HEX = 0xffd166;
const HIGHLIGHT_CSS = '#FFD166';

const STATES = [
  { label: '1s', Q: [1, 0, 1], color: 0x52e3c2, css: '#52E3C2' },
  { label: '2s', Q: [2, 0, 1], color: 0x7be8d4, css: '#7BE8D4' },
  { label: '2p', Q: [2, 1, 1], color: 0xf6a150, css: '#F6A150' },
];

// Scale so the 3-axis lattice reads clearly
const SX = 1.8, SY = 2.2, SZ = 1.8;
function latticePos(n, l, k) {
  return [(n - 1.5) * SX, (l - 0.5) * SY, (k - 1) * SZ];
}

function makeLabelSprite(text, color, scale = 0.55) {
  const canvas = document.createElement('canvas');
  canvas.width = 256; canvas.height = 128;
  const ctx = canvas.getContext('2d');
  ctx.font = '600 54px Space Grotesk, sans-serif';
  ctx.fillStyle = color;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(text, 128, 68);
  const tex = new THREE.CanvasTexture(canvas);
  tex.minFilter = THREE.LinearFilter;
  const mat = new THREE.SpriteMaterial({ map: tex, transparent: true, depthTest: false });
  const sp = new THREE.Sprite(mat);
  sp.scale.set(scale * 2, scale, 1);
  return sp;
}

function makeAxisLine(from, to, color) {
  const geo = new THREE.BufferGeometry().setFromPoints([
    new THREE.Vector3(...from), new THREE.Vector3(...to),
  ]);
  return new THREE.Line(geo, new THREE.LineBasicMaterial({ color, transparent: true, opacity: 0.5 }));
}

export default function PsiCloud3D() {
  const mountRef = useRef(null);
  const readoutRef = useRef(null);
  const [playing, setPlaying] = useState(true);
  const playRef = useRef(true);
  useEffect(() => { playRef.current = playing; }, [playing]);

  useEffect(() => {
    const mount = mountRef.current;
    let W = mount.clientWidth, H = mount.clientHeight;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x070b14);
    const camera = new THREE.PerspectiveCamera(42, W / H, 0.1, 100);
    camera.position.set(0, 0, 10);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.setSize(W, H);
    mount.appendChild(renderer.domElement);

    scene.add(new THREE.AmbientLight(0xffffff, 0.9));
    const dl = new THREE.DirectionalLight(0xffffff, 0.7);
    dl.position.set(6, 8, 10); scene.add(dl);

    const group = new THREE.Group();
    scene.add(group);

    // ── Axis lines ──────────────────────────────────────────────────────
    const origin = latticePos(1, 0, 1);
    const nEnd   = latticePos(3, 0, 1);
    const lEnd   = latticePos(1, 2, 1);
    const kEnd   = latticePos(1, 0, 3);
    group.add(makeAxisLine(origin, nEnd, 0x52e3c2));
    group.add(makeAxisLine(origin, lEnd, 0xf6a150));
    group.add(makeAxisLine(origin, kEnd, 0xb18cf2));

    // axis tick marks
    for (let n = 1; n <= 2; n++) {
      const p = latticePos(n, 0, 1);
      const lbl = makeLabelSprite(`n=${n}`, '#52E3C2', 0.38);
      lbl.position.set(p[0], p[1] - 0.55, p[2]);
      group.add(lbl);
    }
    for (let l = 0; l <= 1; l++) {
      const p = latticePos(1, l, 1);
      const lbl = makeLabelSprite(`ℓ=${l}`, '#F6A150', 0.38);
      lbl.position.set(p[0] - 0.85, p[1], p[2]);
      group.add(lbl);
    }
    for (let k = 1; k <= 2; k++) {
      const p = latticePos(1, 0, k);
      const lbl = makeLabelSprite(`k=${k}`, '#B18CF2', 0.38);
      lbl.position.set(p[0], p[1], p[2] - 0.55);
      group.add(lbl);
    }

    // axis name labels at ends
    const nAxisLbl = makeLabelSprite('n (shell)', '#52E3C2', 0.46);
    nAxisLbl.position.set(...latticePos(3.4, 0, 1));
    group.add(nAxisLbl);
    const lAxisLbl = makeLabelSprite('ℓ (subshell)', '#F6A150', 0.46);
    lAxisLbl.position.set(...latticePos(1, 2.5, 1));
    group.add(lAxisLbl);
    const kAxisLbl = makeLabelSprite('k (e⁻ count)', '#B18CF2', 0.46);
    kAxisLbl.position.set(...latticePos(1, 0, 3.5));
    group.add(kAxisLbl);

    // ── Basis-state nodes ───────────────────────────────────────────────
    const nodeGeo = new THREE.SphereGeometry(1, 24, 24);
    const nodeMeshes = STATES.map((s) => {
      const mat = new THREE.MeshStandardMaterial({
        color: s.color, transparent: true, opacity: 0.55, roughness: 0.3, metalness: 0.1,
      });
      const mesh = new THREE.Mesh(nodeGeo, mat);
      mesh.position.set(...latticePos(...s.Q));
      group.add(mesh);

      const lbl = makeLabelSprite(s.label, s.css, 0.48);
      lbl.position.set(...latticePos(...s.Q).map((v, i) => i === 1 ? v + 0.85 : v));
      group.add(lbl);
      return mesh;
    });

    // ── Connecting edges (neighbourhood) ────────────────────────────────
    [[0,1],[1,2]].forEach(([a,b]) => {
      const geo = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(...latticePos(...STATES[a].Q)),
        new THREE.Vector3(...latticePos(...STATES[b].Q)),
      ]);
      group.add(new THREE.Line(geo, new THREE.LineBasicMaterial({ color: 0x3a4a66, transparent: true, opacity: 0.6 })));
    });

    // ── ⟨Q⟩(t) expectation marker ────────────────────────────────────────
    const expGeo = new THREE.SphereGeometry(0.18, 16, 16);
    const expMesh = new THREE.Mesh(expGeo, new THREE.MeshBasicMaterial({ color: HIGHLIGHT_HEX }));
    const haloMesh = new THREE.Mesh(
      new THREE.SphereGeometry(0.33, 14, 14),
      new THREE.MeshBasicMaterial({ color: HIGHLIGHT_HEX, transparent: true, opacity: 0.22, wireframe: true })
    );
    group.add(expMesh); group.add(haloMesh);
    const expLbl = makeLabelSprite('⟨Q⟩(t)', HIGHLIGHT_CSS, 0.48);
    group.add(expLbl);

    // ── σ²(t) variance sphere (grows/shrinks) ────────────────────────────
    const varGeo = new THREE.SphereGeometry(1, 16, 16);
    const varMesh = new THREE.Mesh(varGeo, new THREE.MeshBasicMaterial({
      color: HIGHLIGHT_HEX, transparent: true, opacity: 0.07, wireframe: false, depthWrite: false,
    }));
    group.add(varMesh);

    // ── Trajectory trail of ⟨Q⟩ ─────────────────────────────────────────
    const TRAIL = 48;
    const trailPts = Array(TRAIL).fill(null).map(() => new THREE.Vector3());
    const trailGeo = new THREE.BufferGeometry().setFromPoints(trailPts);
    const trailLine = new THREE.Line(trailGeo, new THREE.LineBasicMaterial({
      color: HIGHLIGHT_HEX, transparent: true, opacity: 0.45,
    }));
    group.add(trailLine);
    let trailHead = 0;

    group.rotation.set(-0.35, 0.55, 0);

    // ── Drag to rotate ────────────────────────────────────────────────────
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
      camera.position.z = Math.max(4, Math.min(18, camera.position.z + e.deltaY * 0.007));
    }, { passive: false });
    window.addEventListener('resize', () => {
      W = mount.clientWidth; H = mount.clientHeight;
      camera.aspect = W / H; camera.updateProjectionMatrix();
      renderer.setSize(W, H);
    });

    let raf, t = 0, lastMs = performance.now();
    function animate() {
      const now = performance.now();
      if (playRef.current) t += (now - lastMs) / 1000 * OMEGA;
      lastMs = now;

      const p0 = Math.cos(t) ** 2;
      const ph = Math.sin(t) ** 2 / 2;
      const probs = [p0, ph, ph];

      // scale nodes by sqrt(p) → volume ∝ p
      nodeMeshes.forEach((m, i) => {
        const r = 0.15 + 0.8 * Math.sqrt(probs[i]);
        m.scale.setScalar(r);
        m.material.opacity = 0.1 + 0.7 * probs[i];
      });

      // ⟨Q⟩
      let En = 0, El = 0, Ek = 0;
      STATES.forEach((s, i) => {
        En += probs[i] * s.Q[0]; El += probs[i] * s.Q[1]; Ek += probs[i] * s.Q[2];
      });
      const [ex, ey, ez] = latticePos(En, El, Ek);
      expMesh.position.set(ex, ey, ez);
      haloMesh.position.set(ex, ey, ez);
      expLbl.position.set(ex, ey + 0.6, ez);

      // σ²
      let sig2 = 0;
      STATES.forEach((s, i) => {
        sig2 += probs[i] * ((s.Q[0]-En)**2 + (s.Q[1]-El)**2 + (s.Q[2]-Ek)**2);
      });
      const sigR = Math.sqrt(sig2) * 0.7;
      varMesh.position.set(ex, ey, ez);
      varMesh.scale.setScalar(sigR);
      varMesh.material.opacity = sig2 > 0.01 ? 0.09 : 0;

      // trail
      trailPts[trailHead].set(ex, ey, ez);
      trailHead = (trailHead + 1) % TRAIL;
      const ordered = [];
      for (let i = 0; i < TRAIL; i++) ordered.push(trailPts[(trailHead + i) % TRAIL]);
      trailGeo.setFromPoints(ordered);
      trailGeo.attributes.position.needsUpdate = true;

      // readout
      if (readoutRef.current) {
        readoutRef.current.textContent =
          `|c\u2080|\u00b2=${p0.toFixed(3)}  |c\u2081|\u00b2=|c\u2082|\u00b2=${ph.toFixed(3)}` +
          `   \u27e8n\u27e9=${En.toFixed(2)} \u27e8\u2113\u27e9=${El.toFixed(2)} \u27e8k\u27e9=${Ek.toFixed(2)}` +
          `   \u03c3\u00b2=${sig2.toFixed(3)}`;
      }

      renderer.render(scene, camera);
      raf = requestAnimationFrame(animate);
    }
    animate();

    return () => {
      cancelAnimationFrame(raf);
      mount.removeChild(renderer.domElement);
      renderer.dispose();
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
          Ψ_H(t) — 3D configuration-space plot
        </div>
        <div style={{ fontSize: '11px', color: '#8B97AC', marginTop: '3px', fontFamily: "'JetBrains Mono', monospace", lineHeight: 1.5 }}>
          axes: n (shell) · ℓ (subshell) · k (e⁻ count) &nbsp;|&nbsp;
          sphere size ∝ |c_i(t)|² &nbsp;|&nbsp;
          <span style={{ color: HIGHLIGHT_CSS }}>gold dot</span>: ⟨Q⟩(t) &nbsp;|&nbsp; gold trail: path of expectation &nbsp;|&nbsp; haze: σ²(t) spread
        </div>
      </div>

      <div ref={mountRef} style={{ flex: 1, minHeight: 0 }} />

      <div style={{
        padding: '12px 18px', borderTop: '1px solid rgba(255,255,255,0.06)', flexShrink: 0,
        minHeight: '52px', display: 'flex', alignItems: 'center', gap: '12px', justifyContent: 'space-between',
      }}>
        <div ref={readoutRef} style={{ fontSize: '11px', color: '#C7D0DD', fontFamily: "'JetBrains Mono', monospace" }} />
        <button
          onClick={() => setPlaying(s => !s)}
          style={{
            background: playing ? 'rgba(255,209,102,0.12)' : 'rgba(255,255,255,0.08)',
            border: '1px solid rgba(255,209,102,0.35)', color: HIGHLIGHT_CSS,
            borderRadius: '6px', padding: '6px 12px', fontSize: '11px',
            fontFamily: "'Inter', sans-serif", cursor: 'pointer', flexShrink: 0,
          }}
        >{playing ? 'Pause' : 'Play'}</button>
      </div>
    </div>
  );
}