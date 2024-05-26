# کتابخانه برای کنترل سیستم
import os
# کتابخانه ای برای پیدا کردن اندازه صفحه سیستم
import ctypes
# کتابخانه برای دریافت برخی اطلاعات پیش فرض کتابخانه پای گیم
from pygame import *

# دریافت اندازه صفحه کامپیوتر و ساخت تصویر بازی کوچک تر از صفحه سیستم
screen_x = ctypes.windll.user32.GetSystemMetrics(0)-100
screen_y = ctypes.windll.user32.GetSystemMetrics(1)-100
# تابعی برای تغییر تنظیمات بازی 
# مثلا رنگ گروه 1 را تغییر دهیم
def Edit_Setting(Set_valiue:bytes, New):
    global Settings
    # پیدا کردن پوشه اکانت بازیکن
    SystemAdress = os.path.expanduser('~')

    # ساخت و خواندن محتوات فایلی برای تنظیمات در سیستم
    All_Setting = open(SystemAdress+"/Football.set","w")
    Settings[Set_valiue] = New
    All_Setting.write("Is Full Screen:"+Settings[b"Is Full Screen"]+
                      "\nColor Grupe one:"+Settings[b"Color Grupe one"]+
                      "\nColor Grupe two:"+Settings[b"Color Grupe two"])

# تابعی برای تغییر تنظیمات بازی 
# مثلا رنگ صورتی را اضافه کنیم
def Add_Color(Color:str):
    # پیدا کردن پوشه اکانت بازیکن
    SystemAdress = os.path.expanduser('~')

    # ساخت و خواندن محتوات فایلی برای رنگ ها در سیستم
    try:
        All_Color =  open(SystemAdress+"/Football.col","r")
    except :
        Col = open(SystemAdress+"/Football.col","w")
        Col.write("black :0,0,0\nred :255,0,0\ngreen :0,255,0\nblue :0,0,255"+
                  "\nwhite :255,255,255\nyellow :255,255,102\nSUN_TOP :255,218,69"+
                  "\nSUN_BOTTOM :255,79,105\nSKY_TOP :73,231,236\nSKY_BOTTOM :171,31,101"+
                  "\nLINES :255,79,105\nBG_COLOR :43,15,84")
        Col.close()
    All_Color = open(SystemAdress+"/Football.col","a")
    All_Color.write("\n"+color)
# تابعی برای برگرداندن تنظیمات به حالت اولیه
def Reset_Setting():
    Set = open(SystemAdress+"/Football.set","w")
    Set.write("Is Full Screen:No\nColor Grupe one:red\nColor Grupe two:blue")
    Set.close()
    exit(0)

# پیدا کردن پوشه اکانت بازیکن
SystemAdress = os.path.expanduser('~')
# ساخت و خواندن محتوات فایلی برای تنظیمات در سیستم
try:
    All_Setting = open(SystemAdress+"/Football.set","r")
except :
    Set = open(SystemAdress+"/Football.set","w")
    Set.write("Is Full Screen:No\nColor Grupe one:red\nColor Grupe two:blue")
    Set.close()
    All_Setting = open(SystemAdress+"/Football.set","r")

# ساخت و خواندن محتوات فایلی برای رنگ ها در سیستم
try:
    All_Color =  open(SystemAdress+"/Football.col","r")
except :
    Col = open(SystemAdress+"/Football.col","w")
    Col.write("black :0,0,0\nred :255,0,0\ngreen :0,255,0\nblue :0,0,255"+
                "\nwhite :255,255,255\nyellow :255,255,102\nSUN_TOP :255,218,69"+
                "\nSUN_BOTTOM :255,79,105\nSKY_TOP :73,231,236\nSKY_BOTTOM :171,31,101"+
                "\nLINES :255,79,105\nBG_COLOR :43,15,84")
    Col.close()
    All_Color = open(SystemAdress+"/Football.col","r")

# ساخت متغیری برای ریختن محتویات فایل تنظیمات
Settings = {b"Is Full Screen":"No Data",
            b"Color Grupe one":"No Data",
            b"Color Grupe two":"No Data"}
# جدا کردن تنظیمات ذخیره شده
Check_Settinges = []
for Set in All_Setting:
    Ting = Set.strip().split(':')
    Check_Settinges.append(Ting)
# قرار دادن نتظیمات تفکیک شده در متغیر هایی
try :
    Settings[b"Is Full Screen"] = Check_Settinges[0][1]
    Settings[b"Color Grupe one"] = Check_Settinges[1][1]
    Settings[b"Color Grupe two"] = Check_Settinges[2][1]
except :
    exit()

# اعمال تنظیمات ذخیره شده
SCREEN_SIZE = RESIZABLE
Is_Full_Screen = False
if   Settings[b"Is Full Screen"] == "Yes" :
    SCREEN_SIZE = FULLSCREEN
    Is_Full_Screen = True
elif Settings[b"Is Full Screen"] == "No"  : 
    SCREEN_SIZE = RESIZABLE
    Is_Full_Screen = False
elif Settings[b"Is Full Screen"] == "No Data"  : exit()
else : exit()


# ساخت متغیر هایی و پر کردن انها با اطلاعات درون فایل رنگ ها قرار دارند
# فایل رنگ ها Football.col است
Colors = []
for Col in All_Color:
    Colors.append(Col.strip().split('\n'))
for My_color in Colors:
    color_name, rgb = My_color[0].split(':')
    color_name = color_name.strip()
    rgb = tuple(map(int, rgb.split(',')))
    globals()[color_name] = rgb
