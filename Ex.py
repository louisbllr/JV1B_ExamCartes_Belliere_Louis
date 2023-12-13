class Carte:
    def __init__(self,name,mana,description):
        self.__nom = name
        self.__mana = mana
        self.__description = description
    def getName(self):    
        return self.__nom
    def getMana(self):
        return self.__mana
    def getDescription(self):
        return self.__description
    


class Mage:
    def __init__(self,name,hp,maxmana,main,defausse,zdj,joue,stockmana,attaque):
        self.__name = name
        self.__hp = hp
        self.__maxmana = maxmana
        self.__main = main
        self.__defausse = defausse 
        self.__zdj = zdj
        self.__joue = joue
        self.__stockmana = stockmana
        self.__attaque = attaque
    def getName(self):
        return self.__name
    def getHp(self):
        return self.__hp
    def getTotalmana(self):
        return self.__maxmana  
    def getMain(self):
        return self.__main
    def getDefausse(self):
        return self.__defausse
    def getZdj(self):
        return self.__zdj
    def getJoue(self):
        self.__main -=1
        self.__stockmana -=20
        self.__zdj +=1
        return self.__joue
    def getStockmana(self):
        self.__stockmana +=50
        return self.__stockmana
    def getAttaque(self):
        self.__zdj -=1 
        return self.__attaque

        
class Cristal(Carte,Mage):  
    def __init__(self, name, mana, description,valeur,coutmana):
        super().__init__(name, mana, description)
        self.__valeur=valeur
        self.__coutmana=coutmana
    def getValeur(self):
        return self.__valeur
    def getCoutmana(self):
        return self.__coutmana
    def getCristal(self):
        self.__coutmana -= self.__stockmana
        self.__maxmana = self.__maxmana + self.__maxmana
    
class Creature(Carte,Mage):
    def __init__(self, name, mana, description,hp,attaque, coutmana):
        super().__init__(name, mana, description)  
        self.__hp=hp
        self.__attaque=attaque 
        self.__coutmana = coutmana

    def Attaque(self):
        self.__coutmana -= self.__stockmana 
        self.__hp -= self.__attaque
        return self.__attaque         
    def Hp(self):
        return self.__hp    


class Blast(Carte,Mage):
    def __init__(self, name, mana, description,valeur):
        super().__init__(name, mana, description)            
        self.__valeur=valeur

    def Valeur(self):
        self.__valeur -= self.__hp
        return self.__valeur    
    
