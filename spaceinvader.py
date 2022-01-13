"""
Connor Barajas
cbarajas@wesleyan.edu

Final Project
"""

import turtle
import time
from math import sqrt

# This variable store the horizontal position
# of the player's ship. It will be adjusted
# when the user press left and right keys, and
# will be used by the frame() function to draw

# the ship. The ship never moves vertically, so
# we don't need a variable to store its y position.
userx = 0

# This variable is a list of enemies currently in
# the game. Each enemy is represented by a tuple
# containing its x,y position as well as a string
# indicated the enemy's current direction of travel
# (either left or right). 
# Your final game should include more enemies, although
# the exact arrangement is up to you.
enemies = [(350, -100, "right"), (250,-100,"right"), (150,-100,"right"),
           (200, 100, "left"), (300, 100, "left"), (400, 100, "left"),
           (200, 250, "right"), (-150, 350, "right"), (-350, 350, "right"),
           (-200, 200, "right"), (-100, 200, "right"), (0, 200, "right"),
           (-50, 300, "right"), (-150, 300, "right"), (-250, 300, "left"),
           (-450, 0, "right"), (-350, 0, "right"), (-250, 0, "right"),
           (-50, 150, "left"), (-100, 150, "left"), (100, 250, "right")
           ]

# This variable is a list of all bullets currently
# in the game. It is a list of tuples of (x,y)
# coordinates, one for each bullet. An elements will
# be added when a new bullet is fired, and removed
# when a bullet is destroyed (either by leaving
# the screen or by hitting an enemy).
bullets = []

# This variable is checked by the game's main

# loop to determine when it should end. When
# the game ends (either when the player's ship
# is destroyed, or when all enemies have been 
# destroyed), your code should set this variable
# to True, causing the main loop to end.
gameover = False

score = 0

def frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the player's ship,
    the enemies, and the bullets.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    turtle.bgpic("giphy.gif")
    turtle.up()
    turtle.setposition(userx,-350)
    turtle.down()
    turtle.color("black","blue")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    i = 0
    while i < len(enemies):
        ex_cor = int(enemies[i][0])
        ey_cor = int(enemies[i][1])        
        turtle.up()
        turtle.setposition(ex_cor,ey_cor)
        turtle.down()
        turtle.color("black","orange")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        i += 1
    f = 0
    while f < len(bullets):
        bx_cor = bullets[f][0] - 7.5
        by_cor = bullets[f][1] + 10
        turtle.up()
        turtle.setposition(bx_cor,by_cor)
        turtle.down()
        turtle.color("black","red")
        turtle.begin_fill()
        count = 0
        while count < 3 :
            turtle.forward(15)
            turtle.left(120)
            count += 1
        turtle.end_fill()
        f += 1
    turtle.up()
    turtle.color("white")
    turtle.setposition(-680,370)
    turtle.down()
    turtle.write("Score: %s" %score, False, align= "left", font= ("Arial", 12, "normal"))
    

userx_speed = 15
bullety_speed = 10
enemyx_speed = 10
enemyy_speed = 40

def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    userx.
    """
    global userx
    x = userx
    x -= userx_speed
    if x < -600:
        x = -600
    userx = x

def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    user1x.
    """
    global userx
    x = userx
    x += userx_speed
    if x > 600:
        x = 600
    userx = x

def key_space():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the space key. It should
    add a new bullet to the list of bullets.
    """
    x_cor = userx
    y_cor = -350
    bullets.append(tuple((x_cor,y_cor)))
    
def physics():
    """
    signature: () -> NoneType 
    Update the state of the game world, as
    stored in the global variables. Here, you
    should check the positions of the bullets,
    and remove them if they go off the screen
    or collide with an enemy. In the later case
    you should also remove the enemy. That is,
    given the current position of the bullets,
    calculate their position in the next frame.
    """
    global bullets
    global enemies
    global score
    bullet = 0
    new_list = []
    n = 0
    while n < len(enemies):
        ex_cor = enemies[n][0]
        ey_cor = enemies[n][1]
        ey_cor += 10
        while bullet < len(bullets):
            mx_cor = bullets[bullet][0]
            my_cor = bullets[bullet][1]
            if (25 >= sqrt(((ex_cor - mx_cor + 7.5)**2) + ((ey_cor - my_cor + 6)**2))):
                bullets.pop(bullet)
                enemies.pop(n)
                score += 10
                turtle.write("Score: %s" %score, False, align= "left", font= ("Arial", 12, "normal"))
            elif my_cor > 500:
                bullets.pop(bullet)
            else:
                my_cor += bullety_speed
                bullets.pop(bullet)
                new_list.append((mx_cor, my_cor))
        n += 1
    if len(bullets) == 0:
        bullets += new_list
        new_list = []
            
def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by updating the position of the
    enemies, storied in the enemies global
    variable. That is, given their current
    position, calculate their position
    in the next frame.
    If the enemies reach the player's ship,
    you should set the gameover variable
    to True. Also, if there are no more
    enemies left, set gameover to True.
    """
    global enemies
    global gameover
    global score
    enemy = 0
    e_list = []
    for en in enemies:
        emx_cor = enemies[enemy][0]
        emy_cor = enemies[enemy][1]
        direction = enemies[enemy][2]
        if enemies[enemy][2] == "left":
            if emx_cor < -480:
                emy_cor -= enemyy_speed
                emx_cor += enemyx_speed
                enemies.pop(enemy)
                e_list.append((emx_cor, emy_cor, "right"))
            else:
                emx_cor -= enemyx_speed
                enemies.pop(enemy)
                e_list.append((emx_cor, emy_cor, direction))
        else:
            if emx_cor > 480:
                emy_cor -= enemyy_speed
                emx_cor -= enemyx_speed
                enemies.pop(enemy)
                e_list.append((emx_cor, emy_cor, "left"))
            else:
                emx_cor += enemyx_speed
                enemies.pop(enemy)
                e_list.append((emx_cor, emy_cor, direction))
        enemies += e_list
        e_list = []
    emy_cor += 10
    if len(enemies) == 0 or (40 >= sqrt(((emx_cor - userx)**2) + ((emy_cor + 340)**2))):
            gameover = True
            
            
def reset():
    """
    signature: () -> NoneType
    This function is called when your game starts.
    It should set initial value for all the
    global variables.
    """
    global enemies
    global bullets
    global userx
    global gameover
    global score
    score = 0
    gameover = False
    userx = 0
    bullets = []
    enemies = [(350, -100, "right"), (250,-100,"right"), (150,-100,"right"),
           (200, 100, "left"), (300, 100, "left"), (400, 100, "left"),
           (200, 250, "right"), (-150, 350, "right"), (-350, 350, "right"),
           (-200, 200, "right"), (-100, 200, "right"), (0, 200, "right"),
           (-50, 300, "right"), (-150, 300, "right"), (-250, 300, "left"),
           (-450, 0, "right"), (-350, 0, "right"), (-250, 0, "right"),
           (-50, 150, "left"), (-100, 150, "left"), (100, 250, "right"),
           ]
    
def main():
    """
    signature: () -> NoneType
    Run the game. You shouldn't need to
    modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_space, "space")
    turtle.listen()
    reset()
    while not gameover:
        turtle.clear()
        physics()
        ai()
        frame()
        turtle.update()
        time.sleep(0.05)

main()
