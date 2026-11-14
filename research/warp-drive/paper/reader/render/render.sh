#!/usr/bin/env bash
# render.sh -- the reader's edition: PAPER.md -> build/PAPER.html -> build/PAPER.pdf
#
#   bash render/render.sh [SOURCE.md]   render (default ../PAPER.md), then write check PNGs of the first two pages
#                                       and the last page into build/check/
#
# Pipeline: build_html.py (escape the Markdown constructs that misfire on Unicode mathematics in a temporary copy,
# pandoc's GFM reader to an HTML5 body, display blocks sized to the measure, accented Greek set in a face that attaches
# the accent, long tables allowed to break), then render.mjs (Playwright Chromium, A4, page numbers in the footer;
# fails if any element overflows the measure). Reads the source only; writes only under build/ (not committed).
set -euo pipefail
DIR=$(cd "$(dirname "$0")" && pwd)
SRC=${1:-$DIR/../PAPER.md}
OUT=$DIR/../build
mkdir -p "$OUT/check"
echo "source md5 $(md5sum "$SRC" | cut -d' ' -f1)"
python3 "$DIR/build_html.py" "$SRC" "$OUT/PAPER.html"
NODE_PATH=${NODE_PATH:-/usr/local/lib/node_modules_global} node "$DIR/render.mjs" "$OUT/PAPER.html" "$OUT/PAPER.pdf"
PAGES=$(pdfinfo "$OUT/PAPER.pdf" | awk '/^Pages:/{print $2}')
echo "pages: $PAGES"
md5sum "$OUT/PAPER.html" "$OUT/PAPER.pdf"
rm -f "$OUT"/check/p-*.png
for p in 1 2 "$PAGES"; do
  pdftoppm -r 96 -png -f "$p" -l "$p" -singlefile "$OUT/PAPER.pdf" "$OUT/check/p-$p"
done
echo "check PNGs: $(ls "$OUT"/check/ | tr '\n' ' ')"
