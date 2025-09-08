import mysql.connector

def lentokenttahaku(ICAO):
    sql = f"SELECT name, municipality FROM airport where ident='{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]}, Sijaintikunta: {rivi[1]}")
    return

yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="12345",
        autocommit=True,
        database="flight_game"
        )
icao = input("Anna ICAO koodi: ")
lentokenttahaku(icao)