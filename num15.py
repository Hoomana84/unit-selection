
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    st: str
    name : str
    date : str
    number : str
    Reshteh: str
    Reshte: str
    phone : str
    life : str
    serial :str
    provins: str
    city: str
    address:str
    postal_code: str
    phone: str



@app.post("/home/")
def checking(student: Item):
    l = len(student.st)
    st = int(student.st)
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



#---------------شناسنامه ---------------------------------------------------2



    l = len(name)
    n =["آ","ب","پ","ت","ث","ج","چ","ح","خ","د","ذ","ر","ز","ژ","س",
        "ش","ص","ض","ط","ظ","ع","غ","ک","گ","ل","م","ن","و","ه","ی"]
    if (l >= 10) and (name[0:l-1] == n):
        return("message",f'your {name} is True')



#-تاریخ تولد -----------3



    try:
        datetime.strptime(date_str,"%d/%m/%Y")
        return True
    except ValueError:
        return False


    if validate_shamsi_date(date):
        return {"message":"date is valid "}
    raise HTTPException(status_code=404,detail="date is invalid")

#------------------------------------4from



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


#------------------------------------------------------------------------------------------------------------------5



    m =  ["Yazd","Fars","Lorestan","Isfahan","Hamadan","Hormozgan","Markazi","Mazindaran","Gilan","Golestan"
        ,"Kermanshah","Kohkiluie boier ahmad","Kerman","Kordestan","Qom","Qazvin","Sistan & Balochestan","Semnan"
        ,"Zanjan","Khozestan","Khorasan shomali","Khorasan razavi","Khorasan jonobi","Chaharmahal & bakhtiari",
          "Tehran","Bushehr","Ilam","Alborz","Ardebil","Azerbaijan sharghi","azerbaigan gharbi"]
    if Provins  not in m:
        return "your Province is not  Official"


#-----------------------------------------------------------------------------------------------------6


    n = ["shiraz","Tehran","Isfahan","Yazd","Tabriz","Karaj","Ahvaz","Rasht","Yasuj","Sanandag","Sari",
         "Gorgan","Semnan","Mashhad","Khoramabad","Ilam","Shahrekord","Arak","BandarAbas","Bushehr","Zahedan",
         "Kerman","Kermanshah","Qom","Bojnord","Birjand","Qazvin","Hamedan","Zangan","Urmia","Ardebil",]
    if city  not in  n:
        return {"message":"your city is not the center of your province"}

#کدیافتن آدرس  درست ------------------------------------------------------------------------------------




    l = len(addres)
    if  not (0 < l < 101):
        return "message:" "your address is False!"


#--------------------------------------------------------------------------------------------------------8



    l = len(postal_code)
    if l != 10:
        return ("your postal code is False!")
    return ("True")

#-------------------------------------------------کد شماره 9------------------------------------------



    l = int(len(phone))
    if  l != 11 or phone[0:2] != '09':
        return "FALSE"


#--------------------------------------کد شماره 10 ----------------------------------------------



    Fn = ["071", "084", "021", "011", "017", "066", "031", "041", "045", "061", "051",
          "056", "058", "028", "026","044", "024", "023", "076", "074", "035", "054"]
    S = int(len(phone))
    M = phone[0:3]
    if (M in Fn) and (len(phone) == 11):
        return {"message": "your phone number have not wrong!"}

#----------------------------------------------کد شماره 11---------------------------------------



    Names = ["گرایش عمومی", "حقوق بین الملل", "حقوق بشر", "حقوق خانواده", "حقوق اقتصادی", "حقوق خصوصی",
            "حقوق جزا و جرم شناسی"]
    if Reshteh not  in Names:
        return "شما در دانشکده حقوق تحصیل می کنید!"
    M = ["مهندسی برق", "متالوروژی", " مهندسی کامپیوتر", 'مهندسی مکانیک', "مهندسی عمران", "مهندسی معدن",
         "شیمی کاربردی", "الکترونیک", "شیمی محض", "مهندسی صنایع"]
    if Reshteh  not in M:
        return "شما در دانشکده فنی و مهندسی تحصیل می کنید!"


#کد شماره 12--------------------------------------------------------------------------



    M = ["مهندسی برق", "متالوروژی", " مهندسی کامپیوتر", 'مهندسی مکانیک', "مهندسی عمران", "مهندسی معدن",
         "شیمی کاربردی", "الکترونیک", "شیمی محض", "مهندسی صنایع"]
    if Reshte not  in  M:
        return ("نام دانشکده وارد شده نادرست است ")


#-----------------------------------کد شماره 13+++++++++++++++++++++++++++++++++++++++




    Fate = ["مجرد","متاهل"]
    if life not in Fate:
        return "'لطفا یکی از دو مقدار متاهل و یا مجرد را انتخاب کنید"


#---------------------کد شماره 14-------------------------------




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


    return "همه ورودی ها صحیح است"
