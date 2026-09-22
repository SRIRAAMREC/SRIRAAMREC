import json, os
cells=json.load(open('data/contributions.json',encoding='utf-8'))
cols=53; rows=7; size=15; gap=4; left=18; top=18
W=cols*(size+gap)+left*2; H=rows*(size+gap)+top*2
colors=['#161b22','#0e4429','#006d32','#26a641','#39d353']
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" rx="10" fill="#0d1117"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="10" fill="none" stroke="#30363d"/>']
for i,c in enumerate(cells[:cols*rows]):
    x=i//rows; y=i%rows; lvl=int(c.get('level',0)); xx=left+x*(size+gap); yy=top+y*(size+gap)
    svg.append(f'<rect x="{xx}" y="{yy}" width="{size}" height="{size}" rx="3" fill="{colors[max(0,min(4,lvl))]}"><animate attributeName="opacity" from="0" to="1" begin="{i*0.012:.3f}s" dur=".18s" fill="freeze"/></rect>')
svg.append('</svg>')
os.makedirs('assets',exist_ok=True)
open('assets/contrib-heatmap.svg','w',encoding='utf-8').write(''.join(svg))
print('assets/contrib-heatmap.svg')
