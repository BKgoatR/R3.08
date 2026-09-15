def division(a, b):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("la valeur fournie doit etre reele")
    return a / b

try :
    resultat = division(4, "2")
except TypeError as terr:
    print(terr)
except ValueError as verr:
    print(verr)
except Exception as e:
    print(e)
else :
    print("Bonne division")
finally :
    print("fin du bloc")