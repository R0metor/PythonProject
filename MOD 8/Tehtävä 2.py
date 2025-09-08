import mysql.connector
def kentat(maakoodi):
    sql = f"SELECT type, COUNT(*) AS lukumaara FROM airport where iso_country = '{maakoodi.upper()}' GROUP BY type ORDER BY lukumaara DESC"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        print(f"Lentokentät maassa {maakoodi.upper()} tyypeittäin:")
        for tyyppi, lukumaara in tulos:
            print(f"{tyyppi}: {lukumaara} kpl")


yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="12345",
        autocommit=True,
        database="flight_game"
        )
maakoodi = input("Anna maakodi: ")
kentat(maakoodi)