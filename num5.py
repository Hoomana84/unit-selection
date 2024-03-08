from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{Provins}")
async def cheking(Provins:str):
    m =  ["Yazd","Fars","Lorestan","Isfahan","Hamadan","Hormozgan","Markazi","Mazindaran","Gilan","Golestan","Kermanshah","Kohkiluie boier ahmad","Kerman","Kordestan","Qom","Qazvin","Sistan & Balochestan","Semnan","Zanjan","Khozestan","Khorasan shomali","Khorasan razavi","Khorasan jonobi","Chaharmahal & bakhtiari","Tehran","Bushehr","Ilam","Alborz","Ardebil","Azerbaijan sharghi","azerbaigan gharbi"]
    if Provins in m:
        return {"your Province is Official"}
    else:
        return{"your Province is not Official"}
