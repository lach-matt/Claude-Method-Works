# mkref.py — build the press reference document.
# usage: python3 mkref.py "<running header title>" [out.docx]
#
# W-013's recipe, codified. It was performed BY HAND every session that pressed, and doing it by hand
# is how the page numbers stayed missing: the recipe's verification rubric names fonts, page size,
# margins and ONE sz at 21, and says nothing about a header or a footer, so nothing ever failed for
# their absence. The reportlab-era press printed BOTH a folio and a running header ("The Method —
# The Lach Cylinder", register 651's sampler kept mistaking them for lost text). They were lost at the
# migration to pandoc + LibreOffice. This restores them.
#
# W-013(i)   <w:sectPr /> SERIALISES WITH A SPACE. Match by ELEMENT NAME, never by one literal.
# W-013(ii)  docDefaults already carries w:sz/w:szCs — REPLACE, do not insert.
# W-013(iii) docDefaults' fonts are THEME attributes. Convert them document-wide, or the reference
#            is not Georgia at the default. The sz replacement is SCOPED TO docDefaults; scoping the
#            FONT pass there too converts only 3 of 36 and the rubric catches it.
import re,sys,zipfile,subprocess,os

TITLE=sys.argv[1] if len(sys.argv)>1 else 'The Method 1.6'
OUT=sys.argv[2] if len(sys.argv)>2 else 'ref.docx'
NS=('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

FOOTER=('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:ftr %s>'
        '<w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/>'
        '<w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr></w:pPr>'
        '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
        '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
        '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
        '<w:r><w:rPr><w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/><w:sz w:val="18"/></w:rPr>'
        '<w:t>1</w:t></w:r>'
        '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')%NS

HEADER=('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:hdr %s>'
        '<w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/>'
        '<w:i/><w:sz w:val="17"/><w:szCs w:val="17"/></w:rPr></w:pPr>'
        '<w:r><w:rPr><w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/><w:i/><w:sz w:val="17"/>'
        '<w:szCs w:val="17"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p></w:hdr>')%(NS,esc(TITLE))

BLANK=('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:%s %s><w:p/></w:%s>')

base='/tmp/_refbase.docx'
subprocess.run('pandoc --print-default-data-file reference.docx > %s'%base,shell=True,check=True)
zin=zipfile.ZipFile(base); names=zin.namelist(); data={n:zin.read(n) for n in names}; zin.close()

# ---- styles.xml -------------------------------------------------------------
st=data['word/styles.xml'].decode('utf-8')
conv=lambda m:'w:%s="Georgia"'%m.group(1)
st,nt=re.subn(r'w:(ascii|hAnsi|eastAsia|cs)Theme="[^"]*"',conv,st)
st,npl=re.subn(r'w:(ascii|hAnsi|eastAsia|cs)="[^"]*"',conv,st)
m=re.search(r'<w:docDefaults>.*?</w:docDefaults>',st,re.S); dd0=m.group(0)
dd=re.sub(r'<w:sz w:val="\d+"\s*/>','<w:sz w:val="21" />',dd0)
dd=re.sub(r'<w:szCs w:val="\d+"\s*/>','<w:szCs w:val="21" />',dd)
st=st.replace(dd0,dd,1)
st=st.replace('</w:styles>',
  '<w:style w:type="paragraph" w:customStyle="1" w:styleId="EntryBody">'
  '<w:name w:val="Entry Body" /><w:basedOn w:val="BodyText" /><w:qFormat />'
  '<w:rPr><w:i /><w:iCs /></w:rPr></w:style></w:styles>',1)
data['word/styles.xml']=st.encode('utf-8')

# ---- new parts --------------------------------------------------------------
data['word/footer1.xml']=FOOTER.encode('utf-8')
data['word/header1.xml']=HEADER.encode('utf-8')
data['word/footer2.xml']=(BLANK%('ftr',NS,'ftr')).encode('utf-8')   # title page: no folio
data['word/header2.xml']=(BLANK%('hdr',NS,'hdr')).encode('utf-8')
names=list(names)+['word/footer1.xml','word/header1.xml','word/footer2.xml','word/header2.xml']

ct=data['[Content_Types].xml'].decode('utf-8')
adds=''.join('<Override PartName="/word/%s.xml" ContentType="application/vnd.openxmlformats-'
             'officedocument.wordprocessingml.%s+xml"/>'%(p,p[:-1]) for p in
             ('footer1','header1','footer2','header2'))
data['[Content_Types].xml']=ct.replace('</Types>',adds+'</Types>',1).encode('utf-8')

rels=data['word/_rels/document.xml.rels'].decode('utf-8')
B='http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
radd=''.join('<Relationship Id="%s" Type="%s%s" Target="%s.xml"/>'%(rid,B,typ,tgt) for rid,typ,tgt in
             (('rIdFtr1','footer','footer1'),('rIdHdr1','header','header1'),
              ('rIdFtr2','footer','footer2'),('rIdHdr2','header','header2')))
data['word/_rels/document.xml.rels']=rels.replace('</Relationships>',radd+'</Relationships>',1).encode('utf-8')

# ---- document.xml sectPr: match BY ELEMENT NAME (W-013 i) --------------------
doc=data['word/document.xml'].decode('utf-8')
mm=re.search(r'<w:sectPr\b[^>]*/>',doc)
if not mm: mm=re.search(r'<w:sectPr\b.*?</w:sectPr>',doc,re.S)
sect=('<w:sectPr>'
      '<w:headerReference w:type="default" r:id="rIdHdr1"/>'
      '<w:footerReference w:type="default" r:id="rIdFtr1"/>'
      '<w:headerReference w:type="first" r:id="rIdHdr2"/>'
      '<w:footerReference w:type="first" r:id="rIdFtr2"/>'
      '<w:pgSz w:w="12240" w:h="15840" />'
      '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
      'w:header="720" w:footer="720" w:gutter="0" />'
      '<w:titlePg/></w:sectPr>')
data['word/document.xml']=(doc[:mm.start()]+sect+doc[mm.end():]).encode('utf-8')

zo=zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED)
for n in names: zo.writestr(n,data[n])
zo.close()

# ---- VERIFY. The rubric now names the folio and the running header. ---------
z=zipfile.ZipFile(OUT); st=z.read('word/styles.xml').decode(); doc=z.read('word/document.xml').decode()
fonts=re.findall(r'w:(?:ascii|hAnsi|eastAsia|cs)="([^"]*)"',st)
dd=re.search(r'<w:docDefaults>.*?</w:docDefaults>',st,re.S).group(0)
checks=[('zip clean',z.testzip() is None),
        ('0 theme attrs',len(re.findall(r'Theme="',st))==0),
        ('0 non-Georgia fonts',len([f for f in fonts if f!='Georgia'])==0),
        ('ONE sz at 21',len(re.findall(r'<w:sz w:val="21"',st))==1 and '21' in dd),
        ('EntryBody','EntryBody' in st),
        ('pgSz 12240x15840','w:w="12240" w:h="15840"' in doc),
        ('four 1440 margins',len(re.findall(r'w:(?:top|right|bottom|left)="1440"',doc))==4),
        ('FOOTER referenced','rIdFtr1' in doc),
        ('HEADER referenced','rIdHdr1' in doc),
        ('PAGE field present','PAGE' in z.read('word/footer1.xml').decode()),
        ('title in header',esc(TITLE) in z.read('word/header1.xml').decode()),
        ('titlePg set','<w:titlePg/>' in doc)]
print('theme converted %d · plain converted %d · %d bytes'%(nt,npl,os.path.getsize(OUT)))
bad=[n for n,ok in checks if not ok]
for n,ok in checks: print(('  OK   ' if ok else '  FAIL ')+n)
sys.exit(1 if bad else 0)
