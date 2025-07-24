import json
import re

"""
Ein einfaches Python-Programm zur Verwaltung eines Kundenmanagement-Systems (CRM).
Es ermöglicht das Hinzufügen, Anzeigen, Suchen, Aktualisieren und Löschen von Kunden
sowie das Speichern und Laden der Kundendaten in/aus einer JSON-Datei.
"""

# Globale Variable zum Speichern der Kundendaten
# Schlüssel: Kundenname (String), Wert: Dictionary mit Kundendetails
kunden = {}
DATEINAME = "kunden.json" # Dateiname für die Speicherung des Katalogs

def kunden_anzeigen():
    """
    Zeigt alle Kunden im aktuellen CRM-Katalog an.
    Gibt eine Meldung aus, wenn der Katalog leer ist.
    """
    if not kunden:
        print("Der Katalog ist leer.")
        return

    print("\n--- Deine Kundenliste ---")
    # Iteriere durch das Kunden-Dictionary und zeige Details an
    for name, details in kunden.items():
        print(f"Name: {name}")
        # Verwende .get() mit Standardwert 'N/A', falls ein Detail fehlt
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def kunde_hinzufuegen():
    """
    Fügt einen neuen Kunden zum CRM-Katalog hinzu.
    Fragt den Benutzer nach Name, E-Mail und Telefonnummer.
    Validiert die Eingaben für E-Mail und Telefonnummer.
    Verhindert das Hinzufügen von Kunden mit bereits existierendem Namen.
    """
    print("\n--- Kunden hinzufügen ---")
    while True:
        name = input("Name des Kunden: ")
        if name and name.isalpha():
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

    # Validierung für E-Mail: Schleife, bis ein gültiges Format eingegeben wird
    while True:
        email = input("E-Mail des Kunden: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email): # Einfache E-Mail-Validierung
            break
        else:
            print("Ungültiges E-Mail-Format. Bitte versuchen Sie es erneut.")

    # Validierung für Telefonnummer: Schleife, bis nur Ziffern (optional mit +) eingegeben werden
    while True:
        telefon = input("Telefonnummer des Kunden: ")
        # Prüft, ob die Telefonnummer nur Ziffern enthält (optional: + am Anfang erlauben)
        if telefon.replace('+', '').isdigit() and (telefon.startswith('+') or not telefon.startswith('+')):
            break
        else:
            print("Ungültige Telefonnummer. Bitte geben Sie nur Ziffern ein (optional mit + am Anfang).")

    # Überprüfe, ob der Name bereits existiert, um Duplikate zu vermeiden
    if name in kunden:
        print(f"Fehler: Kunde '{name}' existiert bereits im Katalog.")
        return

    # Speichere die Kundendetails als verschachteltes Dictionary
    kunden[name] = {
        "email": email,
        "telefon": telefon
    }
    print(f"Kunde '{name}' wurde hinzugefügt.")

def kunde_suchen():
    """
    Sucht Kunden im Katalog basierend auf einem Teil des Namens oder der E-Mail-Adresse.
    Zeigt alle passenden Kunden mit ihren Details an.
    """
    print("\n--- Kunden suchen ---")
    # Suchbegriff in Kleinbuchstaben umwandeln für case-insensitive Suche
    suchbegriff = input("Geben Sie einen Suchbegriff (Name oder E-Mail) ein: ").lower()
    gefundene_kunden = {}

    # Iteriere durch alle Kunden im Katalog
    for name, details in kunden.items():
        # Überprüfe, ob der Suchbegriff im Namen oder in der E-Mail enthalten ist
        if suchbegriff in name.lower() or suchbegriff in details.get('email', '').lower():
            gefundene_kunden[name] = details

    # Wenn keine Kunden gefunden wurden
    if not gefundene_kunden:
        print(f"Keine Kunden gefunden, die '{suchbegriff}' im Namen oder in der E-Mail enthalten.")
        return

    print(f"\n--- Gefundene Kunden für '{suchbegriff}' ---")
    # Zeige die Details der gefundenen Kunden an
    for name, details in gefundene_kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def kunde_aktualisieren():
    """
    Aktualisiert die E-Mail-Adresse und/oder Telefonnummer eines bestehenden Kunden.
    Fragt den Benutzer nach dem Kundennamen und dann nach den neuen Daten.
    Leere Eingaben für E-Mail/Telefon lassen die bestehenden Werte unverändert.
    """
    print("\n--- Kunden aktualisieren ---")
    name_zu_aktualisieren = input("Name des zu aktualisierenden Kunden: ")

    if name_zu_aktualisieren not in kunden:
        print(f"Fehler: Kunde '{name_zu_aktualisieren}' nicht im Katalog gefunden.")
        return

    print(f"Aktuelle Daten für {name_zu_aktualisieren}:")
    print(f"  E-Mail: {kunden[name_zu_aktualisieren]['email']}")
    print(f"  Telefon: {kunden[name_zu_aktualisieren]['telefon']}")

    neue_email = input("Neue E-Mail (leer lassen für keine Änderung): ")
    if neue_email: # Nur validieren und aktualisieren, wenn eine Eingabe gemacht wurde
        while not re.match(r"[^@]+@[^@]+\.[^@]+", neue_email):
            print("Ungültiges E-Mail-Format. Bitte versuchen Sie es erneut.")
            neue_email = input("Neue E-Mail (leer lassen für keine Änderung): ")
        kunden[name_zu_aktualisieren]['email'] = neue_email

    neue_telefon = input("Neue Telefonnummer (leer lassen für keine Änderung): ")
    if neue_telefon: # Nur validieren und aktualisieren, wenn eine Eingabe gemacht wurde
        while not (neue_telefon.replace('+', '').isdigit() and (neue_telefon.startswith('+') or not neue_telefon.startswith('+'))):
            print("Ungültige Telefonnummer. Bitte geben Sie nur Ziffern ein (optional mit + am Anfang).")
            neue_telefon = input("Neue Telefonnummer (leer lassen für keine Änderung): ")
        kunden[name_zu_aktualisieren]['telefon'] = neue_telefon

    print(f"Kunde '{name_zu_aktualisieren}' wurde aktualisiert.")

def kunde_loeschen():
    """
    Löscht einen Kunden aus dem Katalog anhand seines Namens.
    Gibt eine Fehlermeldung aus, wenn der Kunde nicht gefunden wird.
    """
    print("\n--- Kunden löschen ---")
    titel_zu_loeschen = input("Name des zu löschenden Kunden: ")
    if titel_zu_loeschen in kunden:
        del kunden[titel_zu_loeschen]
        print(f"Kunde '{titel_zu_loeschen}' wurde aus dem Katalog entfernt.")
    else:
        print(f"Fehler: Kunde '{titel_zu_loeschen}' nicht im Katalog gefunden.")

def katalog_speichern():
    """
    Speichert den aktuellen Kundenkatalog in einer JSON-Datei.
    Der Dateiname wird durch die globale Variable DATEINAME definiert.
    Behandelt IOError bei Problemen mit der Dateispeicherung.
    """
    try:
        with open(DATEINAME, 'w', encoding='utf-8') as f:
            json.dump(kunden, f, indent=4, ensure_ascii=False)
        print(f"\033[32mKatalog erfolgreich in\033[0m '\033[34m{DATEINAME}\033[0m' \033[32mgespeichert.\033[0m")
    except IOError as e:
        print(f"Fehler beim Speichern des Katalogs: {e}")

def katalog_laden():
    """
    Lädt den Kundenkatalog aus einer JSON-Datei.
    Der Dateiname wird durch die globale Variable DATEINAME definiert.
    Initialisiert den Katalog neu, wenn die Datei nicht gefunden wird
    oder ungültiges JSON enthält.
    """
    global kunden
    try:
        with open(DATEINAME, 'r', encoding='utf-8') as f:
            kunden.update(json.load(f))
        print(f"Katalog erfolgreich aus '{DATEINAME}' geladen.")
    except FileNotFoundError:
        print("Keine vorhandene Katalogdatei gefunden. Starte mit leerem Katalog.")
        kunden.clear()
    except json.JSONDecodeError as e:
        print(f"Fehler beim Laden des Katalogs (ungültiges JSON): {e}. Starte mit leerem Katalog.")
        kunden.clear()
    except Exception as e:
        print(f"Ein unerwarteter Fehler beim Laden ist aufgetreten: {e}. Starte mit leerem Katalog.")
        kunden.clear()

def zeige_menue():
    """
    Zeigt das Hauptmenü des CRM-Systems an.
    """
    print("\n\033[30m---\033[0m \033[33mCRM Menü\033[0m \033[30m---\033[0m")
    print("\033[36m1\033[0m. Kunde hinzufügen")
    print("\033[36m2\033[0m. Kunden anzeigen")
    print("\033[36m3\033[0m. Kunde suchen")
    print("\033[36m4\033[0m. Kunde aktualisieren")
    print("\033[36m5\033[0m. Kunde löschen")
    print("\033[36m6\033[0m. Beenden")
    print("\033[30m----------------\033[0m")

def main():
    """
    Die Hauptfunktion des Programms.
    Lädt den Katalog beim Start, zeigt das Menü an und verarbeitet Benutzereingaben.
    Speichert den Katalog beim Beenden.
    """
    katalog_laden()
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            kunde_hinzufuegen()
        elif wahl == '2':
            kunden_anzeigen()
        elif wahl == '3':
            kunde_suchen()
        elif wahl == '4':
            kunde_aktualisieren()
        elif wahl == '5':
            kunde_loeschen()
        elif wahl == '6':
            katalog_speichern()
            print("\033[32mProgramm wird beendet. Auf Wiedersehen!\033[0m")
            break
        else:
            print("\033[31mUngültige Eingabe. Bitte versuchen Sie es erneut.\033[0m")

if __name__ == "__main__":
    main()