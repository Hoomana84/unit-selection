from fastapi import FastAPI


app = FastAPI()


@app.get("/home/{life}")
async def cla(life :str):
    Fate = ["مجرد","متاهل"]
    if life in Fate and life == "مجرد":
        return "'شما مجرد هستید"
    return "شما متاهل هستید"

