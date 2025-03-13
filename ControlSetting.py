# Library for system control
import os
# A library to find the system page size
import ctypes
# Library to get some default information from the PiGame library
from pygame import *

# Get the computer screen size and make the game image smaller than the system screen
screen_x = ctypes.windll.user32.GetSystemMetrics(0)-100
screen_y = ctypes.windll.user32.GetSystemMetrics(1)-100
# A function to change game settings
# For example, change the color of group 1
def Edit_Setting(Set_valiue:bytes, New):
    global Settings
    # Find the player account folder
    SystemAdress = os.path.expanduser('~')

    # Create and read the contents of a file for system settings
    All_Setting = open(SystemAdress+"/Football.set","w")
    Settings[Set_valiue] = New
    All_Setting.write("Is Full Screen:"+Settings[b"Is Full Screen"]+
                      "\nColor Grupe one:"+Settings[b"Color Grupe one"]+
                      "\nColor Grupe two:"+Settings[b"Color Grupe two"])

# A function to change game settings
# For example, add the color pink
def Add_Color(Color:str):
# Find the player's account folder
    SystemAdress = os.path.expanduser('~')

    # Create and read the contents of a file for colors in the system
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
# A function to restore the settings to their original state
def Reset_Setting():
    Set = open(SystemAdress+"/Football.set","w")
    Set.write("Is Full Screen:No\nColor Grupe one:red\nColor Grupe two:blue")
    Set.close()
    exit(0)

# Find the player's account folder
SystemAddress = os.path.expanduser('~')
# Create and read the contents of a file for system settings
try:
    All_Setting = open(SystemAdress+"/Football.set","r")
except :
    Set = open(SystemAdress+"/Football.set","w")
    Set.write("Is Full Screen:No\nColor Grupe one:red\nColor Grupe two:blue")
    Set.close()
    All_Setting = open(SystemAdress+"/Football.set","r")

# Create and read the contents of a file for colors in the system
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

# Create a variable to dump the contents of the configuration file
Settings = {b"Is Full Screen":"No Data",
            b"Color Grupe one":"No Data",
            b"Color Grupe two":"No Data"}
# Detach saved settings
Check_Settinges = []
for Set in All_Setting:
    Ting = Set.strip().split(':')
    Check_Settinges.append(Ting)
# Putting separated settings into variables
try :
    Settings[b"Is Full Screen"] = Check_Settinges[0][1]
    Settings[b"Color Grupe one"] = Check_Settinges[1][1]
    Settings[b"Color Grupe two"] = Check_Settinges[2][1]
except :
    exit()

# Apply saved settings
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

# Create variables and fill them with information from the colors file
# The colors file is Football.col
Colors = []
for Col in All_Color:
    Colors.append(Col.strip().split('\n'))
for My_color in Colors:
    color_name, rgb = My_color[0].split(':')
    color_name = color_name.strip()
    rgb = tuple(map(int, rgb.split(',')))
    globals()[color_name] = rgb
