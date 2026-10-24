from common import *
BIG='class="fr" style="font-size:110px;line-height:1.04"'
CTA=lambda a,b: f'''<div class="sc" data-s="{a}" data-e="{b}"><div class="fr" style="font-size:84px;line-height:1.1" data-a="0">Le marché de tout,<br><span class="red">près de chez vous</span></div>
<div class="pill" style="margin-top:46px;font-size:36px;padding:16px 34px" data-a=".3">📍 Partout au Sénégal · sans commission</div>
<div class="cta" style="margin-top:56px;font-size:48px;padding:32px 58px" data-a=".6" data-k="pop">Publie ton annonce</div>
<div class="fr" style="font-size:62px;margin-top:46px" data-a=".9">senanos.com</div><div style="font-size:34px;color:#888;margin-top:14px" data-a="1.1">Lien dans la bio 👆</div></div>'''
# Reel A : avance sur visite
bub=lambda txt,me,a,extra='': f'''<div data-a="{a}" data-k="left" style="align-self:{'flex-end' if me else 'flex-start'};max-width:78%;background:{'#dcf8c6' if me else '#fff'};border-radius:28px;padding:22px 28px;font-size:34px;line-height:1.35;text-align:left;box-shadow:0 6px 14px rgba(0,0,0,.08);{extra}">{txt}</div>'''
sA=f'''
<div class="sc" data-s="0" data-e="3.2"><div style="font-size:150px" data-a="0" data-k="pop">🏠</div><div {BIG} data-a=".2">Payer <span class="red">avant</span><br>de visiter ?</div></div>
<div class="sc" data-s="3" data-e="9.3"><div class="card" style="width:860px;padding:34px;background:#efeae2;display:flex;flex-direction:column;gap:22px" data-a="0">
<div style="display:flex;align-items:center;gap:18px;padding-bottom:18px;border-bottom:2px solid #ddd5ca" ><div style="width:70px;height:70px;border-radius:50%;background:#ccc;display:flex;align-items:center;justify-content:center;font-size:38px">👤</div><div style="text-align:left"><div style="font-size:32px;font-weight:600">« Propriétaire »</div><div style="font-size:24px;color:#888">en ligne</div></div></div>
{bub('Bonjour, l’appartement est toujours disponible ?',True,.4)}
{bub('Oui ! Mais beaucoup de demandes 😅',False,1.4)}
{bub('Envoie <b>10 000 F par Wave</b> pour réserver ta visite, sinon je la donne à quelqu’un d’autre.',False,2.6,'border:3px solid #d7263d')}
</div></div>
<div class="sc" data-s="9.2" data-e="12.4"><div style="font-size:170px" data-a="0" data-k="pop">✋</div><div {BIG} data-a=".2">STOP.<br><span class="red">C’est une arnaque.</span></div></div>
<div class="sc" data-s="12.3" data-e="16.4"><div class="fr" style="font-size:80px;line-height:1.1;margin-bottom:46px" data-a="0">La bonne méthode</div>
<div class="card" style="padding:30px 40px;font-size:42px;font-weight:600;margin-bottom:20px;width:820px;text-align:left" data-a=".4" data-k="left">✅ Visite d’abord</div>
<div class="card" style="padding:30px 40px;font-size:42px;font-weight:600;margin-bottom:20px;width:820px;text-align:left" data-a="1" data-k="left">✅ Rencontre le vrai propriétaire</div>
<div class="card" style="padding:30px 40px;font-size:42px;font-weight:600;width:820px;text-align:left" data-a="1.6" data-k="left">❌ Aucun paiement avant</div></div>
{CTA(16.3,21)}'''
subsA=[[0,3.1,'On te demande de payer avant la visite ?'],[3.1,9.2,'Le faux propriétaire te presse pour avoir ton argent'],[9.2,12.3,'Ne paie jamais pour réserver une visite'],[12.3,16.3,'Visite d’abord, paie seulement après'],[16.3,20,'Trouve ton logement sur senanos.com']]
reel('reelA-avance-visite',20,sA,subsA,seed=1,bell_from=16.3)
# Reel B : vide ta maison
tile=lambda em,lab,a: f'<div class="card" data-a="{a}" data-k="pop" style="width:270px;height:270px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;box-shadow:0 14px 30px rgba(0,0,0,.07)"><div style="font-size:100px">{em}</div><div style="font-size:32px;font-weight:600">{lab}</div></div>'
step=lambda n,txt,a: f'<div data-a="{a}" data-k="left" style="display:flex;align-items:center;gap:30px;margin-bottom:34px;width:840px;text-align:left"><div class="fr" style="width:110px;height:110px;border-radius:50%;background:#d7263d;color:#fff;font-size:60px;display:flex;align-items:center;justify-content:center;flex-shrink:0">{n}</div><div class="fr" style="font-size:66px">{txt}</div></div>'
sB=f'''
<div class="sc" data-s="0" data-e="3.3"><div style="font-size:150px" data-a="0" data-k="pop">💸</div><div class="fr" style="font-size:96px;line-height:1.06" data-a=".2">Ce qui dort chez toi<br>peut te <span class="red">rapporter<br>de l’argent</span></div></div>
<div class="sc" data-s="3.2" data-e="8.4"><div class="fr" style="font-size:70px;margin-bottom:50px" data-a="0">Un vieux…</div>
<div style="display:grid;grid-template-columns:repeat(3,270px);gap:26px">{tile('📱','Téléphone',.3)}{tile('🧊','Frigo',.6)}{tile('🚲','Vélo',.9)}{tile('👗','Vêtements',1.2)}{tile('🛋️','Meuble',1.5)}{tile('📺','Télé',1.8)}</div></div>
<div class="sc" data-s="8.3" data-e="13.4"><div class="fr" style="font-size:76px;margin-bottom:60px" data-a="0">Vends-le en <span class="red">3 étapes</span></div>
{step(1,'Prends une photo',.4)}{step(2,'Fixe ton prix',1.2)}{step(3,'Publie sur SenAnos',2)}</div>
<div class="sc" data-s="13.3" data-e="16.4"><div class="fr red" style="font-size:300px;line-height:1" data-a="0" data-k="pop">0 F</div><div class="fr" style="font-size:84px;margin-top:10px" data-a=".3">de commission</div><div style="font-size:44px;color:#555;margin-top:30px;line-height:1.4" data-a=".6">Tout l’argent de la vente<br>reste pour toi.</div></div>
{CTA(16.3,21)}'''
subsB=[[0,3.2,'Ce qui dort chez toi peut te rapporter de l’argent'],[3.2,8.3,'Téléphone, frigo, vélo, vêtements, meubles…'],[8.3,13.3,'Une photo, un prix, et ton annonce est en ligne'],[13.3,16.3,'Zéro commission sur ta vente'],[16.3,20,'Publie ton annonce sur senanos.com']]
reel('reelB-vide-ta-maison',20,sB,subsB,seed=2,bell_from=13.3)
