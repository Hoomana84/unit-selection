from fastapi import FastAPI

app = FastAPI()


@app.get("/home/{phone}")
async def reading(phone:str):
    Fn = ["071", "084", "021", "011", "017", "066", "031", "041", "045", "061", "051",
          "056", "058", "028", "026","044", "024", "023", "076", "074", "035", "054"]
    S = int(len(phone))
    M = phone[0:3]
    if (M in Fn) and (len(phone) == 11):
        return {"message": "your phone number have not wrong!"}
    return "None"
