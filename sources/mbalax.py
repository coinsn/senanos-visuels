# Bande-son ORIGINALE inspirée du mbalax (aucune musique existante) : sabar (mbëng-mbëng, nder, tama),
# basse, accords de clavier en contretemps, shaker. Varier seed pour changer de morceau
# (tempo, tonalité, motifs et instruments changent avec seed).
import numpy as np, wave
SR=44100
def mbalax(path,D,seed=1):
    rng=np.random.default_rng(seed); N=int(SR*D); out=np.zeros((N,2))
    bpm=[122,128,132,126,136,124][seed%6]; s16=60/bpm/4
    root=[110,116.54,98,123.47,103.83,130.81][(seed//2)%6]   # tonalité (La, Sib, Sol, Si, Lab, Do)
    env=lambda n,d: np.exp(-np.arange(n)/SR/d)
    def put(sig,t,g,pan=0):
        i=int(t*SR)
        if i>=N: return
        j=min(N,i+len(sig)); s=sig[:j-i]*g
        out[i:j,0]+=s*(1-pan)*.9+s*.1; out[i:j,1]+=s*(1+pan)*.9+s*.1
    def noise(n): return np.diff(np.concatenate([[0],rng.standard_normal(n)]))
    def drum(f0,f1,dec,dur,nz=0,nd=.02,glide=30):
        n=int(SR*dur); t=np.arange(n)/SR; f=f1+(f0-f1)*np.exp(-t*glide)
        s=np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,dec)
        if nz: s+=nz*noise(n)*env(n,nd)
        return s
    def tama(up):  # tambour d'aisselle : hauteur qui glisse
        n=int(SR*.22); t=np.arange(n)/SR; f=(420+260*(1-np.exp(-t*25))) if up else (680-260*(1-np.exp(-t*25)))
        return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.07)+.3*noise(n)*env(n,.01)
    def pluck(f,dur,bright=3):
        n=int(SR*dur); t=np.arange(n)/SR
        return sum(np.sin(2*np.pi*f*k*t)/k**1.3*np.exp(-t*(4+k*bright)) for k in range(1,6))
    def chord(fs,dur):
        n=int(SR*dur); t=np.arange(n)/SR; a=np.minimum(1,t/.005)*np.exp(-t*9)
        return sum(np.sign(np.sin(2*np.pi*f*t))*.25+np.sin(2*np.pi*f*t) for f in fs)*a/len(fs)
    P=[  # 16 doubles-croches par mesure : basse-tambour, nder (claque aiguë), mbëng ouvert, tama
     ("x..x..x...x..x..","....x..x....x.xx","x.....x..x......","..x.......x..x.."),
     ("x..x...x..x.x...","..x...x.x.x...x.","x.......x..x....",".x...x.....x...x"),
     ("x.x...x..x..x...","...xx.....x.x.x.","x..x.......x....","......x.x.....x."),
    ][seed%3]
    BASS=[(0,0),(3,0),(6,7),(10,5),(13,7)] if seed%2 else [(0,0),(4,12),(7,7),(10,0),(12,5),(14,7)]
    PROG=[[0,4,7],[5,9,12],[7,11,14],[5,9,12]]
    st=lambda r,semi: r*2**(semi/12)
    nbar=int(D/(16*s16))+1
    for bar in range(nbar):
        for k in range(16):
            t=(bar*16+k)*s16
            if t>=D: break
            sw=t+(s16*.12 if k%2 else 0)            # léger swing
            intro=t<1.2
            if P[0][k]=='x': put(drum(140,55,.16,.45,.2),sw,.95)
            if P[1][k]=='x' and not intro: put(drum(900,700,.025,.12,1.2,.02),sw,.42+.1*rng.random(),.35)
            if P[2][k]=='x': put(drum(260,200,.09,.3,.4),sw,.5,-.3)
            if P[3][k]=='x' and t>2: put(tama(k%4==2),sw,.35,.5)
            if k%2==0: put(noise(int(SR*.05))*env(int(SR*.05),.012),sw,.12 if k%4 else .2,-.5)  # shaker
            if t>2.0:
                for (pos,semi) in BASS:
                    if pos==k: put(pluck(st(root/2,semi+PROG[bar%4][0]),.35,1.5),sw,.55)
            if t>4.0 and k in (2,6,10,14):   # accords en contretemps
                put(chord([st(root*2,x) for x in PROG[bar%4]],.18),sw,.16,.2)
            if t>8 and bar%2==1 and k in (0,3,6,8,11):  # petite mélodie de clavier
                put(pluck(st(root*4,[0,4,7,9,7][[0,3,6,8,11].index(k)]+PROG[bar%4][0]),.25,6),sw,.1,-.2)
    # roulement de sabar en fin de phrase toutes les 4 mesures
    for bar in range(3,nbar,4):
        for k in range(12,16):
            put(drum(950,750,.02,.1,1.3,.015),(bar*16+k)*s16+.5*s16,.35,.3)
    fi=int(.15*SR); fo=int(1.5*SR); out[:fi]*=np.linspace(0,1,fi)[:,None]; out[-fo:]*=np.linspace(1,0,fo)[:,None]
    out=np.tanh(out/np.max(np.abs(out))*1.6)/np.tanh(1.6)*.9
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype('<i2').tobytes()); w.close()
    return bpm
