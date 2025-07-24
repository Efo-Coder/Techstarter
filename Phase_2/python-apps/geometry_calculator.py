import math

def calculate_hypotenuse(side_a, side_b):
    """
    Berechnet die Hypotenuse eines rechtwinkligen Dreiecks.
    Verwendet den Satz des Pythagoras: c = sqrt(a^2 + b^2)
    """
    return math.sqrt(side_a**2 + side_b**2)

def calculate_circle_area(radius):
    """
    Berechnet den Flächeninhalt eines Kreises.
    Formel: A = pi * r^2
    """
    return math.pi * radius**2

if __name__ == "__main__":
    print("Willkommen zum Geometrie-Rechner!")

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

                print(f"Die Hypotenuse des Dreiecks ist {calculate_hypotenuse(seite_a, seite_b):.2f} Einheiten lang.")


            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")
        elif choice == '2':
            try:
                radius = float(input("Bitte geben Sie den Radius an: "))

                print(f"Die Fläche des Kreises beträgt {calculate_circle_area(radius):.2f}.")

            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        elif choice == '3':
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Wahl. Bitte wählen Sie 1, 2 oder 3.")