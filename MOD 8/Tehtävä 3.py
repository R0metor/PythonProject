import mysql.connector
from geopy import distance
def koordinaatit(ICAO):
    sql = (f"SELECT latitude_deg, longitude_deg FROM airport where ident = '{ICAO}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="12345",
    autocommit=True,
    database="flight_game"
)

icao1 = input("Anna ensimmäisen lentokentän ICAO koodi:")
icao2 = input("Anna toisen lentoknetän ICAO koodi:")

coord1 = koordinaatit(icao1)
coord2 = koordinaatit(icao2)

if coord1 and coord2:
    print(f"Lentokenttien välinen etäisyys on {distance.distance(coord1, coord2).km:.2f} km")
else:
    print("Virhe, ei löytynyt")
