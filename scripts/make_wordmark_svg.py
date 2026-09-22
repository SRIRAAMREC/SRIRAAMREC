import sys, os, html
text=sys.argv[1] if len(sys.argv)>1 else 'SRIRAAM'
out=sys.argv[2] if len(sys.argv)>2 else 'assets/wordmark.svg'
W,H=490,260
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">',
   '<rect width="100%" height="100%" rx="10" fill="#0d1117"/>',
   '<rect x=".5" y=".5" width="489" height="259" rx="10" fill="none" stroke="#30363d"/>',
   '<line x1="0" y1="30" x2="490" y2="30" stroke="#30363d"/>',
   '<circle cx="20" cy="15" r="5" fill="#ff5f56"/><circle cx="36" cy="15" r="5" fill="#ffbd2e"/><circle cx="52" cy="15" r="5" fill="#27c93f"/>',
   '<text x="245" y="19" fill="#7d8590" font-size="12" text-anchor="middle">sriraam@github:~$ ./wordmark.sh</text>']
# layered extrusion
for i in range(12,0,-1):
    op=0.12+0.015*(12-i)
    p.append(f'<text x="245" y="145" text-anchor="middle" font-size="76" font-weight="700" letter-spacing="5" fill="#1f2937" opacity="{op:.2f}" transform="translate({i*1.7},{i*1.5})">{html.escape(text)}</text>')
p.append(f'<text x="245" y="145" text-anchor="middle" font-size="76" font-weight="700" letter-spacing="5" fill="#c9d1d9"><animate attributeName="opacity" from="0" to="1" dur="0.9s" fill="freeze"/>{html.escape(text)}</text>')
p.append(f'<text x="245" y="145" text-anchor="middle" font-size="76" font-weight="700" letter-spacing="5" fill="none" stroke="#58a6ff" stroke-width="1" opacity="0.45">{html.escape(text)}<animateTransform attributeName="transform" type="rotate" values="0 245 145;2 245 145;-2 245 145;0 245 145" dur="5s" repeatCount="indefinite"/></text>')
p.append('<text x="245" y="185" text-anchor="middle" fill="#7d8590" font-size="14">AI / DATA SCIENCE / FULL STACK</text>')
p.append('<text x="245" y="222" text-anchor="middle" fill="#58a6ff" font-size="13">building intelligent systems</text>')
p.append('</svg>')
os.makedirs(os.path.dirname(out),exist_ok=True); open(out,'w',encoding='utf-8').write(''.join(p)); print(out)
