
import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="",  # password
                     db="dbbank")  # name of the database


def cek_data():
    try:
        c = db.cursor()

        NO_rek = "1301160802"

        c.execute("SELECT * FROM customer WHERE no_rek =" + NO_rek + "")

        result = c.fetchone()

        nama_orgtua = result[1]
        nama = result[2]

        response = """ Nama orang tua saudara {} . Pemilik ATM yang bernama {} , atm saudara sudah di blok """.format(nama_orgtua, nama)
        print(response)
    finally:
        db.close()

cek_data()