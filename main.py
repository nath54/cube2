#coding:utf-8
#on importe les librairies
import random,pygame,time,numpy,math,os
from pygame.locals import *
from os.path import expanduser

#on initialise les variables de base
pygame.init()
btex,btey=1280/1.5,1024/1.5
io = pygame.display.Info()
mtex,mtey=io.current_w,io.current_h
tex,tey=int(mtex/1.5),int(mtey/1.5)
fullscreen=False
acchardware=False
doublebuf=False

#emplacement du dossier des images
dimg="images/"

#images des skins, les skins
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

#fonction qui est appelée lorqu'un succes est débloqué
def new_succes(s,liste_succes):
    print("Nouveau Succès Débloqué : "+str(s[0]))
    print("   -"+str(s[1]))
    liste_succes.append( [s[0],s[1],3,time.time()] )
    return liste_succes

#classe des succes
class Succes:
    def __init__(self):
        self.s1=["Première Partie"                     ,"A joué 1 partie"                                                  ,False,"nbp"   ,">=" ,1          ]
        self.s2=["Le début d'une grande aventure"      ,"A joué 10 parties"                                                ,False,"nbpb"  ,">=" ,10         ]
        self.s3=["Vétérand"                            ,"A joué 100 parties"                                               ,False,"nbpb"  ,">=" ,100        ]
        self.s4=["Courageux"                           ,"A joué 1000 parties"                                              ,False,"nbpb"  ,">=" ,1000       ]
        self.s5=["Suicidaire"                          ,"A joué 10000 parties"                                             ,False,"nbpb"  ,">=" ,10000      ]
        self.s6=["Niveau bronze"                       ,"Est déja arrivé au niveau 10"                                     ,False,"cniv"  ,">=" ,10         ]
        self.s7=["Niveau argent"                       ,"Est déjà arrivé au niveau 20"                                     ,False,"cniv"  ,">=" ,20         ]
        self.s8=["Niveau or"                           ,"Est déjà arrivé au niveau 40"                                     ,False,"cniv"  ,">=" ,40         ]
        self.s9=["Niveau diamant"                      ,"Est déjà arrivé au niveau 70"                                     ,False,"cniv"  ,">=" ,70         ]
        self.s10=["Niveau platinium"                   ,"Est déjà arrivé au niveau 95"                                     ,False,"cniv"  ,">=" ,95         ]
        self.s11=["Vous êtes divins !"                 ,"A déjà réussit à gagner une partie (niv 100)"                     ,False,"cniv"  ,">=" ,100        ]
        self.s12=["Première mort"                      ,"Est déjà mort 1 fois (mais avec un minimum de déplacement)"       ,False,"bmor"  ,">=" ,1          ]
        self.s13=["Habitué à mourir"                   ,"Est déjà mort 100 fois (mais avec un minimum de déplacement)"     ,False,"bmor"  ,">=" ,100        ]
        self.s14=["Pluie de morts"                     ,"Est déjà mort 1000 fois (mais avec un minimum de déplacement)"    ,False,"bmor"  ,">=" ,1000       ]
        self.s15=["Cimetière"                          ,"Est déjà mort 10000 fois (mais avec un minimum de déplacement)"   ,False,"bmor"  ,">=" ,10000      ]
        self.s16=["Hécatombe"                          ,"Est déjà mort 100000 fois (mais avec un minimum de déplacement)"  ,False,"bmor"  ,">=" ,100000     ]
        self.s17=["Petit collectionneur"               ,"Possède 10 skins"                                                 ,False,"nbsk"  ,">=" ,10         ]
        self.s18=["Collectionneur affirmé"             ,"Possède 40 skins"                                                 ,False,"nbsk"  ,">=" ,40         ]
        self.s19=["Collectionneur complet"             ,"Possède tous les skins"                                           ,False,"nbsk"  ,">=" ,len(skins) ]
        self.s20=["Premiers pas"                       ,"A parcouru une distance de 100.000 pixels"                        ,False,"distt" ,">=" ,100000     ]
        self.s21=["Voyageur"                           ,"A parcouru une distance de 10.000.000 pixels"                     ,False,"distt" ,">=" ,10000000   ]
        self.s22=["Grand Voyageur"                     ,"A parcouru une distance de 100.000.000 pixels"                    ,False,"distt" ,">=" ,100000000  ]
        self.s23=["GlobeTrotter"                       ,"A parcouru une distance de 1.000.000.000 pixels"                  ,False,"distt" ,">=" ,1000000000 ]
        self.nbparties=0
        self.nbpartiesbons=0
        self.niveau_max=0
        self.distance_parcourue=0
        self.mort_avec_dist_min=0
        self.succes=[self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.s10,self.s11,self.s12,self.s13,self.s14,self.s15,self.s16,self.s17,self.s18,self.s19,self.s20,self.s21,self.s22,self.s23]
    def test_succes(self,cube,niv,skins_possedes,liste_succes):
        for s in self.succes:
            if not s[2]:
                v=0
                cond=False
                if s[3]=="nbp":
                    v=self.nbparties
                elif s[3]=="nbpb":
                    v=self.nbpartiesbons
                elif s[3]=="cniv":
                    v=niv
                elif s[3]=="bmor":
                    v=self.mort_avec_dist_min
                elif s[3]=="nbsk":
                    v=len(skins_possedes)
                elif s[3]=="distt":
                    if cube!=None:
                        v=cube.dist_parc+self.distance_parcourue
                    else:
                        v=self.distance_parcourue
                if s[4]==">=":
                    cond=v>=s[5]
                elif s[4]==">":
                    cond=v>s[5]
                elif s[4]=="==":
                    cond=v==s[5]
                elif s[4]=="<=":
                    cond=v<=s[5]
                elif s[4]=="<":
                    cond=v<s[5]
                elif s[4]=="!=":
                    cond=s[5]!=v
                if cond:
                    s[2]=True
                    liste_succes=new_succes(s,liste_succes)
        return liste_succes

#on crée la classe succes
succes=Succes()

#variable de séparations des fichiers de sauvegarde
cac="|"
cacc="#"
ccac="@"

#on cherche le dossier home
home = expanduser("~")
dre="Cube2/"
#si le dossier "Cube2" n'est pas présent dans le home du joueur, on le crée
if not dre[:-1] in os.listdir(home): os.mkdir(home+"/"+dre)
#variable du dossier de sauvegarde
dire=home+"/"+dre

#variable du nom de la sauvegarde
dfs="save.nath"
#si il n'y a pas de sauvegarde présente, on la crée
if not dfs in os.listdir(dire):
    txt=""
    txt+=str(0)+cac #skin equipé
    txt+=str(0)+cac #skins possedés
    txt+=str(tex)+cac+str(tey)+cac #resolution de l'ecran
    txt+=str(0)+cac #fullscreen 0=False 1=True
    txt+=str(0)+cac #accelerated hardware 0=False 1=True
    txt+=str(0)+cac #double buffering 0=False 1=True
    for s in succes.succes: #succes faits ou pas
        txt+=str(0)+cacc #0=False 1=True
    txt=txt[:-1]+cac
    txt+=str(0)+cac #nbparties
    txt+=str(0)+cac #nbpartiesbon
    txt+=str(0)+cac #niv max atteint
    txt+=str(0)+cac #dist parcourue
    txt+=str(0) #morts avec dist min
    
    f=open(dire+dfs,"w")
    f.write(txt)
    f.close()

#variables des skins possédés et équipés
skins_possedes=[]
skin_equipe=0

successes=[]
#nombre de succès affiché en 1 page de succès
nbspp=6

#on load le jeu :
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
if len(f)>7:  successes=f[7].split(cacc)

for xs in range(len(successes)):
    et=False
    if successes[xs].strip()=="1": et=True
    succes.succes[xs][2]=et

if len(f)>8: succes.nbparties=int(f[8])
if len(f)>9: succes.nbpartiesbons=int(f[9])
if len(f)>10: succes.niveau_max=int(f[10])
if len(f)>11: succes.distance_parcourue=float(f[11])
if len(f)>12: succes.mort_avec_dist_min=int(f[12])


#fonction relatives a la résolution de l'ecran du joueur
def rx(x): return int(x/btex*tex)
def ry(y): return int(y/btey*tey)

def rxx(x): return float(float(x)/float(btex)*float(tex))
def ryy(y): return float(float(y)/float(btey)*float(tey))

#options
options=0
if fullscreen: options|=pygame.FULLSCREEN
if acchardware: options|=pygame.HWSURFACE
if doublebuf: options|=pygame.DOUBLEBUF

#creation de la fenetre
fenetre=pygame.display.set_mode([tex,tey],options)
pygame.display.set_caption("Cube2")
font1=pygame.font.SysFont("Arial",ry(17))
font2=pygame.font.SysFont("Arial",ry(20))
font3=pygame.font.SysFont("Arial",ry(30))
font4=pygame.font.SysFont("Arial",ry(40))
font5=pygame.font.SysFont("Serif",ry(60))

#creation curseur
cursor1,mask1=pygame.cursors.compile(("XXXXXXXXXXXXXXXX","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","X..............X","XXXXXXXXXXXXXXXX"), black='X', white='.', xor='o')
cursor_sizer1=((16,16),(9,8),cursor1,mask1)
pygame.mouse.set_cursor(*cursor_sizer1)

#creation joystick
mon_joystick="joystick"
nb_joysticks = pygame.joystick.get_count()
if nb_joysticks > 0:
	mon_joystick = pygame.joystick.Joystick(0)
	mon_joystick.init()

#fonction couleur aléattoire
def rcl(): return (random.randint(50,200),random.randint(50,100),random.randint(50,200))

tpage=int((rx(750)/ry(150))*3)

#gestion des skins
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

#fonction aff_succes
def aff_succes(liste_succes):
    n=1
    for s in liste_succes:
        pygame.draw.rect( fenetre , (70,70,70) , ( tex-rxx(350) , tey-(ryy(70)*n) , rx(350) , ry(70) ) , 0)
        fenetre.blit( font2.render("Nouveau succès débloqué : ",True,(230,230,230)) , (tex-rx(345),tey-(ry(70)*n)+ry(2)) )
        fenetre.blit( font2.render(s[0],True,(255,255,255)) , (tex-rx(340),tey-(ry(70)*n)+ry(20)) )
        fenetre.blit( font1.render(s[1],True,(200,200,200)) , (tex-rx(330),tey-(ry(70)*n)+ry(45)) )
        n+=1

#fonction save
def save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf,succes):
    txt=str(skin_equipe)+cac
    for s in skins_possedes:
        txt+=str(s)+cacc
    txt=txt[:-1]+cac
    txt+=str(tex)+cac+str(tey)+cac
    fs="0"
    if fullscreen: fs="1"
    txt+=fs+cac
    ah="0"
    if acchardware: ah="1"
    txt+=ah+cac
    db="0"
    if doublebuf: db="1"
    txt+=db+cac
    for s in succes.succes:
        v="0"
        if s[2]: v="1"
        txt+=v+cacc
    txt=txt[:-1]+cac
    txt+=str(succes.nbparties)+cac
    txt+=str(succes.nbpartiesbons)+cac
    txt+=str(succes.niveau_max)+cac
    txt+=str(succes.distance_parcourue)+cac
    txt+=str(succes.mort_avec_dist_min)
    
    f=open(dire+dfs,"w")
    f.write(txt)
    f.close()

#classe de la mape
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

#class du cube2 (celui qui suit le perso)
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
        self.dist_parc=0
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
            apx,apy=self.px,self.py
            self.px,self.py=self.keys[0]
            self.dist_parc+=math.sqrt( (self.px-apx)**2 + (self.py-apy)**2 )
            self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
            del(self.keys[0])

#classe du cube (le perso principal)
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
        self.dist_parc=0
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
            self.dist_parc+=math.sqrt(self.vitx**2+self.vity**2)
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

#fonction qui verifie et gere les inputs          
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

#fonction ecran de chargement
def ecran_chargement():
    fenetre.fill((0,0,0))
    fenetre.blit( font4.render("chargement...",True,(255,255,255)) , [tex/3,tey/3])
    pygame.display.update()

#fonction debloque_grappin(grappin débloqué)
def ecran_grappin():
    fenetre.fill((0,0,0))
    fenetre.blit( font3.render("Vous avez débloqué le Grappin",True,(255,255,255)) , [rx(200),ry(250)])
    fenetre.blit( font2.render("Pour l'utiliser, il suffit de cliquer à l'endroit où vous voulez aller",True,(255,255,255)) , [rx(100),ry(300)])
    fenetre.blit( font2.render("Mais faites attention à ce qu'il n'y ai pas un mur entre vous et la destination",True,(255,255,255)) , [rx(100),ry(400)])
    fenetre.blit( font2.render("Il vous faudra attendre 3 secondes entre chaque utilisation",True,(255,255,255)) , [rx(100),ry(500)])
    pygame.display.update()
    encour_f=True
    while encour_f:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE: encour_f=False

#fonction ecran de fin(partie finie)
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

#fonction ecran de mort(partie perdue)
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

#fonction ecran de quittage de partie(le joueur quitte sa partie)
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
    

#fonction qui montre la carte du niveau
def ecran_dep_lvl(mape,liste_succes):
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
    for l in liste_succes:
        l[3]=time.time()
    return liste_succes

#fonction affichage du jeu
def aff(cube,mape,cam,tc,fps,niv,morts,cube2,tps1,tpstot,liste_succes):
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
    aff_succes(liste_succes)
    pygame.display.update()

#fonction qui crée un niveau
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

#fonction main jeu
def main_jeu(skin_equipe,skins_possedes,liste_succes,succes):
    mbp=False
    succes.nbparties+=1
    tcb=rx(100)
    niv=1
    ecran_chargement()
    mape,cube,cam,cube2,tps1,tpstot,tc=cniv(tcb,niv,skin_equipe,skins_possedes)
    liste_succes=ecran_dep_lvl(mape,liste_succes)
    cube2.reload(cube)
    encour_g=True
    morts=0
    fps=0
    succes.test_succes(cube,niv,skins_possedes,liste_succes)
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
            if cube.dist_parc>=200:
                succes.mort_avec_dist_min+=1
                print("Mort")
            succes.distance_parcourue+=cube.dist_parc
            cube.dist_parc=0
            cube.px=cube.checkpoint[0]
            cube.py=cube.checkpoint[1]
            cube.vitx,cube.vity=0,0
            cube.isgrap=False
            cube.dist_parc=0
            time.sleep(0.1)
            cube2.reload(cube)
            succes.test_succes(cube,niv,skins_possedes,liste_succes)
        elif etat==True:
            if niv>=3 and not mbp:
                succes.nbpartiesbons+=1
                mpb=True
            if niv==9:
                ecran_grappin()
            if niv<100:
                niv+=1
                succes.distance_parcourue+=cube2.dist_parc
                cube2.dist_parc=0
                ecran_chargement()
                mape,cube,cam,cube2,tps1,tpstot,tc=cniv(tcb,niv,skin_equipe,skins_possedes)
                liste_succes=ecran_dep_lvl(mape,liste_succes)
                cube2.reload(cube)
                succes.test_succes(cube,niv,skins_possedes,liste_succes)
            else:
                encour_g=False
                succes.distance_parcourue+=cube2.dist_parc
                cube2.dist_parc=0
                succes.test_succes(cube,niv,skins_possedes,liste_succes)
                ecran_fin()
        if time.time()-tps1>=tpstot:
            encour=False
            perdu=True
            succes.distance_parcourue+=cube2.dist_parc
            cube2.dist_parc=0
            if niv>=3 and not mbp: succes.nbpartiesbons,mbp=succes.nbpartiesbons+1,True
            succes.test_succes(cube,niv,skins_possedes,liste_succes)
            ecran_mort()
            break
        #gestion succes aff
        for s in liste_succes:
            if time.time()-s[3]>=s[2]:
                del(liste_succes[liste_succes.index(s)])
        cam=[-cube.px+tex/2,-cube.py+tey/2]
        #mape
        mape.update()
        #aff
        aff(cube,mape,cam,tc,fps,niv,morts,cube2,tps1,tpstot,liste_succes)
        #event
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    encour_g=False
                    ecran_quit()
                elif event.key==K_n:
                    tpstot/=2
                    liste_succes=ecran_dep_lvl(mape,liste_succes)
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
    succes.test_succes(cube,niv,skins_possedes,liste_succes)
    return skin_equipe,skins_possedes,liste_succes

#fonction affichage du menu
def aff_menu(men,skin_equipe,skins_possedes,ps,an,tex,tey,fullscreen,acchardware,doublebuf,liste_succes,succes,pscs):
    btn,btn2,btn3,btn4,btn5,btn6,bts1,bts2,btn7=None,None,None,None,None,None,None,None,None
    bts=[]
    for x in range(3*(tpage+1)): bts.append( None )
    bst=[]
    for x in range(10): bst.append( None )
    fenetre.fill((0,0,0))
    if men==0: #main
        fenetre.blit( font5.render("Cube2",20,(255,255,255)) , [rx(300),ry(10)] )
        fenetre.blit( font2.render("Le but de ce jeu est de trouver la sortie de chaque niveau",20,(255,255,255)) , [rx(100),ry(100)] )
        fenetre.blit( font2.render("La sortie d'un niveau est représentée par un carré noir",20,(255,255,255)) , [rx(100),ry(130)] )
        fenetre.blit( font2.render("Vous dirigez un carré blanc avec les flèches du clavier",20,(255,255,255)) , [rx(100),ry(160)] )
        fenetre.blit( font2.render("Si vous touchez un mur, vous revenez au point de départ",20,(255,255,255)) , [rx(100),ry(190)] )
        fenetre.blit( font2.render("Il y aura du temps pour finir le niveau",20,(255,255,255)) , [rx(100),ry(220)] )
        fenetre.blit( font2.render("Le temps est représenté par une barre tout en haut de l'ecran",20,(255,255,255)) , [rx(120),ry(250)] )
        fenetre.blit( font2.render("A partir du niveau 10, vous débloquez le grapin",20,(255,255,255)) , [rx(120),ry(280)] )
        fenetre.blit( font2.render("Si vous terminez le niveau 100, vous avez fini le jeu",20,(255,255,255)) , [rx(100),ry(310)] )
        fenetre.blit( font2.render("Il y aura un autre cube qui vous suivra, s'il vous touche, vous perdrez de la vie.",20,(255,255,255)) , [rx(100),ry(340)] )
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
        btn7=pygame.draw.rect(fenetre,(200,200,200),(rx(50),ry(435),rx(200),ry(50)),0)
        fenetre.blit( font3.render("Succes",20,(25,25,25)) , [rx(60),ry(445)] )
    elif men==1: #skins
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
    elif men==2: #parametres
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
    elif men==3: #succes
        btn3=pygame.draw.rect(fenetre,(200,200,200),(rx(20),ry(20),rx(100),ry(50)),0)
        fenetre.blit( font3.render("retour",20,(25,25,25)) , [rx(30),ry(30)] )
        n=0
        x=0   
        for s in succes.succes:
            n+=1
            if n>=pscs and n<=pscs+nbspp-1:
                pygame.draw.rect(fenetre,(200,200,200),(rx(100),ry(100)+x*ry(80),rx(650),ry(70)),0)
                fenetre.blit( font2.render("Succes N°"+str(n)+" : "+s[0],True,(0,0,0)) , (rx(120),ry(120)+x*ry(80)) )
                fenetre.blit( font1.render(s[1],True,(20,20,20)) , (rx(130),ry(140)+x*ry(80)) )
                if s[2]:
                    fenetre.blit( font2.render("Complété.",True,(0,255,0)) , (rx(600),ry(110)+x*ry(80)) )
                else:
                    v=0
                    if s[3]=="nbp":     v=succes.nbparties
                    elif s[3]=="nbpb":  v=succes.nbpartiesbons
                    elif s[3]=="cniv":  v=succes.niveau_max
                    elif s[3]=="bmor":  v=succes.mort_avec_dist_min
                    elif s[3]=="nbsk":  v=len(skins_possedes)
                    elif s[3]=="distt": v=succes.distance_parcourue
                    if s[4]==">=":
                        pc=((v/s[5]))
                        if pc>1: pc=1
                        cl=(int(255-pc*255),int(pc*255),0)
                        fenetre.blit( font2.render("Non débloqué",True,cl) , (rx(600),ry(110)+x*ry(80)) )
                        fenetre.blit( font1.render(str(pc*100.)[:5]+"%",True,cl) , (rx(600),ry(130)+x*ry(80)) )
                        pygame.draw.rect( fenetre , cl , (rx(600),ry(150)+x*ry(80),int(pc*rx(100)),ry(10) ) , 0 )
                        pygame.draw.rect( fenetre , (0,0,0) , (rx(600),ry(150)+x*ry(80),rx(100),ry(10) ) , rx(2) )
                x+=1
        ln=len(succes.succes)
        tty=ry(500)
        a=int(ln/nbspp*tty)
        pygame.draw.rect( fenetre , (150,150,150) , (tex-rx(50),ry(100),rx(30),tty) , 0 )
        pygame.draw.rect( fenetre , (50,50,50) , (tex-rx(50),ry(100)+int(ry(400)*len(succes.succes)/nbspp),rx(30),int(ry(400)*nbspp/n)) , 0 )
        bts1=pygame.draw.rect( fenetre , (250,250,250) , (tex-rx(50),ry(10),rx(30),ry(30)) , 0)
        pygame.draw.rect( fenetre , (0,0,0) , (tex-rx(50),ry(10),rx(30),ry(30)) , rx(2))
        fenetre.blit( font2.render("^",True,(20,20,20)) , (tex-rx(45),ry(20)) )
        bts2=pygame.draw.rect( fenetre , (250,250,250) , (tex-rx(50),tey-ry(50),rx(30),ry(30)) , 0)
        pygame.draw.rect( fenetre , (0,0,0) , (tex-rx(50),tey-ry(50),rx(30),ry(30)) , rx(2))
        fenetre.blit( font1.render("v",True,(20,20,20)) , (tex-rx(45),tey-ry(40)) )
    aff_succes(liste_succes)
    pygame.display.update()
    return btn,btn2,btn3,btn4,btn5,btn6,bts,bst,bts1,bts2,btn7

#fonction du menu
def menu(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf,succes):
    cube=None
    niv=0
    pscs=1
    ps=0
    an=0
    men=0
    tan=0.1
    encour=True
    needtoaff=True
    dan=time.time()
    liste_succes=[]
    while encour:
        if time.time()-dan>=tan and len(skins[skins_possedes[skin_equipe]][0])>1:
            dan=time.time()
            an+=1
            if an >= len(skins[skins_possedes[skin_equipe]][0]): an=0
            needtoaff=True
        if needtoaff:
            succes.test_succes(cube,niv,skins_possedes,liste_succes)
            btn,btn2,btn3,btn4,btn5,btn6,bts,bst,bts1,bts2,btn7=aff_menu(men,skin_equipe,skins_possedes,ps,an,tex,tey,fullscreen,acchardware,doublebuf,liste_succes,succes,pscs)
            needtoaff=False
        for s in liste_succes:
            if time.time()-s[3]>=s[2]:
                del(liste_succes[liste_succes.index(s)])
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour=False
                elif event.key==K_UP and men==3:
                    if pscs>1: pscs-=1
                elif event.key==K_DOWN and men==3:
                    if pscs<len(succes.succes)-1: pscs+=1
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if btn!=None and btn.collidepoint(pos):
                    save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf,succes)
                    skin_equipe,skins_possedes,liste_succes=main_jeu(skin_equipe,skins_possedes,liste_succes,succes)
                    an=0
                    if skin_equipe>=len(skins_possedes): skin_equipe=0
                    save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf,succes)
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
                elif bts1!=None and bts1.collidepoint(pos):
                    pscs-=nbspp
                    if pscs<1: pscs=1
                    an=0
                elif bts2!=None and bts2.collidepoint(pos):
                    pscs+=nbspp
                    if pscs>len(succes.succes): pscs=len(succes.succes)
                    an=0
                elif btn7!=None and btn7.collidepoint(pos):
                    if men==0: men=3
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
                        save(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf,succes)
                needtoaff=True

#ON LANCE LE JEU ICI :

#try:
if True:
    menu(skin_equipe,skins_possedes,tex,tey,fullscreen,acchardware,doublebuf,succes)
#except Exception as e:
else:
    pygame.quit()
    if e!="name 'exit' is not defined":
        print(e)
        input("please send this at : nathpython@gmail.com")

