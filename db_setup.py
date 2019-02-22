import mysql.connector as mysc

db = mysc.connect(
    host = 'localhost',
    user = 'root',
    password = 'GordonRamsey12321'
)

cursor = db.cursor()

cursor.execute('CREATE DATABASE Squiggle_Rock_Museum')