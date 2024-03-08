from fastapi import FastAPI

app = FastAPI()

@app.get("/Univercity/{st_id}")
def checking(st):
    l = len(st)
    st_id = int(st)
    if l == 11:
        year = (st // 100000000)
        if 400 <= year <= 402:
            Fixed = (st // 100) - (year * 1000000)
            if Fixed == 114150:
                last = st % 100
                if 0 < last < 100:
                    return f'شماره دانشجویی صحیح است'
                return f'قسمت اندیس اشتباه است '
            return f'قسمت ثابت اشتباه است'
        return f'قسمت سال اشتباه است'
    return f'شماره دانشجویی وارد شده نادرست است '



#---------------------------------------------------------------------------------------

from fastapi import FastAPI

app = FastAPI()

@app.get("/name/{name}")
async def checkname(name:str):
    l = len(name)
    n =["آ","ب","پ","ت","ث","ج","چ","ح","خ","د","ذ","ر","ز","ژ","س",
        "ش","ص","ض","ط","ظ","ع","غ","ک","گ","ل","م","ن","و","ه","ی"]
    if (l >= 10) and (name[0:l-1] == n):
        return("message",f'your {name} is True')
    return("message",f'your {name} is True')


#----------------------------------------------------------------------------------