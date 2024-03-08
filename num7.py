from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{address}")
async def Read(addres: str):
    l = len(addres)
    if  not (0 < l < 101):
        return "message:" "your address is False!"
    return "True"
