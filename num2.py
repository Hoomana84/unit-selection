from fastapi import FastAPI

app = FastAPI()

@app.get("/name/{name}")
def checkname(name:str):
    l = len(name)
    n =["آ","ب","پ","ت","ث","ج","چ","ح","خ","د","ذ","ر","ز","ژ","س",
        "ش","ص","ض","ط","ظ","ع","غ","ک","گ","ل","م","ن","و","ه","ی"]
    if (l >= 10) and (name[0:l-1] == n):
        return("message",f'your {name} is True')
    return("message",f'your {name} is True')


