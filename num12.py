from fastapi import FastAPI

app = FastAPI()

@app.get("/Uni/{Reshte}")
def read(Reshte:str) :
    M = ["مهندسی برق", "متالوروژی", " مهندسی کامپیوتر", 'مهندسی مکانیک', "مهندسی عمران", "مهندسی معدن",
         "شیمی کاربردی", "الکترونیک", "شیمی محض", "مهندسی صنایع"]
    if Reshte not  in  M:
        return ("نام دانشکده وارد شده نادرست است ")
    return "نام ئانشکده وارد شده صحیح است "