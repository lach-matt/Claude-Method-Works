import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';

// Interaction expression for Iron (Z=26):
//   𝒮_Fe(t) = cos(2Ωt) · ΔQ_Fe
//   ΔQ_Fe = (-0.5, -0.5, 0)
//
// Visualised as the displacement between:
//   ⟨Q⟩(t)  from Ψ_Fe    (forward,  p0=cos²t,  ph=sin²t/2)
//   ⟨Q̄⟩(t) from Ψ⁻¹_Fe  (inverse,  p0=sin²t,  ph=cos²t/2)
//
// Fe ground state:   Q0 = (3, 2, 6)   3d⁶
// Shell excitation:  Q1 = (4, 2, 6)
// Subshell excit.:   Q2 = (3, 3, 6)

const OMEGA = 0.5;
const Q0 = [3, 2, 6];
const Q1 = [4, 2, 6];
const Q2 = [3, 3, 6];
const DQ = [-0.5, -0.5, 0];          // ΔQ_Fe

const FWD_HEX  = 0xb18cf2;   // purple  — forward Ψ
const FWD_CSS  = '#B18CF2';
const INV_HEX  = 0xe8b84b;   // amber   — inverse Ψ⁻¹
const INV_CSS  = '#E8B84B';
const INT_HEX  = 0xffd166;   // gold    — interaction 𝒮
const INT_CSS  = '#FFD166';

const SX=1.8, SY=2.2, SZ=0.52;
function lp(n,l,k){ return [(n-3.5)*SX, (l-2)*SY, (k-6)*SZ]; }

function fwdProbs(t){ return [Math.cos(t)**2, Math.sin(t)**2/2, Math.sin(t)**2/2]; }
function invProbs(t){ return [Math.sin(t)**2, Math.cos(t)**2/2, Math.cos(t)**2/2]; }

function expectation(probs, Q0, Q1, Q2){
  const [p0,p1,p2]=probs;
  return [p0*Q0[0]+p1*Q1[0]+p2*Q2[0], p0*Q0[1]+p1*Q1[1]+p2*Q2[1], p0*Q0[2]+p1*Q1[2]+p2*Q2[2]];
}

function sig2(probs, Q0, Q1, Q2){
  const E=expectation(probs,Q0,Q1,Q2), [p0,p1,p2]=probs;
  return (p0*((Q0[0]-E[0])**2+(Q0[1]-E[1])**2+(Q0[2]-E[2])**2)
        + p1*((Q1[0]-E[0])**2+(Q1[1]-E[1])**2+(Q1[2]-E[2])**2)
        + p2*((Q2[0]-E[0])**2+(Q2[1]-E[1])**2+(Q2[2]-E[2])**2));
}

function makeLabel(text, color, sw=1.1, sh=0.5){
  const c=document.createElement('canvas'); c.width=256; c.height=128;
  const ctx=c.getContext('2d');
  ctx.font='600 50px Space Grotesk,sans-serif';
  ctx.fillStyle=color; ctx.textAlign='center'; ctx.textBaseline='middle';
  ctx.fillText(text,128,68);
  const tex=new THREE.CanvasTexture(c); tex.minFilter=THREE.LinearFilter;
  const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:tex,transparent:true,depthTest:false}));
  sp.scale.set(sw,sh,1); return sp;
}

function axLine(a,b,color,op=0.4){
  const g=new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(...a),new THREE.Vector3(...b)]);
  return new THREE.Line(g,new THREE.LineBasicMaterial({color,transparent:true,opacity:op}));
}

const TRAIL_LEN = 80;

export default function InteractionFe() {
  const mountRef   = useRef(null);
  const readoutRef = useRef(null);
  const [playing, setPlaying] = useState(true);
  const playRef = useRef(true);
  useEffect(()=>{ playRef.current=playing; },[playing]);

  useEffect(()=>{
    const mount=mountRef.current;
    let W=mount.clientWidth, H=mount.clientHeight;

    const scene=new THREE.Scene();
    scene.background=new THREE.Color(0x070b14);
    const camera=new THREE.PerspectiveCamera(42,W/H,0.1,100);
    camera.position.set(0,0,12);

    const renderer=new THREE.WebGLRenderer({antialias:true});
    renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
    renderer.setSize(W,H);
    mount.appendChild(renderer.domElement);

    scene.add(new THREE.AmbientLight(0xffffff,0.95));
    const dl=new THREE.DirectionalLight(0xffffff,0.65); dl.position.set(6,8,12); scene.add(dl);

    const group=new THREE.Group();
    scene.add(group);

    // ── Axes ─────────────────────────────────────────────────────────────
    const orig=lp(1,0,1);
    group.add(axLine(orig, lp(5,0,1), 0x52e3c2));   // n
    group.add(axLine(orig, lp(1,4,1), 0xf6a150));   // ℓ
    group.add(axLine(orig, lp(1,0,14),0xb18cf2));   // k

    const nL=makeLabel('n','#52E3C2',0.5,0.38); nL.position.set(...lp(5.5,0,1)); group.add(nL);
    const lL=makeLabel('\u2113','#F6A150',0.5,0.38); lL.position.set(...lp(1,4.7,1)); group.add(lL);
    const kL=makeLabel('k','#B18CF2',0.5,0.38); kL.position.set(...lp(1,0,15.2)); group.add(kL);

    // tick labels on n
    [3,4].forEach(n=>{
      const lb=makeLabel(String(n),'#8B97AC',0.38,0.3);
      const p=lp(n,0,1); lb.position.set(p[0],p[1]-0.55,p[2]); group.add(lb);
    });
    // tick labels on ℓ
    ['d (2)','f (3)'].forEach((nm,i)=>{
      const lb=makeLabel(nm,'#8B97AC',0.7,0.3);
      const p=lp(1,i+2,1); lb.position.set(p[0]-1.1,p[1],p[2]); group.add(lb);
    });
    // k=6 marker
    const k6=makeLabel('k=6','#8B97AC',0.55,0.3);
    const p6=lp(1,0,6); k6.position.set(p6[0]-0.1,p6[1]-0.55,p6[2]); group.add(k6);

    // ── State nodes ───────────────────────────────────────────────────────
    const nodeGeo=new THREE.SphereGeometry(1,20,20);

    // Q0 ground — solid purple
    const q0Mesh=new THREE.Mesh(nodeGeo, new THREE.MeshStandardMaterial({color:FWD_HEX,roughness:0.3,metalness:0.1}));
    q0Mesh.position.set(...lp(...Q0)); group.add(q0Mesh);
    const q0Lbl=makeLabel('3d\u2076 (Q\u2080)',FWD_CSS,1.1,0.42); q0Lbl.position.set(...lp(Q0[0],Q0[1]+0.9,Q0[2])); group.add(q0Lbl);

    // Q1 — shell excitation
    const q1Mesh=new THREE.Mesh(nodeGeo, new THREE.MeshStandardMaterial({color:FWD_HEX,transparent:true,opacity:0.35,roughness:0.3}));
    q1Mesh.position.set(...lp(...Q1)); group.add(q1Mesh);
    const q1Lbl=makeLabel('4d\u2076 (Q\u2081)',FWD_CSS,1.1,0.42); q1Lbl.position.set(...lp(Q1[0],Q1[1]+0.9,Q1[2])); group.add(q1Lbl);

    // Q2 — subshell excitation
    const q2Mesh=new THREE.Mesh(nodeGeo, new THREE.MeshStandardMaterial({color:FWD_HEX,transparent:true,opacity:0.35,roughness:0.3}));
    q2Mesh.position.set(...lp(...Q2)); group.add(q2Mesh);
    const q2Lbl=makeLabel('3f\u2076 (Q\u2082)',FWD_CSS,1.1,0.42); q2Lbl.position.set(...lp(Q2[0],Q2[1]+0.9,Q2[2])); group.add(q2Lbl);

    // neighbourhood edges Q0-Q1, Q1-Q2
    [[Q0,Q1],[Q0,Q2]].forEach(([a,b])=>{
      const g=new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(...lp(...a)),new THREE.Vector3(...lp(...b))]);
      group.add(new THREE.Line(g,new THREE.LineBasicMaterial({color:FWD_HEX,transparent:true,opacity:0.3})));
    });

    // midpoint of Q1+Q2 — marks Q0 + ΔQ_Fe end
    const MID = [(Q1[0]+Q2[0])/2, (Q1[1]+Q2[1])/2, (Q1[2]+Q2[2])/2];
    const midMesh=new THREE.Mesh(new THREE.SphereGeometry(0.12,12,12),new THREE.MeshBasicMaterial({color:INT_HEX,transparent:true,opacity:0.7,wireframe:true}));
    midMesh.position.set(...lp(...MID)); group.add(midMesh);
    const midLbl=makeLabel('\u00bd(Q\u2081+Q\u2082)',INT_CSS,1.1,0.42); midLbl.position.set(...lp(MID[0],MID[1]+0.85,MID[2])); group.add(midLbl);

    // dashed ΔQ_Fe arrow: from midpoint to Q0
    const dqGeo=new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(...lp(...MID)),new THREE.Vector3(...lp(...Q0))]);
    const dqLine=new THREE.Line(dqGeo,new THREE.LineDashedMaterial({color:INT_HEX,dashSize:0.15,gapSize:0.1,transparent:true,opacity:0.8}));
    dqLine.computeLineDistances(); group.add(dqLine);
    const dqLbl=makeLabel('\u0394Q_Fe=(-0.5,-0.5,0)',INT_CSS,1.8,0.4); dqLbl.position.set(...lp(3.0,2.35,6)); group.add(dqLbl);

    // ── Forward ⟨Q⟩ expectation marker + trail ────────────────────────────
    const fwdExpMesh=new THREE.Mesh(new THREE.SphereGeometry(0.18,14,14),new THREE.MeshBasicMaterial({color:FWD_HEX}));
    const fwdHalo=new THREE.Mesh(new THREE.SphereGeometry(0.33,12,12),new THREE.MeshBasicMaterial({color:FWD_HEX,transparent:true,opacity:0.2,wireframe:true}));
    group.add(fwdExpMesh); group.add(fwdHalo);
    const fwdLbl=makeLabel('\u27e8Q\u27e9(t)',FWD_CSS,0.85,0.38); group.add(fwdLbl);

    const fTrailPts=Array.from({length:TRAIL_LEN},()=>new THREE.Vector3(...lp(...Q0)));
    const fTrailGeo=new THREE.BufferGeometry().setFromPoints(fTrailPts);
    const fTrail=new THREE.Line(fTrailGeo,new THREE.LineBasicMaterial({color:FWD_HEX,transparent:true,opacity:0.5}));
    group.add(fTrail);

    // ── Inverse ⟨Q̄⟩ expectation marker + trail ────────────────────────────
    const invExpMesh=new THREE.Mesh(new THREE.SphereGeometry(0.18,14,14),new THREE.MeshBasicMaterial({color:INV_HEX}));
    const invHalo=new THREE.Mesh(new THREE.SphereGeometry(0.33,12,12),new THREE.MeshBasicMaterial({color:INV_HEX,transparent:true,opacity:0.2,wireframe:true}));
    group.add(invExpMesh); group.add(invHalo);
    const invLbl=makeLabel('\u27e8Q\u0305\u27e9(t)',INV_CSS,0.9,0.38); group.add(invLbl);

    const iTrailPts=Array.from({length:TRAIL_LEN},()=>new THREE.Vector3(...lp(...Q0)));
    const iTrailGeo=new THREE.BufferGeometry().setFromPoints(iTrailPts);
    const iTrail=new THREE.Line(iTrailGeo,new THREE.LineBasicMaterial({color:INV_HEX,transparent:true,opacity:0.5}));
    group.add(iTrail);

    // ── Interaction vector 𝒮_Fe(t) — live gold arrow between the two ⟨Q⟩ ─
    const intGeo=new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(...lp(...Q0)),new THREE.Vector3(...lp(...Q0))]);
    const intLine=new THREE.Line(intGeo,new THREE.LineBasicMaterial({color:INT_HEX,transparent:true,opacity:0.9}));
    group.add(intLine);
    const intLbl=makeLabel('\u{1D4A2}_Fe(t)',INT_CSS,0.9,0.38); group.add(intLbl);

    // σ² variance hazes
    const fVarMesh=new THREE.Mesh(new THREE.SphereGeometry(1,14,14),new THREE.MeshBasicMaterial({color:FWD_HEX,transparent:true,opacity:0.07,depthWrite:false}));
    const iVarMesh=new THREE.Mesh(new THREE.SphereGeometry(1,14,14),new THREE.MeshBasicMaterial({color:INV_HEX,transparent:true,opacity:0.07,depthWrite:false}));
    group.add(fVarMesh); group.add(iVarMesh);

    group.rotation.set(-0.3,0.55,0);

    let fHead=0, iHead=0;

    // ── Drag & zoom ───────────────────────────────────────────────────────
    let isDragging=false, last={x:0,y:0};
    const domEl=renderer.domElement;
    domEl.style.touchAction='none';
    domEl.addEventListener('pointerdown',e=>{ isDragging=true; last={x:e.clientX,y:e.clientY}; });
    domEl.addEventListener('pointermove',e=>{
      if(!isDragging) return;
      group.rotation.y+=(e.clientX-last.x)*0.006;
      group.rotation.x=Math.max(-1.4,Math.min(1.4,group.rotation.x+(e.clientY-last.y)*0.006));
      last={x:e.clientX,y:e.clientY};
    });
    domEl.addEventListener('pointerup',()=>{ isDragging=false; });
    domEl.addEventListener('pointerleave',()=>{ isDragging=false; });
    domEl.addEventListener('wheel',e=>{ e.preventDefault(); camera.position.z=Math.max(5,Math.min(22,camera.position.z+e.deltaY*0.008)); },{passive:false});
    window.addEventListener('resize',()=>{ W=mount.clientWidth;H=mount.clientHeight;camera.aspect=W/H;camera.updateProjectionMatrix();renderer.setSize(W,H); });

    let raf, t=0, lastMs=performance.now();
    function animate(){
      const now=performance.now();
      if(playRef.current) t+=(now-lastMs)/1000*OMEGA;
      lastMs=now;

      const fp=fwdProbs(t), ip=invProbs(t);

      // Forward expectation
      const FE=expectation(fp,Q0,Q1,Q2);
      const fs2=sig2(fp,Q0,Q1,Q2);
      fwdExpMesh.position.set(...lp(...FE));
      fwdHalo.position.set(...lp(...FE));
      fwdLbl.position.set(lp(...FE)[0],lp(...FE)[1]+0.58,lp(...FE)[2]);
      fVarMesh.position.set(...lp(...FE));
      fVarMesh.scale.setScalar(Math.max(0.01,Math.sqrt(fs2)*0.7));
      fVarMesh.material.opacity=fs2>0.01?0.08:0;

      // Pulse node sizes
      q0Mesh.scale.setScalar(0.13+0.07*fp[0]);
      q1Mesh.scale.setScalar(0.09+0.12*fp[1]);
      q2Mesh.scale.setScalar(0.09+0.12*fp[2]);

      // Inverse expectation
      const IE=expectation(ip,Q0,Q1,Q2);
      const is2=sig2(ip,Q0,Q1,Q2);
      invExpMesh.position.set(...lp(...IE));
      invHalo.position.set(...lp(...IE));
      invLbl.position.set(lp(...IE)[0],lp(...IE)[1]+0.58,lp(...IE)[2]);
      iVarMesh.position.set(...lp(...IE));
      iVarMesh.scale.setScalar(Math.max(0.01,Math.sqrt(is2)*0.7));
      iVarMesh.material.opacity=is2>0.01?0.08:0;

      // Interaction vector
      const FA=lp(...FE), IA=lp(...IE);
      intGeo.setFromPoints([new THREE.Vector3(...FA),new THREE.Vector3(...IA)]);
      intGeo.attributes.position.needsUpdate=true;
      const midX=(FA[0]+IA[0])/2, midY=(FA[1]+IA[1])/2, midZ=(FA[2]+IA[2])/2;
      intLbl.position.set(midX,midY+0.55,midZ);

      // Interaction magnitude = cos(2t) * |ΔQ|
      const cos2t=Math.cos(2*t);
      const intMag=Math.abs(cos2t)*Math.sqrt(0.5); // |ΔQ_Fe|=1/√2

      // Trails
      fTrailPts[fHead].set(...lp(...FE)); fHead=(fHead+1)%TRAIL_LEN;
      const fOrd=[]; for(let i=0;i<TRAIL_LEN;i++) fOrd.push(fTrailPts[(fHead+i)%TRAIL_LEN]);
      fTrailGeo.setFromPoints(fOrd); fTrailGeo.attributes.position.needsUpdate=true;

      iTrailPts[iHead].set(...lp(...IE)); iHead=(iHead+1)%TRAIL_LEN;
      const iOrd=[]; for(let i=0;i<TRAIL_LEN;i++) iOrd.push(iTrailPts[(iHead+i)%TRAIL_LEN]);
      iTrailGeo.setFromPoints(iOrd); iTrailGeo.attributes.position.needsUpdate=true;

      if(readoutRef.current){
        readoutRef.current.textContent=
          `\u03a9t=${t.toFixed(2)}  cos(2\u03a9t)=${cos2t.toFixed(3)}  |\u{1D4A2}_Fe|=${intMag.toFixed(3)}`+
          `   \u27e8Q\u27e9=(${FE.map(v=>v.toFixed(2)).join(',')})  \u27e8Q\u0305\u27e9=(${IE.map(v=>v.toFixed(2)).join(',')})`;
      }

      renderer.render(scene,camera);
      raf=requestAnimationFrame(animate);
    }
    animate();

    return ()=>{
      cancelAnimationFrame(raf);
      mount.removeChild(renderer.domElement);
      renderer.dispose();
    };
  },[]);

  return (
    <div style={{width:'100%',height:'100vh',background:'#070B14',color:'#E7ECF3',fontFamily:"'Inter',sans-serif",display:'flex',flexDirection:'column',overflow:'hidden'}}>
      <style>{`@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;600&display=swap');`}</style>

      <div style={{padding:'14px 18px 10px',borderBottom:'1px solid rgba(255,255,255,0.06)',flexShrink:0}}>
        <div style={{fontFamily:"'Space Grotesk',sans-serif",fontWeight:700,fontSize:'17px'}}>
          \u{1D4A2}_Fe(t) = cos(2\u03a9t) \u00b7 \u0394Q_Fe &nbsp;&mdash;&nbsp; Iron interaction expression
        </div>
        <div style={{fontSize:'11px',color:'#8B97AC',marginTop:'3px',fontFamily:"'JetBrains Mono',monospace",lineHeight:1.5}}>
          <span style={{color:FWD_CSS}}>\u25cf \u03a8_Fe</span>: ground\u21923d\u2076 absorbing (cos\u00b2t) &nbsp;|&nbsp;
          <span style={{color:INV_CSS}}>\u25cf \u03a8\u207b\u00b9_Fe</span>: emitting (sin\u00b2t) &nbsp;|&nbsp;
          <span style={{color:'#FFD166'}}>\u2014 \u0394Q_Fe</span>: static vector (-0.5,-0.5,0) &nbsp;|&nbsp;
          <span style={{color:'#FFD166'}}>\u2500 \u{1D4A2}_Fe(t)</span>: live interaction
        </div>
      </div>

      <div ref={mountRef} style={{flex:1,minHeight:0}} />

      <div style={{padding:'10px 18px',borderTop:'1px solid rgba(255,255,255,0.06)',flexShrink:0,minHeight:'48px',display:'flex',alignItems:'center',justifyContent:'space-between',gap:'12px'}}>
        <div ref={readoutRef} style={{fontSize:'11px',color:'#C7D0DD',fontFamily:"'JetBrains Mono',monospace",flex:1}} />
        <button onClick={()=>setPlaying(s=>!s)} style={{background:playing?'rgba(255,209,102,0.12)':'rgba(255,255,255,0.08)',border:'1px solid rgba(255,209,102,0.35)',color:'#FFD166',borderRadius:'6px',padding:'6px 12px',fontSize:'11px',fontFamily:"'Inter',sans-serif",cursor:'pointer',flexShrink:0}}>{playing?'Pause':'Play'}</button>
      </div>
    </div>
  );
}