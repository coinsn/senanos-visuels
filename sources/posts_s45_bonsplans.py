from posts_lib import *
# ---- Visuel : bons plans (annonces réelles relevées sur senanos.com le 01/11/2026)
items=[('🛵','Honda Lead, très bon état','Occasion','250 000','Guédiawaye','#fdeee6'),('📱','iPhone 13 Pro 128 Go','Neuf','230 000','Dakar','#e8edfb'),
('🏠','Appartement à louer','','150 000','Rufisque · Keur Ndiaye Lo','#eef6ea'),('🚲','Vélo VTT 26 pouces','Occasion','75 000','Saint-Louis','#e6f2f5'),
('🧴','Crème épilatoire','Neuf','2 000','Tivaouane','#f3eefb'),('💋','Masque lèvres collagène','Neuf','1 500','Tivaouane','#fbe9f1')]
cards=''.join(f'''<div class="card" style="display:flex;align-items:center;gap:24px;padding:15px 24px;border-radius:26px;box-shadow:0 10px 24px rgba(0,0,0,.05)">
<div style="width:80px;height:80px;border-radius:22px;background:{bg};display:flex;align-items:center;justify-content:center;font-size:44px;flex-shrink:0">{em}</div>
<div style="flex:1;min-width:0"><div style="font-size:31px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{t}</div><div style="font-size:24px;color:#888;margin-top:2px">📍 {v}{' · ' if st else ''}{st}</div></div>
<div class="fr red" style="font-size:36px;letter-spacing:-.5px;white-space:nowrap">{p} <sup style="font-size:19px">F</sup></div></div>''' for em,t,st,p,v,bg in items)
v=[f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;inset:0;padding:60px 70px 56px;display:flex;flex-direction:column">
<div>{BRAND}</div>
<div class="pill" style="align-self:flex-start;margin-top:26px">🔥 En ce moment sur SenAnos</div>
<div class="fr" style="font-size:72px;line-height:1.04;margin-top:18px">Les bons plans<br><span class="red">près de chez toi</span></div>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:28px">{cards}</div>
<div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between"><span class="cta" style="font-size:34px;padding:22px 40px">Voir sur senanos.com</span><span style="font-size:26px;color:#888">Lien dans la bio</span></div></div>''']
shoot_pages(v,W,H,'bp')
