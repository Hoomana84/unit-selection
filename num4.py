from fastapi import FastAPI

app = FastAPI()

@app.get("/Date/{Date}")
def Valid (Date):
    if  (Date)[:6] not in range(1300, 1402):
        return "تاریخ وارد شده نادرست است."
    return "تاریخ وارد شده صحیح است"