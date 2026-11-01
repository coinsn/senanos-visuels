from posts_lib import *
T=7
END=lambda a,b,c: frame(f'''<div class="fr" style="font-size:96px;line-height:1.05">{a}</div>
<div style="font-size:38px;color:#555;margin-top:36px;line-height:1.4">{b}</div>
<div style="margin-top:50px;display:flex;align-items:center;gap:30px"><span class="cta">Publie ton annonce</span><span class="fr" style="font-size:40px">senanos.com</span></div>
<div style="font-size:30px;color:#888;margin-top:22px">{c}</div>''',7,T,swipe=False)
# ---- Carrousel : que vendre pour la fin d'année
c5=[frame(f'''<div class="pill" style="align-self:flex-start">🎉 Spécial fin d’année</div>
<div class="fr" style="font-size:100px;line-height:1.04;margin-top:36px">Que vendre<br>avant les <span class="red">fêtes</span><br>de fin d’année ?</div>
<div style="font-size:36px;color:#555;margin-top:34px;line-height:1.4">Décembre approche : cadeaux, réveillons, vacances… Voici 5 idées de choses à vendre maintenant 👇</div>''',1,T),
tip(2,T,'📱','Téléphones et tablettes','En fin d’année, beaucoup cherchent un cadeau ou changent de téléphone. Ton ancien modèle peut servir à quelqu’un.','Vends-le avant les fêtes, pas après.'),
tip(3,T,'👗','Tenues et chaussures de fête','Robes, boubous, costumes, chaussures portés une ou deux fois : les fêtes et cérémonies arrivent.','Photo de face, en entier, à la lumière du jour.'),
tip(4,T,'🍳','Électroménager de cuisine','Four, mixeur, friteuse, réchaud… Les grands repas de fin d’année donnent envie de s’équiper.','Indique s’il fonctionne et depuis quand tu l’as.'),
tip(5,T,'🎮','Consoles, jeux et jouets','Les vacances scolaires de décembre arrivent : jeux, vélos et jouets en bon état intéressent les parents.','Mentionne les manettes et accessoires inclus.'),
tip(6,T,'🛋️','Déco et meubles','Nouvelle année, nouvelle maison : fais de la place et laisse un autre foyer en profiter.','Donne les dimensions dans la description.'),
END('Tu as trouvé<br>quoi vendre ?<br><span class="red">Publie ton<br>annonce.</span>','0 commission : tout l’argent de la vente reste pour toi.','📌 Enregistre ce post · Lien dans la bio')]
shoot_pages(c5,W,H,'c5')
# ---- Carrousel : acheter un téléphone d'occasion, 5 vérifications
c6=[frame(f'''<div class="pill" style="align-self:flex-start">🛡️ Acheter en confiance</div>
<div class="fr" style="font-size:96px;line-height:1.04;margin-top:36px">Téléphone<br>d’occasion :<br><span class="red">5 vérifications</span><br>avant de payer</div>
<div style="font-size:36px;color:#555;margin-top:34px;line-height:1.4">Au rendez-vous, prends 5 minutes. Elles peuvent t’éviter une mauvaise surprise 👇</div>''',1,T),
tip(2,T,'📲','L’écran et le tactile','Allume-le, regarde s’il y a des taches ou des lignes, touche tout l’écran, même les coins.','Fais glisser une icône d’un bord à l’autre.'),
tip(3,T,'🔋','La batterie et la charge','Branche-le avec un chargeur : il doit charger normalement. Demande l’état de la batterie si le téléphone l’affiche.','Pas de charge testée = pas de paiement.'),
tip(4,T,'📞','Appels, réseau et caméra','Mets ta puce, passe un appel, envoie un message, prends une photo avec chaque caméra.','Teste aussi le haut-parleur et le micro.'),
tip(5,T,'🔓','Le compte est déconnecté','Le compte iCloud ou Google du vendeur doit être retiré, sinon le téléphone peut rester bloqué.','Demande une réinitialisation devant toi.'),
tip(6,T,'🔢','Le bon numéro IMEI','Compose *#06# : le numéro affiché doit être le même que celui de la boîte ou de la facture.','Puis seulement, tu paies.'),
END('Tu vends<br>ton téléphone ?<br><span class="red">Publie ton<br>annonce.</span>','Prépare ces 5 points : les acheteurs te feront confiance.','📤 Envoie à quelqu’un qui veut acheter un téléphone')]
shoot_pages(c6,W,H,'c6')
# ---- Visuel marque : 0 commission
rows=[('💰','Tu fixes ton prix','C’est toi qui décides combien tu demandes.'),('🤝','Tu discutes avec l’acheteur','Entre particuliers, près de chez toi.'),('🧾','0 commission sur ta vente','Ce que l’acheteur paie, tu le gardes.')]
cards=''.join(f'<div class="card" style="display:flex;gap:28px;align-items:center;padding:30px 36px;box-shadow:0 10px 24px rgba(0,0,0,.05)"><div style="width:110px;height:110px;flex:none;border-radius:30px;background:#fdecee;display:flex;align-items:center;justify-content:center;font-size:60px">{e}</div><div><div class="fr" style="font-size:46px;line-height:1.1">{t}</div><div style="font-size:30px;color:#666;margin-top:8px">{d}</div></div></div>' for e,t,d in rows)
v3=[f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;inset:0;padding:60px 70px 56px;display:flex;flex-direction:column">
<div>{BRAND}</div>
<div class="pill" style="align-self:flex-start;margin-top:40px">🇸🇳 Jënd ak jaay, sans commission</div>
<div class="fr" style="font-size:92px;line-height:1.04;margin-top:26px">Ce que tu vends,<br><span class="red">tu le gardes.</span></div>
<div style="display:flex;flex-direction:column;gap:22px;margin-top:44px">{cards}</div>
<div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between"><span class="cta" style="font-size:34px;padding:22px 40px">Publie ton annonce</span><span class="fr" style="font-size:40px">senanos.com</span></div></div>''']
shoot_pages(v3,W,H,'v3')
