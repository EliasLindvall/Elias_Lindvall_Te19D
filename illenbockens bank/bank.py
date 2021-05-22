from functions import *
import os

move_transactions()
    
# Programloopen
while True:

    # Skriver ut menyn och frågar användar efter sitt val
    meny = ("\n############################"
    "\n#                          #"
    "\n#    illenbockens bank     #"
    f"\n#       Saldo: {balance()}kr      #"
    "\n#                          #"
    "\n############################"
    "\n "

    "\n 1: Visa transaktioner."
    "\n 2: Sätt in pengar."
    "\n 3: Ta ut pengar."
    "\n 4: Nollställ kontot"
    "\n 5: Avsluta applikationen."
    "\n Gör ditt val (1-5):")


    val = validate_int(meny, "Felaktig inmatning! Gör om gör rätt.")            # Kollar om valet är ett giltigt svar


    if val == 1:            # Visa transaktionslistan
        print_transactions()


    elif val == 2:          # Sätta in pengar
        insättning = validate_int("Hur mycket pengar vill du sätta in (kr)?","Felaktig inmatning! Gör om gör rätt.")
        if insättning > 0:
            add_transaction(insättning, True)
        else:
             print("insättningen kan inte vara negativ.")
    

    elif val == 3:          # Ta ut pengar
        uttag = validate_int("Hur mycket pengar vill du ta ut (kr)?", "Felaktig inmatning! Gör om gör rätt.")
        if uttag > balance():
            print(f"Du kan inte ta ut mer än {balance()}kr")
        elif uttag < 0:
            print("uttaget kan inte vara negativt.")
        else:
            add_transaction(-uttag, True)  


    elif val == 4:          # Nollställa kontot
        nollställ= int(input("Är du säker detta nollställer hela kontot?\n1. Ja\n2. Nej\nVälj (1-2):"))
        if nollställ == 1:
            os.remove(filename)
            transaktioner.clear()
            move_transactions()
        else:
            continue


    elif val == 5:          # Avsluta programmet
        break


