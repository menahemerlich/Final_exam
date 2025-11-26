from fastapi import FastAPI, UploadFile, File, Depends
from sqlmodel import Session

from functions.io_with_csv import read_csv
from models.soldier import Soldier
from db import create_db_and_tables, get_session

app = FastAPI()
create_db_and_tables()

@app.post("/assignWithCsv")
def assign_with_csv(file_name, session: Session = Depends(get_session)):
    data = read_csv(file_name)
    for row in data:
        new_soldier = Soldier(row)
        return new_soldier
        session.add(new_soldier)
        session.commit()





