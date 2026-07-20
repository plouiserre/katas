from fastapi import FastAPI
from BirthdayGreetings.adapters.driving.cli import greetings_birthday_employees
from BirthdayGreetings.adapters.driving.controllers import greetings

#greetings_birthday_employees("2026/9/1")

app = FastAPI()

app.include_router(greetings.router)

@app.get("/")
async def root():
    return {"Welcome in this API"}