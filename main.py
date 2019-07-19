#coding:utf-8
import random,pygame,time,numpy
from pygame.locals import *

pygame.init()
btex,btey=1280/1.5,1024/1.5
io = pygame.display.Info()
mtex,mtey=io.current_w,io.current_h
tex,tey=int(mtex/1.5),int(mtey/1.5)

def rx(x): return int(x/btex*tex)
def ry(y): return int(y/btey*tey)

fenetre=pygame.display.set_mode([tex,tey])
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

class Mape:
    def __init__(self,niv):
        dif=int(float(niv)/100.*10.)+1
        self.tx=100*dif
        self.ty=100*dif
        self.clm=rcl()
        self.cls=(255-self.clm[0],255-self.clm[1],255-self.clm[2])
        self.mape=numpy.zeros([self.tx,self.ty],dtype=int)
        self.chem=[[random.randint(0,self.tx-1),random.randint(0,self.ty-1)]]
        self.deb=self.chem[0]
        nbbranches=dif
        for y in range(nbbranches):
            self.chem.append( self.deb ) 
            for x in range(random.randint(200*dif,1100*dif)):
                c=self.chem[len(self.chem)-1]
                ax,ay=0,0
                if random.randint(0,1)==1: ax=random.randint(-1,1)
                else: ay=random.randint(-1,1)
                cx,cy=c[0]+ax,c[1]+ay
                if cx < 0: cx=0
                elif cx > self.tx-1: cx=self.tx-1
                if cy < 0: cy=0
                elif cy > self.ty-1: cy=self.ty-1
                self.chem.append([cx,cy])
        self.fin=self.chem[len(self.chem)-1]
        for x in range(self.tx):
            for y in range(self.ty):
                if [x,y] in self.chem:
                    if [x,y]!=self.deb and [x,y]!=self.fin and random.randint(1,30-dif)==1: self.mape[x,y]=2 #piege clignotant
                    else:self.mape[x,y]=0 #sol
                else: self.mape[x,y]=1 #mur
        self.p1=False
        self.dp1=time.time()
        self.tp1=1.5
    def update(self):
        if time.time()-self.dp1>=self.tp1:
            self.p1=not self.p1
            self.dp1=time.time()

class Cube:
    def __init__(self,tc,mape):
        self.px=mape.chem[0][0]*tc+tc/10
        self.py=mape.chem[0][1]*tc+tc/10
        self.tx=int(tc/3)
        self.ty=int(tc/3)
        self.cl=(255,255,255)
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.dbg=time.time()
        self.tbg=0.01
        self.vitx=0.
        self.vity=0.
        self.acc=0.1
        self.decc=0.01
        self.vitmax=5
        self.dk=time.time()
        self.tk=0.01
        self.checkpoint=[self.px,self.py]
    def bouger(self,aa):
        if time.time()-self.dk >= self.tk:
            self.dk=time.time()
            if aa=="up": self.vity-=self.acc
            elif aa=="down": self.vity+=self.acc
            elif aa=="left": self.vitx-=self.acc
            elif aa=="right": self.vitx+=self.acc
    def update(self,mape,tc):
        if time.time()-self.dbg>=self.tbg:
            self.dbg=time.time()
            #deplacements
            if self.vitx>self.vitmax: self.vitx=self.vitmax
            if self.vitx<-self.vitmax: self.vitx=-self.vitmax
            if self.vity>self.vitmax: self.vity=self.vitmax
            if self.vity<-self.vitmax: self.vity=-self.vitmax
            self.px+=self.vitx
            self.py+=self.vity
            #collisions
            self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
            for x in range( int((self.px)/tc)-2 , int((self.px)/tc)+2 ):
                for y in range( int((self.py)/tc)-2 , int((self.py)/tc)+2 ):
                    if x >= 0 and x < mape.tx and y >= 0 and y < mape.ty and self.rect.colliderect( pygame.Rect(x*tc,y*tc,tc,tc) ):
                        if mape.mape[x,y]==1: return False
                        if mape.mape[x,y]==2 and mape.p1: return False
                        if mape.fin==[x,y]: return True
            if self.px<0: return False
            if self.px+self.tx>mape.tx*tc: return False
            if self.py<0: return False
            if self.py+self.ty>mape.ty*tc: return False
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
                        
def verif_keys(cube):
    keys=pygame.key.get_pressed()
    if keys[K_UP]: cube.bouger("up")
    if keys[K_DOWN]: cube.bouger("down")
    if keys[K_LEFT]: cube.bouger("left")
    if keys[K_RIGHT]: cube.bouger("right")
    if nb_joysticks > 0:
        #haut-bas
        aa=float(mon_joystick.get_axis(1))
        if aa > 0.5: aa=1
        elif aa < -0.5 : aa=-1
        else: aa=0 
        if aa==-1: cube.bouger("up")
        if aa==1: cube.bouger("down")
        #haut-bas
        aa=float(mon_joystick.get_axis(0))
        if aa > 0.5: aa=1
        elif aa < -0.5 : aa=-1
        else: aa=0 
        if aa==-1: cube.bouger("left")
        if aa==1: cube.bouger("right")
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

def aff(cube,mape,cam,tc,fps,niv,morts):
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
    pygame.draw.rect(fenetre,cube.cl,(cam[0]+cube.px,cam[1]+cube.py,cube.tx,cube.ty),0)
    fenetre.blit( font1.render("fps : "+str(fps),20,(255,255,255)), [rx(15),ry(15)] )
    fenetre.blit( font1.render("lvl : "+str(niv),20,(255,255,255)), [tex-rx(100),ry(25)] )
    fenetre.blit( font1.render("vous êtes mort : "+str(morts)+" fois",20,(255,255,255)), [tex-rx(200),ry(10)] )
    pygame.display.update()

def cniv(tc,niv):
    mape=Mape(niv)
    cube=Cube(tc,mape)
    cam=[-cube.px+tex/2,-cube.py+tey/2]
    return mape,cube,cam

def main_jeu():
    tc=rx(100)
    niv=1
    ecran_chargement()
    mape,cube,cam=cniv(tc,niv)
    encour_g=True
    morts=0
    fps=0
    while encour_g:
        t1=time.time()
        #cube
        cube=verif_keys(cube)
        etat=cube.update(mape,tc)
        if etat==False:
            morts+=1
            if morts>=100:
                encour=False
                ecran_mort()
                break
            else:
                cube.px=cube.checkpoint[0]
                cube.py=cube.checkpoint[1]
                cube.vitx,cube.vity=0,0
        elif etat==True:
            if niv<100:
                niv+=1
                ecran_chargement()
                mape,cube,cam=cniv(tc,niv)
            else:
                encour_g=False
                ecran_fin()
        cam=[-cube.px+tex/2,-cube.py+tey/2]
        #mape
        mape.update()
        #aff
        aff(cube,mape,cam,tc,fps,niv,morts)
        #event
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    encour_g=False
                    ecran_quit()
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
        t2=time.time()
        tt=t2-t1
        if tt!=0: fps=int(1./tt)

def aff_menu():
    fenetre.fill((0,0,0))
    fenetre.blit( font5.render("Cube2",20,(255,255,255)) , [rx(300),ry(10)] )
    fenetre.blit( font2.render("Le but de ce jeu est de trouver la sortie de chaque niveau",20,(255,255,255)) , [rx(100),ry(100)] )
    fenetre.blit( font2.render("La sortie d'un niveau est représentée par un carré noir",20,(255,255,255)) , [rx(100),ry(130)] )
    fenetre.blit( font2.render("Vous dirigez un carré blanc avec les flèches du clavier",20,(255,255,255)) , [rx(100),ry(160)] )
    fenetre.blit( font2.render("Si vous touchez un mur, vous revenez au point de départ",20,(255,255,255)) , [rx(100),ry(190)] )
    fenetre.blit( font2.render("Il y a des pièges qui clignotent:",20,(255,255,255)) , [rx(100),ry(220)] )
    fenetre.blit( font2.render("Si il est vert, vous pouvez passer dessus",20,(255,255,255)) , [rx(120),ry(250)] )
    fenetre.blit( font2.render("Si il est rouger, vous mourrez",20,(255,255,255)) , [rx(120),ry(280)] )
    fenetre.blit( font2.render("Si vous terminez le niveau 100, vous avez fini le jeu",20,(255,255,255)) , [rx(100),ry(310)] )
    fenetre.blit( font2.render("Par contre, si vous mourrez 100 fois, vous perdez la partie",20,(255,255,255)) , [rx(100),ry(340)] )
    fenetre.blit( font2.render("Vous pouvez quitter le jeu à tout moment en appuyant sur Echap",20,(255,255,255)) , [rx(100),ry(370)] )
    fenetre.blit( font2.render("Bonne chance !",20,(255,255,255)) , [rx(100),ry(400)] )
    btn=pygame.draw.rect(fenetre,(150,150,150),(rx(300),ry(500),rx(200),ry(75)),0)
    fenetre.blit( font4.render("Jouer",20,(255,255,255)) , [rx(350),ry(520)] )
    btn2=pygame.draw.rect(fenetre,(150,150,150),(rx(300),ry(600),rx(200),ry(75)),0)
    fenetre.blit( font4.render("quitter",20,(255,255,255)) , [rx(350),ry(620)] )
    pygame.display.update()
    return btn,btn2

def menu():
    btn,btn2=aff_menu()
    encour=True
    while encour:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if btn.collidepoint(pos):
                    main_jeu()
                    btn,btn2=aff_menu()
                elif btn2.collidepoint(pos): exit()

menu()

