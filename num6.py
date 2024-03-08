from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{city}")
async def search(city:str):
    n = ["shiraz","Tehran","Isfahan","Yazd","Tabriz","Karaj","Ahvaz","Rasht","Yasuj","Sanandag","Sari","Gorgan","Semnan","Mashhad","Khoramabad","Ilam","Shahrekord","Arak","BandarAbas","Bushehr","Zahedan","Kerman","Kermanshah","Qom","Bojnord","Birjand","Qazvin","Hamedan","Zangan","Urmia","Ardebil",]
    if city in n:
        return {"message":"your city is the center of your province"}
    else:
        return{"None"}
