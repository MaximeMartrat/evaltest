import mysql.connector

connection_params = {
    'host': "localhost",
    'user': "user",
    'password': "password",
    'database': "db",
}

with mysql.connector.connect(**connection_params) as db:
    with db.cursor() as c:
        c.execute("INSERT INTO utilisateur (nom, score, actif) \
                   VALUES ('david', 10, True)")
        db.commit()