import obd
import pygame
import time
import obd
#obd.logger.setLevel(obd.logging.DEBUG)
startTime = time.time()

#obd.logger.setLevel(obd.logging.DEBUG)
startTime = time.time()

#globals
rpm = 0
rpm_target_temp = 0
oil_change_interval = 0
oil_change_count = 0
transmission_oil_change_interval = 0
brake_change_interval = 0
oil_mileage = 0
transmission_oil_mileage = 0
brake_mileage = 0
trip_distance = 0
prev_trip_distance = 0

avg_mpg = 0
inst_mpg = 0
maf_reading = 0
throttle_position = 0
load = 0
fuel_pressure = 0
intake_temp = 0
temp_value = 0


limit = False
speed_limit = False
temp_limit = False
current_page = 1
sports_button_press = False
back_button_press = False
reset_button_press = False
interval_button_press = False
three_thousand_press = False
five_thousand_press = False
seven_thousand_five_press = False
ten_thousand_press = False
fifteen_thousand_press = False
clear_dtc_press = False
dtc_code_present = False
dtc_code = 'N/A'
current_maintenance = 1
increment_press = False
decrement_press = False
# colors_button_press = False

#initialize the interface
pygame.init()

#clock
clock = pygame.time.Clock()

#create screen
infoObject = pygame.display.Info()
display_width = infoObject.current_w
display_height = infoObject.current_h

screen = pygame.display.set_mode((display_width,display_height))
#screen = pygame.display.set_mode((1024, 600))
#screen = pygame.display.set_mode((800, 480))

#Title of app
pygame.display.set_caption("Dashboard 2.0")

#OBD Initilization
#connection = obd.Async(fast=False, check_voltage=True)
connection = obd.Async(fast=False)
#connection = obd.OBD()

#logo and project heading
logo_img = pygame.image.load('logos_headings/Chilly Willie.png')
project_heading_img = pygame.image.load('logos_headings/Dashboard 2.0.png')

def display_logos():
    screen.blit(logo_img, (910, 450))
    screen.blit(project_heading_img, (390, 25))
    
#Tachometer
tachometerX = 205
tachometerY = 0

blank_tach_img = pygame.image.load('needle_tach/Tach.png')
sport_tach_img = pygame.image.load('sport_mode/Tach_sports.png')
needle_img = pygame.image.load('needle_tach/needle.png')
inner_tach = pygame.image.load('needle_tach/inner_tach.png')

def display_blank_tach():
    screen.blit(blank_tach_img, (tachometerX, tachometerY))

def display_blank_sports_tach():
    screen.blit(sport_tach_img, (tachometerX, tachometerY))

def display_inner_tach():
    mx, my = pygame.mouse.get_pos()
    screen.blit(inner_tach, (433, 225))

def display_needle(rotation_angle):
    mx, my = pygame.mouse.get_pos()

    img_copy = pygame.transform.rotate(needle_img, rotation_angle)
    screen.blit(img_copy, (515 - int(img_copy.get_width() / 2), int(305 - img_copy.get_height() /2)))

def needle_positioning():
    # 0 -1000
    rotation_angle = 0
    if rpm > 0 and rpm <= 29:
        rotation_angle = -1
    elif rpm > 29 and rpm <= 58:
        rotation_angle = -2
    elif rpm > 58 and rpm <= 87:
        rotation_angle = -3
    elif rpm > 87 and rpm <= 116:
        rotation_angle = -4
    elif rpm > 116 and rpm <= 145:
        rotation_angle = -5
    elif rpm > 145 and rpm <= 174:
        rotation_angle = -6
    elif rpm > 174 and rpm <= 203:
        rotation_angle = -7
    elif rpm > 203 and rpm <= 232:
        rotation_angle = -8
    elif rpm > 232 and rpm <= 261:
        rotation_angle = -9
    elif rpm > 261 and rpm <= 290:
        rotation_angle = -10
    elif rpm > 290 and rpm <= 319:
        rotation_angle = -11
    elif rpm > 319 and rpm <= 348:
        rotation_angle = -12
    elif rpm > 348 and rpm <= 377:
        rotation_angle = -13
    elif rpm > 377 and rpm <= 406:
        rotation_angle = -14
    elif rpm > 406 and rpm <= 435:
        rotation_angle = -15
    elif rpm > 435 and rpm <= 464:
        rotation_angle = -16
    elif rpm > 464 and rpm <= 493:
        rotation_angle = -17
    elif rpm > 493 and rpm <= 522:
        rotation_angle = -18
    elif rpm > 522 and rpm <= 551:
        rotation_angle = -19
    elif rpm > 551 and rpm <= 580:
        rotation_angle = -20
    elif rpm > 580 and rpm <= 609:
        rotation_angle = -21
    elif rpm > 609 and rpm <= 638:
        rotation_angle = -22
    elif rpm > 638 and rpm <= 667:
        rotation_angle = -23
    elif rpm > 667 and rpm <= 696:
        rotation_angle = -24
    elif rpm > 696 and rpm <= 725:
        rotation_angle = -25
    elif rpm > 725 and rpm <= 754:
        rotation_angle = -26
    elif rpm > 754 and rpm <= 783:
        rotation_angle = -27
    elif rpm > 783 and rpm <= 812:
        rotation_angle = -28
    elif rpm > 812 and rpm <= 841:
        rotation_angle = -29
    elif rpm > 841 and rpm <= 870:
        rotation_angle = -30
    elif rpm > 870 and rpm <= 899:
        rotation_angle = -31
    elif rpm > 899 and rpm <= 928:
        rotation_angle = -32
    elif rpm > 928 and rpm <= 957:
        rotation_angle = -33
    elif rpm > 957 and rpm <= 986:
        rotation_angle = -34
    elif rpm > 986 and rpm <= 1000:
        rotation_angle = -35

    #1000-2000
    elif rpm > 1000 and rpm <= 1031:
        rotation_angle = -36
    elif rpm > 1031 and rpm <= 1061:
        rotation_angle = -37
    elif rpm > 1061 and rpm <= 1093:
        rotation_angle = -38
    elif rpm > 1093 and rpm <= 1124:
        rotation_angle = -39
    elif rpm > 1124 and rpm <= 1155:
        rotation_angle = -40
    elif rpm > 1155 and rpm <= 1186:
        rotation_angle = -41
    elif rpm > 1186 and rpm <= 1217:
        rotation_angle = -42
    elif rpm > 1217 and rpm <= 1248:
        rotation_angle = -43
    elif rpm > 1248 and rpm <= 1279:
        rotation_angle = -44
    elif rpm > 1279 and rpm <= 1310:
        rotation_angle = -45
    elif rpm > 1310 and rpm <= 1341:
        rotation_angle = -46
    elif rpm > 1341 and rpm <= 1372:
        rotation_angle = -47
    elif rpm > 1372 and rpm <= 1403:
        rotation_angle = -48
    elif rpm > 1403 and rpm <= 1434:
        rotation_angle = -49
    elif rpm > 1434 and rpm <= 1465:
        rotation_angle = -50
    elif rpm > 1465 and rpm <= 1496:
        rotation_angle = -51
    elif rpm > 1496 and rpm <= 1527:
        rotation_angle = -52
    elif rpm > 1527 and rpm <= 1558:
        rotation_angle = -53
    elif rpm > 1558 and rpm <= 1589:
        rotation_angle = -54
    elif rpm > 1589 and rpm <= 1620:
        rotation_angle = -55
    elif rpm > 1620 and rpm <= 1651:
        rotation_angle = -56
    elif rpm > 1651 and rpm <= 1682:
        rotation_angle = -57
    elif rpm > 1682 and rpm <= 1713:
        rotation_angle = -58
    elif rpm > 1713 and rpm <= 1744:
        rotation_angle = -59
    elif rpm > 1744 and rpm <= 1775:
        rotation_angle = -60
    elif rpm > 1775 and rpm <= 1806:
        rotation_angle = -61
    elif rpm > 1806 and rpm <= 1837:
        rotation_angle = -62
    elif rpm > 1837 and rpm <= 1868:
        rotation_angle = -63
    elif rpm > 1868 and rpm <= 1899:
        rotation_angle = -64
    elif rpm > 1899 and rpm <= 1930:
        rotation_angle = -65
    elif rpm > 1930 and rpm <= 1961:
        rotation_angle = -66
    elif rpm > 1961 and rpm <= 2000:
        rotation_angle = -67

    #2000-3000
    elif rpm > 2000 and rpm <= 2031:
        rotation_angle = -68
    elif rpm > 2031 and rpm <= 2061:
        rotation_angle = -69
    elif rpm > 2061 and rpm <= 2093:
        rotation_angle = -70
    elif rpm > 2093 and rpm <= 2124:
        rotation_angle = -71
    elif rpm > 2124 and rpm <= 2155:
        rotation_angle = -72
    elif rpm > 2155 and rpm <= 2186:
        rotation_angle = -73
    elif rpm > 2186 and rpm <= 2217:
        rotation_angle = -74
    elif rpm > 2217 and rpm <= 2248:
        rotation_angle = -75
    elif rpm > 2248 and rpm <= 2279:
        rotation_angle = -76
    elif rpm > 2279 and rpm <= 2310:
        rotation_angle = -77
    elif rpm > 2310 and rpm <= 2341:
        rotation_angle = -78
    elif rpm > 2341 and rpm <= 2372:
        rotation_angle = -79
    elif rpm > 2372 and rpm <= 2403:
        rotation_angle = -80
    elif rpm > 2403 and rpm <= 2434:
        rotation_angle = -81
    elif rpm > 2434 and rpm <= 2465:
        rotation_angle = -82
    elif rpm > 2465 and rpm <= 2496:
        rotation_angle = -83
    elif rpm > 2496 and rpm <= 2527:
        rotation_angle = -84
    elif rpm > 2527 and rpm <= 2558:
        rotation_angle = -85
    elif rpm > 2558 and rpm <= 2589:
        rotation_angle = -86
    elif rpm > 2589 and rpm <= 2620:
        rotation_angle = -87
    elif rpm > 2620 and rpm <= 2651:
        rotation_angle = -88
    elif rpm > 2651 and rpm <= 2682:
        rotation_angle = -89
    elif rpm > 2682 and rpm <= 2713:
        rotation_angle = -90
    elif rpm > 2713 and rpm <= 2744:
        rotation_angle = -91
    elif rpm > 2744 and rpm <= 2775:
        rotation_angle = -92
    elif rpm > 2775 and rpm <= 2806:
        rotation_angle = -93
    elif rpm > 2806 and rpm <= 2837:
        rotation_angle = -94
    elif rpm > 2837 and rpm <= 2868:
        rotation_angle = -95
    elif rpm > 2868 and rpm <= 2899:
        rotation_angle = -96
    elif rpm > 2899 and rpm <= 2930:
        rotation_angle = -97
    elif rpm > 2930 and rpm <= 2961:
        rotation_angle = -98
    elif rpm > 2961 and rpm <= 2992:
        rotation_angle = -99
    elif rpm > 2992 and rpm <= 3000:
        rotation_angle = -100

    #3000-4000
    elif rpm > 3000 and rpm <= 3029:
        rotation_angle = -101
    elif rpm > 3029 and rpm <= 3058:
        rotation_angle = -102
    elif rpm > 3058 and rpm <= 3087:
        rotation_angle = -103
    elif rpm > 3087 and rpm <= 3116:
        rotation_angle = -104
    elif rpm > 3116 and rpm <= 3145:
        rotation_angle = -105
    elif rpm > 3145 and rpm <= 3174:
        rotation_angle = -106
    elif rpm > 3174 and rpm <= 3203:
        rotation_angle = -107
    elif rpm > 3203 and rpm <= 3232:
        rotation_angle = -108
    elif rpm > 3232 and rpm <= 3261:
        rotation_angle = -109
    elif rpm > 3261 and rpm <= 3290:
        rotation_angle = -110
    elif rpm > 3290 and rpm <= 3319:
        rotation_angle = -111
    elif rpm > 3319 and rpm <= 3348:
        rotation_angle = -112
    elif rpm > 3348 and rpm <= 3377:
        rotation_angle = -113
    elif rpm > 3377 and rpm <= 3406:
        rotation_angle = -114
    elif rpm > 3406 and rpm <= 3435:
        rotation_angle = -115
    elif rpm > 3435 and rpm <= 3464:
        rotation_angle = -116
    elif rpm > 3464 and rpm <= 3493:
        rotation_angle = -117
    elif rpm > 3493 and rpm <= 3522:
        rotation_angle = -118
    elif rpm > 3522 and rpm <= 3551:
        rotation_angle = -119
    elif rpm > 3551 and rpm <= 3580:
        rotation_angle = -120
    elif rpm > 3580 and rpm <= 3609:
        rotation_angle = -121
    elif rpm > 3609 and rpm <= 3638:
        rotation_angle = -122
    elif rpm > 3638 and rpm <= 3667:
        rotation_angle = -123
    elif rpm > 3667 and rpm <= 3696:
        rotation_angle = -124
    elif rpm > 3696 and rpm <= 3725:
        rotation_angle = -125
    elif rpm > 3725 and rpm <= 3754:
        rotation_angle = -126
    elif rpm > 3754 and rpm <= 3783:
        rotation_angle = -127
    elif rpm > 3783 and rpm <= 3812:
        rotation_angle = -128
    elif rpm > 3812 and rpm <= 3841:
        rotation_angle = -129
    elif rpm > 3841 and rpm <= 3870:
        rotation_angle = -130
    elif rpm > 3870 and rpm <= 3899:
        rotation_angle = -131
    elif rpm > 3899 and rpm <= 3928:
        rotation_angle = -132
    elif rpm > 3928 and rpm <= 3957:
        rotation_angle = -133
    elif rpm > 3957 and rpm <= 3986:
        rotation_angle = -134
    elif rpm > 3986 and rpm <= 4000:
        rotation_angle = -135

    #4000-5000
    elif rpm > 4000 and rpm <= 4029:
        rotation_angle = -136
    elif rpm > 4029 and rpm <= 4058:
        rotation_angle = -137
    elif rpm > 4058 and rpm <= 4087:
        rotation_angle = -138
    elif rpm > 4087 and rpm <= 4116:
        rotation_angle = -139
    elif rpm > 4116 and rpm <= 4145:
        rotation_angle = -140
    elif rpm > 4145 and rpm <= 4174:
        rotation_angle = -141
    elif rpm > 4174 and rpm <= 4203:
        rotation_angle = -142
    elif rpm > 4203 and rpm <= 4232:
        rotation_angle = -143
    elif rpm > 4232 and rpm <= 4261:
        rotation_angle = -144
    elif rpm > 4261 and rpm <= 4290:
        rotation_angle = -145
    elif rpm > 4290 and rpm <= 4319:
        rotation_angle = -146
    elif rpm > 4319 and rpm <= 4348:
        rotation_angle = -147
    elif rpm > 4348 and rpm <= 4377:
        rotation_angle = -148
    elif rpm > 4377 and rpm <= 4406:
        rotation_angle = -149
    elif rpm > 4406 and rpm <= 4435:
        rotation_angle = -150
    elif rpm > 4435 and rpm <= 4464:
        rotation_angle = -151
    elif rpm > 4464 and rpm <= 4493:
        rotation_angle = -152
    elif rpm > 4493 and rpm <= 4522:
        rotation_angle = -153
    elif rpm > 4522 and rpm <= 4551:
        rotation_angle = -154
    elif rpm > 4551 and rpm <= 4580:
        rotation_angle = -155
    elif rpm > 4580 and rpm <= 4609:
        rotation_angle = -156
    elif rpm > 4609 and rpm <= 4638:
        rotation_angle = -157
    elif rpm > 4638 and rpm <= 4667:
        rotation_angle = -158
    elif rpm > 4667 and rpm <= 4696:
        rotation_angle = -159
    elif rpm > 4696 and rpm <= 4725:
        rotation_angle = -160
    elif rpm > 4725 and rpm <= 4754:
        rotation_angle = -161
    elif rpm > 4754 and rpm <= 4783:
        rotation_angle = -162
    elif rpm > 4783 and rpm <= 4812:
        rotation_angle = -163
    elif rpm > 4812 and rpm <= 4841:
        rotation_angle = -164
    elif rpm > 4841 and rpm <= 4870:
        rotation_angle = -165
    elif rpm > 4870 and rpm <= 4899:
        rotation_angle = -166
    elif rpm > 4899 and rpm <= 4928:
        rotation_angle = -167
    elif rpm > 4928 and rpm <= 4957:
        rotation_angle = -168
    elif rpm > 4957 and rpm <= 4986:
        rotation_angle = -169
    elif rpm > 4986 and rpm <= 5000:
        rotation_angle = -170

    #5000-6000
    elif rpm > 5000 and rpm <= 5029:
        rotation_angle = -171
    elif rpm > 5029 and rpm <= 5058:
        rotation_angle = -172
    elif rpm > 5058 and rpm <= 5087:
        rotation_angle = -173
    elif rpm > 5087 and rpm <= 5116:
        rotation_angle = -174
    elif rpm > 5116 and rpm <= 5145:
        rotation_angle = -175
    elif rpm > 5145 and rpm <= 5174:
        rotation_angle = -176
    elif rpm > 5174 and rpm <= 5203:
        rotation_angle = -177
    elif rpm > 5203 and rpm <= 5232:
        rotation_angle = -178
    elif rpm > 5232 and rpm <= 5261:
        rotation_angle = -179
    elif rpm > 5261 and rpm <= 5290:
        rotation_angle = -180
    elif rpm > 5290 and rpm <= 5319:
        rotation_angle = -181
    elif rpm > 5319 and rpm <= 5348:
        rotation_angle = -182
    elif rpm > 5348 and rpm <= 5377:
        rotation_angle = -183
    elif rpm > 5377 and rpm <= 5406:
        rotation_angle = -184
    elif rpm > 5406 and rpm <= 5435:
        rotation_angle = -185
    elif rpm > 5435 and rpm <= 5464:
        rotation_angle = -186
    elif rpm > 5464 and rpm <= 5493:
        rotation_angle = -187
    elif rpm > 5493 and rpm <= 5522:
        rotation_angle = -188
    elif rpm > 5522 and rpm <= 5551:
        rotation_angle = -189
    elif rpm > 5551 and rpm <= 5580:
        rotation_angle = -190
    elif rpm > 5580 and rpm <= 5609:
        rotation_angle = -191
    elif rpm > 5609 and rpm <= 5638:
        rotation_angle = -192
    elif rpm > 5638 and rpm <= 5667:
        rotation_angle = -193
    elif rpm > 5667 and rpm <= 5696:
        rotation_angle = -194
    elif rpm > 5696 and rpm <= 5725:
        rotation_angle = -195
    elif rpm > 5725 and rpm <= 5754:
        rotation_angle = -196
    elif rpm > 5754 and rpm <= 5783:
        rotation_angle = -197
    elif rpm > 5783 and rpm <= 5812:
        rotation_angle = -198
    elif rpm > 5812 and rpm <= 5841:
        rotation_angle = -199
    elif rpm > 5841 and rpm <= 5870:
        rotation_angle = -200
    elif rpm > 5870 and rpm <= 5899:
        rotation_angle = -201
    elif rpm > 5899 and rpm <= 5928:
        rotation_angle = -202
    elif rpm > 5928 and rpm <= 5957:
        rotation_angle = -203
    elif rpm > 5957 and rpm <= 5986:
        rotation_angle = -204
    elif rpm > 5986 and rpm <= 6000:
        rotation_angle = -205

    # 6000-7000
    elif rpm > 6000 and rpm <= 6029:
        rotation_angle = -206
    elif rpm > 6029 and rpm <= 6058:
        rotation_angle = -207
    elif rpm > 6058 and rpm <= 6087:
        rotation_angle = -208
    elif rpm > 6087 and rpm <= 6116:
        rotation_angle = -209
    elif rpm > 6116 and rpm <= 6145:
        rotation_angle = -210
    elif rpm > 6145 and rpm <= 6174:
        rotation_angle = -211
    elif rpm > 6174 and rpm <= 6203:
        rotation_angle = -212
    elif rpm > 6203 and rpm <= 6232:
        rotation_angle = -213
    elif rpm > 6232 and rpm <= 6261:
        rotation_angle = -214
    elif rpm > 6261 and rpm <= 6290:
        rotation_angle = -215
    elif rpm > 6290 and rpm <= 6319:
        rotation_angle = -216
    elif rpm > 6319 and rpm <= 6348:
        rotation_angle = -217
    elif rpm > 6348 and rpm <= 6377:
        rotation_angle = -218
    elif rpm > 6377 and rpm <= 6406:
        rotation_angle = -219
    elif rpm > 6406 and rpm <= 6435:
        rotation_angle = -220
    elif rpm > 6435 and rpm <= 6464:
        rotation_angle = -221
    elif rpm > 6464 and rpm <= 6493:
        rotation_angle = -222
    elif rpm > 6493 and rpm <= 6522:
        rotation_angle = -223
    elif rpm > 6522 and rpm <= 6551:
        rotation_angle = -224
    elif rpm > 6551 and rpm <= 6580:
        rotation_angle = -225
    elif rpm > 6580 and rpm <= 6609:
        rotation_angle = -226
    elif rpm > 6609 and rpm <= 6638:
        rotation_angle = -227
    elif rpm > 6638 and rpm <= 6667:
        rotation_angle = -228
    elif rpm > 6667 and rpm <= 6696:
        rotation_angle = -229
    elif rpm > 6696 and rpm <= 6725:
        rotation_angle = -230
    elif rpm > 6725 and rpm <= 6754:
        rotation_angle = -231
    elif rpm > 6754 and rpm <= 6783:
        rotation_angle = -232
    elif rpm > 6783 and rpm <= 6812:
        rotation_angle = -233
    elif rpm > 6812 and rpm <= 6841:
        rotation_angle = -234
    elif rpm > 6841 and rpm <= 6870:
        rotation_angle = -235
    elif rpm > 6870 and rpm <= 6899:
        rotation_angle = -236
    elif rpm > 6899 and rpm <= 6928:
        rotation_angle = -237
    elif rpm > 6928 and rpm <= 6957:
        rotation_angle = -238
    elif rpm > 6957 and rpm <= 6986:
        rotation_angle = -239
    elif rpm > 6986 and rpm <= 7000:
        rotation_angle = -240

    # 7000-8000
    elif rpm > 7000 and rpm <= 7029:
        rotation_angle = -241
    elif rpm > 7029 and rpm <= 7058:
        rotation_angle = -242
    elif rpm > 7058 and rpm <= 7087:
        rotation_angle = -243
    elif rpm > 7087 and rpm <= 7116:
        rotation_angle = -244
    elif rpm > 7116 and rpm <= 7145:
        rotation_angle = -245
    elif rpm > 7145 and rpm <= 7174:
        rotation_angle = -246
    elif rpm > 7174 and rpm <= 7203:
        rotation_angle = -247
    elif rpm > 7203 and rpm <= 7232:
        rotation_angle = -248
    elif rpm > 7232 and rpm <= 7261:
        rotation_angle = -249
    elif rpm > 7261 and rpm <= 7290:
        rotation_angle = -250
    elif rpm > 7290 and rpm <= 7319:
        rotation_angle = -251
    elif rpm > 7319 and rpm <= 7348:
        rotation_angle = -252
    elif rpm > 7348 and rpm <= 7377:
        rotation_angle = -253
    elif rpm > 7377 and rpm <= 7406:
        rotation_angle = -254
    elif rpm > 7406 and rpm <= 7435:
        rotation_angle = -255
    elif rpm > 7435 and rpm <= 7464:
        rotation_angle = -256
    elif rpm > 7464 and rpm <= 7493:
        rotation_angle = -257
    elif rpm > 7493 and rpm <= 7522:
        rotation_angle = -258
    elif rpm > 7522 and rpm <= 7551:
        rotation_angle = -259
    elif rpm > 7551 and rpm <= 7580:
        rotation_angle = -260
    elif rpm > 7580 and rpm <= 7609:
        rotation_angle = -261
    elif rpm > 7609 and rpm <= 7638:
        rotation_angle = -262
    elif rpm > 7638 and rpm <= 7667:
        rotation_angle = -263
    elif rpm > 7667 and rpm <= 7696:
        rotation_angle = -264
    elif rpm > 7696 and rpm <= 7725:
        rotation_angle = -265
    elif rpm > 7725 and rpm <= 7754:
        rotation_angle = -266
    elif rpm > 7754 and rpm <= 7783:
        rotation_angle = -267
    elif rpm > 7783 and rpm <= 7812:
        rotation_angle = -268
    elif rpm > 7812 and rpm <= 7841:
        rotation_angle = -269
    elif rpm > 7841 and rpm <= 7870:
        rotation_angle = -270
    elif rpm > 7870 and rpm <= 7899:
        rotation_angle = -271
    elif rpm > 7899 and rpm <= 7928:
        rotation_angle = -272
    elif rpm > 7928 and rpm <= 7957:
        rotation_angle = -273
    elif rpm > 7957 and rpm <= 7986:
        rotation_angle = -274
    elif rpm > 7986 and rpm <= 8000:
        rotation_angle = -275

    # 8000-9000
    elif rpm > 8000 and rpm <= 8031:
        rotation_angle = -276
    elif rpm > 8031 and rpm <= 8061:
        rotation_angle = -277
    elif rpm > 8061 and rpm <= 8093:
        rotation_angle = -278
    elif rpm > 8093 and rpm <= 8124:
        rotation_angle = -279
    elif rpm > 8124 and rpm <= 8155:
        rotation_angle = -280
    elif rpm > 8155 and rpm <= 8186:
        rotation_angle = -281
    elif rpm > 8186 and rpm <= 8217:
        rotation_angle = -282
    elif rpm > 8217 and rpm <= 8248:
        rotation_angle = -283
    elif rpm > 8248 and rpm <= 8279:
        rotation_angle = -284
    elif rpm > 8279 and rpm <= 8310:
        rotation_angle = -285
    elif rpm > 8310 and rpm <= 8341:
        rotation_angle = -286
    elif rpm > 8341 and rpm <= 8372:
        rotation_angle = -287
    elif rpm > 8372 and rpm <= 8403:
        rotation_angle = -288
    elif rpm > 8403 and rpm <= 8434:
        rotation_angle = -289
    elif rpm > 8434 and rpm <= 8465:
        rotation_angle = -290
    elif rpm > 8465 and rpm <= 8496:
        rotation_angle = -291
    elif rpm > 8496 and rpm <= 8527:
        rotation_angle = -292
    elif rpm > 8527 and rpm <= 8558:
        rotation_angle = -293
    elif rpm > 8558 and rpm <= 8589:
        rotation_angle = -294
    elif rpm > 8589 and rpm <= 8620:
        rotation_angle = -295
    elif rpm > 8620 and rpm <= 8651:
        rotation_angle = -296
    elif rpm > 8651 and rpm <= 8682:
        rotation_angle = -297
    elif rpm > 8682 and rpm <= 8713:
        rotation_angle = -298
    elif rpm > 8713 and rpm <= 8744:
        rotation_angle = -299
    elif rpm > 8744 and rpm <= 8775:
        rotation_angle = -300
    elif rpm > 8775 and rpm <= 8806:
        rotation_angle = -301
    elif rpm > 8806 and rpm <= 8837:
        rotation_angle = -302
    elif rpm > 8837 and rpm <= 8868:
        rotation_angle = -303
    elif rpm > 8868 and rpm <= 8899:
        rotation_angle = -304
    elif rpm > 8899 and rpm <= 8930:
        rotation_angle = -305
    elif rpm > 8930 and rpm <= 8961:
        rotation_angle = -306
    elif rpm > 8961 and rpm <= 9000:
        rotation_angle = -307

    return rotation_angle

# Speed
speed_value = 0
speed_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 50)
mphfont = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)

rpm_font = pygame.font.Font('Fonts/pirulen rg.ttf', 34)
srpmfont = pygame.font.Font('Fonts/pirulen rg.ttf', 25)


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

def sdisplay_rpm():
    srpm = rpm_font.render(str(rpm_target), True, (255, 255, 255))
    rpm_text = srpmfont.render("RPM", True, (255, 255, 255))

    if rpm_target <= 9:
        screen.blit(srpm, (speedtextX0, speedtextY0+15))
    elif rpm_target >= 10 and rpm_target <= 99:
        screen.blit(srpm, (speedtextX10-5, speedtextY10+15))
    elif rpm_target >= 100 and rpm_target <= 999:
        screen.blit(srpm, (speedtextX10 - 20, speedtextY10 + 15))
    elif rpm_target >= 1000 and rpm_target <= 1999:
        screen.blit(srpm, (speedtextX10 - 22, speedtextY10 + 15))
    elif rpm >= 2000:
        screen.blit(srpm, (speedtextX100-25, speedtextY100+15))

    screen.blit(rpm_text, (mphtextX-10, mphtextY-10))

#main display information
def display_more_info():
    info_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 30)

    rpm_norm = info_font.render('Tach ' + str(rpm_target) + ' RPM', True, (255, 255, 255))
    screen.blit(rpm_norm, (775, 330))

    mpg_inst_norm = info_font.render('MPG ' + str(inst_mpg), True, (255, 255, 255))
    screen.blit(mpg_inst_norm, (775, 370))

    mpg_avg_norm = info_font.render('MPG (Avg) ' + str(avg_mpg), True, (255, 255, 255))
    screen.blit(mpg_avg_norm, (775, 410))

#sport display information
def display_more_info_sport():
    info_font = pygame.font.Font('Fonts/pirulen rg.ttf', 25)

    maf_sport = info_font.render('MAF ' + str(maf_reading) +' g/s', True, (255, 255, 255))
    screen.blit(maf_sport, (755, 150))

    throttle_sport = info_font.render('Throttle ' + str(throttle_position) + '%', True, (255, 255, 255))
    screen.blit(throttle_sport, (755, 190))

    load_sport = info_font.render('Load ' + str(load) + '%', True, (255, 255, 255))
    screen.blit(load_sport, (755, 230))

    speed_sport = info_font.render('Speed ' + str(speed_value) + ' MPH', True, (255, 255, 255))
    screen.blit(speed_sport, (745, 380))

#temperature guages
temp_indicator_img = pygame.image.load('temp_gauge/indicator.png')
temp_gauge_img = pygame.image.load('temp_gauge/Temp Gauge.png')
temp_indicatorX = 140  #135 = middle, 240 = max, 30 = min
temp_indicatorY = 399
temp_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)
stemp_font = pygame.font.Font('Fonts/pirulen rg.ttf', 20)

temp_txt_X = 30
temp_txt_Y = 420

#Intake Temp Gauge
def intake_temp_gauge():
    intake_icon_img = pygame.image.load('temp_gauge/oil_white.png')
    temp_intake = stemp_font.render(('Intake Temp ' + str(intake_temp) + ' °F'), True, (255, 255, 255))
    screen.blit(temp_intake, (temp_txt_X , 245))

    screen.blit(temp_gauge_img, (19, 220))

    if intake_temp >= 180 and intake_temp <= 220:
        screen.blit(temp_indicator_img, (temp_indicatorX, 220))
    elif intake_temp >= 170 and intake_temp < 180:
        screen.blit(temp_indicator_img, (temp_indicatorX - 10, 220))
    elif intake_temp >= 100 and intake_temp < 170:
        screen.blit(temp_indicator_img, (temp_indicatorX - 50, 220))
    elif intake_temp >= 0 and intake_temp < 100:
        screen.blit(temp_indicator_img, (temp_indicatorX - 105, 220))
    elif intake_temp > 220 and intake_temp <= 250:
        screen.blit(temp_indicator_img, (temp_indicatorX + 10, 220))
    elif intake_temp > 250 and intake_temp <= 300:
        screen.blit(temp_indicator_img, (temp_indicatorX + 70, 220))
    elif intake_temp > 300:
        screen.blit(temp_indicator_img, (temp_indicatorX + 95, 220))

    pressure_fuel = stemp_font.render(('Fuel Pressure ' + str(fuel_pressure) + ' PSI'), True, (255, 255, 255))
    screen.blit(pressure_fuel, (temp_txt_X - 20, 185))

    screen.blit(intake_icon_img, (120, 145))

#Coolant Temp Gauge
def temp_gauge():

    if temp_value >= 200 and temp_value <= 220:
        screen.blit(temp_indicator_img, (temp_indicatorX, temp_indicatorY))
    elif temp_value >= 180 and temp_value < 200:
        screen.blit(temp_indicator_img, (temp_indicatorX - 10, temp_indicatorY))
    elif temp_value >= 100 and temp_value < 180:
        screen.blit(temp_indicator_img, (temp_indicatorX - 50, temp_indicatorY))
    elif temp_value >= 0 and temp_value < 100:
        screen.blit(temp_indicator_img, (temp_indicatorX - 105, temp_indicatorY))
    elif temp_value > 195 and temp_value <= 225:
        screen.blit(temp_indicator_img, (temp_indicatorX + 10, temp_indicatorY))
    elif temp_value > 225 and temp_value <= 275:
        screen.blit(temp_indicator_img, (temp_indicatorX + 70, temp_indicatorY))
    elif temp_value > 275:
        screen.blit(temp_indicator_img, (temp_indicatorX + 95, temp_indicatorY))


def display_temp():
    temp = temp_font.render(('Coolant Temp ' + str(temp_value) + ' °F'), True, (255, 255, 255))

    screen.blit(temp, (temp_txt_X, temp_txt_Y))

def sdisplay_temp():
    temp = stemp_font.render(('Coolant ' + str(temp_value) + ' °F'), True, (255, 255, 255))

    screen.blit(temp, (temp_txt_X-5, temp_txt_Y+5))

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

# Current interval text
interval_txt_X = 220
interval_txt_Y = 200
interval_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 40)

def interval_text(interval_string, maintenance_interval, offset):

    interval_message = interval_font.render(interval_string + str(maintenance_interval), True, (255, 255, 255))

    screen.blit(interval_message, (interval_txt_X + offset, interval_txt_Y))

# Oil change interval buttons
def three_thousand():
    if three_thousand_press is True:
        three_thousand_img = pygame.image.load('3000_P.png')
    else:
        three_thousand_img = pygame.image.load('3000_NP.png')
    screen.blit(three_thousand_img, (115, 260))

def five_thousand():
    if five_thousand_press is True:
        five_thousand_img = pygame.image.load('5000_P.png')
    else:
        five_thousand_img = pygame.image.load('5000_NP.png')
    screen.blit(five_thousand_img, (265, 260))

def seven_thousand_five():
    if seven_thousand_five_press is True:
        seven_thousand_five_img = pygame.image.load('7500_P.png')
    else:
        seven_thousand_five_img = pygame.image.load('7500_NP.png')
    screen.blit(seven_thousand_five_img, (415, 260))

def ten_thousand():
    if ten_thousand_press is True:
        ten_thousand_img = pygame.image.load('10000_P.png')
    else:
        ten_thousand_img = pygame.image.load('10000_NP.png')
    screen.blit(ten_thousand_img, (565, 260))

def fifteen_thousand():
    if fifteen_thousand_press is True:
        fifteen_thousand_img = pygame.image.load('15000_P.png')
    else:
        fifteen_thousand_img = pygame.image.load('15000_NP.png')
    screen.blit(fifteen_thousand_img, (715, 260))

def increment():
    if increment_press is True:
        increment_img = pygame.image.load('Plus Button Pressed.png')
    else:
        increment_img = pygame.image.load('Plus Button Not Pressed.png')
    screen.blit(increment_img, (600, 260))

def decrement():
    if decrement_press is True:
        decrement_img = pygame.image.load('Subtract Button Pressed.png')
    else:
        decrement_img = pygame.image.load('Subtract button Not pressed.png')
    screen.blit(decrement_img, (250, 260))

# Maintenance Display

#File Objects and Maintenance and Mileage Tracking
with open('maintenance/interval.txt', 'r+') as int_file:
    oil_change_string = int_file.readline()
    oil_change_interval = int(oil_change_string)

with open('maintenance/transmission_interval.txt', 'r+') as int_file:
    transmission_change_string = int_file.readline()
    transmission_oil_change_interval = int(transmission_change_string)

with open('maintenance/brake_interval.txt', 'r+') as int_file:
    brake_change_string = int_file.readline()
    brake_change_interval = int(brake_change_string)

with open('maintenance/mileage.txt', 'r+') as mileage_file:
    oil_mileage_string = mileage_file.readline()
    oil_mileage = int(oil_mileage_string)

with open('maintenance/transmission_mileage.txt', 'r+') as mileage_file:
    transmission_mileage_string = mileage_file.readline()
    transmission_oil_mileage = int(transmission_mileage_string)

with open('maintenance/brake_mileage.txt', 'r+') as mileage_file:
    brake_mileage_string = mileage_file.readline()
    brake_mileage = int(brake_mileage_string)

def maintenance_counter(mileage, interval):
    maintenance_count = interval - mileage
    return maintenance_count

oil_change_count = maintenance_counter(oil_mileage, oil_change_interval)
transmission_oil_change_count = maintenance_counter(transmission_oil_mileage, transmission_oil_change_interval)
brake_change_count = maintenance_counter(brake_mileage, brake_change_interval)

def display_maintenance_distance(maintenance_string, past_due_string, maintenance_count, offset, offset_due):

    maintenance_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 40)
    txt_X = 255
    txt_Y = 330

    if maintenance_count > 0:
        maintenance_change = maintenance_font.render((maintenance_string + str(maintenance_count) + ' Miles'), True, (255, 255, 255))
        screen.blit(maintenance_change, (txt_X + offset, txt_Y))
    elif maintenance_count < 0:
        maintenance_past_due = maintenance_font.render((past_due_string + str(maintenance_count * -1) + ' Miles'), True, (255, 255, 255))
        screen.blit(maintenance_past_due, (txt_X + offset_due, txt_Y))


#Warning Indicator

def display_warning_indicator(maintenance_count, maintenance_page):
    warning_big_img = pygame.image.load('maintenance/warning_big.png')
    brake_img = pygame.image.load('maintenance/brake.png')
    transmission_img = pygame.image.load('maintenance/gearbox.png')
    oil_img = pygame.image.load('maintenance/oil_white_big.png')

    warning_bigX = 470
    warning_bigY = 235

    if maintenance_count < 500:
        screen.blit(warning_big_img, (warning_bigX, warning_bigY))
    else:
        if maintenance_page == 1:
            screen.blit(oil_img, (warning_bigX - 20, warning_bigY))
        elif maintenance_page == 2:
            screen.blit(transmission_img, (warning_bigX, warning_bigY - 15))
        elif maintenance_page ==3:
            screen.blit(brake_img, (warning_bigX, warning_bigY - 15))


#Main Page Maintenance Indicators

warning_small_img = pygame.image.load('maintenance/warning_small.png')
everything_ok_img = pygame.image.load('maintenance/maintenance ok.png')

def display_warning_indicator_small(oil_change_count, transmission_change_count, brake_change_count):

    warning_smallX = 120
    warning_smallY = 230

    maintenance_txt_X = 45
    maintenance_txt_Y = 175

    if oil_change_count < 500 or transmission_change_count < 500 or brake_change_count < 500:
        screen.blit(warning_small_img, (warning_smallX, warning_smallY))
        maintenance_change_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 25)
        maintenance_line1 = maintenance_change_font.render(('Maintenance Due'), True, (255, 255, 255))
        screen.blit(maintenance_line1, (maintenance_txt_X, maintenance_txt_Y))
    else:
        screen.blit(everything_ok_img, (15, 200))


#Maintenance Headings
vehicle_maint_heading_img = pygame.image.load('maintenance/maintenance_heading.png')
maint_headingX = 210
maint_headingY = 65
next_maintenance = pygame.image.load('next.png')
previous_maintenance = pygame.image.load('back.png')

oil_change_int_heading_img = pygame.image.load('maintenance/oil_change_interval_heading.png')
transmission_oil_change_int_heading_img = pygame.image.load('maintenance/transmission_interval_heading.png')
brake_change_int_heading_img = pygame.image.load('maintenance/brake_interval_heading.png')

def display_maint_heading():
    screen.blit(vehicle_maint_heading_img, (maint_headingX, maint_headingY))
    screen.blit(next_maintenance, (765, 75))
    screen.blit(previous_maintenance, (210, 75))

def display_int_heading(maintenance_heading_img):
    screen.blit(maintenance_heading_img, (maint_headingX, maint_headingY))


#Diagnostic Display
diag_heading_img = pygame.image.load('diagnostics/vehicle_diagnostics_heading.png')

def display_diag_heading():
    screen.blit(diag_heading_img, (maint_headingX, maint_headingY))

# Diagnostics Display
clear_dtc_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 20)
clear_dtc_button_label = clear_dtc_font.render('Clear DTC', True, (255, 255, 255))

def clear_dtc_button():
    if clear_dtc_press is False:
        clear_dtc = pygame.image.load('Sport Button not pressed (no label).png')
    else:
        clear_dtc = pygame.image.load('Sport Button Pressed (no label).png')
    screen.blit(clear_dtc, (840, 425))
    screen.blit(clear_dtc_button_label, (888, 500))


diagnostic_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 30)
no_error_msg = diagnostic_font.render('No DTC Codes Detected', True, (255, 255, 255))
no_error_symbol = pygame.image.load('car.png')

error_symbol_small = pygame.image.load('engine_check_small.png')
error_symbol = pygame.image.load('engine_check.png')


#Display functions for UI
def displays():
    sports_button()
    display_blank_tach()
    display_needle(needle_positioning())
    display_inner_tach()
    framework()
    temp_gauge()
    display_temp()
    display_warning_indicator_small(oil_change_count, transmission_oil_change_count, brake_change_count)
    display_speed()
    display_more_info()
    display_logos()

def sports_display():
    display_blank_sports_tach()
    display_needle(needle_positioning())
    display_inner_tach()
    sports_button()
    sframework()
    sdisplay_rpm()
    temp_gauge()
    sdisplay_temp()
    display_more_info_sport()
    intake_temp_gauge()
    display_logos()

def maintenance_display():
    reset_button()
    interval_button()
    back_button()
    display_maint_heading()
    # Changes maintenance information
    if current_maintenance == 1:
        display_maintenance_distance('Oil Change Due In ', 'Oil Change Past Due by ', oil_change_count, 0, -50)
        display_warning_indicator(oil_change_count, 1)
    elif current_maintenance == 2:
        display_maintenance_distance('Transmission Oil Change Due In ', 'Transmission Oil Change Past Due by ', transmission_oil_change_count, -100, -150)
        display_warning_indicator(transmission_oil_change_count, 2)
    elif current_maintenance == 3:
        display_maintenance_distance('Brake Change Due In ', 'Brake Change Past Due by ', brake_change_count, -30, -60)
        display_warning_indicator(brake_change_count, 3)

def interval_display():
    if current_maintenance == 1:
        display_int_heading(oil_change_int_heading_img)
        three_thousand()
        five_thousand()
        seven_thousand_five()
        ten_thousand()
        fifteen_thousand()
        interval_text('Current Oil Change Interval: ', oil_change_interval, 0)
    elif current_maintenance == 2:
        increment()
        decrement()
        interval_text('Current Transmission Oil Change Interval: ', transmission_oil_change_interval, -100)
        display_int_heading(transmission_oil_change_int_heading_img)
    elif current_maintenance == 3:
        increment()
        decrement()
        interval_text('Current Brake Change Interval: ', brake_change_interval, -20)
        display_int_heading(brake_change_int_heading_img)
    #all pages
    back_button()

error_font = pygame.font.Font('Fonts/LeelUlsl.ttf', 20)

def diag_display():
    display_diag_heading()
    back_button()
    if current_page == 5:
        screen.blit(no_error_symbol, (435, 175))
        screen.blit(no_error_msg, (340, 300))

    elif current_page == 6:
        screen.blit(error_symbol_small, (465, 155))
        for i in dtc_code:
            error_label = error_font.render(dtc_code[i] + '\n', True, (255, 255, 255))
            screen.blit(error_label, (465, 200))
        clear_dtc_button()
    # else:
    #     screen.blit(error_symbol, (453, 160))

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
            interval_display()
        else:
            diag_display()

    pygame.display.update()
    
#OBD Callback Definitions
def get_rpm(rpmRaw):
    if not rpmRaw.is_null():
        global rpm_target
        rpm_target = int(rpmRaw.value.magnitude)

def get_speed(speedRaw):
    if not speedRaw.is_null():
        global speed_value
        speed_value = int(speedRaw.value.magnitude * 0.621371) #to MPH instead of KMH

def get_temp(tempRaw):
    if not tempRaw.is_null():
        global temp_value
        temp_value = int((tempRaw.value.magnitude * 1.8) + 32)

def get_throttle_position(throttlepositionRaw):
    if not throttlepositionRaw.is_null():
        global throttle_position
        throttle_position = int(throttlepositionRaw.value.magnitude)

def get_maf(mafRaw):
    if not mafRaw.is_null():
        global maf_reading
        maf_reading = int(mafRaw.value.magnitude)

def get_load(loadRaw):
    if not loadRaw.is_null():
        global load
        load = int(loadRaw.value.magnitude)

def get_fuel_pressure(fuelpressureRaw):
    if not fuelpressureRaw.is_null():
        global fuel_pressure
        fuel_pressure = int(fuelpressureRaw.value.magnitude * 0.14503)

def get_intake_temp(intaketempRaw):
    if not intaketempRaw.is_null():
        global intake_temp
        intake_temp = int((intaketempRaw.value.magnitude * 1.8) + 32)

def get_trip_distance(tripdistanceRaw):
    if not tripdistanceRaw.is_null():
        global trip_distance
        trip_distance = int(tripdistanceRaw.value.magnitude * 0.621371)

def get_dtc_codes(dtcRaw):
    global dtc_code
    dtc_code = dtcRaw.value
    if dtcRaw.value:
        dtc_code_present = True
    else:
        dtc_code_present = False
    print(dtcRaw.value)
        
#OBD Connection Callbacks
connection.watch(obd.commands.RPM, callback=get_rpm)
connection.watch(obd.commands.SPEED, callback=get_speed)
connection.watch(obd.commands.COOLANT_TEMP, callback=get_temp)
connection.watch(obd.commands.THROTTLE_POS, callback=get_throttle_position)
connection.watch(obd.commands.MAF, callback=get_maf)
connection.watch(obd.commands.ENGINE_LOAD, callback=get_load)
connection.watch(obd.commands.FUEL_PRESSURE, callback=get_fuel_pressure)
connection.watch(obd.commands.INTAKE_TEMP, callback=get_intake_temp)
connection.watch(obd.commands.DISTANCE_SINCE_DTC_CLEAR, callback=get_trip_distance)
connection.watch(obd.commands.GET_DTC, callback=get_dtc_codes)

connection.start()


#Game Loop
app_running = True
while app_running:
    clock.tick(60)

    #screen fill
    screen.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    #print(mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            connection.stop()
            connection.close()
            app_running = False

        # Checks for when we press the mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if the mouse click was where the button is
            # mouse[0] is the x coordinate, mouse[1] is the y
            if 90 < mouse[0] < 180 and 495 < mouse[1] < 585 and current_page < 3:
                sports_button_press = True
            elif 56 < mouse[0] < 146 and 471 < mouse[1] < 561 and current_page > 2:
                back_button_press = True
            elif 745 < mouse[0] < 835 and 471 < mouse[1] < 561 and current_page == 3:
                reset_button_press = True
            elif 870 < mouse[0] < 960 and 471 < mouse[1] < 561 and current_page == 3:
                interval_button_press = True
            elif current_maintenance == 1:
                if 160 < mouse[0] < 250 and 305 < mouse[1] < 395 and current_page == 4:
                    three_thousand_press = True
                elif 310 < mouse[0] < 400 and 305 < mouse[1] < 395 and current_page == 4:
                    five_thousand_press = True
                elif 460 < mouse[0] < 550 and 305 < mouse[1] < 395 and current_page == 4:
                    seven_thousand_five_press = True
                elif 610 < mouse[0] < 700 and 305 < mouse[1] < 395 and current_page == 4:
                    ten_thousand_press = True
                elif 760 < mouse[0] < 850 and 305 < mouse[1] < 395 and current_page == 4:
                    fifteen_thousand_press = True
            elif 885 < mouse[0] < 975 and 470 < mouse[1] < 560 and current_page == 6:
                clear_dtc_press = True
            elif 295 < mouse[0] < 385 and 305 < mouse[1] < 395 and current_page == 4:
                decrement_press = True
            elif 645 < mouse[0] < 735 and 305 < mouse[1] < 395 and current_page == 4:
                increment_press = True


        # Checks for when we let go of the mouse button
        if event.type == pygame.MOUSEBUTTONUP:
            interval_button_press = reset_button_press = diagnostic_press = maintenance_press = back_button_press = sports_button_press = False
            three_thousand_press = five_thousand_press = seven_thousand_five_press = ten_thousand_press = fifteen_thousand_press = False
            decrement_press = increment_press = False
            clear_dtc_press = False
            # current_page condition is used to prevent users from going to pages in the wrong order
            # ex. Going from maintenance to sports mode
            if 90 < mouse[0] < 180 and 495 < mouse[1] < 585 and current_page < 3:
                if current_page != 2:
                    current_page = 2
                else:
                    current_page = 1
            # Goes to vehicle maintenance
            elif 10 < mouse[0] < 270 and 130 < mouse[1] < 300 and current_page == 1:
                current_page = 3
            # Navigates through the different maintenances
            # Previous maintenance
            elif 210 < mouse[0] < 260 and 65 < mouse[1] < 135 and current_page == 3:
                if current_maintenance == 1:
                    current_maintenance = 3
                else:
                    current_maintenance -= 1
            # Next maintenance
            elif 765 < mouse[0] < 810 and 65 < mouse[1] < 135 and current_page == 3:
                if current_maintenance == 3:
                    current_maintenance = 1
                else:
                    current_maintenance += 1
            # Goes to vehicle diagnostics
            elif 754 < mouse[0] < 1016 and 130 < mouse[1] < 300 and current_page < 2:
                # Page 6 if there is an error
                if dtc_code_present is True:
                    current_page = 6
                else:
                    current_page = 5
            # Back button
            elif 56 < mouse[0] < 146 and 471 < mouse[1] < 561:
                if current_page == 3 or current_page == 5 or current_page == 6:
                    current_page = 1
                else:
                    current_page -= 1
            # Reset button
            elif 745 < mouse[0] < 835 and 471 < mouse[1] < 561 and current_page == 3:
                if current_maintenance == 1:
                    oil_mileage = 0
                elif current_maintenance == 2:
                    transmission_oil_mileage = 0
                elif current_maintenance == 3:
                    brake_mileage = 0
            # Interval button
            elif 870 < mouse[0] < 960 and 471 < mouse[1] < 561 and current_page == 3:
                current_page = 4
            if current_maintenance == 1 and current_page == 4:
                if 160 < mouse[0] < 250 and 305 < mouse[1] < 395:
                    oil_change_interval = 3000
                    with open('maintenance/interval.txt', 'w') as interval_file:
                        interval_file.write(str(oil_change_interval))
                elif 310 < mouse[0] < 400 and 305 < mouse[1] < 395:
                    oil_change_interval = 5000
                    with open('maintenance/interval.txt', 'w') as interval_file:
                        interval_file.write(str(oil_change_interval))
                elif 460 < mouse[0] < 550 and 305 < mouse[1] < 395:
                    oil_change_interval = 7500
                    with open('maintenance/interval.txt', 'w') as interval_file:
                        interval_file.write(str(oil_change_interval))
                elif 610 < mouse[0] < 700 and 305 < mouse[1] < 395:
                    oil_change_interval = 10000
                    with open('maintenance/interval.txt', 'w') as interval_file:
                        interval_file.write(str(oil_change_interval))
                elif 760 < mouse[0] < 850 and 305 < mouse[1] < 395:
                    oil_change_interval = 15000
                    with open('maintenance/interval.txt', 'w') as interval_file:
                        interval_file.write(str(oil_change_interval))
            elif current_maintenance == 2 and current_page == 4:
                if 295 < mouse[0] < 385 and 305 < mouse[1] < 395:
                    transmission_oil_change_interval = transmission_oil_change_interval - 500
                    print(transmission_oil_change_interval)
                    with open('maintenance/transmission_interval.txt', 'w') as interval_file:
                        interval_file.write(str(transmission_oil_change_interval))
                elif 645 < mouse[0] < 735 and 305 < mouse[1] < 395:
                    transmission_oil_change_interval = transmission_oil_change_interval + 500
                    print(transmission_oil_change_interval)
                    with open('maintenance/transmission_interval.txt', 'w') as interval_file:
                        interval_file.write(str(transmission_oil_change_interval))
            elif current_maintenance == 3 and current_page == 4:
                if 295 < mouse[0] < 385 and 305 < mouse[1] < 395:
                    brake_change_interval = brake_change_interval - 500
                    print(brake_change_interval)
                    with open('maintenance/brake_interval.txt', 'w') as interval_file:
                        interval_file.write(str(brake_change_interval))
                elif 645 < mouse[0] < 735 and 305 < mouse[1] < 395:
                    brake_change_interval = brake_change_interval + 500
                    print(brake_change_interval)
                    with open('maintenance/brake_interval.txt', 'w') as interval_file:
                        interval_file.write(str(brake_change_interval))
            elif current_page == 6:
                if 885 < mouse[0] < 975 and 470 < mouse[1] < 560:
                    obd.commands.CLEAR_DTC

#Mileage/Oil Change Interval Functions

    oil_change_count = maintenance_counter(oil_mileage, oil_change_interval)
    transmission_oil_change_count = maintenance_counter(transmission_oil_mileage, transmission_oil_change_interval)
    brake_change_count = maintenance_counter(brake_mileage, brake_change_interval)

    convert_oil_mileage = str(oil_mileage)
    convert_trans_oil_mileage = str(transmission_oil_mileage)
    convert_brake_mileage = str(brake_mileage)

    with open('maintenance/mileage.txt', 'w') as mileage_file:
        mileage_file.write(convert_oil_mileage)

    with open('maintenance/transmission_mileage.txt', 'w') as mileage_file:
        mileage_file.write(convert_trans_oil_mileage)

    with open('maintenance/brake_mileage.txt', 'w') as mileage_file:
        mileage_file.write(convert_brake_mileage)



#Redraw UI
    RedrawWindow()

#rpm needle smoothening
    if rpm < rpm_target_temp:
        rpm += 100
    elif rpm > rpm_target_temp:
        rpm -= 25
    elif rpm == rpm_target_temp:
        rpm == rpm_target

    endTime = time.time()

    if (endTime - startTime > .05):
        rpm_target_temp = rpm_target
        startTime = time.time()

#instant mpg
    if speed_value < 1:
        inst_mpg = 0
    elif speed_value >= 1 and maf_reading > 0.5:
        if ((710.7 + speed_value)/maf_reading) > 100:
            inst_mpg = 99
        else:
            inst_mpg = round((710.7 + speed_value)/maf_reading)
    else:
        inst_mpg = 0;

#average mpg
    
##
###speed testing
##    if speed_value < 175 and speed_limit == False:
##        speed_value += 1
##        if speed_value >= 175:
##            speed_limit = True
##    elif speed_limit == True:
##        speed_value -= 1
##        if speed_value <= 0:
##            speed_limit = False
##
###temp gauge testing
##    if temp_value < 310 and temp_limit == False:
##        temp_value += 1
##        if temp_value >= 310:
##            temp_value = True
##    elif temp_value == True:
##        temp_value -= 1
##        if temp_value <= 0:
##            temp_value = False

###rpm testing
##    if rpm < 9000 and limit == False:
##        rpm += 20
##        if rpm >= 9000:
##            limit = True
##    elif limit == True:
##        rpm -= 20
##        if rpm <= 0:
##            limit = False
##
###speed testing
##    if speed_value < 175 and speed_limit == False:
##        speed_value += 1
##        if speed_value >= 175:
##            speed_limit = True
##    elif speed_limit == True:
##        speed_value -= 1
##        if speed_value <= 0:
##            speed_limit = False
##
###temp gauge testing
##    if temp_value < 310 and temp_limit == False:
##        temp_value += 1
##        if temp_value >= 310:
##            temp_value = True
##    elif temp_value == True:
##        temp_value -= 1
##        if temp_value <= 0:
##            temp_value = False

#Where mileage should increment
    if trip_distance > prev_trip_distance + 1:
        oil_mileage = oil_mileage + 1
        transmission_oil_mileage = transmission_oil_mileage + 1
        brake_mileage = brake_mileage + 1
        prev_trip_distance = trip_distance
##    oil_mileage = oil_mileage + 1
##    transmission_oil_mileage = transmission_oil_mileage + 1
##    brake_mileage = brake_mileage + 1
