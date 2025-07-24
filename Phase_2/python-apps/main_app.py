import geometry_calculator
import greetings
import math_utils
import list_utils
import number_generator
import os
import platform
import time

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    app_names = ["",
                   "\033[31m1\033[0m Geometry Calculator",
                   "\033[32m2\033[0m Greetings", 
                   "\033[34m3\033[0m Math Utils", 
                   "\033[36m4\033[0m List Utils", 
                   "\033[33m5\033[0m Number Generator",
                   "\033[37m6\033[0m Beenden"]

    while True:
        print("\n\033[36mWillkommen zu meiner eigenen Modul-Anwendung!\033[0m\n")

        # Benutzer Interface zur Abfrage
        print("""App Auswahl:          
\033[31m1\033[0m \033[30mGeometry Calculator\033[0m 
\033[32m2\033[0m \033[30mGreetings\033[0m 
\033[34m3\033[0m \033[30mMath Utils\033[0m
\033[36m4\033[0m \033[30mList Utils\033[0m
\033[33m5\033[0m \033[30mNumber Generator\033[0m
\033[37m6\033[0m \033[30mBeenden\033[0m
              """)

        auswahl = input()

        time.sleep(0)
        clear_console()

        # Benutzer Interface zur Abfrage
        print("\n\033[36mWillkommen zu meiner eigenen Modul-Anwendung!\033[0m\n")
        print("""App Auswahl:          
\033[31m1\033[0m \033[30mGeometry Calculator\033[0m 
\033[32m2\033[0m \033[30mGreetings\033[0m 
\033[34m3\033[0m \033[30mMath Utils\033[0m
\033[36m4\033[0m \033[30mList Utils\033[0m
\033[33m5\033[0m \033[30mNumber Generator\033[0m
\033[37m6\033[0m \033[30mBeenden\033[0m
              """)
        
        for i, name in enumerate(app_names):
            if auswahl == str(i):
                print(f"{app_names[i]}\033[0m")

        # Geometry Calculator
        if auswahl == "1":
            while True:
                print("\nWas möchten Sie berechnen?")
                print("1. Hypotenuse eines rechtwinkligen Dreiecks")
                print("2. Flächeninhalt eines Kreises")
                print("3. Beenden")

                choice = input("Ihre Wahl (1/2/3): ")

                if choice == '1':
                    try:
                        seite_a = float(input("Gebe die Länge von Seite A an: "))
                        seite_b = float(input("Gebe die Länge von Seite B an: "))

                        print(f"Die Hypotenuse des Dreiecks ist {geometry_calculator.calculate_hypotenuse(seite_a, seite_b):.2f} Einheiten lang.")
                    except ValueError:
                        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")
                elif choice == '2':
                    try:
                        radius = float(input("Bitte geben Sie den Radius an: "))

                        print(f"Die Fläche des Kreises beträgt {geometry_calculator.calculate_circle_area(radius):.2f}.")

                    except ValueError:
                        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                elif choice == '3':
                    print("\033[32mAuf Wiedersehen!\033[0m")
                    break
                else:
                    print("Ungültige Wahl. Bitte wählen Sie 1, 2 oder 3.")

        # Greetings
        if auswahl == "2":
            while True:
                print("\nMöchten sie jemanden begrüßen oder verabschieden?")
                print("1. Begrüßen")
                print("2. Verabschieden")
                print("3. Beenden")

                choice = input("Ihre Wahl (1/2/3): ")

                if choice == '1':
                    while True:
                        name = input("Bitte geben Sie einen Namen an: ")
                        if name.isalpha():
                            greetings.say_hello(name)
                            break
                        else:
                            print("\033[31mUngültige Eingabe.\033[0m")
                elif choice == '2':
                    name = input("Bitte geben Sie einen Namen an: ")
                    while True:
                        if name.isalpha():
                            greetings.say_goodbye(name)
                            break
                        else:
                            print("\033[31mUngültige Eingabe.\033[0m")
                elif choice == '3':
                    print("\033[32mAuf Wiedersehen!\033[0m")
                    break
        
        if auswahl == "3":
            # Math Utils
            print(f"\n2 + 4 = {math_utils.add(2, 4)}")
            print(f"10 - 3 = {math_utils.subtract(10, 3)}")
            print(f"3 * 5 = {math_utils.multiply(3, 5)}")
            print(f"9 / 2 = {math_utils.divide(9, 2)}")
            print(f"9 // 2 = {math_utils.divide(9, 2, isIntegerDivision=True)}")
            print(f"2⁵ = {math_utils.pow(2, 5)}")
            print(f"3. Wurzel aus 81 = {math_utils.root(81, 3)}")

        if auswahl == "4":
            # List Utils
            print()
            liste = ["a", "a", "b", "c", "d", "e", "e"]
            print(f"Liste: {liste}")
            neue_liste = list_utils.remove_duplicates(liste)
            print(f"Liste ohne Duplikate: {neue_liste}")

        if auswahl == "5":
            # Number Generator
            # Generiere eine Liste mit 10 Zufallszahlen zwischen 1 und 50.
            numbers = number_generator.generate_random_numbers(10, 1, 50)
            print(f"\nListe mit 10 zufälligen Zahlen zwischen 1-50: {numbers}")

            # Finde höchsten Wert
            print(f"Höchster Wert aus der Liste: {list_utils.find_max(numbers)}")

        if auswahl == "6":
            print("Das Programm wurde beendet.")
            break