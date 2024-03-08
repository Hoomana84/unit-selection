from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{Postal code}")
async def checkin (postal_code):
    l = len(postal_code)
    if l != 10:
        return ("your postal code is False!")
    return ("True")
