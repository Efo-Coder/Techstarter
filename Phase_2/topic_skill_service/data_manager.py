# Importieren von Modulen zur Arbeit mit JSON und Dateisystem
import json
import os

# Definition einer Klasse zur Verwaltung von JSON-Daten
class JsonDataManager:
    def __init__(self):
        # Konstruktor – derzeit ohne spezielle Initialisierung
        pass

    # Methode zum Lesen von JSON-Daten aus einer Datei
    def read_data(self, filepath):
        # Wenn die Datei nicht existiert, gib eine leere Liste zurück
        if not os.path.exists(filepath):
            return []

        try:
            # Öffne die Datei im Lesemodus mit UTF-8-Kodierung
            with open(filepath, 'r', encoding='utf-8') as file:
                # Lese den JSON-Inhalt und gib ihn zurück
                return json.load(file)
        except json.JSONDecodeError:
            # Fehler bei ungültiger JSON-Syntax
            print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
            return []
        except Exception as e:
            # Allgemeine Fehlerbehandlung
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
            return []

    # Methode zum Schreiben von Daten in eine JSON-Datei
    def write_data(self, filepath, data):
        # Erstelle den Zielordner, falls er noch nicht existiert
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        try:
            # Öffne die Datei im Schreibmodus mit UTF-8-Kodierung
            with open(filepath, 'w', encoding='utf-8') as file:
                # Schreibe die Daten im JSON-Format in die Datei, schön formatiert (indent=4)
                json.dump(data, file, indent=4)
                return True
        except Exception as e:
            # Allgemeine Fehlerbehandlung beim Schreiben
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Schreiben von {filepath}: {e}")
            return False