import os
import uuid
from flask import Flask, jsonify, request
from data_manager import JsonDataManager 

app = Flask(__name__)
data_manager = JsonDataManager()

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json')


@app.route('/')
def hello_world():
    return "Hello from Topic and Skill Service!"


@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics)


@app.route('/skills', methods=['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)


@app.route('/topics/<id>', methods=['GET'])
def get_topic_by_id(id):
    topics = data_manager.read_data(TOPICS_FILE)
    topic = next((topic for topic in topics if topic.get('id').lower() == id.lower()), None)
    if topic:
        return jsonify(topic)
    else:
        return jsonify({"error": "Topic not found."}), 404


@app.route('/skills/<id>', methods=['GET'])
def get_skill_by_id(id):
    skills = data_manager.read_data(SKILLS_FILE)
    skill = next((skill for skill in skills if skill.get('id').lower() == id.lower()), None)
    if skill:
        return jsonify(skill)
    else:
        return jsonify({"error": "Skill not found."}), 404
    

@app.route('/topics', methods=['POST'])
def create_topic():
    new_topic_data = request.json

    if not new_topic_data or 'name' not in new_topic_data or 'description' not in new_topic_data:
        return jsonify({"error": "'name' and 'description' for the topic are required in the request body."}), 400

    new_topic_id = str(uuid.uuid4())
    
    topic = {
        "id": new_topic_id,
        "name": new_topic_data['name'],
        "description": new_topic_data['description']
    }

    topics = data_manager.read_data(TOPICS_FILE)
    topics.append(topic)

    data_manager.write_data(TOPICS_FILE, topics)

    return jsonify(topic), 201


@app.route('/skills', methods=['POST'])
def create_skill():
    new_skill_data = request.json

    if not new_skill_data or 'name' not in new_skill_data or 'topicId' not in new_skill_data:
        return jsonify({"error": "'name' and 'topicId' for the skill are required in the request body."}), 400

    new_skill_id = str(uuid.uuid4())
    
    skill = {
        "id": new_skill_id,
        "name": new_skill_data['name'],
        "topicId": new_skill_data['topicId'],
        "difficulty": new_skill_data.get('difficulty', 'unknown')
    }

    skills = data_manager.read_data(SKILLS_FILE)
    skills.append(skill)

    data_manager.write_data(SKILLS_FILE, skills)

    return jsonify(skill), 201


# --- NEUER ENDPUNKT für PUT /topics/<id> ---
@app.route('/topics/<id>', methods=['PUT'])
def update_topic(id):
    # 1. Daten aus dem Request-Body lesen
    updated_data = request.json

    # 2. Validierung der eingehenden Daten
    # Für eine PUT-Anfrage, die eine vollständige Aktualisierung darstellt,
    # erwarten wir, dass alle erforderlichen Felder (name, description) vorhanden sind.
    if not updated_data or 'name' not in updated_data or 'description' not in updated_data:
        return jsonify({"error": "Name und Beschreibung für das Topic sind erforderlich"}), 400

    # 3. Alle Topics laden
    topics = data_manager.read_data(TOPICS_FILE)

    # 4. Topic in der Liste finden und Index speichern
    # Wir suchen nach dem Topic mit der übergebenen ID.
    found_index = -1
    for i, t in enumerate(topics):
        if t['id'] == id:
            found_index = i
            break

    # 5. Überprüfen, ob Topic gefunden wurde
    if found_index == -1:
        # Wenn das Topic nicht gefunden wurde, geben wir 404 Not Found zurück.
        return jsonify({"error": "Topic not found"}), 404

    # 6. Topic aktualisieren
    # Das gefundene Topic wird mit den neuen Daten überschrieben.
    # Wichtig: Die ID bleibt unverändert.
    topics[found_index]['name'] = updated_data['name']
    topics[found_index]['description'] = updated_data['description']
    # Hier könnten weitere Felder aktualisiert werden, falls sie im Request-Body sind.
    # Beispiel: topics[found_index]['prerequisites'] = updated_data.get('prerequisites', [])

    # 7. Aktualisierte Liste speichern
    data_manager.write_data(TOPICS_FILE, topics)

    # 8. Erfolgreiche Antwort zurückgeben
    # Bei erfolgreicher Aktualisierung geben wir den Status 200 OK zurück.
    # Die Antwort enthält die vollständigen Daten des aktualisierten Topics.
    return jsonify(topics[found_index]), 200


# --- NEUER ENDPUNKT für PUT /skills/<id> ---
@app.route('/skills/<id>', methods=['PUT'])
def update_skill(id):
    updated_data = request.json

    # Validierung für Skill-Daten: 'name' und 'topicId' sind erforderlich
    if not updated_data or 'name' not in updated_data or 'topicId' not in updated_data:
        return jsonify({"error": "Name und Topic ID für den Skill sind erforderlich"}), 400

    skills = data_manager.read_data(SKILLS_FILE)

    found_index = -1
    for i, s in enumerate(skills):
        if s['id'] == id:
            found_index = i
            break

    if found_index == -1:
        return jsonify({"error": "Skill not found"}), 404

    # Skill aktualisieren
    skills[found_index]['name'] = updated_data['name']
    skills[found_index]['topicId'] = updated_data['topicId']
    skills[found_index]['difficulty'] = updated_data.get('difficulty', skills[found_index].get('difficulty', 'unknown'))
    # .get('difficulty', skills[found_index].get('difficulty', 'unknown'))
    # Bedeutung: Versuche, 'difficulty' aus den updated_data zu holen.
    # Wenn nicht vorhanden, versuche es aus dem bestehenden Skill zu holen.
    # Wenn auch dort nicht vorhanden, setze 'unknown'.

    data_manager.write_data(SKILLS_FILE, skills)

    return jsonify(skills[found_index]), 200


# --- NEUER ENDPUNKT für DELETE /topics/<id> ---
@app.route('/topics/<id>', methods=['DELETE'])
def delete_topic(id):
    topics = data_manager.read_data(TOPICS_FILE)

    # Topic finden und dessen Index speichern
    found_index = -1
    for i, t in enumerate(topics):
        if t['id'] == id:
            found_index = i
            break

    if found_index == -1:
        # Wenn das Topic nicht gefunden wurde, 404 Not Found
        return jsonify({"error": "Topic not found"}), 404

    # Topic aus der Liste entfernen
    # pop(index) entfernt das Element an der angegebenen Position
    deleted_topic = topics.pop(found_index)

    # Aktualisierte Liste speichern
    data_manager.write_data(TOPICS_FILE, topics)

    # Erfolgreiche Antwort: 204 No Content
    # 204 No Content ist die Best Practice für DELETE-Anfragen, die erfolgreich waren
    # und keine Antwortdaten zurückgeben müssen.
    return '', 204 # Leerer String als Body, 204 als Statuscode


# --- NEUER ENDPUNKT für DELETE /skills/<id> ---
@app.route('/skills/<id>', methods=['DELETE'])
def delete_skill(id):
    skills = data_manager.read_data(SKILLS_FILE)

    found_index = -1
    for i, s in enumerate(skills):
        if s['id'] == id:
            found_index = i
            break

    if found_index == -1:
        return jsonify({"error": "Skill not found"}), 404

    skills.pop(found_index)
    data_manager.write_data(SKILLS_FILE, skills)

    return '', 204
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)