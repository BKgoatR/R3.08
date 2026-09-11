import math

class Point :
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'Point : ({self.__x}, {self.__y})'

    def distanceCoordonees(self,x : float, y: float):
        distance = math.sqrt(math.pow(self.__x-x,2)+math.pow(self.__y-y,2))
        return distance
    def distancePoint(self, camarade : "Point") -> float:
        return self.distanceCoordonees(camarade.__x,camarade.__y)

class Cercle:
    def __init__(self, rayon: float, centre : "Point"):
        self.__rayon = rayon
        self._centre = centre
    def __str__(self):
        return f'Cercle : ({self.__rayon}, {self._centre})'
    def diametre (self)-> float:
        return 2 * self.__rayon
    def perimetre(self)-> float:
        return 2 * math.pi * self.__rayon
    def surface(self)-> float:
        return math.pi * self.__rayon * self.__rayon
    def 

class Rectangle:


if __name__ == '__main__':
    point1 = Point(2,3,4)
    print(point1)
    point2 = Point()
    print(point2)
    print(point1.distanceCoordonees(2,3))


