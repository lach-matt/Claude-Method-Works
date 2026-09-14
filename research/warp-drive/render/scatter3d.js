/* A small 3-D scatter on a 2-D canvas. No library: the artifact CSP admits
   cdnjs, but a hand-rolled projector is ~120 lines and cannot fail to load. */
function scatter3d(opts){
  const cv = document.getElementById(opts.id);
  if(!cv) return;
  const wrap = cv.parentElement;
  const css = getComputedStyle(document.documentElement);
  const tok = n => css.getPropertyValue(n).trim() || '#888';
  let az = opts.az ?? 0.62, el = opts.el ?? 0.26;
  let spin = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let drag = null;

  const pts = opts.points;
  const rng = a => { const v = pts.map(p=>p[a]); return [Math.min(...v), Math.max(...v)]; };
  const rx = opts.rx || rng('x'), ry = opts.ry || rng('y'), rz = opts.rz || rng('z');
  const nrm = (v,r) => r[1]===r[0] ? 0 : (v - r[0])/(r[1]-r[0])*2 - 1;

  function project(x,y,z,W,H){
    const ca=Math.cos(az), sa=Math.sin(az), ce=Math.cos(el), se=Math.sin(el);
    const x1 =  x*ca - z*sa;
    const z1 =  x*sa + z*ca;
    const y2 =  y*ce - z1*se;
    const z2 =  y*se + z1*ce;
    const d = 3.4, s = d/(d + z2);
    const k = Math.min(W,H) * 0.255;
    return [W/2 + x1*s*k, H/2 - y2*s*k, z2, s];
  }

  function axis(ctx,W,H,a,b,label,colour){
    const p = project(...a,W,H), q = project(...b,W,H);
    ctx.strokeStyle = tok('--rule-hard'); ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(p[0],p[1]); ctx.lineTo(q[0],q[1]); ctx.stroke();
    ctx.fillStyle = colour; ctx.font = '600 11px "IBM Plex Mono", monospace';
    ctx.textAlign='center'; ctx.textBaseline='middle';
    const dx = q[0]-p[0], dy = q[1]-p[1], L = Math.hypot(dx,dy)||1;
    const lx = Math.max(16, Math.min(W-16, q[0]+dx/L*20));
    const ly = Math.max(12, Math.min(H-10, q[1]+dy/L*16));
    ctx.fillText(label, lx, ly);
  }

  function draw(){
    const W = wrap.clientWidth, H = opts.height || 420;
    const dpr = Math.min(window.devicePixelRatio||1, 2);
    if(cv.width !== W*dpr || cv.height !== H*dpr){
      cv.width = W*dpr; cv.height = H*dpr;
      cv.style.width = W+'px'; cv.style.height = H+'px';
    }
    const ctx = cv.getContext('2d');
    ctx.setTransform(dpr,0,0,dpr,0,0);
    ctx.clearRect(0,0,W,H);

    // the box, drawn faintly so the rotation is legible
    ctx.strokeStyle = tok('--rule'); ctx.lineWidth = 1;
    const C = [];
    for(const sx of [-1,1]) for(const sy of [-1,1]) for(const sz of [-1,1])
      C.push([sx,sy,sz]);
    const E = [[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,6],[3,7],[4,5],[4,6],[5,7],[6,7]];
    ctx.globalAlpha = .5;
    for(const [i,j] of E){
      const p = project(...C[i],W,H), q = project(...C[j],W,H);
      ctx.beginPath(); ctx.moveTo(p[0],p[1]); ctx.lineTo(q[0],q[1]); ctx.stroke();
    }
    ctx.globalAlpha = 1;

    axis(ctx,W,H,[-1,-1,-1],[1,-1,-1], opts.xlab, tok(opts.xcol||'--muted'));
    axis(ctx,W,H,[-1,-1,-1],[-1,1,-1], opts.ylab, tok(opts.ycol||'--muted'));
    axis(ctx,W,H,[-1,-1,-1],[-1,-1,1], opts.zlab, tok(opts.zcol||'--muted'));

    const S = pts.map(p => {
      const [sx,sy,sz,sc] = project(nrm(p.x,rx), nrm(p.y,ry), nrm(p.z,rz), W, H);
      return {p, sx, sy, sz, sc};
    }).sort((a,b) => b.sz - a.sz);

    // points first, labels second: a near point must never paint over a
    // label already placed for a farther one.
    for(const o of S){
      const r = (opts.r || 4) * o.sc;
      ctx.beginPath(); ctx.arc(o.sx, o.sy, r, 0, 6.2832);
      ctx.fillStyle = tok(opts.colour(o.p));
      ctx.globalAlpha = .35 + .65*o.sc*0.9;
      ctx.fill();
      if(opts.stroke){ ctx.globalAlpha=1; ctx.strokeStyle = tok('--panel');
        ctx.lineWidth = 1; ctx.stroke(); }
      ctx.globalAlpha = 1;
    }
    if(opts.labels){
      const placed = [];
      ctx.font = '10px "IBM Plex Mono", monospace';
      ctx.textAlign='left'; ctx.textBaseline='middle';
      for(const o of S.slice().reverse()){
        if(!o.p.n) continue;
        const r = (opts.r || 4) * o.sc;
        const w = ctx.measureText(o.p.n).width, lx = o.sx + r + 6;
        let ly = o.sy;
        for(let t=0; t<14; t++){
          const clash = placed.some(q => Math.abs(q.y-ly) < 13 &&
                                         lx < q.x+q.w+8 && q.x < lx+w+8);
          if(!clash) break;
          ly = o.sy + (t%2 ? 1 : -1) * 13 * Math.ceil((t+1)/2);
        }
        placed.push({x:lx, y:ly, w});
        if(Math.abs(ly-o.sy) > 2){
          ctx.strokeStyle = tok('--rule-hard'); ctx.lineWidth = .8;
          ctx.beginPath(); ctx.moveTo(o.sx + r + 1, o.sy);
          ctx.lineTo(lx - 2, ly); ctx.stroke();
        }
        ctx.fillStyle = tok('--body');
        ctx.fillText(o.p.n, lx, ly);
      }
    }
  }

  let raf = null;
  function loop(){
    if(spin && !drag){ az += 0.0032; draw(); }
    raf = requestAnimationFrame(loop);
  }

  cv.addEventListener('pointerdown', e => {
    drag = {x:e.clientX, y:e.clientY, az, el};
    cv.setPointerCapture(e.pointerId); cv.style.cursor='grabbing';
  });
  cv.addEventListener('pointermove', e => {
    if(!drag) return;
    az = drag.az + (e.clientX - drag.x)*0.0075;
    el = Math.max(-1.35, Math.min(1.35, drag.el + (e.clientY - drag.y)*0.0075));
    draw();
  });
  const stop = e => { if(drag){ drag=null; cv.style.cursor='grab'; } };
  cv.addEventListener('pointerup', stop);
  cv.addEventListener('pointercancel', stop);
  cv.style.cursor = 'grab';
  cv.style.touchAction = 'none';

  const btn = document.getElementById(opts.id + '-spin');
  if(btn){
    const sync = () => btn.textContent = spin ? 'pause rotation' : 'resume rotation';
    sync();
    btn.addEventListener('click', () => { spin = !spin; sync(); draw(); });
  }

  new ResizeObserver(draw).observe(wrap);
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', draw);
  draw();
  loop();
}
