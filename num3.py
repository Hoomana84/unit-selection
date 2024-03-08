from fastapi import FastAPI,HTTPException
import datetime
app = FastAPI()

def validate_shamsi_date(date_str):
    try:
        datetime.strptime(date_str,"%d/%m/%Y")
        return True
    except ValueError:
        return False

@app.get("/home/{date}")
async def date(date):
    if validate_shamsi_date(date):
        return {"message":"date is valid "}
    raise HTTPException(status_code=404,detail="date is invalid")
