from fastapi import FastAPI

app = FastAPI()


@app.get("/home/{phone}")
def reading(phone: str):
    l = int(len(phone))
    if  l != 11 or phone[0:2] != '09':
        return "FALSE"
    return "TRUE"
