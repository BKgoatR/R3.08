


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

    def attaque(self, opposant : Personnage):
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

    def combat(self, attaque, opposant : Personnage):
        while (opposant.__pv or self.__pv <= 0):


