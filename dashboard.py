import pygame
import time

#globals
rpm = 0
oil_change_interval = 0
oil_change_count = 0
mileage = 0
limit = False
speed_limit = False
temp_limit = False
current_page = 1
sports_button_press = False
back_button_press = False
reset_button_press = False
interval_button_press = False

# colors_button_press = False

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

#sports mode tach
stachometer_0 = [pygame.image.load('sport_mode/0-1000/Tach1.png'), pygame.image.load('sport_mode/0-1000/Tach2.png'), pygame.image.load('sport_mode/0-1000/Tach3.png'), pygame.image.load('sport_mode/0-1000/Tach4.png'), pygame.image.load('sport_mode/0-1000/Tach5.png'),pygame.image.load('sport_mode/0-1000/Tach6.png'), pygame.image.load('sport_mode/0-1000/Tach7.png'), pygame.image.load('sport_mode/0-1000/Tach8.png')]
stachometer_1 = [pygame.image.load('sport_mode/1000-2000/Tach1.png'), pygame.image.load('sport_mode/1000-2000/Tach2.png'), pygame.image.load('sport_mode/1000-2000/Tach3.png'), pygame.image.load('sport_mode/1000-2000/Tach4.png'), pygame.image.load('sport_mode/1000-2000/Tach5.png'),pygame.image.load('sport_mode/1000-2000/Tach6.png'), pygame.image.load('sport_mode/1000-2000/Tach7.png'), pygame.image.load('sport_mode/1000-2000/Tach8.png')]
stachometer_2 = [pygame.image.load('sport_mode/2000-3000/Tach1.png'), pygame.image.load('sport_mode/2000-3000/Tach2.png'), pygame.image.load('sport_mode/2000-3000/Tach3.png'), pygame.image.load('sport_mode/2000-3000/Tach4.png'), pygame.image.load('sport_mode/2000-3000/Tach5.png'),pygame.image.load('sport_mode/2000-3000/Tach6.png'), pygame.image.load('sport_mode/2000-3000/Tach7.png'), pygame.image.load('sport_mode/2000-3000/Tach8.png'), pygame.image.load('sport_mode/2000-3000/Tach9.png')]
stachometer_3 = [pygame.image.load('sport_mode/3000-4000/Tach1.png'), pygame.image.load('sport_mode/3000-4000/Tach2.png'), pygame.image.load('sport_mode/3000-4000/Tach3.png'), pygame.image.load('sport_mode/3000-4000/Tach4.png'), pygame.image.load('sport_mode/3000-4000/Tach5.png'),pygame.image.load('sport_mode/3000-4000/Tach6.png'), pygame.image.load('sport_mode/3000-4000/Tach7.png')]
stachometer_4 = [pygame.image.load('sport_mode/4000-5000/Tach1.png'), pygame.image.load('sport_mode/4000-5000/Tach2.png'), pygame.image.load('sport_mode/4000-5000/Tach3.png'), pygame.image.load('sport_mode/4000-5000/Tach4.png'), pygame.image.load('sport_mode/4000-5000/Tach5.png'),pygame.image.load('sport_mode/4000-5000/Tach6.png'), pygame.image.load('sport_mode/4000-5000/Tach7.png'), pygame.image.load('sport_mode/4000-5000/Tach8.png')]
stachometer_5 = [pygame.image.load('sport_mode/5000-6000/Tach1.png'), pygame.image.load('sport_mode/5000-6000/Tach2.png'), pygame.image.load('sport_mode/5000-6000/Tach3.png'), pygame.image.load('sport_mode/5000-6000/Tach4.png'), pygame.image.load('sport_mode/5000-6000/Tach5.png'),pygame.image.load('sport_mode/5000-6000/Tach6.png'), pygame.image.load('sport_mode/5000-6000/Tach7.png'), pygame.image.load('sport_mode/5000-6000/Tach8.png'), pygame.image.load('sport_mode/5000-6000/Tach9.png')]
stachometer_6 = [pygame.image.load('sport_mode/6000-7000/Tach1.png'), pygame.image.load('sport_mode/6000-7000/Tach2.png'), pygame.image.load('sport_mode/6000-7000/Tach3.png'), pygame.image.load('sport_mode/6000-7000/Tach4.png'), pygame.image.load('sport_mode/6000-7000/Tach5.png'),pygame.image.load('sport_mode/6000-7000/Tach6.png'), pygame.image.load('sport_mode/6000-7000/Tach7.png')]
stachometer_7 = [pygame.image.load('sport_mode/7000-8000/Tach1.png'), pygame.image.load('sport_mode/7000-8000/Tach2.png'), pygame.image.load('sport_mode/7000-8000/Tach3.png'), pygame.image.load('sport_mode/7000-8000/Tach4.png'), pygame.image.load('sport_mode/7000-8000/Tach5.png'),pygame.image.load('sport_mode/7000-8000/Tach6.png'), pygame.image.load('sport_mode/7000-8000/Tach7.png'), pygame.image.load('sport_mode/7000-8000/Tach8.png'), pygame.image.load('sport_mode/7000-8000/Tach9.png')]
stachometer_8 = [pygame.image.load('sport_mode/8000-9000/Tach1.png'), pygame.image.load('sport_mode/8000-9000/Tach2.png'), pygame.image.load('sport_mode/8000-9000/Tach3.png'), pygame.image.load('sport_mode/8000-9000/Tach4.png'), pygame.image.load('sport_mode/8000-9000/Tach5.png'),pygame.image.load('sport_mode/8000-9000/Tach6.png'), pygame.image.load('sport_mode/8000-9000/Tach7.png')]

def stachometer(rpm):

    #0-1000
    if rpm > 0 and rpm <=142:
        screen.blit(stachometer_0[1], (tachometerX, tachometerY))
    elif rpm > 142 and rpm <= 284:
        screen.blit(stachometer_0[2], (tachometerX, tachometerY))
    elif rpm > 284 and rpm <= 426:
        screen.blit(stachometer_0[3], (tachometerX, tachometerY))
    elif rpm > 426 and rpm <= 568:
        screen.blit(stachometer_0[4], (tachometerX, tachometerY))
    elif rpm > 568 and rpm <= 710:
        screen.blit(stachometer_0[5], (tachometerX, tachometerY))
    elif rpm > 710 and rpm <= 852:
        screen.blit(stachometer_0[6], (tachometerX, tachometerY))
    elif rpm > 852 and rpm <= 1000:
        screen.blit(stachometer_0[7], (tachometerX, tachometerY))

    #1000-2000
    elif rpm > 1000 and rpm <= 1125:
        screen.blit(stachometer_1[0], (tachometerX, tachometerY))
    elif rpm > 1125 and rpm <= 1250:
        screen.blit(stachometer_1[1], (tachometerX, tachometerY))
    elif rpm > 1250 and rpm <= 1375:
        screen.blit(stachometer_1[2], (tachometerX, tachometerY))
    elif rpm > 1375 and rpm <= 1500:
        screen.blit(stachometer_1[3], (tachometerX, tachometerY))
    elif rpm > 1500 and rpm <= 1625:
        screen.blit(stachometer_1[4], (tachometerX, tachometerY))
    elif rpm > 1625 and rpm <= 1750:
        screen.blit(stachometer_1[5], (tachometerX, tachometerY))
    elif rpm > 1750 and rpm <= 1875:
        screen.blit(stachometer_1[6], (tachometerX, tachometerY))
    elif rpm > 1875 and rpm <= 2000:
        screen.blit(stachometer_1[7], (tachometerX, tachometerY))

    #2000-3000
    elif rpm > 2000 and rpm <= 2111:
        screen.blit(stachometer_2[0], (tachometerX, tachometerY))
    elif rpm > 2111 and rpm <= 2222:
        screen.blit(stachometer_2[1], (tachometerX, tachometerY))
    elif rpm > 2222 and rpm <= 2333:
        screen.blit(stachometer_2[2], (tachometerX, tachometerY))
    elif rpm > 2333 and rpm <= 2444:
        screen.blit(stachometer_2[3], (tachometerX, tachometerY))
    elif rpm > 2444 and rpm <= 2555:
        screen.blit(stachometer_2[4], (tachometerX, tachometerY))
    elif rpm > 2555 and rpm <= 2666:
        screen.blit(stachometer_2[5], (tachometerX, tachometerY))
    elif rpm > 2666 and rpm <= 2777:
        screen.blit(stachometer_2[6], (tachometerX, tachometerY))
    elif rpm > 2777 and rpm <= 2888:
        screen.blit(stachometer_2[7], (tachometerX, tachometerY))
    elif rpm > 2888 and rpm <= 3000:
        screen.blit(stachometer_2[8], (tachometerX, tachometerY))

    #3000-4000
    elif rpm > 3000 and rpm <= 3142:
        screen.blit(stachometer_3[0], (tachometerX, tachometerY))
    elif rpm > 3142 and rpm <= 3284:
        screen.blit(stachometer_3[1], (tachometerX, tachometerY))
    elif rpm > 3284 and rpm <= 3426:
        screen.blit(stachometer_3[2], (tachometerX, tachometerY))
    elif rpm > 3426 and rpm <= 3568:
        screen.blit(stachometer_3[3], (tachometerX, tachometerY))
    elif rpm > 3568 and rpm <= 3710:
        screen.blit(stachometer_3[4], (tachometerX, tachometerY))
    elif rpm > 3710 and rpm <= 3852:
        screen.blit(stachometer_3[5], (tachometerX, tachometerY))
    elif rpm > 3852 and rpm <= 4000:
        screen.blit(stachometer_3[6], (tachometerX, tachometerY))

    #4000-5000
    elif rpm > 4000 and rpm <= 4125:
        screen.blit(stachometer_4[0], (tachometerX, tachometerY))
    elif rpm > 4125 and rpm <= 4250:
        screen.blit(stachometer_4[1], (tachometerX, tachometerY))
    elif rpm > 4250 and rpm <= 4375:
        screen.blit(stachometer_4[2], (tachometerX, tachometerY))
    elif rpm > 4375 and rpm <= 4500:
        screen.blit(stachometer_4[3], (tachometerX, tachometerY))
    elif rpm > 4500 and rpm <= 4625:
        screen.blit(stachometer_4[4], (tachometerX, tachometerY))
    elif rpm > 4625 and rpm <= 4750:
        screen.blit(stachometer_4[5], (tachometerX, tachometerY))
    elif rpm > 4750 and rpm <= 4875:
        screen.blit(stachometer_4[6], (tachometerX, tachometerY))
    elif rpm > 4875 and rpm <= 5000:
        screen.blit(stachometer_4[7], (tachometerX, tachometerY))

    #5000-6000
    elif rpm > 5000 and rpm <= 5111:
        screen.blit(stachometer_5[0], (tachometerX, tachometerY))
    elif rpm > 5111 and rpm <= 5222:
        screen.blit(stachometer_5[1], (tachometerX, tachometerY))
    elif rpm > 5222 and rpm <= 5333:
        screen.blit(stachometer_5[2], (tachometerX, tachometerY))
    elif rpm > 5333 and rpm <= 5444:
        screen.blit(stachometer_5[3], (tachometerX, tachometerY))
    elif rpm > 5444 and rpm <= 5555:
        screen.blit(stachometer_5[4], (tachometerX, tachometerY))
    elif rpm > 5555 and rpm <= 5666:
        screen.blit(stachometer_5[5], (tachometerX, tachometerY))
    elif rpm > 5666 and rpm <= 5777:
        screen.blit(stachometer_5[6], (tachometerX, tachometerY))
    elif rpm > 5777 and rpm <= 5888:
        screen.blit(stachometer_5[7], (tachometerX, tachometerY))
    elif rpm > 5888 and rpm <= 6000:
        screen.blit(stachometer_5[8], (tachometerX, tachometerY))

    #6000-7000
    elif rpm > 6000 and rpm <= 6142:
        screen.blit(stachometer_6[0], (tachometerX, tachometerY))
    elif rpm > 6142 and rpm <= 6284:
        screen.blit(stachometer_6[1], (tachometerX, tachometerY))
    elif rpm > 6284 and rpm <= 6426:
        screen.blit(stachometer_6[2], (tachometerX, tachometerY))
    elif rpm > 6426 and rpm <= 6568:
        screen.blit(stachometer_6[3], (tachometerX, tachometerY))
    elif rpm > 6568 and rpm <= 6710:
        screen.blit(stachometer_6[4], (tachometerX, tachometerY))
    elif rpm > 6710 and rpm <= 6852:
        screen.blit(stachometer_6[5], (tachometerX, tachometerY))
    elif rpm > 6852 and rpm <= 7000:
        screen.blit(stachometer_6[6], (tachometerX, tachometerY))

    #7000-8000
    elif rpm > 7000 and rpm <= 7111:
        screen.blit(stachometer_7[0], (tachometerX, tachometerY))
    elif rpm > 7111 and rpm <= 7222:
        screen.blit(stachometer_7[1], (tachometerX, tachometerY))
    elif rpm > 7222 and rpm <= 7333:
        screen.blit(stachometer_7[2], (tachometerX, tachometerY))
    elif rpm > 7333 and rpm <= 7444:
        screen.blit(stachometer_7[3], (tachometerX, tachometerY))
    elif rpm > 7444 and rpm <= 7555:
        screen.blit(stachometer_7[4], (tachometerX, tachometerY))
    elif rpm > 7555 and rpm <= 7666:
        screen.blit(stachometer_7[5], (tachometerX, tachometerY))
    elif rpm > 7666 and rpm <= 7777:
        screen.blit(stachometer_7[6], (tachometerX, tachometerY))
    elif rpm > 7777 and rpm <= 7888:
        screen.blit(stachometer_7[7], (tachometerX, tachometerY))
    elif rpm > 7888 and rpm <= 8000:
        screen.blit(stachometer_7[8], (tachometerX, tachometerY))

    #8000-9000
    elif rpm > 8000 and rpm <= 8142:
        screen.blit(stachometer_8[0], (tachometerX, tachometerY))
    elif rpm > 8142 and rpm <= 8284:
        screen.blit(stachometer_8[1], (tachometerX, tachometerY))
    elif rpm > 8284 and rpm <= 8426:
        screen.blit(stachometer_8[2], (tachometerX, tachometerY))
    elif rpm > 8426 and rpm <= 8568:
        screen.blit(stachometer_8[3], (tachometerX, tachometerY))
    elif rpm > 8568 and rpm <= 8710:
        screen.blit(stachometer_8[4], (tachometerX, tachometerY))
    elif rpm > 8710 and rpm <= 8852:
        screen.blit(stachometer_8[5], (tachometerX, tachometerY))
    elif rpm > 8852 and rpm <= 8000:
        screen.blit(stachometer_8[6], (tachometerX, tachometerY))

    else:
        screen.blit(stachometer_0[0], (tachometerX, tachometerY))


# Speed
speed_value = 0
speed_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 50)
mphfont = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)

sspeed_font = pygame.font.Font('Fonts/pirulen rg.ttf', 50)
smphfont = pygame.font.Font('Fonts/pirulen rg.ttf', 25)


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

def sdisplay_speed():
    speed = sspeed_font.render(str(speed_value), True, (255, 255, 255))
    mph = smphfont.render("MPH", True, (255, 255, 255))

    if speed_value <= 9:
        screen.blit(speed, (speedtextX0-10, speedtextY0))
    elif speed_value >= 10 and speed_value <= 99:
        screen.blit(speed, (speedtextX10-18, speedtextY10))
    elif speed_value >= 100:
        screen.blit(speed, (speedtextX100-18, speedtextY100))

    screen.blit(mph, (mphtextX-13, mphtextY))

#Temp Gauge
temp_value = 0

temp_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)
stemp_font = pygame.font.Font('Fonts/pirulen rg.ttf', 20)

temp_txt_X = 30
temp_txt_Y = 420

temp_indicator_img = pygame.image.load('temp_gauge/indicator.png')
temp_indicatorX = 140  #135 = middle, 240 = max, 30 = min
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
        screen.blit(temp_indicator_img, (temp_indicatorX + 95, temp_indicatorY))

def display_temp():
    temp = temp_font.render(('Coolant Temp ' + str(temp_value) + ' °F'), True, (255, 255, 255))

    screen.blit(temp, (temp_txt_X, temp_txt_Y))

def sdisplay_temp():
    temp = stemp_font.render(('Coolant ' + str(temp_value) + ' °F'), True, (255, 255, 255))

    screen.blit(temp, (temp_txt_X-5, temp_txt_Y))

#Framework
framework_img = pygame.image.load('framework.png')
frameworkX = 8
frameworkY = 95

sframework_img = pygame.image.load('sport_mode/framework/Framework.png')
frameworkX = 8
frameworkY = 95

def framework():
    screen.blit(framework_img, (frameworkX, frameworkY))

def sframework():
    screen.blit(sframework_img, (frameworkX, frameworkY))

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

#Button Text
sports_txt_X = 98
sports_txt_Y = 530
normal_txt_X = 97
normal_txt_Y = 530

def sports_button():
    if sports_button_press is True:
        button_img = pygame.image.load('Sport Button Pressed (no label).png')
    else:
        button_img = pygame.image.load('Sport button not pressed (no label).png')
    screen.blit(button_img, (45, 450))
    # Checks the state and changes the text accordingly
    if current_page != 2:
        button_label = sports_font.render('Sports', True, (255, 255, 255))
        screen.blit(button_label, (sports_txt_X, sports_txt_Y))
    else:
        button_label = sports_font.render('Normal', True, (255, 255, 255))
        screen.blit(button_label, (normal_txt_X, normal_txt_Y))


def back_button():
    if back_button_press is True:
        back_img = pygame.image.load('Back Button Pressed.png')
    else:
        back_img = pygame.image.load('Back Button.png')
    screen.blit(back_img, (10, 425))

def reset_button():
    if reset_button_press is True:
        reset_img = pygame.image.load('Reset Interval Button Pressed.png')
    else:
        reset_img = pygame.image.load('Reset Interval Button.png')
    screen.blit(reset_img, (700, 425))

def interval_button():
    if interval_button_press is True:
        interval_img = pygame.image.load('Interval Button Pressed.png')
    else:
        interval_img = pygame.image.load('Interval Button.png')
    screen.blit(interval_img, (825, 425))

# Colors button
# colors_txt_X = 809
# colors_txt_Y = 530
#
# def colors_button():
#     if colors_button_press is True:
#         colors_img = pygame.image.load('Sport Button Pressed (no label).png')
#     else:
#         colors_img = pygame.image.load('Sport button not pressed (no label).png')
#     screen.blit(colors_img, (754, 450))
#     colors_label = sports_font.render('Colors', True, (255, 255, 255))
#     screen.blit(colors_label, (colors_txt_X, colors_txt_Y))

#Maintenance Display

#File Objects and Maintenance and Mileage Tracking
with open('maintenance/interval.txt', 'r+') as int_file:
    oil_change_string = int_file.readline()
    oil_change_interval = int(oil_change_string)


with open('maintenance/mileage.txt', 'r+') as mileage_file:
    mileage_string = mileage_file.readline()
    mileage = int(mileage_string)

def oil_change_counter(mileage, interval):
    oil_change_count = interval - mileage
    return oil_change_count

oil_change_count = oil_change_counter(mileage, oil_change_interval)

def display_oilchange_distance(oil_change_count):
    oil_txt_X = 265
    oil_txt_Y = 290

    oil_change_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 40)
    oil_change = oil_change_font.render(('Oil Change Due ' + str(oil_change_count) + ' Miles'), True, (255, 255, 255))
    screen.blit(oil_change, (oil_txt_X, oil_txt_Y))




#display functions
def displays():
    sports_button()
    tachometer(rpm)
    framework()
    display_speed()
    temp_gauge()
    display_temp()

def sports_display():
    stachometer(rpm)
    sports_button()
    sframework()
    sdisplay_speed()
    temp_gauge()
    sdisplay_temp()

def maintenance_display():
    display_oilchange_distance(oil_change_count)
    reset_button()
    interval_button()
    back_button()

#Redraw
def RedrawWindow():
    # Checks which background image to use
    if current_page == 2:
        sports()

    else:
        gradient()

    # Checks if the current screen needs the gauges and normal information
    if current_page < 3 and current_page != 2:
        displays()
    else:
        if current_page == 2:
            sports_display()
        elif current_page == 3:
            maintenance_display()
        elif current_page == 4:
            back_button()
        elif current_page == 5:
            back_button()

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
            if 90 < mouse[0] < 180 and 495 < mouse[1] < 585 and current_page < 3:
                sports_button_press = True
            elif 56 < mouse[0] < 146 and 471 < mouse[1] < 561 and current_page > 2:
                back_button_press = True
            elif 745 < mouse[0] < 835 and 471 < mouse[1] < 561:
                reset_button_press = True
            elif 870 < mouse[0] < 960 and 471 < mouse[1] < 561:
                interval_button_press = True
        # Checks for when we let go of the mouse button
        if event.type == pygame.MOUSEBUTTONUP:
            interval_button_press = reset_button_press = diagnostic_press = maintenance_press = back_button_press = sports_button_press = False
            # current_page condition is used to prevent users from going to pages in the wrong order
            # ex. Going from maintenance to sports mode
            if 90 < mouse[0] < 180 and 495 < mouse[1] < 585 and current_page < 3:
                if current_page != 2:
                    current_page = 2
                else:
                    current_page = 1
            # Goes to vehicle maintenance
            elif 10 < mouse[0] < 270 and 130 < mouse[1] < 300 and current_page < 3:
                current_page = 3
            # Goes to vehicle diagnostics
            elif 754 < mouse[0] < 1016 and 130 < mouse[1] < 300 and current_page < 3:
                current_page = 5
            # Back button
            elif 56 < mouse[0] < 146 and 471 < mouse[1] < 561:
                if current_page == 3 or current_page == 5:
                    current_page = 1
                else:
                    current_page -= 1
            # Reset button
            # elif 745 < mouse[0] < 835 and 471 < mouse[1] < 561:
                # Reset the mileage
            # Interval button
            elif 870 < mouse[0] < 960 and 471 < mouse[1] < 561:
                current_page = 4

#Mileage/Oil Change Interval Functions

    oil_change_count = oil_change_counter(mileage, oil_change_interval)
    convert_mileage = str(mileage)

    with open('maintenance/mileage.txt', 'w') as mileage_file:
        mileage_file.write(convert_mileage)


#Redraw UI
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

#mileage increment testing
    mileage = mileage + 1




