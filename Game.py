from pygame import *
from pygame.mouse import *
# Two handwritten libraries that are located in the files next to this file
# These two libraries contain game settings functions
from definitions import *
from ControlSetting import *

init()
bgcolor = green
GAMES = True

# Define a rectangle for the "restart" button
restart_button = Rect(screen_x/2-32.5, 7, 75, 20)
# Number of goals scored by each team
score_k1 = 0
score_k2 = 0

# Restart function
def Restart(isStart = False):
    # Team 1
    global Speed_PlayersGrup1 ,Color_PlayersGrup1 ,score_k1 ,Player1_1 ,Player1_2 ,Player1_3
    # Team 3
    global SpeedPlayersGrup2 ,Color_PlayersGrup2 ,score_k2 ,Player2_1 ,Player2_2 ,Player2_3
    # Goals
    global color_tir1 ,tir1 ,color_tir2 ,tir2
    # Ball
    global speed_Ball ,color_Ball ,Ball
    global screen

    Speed_PlayersGrup1 = 2
    Color_PlayersGrup1 = Settings[b"Color Grupe one"]
    
    # Team 1 player
    Player1_1 = Rect(screen_x-80, (screen_y/2)-20 , 40, 40)
    # Team 1 player
    Player1_2 = Rect(screen_x-260, (screen_y/2)+160 , 40, 40)
    # Team 1 player
    Player1_3 = Rect(screen_x-260, (screen_y/2)-200 , 40, 40)

    SpeedPlayersGrup2 = 2
    Color_PlayersGrup2 = Settings[b"Color Grupe two"]
    # Team 2 player
    Player2_1 = Rect(40,(screen_y/2)-20 , 40, 40)
    # Team 2 player
    Player2_2 = Rect(260,(screen_y/2)+160 , 40, 40)
    # Team 2 player
    Player2_3 = Rect(260,(screen_y/2)-200 , 40, 40)

    if isStart:
        score_k1 = 0
        score_k2 = 0
        screen = display.set_mode((screen_x, screen_y),SCREEN_SIZE)
        display.set_caption("             Football Buttons/Game")

    # Team 1 goal
    color_tir2 = black
    tir2 = Rect(screen_x-25 , (screen_y/2)-105 , 5, 200)
    # Team 2 goal
    color_tir1 = black
    tir1 = Rect(20,(screen_y/2)-105 , 5, 200)
    # Ball
    speed_Ball = [2, 2]
    color_Ball = (255 , 0 , 255)
    Ball = Rect((screen_x/2)-15 , (screen_y/2)-15 , 30, 30)
    Game()

def Game():
    # UI
    global black ,red ,green ,white ,bgcolor ,screen_x ,screen_y ,screen ,restart_button
    global GAMES
    # Team 1
     global Speed_PlayersGrup1 ,Color_PlayersGrup1 ,Player1_1 ,score_k1 ,Player1_2 ,Player1_3 ,Player1 ,PlayersGrupe1
     # Team 3
     global SpeedPlayersGroup2 ,Color_PlayersGroup2 ,score_k2 ,Player2_1 ,Player2_2 ,Player2_3 ,Player2 ,PlayersGroup2
     # Gates
     global color_tir1,tir1,color_tir2,tir2
     # Ball
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

        # Receive button press
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
            # Control player 1's movements
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

            # Control player 2's movements
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

            # Control collision errors and control not exiting
            if Player1.colliderect(Player2) :
                Restart()
            else:
                # If they hadn't collided
                # they wouldn't come within 1 pixel of each other
                H = Check(Player1 , Player2)
                if len(H) == 1 : colliderect_Player = H[0]
                else : colliderect_Player = "N"

            if (Player1_1.width != Player1_1.height or Player2_1.width != Player2_1.height or
                Player1_2.width != Player1_2.height or Player2_2.width != Player2_2.height or
                Player1_3.width != Player1_3.height or Player2_3.width != Player2_3.height ):
                    show_confirmation("Error", "): It seems there was a problem. Try again! \nClick the button to restart the game")

        # Draw all items
        # The goalposts
        tir1 = draw.rect(screen, color_tir1,tir1)
        tir2 = draw.rect(screen, color_tir2,tir2)
        # Number of goals scored
        message(("Score Palyer One :"+str(score_k1)),screen,black,screen_x-300,0,25)
        message(("Score Palyer two :"+str(score_k2)),screen,black,30,0,25)
        # Show the "restart" button
        draw.rect(screen, (255, 0, 0), restart_button)
        # Define the rectangle for the "restart" button
        message("Restart",screen, (255, 255, 255), restart_button.x+5, restart_button.y,15)
        draw_soccer_field(screen) # Draw a soccer field
        # The players
        if P1 == 0 : Player1_1 = Player1
        if P1 == 1 : Player1_2 = Player1
        if P1 == 2 : Player1_3 = Player1

        if Player2 == PlayersGrupe2[0] : Player2_1 = Player2
        if Player2 == PlayersGrupe2[1] : Player2_1 = Player2
        if Player2 == PlayersGrupe2[2] : Player2_3 = Player2
        # First team
        Player1_1 = draw.rect(screen, Color_PlayersGroup1, Player1_1)
        Player1_2 = draw.rect(screen, Color_PlayersGroup1, Player1_2)
        Player1_3 = draw.rect(screen, Color_PlayersGroup1, Player1_3)
        # # The second team
        Player2_1 = draw.rect(screen, Color_PlayersGroup2, Player2_1)
        Player2_2 = draw.rect(screen, Color_PlayersGroup2, Player2_2)
        Player2_3 = draw.rect(screen, Color_PlayersGroup2, Player2_3)
        # Ball
        Ball = draw.rect(screen, color_Ball, Ball,11,100)
        draw.rect(screen, white, (Ball.x+10 , Ball.y+10 , 10, 10),11,100)

        # # If the ball goes into one of the goals
        if Rect.colliderect(Ball, tir1):
            score_k1 += 1
            show_confirmation("Goal!!!", "What a goal!! \n Click the button to restart the game")
            Restart()
        if Rect.colliderect(Ball, tir2) :
            score_k2 += 1
            show_confirmation("Goal!!!", "What a goal!! \n Click the button to restart the game")
            Restart()

        # Checking the ball hitting the players
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
        # Ball reflection from walls
        if Ball.top <= 20 or Ball.bottom >= screen_x:
            speed_Ball[1] = -speed_Ball[1]
        if Ball.left <= 0 or Ball.right >= screen_y:
            speed_Ball[0] = -speed_Ball[0]

        display.update()

if __name__ == '__main__':
    screen = display.set_mode((screen_x, screen_y),SCREEN_SIZE)
    display.set_caption("             Football Buttons/Game")
    Restart(True)
