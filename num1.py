from fastapi import FastAPI

app = FastAPI()

@app.get("/Univercity/{st}")
def checking(st):
    l = len(st)
    st = int(st)
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
