def main():
    #escribe tu código abajo de esta línea
    nacimiento = int(input("Dame el año de nacimiento: "))
    actual = int(input("Dame el año actual: "))
    lustros_vividos = (actual - nacimiento) / 5
    print("Los lustros que has vivido son:", lustros_vividos)



if __name__ == '__main__':
    main()
