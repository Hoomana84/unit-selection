from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{address}")
async def Read(addres: str):
    l = len(addres)
    if (0 < l < 101):
        return "message:" "your address is True!"
    else:
        return "None"
