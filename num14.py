from fastapi import FastAPI

app = FastAPI()


@app.get("/code/{number}")
async def Validation(number: str):
    l = len(number)
    Total = 0
    for i in range(0, l - 1):
        c = ord(number[i])
        c = c - 48
        Total = Total + c * (l - i)
    r = Total % 11
    c = ord(number[l - 1])
    c -= 48
    if r > 2:
        r = 11 - r
    if r == c:
        return "this number is valid"
    else:
        return "this number have wrong!"
