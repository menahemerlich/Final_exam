
def soldiers_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
                CREATE TABLE IF NOT EXISTS soldiers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_number TEXT NOT NULL,
                    First_name TEXT NOT NULL,
                    Last_name TEXT NOT NULL,
                    sex TEXT NOT NULL,
                    City TEXT NOT NULL,
                    Distance INT NOT NULL,
                    status TEXT,
                    house_id INT,
                    room_id INT)
                    """)
        conn.commit()
    finally:
        conn.close()

def insert_soldiers(conn, new_soldier):
    cur = conn.cursor()
    try:
        if 8000000 <= int(new_soldier.personal_number) < 9000000:
            cur.execute(
                "INSERT INTO soldiers (personal_number, First_name, Last_name, sex, City, Distance) VALUES (?, ?, ?, ?, ?, ?)",
                (new_soldier.personal_number, new_soldier.First_name, new_soldier.Last_name, new_soldier.sex,
                 new_soldier.City, new_soldier.Distance))
            conn.commit()
    finally:
        conn.close()

def houses(conn):
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS houses (
                house_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)
                """)
    conn.commit()


def rooms(conn):

    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                house_id INT,
                FOREIGN KEY(house_id) REFERENCES houses(id))
                """)
    conn.commit()


def create_houses(conn, houses_num, room_num):
    total_houses = 0
    total_rooms = 0
    houses(conn)
    rooms(conn)
    for _ in range(houses_num):
        total_houses += 1
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO houses (name) VALUES (?)",
            (f"בית מספר {total_houses}",))
        conn.commit()
        for _ in range(room_num):
            total_rooms += 1
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO rooms (name, house_id) VALUES (?, ?)",
                (f"חדר מספר {total_rooms}",total_houses))
            conn.commit()





