import math
class Exceptions(Exception):
    pass
class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        if not isinstance (x, int | float) or not isinstance (y, int | float):
            raise TypeError("la valeur doite etre entiere ou reele")
        self.__x = float(x)
        self.__y = float(y)

    def distanceCoord(self,a:float,b:float)->float:
        if not isinstance (a, int | float) or not isinstance (b, int | float):
            raise TypeError("les coordonnees doivent etre entiere ou reele")
        return math.sqrt((self.__x - a) ** 2 + (self.__y - b) ** 2)
    def distancePoint(self, camarade: "Point") -> float:
        if not isinstance (camarade, Point):
            raise TypeError("l'argument doit etre point")
        return self.distanceCoord(camarade.__x, camarade.__y)
    def __str__(self) -> str:
        return f"Point : ({self.__x},{self.__y})"
    def get_x(self) -> float:
        return self.__x
    def get_y(self) -> float:
        return self.__y


class Cercle:

    def __init__(self, rayon: float, centre: Point=Point(0,0)):
        if not isinstance(rayon, int | float):
            raise TypeError("Le rayon doit etre reel")
        if not isinstance(centre, Point):
            raise TypeError("Le centre doit etre Point")
        if rayon <= 0:
            raise Exceptions("Le rayon ne peut pas etre negatif ou nul")
        self.__rayon = float(rayon)
        self.__centre = centre

    def diametre(self) -> float:
        return 2 * self.__rayon
    def perimetre(self) -> float:
        return 2 * math.pi * self.__rayon
    def surface(self) -> float:
        return math.pi * (self.__rayon**2)
    def est_en_intersection(self, autre: "Cercle") -> bool:
        dist_centres = self.__centre.distancePoint(autre.__centre)
        return dist_centres <= self.__rayon + autre.__rayon
    def contient_point(self, p: Point) -> bool:
        return self.__centre.distancePoint(p) <= self.__rayon


class Rectangle:

    def  __init__(self, bas_gauche:Point=Point(0,0), longeur:float=1.0, hauteur:float=1.0, haut_droit:Point=None):
        if not isinstance(bas_gauche, Point):
            raise TypeError("L'origine bas_gauche doit etre un Point")
        if haut_droit is None:
            if not isinstance(haut_droit, int | float):
                raise TypeError("L'origine haut_droit doit etre entiere ou reele")
            self.__bas_gauche = bas_gauche
            self.__longeur = longeur
            self.__hauteur = hauteur
        else:
            self.__bas_gauche = bas_gauche
            self.__longeur = haut_droit.get_x() - bas_gauche.get_x()
            self.__hauteur = haut_droit.get_y() - bas_gauche.get_y()


    def surface(self) -> float:
        return self.__longeur * self.__hauteur
    def perimetre(self) -> float:
        return 2 * (self.__longeur + self.__hauteur)

    @property
    def bas_gauche(self) -> Point:
        return self.__bas_gauche
    @property
    def bas_droit(self) -> Point:
        return Point(self.__bas_gauche.get_x() + self.__longeur, self.__bas_gauche.get_y())
    @property
    def haut_gauche(self) -> Point:
        return Point(self.__bas_gauche.get_x(), self.__bas_gauche.get_y() + self.__hauteur)
    @property
    def haut_droit(self) -> Point:
        return Point(self.__bas_gauche.get_x() + self.__longeur, self.bas_gauche.get_y() + self.__hauteur)

    def contient_point(self, p: Point) -> bool:
        if p.get_x() >= self.bas_gauche.get_x() and p.get_x() <= self.bas_droit.get_x():
            if p.get_y() >= self.bas_gauche.get_y() and p.get_y() <= self.haut_gauche.get_y():
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
   point1 = Point(2,3.4)
   print(point1)
   point2 = Point(2,5)
   print(point2)
   print(point1.distancePoint(point2))