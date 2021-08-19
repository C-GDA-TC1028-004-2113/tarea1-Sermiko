def main():
    #escribe tu código abajo de esta línea
    n_mensajes = int(input("Dame el número de mensajes: "))
    n_megas = float(input("Dame el número de megas: "))
    n_minutos = int(input("Dame el número de minutos: "))
    costo_mensual = (n_mensajes + n_megas + n_minutos)*0.8
    print("El costo mensual es:", costo_mensual)


if __name__ == '__main__':
    main()
