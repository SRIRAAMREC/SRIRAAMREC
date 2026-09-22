from PIL import Image, ImageEnhance
import html, sys, os
src = sys.argv[1]
out = sys.argv[2]
COLS, ROWS = 100, 53
CELL_W, CELL_H = 8, 15
PAD, TITLE = 20, 30
RAMP = ' .`:-=+*cs#%@'
WHITE = 0.80
im = Image.open(src).convert('L')
im = ImageEnhance.Contrast(im).enhance(1.08).resize((COLS, ROWS), Image.Resampling.LANCZOS)
px = im.load(); rows=[]
for y in range(ROWS):
    s=''
    for x in range(COLS):
        lum=(px[x,y]/255.0)**1.18
        if lum >= WHITE:
            s += ' '
        else:
            idx=int((1-lum)*(len(RAMP)-1)+0.5)
            s += RAMP[max(0,min(len(RAMP)-1,idx))]
    rows.append(s)
W=COLS*CELL_W+PAD*2; H=TITLE+ROWS*CELL_H+PAD+30
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">',
   f'<rect width="100%" height="100%" rx="10" fill="#0d1117"/>',
   f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="10" fill="none" stroke="#30363d"/>',
   f'<line x1="0" y1="{TITLE}" x2="{W}" y2="{TITLE}" stroke="#30363d"/>']
for i,c in enumerate(['#ff5f56','#ffbd2e','#27c93f']): p.append(f'<circle cx="{PAD+i*16}" cy="15" r="5" fill="{c}"/>')
p.append(f'<text x="{W/2}" y="19" fill="#7d8590" font-size="12" text-anchor="middle">sriraam@github:~$ ./portrait.sh</text>')
for ry,line in enumerate(rows):
    y=TITLE+PAD*.35+ry*CELL_H+CELL_H*.74
    rowy=TITLE+PAD*.35+ry*CELL_H
    safe=html.escape(line); delay=ry*.055
    txt=f'<text xml:space="preserve" x="{PAD}" y="{y:.1f}" fill="#c9d1d9" font-size="12.9" textLength="{COLS*CELL_W}" lengthAdjust="spacing">{safe}</text>'
    p += [f'<clipPath id="r{ry}"><rect x="{PAD}" y="{rowy:.1f}" height="{CELL_H}" width="0"><animate attributeName="width" from="0" to="{COLS*CELL_W}" begin="{delay:.3f}s" dur=".09s" fill="freeze"/></rect></clipPath>',
          f'<g clip-path="url(#r{ry})">{txt}</g>']
sy=TITLE+ROWS*CELL_H+PAD*.35
p += [f'<line x1="0" y1="{sy:.1f}" x2="{W}" y2="{sy:.1f}" stroke="#30363d"/>',
      f'<text x="{PAD}" y="{sy+19:.1f}" fill="#7d8590" font-size="13">sriraam@github:~$ whoami <tspan fill="#c9d1d9">SRIRAAM GV</tspan></text>', '</svg>']
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out,'w',encoding='utf-8').write(''.join(p))
print(out)
