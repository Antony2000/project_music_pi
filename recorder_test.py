import msvcrt

def main():
    while True:
        key_pressed = msvcrt.getch()
        if key_pressed:
            # Ejecutar bloque de código mientras se presiona la tecla
            print("Tecla pulsada")
        else:
            # Ejecutar otro bloque de código cuando se deja de pulsar la tecla
            print("Tecla no pulsada")

if __name__ == '__main__':
    main()