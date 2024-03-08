from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{city}")
async def search(city:str):
    n = ["shiraz","Tehran","Isfahan","Yazd","Tabriz","Karaj","Ahvaz","Rasht","Yasuj","Sanandag","Sari","Gorgan","Semnan","Mashhad","Khoramabad","Ilam","Shahrekord","Arak","BandarAbas","Bushehr","Zahedan","Kerman","Kermanshah","Qom","Bojnord","Birjand","Qazvin","Hamedan","Zangan","Urmia","Ardebil",]
    if city  not in  n:
        return {"message":"your city is not the center of your province"}
    return{"True"}
