import mysql.connector

cnx = mysql.connector.connect(user='root', password='remotecontrol',
                              host='127.0.0.1',
                              database='smart_yard')
cnx.close()
