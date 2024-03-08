from fastapi import FastAPI,HTTPException
import datetime
app = FastAPI()

def validate_shamsi_date(date_str):
    try:
        datetime.strptime(date_str,"%d/%m/%Y")
        return True
    except ValueError:
        return False

@app.get("/validate-shamsi-date/{date}")
async def validate_shamsi_date_endpoint(date:str):
    if validate_shamsi_date(date):
        return {"message":"date is valid "}
    else:
        raise HTTPException(status_code=404,detail="date is invalid")
