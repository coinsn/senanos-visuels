import sys, os, json; sys.path.insert(0,'/home/claude/senanos-visuels/sources')
import reels_s46 as R
from common import reel
from PIL import Image, ImageOps
SRC='/home/claude/senanos-visuels/annonces/'; TMP='/home/claude/work/ann/'
def prep(ident,n):
    out=f'{TMP}{ident}-{n}.jpg'
    im=ImageOps.exif_transpose(Image.open(f'{SRC}{ident}/{n}.jpg')).convert('RGB'); im.thumbnail((1800,1800)); im.save(out,quality=90)
    return out, im.size[0]/im.size[1]
def ph(path,h,a,fit='cover',pos='center'):
    return f'''<div data-a="{a}" data-k="pop" style="width:900px;height:{h}px;border-radius:44px;border:10px solid #fff;box-shadow:0 18px 40px rgba(0,0,0,.14);background:#fff url('file://{path}') {pos}/{fit} no-repeat"></div>'''
def make(L,seed):
    P=[prep(L['id'],n) for n in L['photos']]
    while len(P)<3: P.append(P[len(P)%len(L['photos'])])
    fit=L.get('fit','cover'); hh=lambda r: 680 if r>1.15 else 860
    top='justify-content:flex-start;padding-top:250px'
    s=f'''
<div class="sc" data-s="0" data-e="3.6" style="{top}"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:34px" data-a="0">👀 Annonce à la une</div>
{ph(P[0][0],hh(P[0][1]),.1,fit,L.get('pos1','center'))}
<div class="fr" style="font-size:{L.get('fs',88)}px;line-height:1.06;margin-top:44px" data-a=".4">{L['t1']}<br><span class="red">{L['t2']}</span></div></div>
<div class="sc" data-s="3.5" data-e="7.1" style="{top}"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:34px" data-a="0">{L['pill']}</div>
{ph(P[1][0],hh(P[1][1]),.1,fit,L.get('pos2','center'))}
<div class="fr red" style="font-size:{L.get('pfs',104)}px;line-height:1;margin-top:40px" data-a=".4" data-k="pop">{L['prix']}</div></div>
<div class="sc" data-s="7.0" data-e="10.6" style="{top}">
{ph(P[2][0],680,0,fit,L.get('pos3','center'))}
<div class="card" style="width:900px;padding:36px 40px;margin-top:36px;text-align:left" data-a=".3"><div style="font-size:42px;font-weight:600;line-height:1.25">{L['titre']}</div><div class="fr red" style="font-size:64px;margin-top:8px">{L['prix']}</div><div style="font-size:36px;color:#666;margin-top:10px">📍 {L['lieu']}</div></div>
<div style="font-size:42px;color:#555;margin-top:34px" data-a=".7">À voir sur senanos.com</div></div>
<div class="sc" data-s="10.5" data-e="13.1"><div style="font-size:150px" data-a="0" data-k="pop">📣</div><div class="fr" style="font-size:92px;line-height:1.08" data-a=".2">Et ton annonce ?<br><span class="red">Elle peut passer ici.</span></div><div style="font-size:42px;color:#555;margin-top:30px" data-a=".6">0 commission sur ta vente</div></div>
{R.CTA(13.0,17)}'''
    subs=[[0,3.5,L['s1']],[3.5,7,'Annonce publiée sur SenAnos'],[7,10.5,L['s3']],[10.5,13,'Publie ton annonce pour plus de visibilité'],[13,16.5,'Publie ton annonce sur senanos.com']]
    name='ann-'+L['slug']
    reel(name,17,s,subs,seed=seed,bell_from=10.5)
    ims=[Image.open(f'fr_{name}/f{i:04d}.jpg').resize((270,480)) for i in (75,180,285)]
    sh=Image.new('RGB',(280*3,480),'white'); [sh.paste(im,(k*280,0)) for k,im in enumerate(ims)]; sh.save(f'{name}-chk.jpg')
LS=[
dict(id='cmusqg0wt000101t6n6y865yk',slug='iphone-13',photos=[2,4,3],t1='iPhone 13 simple',t2='Authentique',pill='📱 Téléphones · Neuf',prix='175 000 FCFA',titre='iPhone 13 simple Authentique',lieu='Dakar',s1='Un iPhone 13 à vendre à Dakar',s3='Envoie ça à quelqu’un qui cherche un iPhone'),
dict(id='cmu6321ap000101nv7hqs5vc3',slug='endoscope',photos=[1],fit='contain',t1='Endoscope',t2='caméra d’inspection',pill='📷 Caméras · Neuf',prix='30 000 FCFA',titre='Endoscope Caméra d’inspection avec ecran 2.4 pouces HD',lieu='Dakar (Patte d’oie)',s1='Une caméra d’inspection à vendre à Dakar',s3='Envoie ça à un mécanicien ou un plombier'),
dict(id='cmu649ian000c01nvuko7rjzp',slug='appartement-rufisque',photos=[1],t1='Appartement',t2='à louer',pill='🏠 À louer · Rufisque',prix='150 000 FCFA',titre='Appartement à louer',lieu='Rufisque (Keur Ndiaye Lo)',s1='Un logement à louer à Rufisque',s3='Envoie ça à quelqu’un qui cherche un logement'),
dict(id='cmv8r3te9000u01mue8yqcnal',slug='creme-epilatoire',photos=[1],fit='contain',t1='Crème',t2='épilatoire',pill='💄 Beauté · Neuf',prix='2 000 FCFA',titre='Crème epilatoire',lieu='Tivaouane (PAM)',s1='Un produit beauté à vendre à Tivaouane',s3='Envoie ça à quelqu’un que ça intéresse'),
dict(id='cmwc9ijg4002n01mu7y90m7ks',slug='terrain-mboro',photos=[1,4,6],t1='Terrain de 8256 m²',t2='vers Touba Ndiaye',fs=80,pill='🌳 Terrains · Mboro',prix='6 500 000 FCFA',pfs=92,titre='Terrain de 8256 m² vers Touba Ndiaye - Mboro - Thiès',lieu='Mboro (Touba Ndiaye)',s1='Un terrain à vendre vers Mboro',s3='Envoie ça à quelqu’un qui cherche un terrain'),
dict(id='cmwgbqjxf004501murhzt9oru',slug='verger-manguiers',photos=[3,1,4],t1='Verger avec manguiers',t2='de 1,91 hectare',fs=78,pill='🥭 Vergers · Thiès',prix='9 850 000 FCFA',pfs=92,titre='Verger avec manguiers de 1,91 hectare vers Tassette - Thiès',lieu='Thiès (Tassette)',s1='Un verger de manguiers à vendre vers Thiès',s3='Envoie ça à quelqu’un qui veut investir'),
dict(id='cmwg8v25q003x01muiadgrmrd',slug='terre-agricole',photos=[6,1,4],t1='Terre Agricole',t2='de 2,23 ha',pill='🌾 Terres agricoles · Mbour',prix='10 058 000 FCFA',pfs=92,titre='Terre Agricole de 2,23 ha vers Ghass - Ndiaguaniao',lieu='Mbour (Ndiaganiao)',s1='Une terre agricole à vendre vers Mbour',s3='Envoie ça à quelqu’un qui veut cultiver'),
dict(id='cmwauhixw001h01muls0jez88',slug='terrain-rn2',photos=[1,3,4],t1='Terrain de 4050 m²',t2='en bordure de la RN2',fs=78,pill='🛣️ Terrains · Tivaouane',prix='9 000 000 FCFA',pfs=92,titre='Terrain en bordure de la RN2 de 4050 m² vers Méouane - Tivaouane',lieu='Tivaouane (Méouane)',s1='Un terrain au bord de la route nationale',s3='Envoie ça à quelqu’un qui cherche un terrain'),
dict(id='cmwdu2ejn003901mu61k1kuxn',slug='verger-agrumes',photos=[4,3,5],t1='Verger d’agrumes',t2='de 3,5 hectares',fs=84,pill='🍊 Vergers · Tivaouane',prix='42 000 000 FCFA',pfs=88,titre='Verger d’agrumes de 3,5 hectares vers Méouane - Tivaouane',lieu='Tivaouane (Méouane)',s1='Un verger d’agrumes à vendre vers Tivaouane',s3='Envoie ça à quelqu’un qui veut investir'),
]
json.dump(LS,open('ann/listings.json','w'),ensure_ascii=False)
only=sys.argv[1:] 
for k,L in enumerate(LS):
    if only and L['slug'] not in only: continue
    make(L,13+k)
