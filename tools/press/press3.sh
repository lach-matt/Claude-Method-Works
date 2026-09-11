#!/bin/sh
# Reading copy: build.py's preparation (press2.py names every anchor it must decline),
# pandoc to HTML on the book template, WeasyPrint to a paged PDF with real page numbers.
set -e
cd /home/claude/build
SRC="$1"; OUT="$2"; TITLE="$3"; DEPTH="${4:-2}"; EXTRA="$5"; STRIP="$6"   # EXTRA reaches the title page as $imprint (it was captured and dropped before)
python3 press2.py "$SRC" "$OUT" "$TITLE" "$DEPTH" $STRIP > "$OUT.press.log" 2>&1
grep -E 'press anchors|DECLINED' "$OUT.press.log" | head -8
cp tmp.md "$OUT.prepared.md"
pandoc "$OUT.prepared.md" -o "$OUT.html" --standalone --embed-resources \
  --from markdown+pipe_tables+smart --toc --toc-depth "$DEPTH" \
  --resource-path /home/claude/build --template book.html \
  --metadata title="$TITLE" --metadata imprint="$EXTRA" 2>&1 | tail -2
python3 -c "
import weasyprint, sys
weasyprint.HTML(filename='$OUT.html', base_url='/home/claude/build/').write_pdf('$OUT.pdf')
" 2>&1 | grep -vi 'warn' | tail -3
python3 -c "
import re; d=open('$OUT.pdf','rb').read()
print('  $OUT.pdf  %.1f MB  %d pages' % (len(d)/1048576, len(re.findall(rb'/Type\s*/Page\b(?!s)', d))))"
