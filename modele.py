# Module modele.py du projet Same réalisé par Nicolas Deronsart


from random import randint


# La classe Case

class Case:
    ''' Classe Case qui modélise une bille du jeu Same '''
    
    def __init__(self,couleur):
        ''' Constructeur de la classe Case

                Arguments : la classe Case et un entier poisitif ou nul couleur
        '''
        
        assert couleur>=0
        
        self.__couleur=couleur
        self.__compo=-1
    
    
    def couleur(self):
        ''' Méthode qui retourne la couleur de la bille

                Argument : une classe Case
                Return : un entier
        '''
        
        return self.__couleur
    
    
    def change_couleur(self,nouvelle_couleur):
        ''' Méthode qui change la couleur de la bille et remet son numéro de composante à -1
                
                Arguments : une classe Case et un entier nouvelle_couleur
                Return :
        '''
        
        self.__couleur=nouvelle_couleur
        self.__compo=-1
    
    
    def supprime(self):
        ''' Méthode qui enlève la bille de la case, c'est à dire qui passe la couleur de la case à -1 et met sa composante à 0
                
                Argument : une classe Case
                Return :
        '''
        
        self.__couleur=-1
        self.__compo=0
        
    
    def est_vide(self):
        ''' Méthode qui indique si la case est vide, c'est à dire si sa couleur est -1
                
                Argument : une classe Case
                Return : True ou False
        '''
        
        if self.__couleur==-1:
            return True
        return False
    
    
    def composante(self):
        ''' Méthode qui retourne le numéro de la composante
                
                Argument : une classe Case
                Return : un entier
        '''
        
        return self.__compo
    
    
    def pose_composante(self,composante):
        ''' Méthode qui qui change la valeur du numéro de la composante de la case
                
                Arguments : une classe Case et un entier composante
                Return :
        '''
        
        self.__compo=composante
        
    
    def supprime_compo(self):
        ''' Méthode qui désaffecte le numéro de composante de la case en le remettant à -1
            Mais si la case est vide la valeur est à 0
                
                Arguments : une classe Case
                Return :
        '''
        
        if self.__couleur==-1:
            self.__compo==0
        else:
            self.__compo=-1
    
    
    def parcourue(self):
        ''' Méthode qui teste si la case a été affectée à un numéro de composante
                
                Arguments : une classe Case
                Return : True ou False
        '''
        
        if self.__compo==-1 or self.__compo==0:
            return False
        return True
    
 

# La classe ModeleSame

class ModeleSame:
    ''' Classe ModeleSame qui modélise le jeu Same '''
    
    def __init__(self,nblig=10,nbcol=17,nbcouleurs=4):
        ''' Constructeur de la classe ModeleSame
            Crée une matrice de nblig lignes et nbcol colonnes d'instances de la classe Case

                Arguments : la classe ModeleSame, et 3 entiers nblig, nbcol et nbcouleurs
        '''
        
        self.__nblig=nblig
        self.__nbcol=nbcol
        self.__nbcouleurs=nbcouleurs
        
        self.__mat=[]
        for i in range(self.__nblig):
            self.__mat.append([])
            for j in range(self.__nbcol):
                self.__mat[i].append(Case(randint(0,self.__nbcouleurs-1)))
                
        self.__score=0
        
        self.__nb_elts_compo=[]
        self.calcule_composantes()
       
       
    def score(self):
        ''' Méthode qui retourne le score du joueur
                
                Arguments : une classe ModeleSame
                Return : un entier
        '''
        
        return self.__score
    
    
    def nblig(self):
        ''' Méthode qui retourne le nombre de lignes du jeu
                
                Arguments : une classe ModeleSame
                Return : un entier
        '''
        
        return self.__nblig
    
    
    def nbcol(self):
        ''' Méthode qui retourne le nombre de colonnes du jeu
                
                Arguments : une classe ModeleSame
                Return : un entier
        '''
        
        return self.__nbcol
    
    
    def nbcouleurs(self):
        ''' Méthode qui retourne le nombre de couleurs dans le jeu
                
                Arguments : une classe ModeleSame
                Return : un entier
        '''
        
        return self.__nbcouleurs
    
    
    def coords_valides(self,i,j):
        ''' Méthode qui indique si les coordonnées (i,j) sont valides
            
                Arguments : une classe ModeleSame et deux entiers i et j
                Return : True ou False
        '''
        
        if 0<=i and i<=self.__nblig-1 and 0<=j and j<=self.__nbcol-1:
            return True
        return False
    
    
    def couleur(self,i,j):
        ''' Méthode qui retourne la couleur de la bille aux coordonnées (i,j)
                
                Arguments : une classe ModeleSame et deux entiers i et j
                Return : un entier
        '''
        
        return self.__mat[i][j].couleur()
    
    
    def supprime_bille(self,i,j):
        ''' Méthode qui supprime la bille la bille aux coordonnées (i,j)
                
                Arguments : une classe ModeleSame et deux entiers i et j
                Return :
        '''
        
        self.__mat[i][j].supprime()
    
    
    def nouvelle_partie(self):
        ''' Méthode qui réinitialise toutes les cases en changeant leur couleur
                
                Arguments : une classe ModeleSame
                Return :
        '''
        
        for i in range(self.__nblig):
            for j in range(self.__nbcol):
                self.__mat[i][j]=Case(randint(0,self.__nbcouleurs-1))
        
        self.__score=0
                
        self.__nb_elts_compo=[]
        self.calcule_composantes()
    
    
    def composante(self,i,j):
        ''' Méthode qui retourne la composante de la bille aux coordonnées (i,j)
                
                Arguments : une classe ModeleSame et deux entiers i et j
                Return : un entier
        '''
        
        return self.__mat[i][j].composante()


    def calcule_composantes(self):
        ''' Méthode qui lance le calcul des composantes sur toutes les cases du jeux

                Arguments : une classe ModeleSame
                Return :
        '''
        
        self.__nb_elts_compo.append(0)
        
        num_compo=1
        for i in range(self.__nblig):
            for j in range(self.__nbcol):
                if self.composante(i,j)==-1:
                    couleur=self.couleur(i,j)
                    self.__nb_elts_compo.append(self.calcule_composante_numero(i,j,num_compo,couleur))
                    num_compo+=1 
                    
    
    def calcule_composante_numero(self,i,j,num_compo,couleur):
        ''' Méthode qui retourne le nombre de cases de la composante num_compo
                
                Arguments : une classe ModeleSame et quatre entiers i, j, num_compo et couleur
                Return : un entier
        '''
        
        if self.__mat[i][j].parcourue() or self.couleur(i,j)!=couleur:
            return 0
        else:
            self.__mat[i][j].pose_composante(num_compo)
            composante=1
            if self.coords_valides(i,j+1):
                composante+=self.calcule_composante_numero(i,j+1,num_compo,couleur)
            if self.coords_valides(i,j-1):
                composante+=self.calcule_composante_numero(i,j-1,num_compo,couleur)
            if self.coords_valides(i+1,j):
                composante+=self.calcule_composante_numero(i+1,j,num_compo,couleur)
            if self.coords_valides(i-1,j):
                composante+=self.calcule_composante_numero(i-1,j,num_compo,couleur)
            return composante
    
    
    def recalc_composantes(self):
        ''' Méthode qui supprime les composantes de toutes les cases du jeux pour ensuite les recalculer
                
                Arguments : une classe ModeleSame
                Return :
        '''
        
        self.__nb_elts_compo=[]
        for i in range (self.__nblig):
            for j in range (self.__nbcol):
                self.__mat[i][j].supprime_compo()
        
        self.calcule_composantes()
    
    
    def supprime_composante(self,num_compo):
        ''' Méthode qui supprime toutes les billes du jeu étant dans la composante num_compo
                
                Arguments : une clase ModeleSame
                Return : True ou False
        '''
        
        if num_compo==0:
            return False
        
        nombre_billes_suppr=0
        for i in range(self.__nblig):
            for j in range(self.__nbcol):
                if self.composante(i,j)==num_compo:
                    nombre_billes_suppr+=1
        
        if nombre_billes_suppr>=2:
            for j in range(self.nbcol()):
                self.supprime_composante_colonne(j,num_compo)  
            self.recalc_composantes()
            
            self.supprime_colonnes_vides()
            self.recalc_composantes()
            
            self.__score+=(nombre_billes_suppr-2)**2
            
            return True
        return False
    
    
    def est_vide(self,i,j):
        ''' Méthode qui indique si la case aux coordonnées (i,j) est vide
                
                Arguments : une classe ModeleSame et deux entiers i et j
                Return : True ou False
        '''
        
        if self.__mat[i][j].est_vide():
            return True
        return False
    
    
    def supprime_composante_colonne(self,j,num_compo):
        ''' Méthode qui supprime les billes de la composante num_compo se trouvant dans la colonne j
            De plus les cases vides se retrouvent en haut de la colonne
            
                Arguments : une classe ModeleSame et deux entiers j et num_compo
                Return :
        '''
        
        for i in range(self.nblig()):
            if self.composante(i,j)==num_compo:
                self.supprime_bille(i,j)
        
        
        cases_colonne=[]
        for i in range(self.nblig()):
            if self.est_vide(i,j):
                cases_colonne.append([self.__mat[i][j].couleur(),self.__mat[i][j].composante()])
        for i in range(self.nblig()):
            if not self.est_vide(i,j):
                cases_colonne.append([self.__mat[i][j].couleur(),self.__mat[i][j].composante()])
        
        for i in range(self.nblig()):
            self.__mat[i][j].change_couleur(cases_colonne[i][0])
            self.__mat[i][j].pose_composante(cases_colonne[i][1])
                
    
    def supprime_colonnes_vides(self):
        ''' Méthode qui décale les colonnes vides vers la droite du jeu
                
                Arguments : une classe ModeleSame
                Return :
        '''
        
        colonnes_vides=[]
        colonnes_final=[]
        
        for j in range(self.nbcol()):
            vide=True
            for i in range(self.nblig()):
                if not self.est_vide(i,j):
                    vide=False
            if vide==True:
                colonnes_vides.append(j)
            else:
                colonnes_final.append(j) 

        for j in colonnes_vides:
            colonnes_final.append(j)
        
        ancien_jeu=[]
        for i in range(self.__nblig):
            ancien_jeu.append([])
            for j in range(self.__nbcol):
                ancien_jeu[i].append(self.__mat[i][j])
        
        for i in range(self.nblig()):
            for j in range(self.nbcol()):
                self.__mat[i][j]=ancien_jeu[i][colonnes_final[j]]
    
    
    def compo_max(self):
        ''' Méthode qui retourne la composante attribuée au plus de cases dans le jeu
                
                Arguments : une classe ModeleSame
                Return : un entier
        '''
        
        composante_max=1
        contenu_max=0
        
        for i in range(self.nblig()):
            for j in range(self.nbcol()):
                compo_testee=self.composante(i,j)
                compte=0
                for k in range(self.nblig()):
                    for l in range(self.nbcol()):
                        if self.composante(k,l)==compo_testee:
                            compte+=1
                if compte>contenu_max and compo_testee>0:
                    contenu_max=compte
                    composante_max=compo_testee
        
        return composante_max
    
    
    def bonus_bombe(self): 
        ''' Méthode associée au bonus bombe qui permet de supprimer aléatoirement une case du jeu avec les 8 cases autour '''
    
        compo_alea=0
           
        while compo_alea==0:
            lig_alea=randint(0,self.nblig()-1)
            col_alea=randint(0,self.nbcol()-1)
            compo_alea=self.composante(lig_alea,col_alea)
        
        self.supprime_bille(lig_alea,col_alea)
        for i in range(-1,2):
            for j in range(-1,2):
                if self.coords_valides(lig_alea+i,col_alea+j):
                    self.supprime_bille(lig_alea+i,col_alea+j)

        
        for j in range(self.nbcol()):
            cases_colonne=[]
            for i in range(self.nblig()):
                if self.est_vide(i,j):
                    cases_colonne.append([self.__mat[i][j].couleur(),self.__mat[i][j].composante()])
            for i in range(self.nblig()):
                if not self.est_vide(i,j):
                    cases_colonne.append([self.__mat[i][j].couleur(),self.__mat[i][j].composante()])
            for i in range(self.nblig()):
                self.__mat[i][j].change_couleur(cases_colonne[i][0])
                self.__mat[i][j].pose_composante(cases_colonne[i][1])
        self.recalc_composantes()
        
        self.supprime_colonnes_vides()
        self.recalc_composantes()
    
    
    def bonus_missile(self):
        ''' Méthode associée au bonus missile qui permet de supprimer aléatoirement une ligne du jeu '''
        
        lig_vide=True
        while lig_vide:
            lig_alea=randint(0,self.nblig()-1)
            for j in range(self.nbcol()):
                if self.composante(lig_alea,j)!=0:
                    lig_vide=False
        
        for j in range(self.nbcol()):
            self.supprime_bille(lig_alea,j)
        
        
        for j in range(self.nbcol()):
            cases_colonne=[]
            for i in range(self.nblig()):
                if self.est_vide(i,j):
                    cases_colonne.append([self.__mat[i][j].couleur(),self.__mat[i][j].composante()])
            for i in range(self.nblig()):
                if not self.est_vide(i,j):
                    cases_colonne.append([self.__mat[i][j].couleur(),self.__mat[i][j].composante()])
            for i in range(self.nblig()):
                self.__mat[i][j].change_couleur(cases_colonne[i][0])
                self.__mat[i][j].pose_composante(cases_colonne[i][1])
        self.recalc_composantes()
        
        self.supprime_colonnes_vides()
        self.recalc_composantes()
    
    
    def bonus_colonne(self):
        ''' Méthode associée au bonus colonne qui permet de supprimer aléatoirement une colonne du jeu '''
        
        col_vide=True
        while col_vide:
            col_alea=randint(0,self.nbcol()-1)
            for i in range(self.nblig()):
                if self.composante(i,col_alea)!=0:
                    col_vide=False
        
        for i in range(self.nblig()):
            self.supprime_bille(i,col_alea)
        
        
        self.recalc_composantes()
        
        self.supprime_colonnes_vides()
        self.recalc_composantes()
    
    
    def partie_finie(self):
        ''' Méthode qui permet d'indiquer si la partie est gagnée, perdu ou non finie
                
                Arguments : une classe ModeleSame
                Return : -1 si la partie n'est pas finie, 0 si elle est perdue et 1 si elle est gagnée
        '''
        
        composante_max=self.compo_max()
        compte=0
        for i in range(self.nblig()):
            for j in range(self.nbcol()):
                if self.composante(i,j)==composante_max:
                    compte+=1
        
        if compte==0:
            return 1
        elif compte==1:
            return 0
        else:
            return -1
        


