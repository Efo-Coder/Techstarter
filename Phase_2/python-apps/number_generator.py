import random
import list_utils

def generate_random_numbers(count, min_val, max_val):
    """
    Generiert eine Liste von Zufallszahlen.
    """
    numbers = []
    # TODO 4: Generiere 'count' viele Zufallszahlen zwischen 'min_val' und 'max_val' und füge sie der Liste 'numbers' hinzu. Nutze random.randint().
    while count > 0:
        count -= 1
        numbers.append(random.randint(min_val, max_val))
    return numbers


# if __name__ == "__main__":
#     print("Willkommen zum Zufallszahlen-Generator und Listen-Helfer!")

#     numbers = generate_random_numbers(10, 1, 50)
#     # TODO 6: Finde die größte Zahl in der generierten Liste und gib sie aus.
#     print(list_utils.find_max(numbers))

#     # TODO 7: Erstelle eine Liste mit Duplikaten zum Testen.

#     # TODO 8: Entferne Duplikate aus der Liste und gib die bereinigte Liste aus.

#     print("Bitte implementieren Sie die TODOs, um die App zu starten!")