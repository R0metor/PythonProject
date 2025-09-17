from flask import Flask, jsonify, abort
import mysql.connector

app = Flask(__name__)

def yhteys():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="12345",
        database="flight_game",
        autocommit = True
        )

@app.get("/kenttä/<icao>")
def hae_kentta(icao: str):
    icao = icao.upper()

    try:
        connection = yhteys()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""select ident as ICAO, name as Name, municipality as Municipality 
                          from airport 
                          where ident = %s
                       """, (icao,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()

    except Exception as ex:
        abort(500, desc=f"Tietokantavirhe: {ex}")

    if row is None:
        abort(404, desc="Kenttää ei löytynyt")

    return jsonify({"ICAO": row["ICAO"], "Name": row["Name"], "Municipality": row["Municipality"],})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=False)