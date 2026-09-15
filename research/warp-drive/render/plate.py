#!/usr/bin/env python3
r"""
plate.py -- the shared scaffold every index plate in this directory is built on.

    It is NOT a plate and NOT an index.  It holds the house CSS, the small
    components the plates share, and `view3d()`, which is the part worth having
    in one place: the 3-D view's AXIS CHOICE and CAMERA are MEASURED at build
    time rather than chosen by eye, and a measurement wants one implementation.

WHAT `view3d` GUARANTEES, and states in its own caption:

  * AN ARITY-3 INDEX IS PLOTTED EXACTLY.  Three coordinates, three axes, every
    cell its own point, nothing collapsed.  The caption says so.

  * AN INDEX OF HIGHER ARITY MUST BE PROJECTED, and the projection is chosen by
    measuring all C(arity, 3) of them: how many points survive, and how many of
    those would carry more than one colour.  A point carrying two colours is a
    lie, and the count is printed whether it is zero or not.

  * THE CAMERA IS SWEPT, not picked.  The constraints are that the whole cube
    stays on canvas at EVERY azimuth the auto-spin passes through -- not just
    the opening one -- that all three axes project to at least 30 % of the
    longest, so the view is actually three-dimensional, and that no axis label
    lands inside the cloud.  Among the survivors it maximises how much of the
    canvas the points cover, less a penalty for sitting off-centre.

  * THE RUNTIME IS INLINED FROM `scatter3d.js` AT BUILD TIME.  The older plates
    each froze their own copy and three generations have since diverged; a
    plate built here cannot drift from the runtime because it does not carry a
    copy of it.  Inlining also means a published artifact needs no supporting
    file, which is why the house does it.
"""

import itertools
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------------------- the camera

def _proj(x, y, z, az, el, W, H, sc):
    ca, sa, ce, se = math.cos(az), math.sin(az), math.cos(el), math.sin(el)
    x1 = x * ca - z * sa
    z1 = x * sa + z * ca
    y2 = y * ce - z1 * se
    z2 = y * se + z1 * ce
    s = 3.4 / (3.4 + z2)
    k = min(W, H) * sc
    return (W / 2 + x1 * s * k, H / 2 - y2 * s * k)


CUBE = [(a, b, c) for a in (-1, 1) for b in (-1, 1) for c in (-1, 1)]


def camera(pts, W=870, heights=(430, 470, 510)):
    """(az, el, scale, height) swept under the constraints in the docstring.

    `pts` is the list of (x, y, z) already normalised to [-1, 1].  A large cloud
    is subsampled for the sweep -- the constraints are about the cloud's extent
    and its centre, and a deterministic stride of at most 600 points settles
    both without charting the whole set eleven thousand times.
    """
    P = pts if len(pts) <= 600 else pts[::max(1, len(pts) // 600)]
    best = None
    for H in heights:
        for si in range(19):                       # 0.34 down to 0.16
            sc = round(0.34 - 0.01 * si, 2)
            for ei in range(16):                   # 0.10 up to 0.70
                el = round(0.10 + 0.04 * ei, 2)
                if not _fits_all_az(el, W, H, sc):
                    continue
                for ai in range(105):              # the full turn
                    az = round(0.06 * ai, 2)
                    O = _proj(-1, -1, -1, az, el, W, H, sc)
                    ends = [_proj(*p, az, el, W, H, sc)
                            for p in ((1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
                    L = [math.hypot(q[0] - O[0], q[1] - O[1]) for q in ends]
                    if min(L) / max(L) < 0.30:     # must be genuinely 3-D
                        continue
                    S = [_proj(*p, az, el, W, H, sc) for p in P]
                    if _label_clash(ends, S):      # no label inside the cloud
                        continue
                    xs = [s[0] for s in S]
                    ys = [s[1] for s in S]
                    cov = ((max(xs) - min(xs)) * (max(ys) - min(ys))) / (W * H)
                    off = (abs((min(xs) + max(xs)) / 2 - W / 2) / W
                           + abs((min(ys) + max(ys)) / 2 - H / 2) / H)
                    score = cov - off + 0.35 * (min(L) / max(L))
                    if best is None or score > best[0]:
                        best = (score, az, el, sc, H)
    if best is None:                       # nothing satisfied every constraint
        print("    camera: NO angle satisfied every constraint; house default")
        return (0.62, 0.26, 0.235, heights[len(heights) // 2])
    return best[1:]


def _fits_all_az(el, W, H, sc):
    for i in range(70):
        az = 0.09 * i
        for p in CUBE:
            u, v = _proj(*p, az, el, W, H, sc)
            if u < 10 or u > W - 10 or v < 10 or v > H - 10:
                return False
    return True


def _label_clash(ends, S):
    """True if an axis label would be drawn over the cloud.

    THE THRESHOLD SCALES WITH THE CLOUD.  A dense scatter can tolerate a few
    points behind a label; a seventeen-point index cannot, because one dot over
    the text is the whole overlap there is.  A fixed count let exactly that
    through on the first three plates built here.
    """
    # The runtime now paints each axis label on its own panel-coloured ground,
    # so a label is legible at every azimuth and this constraint only has to
    # keep the still frame tidy rather than carry legibility on its own.
    near = max(1, len(S) // 40)
    for q in ends:
        n = 0
        for s in S:
            if abs(s[0] - q[0]) < 52 and abs(s[1] - q[1]) < 22:
                n += 1
                if n > near:
                    return True
    return False


# ------------------------------------------------------- the axis choice

def axis_choice(cells, colour_i):
    """(triple, points, impure, table) over every C(arity, 3) projection.

    `colour_i` is the coordinate the points would be coloured by. A projection
    is IMPURE at a point where two cells share the projected position and
    disagree on that coordinate -- which would paint one point two colours.
    """
    cells = sorted(cells)
    ar = len(cells[0])
    if ar == 3:
        return (0, 1, 2), len(cells), 0, []
    rows = []
    for tri in itertools.combinations(range(ar), 3):
        seen = {}
        imp = 0
        for c in cells:
            k = tuple(c[i] for i in tri)
            v = c[colour_i]
            if k in seen and seen[k] != v:
                imp += 1
            seen.setdefault(k, v)
        rows.append((len(seen), imp, tri))
    rows.sort(key=lambda r: (-r[0], r[1]))
    pure = [r for r in rows if r[1] == 0]
    pick = pure[0] if pure else rows[0]
    return pick[2], pick[0], pick[1], rows


# -------------------------------------------------------------- the section

def view3d(pid, points, labels, colour_tokens, caption, sub, snum, title,
           key=None, height=None, radius=3.6, aria=None):
    """One complete 3-D section.

    `points` is [(x, y, z, colour token, hollow, label)]; `labels` the three
    axis names; `colour_tokens` the legend as [(token, what it means)].
    """
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]

    def nrm(v, lo, hi):
        return 0.0 if hi == lo else (v - lo) / (hi - lo) * 2 - 1
    N = [(nrm(p[0], min(xs), max(xs)), nrm(p[1], min(ys), max(ys)),
          nrm(p[2], min(zs), max(zs))) for p in points]
    az, el, sc, H = camera(N, heights=(height,) if height else (430, 470, 510))

    toks = sorted({p[3] for p in points})
    ti = {t: i for i, t in enumerate(toks)}
    # THE LABEL IS PACKED, because view3d took one in its point tuple and then
    # dropped it -- a caption on the master plate promised labelled dots and
    # the view had none.
    labelled = any(len(p) > 5 and p[5] for p in points)
    packed = ",".join(
        "[%s,%s,%s,%d,%d%s]" % (_n(p[0]), _n(p[1]), _n(p[2]), ti[p[3]],
                                1 if p[4] else 0,
                                "," + json.dumps(p[5]) if labelled else "")
        for p in points)
    runtime = open(os.path.join(HERE, "scatter3d.js"), encoding="utf-8").read()
    js = """%s
(function(){
const T=%s;
const RAW=[%s];
const PTS=RAW.map(a=>({x:a[0],y:a[1],z:a[2],c:T[a[3]],hollow:a[4]||0,n:a[5]}));
scatter3d({id:'%s',points:PTS,xlab:%s,ylab:%s,zlab:%s,
  az:%s,el:%s,scale:%s,height:%d,r:%s,%s
  xcol:'--geometry',ycol:'--order',zcol:'--information',
  colour:p=>p.c});
})();""" % (runtime, json.dumps(toks), packed, pid,
            json.dumps(labels[0]), json.dumps(labels[1]), json.dumps(labels[2]),
            az, el, sc, H, radius, "labels:true," if labelled else "")

    legend = "".join(
        '<span><i style="background:var(%s)"></i>%s</span>' % (t, w)
        for t, w in colour_tokens)
    if key:
        legend += key
    return '''<section>
  <div class="shead"><span class="snum">%s</span><h2>%s</h2></div>
  <p class="sub">%s</p>
  <figure class="plate">
    <div class="v3d"><canvas id="%s" aria-label="%s"></canvas></div>
    <div class="v3dbar">
      <button id="%s-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="v3dkey">%s</span>
    </div>
    <figcaption>%s</figcaption>
  </figure>
  <script>%s</script>
</section>

''' % (snum, title, sub, pid, aria or title, pid, legend, caption, js)


def _n(v):
    if isinstance(v, float):
        s = "%.6g" % v
        return s
    return str(v)


def exactness(cells, tri, pts, impure, rows):
    """The sentence the caption must carry about what the view collapses."""
    ar = len(sorted(cells)[0])
    if ar == 3:
        return ("<b>This view is the index itself, not a projection of it.</b> "
                "The chart has three coordinates and they are the three axes, "
                "so every one of the %d cells is its own point and nothing is "
                "collapsed, summarised or dropped." % len(cells))
    best = rows[0] if rows else None
    return ("<b>This view is a projection, and what it costs is measured.</b> "
            "The chart has %d coordinates; all %d three-coordinate projections "
            "were charted and this one keeps <b>%d of %d cells</b> as distinct "
            "points, a %.0f%% collapse, with <b>%d</b> carrying more than one "
            "colour.%s" % (ar, len(rows), pts, len(cells),
                           100 * (1 - pts / len(cells)), impure,
                           "" if not best or best[2] == tri else
                           " The widest projection keeps %d but %d of those "
                           "would be mixed, so it was not used."
                           % (best[0], best[1])))


# ------------------------------------------------------------------- the head

CSS = r"""<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;0,600;0,800;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{
  --ground:#F4F6F8; --panel:#FFFFFF; --sunk:#EDF0F4;
  --ink:#12161C; --body:#2C3440; --muted:#66717F; --faint:#98A2AF;
  --rule:#D9DFE7; --rule-hard:#B6C0CC; --accent:#1B4B78;
  --order:#7A3E9D; --algebra:#B03A64; --geometry:#137A69;
  --information:#B86A12; --statistics:#2456A0;
  --bound:#B86A12; --free:#137A69; --undet:#7C8796;
  --hue7:#8A6D3B; --hue8:#4A5A8C; --hue9:#9C4A6E;
  --shadow:0 1px 2px rgba(18,22,28,.05),0 8px 24px -12px rgba(18,22,28,.16);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0D1117; --panel:#141A22; --sunk:#1B222C;
    --ink:#EEF2F7; --body:#C3CCD8; --muted:#8994A3; --faint:#5F6A79;
    --rule:#262F3B; --rule-hard:#394453; --accent:#7FB2E5;
    --order:#C08FE0; --algebra:#E88AA8; --geometry:#4CC6AF;
    --information:#E0A557; --statistics:#79A9EE;
    --bound:#E0A557; --free:#4CC6AF; --undet:#7C8796;
    --hue7:#CBA96B; --hue8:#8FA3D9; --hue9:#E08AAE;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 28px -14px rgba(0,0,0,.8);
  }
}
:root[data-theme="dark"]{
  --ground:#0D1117; --panel:#141A22; --sunk:#1B222C;
  --ink:#EEF2F7; --body:#C3CCD8; --muted:#8994A3; --faint:#5F6A79;
  --rule:#262F3B; --rule-hard:#394453; --accent:#7FB2E5;
  --order:#C08FE0; --algebra:#E88AA8; --geometry:#4CC6AF;
  --information:#E0A557; --statistics:#79A9EE;
  --bound:#E0A557; --free:#4CC6AF; --undet:#7C8796;
  --hue7:#CBA96B; --hue8:#8FA3D9; --hue9:#E08AAE;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 28px -14px rgba(0,0,0,.8);
}
*{box-sizing:border-box}
body{background:var(--ground);color:var(--body);
  font-family:Spectral,Georgia,serif;font-size:17px;line-height:1.62;
  padding-block:0;padding-left:20px;padding-right:20px;-webkit-font-smoothing:antialiased}
.wrap{max-width:920px;margin:0 auto;padding-block:56px 96px}
h1,h2,h3{color:var(--ink);text-wrap:balance;margin:0}
h1{font-size:clamp(2.05rem,5.4vw,3rem);font-weight:800;line-height:1.08;letter-spacing:-.022em}
h2{font-size:clamp(1.28rem,3vw,1.6rem);font-weight:600;line-height:1.2;letter-spacing:-.012em}
h3{font-size:1.06rem;font-weight:600;margin:34px 0 12px;letter-spacing:-.006em}
p{margin:0 0 1.05em}
p.after{margin-top:18px}
.mono{font-family:'IBM Plex Mono',ui-monospace,monospace;font-variant-numeric:tabular-nums}
.sm{font-size:.82em}
.eqn{font-size:1.16rem;color:var(--ink);background:var(--sunk);border:1px solid var(--rule);
  border-radius:3px;padding:15px 18px;letter-spacing:.02em;margin:0 0 22px;overflow-x:auto}
.hot{color:var(--algebra)}
.mast{border-bottom:2px solid var(--ink);padding-bottom:26px}
.eyebrow{font-family:'IBM Plex Mono',monospace;font-size:.7rem;font-weight:600;
  letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin:0 0 16px}
.dek{font-size:1.15rem;color:var(--muted);margin:16px 0 0;max-width:62ch;font-style:italic}
.stamp{display:flex;flex-wrap:wrap;gap:0 30px;margin-top:22px;
  font-family:'IBM Plex Mono',monospace;font-size:.74rem;color:var(--faint);letter-spacing:.04em}
.stamp b{color:var(--body);font-weight:500}
section{margin-top:60px}
.shead{display:flex;align-items:baseline;gap:14px;margin-bottom:6px}
.snum{font-family:'IBM Plex Mono',monospace;font-size:.78rem;font-weight:600;
  color:var(--accent);letter-spacing:.1em;flex:none;padding-top:.28em}
.sub{color:var(--muted);font-size:.97rem;margin:0 0 26px;max-width:66ch}
.tablewrap{overflow-x:auto;border:1px solid var(--rule);border-radius:3px;background:var(--panel);box-shadow:var(--shadow)}
.tablewrap.tall{max-height:560px;overflow-y:auto}
.tablewrap.tall thead th{position:sticky;top:0;background:var(--panel);z-index:1}
table{border-collapse:collapse;width:100%;min-width:620px}
caption{caption-side:bottom;text-align:left;padding:12px 16px;font-size:.83rem;color:var(--muted);border-top:1px solid var(--rule)}
th,td{padding:9px 14px;text-align:left;border-bottom:1px solid var(--rule)}
thead th{font-family:'IBM Plex Mono',monospace;font-size:.66rem;font-weight:600;
  letter-spacing:.13em;text-transform:uppercase;color:var(--muted);
  border-bottom:1px solid var(--rule-hard);white-space:nowrap}
tbody tr:last-child td{border-bottom:none}
td.name{font-weight:600;color:var(--ink);white-space:nowrap}
td.num,td.cell{font-family:'IBM Plex Mono',monospace;font-variant-numeric:tabular-nums;white-space:nowrap}
td.num{text-align:right}
th.num{text-align:right}
td.cell{color:var(--ink)}
td.mono{font-family:'IBM Plex Mono',monospace;font-variant-numeric:tabular-nums}
.chip{display:inline-block;font-family:'IBM Plex Mono',monospace;font-size:.68rem;
  font-weight:600;letter-spacing:.05em;padding:1px 7px;border-radius:2px;border:1px solid currentColor;line-height:1.5}
.chip.b0{color:var(--free)} .chip.b1{color:var(--bound)} .chip.b2{color:var(--undet)}
.yes{color:var(--geometry);font-weight:600} .no{color:var(--muted);font-weight:600}
figure{margin:0}
.plate{background:var(--panel);border:1px solid var(--rule);border-radius:3px;
  padding:26px 22px 18px;box-shadow:var(--shadow)}
figcaption{font-size:.85rem;color:var(--muted);margin-top:16px;padding-top:14px;border-top:1px solid var(--rule)}
figcaption b{color:var(--ink);font-weight:600}
svg{display:block;max-width:100%;height:auto;margin:0 auto}
svg text{font-family:'IBM Plex Mono',monospace}
rect.b0{fill:var(--free)} rect.b1{fill:var(--bound)} rect.b2{fill:var(--undet)}
.key{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:14px;
  font-family:'IBM Plex Mono',monospace;font-size:.72rem;color:var(--muted)}
.key span{display:flex;align-items:center;gap:7px}
.key i.k{width:11px;height:11px;border-radius:2px;display:block;flex:none}
.key i.b0{background:var(--free)} .key i.b1{background:var(--bound)} .key i.b2{background:var(--undet)}
svg text.tb0{fill:var(--free)} svg text.tb1{fill:var(--bound)} svg text.tb2{fill:var(--undet)}
.note{border-left:3px solid var(--accent);background:var(--sunk);
  padding:16px 20px;margin:26px 0;border-radius:0 3px 3px 0}
.note p:last-child{margin-bottom:0}
.note .lab{font-family:'IBM Plex Mono',monospace;font-size:.66rem;font-weight:600;
  letter-spacing:.14em;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:7px}
.note.warn{border-left-color:var(--algebra)} .note.warn .lab{color:var(--algebra)}
.note.good{border-left-color:var(--geometry)} .note.good .lab{color:var(--geometry)}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
  gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:3px;overflow:hidden}
.kv>div{background:var(--panel);padding:14px 16px}
.kv dt{font-family:'IBM Plex Mono',monospace;font-size:.63rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--muted);margin:0 0 6px}
.kv dd{margin:0;font-family:'IBM Plex Mono',monospace;font-size:1.2rem;font-weight:500;color:var(--ink);line-height:1.15}
.kv dd.hot{color:var(--algebra)}
.kv dd small{display:block;font-size:.68rem;font-weight:400;color:var(--faint);margin-top:5px;letter-spacing:.04em;line-height:1.4}
ul.tight{margin:0 0 1.05em;padding-left:1.15em}
ul.tight li{margin-bottom:.7em}
ul.refuse li b{color:var(--ink)}
.foot{margin-top:72px;padding-top:22px;border-top:1px solid var(--rule);font-size:.83rem;color:var(--faint)}
.foot code{font-family:'IBM Plex Mono',monospace;color:var(--muted);font-size:.95em}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.duo{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
@media(max-width:720px){.trio,.duo{grid-template-columns:1fr}}
.per{border:1px solid var(--rule);border-radius:3px;background:var(--panel);padding:17px 18px;box-shadow:var(--shadow)}
.per .who{font-family:'IBM Plex Mono',monospace;font-size:.66rem;letter-spacing:.13em;
  text-transform:uppercase;color:var(--muted);margin-bottom:9px}
.per .what{font-size:1.12rem;color:var(--ink);font-weight:600;margin-bottom:4px;line-height:1.25}
.per .co{font-family:'IBM Plex Mono',monospace;font-size:.86rem;color:var(--accent);margin-bottom:10px}
.per .obj{font-size:.88rem;color:var(--muted);line-height:1.45}
.v3d{position:relative}
.v3d canvas{display:block;width:100%;border-radius:2px;background:transparent}
.v3dbar{display:flex;flex-wrap:wrap;align-items:center;gap:8px 16px;margin-top:12px;
  font-family:'IBM Plex Mono',monospace;font-size:.72rem;color:var(--muted)}
.v3dbar button{font:inherit;color:var(--accent);background:var(--sunk);
  border:1px solid var(--rule);border-radius:2px;padding:3px 10px;cursor:pointer}
.v3dbar button:hover{border-color:var(--accent)}
.v3dbar button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.v3dbar .hint{color:var(--faint)}
.v3dbar .dims{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.v3dbar .dims button{padding:3px 8px;min-width:30px}
.v3dbar .dims button.on{background:var(--accent);color:var(--panel);border-color:var(--accent)}
.v3dbar .now{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.v3dkey{display:flex;flex-wrap:wrap;gap:6px 14px}
.v3dkey span{display:flex;align-items:center;gap:6px}
.v3dkey i{width:10px;height:10px;border-radius:50%;display:block;flex:none}
@media (prefers-reduced-motion: reduce){.v3d canvas{}}
</style>"""


def head(title):
    """The <title> plus the house stylesheet. ONE copy, shared by every plate."""
    return "<title>%s</title>\n%s" % (title, CSS)
