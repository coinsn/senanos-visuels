from common import *
BIG='class="fr" style="font-size:110px;line-height:1.04"'
CTA=lambda a,b: f'''<div class="sc" data-s="{a}" data-e="{b}"><div class="fr" style="font-size:84px;line-height:1.1" data-a="0">Le marché de tout,<br><span class="red">près de chez vous</span></div>
<div class="pill" style="margin-top:46px;font-size:36px;padding:16px 34px" data-a=".3">📍 Partout au Sénégal · sans commission</div>
<div class="cta" style="margin-top:56px;font-size:48px;padding:32px 58px" data-a=".6" data-k="pop">Publie ton annonce</div>
<div class="fr" style="font-size:62px;margin-top:46px" data-a=".9">senanos.com</div><div style="font-size:34px;color:#888;margin-top:14px" data-a="1.1">Lien dans la bio 👆</div></div>'''
bub=lambda txt,me,a,extra='': f'''<div data-a="{a}" data-k="left" style="align-self:{'flex-end' if me else 'flex-start'};max-width:80%;background:{'#dcf8c6' if me else '#fff'};border-radius:28px;padding:22px 28px;font-size:34px;line-height:1.35;text-align:left;box-shadow:0 6px 14px rgba(0,0,0,.08);{extra}">{txt}</div>'''
# Reel C : faux SMS de transfert
sC=f'''
<div class="sc" data-s="0" data-e="3.2"><div style="font-size:150px" data-a="0" data-k="pop">📩</div><div {BIG} data-a=".2">« Je t’ai envoyé<br>l’argent <span class="red">par erreur</span> »</div></div>
<div class="sc" data-s="3" data-e="9.6"><div class="card" style="width:860px;padding:34px;background:#efeae2;display:flex;flex-direction:column;gap:22px" data-a="0">
<div style="display:flex;align-items:center;gap:18px;padding-bottom:18px;border-bottom:2px solid #ddd5ca"><div style="width:70px;height:70px;border-radius:50%;background:#ccc;display:flex;align-items:center;justify-content:center;font-size:38px">💬</div><div style="text-align:left"><div style="font-size:32px;font-weight:600">SMS · numéro inconnu</div><div style="font-size:24px;color:#888">à l’instant</div></div></div>
{bub('« Transfert reçu : <b>25 000 F</b>. Nouveau solde… »',False,.4,'border:3px solid #d7263d')}
{bub('Wa salam ! Je me suis trompé de numéro 🙏🏾 Renvoie-moi les 25 000 F stp, c’est urgent.',False,1.8)}
{bub('Euh… d’accord ?',True,3.6)}
</div></div>
<div class="sc" data-s="9.5" data-e="12.6"><div style="font-size:170px" data-a="0" data-k="pop">✋</div><div {BIG} data-a=".2">Attends !<br><span class="red">Le SMS peut<br>être faux.</span></div></div>
<div class="sc" data-s="12.5" data-e="16.6"><div class="fr" style="font-size:80px;line-height:1.1;margin-bottom:46px" data-a="0">Le bon réflexe</div>
<div class="card" style="padding:30px 40px;font-size:42px;font-weight:600;margin-bottom:20px;width:840px;text-align:left" data-a=".4" data-k="left">✅ Ouvre ton appli Wave / OM</div>
<div class="card" style="padding:30px 40px;font-size:42px;font-weight:600;margin-bottom:20px;width:840px;text-align:left" data-a="1" data-k="left">✅ Vérifie ton vrai solde</div>
<div class="card" style="padding:30px 40px;font-size:42px;font-weight:600;width:840px;text-align:left" data-a="1.6" data-k="left">❌ Ne renvoie rien sur un SMS</div></div>
{CTA(16.5,21)}'''
subsC=[[0,3.1,'Quelqu’un dit t’avoir envoyé de l’argent par erreur ?'],[3.1,9.5,'Il te presse de le lui renvoyer tout de suite'],[9.5,12.5,'Un SMS de transfert peut être un faux'],[12.5,16.5,'Vérifie toujours ton solde dans ton application'],[16.5,20,'Achète et vends en confiance sur senanos.com']]
reel('reelC-faux-sms',20,sC,subsC,seed=3,bell_from=16.5)
# Reel D : l'annonce qui ne vend pas vs celle qui vend
ann=lambda title,lines,ok,a: f'''<div class="card" data-a="{a}" data-k="pop" style="width:860px;padding:40px;text-align:left;border:4px solid {'#2e9e5b' if ok else '#d7263d'};box-shadow:0 14px 30px rgba(0,0,0,.07)">
<div style="display:flex;gap:28px;align-items:center"><div style="width:170px;height:170px;border-radius:28px;background:{'#e8edfb' if ok else '#ddd'};display:flex;align-items:center;justify-content:center;font-size:96px;{'' if ok else 'filter:blur(3px) grayscale(1)'}">📱</div>
<div class="fr" style="font-size:54px;line-height:1.1;flex:1">{title}</div></div>
<div style="margin-top:28px;font-size:36px;line-height:1.55;color:#444">{lines}</div></div>'''
sD=f'''
<div class="sc" data-s="0" data-e="3.3"><div style="font-size:150px" data-a="0" data-k="pop">🤔</div><div class="fr" style="font-size:100px;line-height:1.05" data-a=".2">Ton annonce<br>ne reçoit<br><span class="red">aucun message ?</span></div></div>
<div class="sc" data-s="3.2" data-e="8.4"><div class="pill" style="font-size:40px;margin-bottom:40px" data-a="0">❌ Avant</div>
{ann('Téléphone à vendre','Prix : à discuter<br>Photo floue, pas de ville',False,.4)}
<div class="fr" style="font-size:60px;margin-top:40px;color:#888" data-a="1.6">0 message 😶</div></div>
<div class="sc" data-s="8.3" data-e="14.4"><div class="pill" style="font-size:40px;margin-bottom:40px" data-a="0">✅ Après</div>
{ann('Marque + modèle + capacité','💵 Prix clair en FCFA<br>📍 Ville + quartier<br>📝 État honnête, accessoires<br>📸 4 à 6 photos nettes',True,.4)}
<div class="fr red" style="font-size:60px;margin-top:40px" data-a="2.2">Les acheteurs écrivent 📲</div></div>
<div class="sc" data-s="14.3" data-e="17.4"><div class="fr" style="font-size:92px;line-height:1.08" data-a="0">Même article.<br><span class="red">Meilleure annonce.</span></div><div style="font-size:44px;color:#555;margin-top:36px;line-height:1.4" data-a=".5">Et 0 commission sur ta vente.</div></div>
{CTA(17.3,22)}'''
subsD=[[0,3.2,'Ton annonce ne reçoit aucun message ?'],[3.2,8.3,'Titre vague, pas de prix, pas de ville…'],[8.3,14.3,'Titre précis, prix clair, ville, photos nettes'],[14.3,17.3,'Une meilleure annonce attire plus d’acheteurs'],[17.3,21,'Publie ton annonce sur senanos.com']]
reel('reelD-avant-apres-annonce',21,sD,subsD,seed=4,bell_from=14.3)
