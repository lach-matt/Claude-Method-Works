#!/usr/bin/env python3
# The press, draft two — matched to the shipped build's design
import os, re, sys
from PIL import Image as PILImage
import numpy as np
from fontTools.ttLib import TTFont as FTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Image, XPreformatted, KeepTogether,
                                Table, TableStyle)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth

FD='/usr/share/fonts/truetype/dejavu/'
for n,f in [('Sans','DejaVuSans.ttf'),('Sans-B','DejaVuSans-Bold.ttf'),
            ('Sans-I','DejaVuSans-Oblique.ttf'),('Sans-BI','DejaVuSans-BoldOblique.ttf'),
            ('Serif','DejaVuSerif.ttf'),('Serif-B','DejaVuSerif-Bold.ttf'),
            ('Mono','DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(n,FD+f))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='Sans-B',italic='Sans-I',boldItalic='Sans-BI')

RUST=Color(0.549,0.176,0.098); BLUE=Color(0.184,0.365,0.486)
INK=Color(0.10,0.10,0.10); GRAY=Color(0.42,0.42,0.42); BOXBG=Color(0.949,0.949,0.949)
RULE=Color(0.35,0.35,0.35)

def cmap(p): return set(FTFont(p).getBestCmap().keys())
SAN=cmap(FD+'DejaVuSans.ttf'); SER=cmap(FD+'DejaVuSerif.ttf'); MON=cmap(FD+'DejaVuSansMono.ttf')
SRC=open('BOOK-restored.md',encoding='utf-8').read()
CH=set(SRC)
bad=[c for c in CH if ord(c)>31 and ord(c) not in SAN and ord(c) not in SER]
if bad: sys.exit("GLYPH GATE: %r"%bad)
F_SANS=set(c for c in CH if ord(c)>31 and ord(c) not in SAN)   # sans -> serif fallback
F_MONO=set(c for c in CH if ord(c)>31 and ord(c) not in MON)

def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def span(t,fb=F_SANS,face='Serif'):
    out=[]
    for ch in t:
        e=esc(ch)
        out.append('<font face="%s">%s</font>'%(face,e) if ch in fb else e)
    return ''.join(out)
def prose(t):
    t=t.replace('\\|','|'); t=re.sub(r'\s+',' ',t).strip()
    t=span(t); t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    return t

PW,PH=A4
LM,RM,TM,BM=54,60,76,64
FW=PW-LM-RM

S=dict(
 body=ParagraphStyle('body',fontName='Sans',fontSize=8.9,leading=12.4,textColor=INK,
                     alignment=TA_JUSTIFY,spaceAfter=6),
 lead=ParagraphStyle('lead',fontName='Sans-B',fontSize=8.9,leading=12.4,textColor=INK,
                     alignment=TA_JUSTIFY,spaceAfter=6),
 cap=ParagraphStyle('cap',fontName='Sans',fontSize=7.8,leading=10.2,textColor=GRAY,
                    alignment=TA_LEFT,leftIndent=6,spaceBefore=4,spaceAfter=12),
 part=ParagraphStyle('part',fontName='Serif-B',fontSize=15,leading=19,textColor=RUST,
                     spaceBefore=22,spaceAfter=14),
 ch=ParagraphStyle('ch',fontName='Serif-B',fontSize=15,leading=19,textColor=RUST,
                   spaceAfter=13),
 sec=ParagraphStyle('sec',fontName='Serif-B',fontSize=13,leading=16.5,textColor=INK,
                    spaceBefore=13,spaceAfter=6),
 sub=ParagraphStyle('sub',fontName='Sans-B',fontSize=10.2,leading=13,textColor=INK,
                    spaceBefore=11,spaceAfter=5),
 boxs=ParagraphStyle('boxs',fontName='Sans',fontSize=8.7,leading=11.8,textColor=INK,
                     backColor=BOXBG,borderPadding=7,leftIndent=6,rightIndent=6,
                     spaceBefore=6,spaceAfter=9),
 toc_part=ParagraphStyle('tp',fontName='Sans-B',fontSize=10.2,leading=15,textColor=INK,spaceBefore=8),
 toc=ParagraphStyle('tc',fontName='Sans',fontSize=8.9,leading=12.6,textColor=INK),
 note_h=ParagraphStyle('nh',fontName='Serif-B',fontSize=13,leading=17,textColor=INK,spaceAfter=4),
)

# ---------------- figures ----------------
figdir='figures'
fs=sorted(f for f in os.listdir(figdir) if f.endswith('.png'))
dims={f:PILImage.open(os.path.join(figdir,f)).size for f in fs}
def ink_(f): return np.array(PILImage.open(os.path.join(figdir,f)).convert('L'),dtype=float).var()
legacy=[];i=0
while i<len(fs):
    if i+1<len(fs) and dims[fs[i]]==dims[fs[i+1]]:
        pair=[fs[i],fs[i+1]]; legacy.append(os.path.join(figdir,max(pair,key=ink_))); i+=2
    else: legacy.append(os.path.join(figdir,fs[i])); i+=1
assert len(legacy)==28
NEW={'Figure 7.2.':'fig-sections.png','Figure 7.3.':'fig-pareto-1.png',
     'Figure 7.4.':'fig-tree-1.png','Figure 7.5.':'fig-silhouette.png'}
q=list(legacy)
def img_flow(path,maxh=6.4*inch):
    w,h=PILImage.open(path).size
    dw=min(FW-14, w*72/150.0); dh=h*dw/w
    if dh>maxh: dw*=maxh/dh; dh=maxh
    return Image(path,width=dw,height=dh)

# ---------------- table builder ----------------
def try_table(lines):
    raw=[l.replace('\\|','|').rstrip() for l in lines if l.strip()]
    width=max(len(l) for l in raw)
    grid=[l.ljust(width) for l in raw]
    seps=[]; run=0
    for col in range(width):
        if all(g[col]==' ' for g in grid): run+=1
        else:
            if run>=2: seps.append((col-run,col))
            run=0
    if not seps: return None
    cuts=[0]+[b for a,b in seps]+[width]
    rows=[]
    for g in grid:
        cells=[g[cuts[i]:cuts[i+1]].strip() for i in range(len(cuts)-1)]
        rows.append(cells)
    ncols=len(rows[0])
    if ncols<2 or ncols>12: return None
    fsz=8.0 if ncols<=5 else 7.2
    hdr=ParagraphStyle('th',fontName='Sans-B',fontSize=fsz,leading=fsz+2.6,textColor=INK)
    bod=ParagraphStyle('td',fontName='Sans',fontSize=fsz,leading=fsz+2.6,textColor=INK)
    data=[]
    for ri,r in enumerate(rows):
        data.append([Paragraph(span(c),hdr if ri==0 else bod) for c in r])
    t=Table(data,colWidths=None,hAlign='LEFT')
    t.setStyle(TableStyle([
        ('LINEABOVE',(0,0),(-1,0),0.8,RULE),
        ('LINEBELOW',(0,0),(-1,0),0.4,RULE),
        ('LINEBELOW',(0,-1),(-1,-1),0.8,RULE),
        ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
        ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),6),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t

def mono_fallback(lines):
    raw=[l.replace('\\|','|').rstrip() for l in lines]
    fsz=7.2
    wmax=max(stringWidth(l,'Mono',fsz) for l in raw)
    if wmax>FW: fsz=max(4.8,fsz*FW/wmax*0.995)
    txt='\n'.join(span(l,F_MONO,'Sans') for l in raw)
    return XPreformatted(txt,ParagraphStyle('mf',fontName='Mono',fontSize=fsz,
             leading=fsz*1.32,textColor=INK,spaceBefore=4,spaceAfter=8))

def callout(lines):
    body='<br/>'.join(prose(l) for l in lines)
    return Paragraph(body,S['boxs'])

# ---------------- parse ----------------
lines=SRC.split('\n')
story=[]
# --- title page (p1): title + blue formula only
story.append(Spacer(1,3.9*inch))
story.append(Paragraph(span(lines[0].strip()),ParagraphStyle('tt',fontName='Serif-B',
             fontSize=44,leading=50,textColor=INK,alignment=TA_CENTER)))
story.append(Spacer(1,18))
story.append(Paragraph(span(lines[1].strip()),ParagraphStyle('tf',fontName='Sans',
             fontSize=15,leading=19,textColor=BLUE,alignment=TA_CENTER)))
story.append(PageBreak())
# --- p2: subtitle, author, F expression with real scripts
story.append(Spacer(1,3.15*inch))
story.append(Paragraph(span((lines[3].strip()+' '+lines[4].strip())),
             ParagraphStyle('sub2',fontName='Serif',fontSize=13.5,leading=18,
                            textColor=BLUE,alignment=TA_CENTER)))
story.append(Spacer(1,26))
story.append(Paragraph(span(lines[6].strip()),ParagraphStyle('au',fontName='Sans-B',
             fontSize=11.5,leading=15,textColor=INK,alignment=TA_CENTER)))
story.append(Paragraph(span(lines[7].strip()),ParagraphStyle('af',fontName='Sans',
             fontSize=8.5,leading=12,textColor=GRAY,alignment=TA_CENTER)))
story.append(Spacer(1,44))
Fexpr=('F = Σ<sub>n</sub> z<sub>1</sub><super>n</super> '
 'Σ<sub>ℓ≤n−1</sub> z<sub>2</sub><super>ℓ</super> '
 'Σ<sub>k≤4ℓ+2</sub> z<sub>3</sub><super>k</super> · '
 '[Σ<sub>S≤k</sub> z<sub>8</sub><super>S</super>] · '
 'Σ<sub>q≤k</sub> z<sub>4</sub><super>q</super> '
 'Σ<sub>e</sub> z<sub>5</sub><super>e</super> '
 'Σ<sub>f&lt;e</sub> z<sub>6</sub><super>f</super> '
 'Σ<sub>g≤min(q,4f+2)</sub> z<sub>7</sub><super>g</super>')
Fid=('[Σ<sub>S≤k</sub> z<sub>8</sub><super>S</super>] = '
 '(1 − z<sub>8</sub><super>k+1</super>) / (1 − z<sub>8</sub>) ··· '
 'F(1) = 976 · F(−1) = 2')
story.append(Paragraph(Fexpr,ParagraphStyle('fx',fontName='Sans',fontSize=8.2,
             leading=13,textColor=INK,alignment=TA_CENTER)))
story.append(Spacer(1,4))
story.append(Paragraph(Fid,ParagraphStyle('fi',fontName='Sans',fontSize=7.2,
             leading=11,textColor=GRAY,alignment=TA_CENTER)))
story.append(PageBreak())

body=lines[11:]
ci=next(i for i,l in enumerate(body) if l.strip()=='Contents')
ce=next(i for i,l in enumerate(body) if 'Index References' in l)

blocks=[]
def emit(seq):
    buf=[]
    def flush():
        if buf: blocks.append(('B',buf[:])); buf.clear()
    for ln in seq:
        if not ln.strip(): flush(); continue
        if ln.startswith('### '): flush(); blocks.append(('H3',ln[4:]))
        elif ln.startswith('## '): flush(); blocks.append(('H2',ln[3:]))
        elif ln.startswith('# '): flush(); blocks.append(('H1',ln[2:]))
        else: buf.append(ln)
    flush()

emit(body[:ci])
blocks.append(('TOC',[l for l in body[ci:ce+1] if l.strip()]))
emit(body[ce+1:])

TBL=re.compile(r'\S {3,}\S')
after_ch=False
for kind,payload in blocks:
    if kind=='TOC':
        left=[];right=[];cur=left
        items=[l for l in payload if l.strip()!='Contents']
        # split near midpoint at a part boundary
        half=len(items)//2
        for i,l in enumerate(items):
            if i>=half and l.startswith('# '): cur=right
            cur.append(l)
        def col(ls):
            out=[]
            for l in ls:
                t=l.lstrip('#').strip()
                sty=S['toc_part'] if l.startswith('# ') else S['toc']
                if not l.startswith('#'): sty=S['toc']
                if l.startswith('# '): sty=S['toc_part']
                elif l.startswith('## '): sty=S['toc']
                out.append(Paragraph(span(t),sty))
            return out
        story.append(Paragraph('Contents',ParagraphStyle('cth',fontName='Serif-B',
                     fontSize=13,leading=17,textColor=INK,spaceAfter=10)))
        t=Table([[col(left),col(right)]],colWidths=[FW/2-6,FW/2-6],hAlign='LEFT')
        t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('LEFTPADDING',(0,0),(-1,-1),0),
                               ('RIGHTPADDING',(0,0),(-1,-1),12)]))
        story.append(t); story.append(PageBreak())
        continue
    if kind=='H1':
        story.append(Paragraph(span(payload.strip()),S['part'])); after_ch=False; continue
    if kind=='H2':
        story.append(PageBreak())
        story.append(Paragraph(prose(payload),S['ch'])); after_ch=True; continue
    if kind=='H3':
        n=payload.split()[0]
        sty=S['sub'] if n.count('.')>=2 else S['sec']
        story.append(Paragraph(prose(payload),sty)); continue
    bl=payload
    first=bl[0].strip()
    if first.startswith('Figure '):
        key=first[:11]
        path=NEW.get(key) or (q.pop(0) if q else None)
        cap=Paragraph(prose(' '.join(bl)),S['cap'])
        story.append(KeepTogether([img_flow(path),cap]) if path else cap)
        after_ch=False; continue
    tabley=sum(1 for l in bl if TBL.search(l.strip()))>=2 and len(bl)>=2
    if tabley:
        t=try_table(bl) or mono_fallback(bl)
        story.append(t); after_ch=False; continue
    if all(l.startswith('    ') for l in bl):
        story.append(callout(bl)); after_ch=False; continue
    if TBL.search(bl[0].strip()) and len(bl)==1:
        story.append(callout(bl)); after_ch=False; continue
    sty=S['lead'] if after_ch else S['body']
    story.append(Paragraph(prose(' '.join(bl)),sty)); after_ch=False

# ---------------- doc ----------------
class BookDoc(BaseDocTemplate):
    def __init__(self,*a,**k):
        super().__init__(*a,**k); self.openers={1,2}
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='ch':
            self.openers.add(self.canv.getPageNumber())

def on_page(canv,doc):
    n=canv.getPageNumber()
    if n<=2: return
    canv.setFillColor(GRAY); canv.setFont('Sans',7)
    canv.drawString(LM, PH-31, 'The Method — The Lach Cylinder')
    if n in doc.openers:
        canv.drawCentredString(PW/2, 40, str(n))
    else:
        canv.drawRightString(PW-RM, PH-31, str(n))

out='/mnt/user-data/outputs/The_Method.pdf'
doc=BookDoc(out,pagesize=A4,leftMargin=LM,rightMargin=RM,topMargin=TM,bottomMargin=BM,
            title='The Method — The Lach Cylinder: an index of transitions',
            author='Matthew Lach',
            subject='Order theory; atomic spectroscopy; index structure',
            creator='draft two')
doc.addPageTemplates([PageTemplate(id='p',frames=[Frame(LM,BM,FW,PH-TM-BM,id='f')],onPage=on_page)])
doc.build(story)
assert not q, "legacy figures left: %d"%len(q)
print("BUILT",out,os.path.getsize(out),"bytes")
