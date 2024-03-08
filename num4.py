from fastapi import FastAPI

app = FastAPI()


@app.get("/serial/{serial}")
def serial(serial):
    z = ["آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س",
         "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"]
    if not len(serial) == 9:
        return "تعداد کارکتر ها نادرست است"
    if not serial[1:3] == int:
        return "قسمت 2 رقمی اعداد نادرست است "
    if not serial[3:10] == int:
        return "قسمت 6 رقمی اعداد نادرست است "
    if not serial[0:1] in z:
        return "قسمت حروف شناسنامه نادرست است"
    return "ورودی شما درست است "
