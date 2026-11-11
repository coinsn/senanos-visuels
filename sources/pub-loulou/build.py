import re, os
F='/home/claude/fonts/node_modules/@fontsource'
SRC=open('/home/claude/pub2/pub.html').read()
LOGO=re.search(r'<svg viewBox="150 140 900 560">.*?</svg>',SRC,re.S).group(0)
BRAND=f'<div class="brand">{LOGO}<div class="word">Sen<b>Anos</b></div></div>'
cats=[('📱','Téléphones','#e8edfb',-4),('🛵','Motos','#fdeee6',3),('🏡','Terrains','#eef6ea',-3),('👗','Mode','#fbe9f1',4),('🧊','Frigos','#e6f2f5',-2)]
cat_html=''.join(f'<div class="cat" data-i="{i}" data-r="{r}"><div class="circ" style="background:{c}">{e}</div><div class="fr" style="font-size:150px;margin-top:30px">{w}</div></div>' for i,(e,w,c,r) in enumerate(cats))
items=[('🏡','Terrain 4004 m²','Mboro · Thiès','4 950 000','#eef6ea'),('🛵','Honda Lead, très bon état','Guédiawaye','250 000','#fdeee6'),('📱','iPhone 13 Pro 128 Go','Dakar','230 000','#e8edfb'),('🧊','Réfrigérateur Samsung','Dakar','150 000','#e6f2f5'),('🌾','Terre agricole 1,25 ha','Khombole','5 500 000','#fff6dc')]
cards=''.join(f'''<div class="lc" data-a="{0.5+0.5*i}" data-k="right"><div class="ic" style="background:{bg}">{e}</div><div style="flex:1;min-width:0;text-align:left"><div class="lt">{t}</div><div class="lv">📍 {v}</div></div><div class="fr red lp">{p} <sup>F</sup></div></div>''' for i,(e,t,v,p,bg) in enumerate(items))
import random; random.seed(4)
conf=''.join(f'<i class="cf" data-x="{random.uniform(-1,1):.3f}" data-y="{random.uniform(.5,1.4):.3f}" data-s="{random.uniform(.6,1.3):.2f}" data-r="{random.randint(-720,720)}" style="background:{random.choice(["#d7263d","#f6be5a","#1f9d55","#3b5bdb","#fff"])}"></i>' for _ in range(70))
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Fraunces;src:url({F}/fraunces/files/fraunces-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:Fraunces;src:url({F}/fraunces/files/fraunces-latin-900-normal.woff2);font-weight:900}}
@font-face{{font-family:DS;src:url({F}/dancing-script/files/dancing-script-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:I;src:url({F}/inter/files/inter-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:I;src:url({F}/inter/files/inter-latin-600-normal.woff2);font-weight:600}}
@font-face{{font-family:I;src:url({F}/inter/files/inter-latin-700-normal.woff2);font-weight:700}}
:root{{--foreground:#222;--primary:#d7263d;--background:#f7f5f2}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:transparent}}
body{{width:1080px;height:1920px;overflow:hidden;font-family:I,sans-serif;color:#222;position:relative}}
.fr{{font-family:Fraunces;font-weight:900;letter-spacing:-2px;line-height:1.04}}
.red{{color:#d7263d}}
.brand{{display:flex;align-items:center;gap:14px}}.brand svg{{width:92px;height:57px}}.word{{font-family:DS;font-weight:700;font-size:58px;line-height:1}}.word b{{color:#d7263d}}
#bg{{position:absolute;inset:0;background:#f7f5f2;overflow:hidden;opacity:0}}
.glow{{position:absolute;border-radius:50%}}
.sc{{position:absolute;inset:0;opacity:0;overflow:hidden}}
.ctr{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 70px}}
[data-a]{{opacity:0}}
#topbrand{{position:absolute;top:96px;left:0;right:0;display:flex;justify-content:center;opacity:0}}
.pillw{{display:inline-flex;align-items:center;background:#fff;border-radius:999px;padding:14px 34px;box-shadow:0 10px 30px rgba(0,0,0,.25)}}
.cat{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0}}
.circ{{width:560px;height:560px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:300px}}
.phone{{position:absolute;left:240px;top:500px;width:600px;height:1040px;background:#fff;border:16px solid #222;border-radius:84px;box-shadow:0 50px 100px rgba(0,0,0,.22);padding:64px 40px 0;text-align:left;overflow:hidden}}
.f{{margin-bottom:24px}}.f label{{display:block;font-size:24px;color:#888;margin-bottom:8px;font-weight:500}}
.f div{{border:3px solid #e6e1db;border-radius:20px;padding:16px 20px;font-size:30px;min-height:74px;background:#faf9f7;font-weight:600;white-space:nowrap}}
.step{{position:absolute;top:270px;left:0;right:0;text-align:center;font-size:104px;opacity:0}}
.cf{{position:absolute;left:540px;top:980px;width:22px;height:30px;border-radius:5px;opacity:0}}
.lc{{display:flex;align-items:center;gap:24px;background:#fff;border:2px solid #ece8e3;border-radius:32px;padding:22px 28px;box-shadow:0 14px 30px rgba(0,0,0,.07);margin-bottom:22px;height:150px}}
.ic{{width:100px;height:100px;border-radius:26px;display:flex;align-items:center;justify-content:center;font-size:58px;flex-shrink:0}}
.lt{{font-size:34px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.lv{{font-size:26px;color:#888;margin-top:6px;font-weight:500}}
.lp{{font-size:42px;letter-spacing:-1px;white-space:nowrap}}.lp sup{{font-size:22px}}
.cta{{display:inline-block;background:#d7263d;color:#fff;border-radius:999px;padding:28px 54px;font-size:46px;font-weight:700;box-shadow:0 16px 36px rgba(215,38,61,.35)}}
</style></head><body>
<div id="bg"><div class="glow" style="width:1100px;height:1100px;right:-400px;top:-350px;background:radial-gradient(circle,rgba(215,38,61,.16),rgba(215,38,61,0) 65%)"></div><div class="glow" style="width:900px;height:900px;left:-350px;bottom:-300px;background:radial-gradient(circle,rgba(246,190,90,.24),rgba(246,190,90,0) 65%)"></div></div>
<div id="topbrand">{BRAND}</div>

<div class="sc" id="s1" data-s="0" data-e="3.5">
 <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 45%,rgba(0,0,0,.82) 86%)"></div>
 <div style="position:absolute;top:90px;left:0;right:0;display:flex;justify-content:center"><div class="pillw" data-a="0.05" data-k="pop">{BRAND}</div></div>
 <div style="position:absolute;left:60px;right:60px;bottom:400px;text-align:center">
  <div class="fr" data-a=".25" data-k="slam" style="font-size:124px;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.5)">Tu as un truc</div>
  <div style="margin-top:14px"><span class="fr" data-a=".95" data-k="slam" data-r="-3" style="display:inline-block;font-size:156px;color:#fff;background:#d7263d;padding:4px 40px 18px;border-radius:30px;box-shadow:0 20px 50px rgba(0,0,0,.4)">à vendre ?</span></div>
  <div style="margin-top:44px"><span data-a="2.1" data-k="up" style="display:inline-block;background:#fff;border-radius:999px;padding:16px 36px;font-size:42px;font-weight:700">Loulou a le bon plan 👇</span></div>
 </div>
</div>

<div class="sc" id="s2" data-s="3.5" data-e="7.5">{cat_html}
 <div class="ctr" id="reveal" style="opacity:0"><div style="font-size:60px;font-weight:600;color:#666">Tout se vend sur</div>
 <div id="biglogo" style="display:flex;flex-direction:column;align-items:center;margin-top:30px"><div style="width:440px">{LOGO}</div><div class="word" style="font-size:210px;margin-top:10px">Sen<b>Anos</b></div></div></div>
</div>

<div class="sc" id="s3" data-s="7.5" data-e="12.5">
 <div class="step fr" data-w="0.2,1.7">1. Une <span class="red">photo</span> 📸</div>
 <div class="step fr" data-w="1.7,3.1">2. Ton <span class="red">prix</span> 💰</div>
 <div class="step fr" data-w="3.1,9">3. <span class="red">Publie !</span> 🚀</div>
 <div class="phone" id="ph">
  <div class="fr" style="font-size:42px;letter-spacing:-1px;margin-bottom:26px">Publier une annonce</div>
  <div style="height:230px;border-radius:22px;background:#fdeee6;display:flex;align-items:center;justify-content:center;margin-bottom:24px;border:3px dashed #f3c9b0;font-size:130px"><span id="pic" style="display:inline-block">🛵</span></div>
  <div class="f"><label>Titre</label><div id="f1"></div></div>
  <div class="f"><label>Prix</label><div id="f2"></div></div>
  <div class="f"><label>Ville</label><div id="f3"></div></div>
  <div id="pub" style="background:#d7263d;color:#fff;border-radius:999px;text-align:center;font-weight:700;font-size:36px;padding:24px;margin-top:8px">Publier</div>
  <div id="ok" style="position:absolute;left:34px;right:34px;top:330px;background:#fff;border-radius:34px;box-shadow:0 24px 70px rgba(0,0,0,.28);padding:44px 30px;text-align:center;opacity:0">
   <div style="width:130px;height:130px;border-radius:50%;background:#e8f6ee;margin:0 auto 22px;display:flex;align-items:center;justify-content:center"><svg width="76" height="76" viewBox="0 0 24 24" fill="none" stroke="#1f9d55" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg></div>
   <div class="fr" style="font-size:44px;letter-spacing:-1px;white-space:nowrap">Annonce en ligne !</div><div style="font-size:28px;color:#888;margin-top:12px;font-weight:500">Les acheteurs peuvent t’écrire</div></div>
 </div>
 {conf}
</div>

<div class="sc" id="s4" data-s="12.5" data-e="15.5" style="background:#d7263d">
 <div id="rays" style="position:absolute;left:-960px;top:-540px;width:3000px;height:3000px;background:repeating-conic-gradient(rgba(255,255,255,.07) 0 10deg,rgba(255,255,255,0) 10deg 20deg)"></div>
 <div class="ctr" style="color:#fff">
  <div id="clab" style="font-size:72px;font-weight:700;opacity:.9">La commission ?</div>
  <div id="cnt" class="fr" style="font-size:400px;line-height:1;margin-top:10px;letter-spacing:-10px">15 %</div>
  <div class="fr" data-a="1.45" data-k="up" style="font-size:104px;margin-top:6px">de commission</div>
  <div data-a="1.9" data-k="pop" style="margin-top:56px;background:#fff;color:#d7263d;border-radius:999px;padding:24px 44px;font-size:42px;font-weight:700">Tout l’argent de ta vente reste pour toi 💸</div>
 </div>
</div>

<div class="sc" id="s5" data-s="15.5" data-e="21.5">
 <div style="position:absolute;left:70px;right:70px;top:230px;text-align:center">
  <div class="fr" data-a="0.05" data-k="up" style="font-size:92px">Ça bouge sur <span class="red">SenAnos</span> 🔥</div>
  <div data-a="0.3" data-k="up" style="font-size:32px;color:#777;font-weight:500;margin-top:14px">De vraies annonces, en ligne en ce moment</div>
  <div style="margin-top:44px">{cards}</div>
  <div class="fr red" data-a="4.0" data-k="slam" data-r="-2" style="font-size:132px;margin-top:26px">Et la tienne ?</div>
 </div>
</div>

<div class="sc" id="s6" data-s="21.5" data-e="99">
 <div id="hole" style="position:absolute;left:90px;top:230px;width:900px;height:960px;border-radius:64px;box-shadow:0 0 0 4000px #f7f5f2"></div>
 <div style="position:absolute;left:82px;top:222px;width:916px;height:976px;border-radius:72px;border:10px solid #fff;box-shadow:0 30px 70px rgba(0,0,0,.18)"></div>
 <div style="position:absolute;top:96px;left:0;right:0;display:flex;justify-content:center">{BRAND}</div>
 <div style="position:absolute;left:60px;right:60px;top:1236px;text-align:center">
  <div class="fr" data-a="0.5" data-k="up" style="font-size:74px">Le marché de tout,<br><span class="red">près de chez vous</span></div>
  <div style="margin-top:34px"><span class="cta" id="cta" data-a="1.3" data-k="pop">Publie ton annonce 👉 senanos.com</span></div>
 </div>
</div>

<script>
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)); const e=x=>1-Math.pow(1-cl(x),3);
const back=x=>{{x=cl(x);const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}};
const $=id=>document.getElementById(id);
function type(id,s,t,a,dur){{const n=Math.floor(cl((t-a)/dur)*s.length);$(id).textContent=s.slice(0,n)+((t>a&&t<a+dur+.25&&Math.floor(t*4)%2==0)?'|':'');}}
window.render=function(t){{
 $('bg').style.opacity=cl((t-3.38)/.2)*cl((21.62-t)/.2);
 document.querySelectorAll('.glow').forEach((g,i)=>g.style.transform=`translate(${{Math.sin(t*.6+i)*50}}px,${{Math.cos(t*.5+i)*50}}px)`);
 $('topbrand').style.opacity=cl((t-3.5)/.3)*cl((21.4-t)/.2)*( (t>5.95&&t<7.5)?0:1 );
 document.querySelectorAll('.sc').forEach(s=>{{const a=+s.dataset.s,b=+s.dataset.e;s.style.opacity=cl((t-a+.08)/.16)*cl((b-t+.08)/.16);
  s.querySelectorAll('[data-a]').forEach(el=>{{const d=a+(+el.dataset.a);const k=el.dataset.k||'up';const r=+(el.dataset.r||0);
   el.style.opacity=cl((t-d)/.14);
   if(k=='pop')el.style.transform=`rotate(${{r}}deg) scale(${{back((t-d)/.45)}})`;
   else if(k=='slam'){{const p=e((t-d)/.28);el.style.transform=`rotate(${{r}}deg) scale(${{2.4-1.4*p+ (t>d+.28? .04*Math.exp(-(t-d-.28)*9)*Math.sin((t-d)*40):0)}})`;}}
   else if(k=='right')el.style.transform=`translateX(${{(1-back((t-d)/.5))*700}}px)`;
   else el.style.transform=`translateY(${{(1-e((t-d)/.5))*80}}px)`;
  }});}});
 // s2 categories
 document.querySelectorAll('.cat').forEach(c=>{{const i=+c.dataset.i,a=3.5+.5*i,b=a+.5;const on=(t>=a-.02&&t<b)?1:0;c.style.opacity=on*cl((t-a+.02)/.06);
   c.style.transform=`rotate(${{c.dataset.r}}deg) scale(${{.55+.45*back((t-a)/.28)}})`;}});
 const rv=$('reveal');rv.style.opacity=cl((t-5.98)/.1);$('biglogo').style.transform=`scale(${{.4+.6*back((t-6.0)/.5)+.02*Math.sin((t-6)*5)*(t>6.5?1:0)}})`;
 // s3
 const u=t-7.5;
 document.querySelectorAll('.step').forEach(s=>{{const [a,b]=s.dataset.w.split(',').map(Number);s.style.opacity=cl((u-a)/.12)*cl((b-u)/.12);s.style.transform=`translateY(${{(1-back((u-a)/.4))*-70}}px)`;}});
 $('ph').style.transform=`perspective(1700px) rotateY(${{-24+18*e(u/.9)+2.5*Math.sin(u*1.3)}}deg) rotateX(${{6-4*e(u/.9)}}deg) translateY(${{(1-e(u/.8))*500}}px)`;
 $('pic').style.transform=`scale(${{back((u-.45)/.45)}})`;
 type('f1','Honda Lead, très bon état',t,8.35,.8);type('f2','250 000 F',t,9.35,.6);type('f3','Guédiawaye',t,10.05,.45);
 $('pub').style.transform=`scale(${{(u>3.25&&u<3.45)?.92:1}})`;
 const ok=$('ok');ok.style.opacity=cl((u-3.5)/.15);ok.style.transform=`scale(${{.5+.5*back((u-3.5)/.45)}})`;
 document.querySelectorAll('.cf').forEach(c=>{{const v=u-3.55;if(v<0){{c.style.opacity=0;return;}}const x=+c.dataset.x,y=+c.dataset.y,s=+c.dataset.s;
   c.style.opacity=cl(1.6-v);c.style.transform=`translate(${{x*620*(1-Math.exp(-v*2.2))}}px,${{-y*1250*v+1500*v*v}}px) rotate(${{c.dataset.r*v}}deg) scale(${{s}})`;}});
 // s4
 const w=t-12.5;$('rays').style.transform=`rotate(${{w*14}}deg)`;
 const cnt=$('cnt');
 if(w<.2){{cnt.textContent='15 %';cnt.style.transform='scale(1)';}}
 else if(w<1.0){{const p=(w-.2)/.8;cnt.textContent=Math.max(1,Math.round(15*(1-p*p)))+' %';cnt.style.transform=`scale(${{1-.12*p}})`;}}
 else{{cnt.textContent='0 F';const p=e((w-1)/.25);cnt.style.transform=`scale(${{2.6-1.6*p}}) translateX(${{(w<1.7?Math.sin(w*70)*14*Math.exp(-(w-1)*6):0)}}px)`;}}
 $('clab').style.opacity=.9*cl((w-.02)/.15)*cl((1.0-w)/.1+ (w>=1?0:0));
 // s6
 const z=t-21.5;$('cta').style.transform=(z>1.8)?`scale(${{1+.035*Math.sin((z-1.8)*6)}})`:$('cta').style.transform;
}};
render(0);
</script></body></html>'''
open('ad.html','w').write(html)
