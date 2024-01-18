from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import db
from tambola_ticket import TambolaTicket
from create_tambola_ticket import generate_tambola_ticket_set
from fastapi.encoders import jsonable_encoder
from get_all_tambola_tickets import get_all_tambola_tickets

app = FastAPI()


@app.on_event("startup")
def startup():
    db.connect()
    # db.create_tables([TambolaTicket])

@app.on_event("shutdown")
def shutdown():
    db.close()

@app.get("/")
def read_root():
    return "WELCOME TO TAMBOLA TICKET GENERATOR"

@app.post("/generate_tickets/{num_of_sets}")
def generate_tickets(num_of_sets: int):
    tickets = []
    for i in range(num_of_sets):
        tickets.append(generate_tambola_ticket_set())
    return JSONResponse(status_code=200, content = {"tickets" : tickets})

@app.get("/get_tickets")
def get_tickets(page: int,page_limit: int):
    tickets = get_all_tambola_tickets(page, page_limit)
    return JSONResponse(status_code=200, content = {"tickets" : jsonable_encoder(tickets)})
