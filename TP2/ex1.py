


class Personnage:
    def __init__(self, pseudo: str, niveau: int):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau

    @property
    def pv(self):
        return self.__pv
    @property
    def initiative(self):
        return self.__initiative
    @property
    def niveau(self):
        return self.__niveau
    @property
    def pseudo(self):
        return self.__pseudo

    def degats(self):
        return self.__niveau

    def soigner(self):
        self.__pv = self.__niveau

    def attaque(self, opposant : 'Personnage'):
        if opposant.__initiative < self.__initiative :
            opposant.__pv = opposant.__pv - self.__niveau
            if opposant.__pv > 0:
                self.__pv = self.__pv - opposant.__niveau
        elif opposant.__initiative == self.initiative :
            opposant.__pv = opposant.__pv - self.__niveau
            self.__pv = self.__pv - opposant.__niveau
        else:
            self.__pv = self.__pv - opposant.__niveau
            if opposant.__pv > 0:
                opposant.__pv = opposant.__pv - self.__niveau

    def combat(self, opposant : 'Personnage'):
        tour = 1
        while self.__pv > 0 and opposant.__pv > 0:
            self.attaque(opposant)
            tour = tour + 1

    def __eq__(self, autre: 'Personnage') -> bool:
        return self.__niveau == autre.__niveau and self.__pseudo == autre.__pseudo


class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.__pv = niveau * 8 + 4
        self.__initiative = niveau * 4 + 6
    def degats(self):
        return self.__niveau *2

class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.__pv = niveau *5 + 10
        self.__initiative = niveau *6 + 4
        self.__mana = niveau *5
    def degats(self):
        if self.__mana >=4:
            self.__mana = self.__mana - 4
            return self.__niveau *3
        else:
            return self.__niveau

class Joueur :
    def __init__(self, nom = str, max_perso = int):
        self.__nom = nom
        self.__max_perso = max_perso
        self.__personnages = []

    def ajouter_pesonnage(self, perso: Personnage):
        if len(self.__personnages) >= self.__max_perso:
            self.__personnages.append(perso)

    def acces_perso_index(self,index:int)->Personnage:
        return self.__personnages[index]

    def acces_perso_nom(self,nom:str)->Personnage:
        for personnage in self.__personnages:
            if personnage.pseudo == nom:
                return personnage

    def acces_perso_avec_personnage(self,personnage:Personnage)->Personnage:
        for p in self.__personnages:
            if p == personnage:
                return p

    def del_perso_index(self,index:int)->Personnage:
        return self.__personnages.pop(index)

    def del_perso_nom(self,nom:str)->Personnage:
        for p in self.__personnages:
            if p.pseudo == nom:
                return self.__personnages.remove(p)

    def del_perso_avec_personnage(self,personnage:Personnage)->Personnage:
        for p in self.__personnages:
            if p == personnage:
                return self.__personnages.remove(p)





