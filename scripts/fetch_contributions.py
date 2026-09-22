import os, json, re
from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup

user=os.environ.get('GH_PROFILE_USER','SRIRAAMREC')
url=f'https://github.com/users/{user}/contributions'
r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=30)
r.raise_for_status()
soup=BeautifulSoup(r.text,'html.parser')
rows=[]
for rect in soup.select('rect[data-date]'):
    rows.append({'date':rect.get('data-date'),'level':int(rect.get('data-level','0'))})
if not rows:
    raise RuntimeError('GitHub did not return contribution cells. Try again in a minute.')
os.makedirs('data',exist_ok=True)
with open('data/contributions.json','w',encoding='utf-8') as f: json.dump(rows,f,indent=2)
print(f'Saved {len(rows)} contribution cells for {user}.')
