from posts_lib import *
T=7
c7=[frame(f'''<div class="pill" style="align-self:flex-start">🏠 Propriétaires & bailleurs</div>
<div class="fr" style="font-size:94px;line-height:1.04;margin-top:36px">Un logement<br>à louer ?<br><span class="red">5 règles pour une<br>annonce qui rassure</span></div>
<div style="font-size:36px;color:#555;margin-top:34px;line-height:1.4">Les locataires se méfient des arnaques. Rassure-les dès la première lecture 👇</div>''',1,T),
tip(2,T,'🏷️','Un titre précis','Type de logement, nombre de pièces, quartier : « Appartement 3 pièces, Keur Massar » plutôt que « Appart à louer ».','Le locataire sait tout de suite si ça lui correspond.'),
tip(3,T,'💵','Loyer et conditions clairs','Écris le loyer mensuel en FCFA, la caution et l’avance demandées. Pas de surprise au moment de signer.','Un chiffre clair attire des contacts sérieux.'),
tip(4,T,'📸','Une photo par pièce','Salon, chambres, cuisine, toilettes, façade, de jour et rangés. Une annonce sans photo inquiète.','4 à 8 photos nettes, à la lumière du jour.'),
tip(5,T,'🔌','Les détails qui comptent','Eau, électricité et compteur, étage, accès à la route, quartier calme ou animé : dis-le d’avance.','Moins de questions, plus de visites.'),
tip(6,T,'🚪','Propose la visite d’abord','Ne demande aucun argent avant la visite. C’est ce que les locataires attendent d’un propriétaire sérieux.','La visite, c’est ton meilleur argument.'),
frame(f'''<div class="fr" style="font-size:96px;line-height:1.05">Ton logement<br>est prêt ?<br><span class="red">Publie ton<br>annonce.</span></div>
<div style="font-size:38px;color:#555;margin-top:36px;line-height:1.4">Sans commission, partout au Sénégal.</div>
<div style="margin-top:50px;display:flex;align-items:center;gap:30px"><span class="cta">Publie ton annonce</span><span class="fr" style="font-size:40px">senanos.com</span></div>
<div style="font-size:30px;color:#888;margin-top:22px">📤 Envoie à un propriétaire que tu connais</div>''',7,T,swipe=False)]
shoot_pages(c7,W,H,'c7')
opt=lambda e,t,d,bg: f'<div class="card" style="flex:1;padding:44px 30px;display:flex;flex-direction:column;align-items:center;text-align:center;box-shadow:0 10px 24px rgba(0,0,0,.05)"><div style="width:150px;height:150px;border-radius:40px;background:{bg};display:flex;align-items:center;justify-content:center;font-size:84px">{e}</div><div class="fr" style="font-size:62px;margin-top:26px">{t}</div><div style="font-size:30px;color:#666;margin-top:14px;line-height:1.4">{d}</div></div>'
v4=[f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;inset:0;padding:60px 70px 56px;display:flex;flex-direction:column">
<div>{BRAND}</div>
<div class="pill" style="align-self:flex-start;margin-top:40px">💬 À toi de choisir</div>
<div class="fr" style="font-size:86px;line-height:1.04;margin-top:24px">Ton prochain<br>téléphone :<br><span class="red">neuf ou occasion ?</span></div>
<div style="display:flex;gap:26px;margin-top:44px">{opt('✨','Neuf','Sous emballage,<br>prix plus élevé','#e8edfb')}<div class="fr" style="align-self:center;font-size:44px;color:#999">ou</div>{opt('♻️','Occasion','Bien vérifié,<br>prix plus doux','#eef6ea')}</div>
<div style="font-size:34px;color:#555;margin-top:36px;text-align:center">Réponds en commentaire : <b>NEUF</b> ou <b>OCCASION</b> 👇</div>
<div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between"><span class="cta" style="font-size:34px;padding:22px 40px">Publie ton annonce</span><span class="fr" style="font-size:40px">senanos.com</span></div></div>''']
shoot_pages(v4,W,H,'v4')
