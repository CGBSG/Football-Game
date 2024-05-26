# کتاب خانه های مورد نیاز
from pygame import *
from pygame_menu import *
from pygame_menu.themes import *
from turtle import *
from tkinter.messagebox import *
# کنترل تنظیمات
from ControlSetting import *

# نمایش پیغامی درصفحه ای جدید
def show_confirmation(Title,Message):
    return showinfo(Title,Message)

# نوشتن پیام روی صفحه
def message(msg, screen, color,width,height,size,F="bahnschrift"):
        font_style = font.SysFont(F, size)
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width, height])

# پرسش سوال
def Qoiz(Title, Qoez, P, Format:type):
    PP = textinput(Title,Qoez)
    if Format == str :
        if P == str(PP) :
             return True
        elif P != str(PP) :
             return False
        else: return error
    elif Format == int :
        if P == int(PP) :
             return True
        elif P != int(PP) :
             return False
        else: return error
    elif Format == float :
        if P == float(PP) :
             return True
        elif P != float(PP) :
             return False
        else: return error
    elif Format == bool :
        return askyesno(Title, Qoez)
    else: return "Noformat"

# ساخت پشت زمینه
def Backgrund(screen_x,screen_y,screen,COLOR1 = (255, 0, 0),COLOR2 = (0, 0, 255)):
    X = screen_x+300
    for y in range(X):
        color = (
            COLOR1[0] + (COLOR2[0] - COLOR1[0]) * y // X,
            COLOR1[1] + (COLOR2[1] - COLOR1[1]) * y // X,
            COLOR1[2] + (COLOR2[2] - COLOR1[2]) * y // X
        )
        draw.line(screen, color, (0, y), (screen_y, y))

# تابعی برای ساخته دکمه
def Draw_Get_Bottons_for_Start(screen,button,String,X = 25,Y=15,Col=(255, 255, 255),FONT="bahnschrift", size=25):
    # نمایش دکمه "شروع مجدد"
    draw.rect(screen, (255, 0, 0), button)
    # تعریف مستطیل برای دکمه "شروع مجدد"
    message(String,screen, Col, button.x+X, button.y+Y,size,FONT)

# تابعی برای چک کردن اینکه ایا بازیکن ها بهم برخورد کرده اند یا خیر
def Check(Rect1:Rect , Rect2:Rect):
    Hit = [] # U , D , L , R

    P1x , P1y = Rect1.x , Rect1.y
    P2x , P2y = Rect2.x , Rect2.y

    if ((P1x == P2x + Rect2.height) and
        (P1y <= P2y + Rect2.height) and
        (P1y + Rect1.height >= P2y)):
            Hit.append("L")
    if ((P1x + Rect1.height == P2x) and 
        (P1y <= P2y + Rect2.height) and
        (P1y + Rect1.height >= P2y)):
            Hit.append("R")
    if ((P1y + Rect1.height == P2y) and
        (P1x <= P2x + Rect2.height) and
        (P1x + Rect1.height >= P2x)):
            Hit.append("D")
    if ((P1y == P2y + Rect2.height) and
        (P1x <= P2x + Rect2.height) and
        (P1x + Rect1.height >= P2x)):
            Hit.append("U")

    return Hit

# تابعی برای رسم زمین فورتبال
def draw_soccer_field(screen):
    draw.rect(screen, white, (20, 30, screen.get_size()[0]-40, screen.get_size()[1]-40), 2)
    draw.circle(screen, white, (screen.get_size()[0]/2, screen.get_size()[1]/2), 100, 2)
    draw.line(screen, white, (screen.get_size()[0]/2, 30),
                             (screen.get_size()[0]/2, screen.get_size()[1]-10), 2)
    draw.circle(screen, white, (screen.get_size()[0]/2, screen.get_size()[1]/2), 10)

# تابعی برای ذخیره تنظیمات ویرایش شده
def Save_Setting ():
    global Is_Full_Screen_var,Color_Grupe_one_var,Color_Grupe_two_var,setting_Menu

    settingsData = setting_Menu.get_input_data()
    for key in settingsData.keys():
        if key == "Is Full Screen" and settingsData[key] == True :
            Edit_Setting(b"Is Full Screen", "Yes")
        if key == "Is Full Screen" and settingsData[key] == False :
            Edit_Setting(b"Is Full Screen", "No")
        if key == "Color Grupe one" : Edit_Setting(b"Color Grupe one", str(settingsData[key][0][0]))
        if key == "Color Grupe two" : Edit_Setting(b"Color Grupe two", str(settingsData[key][0][0]))
    exit(0)

# نمایش تنظیمات
def Setting():
    global Is_Full_Screen_var,Color_Grupe_one_var,Color_Grupe_two_var,Settings,setting_Menu
    screen = display.set_mode((400, 574))
    display.set_caption("             Football Buttons/Setting")

    if   Settings[b"Is Full Screen"] == "Yes" : Is_Full_Screen_var = True
    elif Settings[b"Is Full Screen"] == "No"  : Is_Full_Screen_var = False
    else: Is_Full_Screen_var = None
    Color_Grupe_one_var = Settings[b"Color Grupe one"]
    Color_Grupe_two_var = Settings[b"Color Grupe two"]

    Seve_button = Rect(93 , 500, 240, 50)
    # رنگ های مجاز برای تیم ها
    COLOR_GROGS =  [("black","black") ,
                    ("red","red"),
                    ("blue","blue"),
                    ("white","white"),
                    ("SUN TOP","SUN TOP"),
                    ("SUN BOTTOM","SUN BOTTOM"),
                    ("SKY TOP","SKY TOP"),
                    ("SKY BOTTOM","SKY BOTTOM")]
    index_one_ = [color[0] for color in COLOR_GROGS].index(Color_Grupe_one_var)
    index_two_ = [color[0] for color in COLOR_GROGS].index(Color_Grupe_two_var)

    init()
    while True :
        for j in event.get():
            if j.type == QUIT :
                exit()

        setting_Menu = Menu(title="Settings", 
                    width = screen.get_size()[0],height = screen.get_size()[1],
                    theme=THEME_DARK)
        THEME_DARK.widget_font_size = 18

        setting_Menu.add.toggle_switch(title="Is Full Screen",
                                    default=Is_Full_Screen_var, toggleswitch_id="Is Full Screen")
        setting_Menu.add.label(title="")
        setting_Menu.add.dropselect(title="Color Grupe one",
                                    items=COLOR_GROGS, dropselect_id="Color Grupe one", default=index_one_)
        setting_Menu.add.label(title="")
        setting_Menu.add.dropselect(title="Color Grupe two",
                                    items=COLOR_GROGS, dropselect_id="Color Grupe two", default=index_two_)
        setting_Menu.add.label(title="")
        setting_Menu.add.label(title="")
        setting_Menu.add.label(title="")
        setting_Menu.add.button(title = "Save New Setting", action = Save_Setting ,
                                font_color = black , background_color = green)
        setting_Menu.add.label(title="")
        setting_Menu.add.button(title = " Restore Defaults ", action = Reset_Setting ,
                                font_color = black , background_color = red)

        setting_Menu.mainloop(screen)
# پایان