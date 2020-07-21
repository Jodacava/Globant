def validator(type1, type2):
    def params(func):
        def valpar(par1, par2):
            if type(par1) == type1:
                print("El primer parámetro tiene el tipo de dato correcto")
            else:
                print("El primer parámetro No tiene el tipo de dato correcto")
            if type(par2) == type2:
                print("El segundo parámetro tiene el tipo de dato correcto")
            else:
                print("El segundo parámetro No tiene el tipo de dato correcto")
            return func(par1, par2)
        return valpar
    return params


@validator(int, int)
def add(a, b):
    return a + b

print(add(1.1,1))