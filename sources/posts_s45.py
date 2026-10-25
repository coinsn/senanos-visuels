from posts_lib import *
T=7
# ---- Carrousel : fixer le bon prix
c3=[frame(f'''<div class="pill" style="align-self:flex-start">💰 Astuces vendeurs</div>
<div class="fr" style="font-size:100px;line-height:1.04;margin-top:36px">Comment fixer<br>le <span class="red">bon prix</span><br>pour vendre vite ?</div>
<div style="font-size:36px;color:#555;margin-top:34px;line-height:1.4">Trop cher, personne n’écrit. Trop bas, tu perds de l’argent. Voici la méthode 👇</div>''',1,T),
tip(2,T,'🔎','Regarde les annonces similaires','Cherche le même article sur SenAnos : même modèle, même état, même ville. C’est ton point de départ.','Le marché te donne le vrai prix.'),
tip(3,T,'🧾','Sois honnête sur l’état','Neuf, comme neuf, bon état, avec défauts : chaque niveau change le prix. Rayures et pannes se paient.','Un prix juste évite les disputes au rendez-vous.'),
tip(4,T,'🤝','Garde une marge pour négocier','Au Sénégal, on discute toujours le prix. Annonce un peu au-dessus de ton minimum.','Fixe ton prix plancher avant de publier.'),
tip(5,T,'📦','Valorise les extras','Boîte, chargeur, facture, garantie, accessoires : mentionne-les, ils justifient ton prix.','Écris-les dès la 1re ligne de la description.'),
tip(6,T,'⏱️','Pas de messages ? Ajuste','Si personne ne te contacte après quelques jours, baisse un peu le prix ou améliore tes photos.','Mets ton annonce à jour plutôt que d’attendre.'),
frame(f'''<div class="fr" style="font-size:96px;line-height:1.05">Ton prix<br>est fixé ?<br><span class="red">Publie ton<br>annonce.</span></div>
<div style="font-size:38px;color:#555;margin-top:36px;line-height:1.4">0 commission : tout l’argent de la vente reste pour toi.<br>📌 Enregistre ce post pour ta prochaine vente.</div>
<div style="margin-top:50px;display:flex;align-items:center;gap:30px"><span class="cta">senanos.com</span><span style="font-size:30px;color:#888">Lien dans la bio</span></div>''',7,T,swipe=False)]
shoot_pages(c3,W,H,'c3')
# ---- Carrousel : écrire une annonce qui attire
c4=[frame(f'''<div class="pill" style="align-self:flex-start">✍️ Astuces vendeurs</div>
<div class="fr" style="font-size:100px;line-height:1.04;margin-top:36px">5 règles pour<br>écrire une annonce<br><span class="red">qui attire</span></div>
<div style="font-size:36px;color:#555;margin-top:34px;line-height:1.4">Les acheteurs décident en quelques secondes. Rends-leur la vie facile.</div>''',1,T),
tip(2,T,'🏷️','Un titre précis','Pas « Téléphone à vendre », mais la marque, le modèle, la capacité et l’état. C’est ce que les gens cherchent.','Le titre = ce que l’acheteur tape dans la recherche.'),
tip(3,T,'💵','Un prix clair','Écris le prix en FCFA. « Prix à discuter » tout seul fait fuir beaucoup d’acheteurs.','Un vrai chiffre, puis « négociable » si tu veux.'),
tip(4,T,'📍','Ta ville et ton quartier','Dakar, Rufisque, Guédiawaye, Saint-Louis… L’acheteur veut savoir si c’est près de chez lui.','Plus c’est précis, plus on te contacte.'),
tip(5,T,'📝','Une description honnête','État, ancienneté, défauts, accessoires inclus, raison de la vente : réponds aux questions d’avance.','Moins de questions, plus de rendez-vous.'),
tip(6,T,'⚡','Réponds vite','Un acheteur qui attend va voir une autre annonce. Garde ton téléphone à portée de main.','Répondre vite, c’est déjà vendre.'),
frame(f'''<div class="fr" style="font-size:96px;line-height:1.05">Ton annonce<br>est prête ?<br><span class="red">Publie-la<br>maintenant.</span></div>
<div style="font-size:38px;color:#555;margin-top:36px;line-height:1.4">Sans commission, partout au Sénégal.<br>📤 Envoie à quelqu’un qui veut vendre.</div>
<div style="margin-top:50px;display:flex;align-items:center;gap:30px"><span class="cta">senanos.com</span><span style="font-size:30px;color:#888">Lien dans la bio</span></div>''',7,T,swipe=False)]
shoot_pages(c4,W,H,'c4')
# ---- Visuel marque : tu es de quelle ville ?
cities=[('🌊','Dakar'),('🏘️','Rufisque'),('🏙️','Guédiawaye'),('🌉','Saint-Louis'),('🕌','Tivaouane'),('🚉','Thiès'),('📍','Pikine'),('🌴','Ziguinchor'),('➕','Ta ville ?')]
tiles=''.join(f'<div class="card" style="height:190px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;box-shadow:0 10px 24px rgba(0,0,0,.05){";border:3px dashed #d7263d" if c=="Ta ville ?" else ""}"><div style="font-size:64px">{e}</div><div style="font-size:32px;font-weight:600">{c}</div></div>' for e,c in cities)
v2=[f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;inset:0;padding:60px 70px 56px;display:flex;flex-direction:column">
<div>{BRAND}</div>
<div class="pill" style="align-self:flex-start;margin-top:34px">📍 Le marché de tout, près de chez vous</div>
<div class="fr" style="font-size:86px;line-height:1.04;margin-top:22px">Et toi, tu vends<br><span class="red">depuis quelle ville ?</span></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:36px">{tiles}</div>
<div style="font-size:32px;color:#555;margin-top:30px">💬 Dis-le en commentaire · 📤 Envoie à quelqu’un de ta ville</div>
<div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between"><span class="cta" style="font-size:34px;padding:22px 40px">Publie ton annonce</span><span class="fr" style="font-size:40px">senanos.com</span></div></div>''']
shoot_pages(v2,W,H,'v2')
