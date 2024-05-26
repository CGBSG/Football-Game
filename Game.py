from pygame import *
from pygame.mouse import *
# دو کتابخانه دست نوشته که در فایل هایی که کنار این فایل قرار گرفت اند وجود دارند
# این دو کتابخانه توابع ، تنظیمات بازی قرار دارند
from definitions import *
from ControlSetting import *

init()
bgcolor = green
GAMES = True

# تعریف مستطیل برای دکمه "شروع مجدد"
restart_button = Rect(screen_x/2-32.5, 7, 75, 20)
# تعداد گل های زده شده توسط هر تیم
score_k1 = 0
score_k2 = 0

# تابعی برای شروع دوباره
def Restart(isStart = False):
    # تیم 1
    global Speed_PlayersGrup1 ,Color_PlayersGrup1 ,score_k1 ,Player1_1 ,Player1_2 ,Player1_3
    # تیم 3
    global SpeedPlayersGrup2 ,Color_PlayersGrup2 ,score_k2 ,Player2_1 ,Player2_2 ,Player2_3
    # دروازه ها
    global color_tir1 ,tir1 ,color_tir2 ,tir2 
    # توپ
    global speed_Ball ,color_Ball ,Ball
    global screen

    Speed_PlayersGrup1 = 2
    Color_PlayersGrup1 = Settings[b"Color Grupe one"]
    # بازیکن  تیم 1
    Player1_1 = Rect(screen_x-80,  (screen_y/2)-20 , 40, 40)
    # بازیکن تیم 1
    Player1_2 = Rect(screen_x-260, (screen_y/2)+160 , 40, 40)
    # بازیکن تیم 1
    Player1_3 = Rect(screen_x-260, (screen_y/2)-200 , 40, 40)

    SpeedPlayersGrup2 = 2
    Color_PlayersGrup2 = Settings[b"Color Grupe two"]
    # بازیکن تیم 2
    Player2_1 = Rect(40,(screen_y/2)-20 , 40, 40)
    # بازیکن تیم 2
    Player2_2 = Rect(260,(screen_y/2)+160 , 40, 40)
    # بازیکن تیم 2
    Player2_3 = Rect(260,(screen_y/2)-200 , 40, 40)

    if isStart:
        score_k1 = 0
        score_k2 = 0
        screen = display.set_mode((screen_x, screen_y),SCREEN_SIZE)
        display.set_caption("             Football Buttons/Game")

    # دروازه تیم 1
    color_tir2 = black
    tir2 = Rect(screen_x-25 , (screen_y/2)-105 , 5, 200)
    # دروازه تیم 2
    color_tir1 = black
    tir1 = Rect(20,(screen_y/2)-105 , 5, 200)
    # توپ
    speed_Ball = [2, 2]
    color_Ball = (255 , 0 , 255)
    Ball = Rect((screen_x/2)-15 , (screen_y/2)-15 , 30, 30)
    Game()

def Game():
    # UI
    global black ,red ,green ,white ,bgcolor ,screen_x ,screen_y ,screen ,restart_button
    global GAMES
    # تیم 1
    global Speed_PlayersGrup1 ,Color_PlayersGrup1 ,Player1_1 ,score_k1 ,Player1_2 ,Player1_3 ,Player1 ,PlayersGrupe1
    # تیم 3
    global SpeedPlayersGrup2 ,Color_PlayersGrup2 ,score_k2 ,Player2_1 ,Player2_2 ,Player2_3 ,Player2 ,PlayersGrupe2
    # دروازه ها
    global color_tir1 ,tir1 ,color_tir2 ,tir2
    # توپ
    global speed_Ball ,color_Ball ,Ball

    PlayersGrupe1 = (Player1_1 ,Player1_2 ,Player1_3)
    PlayersGrupe2 = (Player2_1 ,Player2_2 ,Player2_3)
    Player1 = PlayersGrupe1[0]
    P1 = 0
    Player2 = PlayersGrupe2[0]
    P2 = 0
    frame = time.Clock()
    colliderect_Player = "N" # N : No collidepoint-> L : Left , R : Right , U : Up , D : Down
    while GAMES == True :
        frame.tick(99)
        screen.fill(bgcolor)
        for j in event.get():
            if j.type == QUIT :
                exit()
            if j.type == MOUSEBUTTONDOWN:
                mouse_pos = mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    Restart()

        # دریافت فشار دادن دکمه
        keys = key.get_pressed()
        if keys :
            if keys[K_m] :
                if P1 == 0 :
                    P1 = 1
                elif P1 == 1 :
                    P1 = 2
                elif P1 == 2 :
                    P1 = 0
                Player1 = PlayersGrupe1[P1]
            if keys[K_g] :
                if P2 == 0 :
                    P2 = 1
                elif P2 == 1 :
                    P2 = 2
                elif P2 == 2 :
                    P2 = 0
                Player2 = PlayersGrupe2[P2]
            # کنترل حرکات بازیکن 1 
            if (keys[K_LEFT] and Player1.colliderect(Player2) == False and
                    Player1.x > 2 and colliderect_Player != "L" ) :
                Player1.x -= Speed_PlayersGrup1
            if (keys[K_RIGHT]and Player1.colliderect(Player2) == False and
                    Player1.x+Player1.width < screen_x - 2 and colliderect_Player != "R" ) :
                Player1.x += Speed_PlayersGrup1 

            if (keys[K_UP]   and Player1.colliderect(Player2) == False and
                    Player1.y > 2 and colliderect_Player != "U" ) :
                Player1.y -= Speed_PlayersGrup1
            if (keys[K_DOWN] and Player1.colliderect(Player2) == False and
                    Player1.y+Player1.width < screen_y - 2 and colliderect_Player != "D" ) :
                Player1.y += Speed_PlayersGrup1

            # کنترل حرکات بازیکن 2 
            if (keys[K_a] and Player2.colliderect(Player1) == False and
                     Player2.x > 2 and colliderect_Player != "R" ) :
                Player2.x -= SpeedPlayersGrup2
            if (keys[K_d] and Player2.colliderect(Player1) == False and
                     Player2.x+Player2.width < screen_x - 2 and colliderect_Player != "L" ) :
                Player2.x += SpeedPlayersGrup2
            if (keys[K_w] and Player2.colliderect(Player1) == False and
                     Player2_1.y > 2 and colliderect_Player != "D" ) :
                Player2.y -= SpeedPlayersGrup2
            if (keys[K_s] and Player2.colliderect(Player1) == False and
                     Player2.y+Player2.width < screen_y - 2 and colliderect_Player != "U" ) :
                Player2.y += SpeedPlayersGrup2

            # کنترل ارور های بهم برخورد کردن و کنترل بیرون نرفتن
            if Player1.colliderect(Player2) :
                Restart()
            else:
                # اگر به هم برخورد نکرده بودن
                # تا فاصله 1 پیکسل بهم نزدیک نشوند
                H = Check(Player1 , Player2)
                # H = Check(Player1, Player2)
                if len(H) == 1 : colliderect_Player = H[0]
                else : colliderect_Player = "N"

            if (Player1_1.width != Player1_1.height or Player2_1.width != Player2_1.height or
                Player1_2.width != Player1_2.height or Player2_2.width != Player2_2.height or
                Player1_3.width != Player1_3.height or Player2_3.width != Player2_3.height ):
                    show_confirmation("ارور", "): انگاری مشکلی پیش اومده دوباره رو بزن! \n برای شروع مجدد بازی روی دکمه کلیک کن")

        # رسم کردن تمام موارد
        # تیرک ها
        tir1 = draw.rect(screen, color_tir1,tir1)
        tir2 = draw.rect(screen, color_tir2,tir2)
        # تعداد گل زده شده
        message(("Score Palyer One :"+str(score_k1)),screen,black,screen_x-300,0,25)
        message(("Score Palyer two :"+str(score_k2)),screen,black,30,0,25)
        # نمایش دکمه "شروع مجدد"
        draw.rect(screen, (255, 0, 0), restart_button)
        # تعریف مستطیل برای دکمه "شروع مجدد"
        message("Restart",screen, (255, 255, 255), restart_button.x+5, restart_button.y,15)
        draw_soccer_field(screen)  # رسم زمین فوتبال
        # بازیکن ها
        if P1 == 0 : Player1_1 = Player1
        if P1 == 1 : Player1_2 = Player1
        if P1 == 2 : Player1_3 = Player1

        if Player2 == PlayersGrupe2[0] : Player2_1 = Player2
        if Player2 == PlayersGrupe2[1] : Player2_1 = Player2
        if Player2 == PlayersGrupe2[2] : Player2_3 = Player2
            # تیم اول
        Player1_1 = draw.rect(screen, Color_PlayersGrup1, Player1_1)
        Player1_2 = draw.rect(screen, Color_PlayersGrup1, Player1_2)
        Player1_3 = draw.rect(screen, Color_PlayersGrup1, Player1_3)
        #     # تیم دوم
        Player2_1 = draw.rect(screen, Color_PlayersGrup2, Player2_1)
        Player2_2 = draw.rect(screen, Color_PlayersGrup2, Player2_2)
        Player2_3 = draw.rect(screen, Color_PlayersGrup2, Player2_3)
        # توپ
        Ball = draw.rect(screen, color_Ball, Ball,11,100)
        draw.rect(screen, white, (Ball.x+10 , Ball.y+10 , 10, 10),11,100)

        # # اگر توپ در یکی از گل ها رفت
        if Rect.colliderect(Ball, tir1):
            score_k1 += 1
            show_confirmation("گـــــــــــللللللـ!!!", "چه گلی بود!! \n برای شروع مجدد بازی روی دکمه کلیک کن")
            Restart()
        if Rect.colliderect(Ball, tir2) :
            score_k2 += 1
            show_confirmation("گـــــــــــللللللـ!!!", "چه گلی بود!! \n برای شروع مجدد بازی روی دکمه کلیک کن")
            Restart()

        # بررسی برخورد توپ به بازیکن ها
        if Ball.colliderect(Player1) :
            if keys[K_LEFT] :
                speed_Ball[0] = -2
                speed_Ball[1] = 0
            if keys[K_RIGHT]:
                speed_Ball[0] = +2
                speed_Ball[1] = 0
            if keys[K_UP]   :
                speed_Ball[1] = -2
                speed_Ball[0] = 0
            if keys[K_DOWN] :
                speed_Ball[1] = +2
                speed_Ball[0] = 0

            Ball.left = Ball.left+speed_Ball[0]
            Ball.top = Ball.top+speed_Ball[1]
        if Ball.colliderect(Player2) :
            if keys[K_a] :
                speed_Ball[0] = -2
                speed_Ball[1] = 0
            if keys[K_d] :
                speed_Ball[0] = +2
                speed_Ball[1] = 0
            if keys[K_w] :
                speed_Ball[1] = -2
                speed_Ball[0] = 0
            if keys[K_s] :
                speed_Ball[1] = +2
                speed_Ball[0] = 0

            Ball.left = Ball.left+speed_Ball[0]
            Ball.top = Ball.top+speed_Ball[1]
        # بازتاب توپ از دیوارها
        if Ball.top <= 20 or Ball.bottom >= screen_x:
            speed_Ball[1] = -speed_Ball[1]
        if Ball.left <= 0 or Ball.right >= screen_y:
            speed_Ball[0] = -speed_Ball[0]

        display.update()

if __name__ == '__main__':
    screen = display.set_mode((screen_x, screen_y),SCREEN_SIZE)
    display.set_caption("             Football Buttons/Game")
    Restart(True)
