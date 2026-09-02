#def max (a : int, b : int) -> int:
#    if a > b:
#       return a
#    else :
#        return b

#print(max (5, 3))

#def seuil (a : int, b : int=10) -> int:
#    if a > b:
#        return f"seuil dépassé"
#    else :
#        return f"seuil ok"
#print(seuil(4))
#print(seuil(11))

def max_liste (a_liste) -> int:
    max_liste = []
    for i in a_liste:
        if i > max_liste:
            max_liste = i
            return max_liste
print(max_liste([]))
print(max_liste([1]))
print(max_liste([1, 2]))
