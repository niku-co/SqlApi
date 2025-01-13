from flask import Flask, request, jsonify
from app.config import Config
from app.database import get_connection

app = Flask(__name__)

@app.route('/query/<db_name>', methods=['GET'])
def query_db(db_name):
    db_config = Config.DATABASES.get(db_name)
    if not db_config:
        return jsonify({"error": "Database not found"}), 404

    try:
        conn = get_connection(db_config)
        cursor = conn.cursor()
        query = request.args.get("query", "SELECT 1")
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
