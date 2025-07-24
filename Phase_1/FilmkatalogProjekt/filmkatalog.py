import json

"""
Ein einfaches Python-Programm zur Verwaltung eines Filmkatalogs.
Es ermöglicht das Hinzufügen, Anzeigen, Suchen und Löschen von Filmen
sowie das Speichern und Laden des Katalogs in/aus einer JSON-Datei.
"""

# Globale Variable zum Speichern der Filmdaten
# Schlüssel: Filmtitel (String), Wert: Dictionary mit Filmdetails
filme = {}
DATEINAME = "filme.json" # Dateiname für die Speicherung des Katalogs

def filme_anzeigen():
    """
    Zeigt alle Filme im aktuellen Katalog an.
    Gibt eine Meldung aus, wenn der Katalog leer ist.
    """
    if not filme:
        print("Der Katalog ist leer.")
        return

    print("\n--- Dein Filmkatalog ---")
    # Iteriere durch das Filme-Dictionary und zeige Details an
    for titel, details in filme.items():
        print(f"Titel: {titel}")
        # Verwende .get() mit Standardwert 'N/A', falls ein Detail fehlt (für ältere Einträge)
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print(f"  Genre: {details.get('genre', 'N/A')}")
        print(f"  Bewertung: {details.get('bewertung', 'N/A')}")
        print("-----------------------")

def film_hinzufuegen():
    """
    Fügt einen neuen Film zum Katalog hinzu.
    Fragt den Benutzer nach Titel, Regisseur, Jahr, Genre und Bewertung.
    Validiert die Eingaben für Jahr und Bewertung.
    Verhindert das Hinzufügen von Filmen mit bereits existierendem Titel.
    """
    print("\n--- Film hinzufügen ---")
    titel = input("Titel des Films: ")
    regisseur = input("Regisseur des Films: ")

    # Validierung für das Jahr: Schleife, bis eine gültige Zahl eingegeben wird
    while True:
        jahr_str = input("Erscheinungsjahr des Films: ")
        try:
            jahr = int(jahr_str)
            break
        except ValueError:
            print("Ungültige Eingabe. Das Jahr muss eine Zahl sein.")

    genre = input("Genre des Films: ")

    # Validierung für die Bewertung: Schleife, bis eine Zahl zwischen 1 und 5 eingegeben wird
    while True:
        bewertung_str = input("Bewertung (1-5 Sterne): ")
        try:
            bewertung = int(bewertung_str)
            if 1 <= bewertung <= 5:
                break
            else:
                print("Ungültige Bewertung. Bitte geben Sie eine Zahl zwischen 1 und 5 ein.")
        except ValueError:
            print("Ungültige Eingabe. Die Bewertung muss eine Zahl sein.")

    # Überprüfe, ob der Titel bereits existiert, um Duplikate zu vermeiden
    if titel in filme:
        print(f"Fehler: Film '{titel}' existiert bereits im Katalog.")
        return

    # Speichere die Filmdetails als verschachteltes Dictionary
    filme[titel] = {
        "regisseur": regisseur,
        "jahr": jahr,
        "genre": genre,
        "bewertung": bewertung
    }
    print(f"Film '{titel}' wurde hinzugefügt.")

def film_suchen():
    """
    Sucht Filme im Katalog basierend auf einem Teil des Titels.
    Zeigt alle passenden Filme mit ihren Details an.
    """
    print("\n--- Film suchen ---")
    # Suchbegriff in Kleinbuchstaben umwandeln für case-insensitive Suche
    suchbegriff = input("Geben Sie einen Suchbegriff für den Titel ein: ").lower()
    gefundene_filme = {}

    # Iteriere durch alle Filme im Katalog
    for titel, details in filme.items():
        # Überprüfe, ob der Suchbegriff im Titel (kleingeschrieben) enthalten ist
        if suchbegriff in titel.lower():
            gefundene_filme[titel] = details

    # Wenn keine Filme gefunden wurden
    if not gefundene_filme:
        print(f"Keine Filme gefunden, die '{suchbegriff}' im Titel enthalten.")
        return

    print(f"\n--- Gefundene Filme für '{suchbegriff}' ---")
    # Zeige die Details der gefundenen Filme an
    for titel, details in gefundene_filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print(f"  Genre: {details.get('genre', 'N/A')}")
        print(f"  Bewertung: {details.get('bewertung', 'N/A')}")
        print("-----------------------")

def film_loeschen():
    """
    Löscht einen Film aus dem Katalog anhand seines Titels.
    Gibt eine Fehlermeldung aus, wenn der Film nicht gefunden wird.
    """
    print("\n--- Film löschen ---")
    titel_zu_loeschen = input("Titel des zu löschenden Films: ")
    if titel_zu_loeschen in filme:
        del filme[titel_zu_loeschen] # Entferne den Film aus dem Dictionary
        print(f"Film '{titel_zu_loeschen}' wurde aus dem Katalog entfernt.")
    else:
        print(f"Fehler: Film '{titel_zu_loeschen}' nicht im Katalog gefunden.")

def katalog_speichern():
    """
    Speichert den aktuellen Filmkatalog in einer JSON-Datei.
    Der Dateiname wird durch die globale Variable DATEINAME definiert.
    Behandelt IOError bei Problemen mit der Dateispeicherung.
    """
    try:
        # Öffne die Datei im Schreibmodus ('w') mit UTF-8-Kodierung
        with open(DATEINAME, 'w', encoding='utf-8') as f:
            # Speichere das 'filme'-Dictionary als JSON in der Datei
            # indent=4 für schöne Formatierung, ensure_ascii=False für Umlaute
            json.dump(filme, f, indent=4, ensure_ascii=False)
        print(f"Katalog erfolgreich in '{DATEINAME}' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern des Katalogs: {e}")

def katalog_laden():
    """
    Lädt den Filmkatalog aus einer JSON-Datei.
    Der Dateiname wird durch die globale Variable DATEINAME definiert.
    Initialisiert den Katalog neu, wenn die Datei nicht gefunden wird
    oder ungültiges JSON enthält.
    """
    global filme # Erlaube den Zugriff auf die globale 'filme'-Variable
    try:
        # Versuche, die Datei im Lesemodus ('r') zu öffnen
        with open(DATEINAME, 'r', encoding='utf-8') as f:
            filme.update(json.load(f)) # Lade die JSON-Daten in das 'filme'-Dictionary
        print(f"Katalog erfolgreich aus '{DATEINAME}' geladen.")
    except FileNotFoundError:
        # Wenn die Datei nicht existiert, ist das normal beim ersten Start
        print("Keine vorhandene Katalogdatei gefunden. Starte mit leerem Katalog.")
        filme.clear() # Leere das Dictionary, falls es Reste enthält
    except json.JSONDecodeError as e:
        # Wenn die Datei existiert, aber kein gültiges JSON enthält
        print(f"Fehler beim Laden des Katalogs (ungültiges JSON): {e}. Starte mit leerem Katalog.")
        filme.clear()
    except Exception as e:
        # Fange alle anderen unerwarteten Fehler ab
        print(f"Ein unerwarteter Fehler beim Laden ist aufgetreten: {e}. Starte mit leerem Katalog.")
        filme.clear()

def zeige_menue():
    """
    Zeigt das Hauptmenü des Filmkatalogs an.
    """
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Film suchen")
    print("4. Film löschen")
    print("5. Beenden")
    print("------------------------")

def main():
    """
    Die Hauptfunktion des Programms.
    Lädt den Katalog beim Start, zeigt das Menü an und verarbeitet Benutzereingaben.
    Speichert den Katalog beim Beenden.
    """
    katalog_laden() # Katalog beim Start laden
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3':
            film_suchen()
        elif wahl == '4':
            film_loeschen()
        elif wahl == '5':
            katalog_speichern() # Katalog vor dem Beenden speichern
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")


# Startet das Hauptprogramm, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()