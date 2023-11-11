import sqlite3


def fetch_stations():
    connection = sqlite3.connect('sqll.db')
    try:
        cursor = connection.cursor()
        cursor.execute('''select ID, LATITUDE, LONGITUDE from STATIONS''')

        return cursor.fetchall()

    except Exception as e:
        print(e)
    finally:
        connection.close()


def fetch_stations_net():
    connection = sqlite3.connect('sqll.db')
    try:
        cursor = connection.cursor()
        cursor.execute('''select STARTID, ENDID, DISTANCE from STATIONS_NET''')
        return cursor.fetchall()

    except Exception as e:
        print(e)
    finally:
        connection.close()


def fetch_stations_net_with_positions():
    connection = sqlite3.connect('sqll.db')
    try:
        cursor = connection.cursor()
        cursor.execute('''
        select S1.ID AS LID,
               S1.LATITUDE AS LLATITUDE,
               S1.LONGITUDE AS LLONGITUDE,
               S2.ID AS RID,
               S2.LATITUDE AS RLATITUDE,
               S2.LONGITUDE AS RLONGITUDE,
               DISTANCE
        from STATIONS_NET
                 join STATIONS S1 on S1.ID = STATIONS_NET.STARTID
                 join STATIONS S2 on S2.ID = STATIONS_NET.ENDID
        ''')

        return cursor.fetchall()

    except Exception as e:
        print(e)
    finally:
        connection.close()
