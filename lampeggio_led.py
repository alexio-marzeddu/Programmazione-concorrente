
import multiprocessing
import time


def lampeggia(led):
    colori = {
        1: ("verde", 0.3),
        2: ("rosso", 0.7),
        3: ("giallo", 1.2)
    }

    colore, intervallo = colori[led]

    for i in range(10):
        print(f"LED {colore} acceso", flush=True)
        time.sleep(intervallo)

        print(f"LED {colore} spento", flush=True)
        time.sleep(intervallo)


def main():
    while True:
        comando = input(
            "comando (v=verde, r=rosso, g=giallo, q=esci): "
        ).lower().strip()

        if comando == "q":
            print("chiusura del programma.")
            break
        elif comando == "v":
            led = 1
        elif comando == "r":
            led = 2
        elif comando == "g":
            led = 3
        else:
            print("comando non valido!")
            continue

        processo = multiprocessing.Process(
            target=lampeggia,
            args=(led,)
        )
        processo.start()
        processo.join()


if __name__ == "__main__":
    main()
