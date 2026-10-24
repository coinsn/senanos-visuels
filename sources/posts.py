from common import *
W,H=1080,1350
def frame(inner,num=None,total=None,swipe=True):
    n=f'<div style="position:absolute;top:70px;right:70px;font-size:26px;color:#999;font-weight:500">{num}/{total}</div>' if num else ''
    sw='<div style="position:absolute;bottom:64px;right:70px;font-size:26px;color:#999;font-weight:500">Glisse →</div>' if swipe else ''
    return f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;top:60px;left:70px">{BRAND}</div>{n}
<div style="position:absolute;left:70px;right:70px;top:190px;bottom:140px;display:flex;flex-direction:column;justify-content:center">{inner}</div>{sw}'''
def tip(k,total,emoji,title,body,good):
    return frame(f'''<div style="display:flex;align-items:center;gap:26px"><div style="width:120px;height:120px;border-radius:32px;background:#fdecee;display:flex;align-items:center;justify-content:center;font-size:66px">{emoji}</div>
<div class="fr red" style="font-size:120px;line-height:1">{k-1}</div></div>
<div class="fr" style="font-size:78px;line-height:1.08;margin-top:40px">{title}</div>
<div style="font-size:36px;line-height:1.45;color:#555;margin-top:30px">{body}</div>
<div class="card" style="margin-top:44px;padding:28px 32px;display:flex;gap:20px;align-items:flex-start;font-size:32px;line-height:1.4"><span style="font-size:38px">✅</span><span><b>{good}</b></span></div>''',k,total)
# ---- Carrousel 1 : anti-arnaque
T=7
c1=[frame(f'''<div class="pill" style="align-self:flex-start">🛡️ Spécial sécurité</div>
<div class="fr" style="font-size:104px;line-height:1.03;margin-top:36px">5 arnaques<br>à éviter quand<br>tu achètes<br><span class="red">en ligne</span></div>
<div style="font-size:36px;color:#555;margin-top:34px;line-height:1.4">Au Sénégal, elles font encore beaucoup de victimes. Enregistre ce post 📌</div>''',1,T),
tip(2,T,'💸','Payer avant de voir','On te demande un Wave ou un Orange Money avant de voir le produit ? C’est le piège n°1.','Paie seulement à la remise, après avoir vérifié l’article.'),
tip(3,T,'🏠','L’avance sur visite','« Envoie 10 000 F pour réserver la visite » : un propriétaire sérieux ne demande jamais d’argent avant une visite.','Visite d’abord. Aucun paiement avant.'),
tip(4,T,'🤑','Le prix trop beau','Un iPhone neuf à moitié prix, une voiture bradée… Si c’est trop beau, c’est souvent faux.','Compare avec les autres annonces avant de te décider.'),
tip(5,T,'📩','Le faux SMS de transfert','« Je t’ai envoyé l’argent par erreur, renvoie-le moi. » Le SMS peut être faux.','Vérifie toujours ton solde dans ton application, jamais sur un SMS.'),
tip(6,T,'📍','Le rendez-vous isolé','Un lieu désert, tard le soir, seul : ne prends pas de risque, même pour une bonne affaire.','Rencontre en lieu public, en journée, accompagné si possible.'),
frame(f'''<div class="fr" style="font-size:92px;line-height:1.05">Sur SenAnos :<br><span class="red">rencontre,<br>vérifie, paie<br>à la remise.</span></div>
<div style="font-size:38px;color:#555;margin-top:36px;line-height:1.4">📤 Envoie ce post à quelqu’un que tu veux protéger.</div>
<div style="margin-top:50px;display:flex;align-items:center;gap:30px"><span class="cta">senanos.com</span><span style="font-size:30px;color:#888">Lien dans la bio</span></div>''',7,T,swipe=False)]
shoot_pages(c1,W,H,'c1')
# ---- Carrousel 2 : 5 photos qui font vendre
c2=[frame(f'''<div class="pill" style="align-self:flex-start">📸 Astuces vendeurs</div>
<div class="fr" style="font-size:100px;line-height:1.04;margin-top:36px">5 astuces photo<br>pour <span class="red">vendre<br>plus vite</span></div>
<div style="font-size:36px;color:#555;margin-top:34px;line-height:1.4">Une bonne photo, c’est plus de messages d’acheteurs. Tout se fait avec ton téléphone.</div>''',1,T),
tip(2,T,'☀️','La lumière du jour','Photographie près d’une fenêtre ou dehors, en journée. Évite le flash qui écrase les couleurs.','Une photo claire inspire confiance.'),
tip(3,T,'🧺','Un fond simple','Un mur uni, un drap, une table propre : l’acheteur doit voir ton article, pas le désordre autour.','Range 30 secondes avant de photographier.'),
tip(4,T,'🔄','Plusieurs angles','Face, dos, côtés, détails : 4 à 6 photos répondent aux questions avant même qu’on te les pose.','Plus de photos = moins d’hésitation.'),
tip(5,T,'🔍','Montre l’état réel','Rayures, usure, boîte, facture : montre tout. L’honnêteté évite les mauvaises surprises au rendez-vous.','Un acheteur rassuré conclut plus vite.'),
tip(6,T,'🛋️','Une photo en situation','Le meuble dans la pièce, la tenue portée, le téléphone allumé : l’acheteur s’imagine déjà avec.','Termine par cette photo-là.'),
frame(f'''<div class="fr" style="font-size:96px;line-height:1.05">Tes photos<br>sont prêtes ?<br><span class="red">Publie ton<br>annonce.</span></div>
<div style="font-size:38px;color:#555;margin-top:36px;line-height:1.4">Sans commission, partout au Sénégal.<br>📤 Envoie à quelqu’un qui a quelque chose à vendre.</div>
<div style="margin-top:50px;display:flex;align-items:center;gap:30px"><span class="cta">senanos.com</span><span style="font-size:30px;color:#888">Lien dans la bio</span></div>''',7,T,swipe=False)]
shoot_pages(c2,W,H,'c2')
# ---- Visuel : bons plans de la semaine
items=[('🧊','Réfrigérateur Samsung','Occasion','150 000','Dakar','#e6f2f5'),('📱','iPhone 13 authentique','Neuf','175 000','Dakar','#e8edfb'),
('🔦','Caméra d’inspection (endoscope)','Neuf','30 000','Dakar · Patte d’oie','#fdeee6'),('📐','Cours particuliers de maths','','5 000','Dakar','#eef6ea'),
('💇🏾‍♀️','Accessoires de cheveux','Neuf','2 200','Guédiawaye','#fbe9f1'),('🧴','Gommage de visage','Neuf','1 500','Tivaouane','#f3eefb')]
cards=''.join(f'''<div class="card" style="display:flex;align-items:center;gap:22px;padding:16px 22px;border-radius:26px;box-shadow:0 10px 24px rgba(0,0,0,.05)">
<div style="width:72px;height:72px;border-radius:20px;background:{bg};display:flex;align-items:center;justify-content:center;font-size:40px;flex-shrink:0">{em}</div>
<div style="flex:1;min-width:0"><div style="font-size:27px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{t}</div><div style="font-size:21px;color:#888;margin-top:2px">{v}{' · ' if st else ''}{st}</div></div>
<div class="fr red" style="font-size:31px;letter-spacing:-.5px;white-space:nowrap">{p} <sup style="font-size:17px">F</sup></div></div>''' for em,t,st,p,v,bg in items)
v=[f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;inset:0;padding:60px 70px 56px;display:flex;flex-direction:column">
<div>{BRAND}</div>
<div class="pill" style="align-self:flex-start;margin-top:34px">🔥 Sélection de la semaine</div>
<div class="fr" style="font-size:80px;line-height:1.04;margin-top:22px">Les bons plans<br><span class="red">de la semaine</span></div>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:30px">{cards}</div>
<div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between"><span class="cta" style="font-size:34px;padding:22px 40px">Voir sur senanos.com</span><span style="font-size:26px;color:#888">Lien dans la bio</span></div></div>''']
shoot_pages(v,W,H,'v1')
