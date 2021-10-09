default cardInput = 0
default rwd1Lock = 0
default rwd2Lock = 0
default rwd3Lock = 0


default cardSWTitle = False




default swCardClaimed = False
default secretCashCard = False
default purityClaimed = False
default mnt17 = False

default month1CardClaimed = False
default month2CardClaimed = False
default month3CardClaimed = False
default month4CardClaimed = False
default month5CardClaimed = False
default month6CardClaimed = False
default month7CardClaimed = False
default month8CardClaimed = False
default month9CardClaimed = False
default month10CardClaimed = False
default month11CardClaimed = False
default month12CardClaimed = False
default month13CardClaimed = False
default month14CardClaimed = False
default month15CardClaimed = False
default month16CardClaimed = False
default month17CardClaimed = False
default month18CardClaimed = False
default month19CardClaimed = False
default month20CardClaimed = False
default month21CardClaimed = False
default month22CardClaimed = False
default month23CardClaimed = False

image card1 = "gui/card1.png"
image card2 = "gui/card2.png"
image cardHalf1 = "gui/cardHalf1.png"
image cardHalf2 = "gui/cardHalf2.png"
image cardRewardBG = "gui/cardRewardBG.png"
image cardRewardTitle = "gui/cardRewardTitle.png"
image cardSmokeAni = "gui/cardSmoke.png"

style titleStyle is text:
    font "fonts/freshMarker.ttf"

screen cardClaim:
    vbox xalign 0.5 yalign 0.75:
        imagebutton:
            idle "gui/cardClaim.png"
            hover "gui/cardClaim-hover.png"
            action Play("sound", "audio/sfx/cardClaim.mp3"), Return()

label creditcards:
    "It's an ATM."

python:
    cardInput = renpy.input("Enter code...")


if cardInput == "64063" or cardInput == "65878" or cardInput == "58806":
    if month1CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "98459" or cardInput == "86221" or cardInput == "74891":
    if month2CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "66505" or cardInput == "19254" or cardInput == "99332":
    if month3CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "85765" or cardInput == "45691" or cardInput == "21315":
    if month4CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "39540" or cardInput == "42416" or cardInput == "67720":
    if month5CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "68151" or cardInput == "28307" or cardInput == "30357":
    if month6CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "70293" or cardInput == "20959" or cardInput == "26053":
    if month7CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "32996" or cardInput == "61392" or cardInput == "84598":
    if month8CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "55514" or cardInput == "92344" or cardInput == "80906":
    if month9CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "74854" or cardInput == "31009" or cardInput == "81131":
    if month10CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "32577" or cardInput == "98376" or cardInput == "71265":
    if month11CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "575745" or cardInput == "635929" or cardInput == "308694":
    if month12CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "50817" or cardInput == "93795" or cardInput == "69630":
    if month13CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "55166" or cardInput == "70473" or cardInput == "17449":
    if month14CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "69846" or cardInput == "22328" or cardInput == "61252":
    if month15CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "85747" or cardInput == "13633" or cardInput == "51890":
    if month16CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "71067" or cardInput == "79075" or cardInput == "85094":
    if month17CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "75705" or cardInput == "12197" or cardInput == "37067":
    if month18CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "71484" or cardInput == "35957" or cardInput == "72416":
    if month19CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "66559" or cardInput == "24715" or cardInput == "34524":
    if month20CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "74059" or cardInput == "95791" or cardInput == "60168":
    if month21CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "97030" or cardInput == "94788" or cardInput == "21751":
    if month22CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards

elif cardInput == "51760" or cardInput == "94117" or cardInput == "31723":
    if month23CardClaimed == True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
    elif True:
        jump monthlyRewards


elif cardInput == "11218":
    if swCardClaimed == False:
        jump monthlyRewards
    elif True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
elif cardInput == "19531852031545" or cardInput == "1953 1852 0315 45":
    if secretCashCard == False:
        jump monthlyRewards
    elif True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
elif cardInput == "26176":
    if purityClaimed == False:
        jump monthlyRewards
    elif True:
        "This reward has already been claimed."
        if tod == 1:
            jump worldmap
        if tod == 2:
            jump base
elif cardInput == "anitest":
    jump devAniTest
elif cardInput == "cheats":
    jump cheatMenu
elif cardInput == "tentacle":
    $ shrineRestored = 3
    "This code unlocks the tentacle scene picture.{w} Playing it now."
    jump atmTentacle
elif cardInput == "books":
    "This code unlocks the book clerk scene picture.{w} Playing it now."
    jump atmBooks
elif cardInput == "77889":
    jump monthlyRewards
elif cardInput == "28521" or cardInput == "280521":
    "Exiscoming" "Congratulations on beating the game! Remember this code because it can be used in my next game to score some secret items!"
    "Exiscoming" "Did you know that there was a code after the credits for Orange Trainer aswell? Try typing that one into the ATM next~..."
    if tod == 1:
        jump worldmap
    if tod == 2:
        jump base
elif True:


    "Unrecognised code."
    if tod == 1:
        jump worldmap
    if tod == 2:
        jump base

label monthlyRewards:
    show scene_fighting
    with d2
    play sound "audio/sfx/cardAudio2.mp3"
    show card1:
        xalign 0.5 yalign 0.5
    with d5
    pause 0.5
    show card1 at cardshake
    show card2 at cardshakeRed
    show cardSmokeAni at cardSmokeAni
    pause 3.8
    hide cardSmokeAni
    hide card1
    hide card2
    show white
    pause 0.1
    hide white
    show cardHalf1:
        xalign 0.5 yalign 0.5
    show cardHalf2:
        xalign 0.5 yalign 0.5
    show cardHalf1:
        linear 0.2 xalign 0.45 yalign 0.70 rotate -1
    show cardHalf2:
        linear 0.2 xalign 0.55 yalign 0.40 rotate 1
    pause 0.2
    play sound "audio/sfx/fanfare.mp3"
    hide cardHalf1
    hide cardHalf2
    with d5
    show cardRewardBG:
        xalign 0.5 yalign 0.5 zoom 1.0


    if cardInput == "11218":
        $ swCardClaimed = True
        image cardSWReward1 = "models/green/outfit/chest/top8.png"
        image cardSWReward2 = "models/green/outfit/bott/bott8.png"
        image cardSWReward3 = "models/green/hair/greenHair8.png"
        $ top8Sam = True
        $ bott8Sam = True
        $ hair8Sam = True
        $ cardSWTitle = True
        $ faceAcc8Sam = True
        show cardSWReward1:
            xalign 0.50 yalign -0.10
        with d2
        call screen cardClaim
        hide cardSWReward1
        show cardSWReward2:
            xalign 0.50 yalign 0.0 zoom 0.6
        with d2
        call screen cardClaim
        hide cardSWReward2
        show cardSWReward3:
            xalign 0.52 yalign -1.70
        with d2
        call screen cardClaim
        hide cardSWReward3
        show cardRewardTitle:
            xalign 0.5 yalign 0.43
        show text "{size=+40}{color=#000000}{font=fonts/freshmarker.ttf}Lowlife{/font}{/color}{/size}":
            xalign 0.5 yalign 0.53
        with d2
        call screen cardClaim
        hide scene_fighting
        hide cardRewardBG
        hide cardRewardTitle
        hide text
        with d3
        if tod == 1:
            jump worldmap
        elif tod == 2:
            jump base


    if cardInput == "26176":
        $ purityClaimed = True
        $ under6Sam = True
        image cardUnder6 = "models/green/outfit/under/under6.png"
        show cardUnder6:
            xalign 0.52 yalign -0.30
        with d2
        call screen cardClaim
        hide cardUnder6
        hide scene_fighting
        hide cardRewardBG
        with d3
        if tod == 1:
            jump worldmap
        elif tod == 2:
            jump base


    if cardInput == "19531852031545" or cardInput == "1953 1852 0315 45":
        $ secretCashCard = True
        $ cashBoost += 1
        image cardValuSecret = "gui/itemUI/items/itemMatsValu.png"
        show cardValuSecret:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardValuSecret
        hide scene_fighting
        hide cardRewardBG
        with d3
        if tod == 1:
            jump worldmap
        elif tod == 2:
            jump base


    if cardInput == "77889":

        $ top15Sam = True
        $ shoes15Sam = True
        $ faceAcc15Sam = True
        $ hatHall1Clover = True
        $ faceHall1Clover = True
        $ neckHall1Clover = True
        $ topHall1Clover = True
        $ wristHall1Clover = True
        $ bottHall1Clover = True
        $ shoesHall1Clover = True
        $ hat15Alex = True
        $ top15Alex = True
        $ bott15Alex = True
        $ shoes15Alex = True


        $ top14Alex = True
        $ shoes14Alex = True
        $ top14Sam = True
        $ bott14Sam = True
        $ shoes14Sam = True
        $ top14Clover = True
        $ bott14Clover = True
        $ shoes14Clover = True
        $ hat14Clover = True

        $ mnt17 = True
        $ top8Sam = True
        $ bott8Sam = True
        $ hair8Sam = True
        $ cardSWTitle = True
        $ faceAcc8Sam = True
        $ under6Sam = True
        $ top8Alex = True
        $ bott8Alex = True
        $ neck8Alex = True
        $ shoes8Alex = True
        $ wristAcc8Alex = True
        $ hat12Sam = True
        $ shoes12Sam = True
        $ top12Sam = True
        $ bott12Sam = True
        $ under2Sam = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True
        $ under7Clover = True
        $ hat1Sam = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True
        $ hat6Sam = True
        $ top6Sam = True
        $ shoes6Sam = True
        $ bott6Sam = True
        $ under2Clover = True
        $ under3Clover = True
        $ shoes5Alex = True
        $ top5Alex = True
        $ hat5Alex = True
        $ shoes6Alex = True
        $ bott6Alex = True
        $ top6Alex = True
        $ under8Clover = True
        $ neck8Clover = True
        $ shoes8Clover = True
        $ under8Sam = True
        $ shoes8Sam = True
        $ under2Alex = True
        $ under3Alex = True
        $ under6Alex = True
        $ neck7Alex = True
        $ under7Alex = True
        $ under7AlexB = True
        $ under9Alex = True
        $ wristAcc9Alex = True
        $ shoes9Alex = True
        $ top6Clover = True
        $ shoes6Clover = True
        $ bott6Clover = True
        $ under3Sam = True
        $ under10Alex = True
        $ under10Clover = True
        $ under10Sam = True
        $ under11Clover = True
        $ top15Clover = True
        $ bott15Clover = True
        $ shoes15Clover = True

        $ wristAcc7Clover = True
        $ shoes7Clover = True
        $ hat7Clover = True
        $ top7Clover = True
        $ bott7Clover = True

        $ wristAcc6Clover = True
        $ under6Clover = True

        $ top8Clover = True
        $ bott8Clover = True
        $ neck9Clover = True
        $ hat8Clover = True
        $ wristAcc8Clover = True
        image cardValuSecret = "gui/itemUI/items/box1.png"
        show cardValuSecret:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardValuSecret
        hide scene_fighting
        hide cardRewardBG
        with d3
        if tod == 1:
            jump worldmap
        elif tod == 2:
            jump base



    if cardInput == "64063":
        $ month1CardClaimed = True
        $ hat6Sam = True
        $ intelBoost += 1
        image cardHat6 = "models/green/outfit/hat/hat6.png"
        image cardIntel = "gui/itemUI/items/itemIntel1.png"
        show cardHat6:
            xalign 0.50 yalign -0.95
        with d2
        call screen cardClaim
        hide cardHat6
        show cardIntel:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardIntel
        hide scene_fighting
        hide cardRewardBG
        with d3
        if tod == 1:
            jump worldmap
        elif tod == 2:
            jump base

    if cardInput == "65878":
        $ month1CardClaimed = True
        $ hat6Sam = True
        $ bott6Sam = True
        $ intelBoost += 1
        $ matsBoost += 1
        image cardHat6 = "models/green/outfit/hat/hat6.png"
        image cardPants6 = "models/green/outfit/bott/bott6.png"
        image cardIntel = "gui/itemUI/items/itemIntel1.png"
        image cardMats = "gui/itemUI/items/matsCombo.png"

        show cardHat6:
            xalign 0.50 yalign -0.95
        with d2
        call screen cardClaim
        hide cardHat6

        show cardPants6:
            xalign 0.51 ypos -150 zoom 0.9
        with d2
        call screen cardClaim
        hide cardPants6

        show cardIntel:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardIntel

        show cardMats:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardMats

        hide scene_fighting
        hide cardRewardBG
        with d3
        if tod == 1:
            jump worldmap
        elif tod == 2:
            jump base

    if cardInput == "58806":
        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True
        $ intelBoost += 1
        $ matsBoost += 1
        $ cashBoost += 1
        image cardHat6 = "models/green/outfit/hat/hat6.png"
        image cardPants6 = "models/green/outfit/bott/bott6.png"
        image cardTop6 = "models/green/outfit/chest/top6.png"
        image cardIntel = "gui/itemUI/items/itemIntel1.png"
        image cardMats = "gui/itemUI/items/matsCombo.png"
        image cardValu = "gui/itemUI/items/itemMatsValu.png"

        show cardHat6:
            xalign 0.50 yalign -0.95
        with d2
        call screen cardClaim
        hide cardHat6

        show cardPants6:
            xalign 0.51 ypos -150 zoom 0.9
        with d2
        call screen cardClaim
        hide cardPants6

        show cardTop6:
            xalign 0.51 ypos 70 zoom 0.9
        with d2
        call screen cardClaim
        hide cardTop6

        show cardIntel:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardIntel

        show cardMats:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardMats

        show cardValu:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardValu


    if cardInput == "98459":
        $ month2CardClaimed = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        $ shoes7Sam = True
        $ acesRep += 10
        image cardShoe7 = "models/green/outfit/shoes/shoes7.png"
        image cardRepAc = "gui/cardAcRep.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"

        show cardShoe7:
            xalign 0.50 ypos -0.455
        with d2
        call screen cardClaim
        hide cardShoe7

        show cardRepAc:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Aces."
        hide cardRepAc

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth

    if cardInput == "86221":
        $ month3CardClaimed = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ acesRep += 10
        $ punkRep += 10
        image cardShoe7 = "models/green/outfit/shoes/shoes7.png"
        image cardRepAc = "gui/cardAcRep.png"
        image cardRepPnk = "gui/cardPunkRep.png"
        image cardBott7 = "models/green/outfit/bott/bott7.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"

        show cardShoe7:
            xalign 0.50 ypos -0.455
        with d2
        call screen cardClaim
        hide cardShoe7
        hide cardRepAc

        show cardBott7:
            xalign 0.52 ypos -35
        with d2
        call screen cardClaim
        hide cardBott7

        show cardRepAc:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Aces."
        hide cardRepAc

        show cardRepPnk:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Drift Punk."
        hide cardRepPnk

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth

    if cardInput == "74891":
        $ month3CardClaimed = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True
        $ acesRep += 10
        $ punkRep += 10
        $ outsideRep += 10
        image cardShoe7 = "models/green/outfit/shoes/shoes7.png"
        image cardRepAc = "gui/cardAcRep.png"
        image cardRepPnk = "gui/cardPunkRep.png"
        image cardBott7 = "models/green/outfit/bott/bott7.png"
        image cardTop7 = "models/green/outfit/chest/top7.png"
        image cardTripRep = "gui/cardTripleRep.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"

        show cardShoe7:
            xalign 0.50 ypos -0.455
        with d2
        call screen cardClaim
        hide cardShoe7
        hide cardRepAc

        show cardBott7:
            xalign 0.52 ypos -35
        with d2
        call screen cardClaim
        hide cardBott7

        show cardTop7:
            xalign 0.52 ypos 35
        with d2
        call screen cardClaim
        hide cardTop7

        show cardTripRep:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Aces, Drift Punk and The Outsiders."
        hide cardTripRep

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "66505":

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ acesRep += 10

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardShoe9 = "models/red/outfit/shoes/shoes9.png"
        image cardRepAc = "gui/cardAcRep.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"

        show cardShoe9:
            xalign 0.44 ypos -0.555
        with d2
        call screen cardClaim
        hide cardShoe9

        show cardRepAc:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Aces."
        hide cardRepAc

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth

    if cardInput == "19254":

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ acesRep += 10
        $ punkRep += 10

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott9 = "models/red/outfit/bott/bott9.png"
        image cardShoe9 = "models/red/outfit/shoes/shoes9.png"
        image cardRepAc = "gui/cardAcRep.png"
        image cardRepPnk = "gui/cardPunkRep.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"

        show cardShoe9:
            xalign 0.44 ypos -0.555
        with d2
        call screen cardClaim
        hide cardShoe9

        show cardBott9:
            xalign 0.52 ypos -35
        with d2
        call screen cardClaim
        hide cardBott9

        show cardRepAc:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Aces."
        hide cardRepAc

        show cardRepPnk:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Drift Punk."
        hide cardRepPnk

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth

    if cardInput == "99332":

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True
        $ acesRep += 10
        $ punkRep += 10
        $ outsideRep += 10

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott9 = "models/red/outfit/bott/bott9.png"
        image cardShoe9 = "models/red/outfit/shoes/shoes9.png"
        image cardTop9 = "models/red/outfit/chest/top9.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"
        image cardTripRep = "gui/cardTripleRep.png"

        show cardShoe9:
            xalign 0.44 ypos -0.555
        with d2
        call screen cardClaim
        hide cardShoe9
        hide cardRepAc

        show cardBott9:
            xalign 0.52 ypos -35
        with d2
        call screen cardClaim
        hide cardBott9

        show cardTop9:
            xalign 0.52 ypos 35
        with d2
        call screen cardClaim
        hide cardTop9

        show cardTripRep:
            xalign 0.50 ypos 210 zoom 0.9
        with d2
        call screen cardClaim
        "+10 reputation with Aces, Drift Punk and The Outsiders."
        hide cardTripRep

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "85765":

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ intelBoost += 1

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott7 = "models/yellow/outfit/bott/bott7.png"
        image cardShoe7 = "models/yellow/outfit/shoes/shoes7.png"
        image cardTop7 = "models/yellow/outfit/chest/top7a.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"
        image cardIntel = "gui/itemUI/items/itemIntel1.png"

        show cardShoe7:
            xalign 0.50 ypos -0.355 zoom 0.9
        with d2
        call screen cardClaim
        hide cardShoe7

        show cardIntel:
            xalign 0.50 yalign 0.43 zoom 1.1
        with d2
        call screen cardClaim
        hide cardIntel

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth with d3

    if cardInput == "45691":

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ intelBoost += 1
        $ matsBoost += 1

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott7 = "models/yellow/outfit/bott/bott7.png"
        image cardShoe7 = "models/yellow/outfit/shoes/shoes7.png"
        image cardTop7 = "models/yellow/outfit/chest/top7a.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"

        show cardShoe7:
            xalign 0.52 ypos -0.355 zoom 0.9
        with d2
        call screen cardClaim
        hide cardShoe7
        hide cardRepAc

        show cardTop7:
            xalign 0.50 ypos 75
        with d2
        call screen cardClaim
        hide cardTop7

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth

    if cardInput == "21315":

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True
        $ cashBoost += 1
        $ intelBoost += 1
        $ matsBoost += 1

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott7 = "models/yellow/outfit/bott/bott7.png"
        image cardShoe7 = "models/yellow/outfit/shoes/shoes7.png"
        image cardTop7 = "models/yellow/outfit/chest/top7a.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"

        show cardShoe7:
            xalign 0.52 ypos -0.355 zoom 0.9
        with d2
        call screen cardClaim
        hide cardShoe7
        hide cardRepAc

        show cardTop7:
            xalign 0.50 ypos 75
        with d2
        call screen cardClaim
        hide cardTop7

        show cardBott7:
            xalign 0.52 ypos -50
        with d2
        call screen cardClaim
        hide cardBott7

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "39540":

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ cashBoost += 1

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott9 = "models/green/outfit/bott/bott9.png"
        image cardShoe9 = "models/green/outfit/shoes/shoes9.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"
        image cardTripRep = "gui/cardTripleRep.png"

        show cardShoe9:
            xalign 0.48 ypos -0.500 zoom 0.9
        with d2
        call screen cardClaim
        hide cardShoe9
        hide cardRepAc

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "42416":

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ bott9Sam = True
        $ cashBoost += 3

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott9 = "models/green/outfit/bott/bott9.png"
        image cardShoe9 = "models/green/outfit/shoes/shoes9.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"
        image cardTripRep = "gui/cardTripleRep.png"

        show cardShoe9:
            xalign 0.48 ypos -0.500 zoom 0.9
        with d2
        call screen cardClaim
        hide cardShoe9
        hide cardRepAc

        show cardBott9:
            xalign 0.52 ypos -125
        with d2
        call screen cardClaim
        hide cardBott9

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "67720":

        $ month5CardClaimed = True
        $ acesRep += 10
        $ punkRep += 10
        $ outsideRep += 10
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True
        $ cashBoost += 3

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image cardBott9 = "models/green/outfit/bott/bott9.png"
        image cardShoe9 = "models/green/outfit/shoes/shoes9.png"
        image cardTop9 = "models/green/outfit/chest/top9.png"
        image cardLastmonth = "gui/itemUI/items/box1.png"
        image cardTripRep = "gui/cardTripleRep.png"

        show cardShoe9:
            xalign 0.48 ypos -0.500 zoom 0.9
        with d2
        call screen cardClaim
        hide cardShoe9
        hide cardRepAc

        show cardBott9:
            xalign 0.52 ypos -125
        with d2
        call screen cardClaim
        hide cardBott9

        show cardTop9:
            xalign 0.5 ypos 110
        with d2
        call screen cardClaim
        hide cardTop9

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "68151":
        $ month6CardClaimed = True

        $ cashBoost += 1
        $ acesRep += 10
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image acesRepCard = "gui/cardAcRep.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image headphoneCard = "gui/headphones.png"

        show headphoneCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide headphoneCard

        show acesRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide acesRepCard

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "28307":

        $ month6CardClaimed = True
        $ cashBoost += 3
        $ acesRep += 10
        $ punkRep += 10
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image acesRepCard = "gui/cardAcRep.png"
        image punkRepCard = "gui/cardPunkRep.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image headphoneCard = "gui/headphones.png"

        show headphoneCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide headphoneCard

        show acesRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide acesRepCard

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard

        show punkRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide punkRepCard

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "30357":

        $ month6CardClaimed = True
        $ cashBoost += 3
        $ acesRep += 10
        $ punkRep += 10
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image acesRepCard = "gui/cardAcRep.png"
        image punkRepCard = "gui/cardPunkRep.png"
        image outsiderRepCard = "gui/cardOutsRep.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image underwearCard = "models/red/outfit/under/under7b.png"
        image headphoneCard = "gui/headphones.png"

        show headphoneCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide headphoneCard

        show acesRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide acesRepCard

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard

        show punkRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide punkRepCard

        show outsiderRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide outsiderRepCard

        show underwearCard:
            xalign 0.50 ypos 0.05 zoom 0.85
        with d2
        call screen cardClaim
        hide underwearCard

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "70293":

        $ month7CardClaimed = True
        $ under7Sam = True
        $ cashBoost += 1

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image swimCard1 = "models/green/outfit/under/under7.png"
        image swimCard2 = "models/red/outfit/under/under5.png"
        image swimCard3 = "models/yellow/outfit/under/under5.png"


        show swimCard1:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide swimCard1

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "20959":

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ cashBoost += 2

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image swimCard1 = "models/green/outfit/under/under7.png"
        image swimCard2 = "models/red/outfit/under/under5.png"
        image swimCard3 = "models/yellow/outfit/under/under5.png"


        show swimCard1:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide swimCard1

        show swimCard2:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide swimCard2

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "26053":

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True
        $ cashBoost += 3

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image swimCard1 = "models/green/outfit/under/under7.png"
        image swimCard2 = "models/red/outfit/under/under5.png"
        image swimCard3 = "models/yellow/outfit/under/under5.png"


        show swimCard1:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide swimCard1

        show swimCard2:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide swimCard2

        show swimCard3:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide swimCard3

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth



    if cardInput == "32996":

        $ month8CardClaimed = True
        $ acesRep += 10
        $ cashBoost += 1

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image redUnderCard = "models/green/outfit/under/under2.png"
        image acesRepCard = "gui/cardAcRep.png"
        image punkRepCard = "gui/cardPunkRep.png"
        image outsiderRepCard = "gui/cardOutsRep.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show acesRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide acesRepCard

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "61392":

        $ month8CardClaimed = True
        $ acesRep += 10
        $ punkRep += 10
        $ cashBoost += 2

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image redUnderCard = "models/green/outfit/under/under2.png"
        image acesRepCard = "gui/cardAcRep.png"
        image punkRepCard = "gui/cardPunkRep.png"
        image outsiderRepCard = "gui/cardOutsRep.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show acesRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide acesRepCard

        show punkRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide punkRepCard

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "84598":

        $ month8CardClaimed = True
        $ acesRep += 10
        $ punkRep += 10
        $ outsideRep += 10
        $ cashBoost += 3
        $ under2Sam = True

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image redUnderCard = "models/green/outfit/under/under2.png"
        image acesRepCard = "gui/cardAcRep.png"
        image punkRepCard = "gui/cardPunkRep.png"
        image outsiderRepCard = "gui/cardOutsRep.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show acesRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide acesRepCard

        show punkRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide punkRepCard

        show outsiderRepCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide outsiderRepCard

        show redUnderCard:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide redUnderCard

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth



    if cardInput == "55514":

        $ month9CardClaimed = True
        $ top8Alex = True
        $ bott8Alex = True
        $ neck8Alex = True
        $ shoes8Alex = True
        $ wristAcc8Alex = True
        $ hat12Sam = True

        $ month8CardClaimed = True
        $ under2Sam = True

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image alexMonth8Full = "gui/alexMonth8Full.png"
        image samMonth9Hat = "models/green/outfit/hat/hat12.png"


        show alexMonth8Full:
            xalign 0.50 ypos 0.15 zoom 0.9
        with d2
        call screen cardClaim
        hide alexMonth8Full

        show samMonth9Hat:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide samMonth9Hat

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "92344":

        $ month9CardClaimed = True
        $ top8Alex = True
        $ bott8Alex = True
        $ neck8Alex = True
        $ shoes8Alex = True
        $ wristAcc8Alex = True
        $ hat12Sam = True
        $ shoes12Sam = True

        $ month8CardClaimed = True
        $ under2Sam = True

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image alexMonth8Full = "gui/alexMonth8Full.png"
        image samMonth9Hat = "models/green/outfit/hat/hat12.png"
        image samMonth9Shoes = "models/green/outfit/shoes/shoes12.png"


        show alexMonth8Full:
            xalign 0.50 ypos 0.15 zoom 0.9
        with d2
        call screen cardClaim
        hide alexMonth8Full

        show samMonth9Hat:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide samMonth9Hat

        show samMonth9Shoes:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide samMonth9Shoes

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "80906":

        $ month9CardClaimed = True
        $ top8Alex = True
        $ bott8Alex = True
        $ neck8Alex = True
        $ shoes8Alex = True
        $ wristAcc8Alex = True
        $ hat12Sam = True
        $ shoes12Sam = True
        $ top12Sam = True
        $ bott12Sam = True

        $ month8CardClaimed = True
        $ under2Sam = True

        $ month7CardClaimed = True
        $ under7Sam = True
        $ under5Alex = True
        $ under5Clover = True

        $ month6CardClaimed = True
        $ under7Clover = True
        $ hat1Sam = True

        $ month5CardClaimed = True
        $ shoes9Sam = True
        $ hat9Sam = True
        $ top9Sam = True
        $ bott9Sam = True

        $ month4CardClaimed = True
        $ shoes7Alex = True
        $ top7Alex = True
        $ bott7Alex = True

        $ month3CardClaimed = True
        $ shoes9Clover = True
        $ bott9Clover = True
        $ top9Clover = True

        $ month2CardClaimed = True
        $ shoes7Sam = True
        $ bott7Sam = True
        $ top7Sam = True

        $ month1CardClaimed = True
        $ hat6Sam = True
        $ top6Sam = True
        $ bott6Sam = True

        image alexMonth8Full = "gui/alexMonth8Full.png"
        image samMonth9Hat = "models/green/outfit/hat/hat12.png"
        image samMonth9Shoes = "models/green/outfit/shoes/shoes12.png"
        image samMonth9Rest = "gui/samMonth9Rest.png"


        show alexMonth8Full:
            xalign 0.50 ypos 0.15 zoom 0.9
        with d2
        call screen cardClaim
        hide alexMonth8Full

        show samMonth9Hat:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide samMonth9Hat

        show samMonth9Shoes:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide samMonth9Shoes

        show samMonth9Rest:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide samMonth9Rest

        show cardLastmonth:
            xalign 0.50 ypos 250
        with d2
        call screen cardClaim
        "All of last month's rewards have been added to your inventory!"
        hide cardLastmonth


    if cardInput == "74854":
        $ cashBoost += 1
        $ month10CardClaimed = True

        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard


    if cardInput == "31009":
        $ under3Clover = True
        $ cashBoost += 2
        $ month10CardClaimed = True

        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cloverMonth10Under1 = "models/red/outfit/under/under3.png"


        show cloverMonth10Under1:
            xalign 0.50 ypos 0.07 zoom 0.9
        with d2
        call screen cardClaim
        hide cloverMonth10Under1


        show cashCard:
            xalign 0.50 ypos 0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard


    if cardInput == "81131":
        $ under2Clover = True
        $ under3Clover = True
        $ cashBoost += 3
        $ month10CardClaimed = True

        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cloverMonth10Under1 = "models/red/outfit/under/under3.png"
        image cloverMonth10Under2 = "models/red/outfit/under/under2.png"


        show cloverMonth10Under1:
            xalign 0.50 ypos 0.07 zoom 0.9
        with d2
        call screen cardClaim
        hide cloverMonth10Under1

        show cloverMonth10Under2:
            xalign 0.50 ypos 0.07 zoom 0.9
        with d2
        call screen cardClaim
        hide cloverMonth10Under2

        show cashCard:
            xalign 0.50 ypos 0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard


    if cardInput == "32577":
        $ shoes5Alex = True
        $ cashBoost += 1
        $ month11CardClaimed = True

        image rwd1 = "models/yellow/outfit/shoes/shoes5.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1


    if cardInput == "98376":
        $ shoes5Alex = True
        $ chest5Alex = True
        $ cashBoost += 2
        $ month11CardClaimed = True

        image rwd1 = "models/yellow/outfit/shoes/shoes5.png"
        image rwd2 = "models/yellow/outfit/chest/top5.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1
        show rwd2:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2


    if cardInput == "71265":
        $ shoes5Alex = True
        $ top5Alex = True
        $ hat5Alex = True
        $ cashBoost += 3
        $ month11CardClaimed = True

        image rwd1 = "models/yellow/outfit/shoes/shoes5.png"
        image rwd2 = "models/yellow/outfit/chest/top5.png"
        image rwd3 = "models/yellow/outfit/hat/hat5.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.9
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1
        show rwd2:
            xalign 0.50 ypos 0.1 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2
        show rwd3:
            xalign 0.50 ypos 0.2 zoom 0.5
        with d2
        call screen cardClaim
        hide rwd3




    if cardInput == "575745":
        $ shoes6Alex = True


        $ cashBoost += 1
        $ month12CardClaimed = True

        image rwd1 = "models/yellow/outfit/shoes/shoes6a.png"
        image rwd2 = "models/yellow/outfit/bott/bott6.png"
        image rwd3 = "models/yellow/outfit/hat/hat5.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1


    if cardInput == "635929":
        $ shoes6Alex = True
        $ bott6Alex = True

        $ cashBoost += 2
        $ month12CardClaimed = True

        image rwd1 = "models/yellow/outfit/shoes/shoes6a.png"
        image rwd2 = "models/yellow/outfit/bott/bott6.png"
        image rwd3 = "models/yellow/outfit/hat/hat5.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1
        show rwd2:
            xalign 0.50 ypos 0.0 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2


    if cardInput == "308694":
        $ shoes6Alex = True
        $ bott6Alex = True
        $ top6Alex = True
        $ cashBoost += 3
        $ month12CardClaimed = True

        image rwd1 = "models/yellow/outfit/shoes/shoes6a.png"
        image rwd2 = "models/yellow/outfit/bott/bott6.png"
        image rwd3 = "models/yellow/outfit/chest/top6.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"


        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1:
            xalign 0.50 ypos -0.35 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1
        show rwd2:
            xalign 0.50 ypos 0.0 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2
        show rwd3:
            xalign 0.50 ypos 0.15 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd3


    if cardInput == "50817":
        $ under8Clover = True


        $ cashBoost += 1
        $ month13CardClaimed = True
        image rwd1Mht13 = "models/red/outfit/under/under8Card.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1Mht13:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1Mht13


    if cardInput == "93795":
        $ under8Clover = True
        $ neck8Clover = True
        $ cashBoost += 2
        $ month13CardClaimed = True
        image rwd1Mht13 = "models/red/outfit/under/under8Card.png"
        image rwd1Mht13Nk = "models/red/outfit/neck/neck8.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1Mht13:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1Mht13
        show rwd1Mht13Nk:
            xalign 0.50 ypos 200 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1Mht13Nk


    if cardInput == "69630":
        $ under8Clover = True
        $ neck8Clover = True
        $ shoes8Clover = True
        $ cashBoost += 2
        $ month13CardClaimed = True
        image rwd1Mht13 = "models/red/outfit/under/under8Card.png"
        image rwd1Mht13Nk = "models/red/outfit/neck/neck8.png"
        image rwd1Mht13Shs = "models/red/outfit/shoes/shoes8.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        show rwd1Mht13:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1Mht13
        show rwd1Mht13Nk:
            xalign 0.50 ypos 200 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1Mht13Nk
        show rwd1Mht13Shs:
            xalign 0.44 ypos -250 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1Mht13Shs


    if cardInput == "55166":
        $ under8Sam = True
        $ cashBoost += 1
        $ month14CardClaimed = True
        image rwd1 = "models/green/outfit/under/under8Card.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1


    if cardInput == "70473":
        $ under8Sam = True
        $ cashBoost += 2
        $ acesRep += 1
        $ punkRep += 1
        $ outsideRep += 1
        $ month14CardClaimed = True
        image rwd1 = "models/green/outfit/under/under8Card.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image rwd3 = "gui/cardTripleRep.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        show cashCard2:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2

        show rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1

        show rwd3:
            xalign 0.50 ypos 200 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd3


    if cardInput == "17449":
        $ under8Sam = True
        $ shoes8Sam = True
        $ cashBoost += 3
        $ acesRep += 1
        $ punkRep += 1
        $ outsideRep += 1
        $ month14CardClaimed = True
        image rwd1 = "models/green/outfit/under/under8Card.png"
        image rwd2 = "models/green/outfit/shoes/shoes8.png"
        image rwd3 = "gui/cardTripleRep.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.25 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.45 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1 with d3

        show rwd2:
            xalign 0.50 ypos -230 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2

        show rwd3:
            xalign 0.50 ypos 200 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd3




    if cardInput == "69846":
        $ under9Alex = True
        $ cashBoost += 1
        $ month15CardClaimed = True
        image rwd1 = "models/yellow/outfit/under/under9Card.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1


    if cardInput == "22328":
        $ under9Alex = True
        $ under9Alex = True
        $ cashBoost += 1
        $ month15CardClaimed = True
        image rwd1 = "models/yellow/outfit/under/under9Card.png"
        image rwd2acc = "models/yellow/outfit/acc2/acc9.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2

        show rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1

        show rwd2acc:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2acc


    if cardInput == "61252":
        $ under9Alex = True
        $ wristAcc9Alex = True
        $ shoes9Alex = True
        $ cashBoost += 1
        $ month15CardClaimed = True
        image rwd1 = "models/yellow/outfit/under/under9Card.png"
        image rwd2acc = "models/yellow/outfit/acc2/acc9.png"
        image rwd3 = "models/yellow/outfit/shoes/shoes9.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.25 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.45 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1

        show rwd2acc:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2acc

        show rwd3:
            xalign 0.50 ypos -230 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd3



    if cardInput == "85747":
        $ top6Clover = True
        $ cashBoost += 1
        $ month16CardClaimed = True
        image rwd1 = "models/red/outfit/chest/top6.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show rwd1:
            xalign 0.50 ypos 80 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1

    if cardInput == "13633":
        $ top6Clover = True
        $ shoes6Clover = True
        $ cashBoost += 2
        $ month16CardClaimed = True
        image rwd1 = "models/red/outfit/chest/top6.png"
        image rwd2 = "models/red/outfit/shoes/shoes6.png"
        image rwd3 = "models/red/outfit/bott/bott6.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2

        show rwd1:
            xalign 0.50 ypos 80 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1

        show rwd2:
            xalign 0.450 ypos -350 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2

    if cardInput == "51890":
        $ top6Clover = True
        $ shoes6Clover = True
        $ bott6Clover = True
        $ cashBoost += 3
        $ month16CardClaimed = True
        image rwd1 = "models/red/outfit/chest/top6.png"
        image rwd2 = "models/red/outfit/shoes/shoes6.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show rwd1:
            xalign 0.50 ypos 80 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1

        show rwd2:
            xalign 0.450 ypos -350 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd2

        show rwd3:
            xalign 0.5 ypos -100 zoom 0.8
        with d2
        call screen cardClaim
        hide rwd3


    if cardInput == "71067":
        $ under3Sam = True
        $ cashBoost += 1
        $ month17CardClaimed = True
        image 17rwd1 = "models/green/outfit/under/under3a.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show 17rwd1:
            xalign 0.50 ypos 80 zoom 0.9
        with d2
        call screen cardClaim
        hide rwd1

    if cardInput == "79075":
        $ under3Sam = True
        $ cashBoost += 2
        $ month17CardClaimed = True
        image 17rwd1 = "models/green/outfit/under/under3a.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2

        show 17rwd1:
            xalign 0.50 ypos 80 zoom 0.9
        with d2
        call screen cardClaim
        hide 17rwd1

    if cardInput == "85094":
        $ mnt17 = True
        $ under3Sam = True
        $ cashBoost += 3
        $ month17CardClaimed = True
        image 17rwd1 = "models/green/outfit/under/under3.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 17rwd1:
            xalign 0.50 ypos 45 zoom 0.55
        with d2
        call screen cardClaim
        hide 17rwd1


    if cardInput == "75705":
        $ under10Alex = True
        $ cashBoost += 1
        $ month18CardClaimed = True
        image 18rwd1 = "models/yellow/outfit/under/under10.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show 18rwd1:
            xalign 0.50 ypos 50 zoom 0.9
        with d2
        call screen cardClaim
        hide 18rwd1

    if cardInput == "12197":
        $ under10Alex = True
        $ under10Clover = True
        $ cashBoost += 2
        $ month18CardClaimed = True
        image 18rwd1 = "models/yellow/outfit/under/under10.png"
        image 18rwd2 = "models/red/outfit/under/under10.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2

        show 18rwd1:
            xalign 0.50 ypos 50 zoom 0.9
        with d2
        call screen cardClaim
        hide 18rwd1

        show 18rwd2:
            xalign 0.50 ypos 50 zoom 0.9
        with d2
        call screen cardClaim
        hide 18rwd2

    if cardInput == "37067":
        $ under10Alex = True
        $ under10Clover = True
        $ under10Sam = True
        $ cashBoost += 2
        $ month18CardClaimed = True
        image 18rwd1 = "models/yellow/outfit/under/under10.png"
        image 18rwd2 = "models/red/outfit/under/under10.png"
        image 18rwd3 = "models/green/outfit/under/under10.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 18rwd1:
            xalign 0.50 ypos 50 zoom 0.9
        with d2
        call screen cardClaim
        hide 18rwd1

        show 18rwd2:
            xalign 0.50 ypos 50 zoom 0.9
        with d2
        call screen cardClaim
        hide 18rwd2

        show 18rwd3:
            xalign 0.50 ypos 50 zoom 0.9
        with d2
        call screen cardClaim
        hide 18rwd3


    if cardInput == "71484":
        $ wristAcc7Clover = True
        $ shoes7Clover = True
        $ cashBoost += 1
        $ month19CardClaimed = True
        image 19rwd1 = "models/red/outfit/acc2/acc7.png"
        image 19rwd2 = "models/red/outfit/shoes/shoes7.png"
        image 19rwd3 = "models/red/outfit/hat/hat7.png"
        image 19rwd4 = "models/red/outfit/chest/top7.png"
        image 19rwd5 = "models/red/outfit/bott/bott7.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show 19rwd1:
            xalign 0.50 ypos 20 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd1

        show 19rwd2:
            xalign 0.45 ypos -350 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd2


    if cardInput == "35957":
        $ wristAcc7Clover = True
        $ shoes7Clover = True
        $ hat7Clover = True
        $ top7Clover = True
        $ cashBoost += 2
        $ month19CardClaimed = True
        image 19rwd1 = "models/red/outfit/acc2/acc7.png"
        image 19rwd2 = "models/red/outfit/shoes/shoes7.png"
        image 19rwd3 = "models/red/outfit/hat/hat7.png"
        image 19rwd4 = "models/red/outfit/chest/top7.png"
        image 19rwd5 = "models/red/outfit/bott/bott7.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2

        show 19rwd1:
            xalign 0.50 ypos 20 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd1

        show 19rwd2:
            xalign 0.45 ypos -350 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd2

        show 19rwd3:
            xalign 0.50 ypos 250 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd3

        show 19rwd4:
            xalign 0.50 ypos 100 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd4


    if cardInput == "72416":
        $ wristAcc7Clover = True
        $ shoes7Clover = True
        $ hat7Clover = True
        $ top7Clover = True
        $ bott7Clover = True
        $ cashBoost += 3
        $ month19CardClaimed = True
        image 19rwd1 = "models/red/outfit/acc2/acc7.png"
        image 19rwd2 = "models/red/outfit/shoes/shoes7.png"
        image 19rwd3 = "models/red/outfit/hat/hat7.png"
        image 19rwd4 = "models/red/outfit/chest/top7.png"
        image 19rwd5 = "models/red/outfit/bott/bott7.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 19rwd1:
            xalign 0.50 ypos 20 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd1

        show 19rwd2:
            xalign 0.45 ypos -350 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd2

        show 19rwd3:
            xalign 0.50 ypos 250 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd3

        show 19rwd4:
            xalign 0.50 ypos 100 zoom 0.9
        with d2
        call screen cardClaim
        hide 19rwd4

        show 19rwd5:
            xalign 0.50 ypos -70 zoom 0.7
        with d2
        call screen cardClaim
        hide 19rwd5


    if cardInput == "66559":
        $ under7Alex = True
        $ cashBoost += 1
        $ month20CardClaimed = True
        image 20rwd1 = "models/yellow/outfit/under/under7.png"
        image 20rwd2 = "models/yellow/outfit/neck/neck7.png"
        image 20rwd3 = "models/yellow/outfit/under/under7b.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 20rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 20rwd1


    if cardInput == "24715":
        $ under7Alex = True
        $ neck7Alex = True
        $ cashBoost += 2
        $ month20CardClaimed = True
        image 20rwd1 = "models/yellow/outfit/under/under7.png"
        image 20rwd2 = "models/yellow/outfit/neck/neck7.png"
        image 20rwd3 = "models/yellow/outfit/under/under7b.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 20rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 20rwd1

        show 20rwd2:
            xalign 0.5 ypos 150 zoom 0.9
        with d2
        call screen cardClaim
        hide 20rwd2


    if cardInput == "34524":
        $ under7Alex = True
        $ under7AlexB = True
        $ neck7Alex = True
        $ cashBoost += 3
        $ month20CardClaimed = True
        image 20rwd1 = "models/yellow/outfit/under/under7.png"
        image 20rwd2 = "models/yellow/outfit/neck/neck7.png"
        image 20rwd3 = "models/yellow/outfit/under/under7b.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 20rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 20rwd1

        show 20rwd2:
            xalign 0.5 ypos 150 zoom 0.9
        with d2
        call screen cardClaim
        hide 20rwd2

        show 20rwd3:
            xalign 0.50 ypos 0 zoom 0.55
        with d2
        call screen cardClaim
        hide 20rwd3


    if cardInput == "74059":
        $ cashBoost += 1
        $ month21CardClaimed = True
        $ under11Sam = True
        image 21rwd1 = "models/green/outfit/under/under11.png"
        image 21rwd2 = "models/yellow/outfit/neck/neck7.png"
        image 21rwd3 = "models/yellow/outfit/under/under7b.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 21rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 21rwd1

    if cardInput == "95791":
        $ cashBoost += 2
        $ month21CardClaimed = True
        $ under11Sam = True
        image 21rwd1 = "models/green/outfit/under/under11.png"
        image 21rwd2 = "models/green/outfit/neck/neck3.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 21rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 21rwd1

    if cardInput == "60168":
        $ cashBoost += 3
        $ month21CardClaimed = True
        $ neck3Sam = True
        $ under11Sam = True
        image 21rwd1 = "models/green/outfit/under/under11.png"
        image 21rwd2 = "models/green/outfit/neck/neck3.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 21rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 21rwd1

        show 21rwd2:
            xalign 0.50 ypos 140 zoom 0.9
        with d2
        call screen cardClaim
        hide 21rwd2


    if cardInput == "97030":
        $ cashBoost += 1
        $ month22CardClaimed = True
        $ under6Clover = True
        image 22rwd1 = "models/red/outfit/under/under6.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show 22rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 22rwd1

    if cardInput == "94788":
        $ cashBoost += 2
        $ month22CardClaimed = True
        $ under6Clover = True
        image 22rwd1 = "models/red/outfit/under/under6.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2

        show 22rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 22rwd1

    if cardInput == "21751":
        $ cashBoost += 3
        $ month22CardClaimed = True
        $ under6Clover = True
        $ wristAcc6Clover = True
        image 22rwd1 = "models/red/outfit/under/under6.png"
        image 22rwd2 = "models/red/outfit/acc2/acc6.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"
        image cashCard3 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        show cashCard2:
            xalign 0.50 ypos 0.35 zoom 0.8
        show cashCard3:
            xalign 0.50 ypos 0.4 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard
        hide cashCard2
        hide cashCard3

        show 22rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 22rwd1

        show 22rwd2:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 22rwd2


    if cardInput == "51760":
        $ cashBoost += 1
        $ month23CardClaimed = True
        $ top8Clover = True
        $ bott8Clover = True
        image 23rwd1 = "models/red/outfit/chest/top8.1.png"
        image 23rwd2 = "models/red/outfit/bott/bott8.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show 23rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd1

        show 23rwd2:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd2

    if cardInput == "94117":
        $ cashBoost += 2
        $ month23CardClaimed = True
        $ top8Clover = True
        $ bott8Clover = True
        $ neck9Clover = True
        $ hat8Clover = True
        image 23rwd1 = "models/red/outfit/chest/top8.1.png"
        image 23rwd2 = "models/red/outfit/bott/bott8.png"
        image 23rwd3 = "models/red/outfit/neck/neck9.png"
        image 23rwd4 = "models/red/outfit/hat/hat8.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show 23rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd1

        show 23rwd2:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd2

        show 23rwd3:
            xalign 0.50 ypos 170 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd3

        show 23rwd4:
            xalign 0.52 ypos 240 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd4

    if cardInput == "31723":
        $ cashBoost += 3
        $ month23CardClaimed = True
        $ top8Clover = True
        $ bott8Clover = True
        $ neck9Clover = True
        $ hat8Clover = True
        $ wristAcc8Clover = True
        image 23rwd1 = "models/red/outfit/chest/top8.1.png"
        image 23rwd2 = "models/red/outfit/bott/bott8.png"
        image 23rwd3 = "models/red/outfit/neck/neck9.png"
        image 23rwd4 = "models/red/outfit/hat/hat8.png"
        image 23rwd5 = "models/red/outfit/acc2/acc8mini.png"
        image cashCard = "gui/itemUI/items/itemMatsValu.png"
        image cashCard2 = "gui/itemUI/items/itemMatsValu.png"

        show cashCard:
            xalign 0.50 ypos 0.3 zoom 0.8
        with d2
        call screen cardClaim
        hide cashCard

        show 23rwd1:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd1

        show 23rwd2:
            xalign 0.50 ypos 40 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd2

        show 23rwd3:
            xalign 0.50 ypos 170 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd3

        show 23rwd4:
            xalign 0.52 ypos 240 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd4

        show 23rwd5:
            xalign 0.5 ypos 240 zoom 0.9
        with d2
        call screen cardClaim
        hide 23rwd5



    if cardInput == "anitest":
        jump devAniTest

    if cardInput == "cheats":
        jump cheatMenu


    hide scene_fighting
    hide cardRewardBG
    with d3
    if tod == 1:
        jump worldmap
    elif tod == 2:
        jump base

label cheatMenu:
    menu:
        "1000 money" if True:
            "1000 cash added."
            $ cash += 1000
            jump cheatMenu
        "1000 intel" if True:
            "1000 intel added."
            $ intel += 1000
            jump cheatMenu
        "100 notoriety" if True:
            "Notoriety set to 100."
            $ coverCounter = 100
            jump cheatMenu
        "10 freed agents" if True:
            "10 freed agents added."
            $ freedAgents += 10
            jump cheatMenu
        "Herb Select" if True:
            label cheatMenuHerb:
                pass
            menu:
                "Apple Seed [herbHeal]" if True:
                    $ herbHeal += 1
                "Vigor Leaf [herbAphro]" if True:
                    $ herbAphro += 1
                "Strange Vine [herbMutant]" if True:
                    $ herbMutant += 1
                "Goldthorn [herbGold]" if True:
                    $ herbGold += 1
                "Whisper Weed [herbWhisper]" if True:
                    $ herbWhisper += 1
                "Rebel Weed [herbRebel]" if True:
                    $ herbRebel += 1
                "Back" if True:
                    jump cheatMenu
            jump cheatMenuHerb
        "Back" if True:
            if tod == 1:
                jump worldmap
            elif True:
                jump base

label rewardCalculator:
    $ randomRwd = renpy.random.randint(1, 10)
    $ randomRwd1Lock = randomRwd

    $ randomRwd = renpy.random.randint(1, 10)
    if randomRwd == randomRwd1Lock:
        jump rewardCalculator
    $ randomRwd2Lock = randomRwd

    $ randomRwd = renpy.random.randint(1, 10)
    if randomRwd == randomRwd1Lock or randomRwd == randomRwd2Lock:
        jump rewardCalculator
    $ randomRwd3Lock = randomRwd

    if randomRwd1Lock == 1:
        "Show screen reward 1 here"
    if randomRwd1Lock == 2:
        "Show screen reward 2 here"

    if randomRwd2Lock == 1:
        "Show screen reward 1 here"
    if randomRwd2Lock == 2:
        "Show screen reward 2 here"

    if randomRwd3Lock == 1:
        "Show screen reward 1 here"
    if randomRwd3Lock == 2:
        "Show screen reward 2 here"

    $ rwd1Lock = 0
    $ rwd2Lock = 0
    $ rwd3Lock = 0

    jump rewardCalculator

transform cardSmokeAni:
    xalign 0.54 yalign 0.1 alpha 0.0
    linear 4.0 yalign 0.0 alpha 1.0

transform cardshake:
    xalign 0.5 yalign 0.5
    linear 0.15 xalign 0.502
    linear 0.15 xalign 0.498
    linear 0.15 xalign 0.502
    linear 0.15 xalign 0.498
    linear 0.13 xalign 0.502
    linear 0.13 xalign 0.498
    linear 0.13 xalign 0.502
    linear 0.13 xalign 0.498
    linear 0.1 xalign 0.502
    linear 0.1 xalign 0.498
    linear 0.1 xalign 0.502
    linear 0.1 xalign 0.498
    linear 0.07 xalign 0.502
    linear 0.07 xalign 0.498
    linear 0.07 xalign 0.502
    linear 0.07 xalign 0.498
    linear 0.07 xalign 0.502
    linear 0.07 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498

transform cardshakeRed:
    alpha 0.0
    xalign 0.5 yalign 0.5
    linear 0.15 xalign 0.502 alpha 0.02
    linear 0.15 xalign 0.498 alpha 0.04
    linear 0.15 xalign 0.502 alpha 0.06
    linear 0.15 xalign 0.498 alpha 0.08
    linear 0.13 xalign 0.502 alpha 0.10
    linear 0.13 xalign 0.498 alpha 0.12
    linear 0.13 xalign 0.502 alpha 0.14
    linear 0.13 xalign 0.498 alpha 0.16
    linear 0.1 xalign 0.502 alpha 0.18
    linear 0.1 xalign 0.498 alpha 0.20
    linear 0.1 xalign 0.502 alpha 0.22
    linear 0.1 xalign 0.498 alpha 0.24
    linear 0.07 xalign 0.502 alpha 0.26
    linear 0.07 xalign 0.498 alpha 0.28
    linear 0.07 xalign 0.502 alpha 0.30
    linear 0.07 xalign 0.498 alpha 0.32
    linear 0.07 xalign 0.502 alpha 0.34
    linear 0.07 xalign 0.498 alpha 0.36
    linear 0.04 xalign 0.502 alpha 0.38
    linear 0.04 xalign 0.498 alpha 0.40
    linear 0.04 xalign 0.502 alpha 0.42
    linear 0.04 xalign 0.498 alpha 0.44
    linear 0.04 xalign 0.502 alpha 0.46
    linear 0.04 xalign 0.498 alpha 0.48
    linear 0.04 xalign 0.502 alpha 0.50
    linear 0.04 xalign 0.498 alpha 0.52
    linear 0.04 xalign 0.502 alpha 0.54
    linear 0.04 xalign 0.498 alpha 0.56
    linear 0.04 xalign 0.502 alpha 0.58
    linear 0.04 xalign 0.498 alpha 0.60
    linear 0.04 xalign 0.502 alpha 0.62
    linear 0.04 xalign 0.498 alpha 0.64
    linear 0.04 xalign 0.502 alpha 0.66
    linear 0.04 xalign 0.498 alpha 0.68
    linear 0.04 xalign 0.502 alpha 0.70
    linear 0.04 xalign 0.498 alpha 0.72
    linear 0.04 xalign 0.502 alpha 0.74
    linear 0.04 xalign 0.498 alpha 0.76
    linear 0.04 xalign 0.502 alpha 0.78
    linear 0.04 xalign 0.498 alpha 0.80
    linear 0.04 xalign 0.502 alpha 0.82
    linear 0.04 xalign 0.498 alpha 0.84
    linear 0.04 xalign 0.502 alpha 0.86
    linear 0.04 xalign 0.498 alpha 0.88
    linear 0.04 xalign 0.502 alpha 0.90
    linear 0.04 xalign 0.498 alpha 0.92
    linear 0.04 xalign 0.502 alpha 0.94
    linear 0.04 xalign 0.498 alpha 0.96
    linear 0.04 xalign 0.502 alpha 0.97
    linear 0.04 xalign 0.498 alpha 0.98
    linear 0.04 xalign 0.502 alpha 0.99
    linear 0.04 xalign 0.498 alpha 1.0
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498
    linear 0.04 xalign 0.502
    linear 0.04 xalign 0.498

pause
"pause here"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
