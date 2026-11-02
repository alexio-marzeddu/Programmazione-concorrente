import os

#inizializzo le variabili
base = 10
altezza = 5
risultato = 0

#creazione del processo figlio
pid = os.fork()

if pid < 0:
    #rilevamento pid < 0 (impossibile)
    print("errore")

else if pid == 0:
    #calcolo del perimetro
    risultato = 2*(base+altezza)
    print("il figlio ha calcolato perimetro:", risultato)

else:
    #calcolo l'area
    risultato = base*altezza
    print("il padre ha calcolato area:", risultato)

    #attesa del termine dei calcoli
    os.wait()
