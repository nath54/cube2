#coding:utf-8
import random,pygame,time,numpy,math,os
from pygame.locals import *
from os.path import expanduser

pygame.init()
btex,btey=1280/1.5,1024/1.5
io = pygame.display.Info()
mtex,mtey=io.current_w,io.current_h
tex,tey=int(mtex/1.5),int(mtey/1.5)
fullscreen=False
acchardware=False
doublebuf=False

cac="|"
cacc="#"

home = expanduser("~")
dre="Cube2/"
if not dre[:-1] in os.listdir(home): os.mkdir(home+"/"+dre)
dire=home+"/"+dre

dfs="save.nath"
if not dfs in os.listdir(dire):
    f=open(dire+dfs,"w")
    f.write("0|0")
    f.close()

skins_possedes=[]
skin_equipe=0

f=open(dire+dfs,"r").read().split(cac)
skin_equipe=int(f[0])
for ff in f[1].split(cacc):
    try: skins_possedes.append( int(ff) )
    except: pass
if skin_equipe>=len(skins_possedes): skin_equipe=0
if len(f)>3:
    tex=int(f[2])
    tey=int(f[3])
if len(f)>4:  fullscreen=bool(int(f[4]))
if len(f)>5:  acchardware=bool(int(f[5]))
if len(f)>6:  doublebuf=bool(int(f[6]))
    

def rx(x): return int(x/btex*tex)
def ry(y): return int(y/btey*tey)

def rxx(x): return float(float(x)/float(btex)*float(tex))
def ryy(y): return float(float(y)/float(btey)*float(tey))

options=0
if fullscreen: options|=pygame.FULLSCREEN
if acchardware: options|=pygame.HWSURFACE
if doublebuf: options|=pygame.DOUBLEBUF

fenetre=pygame.display.set_mode([tex,tey],options)
pygame.display.set_caption("Cube2")
font1=pygame.font.SysFont("Arial",ry(17))
font2=pygame.font.SysFont("Arial",ry(20))
font3=pygame.font.SysFont("Arial",ry(30))
font4=pygame.font.SysFont("Arial",ry(40))
font5=pygame.font.SysFont("Serif",ry(60))

cursor1,mask1=pygame.cursors.compile(("XXXXXXXXXXXXXXXX","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","XXXXXXXXXXXXXXXX"), black='X', white='.', xor='o')
cursor_sizer1=((16,16),(9,8),cursor1,mask1)
pygame.mouse.set_cursor(*cursor_sizer1)

mon_joystick="joystick"
nb_joysticks = pygame.joystick.get_count()
if nb_joysticks > 0:
	mon_joystick = pygame.joystick.Joystick(0)
	mon_joystick.init()

def rcl(): return (random.randint(50,200),random.randint(50,100),random.randint(50,200))

tpage=int((rx(750)/ry(150))*3)

dimg="images/"

sa1=["skin4-1.png","skin4-2.png","skin4-3.png","skin4-4.png","skin4-5.png","skin4-6.png","skin4-7.png","skin4-8.png","skin4-9.png","skin4-10.png","skin4-11.png","skin4-12.png","skin4-13.png","skin4-12.png","skin4-11.png","skin4-10.png","skin4-9.png","skin4-8.png","skin4-7.png","skin4-6.png","skin4-5.png","skin4-4.png","skin4-3.png","skin4-2.png","skin4-1.png"]
sa2=["skin6.png","skin6-1.png","skin6-2.png","skin6-3.png","skin6-4.png","skin6-5.png","skin6-6.png","skin6-7.png","skin6-8.png","skin6-9.png","skin6-10.png","skin6-11.png","skin6-12.png","skin6-13.png","skin6-14.png","skin6-15.png","skin6-16.png","skin6-17.png","skin6-18.png","skin6-19.png","skin6-20.png"]
sa3=["skin9-1.png","skin9-2.png","skin9-3.png","skin9-4.png","skin9-5.png","skin9-6.png","skin9-7.png","skin9-8.png","skin9-9.png","skin9-10.png","skin9-11.png","skin9-12.png","skin9-13.png","skin9-14.png","skin9-15.png","skin9-16.png","skin9-17.png"]
sa4=["skin11-1.png","skin11-2.png","skin11-3.png","skin11-4.png","skin11-5.png","skin11-6.png","skin11-5.png","skin11-4.png","skin11-3.png","skin11-2.png"]
sa5=["skin13-1.png","skin13-2.png","skin13-3.png","skin13-4.png","skin13-5.png"]
sa6=["skin14-1.png","skin14-2.png","skin14-3.png","skin14-4.png","skin14-5.png","skin14-6.png","skin14-7.png","skin14-8.png","skin14-9.png"]
sa7=["skin15-1.png","skin15-2.png","skin15-3.png","skin15-4.png","skin15-5.png","skin15-6.png","skin15-7.png","skin15-8.png","skin15-9.png","skin15-10.png","skin15-11.png","skin15-12.png","skin15-13.png"]
sa8=["skin16-1.png","skin16-2.png","skin16-3.png","skin16-4.png","skin16-5.png"]
sa9=["skin17-1.png","skin17-2.png","skin17-3.png","skin17-4.png","skin17-5.png"]
skins=[[["skin1.png"],0,False,0],[["skin2.png"],1,True,0],[["skin3.png"],2,True,0],[sa1,3,True,0],[["skin5.png"],1,False,0],[sa2,2,False,0],
[["skin7.png"],0,False,0],[["skin8.png"],0,False,0],[sa3,3,True,180],[["skin10.png"],1,True,0],[sa4,4,True,0],[["skin12.png"],0,False,0],[sa5,3,True,0],
[sa6,1,True,0],[sa7,0,True,0],[sa8,2,True,0],[sa9,4,True,0],[["skin18.png"],1,False,0],[["skin19.png"],1,False,0],[["skin20.png"],1,False,0],[["skin21.png"],1,False,0]
,[["skin22.png"],1,False,0],[["skin23.png"],1,False,0],[["skin24.png"],1,False,0],[["skin25.png"],1,False,0],[["skin26.png"],1,False,0],[["skin27.png"],1,False,0]
,[["skin28.png"],1,False,0],[["skin29.png"],1,False,0],[["skin30.png"],1,False,0],[["skin31.png"],1,False,0],[["skin32.png"],1,False,0],[["skin33.png"],1,False,0]
,[["skin34.png"],1,False,0],[["skin35.png"],1,False,0],[["skin36.png"],1,False,0],[["skin37.png"],1,False,0],[["skin38.png"],1,False,0],[["skin39.png"],1,False,0],[["skin40.png"],1,False,0]
,[["skin41.png"],1,False,0],[["skin42.png"],1,False,0],[["skin43.png"],1,False,0],[["skin44.png"],1,False,0],[["skin45.png"],1,False,0],[["skin46.png"],1,False,0],[["skin47.png"],1,False,0]
,[["skin48.png"],1,False,0],[["skin49.png"],1,False,0],[["skin50.png"],1,False,0],[["skin51.png"],1,False,0],[["skin52.png"],1,False,0],[["skin53.png"],1,False,0],[["skin54.png"],1,False,0]
,[["skin55.png"],1,False,0],[["skin56.png"],1,False,0],[["skin57.png"],1,False,0],[["skin58.png"],1,False,0],[["skin59.png"],1,False,0],[["skin60.png"],1,False,0],[["skin61.png"],1,False,0]
,[["skin62.png"],1,False,0],[["skin63.png"],1,False,0],[["skin64.png"],1,False,0],[["skin65.png"],1,False,0],[["skin67.png"],1,False,0],[["skin68.png"],1,False,0]
,[["skin69.png"],0,False,0],[["skin70.png"],0,False,0],[["skin71.png"],0,False,0],[["skin72.png"],0,False,0],[["skin73.png"],0,False,0]
]
#0=imgs 1 = rarete 2=rotate 3=agl base
#raretes : 0=commun 1=rare 2=epique 3=légendaire 4=divin

skins_com=[]
skins_rar=[]
skins_epi=[]
skins_leg=[]
skins_div=[]

for x in range(len(skins)):
    r=skins[x][1]
    if r==0: skins_com.append( x )
    elif r==1: skins_rar.append( x )
    elif r==2: skins_epi.append( x )
    elif r==3: skins_leg.append( x )
    else: skins_div.append( x )

raretes=["commun","rare","épique","légendaire","divin"]
cl_raretes=[(38,110,224),(199,91,20),(202,14,227),(14,227,49),(255,255,0)]

def save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf):
    txt=str(skin_equipe)+cac
    for s in skins_possedes:
        txt+=str(s)+cacc
    txt=txt[:-1]
    txt+=cac+str(tex)+cac+str(tey)
    fs="0"
    if fullscreen: fs="1"
    txt+=cac+fs
    ah="0"
    if acchardware: ah="1"
    txt+=cac+ah
    db="0"
    if doublebuf: db="1"
    txt+=cac+db
    f=open(dire+dfs,"w")
    f.write(txt)
    f.close()

class Mape:
    def __init__(self,niv):
        dif=int(float(niv)/100.*20.)+1
        self.tx=50+5*dif
        self.ty=50+5*dif
        self.clm=rcl()
        self.cls=(255-self.clm[0],255-self.clm[1],255-self.clm[2])
        self.mape=numpy.zeros([self.tx,self.ty],dtype=int)
        self.chem=[[random.randint(int(self.tx/3),int(self.tx/3*2)),random.randint(int(self.tx/3),int(self.tx/3*2))]]
        self.deb=self.chem[0]
        dbs=[self.deb]
        nbbranches=dif
        dc=0
        fins=[]
        for y in range(nbbranches):
            self.chem.append( random.choice(dbs) ) 
            for x in range(random.randint(400,600)):
                c=self.chem[len(self.chem)-1]
                ax,ay=0,0
                if random.choice([0,1,dc])==1:
                    ax=random.randint(-1,1)
                    dc=1
                else:
                    dc=0
                    ay=random.randint(-1,1)
                cx,cy=c[0]+ax,c[1]+ay
                if cx < 0: cx=0
                elif cx > self.tx-1: cx=self.tx-1
                if cy < 0: cy=0
                elif cy > self.ty-1: cy=self.ty-1
                self.chem.append([cx,cy])
            for x in range(3): dbs.append( self.chem[len(self.chem)-1] )
            fins.append( self.chem[len(self.chem)-1] )
        fpl=fins[0]
        for f in fins:
            if math.sqrt((self.deb[0]-f[0])**2+(self.deb[1]-f[1])**2) > math.sqrt((self.deb[0]-fpl[0])**2+(self.deb[1]-fpl[1])**2): fpl=f
        self.fin=fpl
        for x in range(self.tx):
            for y in range(self.ty):
                if [x,y] in self.chem: self.mape[x,y]=0 #sol
                else: self.mape[x,y]=1 #mur
        self.p1=False
        self.dp1=time.time()
        self.tp1=1.5
        self.dif=dif
    def update(self):
        if time.time()-self.dp1>=self.tp1:
            self.p1=not self.p1
            self.dp1=time.time()

class Cube2:
    def __init__(self,cube):
        self.px=cube.px
        self.py=cube.py
        self.tx=cube.tx
        self.ty=cube.ty
        self.cl=(150,150,150)
        self.img=pygame.transform.scale(pygame.image.load(dimg+"pics.png"),[self.tx,self.ty])
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.dbg=time.time()
        self.tbg=0.01
        self.pbg=False
        self.dpbg=time.time()
        self.tpbg=1.5
        self.keys=[]
    def reload(self,cube):
        self.px=cube.px
        self.py=cube.py
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.vitx=0.
        self.vity=0.
        self.isgrap=False
        self.keys=[]
        self.pbg=False
        self.dpbg=time.time()
    def update(self,cube):
        if not self.pbg and time.time()-self.dpbg >= self.tpbg: self.pbg=True
        if self.pbg and time.time()-self.dbg >= self.tbg:
            self.dbg=time.time()
            self.px,self.py=self.keys[0]
            self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
            del(self.keys[0])

class Cube:
    def __init__(self,tcb,tc,mape,niv,skin_equipe,skins_possedes):
        self.px=mape.chem[0][0]*tc+rx(1)
        self.py=mape.chem[0][1]*tc+ry(1)
        self.tx=int(tcb/3)
        self.ty=int(tcb/3)
        self.cl=(255,255,255)
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.dbg=time.time()
        self.tbg=0.01
        self.vitx=0.
        self.vity=0.
        self.acc=rxx(0.1)
        self.decc=rxx(0.01)
        self.vitmax=rxx(5)
        self.dk=time.time()
        self.tk=0.01
        self.checkpoint=[self.px,self.py]
        self.vie_tot=100
        self.vie=self.vie_tot
        self.cangrap=False
        if niv>=10: self.cangrap=True
        self.isgrap=False
        self.grapx=0
        self.grapy=0
        self.vitgrap=7
        self.dgrap=time.time()
        self.tgrap=3
        self.imgs=[]
        for i in skins[skins_possedes[skin_equipe]][0]:
            self.imgs.append( pygame.transform.scale(pygame.image.load(dimg+i),[int(self.tx*140/100),int(self.ty*140/100)]) )
        self.an=0
        self.dan=time.time()
        self.tan=0.1
        self.agl=0
        self.img=pygame.transform.rotate(self.imgs[self.an],self.agl)
        self.rot=skins[skins_possedes[skin_equipe]][2]
        self.ab=skins[skins_possedes[skin_equipe]][3]
        self.fl1=pygame.transform.scale(pygame.image.load(dimg+"fl1.png"),[int(self.tx*140/100),int(self.ty*140/100)])
        self.fl2=pygame.transform.scale(pygame.image.load(dimg+"fl2.png"),[int(self.tx*140/100),int(self.ty*140/100)])
        self.fl3=pygame.transform.scale(pygame.image.load(dimg+"fl3.png"),[int(self.tx*140/100),int(self.ty*140/100)])
        self.fl4=pygame.transform.scale(pygame.image.load(dimg+"fl4.png"),[int(self.tx*140/100),int(self.ty*140/100)])
        self.fl5=pygame.transform.scale(pygame.image.load(dimg+"fl5.png"),[int(self.tx*140/100),int(self.ty*140/100)])
        self.fl6=pygame.transform.scale(pygame.image.load(dimg+"fl6.png"),[int(self.tx*140/100),int(self.ty*140/100)])
        self.fl7=pygame.transform.scale(pygame.image.load(dimg+"fl7.png"),[int(self.tx*140/100),int(self.ty*140/100)])
        self.fl8=pygame.transform.scale(pygame.image.load(dimg+"fl8.png"),[int(self.tx*140/100),int(self.ty*140/100)])
    def bouger(self,aa,cube2):
        if time.time()-self.dk >= self.tk:
            self.dk=time.time()
            if aa=="up":
                self.vity-=self.acc
                if self.rot: self.agl=180+self.ab
            elif aa=="down":
                self.vity+=self.acc
                if self.rot: self.agl=0+self.ab
            elif aa=="left":
                self.vitx-=self.acc
                if self.rot: self.agl=270+self.ab
            elif aa=="right":
                self.vitx+=self.acc
                if self.rot: self.agl=90+self.ab
            self.img=pygame.transform.rotate(self.imgs[self.an],self.agl)
    def update(self,mape,tc,cube2):
        #animation
        if time.time()-self.dan>=self.tan:
            self.dan=time.time()
            self.an+=1
            if self.an>=len(self.imgs): self.an=0
            self.img=pygame.transform.rotate(self.imgs[self.an],self.agl)
        #reste
        if time.time()-self.dbg>=self.tbg:
            self.dbg=time.time()
            #deplacements
            if self.vitx>self.vitmax: self.vitx=self.vitmax
            if self.vitx<-self.vitmax: self.vitx=-self.vitmax
            if self.vity>self.vitmax: self.vity=self.vitmax
            if self.vity<-self.vitmax: self.vity=-self.vitmax
            self.px+=self.vitx
            self.py+=self.vity
            if self.isgrap:
                if self.grapx>self.px+self.vitgrap: self.px+=self.vitgrap
                elif self.grapx>self.px: self.px=self.grapx
                if self.grapx<self.px-self.vitgrap: self.px-=self.vitgrap
                elif self.grapx<self.px: self.px=self.grapx
                
                if self.grapy>self.py+self.ty/2+self.vitgrap: self.py+=self.vitgrap
                elif self.grapy>self.py+self.ty/2: self.py=self.grapy
                if self.grapy<self.py+self.ty/2-self.vitgrap: self.py-=self.vitgrap
                elif self.grapy<self.py+self.ty/2: self.py=self.grapy
                if self.px==self.grapx and self.py==self.grapy: self.isgrap=False
            cube2.keys.append([self.px,self.py])
            #collisions
            self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
            for x in range( int((self.px)/tc)-2 , int((self.px)/tc)+2 ):
                for y in range( int((self.py)/tc)-2 , int((self.py)/tc)+2 ):
                    if x >= 0 and x < mape.tx and y >= 0 and y < mape.ty and self.rect.colliderect( pygame.Rect(x*tc,y*tc,tc,tc) ):
                        if mape.mape[x,y]==1: self.vie=0
                        if mape.mape[x,y]==2 and mape.p1: self.vie-=50
                        if mape.fin==[x,y]: return True
            if self.px<0:
                self.vie=0
                self.px-=self.vitx
                self.py-=self.vity
            if self.px+self.tx>mape.tx*tc:
                self.vie=0
                self.px-=self.vitx
                self.py-=self.vity
            if self.py<0:
                self.vie=0
                self.px-=self.vitx
                self.py-=self.vity
            if self.py+self.ty>mape.ty*tc:
                self.vie=0
                self.px-=self.vitx
                self.py-=self.vity
            if cube2.pbg and self.rect.colliderect(cube2.rect):
                self.vie-=2
            #physique
            if self.vitx>=self.decc: self.vitx-=self.decc
            if self.vitx>0 and self.vitx<self.decc: self.vitx=0
            if self.vitx<=-self.decc: self.vitx+=self.decc
            if self.vitx<0 and self.vitx>-self.decc: self.vitx=0
            if self.vity>=self.decc: self.vity-=self.decc
            if self.vity>0 and self.vity<self.decc: self.vity=0
            if self.vity<=-self.decc: self.vity+=self.decc
            if self.vity<0 and self.vity>-self.decc: self.vity=0
        return None
                        
def verif_keys(cube,cube2):
    keys=pygame.key.get_pressed()
    if keys[K_UP]: cube.bouger("up",cube2)
    if keys[K_DOWN]: cube.bouger("down",cube2)
    if keys[K_LEFT]: cube.bouger("left",cube2)
    if keys[K_RIGHT]: cube.bouger("right",cube2)
    if nb_joysticks > 0:
        #haut-bas
        aa=float(mon_joystick.get_axis(1))
        if aa > 0.5: aa=1
        elif aa < -0.5 : aa=-1
        else: aa=0 
        if aa==-1: cube.bouger("up",cube2)
        if aa==1: cube.bouger("down",cube2)
        #haut-bas
        aa=float(mon_joystick.get_axis(0))
        if aa > 0.5: aa=1
        elif aa < -0.5 : aa=-1
        else: aa=0 
        if aa==-1: cube.bouger("left",cube2)
        if aa==1: cube.bouger("right",cube2)
    return cube

def ecran_chargement():
    fenetre.fill((0,0,0))
    fenetre.blit( font4.render("chargement...",True,(255,255,255)) , [tex/3,tey/3])
    pygame.display.update()

def ecran_fin():
    fenetre.fill((0,0,0))
    fenetre.blit( font3.render("Vous avez fini le jeu",True,(255,255,255)) , [rx(100),ry(250)])
    fenetre.blit( font3.render("Revenez jouer le plus vite possible",True,(255,255,255)) , [rx(100),ry(300)])
    fenetre.blit( font3.render("Appuyez sur espace pour quitter",True,(255,255,255)) , [rx(100),ry(400)])
    pygame.display.update()
    encour_f=True
    while encour_f:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE: encour_f=False

def ecran_mort():
    fenetre.fill((0,0,0))
    fenetre.blit( font3.render("Vous avez perdu.",True,(255,255,255)) , [rx(100),ry(250)])
    fenetre.blit( font3.render("Revenez jouer le plus vite possible",True,(255,255,255)) , [rx(100),ry(300)])
    fenetre.blit( font3.render("Appuyez sur espace pour quitter",True,(255,255,255)) , [rx(100),ry(400)])
    pygame.display.update()
    encour_f=True
    while encour_f:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE: encour_f=False

def ecran_quit():
    fenetre.fill((0,0,0))
    fenetre.blit( font2.render("Vous avez quitté la partie",True,(255,255,255)) , [rx(50),ry(250)])
    fenetre.blit( font2.render("Si vous avez ragé, ou que vous en avez assez de jouer à ce jeu",True,(255,255,255)) , [rx(50),ry(300)])
    fenetre.blit( font2.render("Ce n'est pas grave, mais revenez jouer quand même ;)",True,(255,255,255)) , [rx(50),ry(350)])
    fenetre.blit( font2.render("Appuyez sur espace pour quitter",True,(255,255,255)) , [rx(50),ry(400)])
    pygame.display.update()
    encour_f=True
    while encour_f:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE: encour_f=False

def ecran_dep_lvl(mape):
    fenetre.fill(mape.clm)
    ctx=int(tex/mape.mape.shape[0])
    cty=int(tey/mape.mape.shape[1])
    for x in range(mape.mape.shape[0]):
        for y in range(mape.mape.shape[1]):
            cl=mape.clm
            if mape.mape[x,y]==0: cl=mape.cls
            if mape.fin==[x,y]: cl=(0,0,0)
            if mape.deb==[x,y]: cl=(255,255,255)
            pygame.draw.rect(fenetre,cl,(x*ctx,y*cty,ctx,cty),0)
    pygame.display.update()
    pygame.display.flip()
    time.sleep(3)

def aff(cube,mape,cam,tc,fps,niv,morts,cube2,tps1,tpstot):
    fenetre.fill(mape.clm)
    for x in range(int((-cam[0])/tc),int((-cam[0]+tex)/tc+1)):
        for y in range(int((-cam[1])/tc),int((-cam[1]+tey)/tc+1)):
            if x>=0 and x < mape.tx and y >= 0 and y < mape.ty and mape.mape[x,y]!=1:
                if mape.mape[x,y]==0:
                    cl=mape.cls
                    if mape.fin==[x,y]: cl=(0,0,0)
                if mape.mape[x,y]==2: #piege clignotant
                    if mape.p1: cl=(255,0,0)
                    else: cl=(0,255,0)
                pygame.draw.rect(fenetre,cl,(cam[0]+x*tc,cam[1]+y*tc,tc,tc),0)
                if niv <= 10 and x >= 1 and mape.mape[x-1,y]==1: pygame.draw.rect(fenetre,(255,0,0),(cam[0]+x*tc-rx(2),cam[1]+y*tc,rx(2),tc),0)
                try:
                    if niv <= 10 and x <= mape.tx-2 and mape.mape[x+1,y]==1: pygame.draw.rect(fenetre,(255,0,0),(cam[0]+x*tc+tc,cam[1]+y*tc,rx(2),tc),0)
                except: pass
                if niv <= 10 and y >= 1 and mape.mape[x,y-1]==1: pygame.draw.rect(fenetre,(255,0,0),(cam[0]+x*tc,cam[1]+y*tc-ry(2),tc,ry(2)),0)
                try:
                    if niv <= 10 and y <= mape.ty-2 and mape.mape[x,y+1]==1: pygame.draw.rect(fenetre,(255,0,0),(cam[0]+x*tc,cam[1]+y*tc+tc,tc,ry(2)),0)
                except: pass
    #cube2
    if cube2.pbg: fenetre.blit(cube2.img,[cam[0]+cube2.px,cam[1]+cube2.py])
    else: pygame.draw.rect(fenetre,(50,50,50),(cam[0]+cube2.px,cam[1]+cube2.py,cube2.tx,cube2.ty),0)
    #cube
    if cube.isgrap: pygame.draw.line(fenetre,(79, 47, 19),(cam[0]+cube.px+cube.tx/2,cam[1]+cube.py+cube.ty/2),(cam[0]+cube.grapx,cam[1]+cube.grapy),rx(4))
    #pygame.draw.rect(fenetre,cube.cl,(cam[0]+cube.px,cam[1]+cube.py,cube.tx,cube.ty),0)
    fenetre.blit( cube.img , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)] )
    if niv==1 and mape.fin[0]*tc > cube.px and abs(mape.fin[1]*tc-cube.py)<tc: fenetre.blit( cube.fl1 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    elif niv==1 and mape.fin[0]*tc < cube.px and abs(mape.fin[1]*tc-cube.py)<tc: fenetre.blit( cube.fl2 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    elif niv==1 and mape.fin[1]*tc > cube.py and abs(mape.fin[0]*tc-cube.px)<tc: fenetre.blit( cube.fl3 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    elif niv==1 and mape.fin[1]*tc < cube.py and abs(mape.fin[0]*tc-cube.px)<tc: fenetre.blit( cube.fl4 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    elif niv==1 and mape.fin[0]*tc > cube.px and mape.fin[1]*tc > cube.py: fenetre.blit( cube.fl5 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    elif niv==1 and mape.fin[0]*tc > cube.px and mape.fin[1]*tc < cube.py: fenetre.blit( cube.fl6 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    elif niv==1 and mape.fin[0]*tc < cube.px and mape.fin[1]*tc > cube.py: fenetre.blit( cube.fl7 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    elif niv==1 and mape.fin[0]*tc < cube.px and mape.fin[1]*tc < cube.py: fenetre.blit( cube.fl8 , [cam[0]+cube.px-int(cube.tx*20/100),cam[1]+cube.py-int(cube.ty*20/100)])
    #ui
    pygame.draw.rect(fenetre,(255-int((tpstot-(time.time()-tps1))/tpstot*255),int((tpstot-(time.time()-tps1))/tpstot*255),0),(rx(0),ry(0),int((tpstot-(time.time()-tps1))/tpstot*tex),ry(10)),0)
    pygame.draw.rect(fenetre,(250,0,0),(rx(100),ry(15),int(cube.vie/cube.vie_tot*rx(200)),ry(15)),0)
    pygame.draw.rect(fenetre,(0,0,0),(rx(100),ry(15),rx(200),ry(15)),1)
    fenetre.blit( font1.render("fps : "+str(fps),20,(255,255,255)), [rx(15),ry(15)] )
    fenetre.blit( font1.render("lvl : "+str(niv),20,(255,255,255)), [tex-rx(100),ry(25)] )
    fenetre.blit( font1.render("vous êtes mort : "+str(morts)+" fois",20,(255,255,255)), [tex-rx(200),ry(10)] )
    pygame.display.update()

def cniv(tcb,niv,skin_equipe,skins_possedes):
    tc=int(tcb/3+float((150-niv)/150.*(tcb/2*1.3)))
    mape=Mape(niv)
    cube=Cube(tcb,tc,mape,niv,skin_equipe,skins_possedes)
    cube2=Cube2(cube)
    cube2.tpbg=1+((30-mape.dif)/30*1)
    cam=[-cube.px+tex/2,-cube.py+tey/2]
    tps1=time.time()
    tpstot=60+40*mape.dif
    return mape,cube,cam,cube2,tps1,tpstot,tc

def main_jeu(skin_equipe,skins_possedes):
    tcb=rx(100)
    niv=1
    ecran_chargement()
    mape,cube,cam,cube2,tps1,tpstot,tc=cniv(tcb,niv,skin_equipe,skins_possedes)
    ecran_dep_lvl(mape)
    cube2.reload(cube)
    encour_g=True
    morts=0
    fps=0
    perdu=False
    while encour_g:
        t1=time.time()
        #cube
        cube2.update(cube)
        cube=verif_keys(cube,cube2)
        etat=cube.update(mape,tc,cube2)
        if cube.vie<=0:
            cube.vie=cube.vie_tot
            morts+=1
            cube.px=cube.checkpoint[0]
            cube.py=cube.checkpoint[1]
            cube.vitx,cube.vity=0,0
            cube.isgrap=False
            time.sleep(0.1)
            cube2.reload(cube)
        elif etat==True:
            if niv<100:
                niv+=1
                ecran_chargement()
                mape,cube,cam,cube2,tps1,tpstot,tc=cniv(tcb,niv,skin_equipe,skins_possedes)
                ecran_dep_lvl(mape)
                cube2.reload(cube)
            else:
                encour_g=False
                ecran_fin()
        if time.time()-tps1>=tpstot:
            encour=False
            perdu=True
            ecran_mort()
            break
        cam=[-cube.px+tex/2,-cube.py+tey/2]
        #mape
        mape.update()
        #aff
        aff(cube,mape,cam,tc,fps,niv,morts,cube2,tps1,tpstot)
        #event
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    encour_g=False
                    ecran_quit()
                elif event.key==K_n:
                    tpstot/=2
                    ecran_dep_lvl(mape)
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if cube.cangrap and time.time()-cube.dgrap>=cube.tgrap:
                    cube.dgrap=time.time()
                    cube.isgrap=True
                    cube.grapx=-cam[0]+pos[0]
                    cube.grapy=-cam[1]+pos[1]
        t2=time.time()
        tt=t2-t1
        if tt!=0: fps=int(1./tt)
    sg,txt,cltxt=None,None,None
    if niv < 15:    
        if perdu:
            sg=random.choice(skins_com)
            txt="Vous avez gagné un skin commun !"
            cltxt=cl_raretes[0]
    elif niv < 30:
        sg=random.choice(skins_rar)
        txt="Vous avez gagné un skin rare !"
        cltxt=cl_raretes[1]
    elif niv < 60:
        sg=random.choice(skins_epi)
        txt="Vous avez gagné un skin épique !"
        cltxt=cl_raretes[2]
    elif niv < 100:
        sg=random.choice(skins_leg)
        txt="Vous avez gagné un skin légendaire !"
        cltxt=cl_raretes[3]
    else:
        sg=random.choice(skins_div)
        txt="Vous avez gagné un skin divin !"
        cltxt=cl_raretes[4]
    if sg!=None:
        skins_possedes.append(sg)
        skins_possedes=list(set(skins_possedes))
        fenetre.fill((0,0,0))
        fenetre.blit( font4.render(txt,True,cltxt) , [rx(50),ry(100)])
        fenetre.blit( pygame.transform.scale(pygame.image.load(dimg+skins[sg][0][0]),[rx(200),ry(200)]) , [rx(200),ry(150)] )
        fenetre.blit( font3.render("Appuyez sur espace pour continuer",True,(255,255,255)) , [rx(100),ry(600)])
        pygame.display.update()
        encour=True
        while encour:
            for event in pygame.event.get():
                if event.type==QUIT: exit()
                elif event.type==KEYDOWN:
                    if event.key==K_SPACE: encour=False
                elif event.type==MOUSEBUTTONUP:
                    encour=False
    return skin_equipe,skins_possedes
    
def aff_menu(men,skin_equipe,skins_possedes,ps,an,tex,tey,fullscreen,acchardware,doublebuf):
    btn,btn2,btn3,btn4,btn5,btn6=None,None,None,None,None,None
    bts=[]
    for x in range(3*(tpage+1)): bts.append( None )
    bst=[]
    for x in range(10): bst.append( None )
    fenetre.fill((0,0,0))
    if men==0:
        fenetre.blit( font5.render("Cube2",20,(255,255,255)) , [rx(300),ry(10)] )
        fenetre.blit( font2.render("Le but de ce jeu est de trouver la sortie de chaque niveau",20,(255,255,255)) , [rx(100),ry(100)] )
        fenetre.blit( font2.render("La sortie d'un niveau est représentée par un carré noir",20,(255,255,255)) , [rx(100),ry(130)] )
        fenetre.blit( font2.render("Vous dirigez un carré blanc avec les flèches du clavier",20,(255,255,255)) , [rx(100),ry(160)] )
        fenetre.blit( font2.render("Si vous touchez un mur, vous revenez au point de départ",20,(255,255,255)) , [rx(100),ry(190)] )
        fenetre.blit( font2.render("Il y aura du temps pour finir le niveau",20,(255,255,255)) , [rx(100),ry(220)] )
        fenetre.blit( font2.render("Le temps est représenté par une barre tout en haut de l'ecran",20,(255,255,255)) , [rx(120),ry(250)] )
        fenetre.blit( font2.render("A partir du niveau 10, vous débloquez le grapin",20,(255,255,255)) , [rx(120),ry(280)] )
        fenetre.blit( font2.render("Si vous terminez le niveau 100, vous avez fini le jeu",20,(255,255,255)) , [rx(100),ry(310)] )
        fenetre.blit( font2.render("Il y aura un ature cube qui vous suivra, s'il vous touche, vous perdrez de la vie.",20,(255,255,255)) , [rx(100),ry(340)] )
        fenetre.blit( font2.render("Vous pouvez quitter le jeu à tout moment en appuyant sur Echap",20,(255,255,255)) , [rx(100),ry(370)] )
        fenetre.blit( font2.render("Bonne chance !",20,(255,255,255)) , [rx(100),ry(400)] )
        btn=pygame.draw.rect(fenetre,(150,150,150),(rx(300),ry(500),rx(200),ry(75)),0)
        fenetre.blit( font4.render("Jouer",20,(255,255,255)) , [rx(350),ry(520)] )
        btn2=pygame.draw.rect(fenetre,(150,150,150),(rx(300),ry(600),rx(200),ry(75)),0)
        fenetre.blit( font4.render("quitter",20,(255,255,255)) , [rx(350),ry(620)] )
        btn3=pygame.draw.rect(fenetre,(200,200,200),(rx(50),ry(500),rx(100),ry(50)),0)
        fenetre.blit( font3.render("skins",20,(25,25,25)) , [rx(60),ry(510)] )
        btn6=pygame.draw.rect(fenetre,(200,200,200),(rx(50),ry(565),rx(200),ry(50)),0)
        fenetre.blit( font3.render("parametres",20,(25,25,25)) , [rx(60),ry(575)] )
    elif men==1:
        btn3=pygame.draw.rect(fenetre,(200,200,200),(rx(20),ry(20),rx(100),ry(50)),0)
        fenetre.blit( font3.render("retour",20,(25,25,25)) , [rx(30),ry(30)] )
        fenetre.blit( font3.render("skins possedes :",20,(250,250,250)) , [rx(20),ry(110)] )
        fenetre.blit( font3.render("skin équipé :",20,(250,250,250)) , [rx(200),ry(30)] )
        if skin_equipe>=0 and skin_equipe<len(skins_possedes) and skins_possedes[skin_equipe]>=0 and skins_possedes[skin_equipe]<len(skins):
            sk=skins_possedes[skin_equipe]
            sk=skins[sk]
            sk=sk[0][an]
            fenetre.blit( pygame.transform.scale(   pygame.image.load(dimg+skins[skins_possedes[skin_equipe]][0][an]) , [ry(150),ry(150)]) , [rx(430),ry(5)])
            pygame.draw.rect(fenetre,cl_raretes[skins[skins_possedes[skin_equipe]][1]],(rx(430),ry(5),ry(150),ry(150)),2)
            fenetre.blit( font3.render(raretes[skins[skins_possedes[skin_equipe]][1]],20,cl_raretes[skins[skins_possedes[skin_equipe]][1]]) , [rx(280),ry(100)] )
        pygame.draw.rect(fenetre,(50,50,50),(rx(50),ry(180),rx(750),ry(450)),0)
        xx,yy=rx(50),ry(180)
        tcx,tcy=ry(150),ry(150)
        for x in range(ps,ps+tpage):
            if x >= 0 and x < len(skins_possedes):
                s=skins_possedes[x]
                #img
                bts[skins_possedes.index(s)]=fenetre.blit( pygame.transform.scale(pygame.image.load(dimg+skins[s][0][0]),[tcx,tcy]) , [xx,yy] )
                pygame.draw.rect(fenetre,cl_raretes[skins[s][1]],(xx,yy,tcx,tcy),2)
                #coordonée image
                xx+=tcx
                if xx>=rx(750):
                    xx=rx(50)
                    yy+=tcy
        btn4=fenetre.blit( pygame.transform.scale(pygame.image.load(dimg+"f1.png"),[rx(50),ry(100)]) , [tex-rx(50),ry(300)])
        btn5=fenetre.blit( pygame.transform.scale(pygame.image.load(dimg+"f2.png"),[rx(50),ry(100)]) , [0,ry(300)])
        ms_com,ms_rar,ms_epi,ms_leg,ms_div=0,0,0,0,0
        for s in skins_possedes:
            if skins[s][1]==0: ms_com+=1
            elif skins[s][1]==1: ms_rar+=1
            elif skins[s][1]==2: ms_epi+=1
            elif skins[s][1]==3: ms_leg+=1
            else: ms_div+=1
        fenetre.blit( font2.render("skins communs : "+str(ms_com)+" / "+str(len(skins_com)),20,cl_raretes[0]) , [rx(620),ry(30)] )
        fenetre.blit( font2.render("skins rares : "+str(ms_rar)+" / "+str(len(skins_rar)),20,cl_raretes[1]) , [rx(620),ry(50)] )
        fenetre.blit( font2.render("skins épiques : "+str(ms_epi)+" / "+str(len(skins_epi)),20,cl_raretes[2]) , [rx(620),ry(70)] )
        fenetre.blit( font2.render("skins légendaires : "+str(ms_leg)+" / "+str(len(skins_leg)),20,cl_raretes[3]) , [rx(620),ry(90)] )
        fenetre.blit( font2.render("skins divins : "+str(ms_div)+" / "+str(len(skins_div)),20,cl_raretes[4]) , [rx(620),ry(110)] )
        fenetre.blit( font2.render("skins : "+str(len(skins_possedes))+" / "+str(len(skins)),20,(250,250,250)) , [rx(620),ry(130)] )
    elif men==2:
        btn6=pygame.draw.rect(fenetre,(200,200,200),(rx(15),ry(15),rx(100),ry(50)),0)
        fenetre.blit( font3.render("retour",20,(25,25,25)) , [rx(25),ry(25)] )
        cl=(150,0,0)
        if fullscreen: cl=(0,150,0)
        bst[0]=pygame.draw.rect( fenetre, cl , (rx(50),ry(250),rx(50),rx(50)) , 0)
        fenetre.blit( font3.render("fullscreen",True,(255,255,255)), [rx(120),ry(260)])
        cl=(150,0,0)
        if acchardware: cl=(0,150,0)
        bst[1]=pygame.draw.rect( fenetre, cl , (rx(50),ry(330),rx(50),rx(50)) , 0)
        fenetre.blit( font3.render("accelerated hardware",True,(255,255,255)), [rx(120),ry(340)]) 
        cl=(150,0,0)
        if doublebuf: cl=(0,150,0)
        bst[2]=pygame.draw.rect( fenetre, cl , (rx(50),ry(410),rx(50),rx(50)) , 0)
        fenetre.blit( font3.render("double buff",True,(255,255,255)), [rx(120),ry(420)])
        fenetre.blit( font3.render("résolution de la fenetre :",True,(255,255,255)), [rx(170),ry(40)])
        bst[3]=pygame.draw.rect( fenetre, (50,50,50), (rx(100),ry(100),rx(50),ry(50)) , 0)
        fenetre.blit( font3.render("<",True,(255,255,255)), [rx(110),ry(110)])
        pygame.draw.rect(fenetre,(210,210,210),(rx(180),ry(100),rx(300),ry(50)),0)
        fenetre.blit( font3.render(str(tex)+" x "+str(tey),True,(25,25,25)), [rx(190),ry(110)])
        bst[4]=pygame.draw.rect( fenetre, (50,50,50), (rx(510),ry(100),rx(50),ry(50)) , 0)
        fenetre.blit( font3.render(">",True,(255,255,255)), [rx(520),ry(110)])
        fenetre.blit( font2.render("Pour que les parametres s'appliquent, veuillez relancer le jeu",True,(150,0,0)), [rx(10),ry(500)])
    pygame.display.update()
    return btn,btn2,btn3,btn4,btn5,btn6,bts,bst

def menu(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf):
    men=0
    needtoaff=True
    ps=0
    an=0
    tan=0.1
    dan=time.time()
    encour=True
    while encour:
        if time.time()-dan>=tan and len(skins[skins_possedes[skin_equipe]][0])>1:
            dan=time.time()
            an+=1
            if an >= len(skins[skins_possedes[skin_equipe]][0]): an=0
            needtoaff=True
        if needtoaff:
            btn,btn2,btn3,btn4,btn5,btn6,bts,bst=aff_menu(men,skin_equipe,skins_possedes,ps,an,tex,tey,fullscreen,acchardware,doublebuf)
            needtoaff=False
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if btn!=None and btn.collidepoint(pos):
                    save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf)
                    skin_equipe,skins_possedes=main_jeu(skin_equipe,skins_possedes)
                    an=0
                    if skin_equipe>=len(skins_possedes): skin_equipe=0
                    save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf)
                elif btn2!=None and btn2.collidepoint(pos): exit()
                elif btn3!=None and btn3.collidepoint(pos):
                    if men==0: men=1
                    else: men=0
                    an=0
                elif btn4!=None and btn4.collidepoint(pos):
                    if len(skins_possedes)>ps+tpage:
                        ps+=tpage
                        an=0
                elif btn5!=None and btn5.collidepoint(pos):
                    if ps>=tpage:
                        ps-=tpage
                        an=0
                elif btn6!=None and btn6.collidepoint(pos):
                    if men==0: men=2
                    else: men=0
                    an=0
                for b in bts:
                    if b!=None and b.collidepoint(pos):
                        skin_equipe=skins_possedes.index(skins_possedes[bts.index(b)])
                        an=0
                for b in bst:
                    if b!=None and b.collidepoint(pos):
                        di=bst.index(b)
                        if di==0:
                            fullscreen=not fullscreen
                            if not fullscreen: tex,tey=int(mtex/1.5),int(mtey/1.5)
                            else: tex,tey=mtex,mtey
                        elif di==1: acchardware=not acchardware
                        elif di==2: doublebuf=not doublebuf
                        elif di==3:
                            d=float(mtex/tex)+0.5
                            if d > 3: d=3
                            tex,tey=int(mtex/d),int(mtey/d)
                        elif di==4:
                            d=float(mtex/tex)-0.5
                            if d < 1: d=1
                            tex,tey=int(mtex/d),int(mtey/d)
                        save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf)
                needtoaff=True

#ry:
if True:
    menu(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf)
#except Exception as e:
else:
    pygame.quit()
    if e!="name 'exit' is not defined":
        print(e)
        input("please send this at : nathpython@gmail.com")

