def printCategory(age):
    if age > 18:
        print('Adulto')
    elif age > 65:
        print('Adulto mayor')
    else:
        print('Niño')

        # Aquí colocas la edad al llamar la función:
printCategory(70)  # 👉 Imprime: Adulto mayor
#printCategory(30)  # 👉 Imprime: Adulto
#printCategory(10)  # 👉 Imprime: Niño