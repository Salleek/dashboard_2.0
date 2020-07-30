import pygame
import time

#globals
rpm = 0
oil_change_interval = 0
oil_change_count = 0
transmission_oil_change_interval = 0
brake_change_interval = 0
oil_mileage = 0
transmission_oil_mileage = 0
brake_mileage = 0
trip_distance = 0

avg_mpg = 0
inst_mpg = 0
maf_reading = 0
throttle_position = 0
load = 0
oil_pressure = 0
oil_temp = 0
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

# Creates dictionary for all rotation angles
rotational_angles = {}
rpms = range(9001)
for i in rpms:
    # 0-1000
    if i >= 0 and i <= 29:
        rotational_angles[i] = -1
    elif i > 29 and i <= 58:
        rotational_angles[i] = -2
    elif i > 58 and i <= 87:
        rotational_angles[i] = -3
    elif i > 87 and i <= 116:
        rotational_angles[i] = -4
    elif i > 116 and i <= 145:
        rotational_angles[i] = -5
    elif i > 145 and i <= 174:
        rotational_angles[i] = -6
    elif i > 174 and i <= 203:
        rotational_angles[i] = -7
    elif i > 203 and i <= 232:
        rotational_angles[i] = -8
    elif i > 232 and i <= 261:
        rotational_angles[i] = -9
    elif i > 261 and i <= 290:
        rotational_angles[i] = -10
    elif i > 290 and i <= 319:
        rotational_angles[i] = -11
    elif i > 319 and i <= 348:
        rotational_angles[i] = -12
    elif i > 348 and i <= 377:
        rotational_angles[i] = -13
    elif i > 377 and i <= 406:
        rotational_angles[i] = -14
    elif i > 406 and i <= 435:
        rotational_angles[i] = -15
    elif i > 435 and i <= 464:
        rotational_angles[i] = -16
    elif i > 464 and i <= 493:
        rotational_angles[i] = -17
    elif i > 493 and i <= 522:
        rotational_angles[i] = -18
    elif i > 522 and i <= 551:
        rotational_angles[i] = -19
    elif i > 551 and i <= 580:
        rotational_angles[i] = -20
    elif i > 580 and i <= 609:
        rotational_angles[i] = -21
    elif i > 609 and i <= 638:
        rotational_angles[i] = -22
    elif i > 638 and i <= 667:
        rotational_angles[i] = -23
    elif i > 667 and i <= 696:
        rotational_angles[i] = -24
    elif i > 696 and i <= 725:
        rotational_angles[i] = -25
    elif i > 725 and i <= 754:
        rotational_angles[i] = -26
    elif i > 754 and i <= 783:
        rotational_angles[i] = -27
    elif i > 783 and i <= 812:
        rotational_angles[i] = -28
    elif i > 812 and i <= 841:
        rotational_angles[i] = -29
    elif i > 841 and i <= 870:
        rotational_angles[i] = -30
    elif i > 870 and i <= 899:
        rotational_angles[i] = -31
    elif i > 899 and i <= 928:
        rotational_angles[i] = -32
    elif i > 928 and i <= 957:
        rotational_angles[i] = -33
    elif i > 957 and i <= 986:
        rotational_angles[i] = -34
    elif i > 986 and i <= 1000:
        rotational_angles[i] = -35

    #1000-2000
    elif i > 1000 and i <= 1031:
        rotational_angles[i] = -36
    elif i > 1031 and i <= 1061:
        rotational_angles[i] = -37
    elif i > 1061 and i <= 1093:
        rotational_angles[i] = -38
    elif i > 1093 and i <= 1124:
        rotational_angles[i] = -39
    elif i > 1124 and i <= 1155:
        rotational_angles[i] = -40
    elif i > 1155 and i <= 1186:
        rotational_angles[i] = -41
    elif i > 1186 and i <= 1217:
        rotational_angles[i] = -42
    elif i > 1217 and i <= 1248:
        rotational_angles[i] = -43
    elif i > 1248 and i <= 1279:
        rotational_angles[i] = -44
    elif i > 1279 and i <= 1310:
        rotational_angles[i] = -45
    elif i > 1310 and i <= 1341:
        rotational_angles[i] = -46
    elif i > 1341 and i <= 1372:
        rotational_angles[i] = -47
    elif i > 1372 and i <= 1403:
        rotational_angles[i] = -48
    elif i > 1403 and i <= 1434:
        rotational_angles[i] = -49
    elif i > 1434 and i <= 1465:
        rotational_angles[i] = -50
    elif i > 1465 and i <= 1496:
        rotational_angles[i] = -51
    elif i > 1496 and i <= 1527:
        rotational_angles[i] = -52
    elif i > 1527 and i <= 1558:
        rotational_angles[i] = -53
    elif i > 1558 and i <= 1589:
        rotational_angles[i] = -54
    elif i > 1589 and i <= 1620:
        rotational_angles[i] = -55
    elif i > 1620 and i <= 1651:
        rotational_angles[i] = -56
    elif i > 1651 and i <= 1682:
        rotational_angles[i] = -57
    elif i > 1682 and i <= 1713:
        rotational_angles[i] = -58
    elif i > 1713 and i <= 1744:
        rotational_angles[i] = -59
    elif i > 1744 and i <= 1775:
        rotational_angles[i] = -60
    elif i > 1775 and i <= 1806:
        rotational_angles[i] = -61
    elif i > 1806 and i <= 1837:
        rotational_angles[i] = -62
    elif i > 1837 and i <= 1868:
        rotational_angles[i] = -63
    elif i > 1868 and i <= 1899:
        rotational_angles[i] = -64
    elif i > 1899 and i <= 1930:
        rotational_angles[i] = -65
    elif i > 1930 and i <= 1961:
        rotational_angles[i] = -66
    elif i > 1961 and i <= 2000:
        rotational_angles[i] = -67

    #2000-3000
    elif i > 2000 and i <= 2031:
        rotational_angles[i] = -68
    elif i > 2031 and i <= 2061:
        rotational_angles[i] = -69
    elif i > 2061 and i <= 2093:
        rotational_angles[i] = -70
    elif i > 2093 and i <= 2124:
        rotational_angles[i] = -71
    elif i > 2124 and i <= 2155:
        rotational_angles[i] = -72
    elif i > 2155 and i <= 2186:
        rotational_angles[i] = -73
    elif i > 2186 and i <= 2217:
        rotational_angles[i] = -74
    elif i > 2217 and i <= 2248:
        rotational_angles[i] = -75
    elif i > 2248 and i <= 2279:
        rotational_angles[i] = -76
    elif i > 2279 and i <= 2310:
        rotational_angles[i] = -77
    elif i > 2310 and i <= 2341:
        rotational_angles[i] = -78
    elif i > 2341 and i <= 2372:
        rotational_angles[i] = -79
    elif i > 2372 and i <= 2403:
        rotational_angles[i] = -80
    elif i > 2403 and i <= 2434:
        rotational_angles[i] = -81
    elif i > 2434 and i <= 2465:
        rotational_angles[i] = -82
    elif i > 2465 and i <= 2496:
        rotational_angles[i] = -83
    elif i > 2496 and i <= 2527:
        rotational_angles[i] = -84
    elif i > 2527 and i <= 2558:
        rotational_angles[i] = -85
    elif i > 2558 and i <= 2589:
        rotational_angles[i] = -86
    elif i > 2589 and i <= 2620:
        rotational_angles[i] = -87
    elif i > 2620 and i <= 2651:
        rotational_angles[i] = -88
    elif i > 2651 and i <= 2682:
        rotational_angles[i] = -89
    elif i > 2682 and i <= 2713:
        rotational_angles[i] = -90
    elif i > 2713 and i <= 2744:
        rotational_angles[i] = -91
    elif i > 2744 and i <= 2775:
        rotational_angles[i] = -92
    elif i > 2775 and i <= 2806:
        rotational_angles[i] = -93
    elif i > 2806 and i <= 2837:
        rotational_angles[i] = -94
    elif i > 2837 and i <= 2868:
        rotational_angles[i] = -95
    elif i > 2868 and i <= 2899:
        rotational_angles[i] = -96
    elif i > 2899 and i <= 2930:
        rotational_angles[i] = -97
    elif i > 2930 and i <= 2961:
        rotational_angles[i] = -98
    elif i > 2961 and i <= 2992:
        rotational_angles[i] = -99
    elif i > 2992 and i <= 3000:
        rotational_angles[i] = -100

    #3000-4000
    elif i > 3000 and i <= 3029:
        rotational_angles[i] = -101
    elif i > 3029 and i <= 3058:
        rotational_angles[i] = -102
    elif i > 3058 and i <= 3087:
        rotational_angles[i] = -103
    elif i > 3087 and i <= 3116:
        rotational_angles[i] = -104
    elif i > 3116 and i <= 3145:
        rotational_angles[i] = -105
    elif i > 3145 and i <= 3174:
        rotational_angles[i] = -106
    elif i > 3174 and i <= 3203:
        rotational_angles[i] = -107
    elif i > 3203 and i <= 3232:
        rotational_angles[i] = -108
    elif i > 3232 and i <= 3261:
        rotational_angles[i] = -109
    elif i > 3261 and i <= 3290:
        rotational_angles[i] = -110
    elif i > 3290 and i <= 3319:
        rotational_angles[i] = -111
    elif i > 3319 and i <= 3348:
        rotational_angles[i] = -112
    elif i > 3348 and i <= 3377:
        rotational_angles[i] = -113
    elif i > 3377 and i <= 3406:
        rotational_angles[i] = -114
    elif i > 3406 and i <= 3435:
        rotational_angles[i] = -115
    elif i > 3435 and i <= 3464:
        rotational_angles[i] = -116
    elif i > 3464 and i <= 3493:
        rotational_angles[i] = -117
    elif i > 3493 and i <= 3522:
        rotational_angles[i] = -118
    elif i > 3522 and i <= 3551:
        rotational_angles[i] = -119
    elif i > 3551 and i <= 3580:
        rotational_angles[i] = -120
    elif i > 3580 and i <= 3609:
        rotational_angles[i] = -121
    elif i > 3609 and i <= 3638:
        rotational_angles[i] = -122
    elif i > 3638 and i <= 3667:
        rotational_angles[i] = -123
    elif i > 3667 and i <= 3696:
        rotational_angles[i] = -124
    elif i > 3696 and i <= 3725:
        rotational_angles[i] = -125
    elif i > 3725 and i <= 3754:
        rotational_angles[i] = -126
    elif i > 3754 and i <= 3783:
        rotational_angles[i] = -127
    elif i > 3783 and i <= 3812:
        rotational_angles[i] = -128
    elif i > 3812 and i <= 3841:
        rotational_angles[i] = -129
    elif i > 3841 and i <= 3870:
        rotational_angles[i] = -130
    elif i > 3870 and i <= 3899:
        rotational_angles[i] = -131
    elif i > 3899 and i <= 3928:
        rotational_angles[i] = -132
    elif i > 3928 and i <= 3957:
        rotational_angles[i] = -133
    elif i > 3957 and i <= 3986:
        rotational_angles[i] = -134
    elif i > 3986 and i <= 4000:
        rotational_angles[i] = -135

    #4000-5000
    elif i > 4000 and i <= 4029:
        rotational_angles[i] = -136
    elif i > 4029 and i <= 4058:
        rotational_angles[i] = -137
    elif i > 4058 and i <= 4087:
        rotational_angles[i] = -138
    elif i > 4087 and i <= 4116:
        rotational_angles[i] = -139
    elif i > 4116 and i <= 4145:
        rotational_angles[i] = -140
    elif i > 4145 and i <= 4174:
        rotational_angles[i] = -141
    elif i > 4174 and i <= 4203:
        rotational_angles[i] = -142
    elif i > 4203 and i <= 4232:
        rotational_angles[i] = -143
    elif i > 4232 and i <= 4261:
        rotational_angles[i] = -144
    elif i > 4261 and i <= 4290:
        rotational_angles[i] = -145
    elif i > 4290 and i <= 4319:
        rotational_angles[i] = -146
    elif i > 4319 and i <= 4348:
        rotational_angles[i] = -147
    elif i > 4348 and i <= 4377:
        rotational_angles[i] = -148
    elif i > 4377 and i <= 4406:
        rotational_angles[i] = -149
    elif i > 4406 and i <= 4435:
        rotational_angles[i] = -150
    elif i > 4435 and i <= 4464:
        rotational_angles[i] = -151
    elif i > 4464 and i <= 4493:
        rotational_angles[i] = -152
    elif i > 4493 and i <= 4522:
        rotational_angles[i] = -153
    elif i > 4522 and i <= 4551:
        rotational_angles[i] = -154
    elif i > 4551 and i <= 4580:
        rotational_angles[i] = -155
    elif i > 4580 and i <= 4609:
        rotational_angles[i] = -156
    elif i > 4609 and i <= 4638:
        rotational_angles[i] = -157
    elif i > 4638 and i <= 4667:
        rotational_angles[i] = -158
    elif i > 4667 and i <= 4696:
        rotational_angles[i] = -159
    elif i > 4696 and i <= 4725:
        rotational_angles[i] = -160
    elif i > 4725 and i <= 4754:
        rotational_angles[i] = -161
    elif i > 4754 and i <= 4783:
        rotational_angles[i] = -162
    elif i > 4783 and i <= 4812:
        rotational_angles[i] = -163
    elif i > 4812 and i <= 4841:
        rotational_angles[i] = -164
    elif i > 4841 and i <= 4870:
        rotational_angles[i] = -165
    elif i > 4870 and i <= 4899:
        rotational_angles[i] = -166
    elif i > 4899 and i <= 4928:
        rotational_angles[i] = -167
    elif i > 4928 and i <= 4957:
        rotational_angles[i] = -168
    elif i > 4957 and i <= 4986:
        rotational_angles[i] = -169
    elif i > 4986 and i <= 5000:
        rotational_angles[i] = -170

    #5000-6000
    elif i > 5000 and i <= 5029:
        rotational_angles[i] = -171
    elif i > 5029 and i <= 5058:
        rotational_angles[i] = -172
    elif i > 5058 and i <= 5087:
        rotational_angles[i] = -173
    elif i > 5087 and i <= 5116:
        rotational_angles[i] = -174
    elif i > 5116 and i <= 5145:
        rotational_angles[i] = -175
    elif i > 5145 and i <= 5174:
        rotational_angles[i] = -176
    elif i > 5174 and i <= 5203:
        rotational_angles[i] = -177
    elif i > 5203 and i <= 5232:
        rotational_angles[i] = -178
    elif i > 5232 and i <= 5261:
        rotational_angles[i] = -179
    elif i > 5261 and i <= 5290:
        rotational_angles[i] = -180
    elif i > 5290 and i <= 5319:
        rotational_angles[i] = -181
    elif i > 5319 and i <= 5348:
        rotational_angles[i] = -182
    elif i > 5348 and i <= 5377:
        rotational_angles[i] = -183
    elif i > 5377 and i <= 5406:
        rotational_angles[i] = -184
    elif i > 5406 and i <= 5435:
        rotational_angles[i] = -185
    elif i > 5435 and i <= 5464:
        rotational_angles[i] = -186
    elif i > 5464 and i <= 5493:
        rotational_angles[i] = -187
    elif i > 5493 and i <= 5522:
        rotational_angles[i] = -188
    elif i > 5522 and i <= 5551:
        rotational_angles[i] = -189
    elif i > 5551 and i <= 5580:
        rotational_angles[i] = -190
    elif i > 5580 and i <= 5609:
        rotational_angles[i] = -191
    elif i > 5609 and i <= 5638:
        rotational_angles[i] = -192
    elif i > 5638 and i <= 5667:
        rotational_angles[i] = -193
    elif i > 5667 and i <= 5696:
        rotational_angles[i] = -194
    elif i > 5696 and i <= 5725:
        rotational_angles[i] = -195
    elif i > 5725 and i <= 5754:
        rotational_angles[i] = -196
    elif i > 5754 and i <= 5783:
        rotational_angles[i] = -197
    elif i > 5783 and i <= 5812:
        rotational_angles[i] = -198
    elif i > 5812 and i <= 5841:
        rotational_angles[i] = -199
    elif i > 5841 and i <= 5870:
        rotational_angles[i] = -200
    elif i > 5870 and i <= 5899:
        rotational_angles[i] = -201
    elif i > 5899 and i <= 5928:
        rotational_angles[i] = -202
    elif i > 5928 and i <= 5957:
        rotational_angles[i] = -203
    elif i > 5957 and i <= 5986:
        rotational_angles[i] = -204
    elif i > 5986 and i <= 6000:
        rotational_angles[i] = -205

    # 6000-7000
    elif i > 6000 and i <= 6029:
        rotational_angles[i] = -206
    elif i > 6029 and i <= 6058:
        rotational_angles[i] = -207
    elif i > 6058 and i <= 6087:
        rotational_angles[i] = -208
    elif i > 6087 and i <= 6116:
        rotational_angles[i] = -209
    elif i > 6116 and i <= 6145:
        rotational_angles[i] = -210
    elif i > 6145 and i <= 6174:
        rotational_angles[i] = -211
    elif i > 6174 and i <= 6203:
        rotational_angles[i] = -212
    elif i > 6203 and i <= 6232:
        rotational_angles[i] = -213
    elif i > 6232 and i <= 6261:
        rotational_angles[i] = -214
    elif i > 6261 and i <= 6290:
        rotational_angles[i] = -215
    elif i > 6290 and i <= 6319:
        rotational_angles[i] = -216
    elif i > 6319 and i <= 6348:
        rotational_angles[i] = -217
    elif i > 6348 and i <= 6377:
        rotational_angles[i] = -218
    elif i > 6377 and i <= 6406:
        rotational_angles[i] = -219
    elif i > 6406 and i <= 6435:
        rotational_angles[i] = -220
    elif i > 6435 and i <= 6464:
        rotational_angles[i] = -221
    elif i > 6464 and i <= 6493:
        rotational_angles[i] = -222
    elif i > 6493 and i <= 6522:
        rotational_angles[i] = -223
    elif i > 6522 and i <= 6551:
        rotational_angles[i] = -224
    elif i > 6551 and i <= 6580:
        rotational_angles[i] = -225
    elif i > 6580 and i <= 6609:
        rotational_angles[i] = -226
    elif i > 6609 and i <= 6638:
        rotational_angles[i] = -227
    elif i > 6638 and i <= 6667:
        rotational_angles[i] = -228
    elif i > 6667 and i <= 6696:
        rotational_angles[i] = -229
    elif i > 6696 and i <= 6725:
        rotational_angles[i] = -230
    elif i > 6725 and i <= 6754:
        rotational_angles[i] = -231
    elif i > 6754 and i <= 6783:
        rotational_angles[i] = -232
    elif i > 6783 and i <= 6812:
        rotational_angles[i] = -233
    elif i > 6812 and i <= 6841:
        rotational_angles[i] = -234
    elif i > 6841 and i <= 6870:
        rotational_angles[i] = -235
    elif i > 6870 and i <= 6899:
        rotational_angles[i] = -236
    elif i > 6899 and i <= 6928:
        rotational_angles[i] = -237
    elif i > 6928 and i <= 6957:
        rotational_angles[i] = -238
    elif i > 6957 and i <= 6986:
        rotational_angles[i] = -239
    elif i > 6986 and i <= 7000:
        rotational_angles[i] = -240

    # 7000-8000
    elif i > 7000 and i <= 7029:
        rotational_angles[i] = -241
    elif i > 7029 and i <= 7058:
        rotational_angles[i] = -242
    elif i > 7058 and i <= 7087:
        rotational_angles[i] = -243
    elif i > 7087 and i <= 7116:
        rotational_angles[i] = -244
    elif i > 7116 and i <= 7145:
        rotational_angles[i] = -245
    elif i > 7145 and i <= 7174:
        rotational_angles[i] = -246
    elif i > 7174 and i <= 7203:
        rotational_angles[i] = -247
    elif i > 7203 and i <= 7232:
        rotational_angles[i] = -248
    elif i > 7232 and i <= 7261:
        rotational_angles[i] = -249
    elif i > 7261 and i <= 7290:
        rotational_angles[i] = -250
    elif i > 7290 and i <= 7319:
        rotational_angles[i] = -251
    elif i > 7319 and i <= 7348:
        rotational_angles[i] = -252
    elif i > 7348 and i <= 7377:
        rotational_angles[i] = -253
    elif i > 7377 and i <= 7406:
        rotational_angles[i] = -254
    elif i > 7406 and i <= 7435:
        rotational_angles[i] = -255
    elif i > 7435 and i <= 7464:
        rotational_angles[i] = -256
    elif i > 7464 and i <= 7493:
        rotational_angles[i] = -257
    elif i > 7493 and i <= 7522:
        rotational_angles[i] = -258
    elif i > 7522 and i <= 7551:
        rotational_angles[i] = -259
    elif i > 7551 and i <= 7580:
        rotational_angles[i] = -260
    elif i > 7580 and i <= 7609:
        rotational_angles[i] = -261
    elif i > 7609 and i <= 7638:
        rotational_angles[i] = -262
    elif i > 7638 and i <= 7667:
        rotational_angles[i] = -263
    elif i > 7667 and i <= 7696:
        rotational_angles[i] = -264
    elif i > 7696 and i <= 7725:
        rotational_angles[i] = -265
    elif i > 7725 and i <= 7754:
        rotational_angles[i] = -266
    elif i > 7754 and i <= 7783:
        rotational_angles[i] = -267
    elif i > 7783 and i <= 7812:
        rotational_angles[i] = -268
    elif i > 7812 and i <= 7841:
        rotational_angles[i] = -269
    elif i > 7841 and i <= 7870:
        rotational_angles[i] = -270
    elif i > 7870 and i <= 7899:
        rotational_angles[i] = -271
    elif i > 7899 and i <= 7928:
        rotational_angles[i] = -272
    elif i > 7928 and i <= 7957:
        rotational_angles[i] = -273
    elif i > 7957 and i <= 7986:
        rotational_angles[i] = -274
    elif i > 7986 and i <= 8000:
        rotational_angles[i] = -275

    # 8000-9000
    elif i > 8000 and i <= 8031:
        rotational_angles[i] = -276
    elif i > 8031 and i <= 8061:
        rotational_angles[i] = -277
    elif i > 8061 and i <= 8093:
        rotational_angles[i] = -278
    elif i > 8093 and i <= 8124:
        rotational_angles[i] = -279
    elif i > 8124 and i <= 8155:
        rotational_angles[i] = -280
    elif i > 8155 and i <= 8186:
        rotational_angles[i] = -281
    elif i > 8186 and i <= 8217:
        rotational_angles[i] = -282
    elif i > 8217 and i <= 8248:
        rotational_angles[i] = -283
    elif i > 8248 and i <= 8279:
        rotational_angles[i] = -284
    elif i > 8279 and i <= 8310:
        rotational_angles[i] = -285
    elif i > 8310 and i <= 8341:
        rotational_angles[i] = -286
    elif i > 8341 and i <= 8372:
        rotational_angles[i] = -287
    elif i > 8372 and i <= 8403:
        rotational_angles[i] = -288
    elif i > 8403 and i <= 8434:
        rotational_angles[i] = -289
    elif i > 8434 and i <= 8465:
        rotational_angles[i] = -290
    elif i > 8465 and i <= 8496:
        rotational_angles[i] = -291
    elif i > 8496 and i <= 8527:
        rotational_angles[i] = -292
    elif i > 8527 and i <= 8558:
        rotational_angles[i] = -293
    elif i > 8558 and i <= 8589:
        rotational_angles[i] = -294
    elif i > 8589 and i <= 8620:
        rotational_angles[i] = -295
    elif i > 8620 and i <= 8651:
        rotational_angles[i] = -296
    elif i > 8651 and i <= 8682:
        rotational_angles[i] = -297
    elif i > 8682 and i <= 8713:
        rotational_angles[i] = -298
    elif i > 8713 and i <= 8744:
        rotational_angles[i] = -299
    elif i > 8744 and i <= 8775:
        rotational_angles[i] = -300
    elif i > 8775 and i <= 8806:
        rotational_angles[i] = -301
    elif i > 8806 and i <= 8837:
        rotational_angles[i] = -302
    elif i > 8837 and i <= 8868:
        rotational_angles[i] = -303
    elif i > 8868 and i <= 8899:
        rotational_angles[i] = -304
    elif i > 8899 and i <= 8930:
        rotational_angles[i] = -305
    elif i > 8930 and i <= 8961:
        rotational_angles[i] = -306
    elif i > 8961 and i <= 9000:
        rotational_angles[i] = -307

#initialize the interface
pygame.init()

#clock
clock = pygame.time.Clock()

#create screen
screen = pygame.display.set_mode((1024, 600))

#Title of app
pygame.display.set_caption("Dashboard 2.0")

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

def display_needle(rpm):
    mx, my = pygame.mouse.get_pos()
    angle = rotational_angles.get(rpm)
    img_copy = pygame.transform.rotate(needle_img, angle)
    screen.blit(img_copy, (515 - int(img_copy.get_width() / 2), int(305 - img_copy.get_height() /2)))

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
    srpm = rpm_font.render(str(rpm), True, (255, 255, 255))
    rpm_text = srpmfont.render("RPM", True, (255, 255, 255))

    if rpm <= 9:
        screen.blit(srpm, (speedtextX0, speedtextY0+15))
    elif rpm >= 10 and rpm <= 99:
        screen.blit(srpm, (speedtextX10-5, speedtextY10+15))
    elif rpm >= 100 and rpm <= 999:
        screen.blit(srpm, (speedtextX10 - 15, speedtextY10 + 15))
    elif rpm >= 1000 and rpm <= 1999:
        screen.blit(srpm, (speedtextX10 - 22, speedtextY10 + 15))
    elif rpm >= 2000:
        screen.blit(srpm, (speedtextX100-25, speedtextY100+15))

    screen.blit(rpm_text, (mphtextX-10, mphtextY-10))

#main display information
def display_more_info():
    info_font = pygame.font.Font('Fonts/LeelUIsl.ttf', 30)

    rpm_norm = info_font.render('Tach ' + str(rpm) + ' RPM', True, (255, 255, 255))
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

#Oil Temp Gauge
def oil_temp_gauge():

    oil_icon_img = pygame.image.load('temp_gauge/oil_white.png')

    temp_oil = stemp_font.render(('Oil Temp ' + str(oil_temp) + ' °F'), True, (255, 255, 255))
    screen.blit(temp_oil, (temp_txt_X , 245))

    screen.blit(temp_gauge_img, (19, 220))

    if oil_temp >= 180 and oil_temp <= 220:
        screen.blit(temp_indicator_img, (temp_indicatorX, 220))
    elif oil_temp >= 170 and oil_temp < 180:
        screen.blit(temp_indicator_img, (temp_indicatorX - 10, 220))
    elif oil_temp >= 100 and oil_temp < 170:
        screen.blit(temp_indicator_img, (temp_indicatorX - 50, 220))
    elif oil_temp >= 0 and oil_temp < 100:
        screen.blit(temp_indicator_img, (temp_indicatorX - 105, 220))
    elif oil_temp > 220 and oil_temp <= 250:
        screen.blit(temp_indicator_img, (temp_indicatorX + 10, 220))
    elif oil_temp > 250 and oil_temp <= 300:
        screen.blit(temp_indicator_img, (temp_indicatorX + 70, 220))
    elif oil_temp > 300:
        screen.blit(temp_indicator_img, (temp_indicatorX + 95, 220))

    pressure_oil = stemp_font.render(('Oil Pressure ' + str(oil_pressure) + ' PSI'), True, (255, 255, 255))
    screen.blit(pressure_oil, (temp_txt_X - 20, 185))

    screen.blit(oil_icon_img, (120, 145))

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
    display_needle(rpm)
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
    display_needle(rpm)
    display_inner_tach()
    sports_button()
    sframework()
    sdisplay_rpm()
    temp_gauge()
    sdisplay_temp()
    display_more_info_sport()
    oil_temp_gauge()
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

def diag_display():
    display_diag_heading()
    back_button()
    if current_page == 5:
        screen.blit(no_error_symbol, (435, 175))
        screen.blit(no_error_msg, (340, 300))

    elif current_page == 6:
        screen.blit(error_symbol_small, (465, 155))
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
            if current_page < 3:
                if 90 < mouse[0] < 180 and 495 < mouse[1] < 585:
                    sports_button_press = True
            elif current_page >= 3:
                if 56 < mouse[0] < 146 and 471 < mouse[1] < 561:
                    back_button_press = True
            elif current_page == 3:
                if 745 < mouse[0] < 835 and 471 < mouse[1] < 561:
                    reset_button_press = True
                elif 870 < mouse[0] < 960 and 471 < mouse[1] < 561:
                    interval_button_press = True
            elif current_page == 4:
                if current_maintenance == 1:
                    if 160 < mouse[0] < 250 and 305 < mouse[1] < 395:
                        three_thousand_press = True
                    elif 310 < mouse[0] < 400 and 305 < mouse[1] < 395:
                        five_thousand_press = True
                    elif 460 < mouse[0] < 550 and 305 < mouse[1] < 395:
                        seven_thousand_five_press = True
                    elif 610 < mouse[0] < 700 and 305 < mouse[1] < 395:
                        ten_thousand_press = True
                    elif 760 < mouse[0] < 850 and 305 < mouse[1] < 395:
                        fifteen_thousand_press = True
                else:
                    if 295 < mouse[0] < 385 and 305 < mouse[1] < 395:
                        decrement_press = True
                    elif 645 < mouse[0] < 735 and 305 < mouse[1] < 395:
                        increment_press = True
            elif current_page == 6:
                if 885 < mouse[0] < 975 and 470 < mouse[1] < 560:
                    clear_dtc_press = True

        # Checks for when we let go of the mouse button
        if event.type == pygame.MOUSEBUTTONUP:
            interval_button_press = reset_button_press = diagnostic_press = maintenance_press = back_button_press = sports_button_press = False
            three_thousand_press = five_thousand_press = seven_thousand_five_press = ten_thousand_press = fifteen_thousand_press = False
            decrement_press = increment_press = False
            # current_page condition is used to prevent users from going to pages in the wrong order
            # ex. Going from maintenance to sports mode
            if current_page < 3:
                if current_page == 1:
                    # Goes to vehicle maintenance
                    if 10 < mouse[0] < 270 and 130 < mouse[1] < 300:
                        current_page = 3
                    # Sports mode button
                    elif 90 < mouse[0] < 180 and 495 < mouse[1] < 585:
                        current_page = 2
                    # Goes to vehicle diagnostics
                    elif 754 < mouse[0] < 1016 and 130 < mouse[1] < 300:
                    # Page 6 if there is an error
                        if dtc_code_present is True:
                            current_page = 6
                        else:
                            current_page = 5
                else:
                    if 90 < mouse[0] < 180 and 495 < mouse[1] < 585:
                        current_page = 1
            # Back button
            elif 56 < mouse[0] < 146 and 471 < mouse[1] < 561:
                if current_page == 3 or current_page == 5 or current_page == 6:
                    current_page = 1
                else:
                    current_page -= 1
            # Navigates through the different maintenances
            elif current_page == 3:
                # Previous maintenance
                if 210 < mouse[0] < 260 and 65 < mouse[1] < 135:
                    if current_maintenance == 1:
                        current_maintenance = 3
                    else:
                        current_maintenance -= 1
                # Next maintenance
                elif 765 < mouse[0] < 810 and 65 < mouse[1] < 135:
                    if current_maintenance == 3:
                        current_maintenance = 1
                    else:
                        current_maintenance += 1
                # Reset button
                elif 745 < mouse[0] < 835 and 471 < mouse[1] < 561:
                    if current_maintenance == 1:
                        oil_mileage = 0
                    elif current_maintenance == 2:
                        transmission_oil_mileage = 0
                    elif current_maintenance == 3:
                        brake_mileage = 0
                # Interval button
                elif 870 < mouse[0] < 960 and 471 < mouse[1] < 561:
                    current_page = 4

            elif current_page == 4:
                if current_maintenance == 1:
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
                elif current_maintenance == 2:
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
                elif current_maintenance == 3:
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

#rpm testing
    if rpm < 9000 and limit == False:
        rpm += 20
        if rpm >= 9000:
            limit = True
    elif limit == True:
        rpm -= 20
        if rpm <= 0:
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

#Where mileage should increment
    #oil_ = oil_mileage + trip_distance
    #transmission_oil_mileage = transmission_oil_mileage + trip_distance
    #brake_mileage = brake_mileage + trip_distance
    oil_mileage = oil_mileage + 1
    transmission_oil_mileage = transmission_oil_mileage + 1
    brake_mileage = brake_mileage + 1