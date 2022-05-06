#Palindromo
def Palindromo(palabra):
    palabra == palabra[::-1]
    if palabra==True:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
    return palabra

