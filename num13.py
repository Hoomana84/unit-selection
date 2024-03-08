from fastapi import FastAPI


app = FastAPI()


@app.get("/home/{life}")
async def cla(life :str):
    Fate = ["مجرد","متاهل"]
    if life in Fate and life == "مجرد":
        return{"message:"f'شما مجرد هستید'}
    else:
        return{"message":f'شما متاهل هستید'}

