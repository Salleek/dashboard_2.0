import pygame
import time

#globals
rpm = 0
limit = False
speed_limit = False
temp_limit = False
sports_mode = False
button_press = False

#initialize the interface
pygame.init()

#clock
clock = pygame.time.Clock()

#create screen
screen = pygame.display.set_mode((1024, 600))

#Title of app
pygame.display.set_caption("Dashboard 2.0")

#Tachometer
tachometer_0 = [pygame.image.load('0-1000/Tach.png'), pygame.image.load('0-1000/Tach2.png'), pygame.image.load('0-1000/Tach3.png'), pygame.image.load('0-1000/Tach4.png'), pygame.image.load('0-1000/Tach5.png'),pygame.image.load('0-1000/Tach6.png'), pygame.image.load('0-1000/Tach7.png'), pygame.image.load('0-1000/Tach8.png')]
tachometer_1 = [pygame.image.load('1000-2000/Tach1.png'), pygame.image.load('1000-2000/Tach2.png'), pygame.image.load('1000-2000/Tach3.png'), pygame.image.load('1000-2000/Tach4.png'), pygame.image.load('1000-2000/Tach5.png'),pygame.image.load('1000-2000/Tach6.png'), pygame.image.load('1000-2000/Tach7.png'), pygame.image.load('1000-2000/Tach8.png')]
tachometer_2 = [pygame.image.load('2000-3000/Tach1.png'), pygame.image.load('2000-3000/Tach2.png'), pygame.image.load('2000-3000/Tach3.png'), pygame.image.load('2000-3000/Tach4.png'), pygame.image.load('2000-3000/Tach5.png'),pygame.image.load('2000-3000/Tach6.png'), pygame.image.load('2000-3000/Tach7.png'), pygame.image.load('2000-3000/Tach8.png')]
tachometer_3 = [pygame.image.load('3000-4000/Tach0.png'), pygame.image.load('3000-4000/Tach1.png'), pygame.image.load('3000-4000/Tach2.png'), pygame.image.load('3000-4000/Tach3.png'), pygame.image.load('3000-4000/Tach4.png'),pygame.image.load('3000-4000/Tach5.png'), pygame.image.load('3000-4000/Tach6.png'), pygame.image.load('3000-4000/Tach7.png')]
tachometer_4 = [pygame.image.load('4000-5000/Tach1.png'), pygame.image.load('4000-5000/Tach2.png'), pygame.image.load('4000-5000/Tach3.png'), pygame.image.load('4000-5000/Tach4.png'), pygame.image.load('4000-5000/Tach5.png'),pygame.image.load('4000-5000/Tach6.png'), pygame.image.load('4000-5000/Tach7.png'), pygame.image.load('4000-5000/Tach8.png')]
tachometer_5 = [pygame.image.load('5000-6000/Tach1.png'), pygame.image.load('5000-6000/Tach2.png'), pygame.image.load('5000-6000/Tach3.png'), pygame.image.load('5000-6000/Tach4.png'), pygame.image.load('5000-6000/Tach5.png'),pygame.image.load('5000-6000/Tach6.png'), pygame.image.load('5000-6000/Tach7.png'), pygame.image.load('5000-6000/Tach8.png'), pygame.image.load('5000-6000/Tach9.png')]
tachometer_6 = [pygame.image.load('6000-7000/Tach1.png'), pygame.image.load('6000-7000/Tach2.png'), pygame.image.load('6000-7000/Tach3.png'), pygame.image.load('6000-7000/Tach4.png'), pygame.image.load('6000-7000/Tach5.png'),pygame.image.load('6000-7000/Tach6.png'), pygame.image.load('6000-7000/Tach7.png'), pygame.image.load('6000-7000/Tach8.png')]
tachometer_7 = [pygame.image.load('7000-8000/Tach1.png'), pygame.image.load('7000-8000/Tach2.png'), pygame.image.load('7000-8000/Tach3.png'), pygame.image.load('7000-8000/Tach4.png'), pygame.image.load('7000-8000/Tach5.png'),pygame.image.load('7000-8000/Tach6.png'), pygame.image.load('7000-8000/Tach7.png'), pygame.image.load('7000-8000/Tach8.png')]
tachometer_8 = [pygame.image.load('8000-9000/Tach1.png'), pygame.image.load('8000-9000/Tach2.png'), pygame.image.load('8000-9000/Tach3.png'), pygame.image.load('8000-9000/Tach4.png'), pygame.image.load('8000-9000/Tach5.png'),pygame.image.load('8000-9000/Tach6.png'), pygame.image.load('8000-9000/Tach7.png'), pygame.image.load('8000-9000/Tach8.png')]
tachometerX = 205
tachometerY = 0

def tachometer(rpm):

    #0-1000
    if rpm > 0 and rpm <=142:
        screen.blit(tachometer_0[1], (tachometerX, tachometerY))
    elif rpm > 142 and rpm <= 284:
        screen.blit(tachometer_0[2], (tachometerX, tachometerY))
    elif rpm > 284 and rpm <= 426:
        screen.blit(tachometer_0[3], (tachometerX, tachometerY))
    elif rpm > 426 and rpm <= 568:
        screen.blit(tachometer_0[4], (tachometerX, tachometerY))
    elif rpm > 568 and rpm <= 710:
        screen.blit(tachometer_0[5], (tachometerX, tachometerY))
    elif rpm > 710 and rpm <= 852:
        screen.blit(tachometer_0[6], (tachometerX, tachometerY))
    elif rpm > 852 and rpm <= 1000:
        screen.blit(tachometer_0[7], (tachometerX, tachometerY))

    #1000-2000
    elif rpm > 1000 and rpm <= 1125:
        screen.blit(tachometer_1[0], (tachometerX, tachometerY))
    elif rpm > 1125 and rpm <= 1250:
        screen.blit(tachometer_1[1], (tachometerX, tachometerY))
    elif rpm > 1250 and rpm <= 1375:
        screen.blit(tachometer_1[2], (tachometerX, tachometerY))
    elif rpm > 1375 and rpm <= 1500:
        screen.blit(tachometer_1[3], (tachometerX, tachometerY))
    elif rpm > 1500 and rpm <= 1625:
        screen.blit(tachometer_1[4], (tachometerX, tachometerY))
    elif rpm > 1625 and rpm <= 1750:
        screen.blit(tachometer_1[5], (tachometerX, tachometerY))
    elif rpm > 1750 and rpm <= 1875:
        screen.blit(tachometer_1[6], (tachometerX, tachometerY))
    elif rpm > 1875 and rpm <= 2000:
        screen.blit(tachometer_1[7], (tachometerX, tachometerY))

    #2000-3000
    elif rpm > 2000 and rpm <= 2125:
        screen.blit(tachometer_2[0], (tachometerX, tachometerY))
    elif rpm > 2125 and rpm <= 2250:
        screen.blit(tachometer_2[1], (tachometerX, tachometerY))
    elif rpm > 2250 and rpm <= 2375:
        screen.blit(tachometer_2[2], (tachometerX, tachometerY))
    elif rpm > 2375 and rpm <= 2500:
        screen.blit(tachometer_2[3], (tachometerX, tachometerY))
    elif rpm > 2500 and rpm <= 2625:
        screen.blit(tachometer_2[4], (tachometerX, tachometerY))
    elif rpm > 2625 and rpm <= 2750:
        screen.blit(tachometer_2[5], (tachometerX, tachometerY))
    elif rpm > 2750 and rpm <= 2875:
        screen.blit(tachometer_2[6], (tachometerX, tachometerY))
    elif rpm > 2875 and rpm <= 3000:
        screen.blit(tachometer_2[7], (tachometerX, tachometerY))

    #3000-4000
    elif rpm > 3000 and rpm <= 3125:
        screen.blit(tachometer_3[0], (tachometerX, tachometerY))
    elif rpm > 3125 and rpm <= 3250:
        screen.blit(tachometer_3[1], (tachometerX, tachometerY))
    elif rpm > 3250 and rpm <= 3375:
        screen.blit(tachometer_3[2], (tachometerX, tachometerY))
    elif rpm > 3375 and rpm <= 3500:
        screen.blit(tachometer_3[3], (tachometerX, tachometerY))
    elif rpm > 3500 and rpm <= 3625:
        screen.blit(tachometer_3[4], (tachometerX, tachometerY))
    elif rpm > 3625 and rpm <= 3750:
        screen.blit(tachometer_3[5], (tachometerX, tachometerY))
    elif rpm > 3750 and rpm <= 3875:
        screen.blit(tachometer_3[6], (tachometerX, tachometerY))
    elif rpm > 3875 and rpm <= 4000:
        screen.blit(tachometer_3[7], (tachometerX, tachometerY))

    #4000-5000
    elif rpm > 4000 and rpm <= 4125:
        screen.blit(tachometer_4[0], (tachometerX, tachometerY))
    elif rpm > 4125 and rpm <= 4250:
        screen.blit(tachometer_4[1], (tachometerX, tachometerY))
    elif rpm > 4250 and rpm <= 4375:
        screen.blit(tachometer_4[2], (tachometerX, tachometerY))
    elif rpm > 4375 and rpm <= 4500:
        screen.blit(tachometer_4[3], (tachometerX, tachometerY))
    elif rpm > 4500 and rpm <= 4625:
        screen.blit(tachometer_4[4], (tachometerX, tachometerY))
    elif rpm > 4625 and rpm <= 4750:
        screen.blit(tachometer_4[5], (tachometerX, tachometerY))
    elif rpm > 4750 and rpm <= 4875:
        screen.blit(tachometer_4[6], (tachometerX, tachometerY))
    elif rpm > 4875 and rpm <= 5000:
        screen.blit(tachometer_4[7], (tachometerX, tachometerY))

    #5000-6000
    elif rpm > 5000 and rpm <= 5111:
        screen.blit(tachometer_5[0], (tachometerX, tachometerY))
    elif rpm > 5111 and rpm <= 5222:
        screen.blit(tachometer_5[1], (tachometerX, tachometerY))
    elif rpm > 5222 and rpm <= 5333:
        screen.blit(tachometer_5[2], (tachometerX, tachometerY))
    elif rpm > 5333 and rpm <= 5444:
        screen.blit(tachometer_5[3], (tachometerX, tachometerY))
    elif rpm > 5444 and rpm <= 5555:
        screen.blit(tachometer_5[4], (tachometerX, tachometerY))
    elif rpm > 5555 and rpm <= 5666:
        screen.blit(tachometer_5[5], (tachometerX, tachometerY))
    elif rpm > 5666 and rpm <= 5777:
        screen.blit(tachometer_5[6], (tachometerX, tachometerY))
    elif rpm > 5777 and rpm <= 5888:
        screen.blit(tachometer_5[7], (tachometerX, tachometerY))
    elif rpm > 5888 and rpm <= 6000:
        screen.blit(tachometer_5[8], (tachometerX, tachometerY))

    #6000-7000
    elif rpm > 6000 and rpm <= 6125:
        screen.blit(tachometer_6[0], (tachometerX, tachometerY))
    elif rpm > 6125 and rpm <= 6250:
        screen.blit(tachometer_6[1], (tachometerX, tachometerY))
    elif rpm > 6250 and rpm <= 6375:
        screen.blit(tachometer_6[2], (tachometerX, tachometerY))
    elif rpm > 6375 and rpm <= 6500:
        screen.blit(tachometer_6[3], (tachometerX, tachometerY))
    elif rpm > 6500 and rpm <= 6625:
        screen.blit(tachometer_6[4], (tachometerX, tachometerY))
    elif rpm > 6625 and rpm <= 6750:
        screen.blit(tachometer_6[5], (tachometerX, tachometerY))
    elif rpm > 6750 and rpm <= 6875:
        screen.blit(tachometer_6[6], (tachometerX, tachometerY))
    elif rpm > 6875 and rpm <= 7000:
        screen.blit(tachometer_6[7], (tachometerX, tachometerY))

    #7000-8000
    elif rpm > 7000 and rpm <= 7125:
        screen.blit(tachometer_7[0], (tachometerX, tachometerY))
    elif rpm > 7125 and rpm <= 7250:
        screen.blit(tachometer_7[1], (tachometerX, tachometerY))
    elif rpm > 7250 and rpm <= 7375:
        screen.blit(tachometer_7[2], (tachometerX, tachometerY))
    elif rpm > 7375 and rpm <= 7500:
        screen.blit(tachometer_7[3], (tachometerX, tachometerY))
    elif rpm > 7500 and rpm <= 7625:
        screen.blit(tachometer_7[4], (tachometerX, tachometerY))
    elif rpm > 7625 and rpm <= 7750:
        screen.blit(tachometer_7[5], (tachometerX, tachometerY))
    elif rpm > 7750 and rpm <= 7875:
        screen.blit(tachometer_7[6], (tachometerX, tachometerY))
    elif rpm > 7875 and rpm <= 8000:
        screen.blit(tachometer_7[7], (tachometerX, tachometerY))

    #8000-9000
    elif rpm > 8000 and rpm <= 8125:
        screen.blit(tachometer_8[0], (tachometerX, tachometerY))
    elif rpm > 8125 and rpm <= 8250:
        screen.blit(tachometer_8[1], (tachometerX, tachometerY))
    elif rpm > 8250 and rpm <= 8375:
        screen.blit(tachometer_8[2], (tachometerX, tachometerY))
    elif rpm > 8375 and rpm <= 8500:
        screen.blit(tachometer_8[3], (tachometerX, tachometerY))
    elif rpm > 8500 and rpm <= 8625:
        screen.blit(tachometer_8[4], (tachometerX, tachometerY))
    elif rpm > 8625 and rpm <= 8750:
        screen.blit(tachometer_8[5], (tachometerX, tachometerY))
    elif rpm > 8750 and rpm <= 8875:
        screen.blit(tachometer_8[6], (tachometerX, tachometerY))
    elif rpm > 8875 and rpm <= 9000:
        screen.blit(tachometer_8[7], (tachometerX, tachometerY))

    else:
        screen.blit(tachometer_0[0], (tachometerX, tachometerY))

# Speed
speed_value = 0
speed_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 50)
mphfont = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)

speedtextX0 = 500   #one's place
speedtextY0 = 255

speedtextX10 = 489  #ten's place
speedtextY10 = 255

speedtextX100 = 480 #hundredth's place
speedtextY100 = 255

mphtextX = 488
mphtextY = 325

def display_speed():
    speed = speed_font.render(str(speed_value), True, (255, 255, 255))
    mph = mphfont.render("MPH", True, (255, 255, 255))

    if speed_value <= 9:
        screen.blit(speed, (speedtextX0, speedtextY0))
    elif speed_value >= 10 and speed_value <= 99:
        screen.blit(speed, (speedtextX10, speedtextY10))
    elif speed_value >= 100:
        screen.blit(speed, (speedtextX100, speedtextY100))

    screen.blit(mph, (mphtextX, mphtextY))

#Temp Gauge
temp_value = 0

temp_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)

temp_txt_X = 115
temp_txt_Y = 420

temp_indicator_img = pygame.image.load('temp_gauge/indicator.png')
temp_indicatorX = 115  #135 = middle, 240 = max, 30 = min
temp_indicatorY = 399

def temp_gauge():

    if temp_value >= 180 and temp_value <= 220:
        screen.blit(temp_indicator_img, (temp_indicatorX, temp_indicatorY))
    elif temp_value >= 170 and temp_value < 180:
        screen.blit(temp_indicator_img, (temp_indicatorX - 10, temp_indicatorY))
    elif temp_value >= 100 and temp_value < 170:
        screen.blit(temp_indicator_img, (temp_indicatorX - 50, temp_indicatorY))
    elif temp_value >= 0 and temp_value < 100:
        screen.blit(temp_indicator_img, (temp_indicatorX - 105, temp_indicatorY))
    elif temp_value > 220 and temp_value <= 250:
        screen.blit(temp_indicator_img, (temp_indicatorX + 10, temp_indicatorY))
    elif temp_value > 250 and temp_value <= 300:
        screen.blit(temp_indicator_img, (temp_indicatorX + 70, temp_indicatorY))
    elif temp_value > 300:
        screen.blit(temp_indicator_img, (temp_indicatorX + 105, temp_indicatorY))

def display_temp():
    temp = temp_font.render((str(temp_value) + ' °F'), True, (255, 255, 255))

    screen.blit(temp, (temp_txt_X, temp_txt_Y))

#Framework
framework_img = pygame.image.load('framework.png')
frameworkX = 8
frameworkY = 95

def framework():
    screen.blit(framework_img, (frameworkX, frameworkY))

#Gradient
gradient_img = pygame.image.load('Gradient.png')
gradientX = 0
gradientY = 0

#Sports
sport_img = pygame.image.load('Gradient_red.png')
sportsX = 0
sportsY = 0

def gradient():
    screen.blit(gradient_img, (gradientX, gradientY))

def sports():
    screen.blit(sport_img, (sportsX, sportsY))

# Buttons
normal_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)
sports_font = pygame.font.Font('Fonts/pirulen rg.ttf', 13)

sports_txt_X = 98
sports_txt_Y = 530
normal_txt_X = 97
normal_txt_Y = 530

def button():
    if button_press is True:
        button_img = pygame.image.load('Sport Button Pressed (no label).png')
    else:
        button_img = pygame.image.load('Sport button not pressed (no label).png')
    screen.blit(button_img, (45, 450))
    # Checks the state and changes the text accordingly
    if sports_mode is False:
        button_label = sports_font.render('Sports', True, (255, 255, 255))
        screen.blit(button_label, (sports_txt_X, sports_txt_Y))
    else:
        button_label = sports_font.render('Normal', True, (255, 255, 255))
        screen.blit(button_label, (normal_txt_X, normal_txt_Y))

#Redraw
def RedrawWindow():
    if sports_mode is False:
        gradient()
    else:
        sports()
    button()
    tachometer(rpm)
    framework()
    display_speed()
    temp_gauge()
    display_temp()
    pygame.display.update()

#Game Loop
app_running = True
while app_running:

    clock.tick(60)

    #screen fill
    screen.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    print(mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        # Checks for when we press the mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if the mouse click was where the button is
            # mouse[0] is the x coordinate, mouse[1] is the y
            if 90 < mouse[0] < 180 and 495 < mouse[1] < 585:
                button_press = True
        # Checks for when we let go of the mouse button
        if event.type == pygame.MOUSEBUTTONUP:
            button_press = False
            if 90 < mouse[0] < 180 and 495 < mouse[1] < 585:
                if sports_mode is False:
                    sports_mode = True
                else:
                    sports_mode = False

    RedrawWindow()

#rpm testing
    if rpm < 5000 and limit == False:
        rpm += 150
        if rpm >= 5000:
            limit = True
    elif limit == True:
        rpm -= 75
        if rpm <= 450:
            limit = False

#speed testing
    if speed_value < 175 and speed_limit == False:
        speed_value += 1
        if speed_value >= 175:
            speed_limit = True
    elif speed_limit == True:
        speed_value -= 1
        if speed_value <= 0:
            speed_limit = False

#temp gauge testing
    if temp_value < 310 and temp_limit == False:
        temp_value += 1
        if temp_value >= 310:
            temp_value = True
    elif temp_value == True:
        temp_value -= 1
        if temp_value <= 0:
            temp_value = False



