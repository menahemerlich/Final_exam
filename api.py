from fastapi import FastAPI, UploadFile, File, Depends
import sqlite3
from functions.io_with_csv import read_csv
from models.soldier import Soldier
from functions.create_table import soldiers_table, insert_soldiers, create_houses
from inlay_strategy import inlay_strategy

app = FastAPI()
DB_PATH = "soldiers.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

@app.post("/assignWithCsv")
def assign_with_csv(file_name):
    conn = get_connection()
    create_houses(conn, 2, 10)
    soldiers_table(conn)

    data = read_csv(file_name)
    for row in data:
        conn = get_connection()
        new_soldier = Soldier(**row)
        insert_soldiers(conn, new_soldier)
    conn = get_connection()
    inlay_strategy(conn)







