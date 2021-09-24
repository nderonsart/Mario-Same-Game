# Module vue.py du projet Same réalisé par Nicolas Deronsart 


import modele
import tkinter
import pygame
import time


# La classe VueSame

class VueSame:
    ''' Classe VueSame qui défini et met en place l'interface graphique du jeu Same '''
    
    def __init__(self,same=modele.ModeleSame()):
        ''' Constructeur de la classe VueSame qui crée l'interface graphique du jeux
                
                Arguments : la classe VueSame et une instance de la classe ModeleSame same
        '''
        
        nouveau_jeu.play()
        
        
        self.__same=same
        
        
        self.__fenetre=tkinter.Tk()
        self.__fenetre.title('Super Mario SameGame')
        
        
        musique.play(-1)
        
        
        self.__images=[]
        self.__images_noires=[]
        for i in range(1,self.__same.nbcouleurs()+1):
            self.__images.append(tkinter.PhotoImage(file='img/sphere'+str(i)+'.gif'))
            self.__images_noires.append(tkinter.PhotoImage(file='img/sphere'+str(i)+'black.gif'))
        self.__images.append(tkinter.PhotoImage(file='img/spherevide.gif'))

        
        self.__les_btns=[]
        for i in range(self.__same.nblig()):
            ligne=[]
            for j in range(self.__same.nbcol()):
                couleur_sphere=self.__same.couleur(i,j)
                if couleur_sphere==-1:
                    ligne.append(tkinter.Button(self.__fenetre,image=self.__images[self.__same.nbcouleurs()]))
                    ligne[j].grid(row=i,column=j)
                else:
                    ligne.append(tkinter.Button(self.__fenetre,image=self.__images[couleur_sphere],command=self.creer_controleur_btn(i,j)))
                    ligne[j].bind('<Motion>',self.arrivee_curseur(i,j))
                    ligne[j].bind('<Leave>',self.depart_curseur(i,j))
                    ligne[j].grid(row=i,column=j)
            self.__les_btns.append(ligne)
        
        
        image_score=tkinter.PhotoImage(file='img/score.gif')
        score_affichage=tkinter.Label(self.__fenetre,image=image_score).grid(row=0,column=self.__same.nbcol())
        score=tkinter.Label(self.__fenetre,text=str(self.__same.score()),width=15,font=200).grid(row=0,column=self.__same.nbcol()+1)
        
        image_ajout=tkinter.PhotoImage(file='img/cubepoint.gif')
        ajout=tkinter.Label(self.__fenetre,image=image_ajout).grid(row=1,column=self.__same.nbcol())
        
        image_quitter=tkinter.PhotoImage(file='img/quitter.gif')
        quitter=tkinter.Button(self.__fenetre,image=image_quitter,command=self.__fenetre.destroy).grid(row=self.__same.nblig()-2,column=self.__same.nbcol()+1)
        
        image_tuyau=tkinter.PhotoImage(file='img/tuyau.gif')
        nouveau=tkinter.Button(self.__fenetre,image=image_tuyau,command=self.nouvelle_partie).grid(row=self.__same.nblig(),column=self.__same.nbcol()+1)
        
        
        
        self.__bonus_indice=5    
        self.__bonus_bombe=3
        self.__bonus_missile=1
        self.__bonus_colonne=1
        
        image_indice=tkinter.PhotoImage(file='img/powerup.gif')
        self.__indice=tkinter.PhotoImage(file='img/indice.gif')
        indice=tkinter.Button(self.__fenetre,image=image_indice,command=self.donne_indice).grid(row=self.__same.nblig()//2-2,column=self.__same.nbcol())
        indice_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_indice),width=3,font=50).grid(row=self.__same.nblig()//2-2,column=self.__same.nbcol()+1)
        
        image_bombe=tkinter.PhotoImage(file='img/bob_omb.gif')
        bombe=tkinter.Button(self.__fenetre,image=image_bombe,command=self.creer_btn_bombe).grid(row=self.__same.nblig()//2-1,column=self.__same.nbcol())
        bombe_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_bombe),width=3,font=50).grid(row=self.__same.nblig()//2-1,column=self.__same.nbcol()+1)
        
        image_missile=tkinter.PhotoImage(file='img/billball.gif')
        missile=tkinter.Button(self.__fenetre,image=image_missile,command=self.creer_btn_missile).grid(row=self.__same.nblig()//2,column=self.__same.nbcol())
        missile_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_missile),width=3,font=50).grid(row=self.__same.nblig()//2,column=self.__same.nbcol()+1)
        
        image_bonus_col=tkinter.PhotoImage(file='img/thwomp.gif')
        bonus_col=tkinter.Button(self.__fenetre,image=image_bonus_col,command=self.creer_btn_suppr_col).grid(row=self.__same.nblig()//2+1,column=self.__same.nbcol())
        colonne_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_colonne),width=3,font=50).grid(row=self.__same.nblig()//2+1,column=self.__same.nbcol()+1)
        
        
        self.__etat=-1
        
        self.__image_gagne=tkinter.PhotoImage(file='img/text_gagne.gif')
        self.__image_perdu=tkinter.PhotoImage(file='img/text_perdu.gif')



        self.__fenetre.mainloop()
        
    
    def redessine(self):
        ''' Méthode qui parcourt tous les boutons de self.__les_btns et change l'image qu'ils afﬁchent en fonction de __same
            
                Arguments : une classe VueSame
                Return :
        '''
        
        for i in range(self.__same.nblig()):
            for j in range(self.__same.nbcol()):
                couleur_sphere=self.__same.couleur(i,j)
                if couleur_sphere==-1:
                    self.__les_btns[i][j]['image']=self.__images[self.__same.nbcouleurs()]
                else:
                    self.__les_btns[i][j]['image']=self.__images[couleur_sphere]
        
        score=tkinter.Label(self.__fenetre,text=str(self.__same.score()),width=15,font=200).grid(row=0,column=self.__same.nbcol()+1)
    
    
    def nouvelle_partie(self):
        ''' Méthode associée au bouton nouveau et qui demande au modèle de réinitialiser une nouvelle partie et ensuite mettre à jour l'affichage
                
                Arguments : une classe VueSame
                Return :
        '''
        
        self.__etat=-1
        
        musique.stop()
        nouveau_jeu.play()
        musique.play(-1)


        self.__same.nouvelle_partie()
        
        
        self.__les_btns=[]
        for i in range(self.__same.nblig()):
            ligne=[]
            for j in range(self.__same.nbcol()):
                couleur_sphere=self.__same.couleur(i,j)
                if couleur_sphere==-1:
                    ligne.append(tkinter.Button(self.__fenetre,image=self.__images[self.__same.nbcouleurs()]))
                    ligne[j].grid(row=i,column=j)
                else:
                    ligne.append(tkinter.Button(self.__fenetre,image=self.__images[couleur_sphere],command=self.creer_controleur_btn(i,j)))
                    ligne[j].bind('<Motion>',self.arrivee_curseur(i,j))
                    ligne[j].bind('<Leave>',self.depart_curseur(i,j))
                    ligne[j].grid(row=i,column=j)
            self.__les_btns.append(ligne)
        
        
        score=tkinter.Label(self.__fenetre,text=str(self.__same.score()),width=15,font=200).grid(row=0,column=self.__same.nbcol()+1)
        
        
        self.__bonus_indice=5    
        self.__bonus_bombe=3
        self.__bonus_missile=1
        self.__bonus_colonne=1
        
        indice_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_indice),width=3,font=50).grid(row=self.__same.nblig()//2-2,column=self.__same.nbcol()+1)
        bombe_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_bombe),width=3,font=50).grid(row=self.__same.nblig()//2-1,column=self.__same.nbcol()+1)
        missile_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_missile),width=3,font=50).grid(row=self.__same.nblig()//2,column=self.__same.nbcol()+1)
        colonne_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_colonne),width=3,font=50).grid(row=self.__same.nblig()//2+1,column=self.__same.nbcol()+1)
        
       
    def creer_controleur_btn(self,i,j):
        ''' Méthode qui retourne la fonction controleur_btn()
            
                Arguments : une classe VueSame et deux entiers i et j
                Return : la fonction controleur_btn()
        '''
        
        def controleur_btn():
            ''' Fonction qui demande au modèle de supprimer les billes des cases ayant la composante de la bille aux coordonnées (i,j) et demande à la vue de se redessiner
                    
                    Arguments :
                    Return :
            '''
            
            composante_sphere=self.__same.composante(i,j)
            
            nombre_billes_a_suppr=0
            if composante_sphere!=0:
                for k in range(self.__same.nblig()):
                    for l in range(self.__same.nbcol()):
                        if self.__same.composante(k,l)==composante_sphere:
                            nombre_billes_a_suppr+=1
            
            if nombre_billes_a_suppr<2:
                non.play()
            else:
                clic.play()
            
            self.__same.supprime_composante(composante_sphere) 
            self.redessine()
            
            self.ecran_fin()
        
        return controleur_btn
    
    
    def arrivee_curseur(self,i,j):
        ''' Méthode qui retourne la fonction arrivee_curseur_bouton

                Arguments : une méthode VueSame et deux entiers i et j
                Return : une fonction arrivee_curseur_bouton
        '''
        
        def arrivee_curseur_bouton(event):
            ''' Fonction qui afﬁche toutes les billes de la composante survolée par le curseur en noir '''
            
            couleur_sphere=self.__same.couleur(i,j)
            composante_sphere=self.__same.composante(i,j)
            
            nombre_billes_a_suppr=0
            
            if composante_sphere!=0:
                for k in range(self.__same.nblig()):
                    for l in range(self.__same.nbcol()):
                        if self.__same.composante(k,l)==composante_sphere:
                            self.__les_btns[k][l]['image']=self.__images_noires[couleur_sphere]
                            nombre_billes_a_suppr+=1
            
            if nombre_billes_a_suppr<2:
                score_add=0
            else:
                score_add=(nombre_billes_a_suppr-2)**2
            
            score_ajout=tkinter.Label(self.__fenetre,text='+ '+str(score_add),width=5,bg='yellow').grid(row=1,column=self.__same.nbcol()+1)
            
        return arrivee_curseur_bouton
    
    
    def depart_curseur(self,i,j):
        ''' Méthode qui retourne la fonction depart_curseur_bouton

                Arguments : une méthode VueSame et deux entiers i et j
                Return : une fonction depart_curseur_bouton
        '''
        
        def depart_curseur_bouton(event):
            ''' Fonction qui réafﬁche la composante pointée avec le cruseur en blanc lorsque on le déplace '''
            
            self.redessine()
            
            score_ajout=tkinter.Label(self.__fenetre,text=' ',width=5).grid(row=1,column=self.__same.nbcol()+1)
        
        return depart_curseur_bouton
    
    
    def donne_indice(self):
        ''' Méthode qui permet de changer les images des cases du jeu ayant la composante la plus présente
                Arguments : une classe VueSame
                Return :
        '''

        if self.__bonus_indice>0:
            
            composante_max=self.__same.compo_max()
            
            nombre_billes_suppr=0
            for i in range(self.__same.nblig()):
                for j in range(self.__same.nbcol()):
                    if self.__same.composante(i,j)==composante_max:
                        nombre_billes_suppr+=1
            
            if nombre_billes_suppr>=2:
                son_indice.play()
            
                for i in range(self.__same.nblig()):
                    for j in range(self.__same.nbcol()):
                        if self.__same.composante(i,j)==composante_max:
                            self.__les_btns[i][j]['image']=self.__indice
            
                self.__bonus_indice-=1
            
                indice_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_indice),width=3,font=50).grid(row=self.__same.nblig()//2-2,column=self.__same.nbcol()+1)
        
            else:
                son_mamamia.play()
                
        else:
            non.play()
        
    
    def creer_btn_bombe(self):
        ''' Méthode qui permet d'utiliser le bonus bombe en retournant la fonction btn_bombe '''
        
        def btn_bombe():
            ''' Fonction qui supprime aléatoirement une case du jeu ainsi que les 8 cases autour d'elle '''
            
            if self.__bonus_bombe>0 and self.__etat==-1:
                son_tictac.play()
                time.sleep(2) 
                son_bombe.play()
                
                self.__same.bonus_bombe()
                self.redessine()
                
                self.__bonus_bombe-=1
                bombe_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_bombe),width=3,font=50).grid(row=self.__same.nblig()//2-1,column=self.__same.nbcol()+1)
                
                self.ecran_fin()
                
            else:
                non.play()
        
        return btn_bombe() 
            
    
    def creer_btn_missile(self):
        ''' Méthode qui permet d'utiliser le bonus missile en retournant la fonction btn_missile '''
        
        def btn_missile():
            ''' Fonction qui supprime aléatoirement une ligne du jeux '''
            
            if self.__bonus_missile>0 and self.__etat==-1:
                son_fusee.play()
                
                self.__same.bonus_missile()
                self.redessine()
                
                self.__bonus_missile-=1
                missile_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_missile),width=3,font=50).grid(row=self.__same.nblig()//2,column=self.__same.nbcol()+1)
                
                self.ecran_fin()
                
            else:
                non.play()
        
        return btn_missile()


    def creer_btn_suppr_col(self):
        ''' Méthode qui permet d'utiliser le bonus missile en retournant la fonction btn_missile '''
        
        def btn_suppr_col():
            ''' Fonction qui supprime aléatoirement une colonne du jeux '''
            
            if self.__bonus_colonne>0 and self.__etat==-1:
                son_suppr_col.play()
                
                self.__same.bonus_colonne()
                self.redessine()
                
                self.__bonus_colonne-=1
                missile_compteur=tkinter.Label(self.__fenetre,text='x'+str(self.__bonus_colonne),width=3,font=50).grid(row=self.__same.nblig()//2+1,column=self.__same.nbcol()+1)
                
                self.ecran_fin()
                
            else:
                non.play()
        
        return btn_suppr_col()
    
    
    def ecran_fin(self):
        ''' Méthode qui permet de vérifier si la partie est fini ainsi que d'afficher un message gagnant ou perdant selon la situation
                
                Arguments : une classe VueSame
                Return :
        '''
        
        if self.__same.partie_finie()==1:
            self.__etat=1
            musique.stop()
            win.play()
            gagne=tkinter.Button(self.__fenetre,image=self.__image_gagne,command=self.effet_gagne).grid(row=self.__same.nblig()//2-1,column=self.__same.nbcol()//2)
        
        elif self.__same.partie_finie()==0 and self.__bonus_bombe==0 and self.__bonus_missile==0 and self.__bonus_colonne==0:
            self.__etat=0
            musique.stop()
            lost.play()
            
            perdu=tkinter.Button(self.__fenetre,image=self.__image_perdu,command=self.effet_perdu).grid(row=self.__same.nblig()//2-1,column=self.__same.nbcol()//2)
    
    
    def effet_gagne(self):
        ''' Méthode permettant de faire un bruit lorsque le joueur clique sur le bouton gagne '''
        
        btn_win.play()
    
    
    def effet_perdu(self):
        ''' Méthode permettant de faire un bruit lorsque le joueur clique sur le bouton perdu '''
        
        btn_lost.play(2)




if __name__=='__main__' :
    
    pygame.mixer.pre_init(200000)
    pygame.mixer.init()
    
    musique=pygame.mixer.Sound('music/musique.wav')
    
    clic=pygame.mixer.Sound('music/clic.wav')
    non=pygame.mixer.Sound('music/non.wav')
    
    nouveau_jeu=pygame.mixer.Sound('music/tuyau.wav')
    son_quitter=pygame.mixer.Sound('music/quitter.wav')
    
    son_indice=pygame.mixer.Sound('music/powerup.wav')
    son_mamamia=pygame.mixer.Sound('music/mamamia.wav')
    son_tictac=pygame.mixer.Sound('music/tictac.wav')
    son_bombe=pygame.mixer.Sound('music/bombe.wav')
    son_fusee=pygame.mixer.Sound('music/fusee.wav')
    son_suppr_col=pygame.mixer.Sound('music/thwomp.wav')
    
    win=pygame.mixer.Sound('music/win.wav')
    btn_win=pygame.mixer.Sound('music/bouton_gagne.wav')
    
    lost=pygame.mixer.Sound('music/lost.wav')
    btn_lost=pygame.mixer.Sound('music/bouton_perdu.wav')
    
    
    same=modele.ModeleSame()
    vue=VueSame(same)
    
    
    musique.stop()
    son_quitter.play()



