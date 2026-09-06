#!/usr/bin/env python3
"""Render the markdown edition to PDF with reportlab. Single source of truth."""
import re, os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, Image, KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics

SRC = '/mnt/user-data/outputs/Transitions.md'
OUT = '/mnt/user-data/outputs/Transitions.pdf'
FIGDIR = '/mnt/user-data/outputs/figures'

INK   = colors.HexColor('#1a1a1a')
GREY  = colors.HexColor('#666666')
RULE  = colors.HexColor('#c8c8c8')
BG    = colors.HexColor('#f4f4f2')
ACC   = colors.HexColor('#7a2020')

# --- Unicode sub/superscripts must become markup: built-in fonts lack the glyphs
SUB = {'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9',
       '₊':'+','₋':'-','ₐ':'a','ₑ':'e','ₒ':'o','ₓ':'x','ₕ':'h','ₖ':'k','ₗ':'l','ₘ':'m',
       'ₙ':'n','ₚ':'p','ₛ':'s','ₜ':'t'}
SUP = {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9',
       '⁺':'+','⁻':'-','ⁿ':'n','ⁱ':'i'}
# glyphs the base-14 fonts do not have, mapped to safe equivalents
FALLBACK = {'φ̂':'phi-hat','Â':'A-hat','∏':'PROD','⟹':'=>','⟺':'<=>','≠':'!=','≤':'<=','≥':'>=',
            '∈':'in','⊆':'subset','∩':'INT','∮':'INT','∫':'INT','ℏ':'h-bar','⌊':'[','⌋':']',
            '·':'.','×':'x','−':'-','—':'--','–':'-','’':"'",'‘':"'",'“':'"','”':'"','…':'...',
            'ℛ':'R','Σ':'SUM','Λ':'Lambda','φ':'phi','λ':'lambda','μ':'mu','ρ':'rho','α':'alpha',
            'β':'beta','γ':'gamma','η':'eta','θ':'theta','ξ':'xi','π':'pi','τ':'tau','ω':'omega',
            'Ω':'Omega','Δ':'Delta','δ':'delta','ε':'eps','ℓ':'l','√':'sqrt','∞':'inf','≈':'~',
            '⊗':'(x)','†':'+','′':"'",'□':'box','∂':'d','∇':'grad','⟨':'<','⟩':'>','ℝ':'R','ℋ':'H'}

def runs(s):
    """Convert unicode sub/superscript runs into reportlab markup, then fallback-map."""
    out=[]; i=0
    while i < len(s):
        c=s[i]
        if c in SUB:
            j=i
            while j<len(s) and s[j] in SUB: j+=1
            out.append('<sub>'+''.join(SUB[k] for k in s[i:j])+'</sub>'); i=j
        elif c in SUP:
            j=i
            while j<len(s) and s[j] in SUP: j+=1
            out.append('<super>'+''.join(SUP[k] for k in s[i:j])+'</super>'); i=j
        else:
            out.append(c); i+=1
    t=''.join(out)
    for a,b in FALLBACK.items(): t=t.replace(a,b)
    return t

def esc(s):
    return s.replace('&','&amp;').replace('<','\x00LT\x00').replace('>','\x00GT\x00')

def unesc(s):
    return s.replace('\x00LT\x00','&lt;').replace('\x00GT\x00','&gt;')

def inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\x01B\x01\1\x01/B\x01', s)
    s = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'\x01I\x01\1\x01/I\x01', s)
    s = re.sub(r'`([^`]+?)`', r'\x01C\x01\1\x01/C\x01', s)
    s = re.sub(r'\[([^\]]+)\]\(#[^)]*\)', r'\1', s)
    s = runs(s)
    s = unesc(s)
    s = (s.replace('\x01B\x01','<b>').replace('\x01/B\x01','</b>')
          .replace('\x01I\x01','<i>').replace('\x01/I\x01','</i>')
          .replace('\x01C\x01','<font name="Courier" size="8.4">').replace('\x01/C\x01','</font>'))
    return s

S = {}
def mkstyles():
    S['title']=ParagraphStyle('t',fontName='Times-Bold',fontSize=25,leading=29,textColor=INK,spaceAfter=5)
    S['sub']=ParagraphStyle('s',fontName='Times-Italic',fontSize=12.5,leading=16,textColor=GREY,spaceAfter=13)
    S['h1']=ParagraphStyle('h1',fontName='Helvetica-Bold',fontSize=14.5,leading=18,textColor=INK,
                           spaceBefore=19,spaceAfter=8)
    S['h2']=ParagraphStyle('h2',fontName='Helvetica-Bold',fontSize=10.8,leading=14,textColor=ACC,
                           spaceBefore=13,spaceAfter=5)
    S['h3']=ParagraphStyle('h3',fontName='Helvetica-Bold',fontSize=9.6,leading=12.5,textColor=INK,
                           spaceBefore=9,spaceAfter=4)
    S['body']=ParagraphStyle('b',fontName='Times-Roman',fontSize=9.6,leading=13.6,textColor=INK,
                             alignment=TA_JUSTIFY,spaceAfter=6)
    S['quote']=ParagraphStyle('q',fontName='Times-Roman',fontSize=9.6,leading=14,textColor=INK,
                              leftIndent=11,rightIndent=8,spaceBefore=5,spaceAfter=7,
                              borderPadding=(6,7,6,9),backColor=BG,borderColor=RULE,borderWidth=0)
    S['bullet']=ParagraphStyle('bu',parent=S['body'],leftIndent=13,bulletIndent=4,spaceAfter=2.5,
                               alignment=TA_LEFT)
    S['cap']=ParagraphStyle('c',fontName='Times-Italic',fontSize=8.3,leading=10.6,textColor=GREY,
                            alignment=TA_CENTER,spaceBefore=3,spaceAfter=10)
    S['code']=ParagraphStyle('co',fontName='Courier',fontSize=7.6,leading=9.6,textColor=INK,
                             leftIndent=8,backColor=BG,borderPadding=(5,6,5,6),spaceBefore=4,spaceAfter=7)
    S['cell']=ParagraphStyle('ce',fontName='Times-Roman',fontSize=8.1,leading=10.2,textColor=INK)
    S['cellh']=ParagraphStyle('ch',fontName='Helvetica-Bold',fontSize=7.7,leading=10,textColor=colors.white)

def table(rows, width):
    head, body = rows[0], rows[1:]
    n=len(head)
    data=[[Paragraph(inline(c),S['cellh']) for c in head]]
    for r in body:
        r=(r+['']*n)[:n]
        data.append([Paragraph(inline(c),S['cell']) for c in r])
    # width by max content length, clamped
    raw=[max(len(str(r[i])) if i<len(r) else 0 for r in rows) for i in range(n)]
    tot=sum(raw) or 1
    cw=[max(width*0.075, width*x/tot) for x in raw]
    sc=width/sum(cw); cw=[c*sc for c in cw]
    t=Table(data,colWidths=cw,repeatRows=1)
    st=[('BACKGROUND',(0,0),(-1,0),INK),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('LEFTPADDING',(0,0),(-1,-1),4.5),('RIGHTPADDING',(0,0),(-1,-1),4.5),
        ('LINEBELOW',(0,0),(-1,-2),0.3,RULE),
        ('LINEBELOW',(0,-1),(-1,-1),0.6,INK)]
    for i in range(1,len(data)):
        if i%2==0: st.append(('BACKGROUND',(0,i),(-1,i),BG))
    t.setStyle(TableStyle(st))
    return t

def build():
    mkstyles()
    src=open(SRC).read().split('\n')
    W=A4[0]-2*20*mm
    story=[]; i=0; incaption=False
    while i < len(src):
        ln=src[i]
        st=ln.strip()
        if not st:
            i+=1; continue
        if st=='---':
            story.append(Spacer(1,4)); i+=1; continue
        # image
        m=re.match(r'!\[[^\]]*\]\((figures/([^)]+))\)', st)
        if m:
            p=os.path.join(FIGDIR,m.group(2))
            if os.path.exists(p):
                try:
                    from PIL import Image as PImage
                    iw,ih=PImage.open(p).size
                    w=min(W, W*0.92); h=w*ih/iw
                    if h>210*mm*0.55: h=210*mm*0.55; w=h*iw/ih
                    story.append(Image(p,width=w,height=h))
                except Exception: pass
            i+=1; continue
        # heading
        if st.startswith('#'):
            lev=len(st)-len(st.lstrip('#')); txt=st.lstrip('# ').strip()
            if lev==1 and not story:
                story.append(Paragraph(inline(txt),S['title'])); i+=1; continue
            sty={1:'h1',2:'h1',3:'h2',4:'h3'}.get(lev,'h3')
            if lev<=2 and story: story.append(Spacer(1,6))
            story.append(Paragraph(inline(txt),S[sty])); i+=1; continue
        # code fence
        if st.startswith('```'):
            i+=1; buf=[]
            while i<len(src) and not src[i].strip().startswith('```'):
                buf.append(src[i]); i+=1
            i+=1
            body='<br/>'.join(runs(esc(b)).replace(' ','&nbsp;') for b in buf)
            story.append(Paragraph(unesc(body),S['code'])); continue
        # blockquote
        if st.startswith('>'):
            buf=[]
            while i<len(src) and src[i].strip().startswith('>'):
                buf.append(src[i].strip().lstrip('> ').rstrip()); i+=1
            story.append(Paragraph(inline(' '.join(x for x in buf if x)),S['quote'])); continue
        # table
        if st.startswith('|'):
            rows=[]
            while i<len(src) and src[i].strip().startswith('|'):
                cells=[c.strip() for c in src[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?',c) for c in cells): rows.append(cells)
                i+=1
            if rows:
                story.append(Spacer(1,2)); story.append(table(rows,W)); story.append(Spacer(1,7))
            continue
        # bullet
        if re.match(r'^[-*] ', st):
            while i<len(src) and re.match(r'^[-*] ', src[i].strip()):
                story.append(Paragraph(inline(src[i].strip()[2:]),S['bullet'],bulletText='\u2022')); i+=1
            story.append(Spacer(1,4)); continue
        # caption (italic line beginning *Figure)
        if st.startswith('*Figure'):
            buf=[st]
            i+=1
            while i<len(src) and src[i].strip() and not src[i].strip().startswith(('#','|','>','!','```')):
                buf.append(src[i].strip()); i+=1
            story.append(Paragraph(inline(' '.join(buf).strip('*')),S['cap'])); continue
        # paragraph
        buf=[]
        while i<len(src) and src[i].strip() and not src[i].strip().startswith(('#','|','>','!','```','- ','* ','---')):
            buf.append(src[i].strip()); i+=1
        if buf:
            sty = S['sub'] if (len(story)<3) else S['body']
            story.append(Paragraph(inline(' '.join(buf)),sty))
    # document
    doc=BaseDocTemplate(OUT,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,
                        topMargin=17*mm,bottomMargin=17*mm,title='Transitions',author='Matthew Lach')
    frame=Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,id='n',
                leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    def deco(canv,d):
        canv.saveState()
        canv.setFont('Times-Roman',7.4); canv.setFillColor(GREY)
        canv.drawString(doc.leftMargin, 11*mm, 'Transitions  ·  v2.0')
        canv.drawRightString(A4[0]-doc.rightMargin, 11*mm, str(canv.getPageNumber()))
        canv.setStrokeColor(RULE); canv.setLineWidth(0.3)
        canv.line(doc.leftMargin,13.4*mm,A4[0]-doc.rightMargin,13.4*mm)
        canv.restoreState()
    doc.addPageTemplates([PageTemplate(id='n',frames=[frame],onPage=deco)])
    doc.build(story)
    return OUT

if __name__=='__main__':
    p=build()
    print('built', p, os.path.getsize(p), 'bytes')
