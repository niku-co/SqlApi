from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# پیکربندی اتصال به دیتابیس
DATABASE_CONFIG = {
    "DRIVER": "{ODBC Driver 17 for SQL Server}",
    "SERVER": "c901884d-10d0-4b98-b5d0-e0d930fd85ad.hsvc.ir",
    "PORT": "30802",
    "DATABASE": "DBtest",
    "UID": "sa",
    "PWD": "3zVeYopmN2uUe6aqAyGoXKwZFEa1SjAD",
}


def get_connection():
    """ایجاد اتصال به دیتابیس"""
    try:
        conn = pyodbc.connect(
            f"DRIVER={DATABASE_CONFIG['DRIVER']};"
            f"SERVER={DATABASE_CONFIG['SERVER']},{DATABASE_CONFIG['PORT']};"
            f"DATABASE={DATABASE_CONFIG['DATABASE']};"
            f"UID={DATABASE_CONFIG['UID']};"
            f"PWD={DATABASE_CONFIG['PWD']};"
            f"Encrypt=yes;TrustServerCertificate=yes;"
        )
        return conn
    except Exception as e:
        return str(e)


@app.route("/test-connection", methods=["GET"])
def test_connection():
    """تست اتصال به دیتابیس"""
    conn = get_connection()
    if isinstance(conn, str):  # اگر خطایی رخ دهد
        return jsonify({"success": False, "error": conn}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        return jsonify({"success": True, "result": result[0]})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
