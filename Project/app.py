from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    con = sqlite3.connect('RHYM(database).db')
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/threat_actors1', methods=['GET'])
def get_threat_actors1():
    result = query_db('SELECT * FROM malpedia_ThreatActors1')
    return jsonify(result)

@app.route('/threat_actors2', methods=['GET'])
def get_threat_actors2():
    result = query_db('SELECT * FROM malpedia_ThreatActors2')
    return jsonify(result)

@app.route('/malware', methods=['GET'])
def get_malware():
    result = query_db('SELECT * FROM malpedia_malware')
    return jsonify(result)

@app.route('/techniques_enterprise', methods=['GET'])
def get_techniques_enterprise():
    result = query_db('SELECT * FROM mitre_TechniquesEnterprise')
    return jsonify(result)

@app.route('/techniques_ics', methods=['GET'])
def get_techniques_ics():
    result = query_db('SELECT * FROM mitre_TechniquesICS')
    return jsonify(result)

@app.route('/techniques_mobile', methods=['GET'])
def get_techniques_mobile():
    result = query_db('SELECT * FROM mitre_TechniquesMobile')
    return jsonify(result)

@app.route('/mitre_threat_actors', methods=['GET'])
def get_mitre_threat_actors():
    result = query_db('SELECT * FROM mitre_ThreatActors')
    return jsonify(result)

@app.route('/mitre_malware', methods=['GET'])
def get_mitre_malware():
    result = query_db('SELECT * FROM mitre_malware')
    return jsonify(result)

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True)
