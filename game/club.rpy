default menuOption1 = "Teasing Tosti"
default menuOption2 = "Locked"
default menuOption3 = "Locked"
default menuOption4 = "Locked"
default menuOption5 = "Locked"
default menuOption6 = "Locked"

default checkMark1 = True
default checkMark2 = False
default checkMark3 = False
default checkMark4 = False
default checkMark5 = False
default checkMark6 = False

default decorationStyle = 0

layeredimage bgBar:
    if clubStage <= 3:
        "bgs/bar/bgClub.jpg"
    if clubStage == 0:
        "bgs/bar/stage0.png"
    if clubStage == 1:
        "bgs/bar/stage1.png"
    if clubStage == 2:
        "bgs/bar/stage2.png"
    if clubStage == 3:
        "bgs/bar/stage3.png"
    if clubStage >= 4:
        "bgs/bar/stage4.jpg"
    if clubStage >= 4 and month == 10 and 14 <= day <= 31:
        "bgs/bar/stageHalloween.jpg"
    if clubStage >= 4 and month == 12 and 14 <= day <= 31:
        "bgs/bar/stageChristmas.jpg"

    if clubStage >= 4 and decorationStyle == 1:
        "bgs/bar/stageAces.jpg"
    if clubStage >= 4 and decorationStyle == 2:
        "bgs/bar/stagePunk.jpg"
    if clubStage >= 4 and decorationStyle == 3:
        "bgs/bar/stageOutsiders.jpg"

default greenStrip = 0
default greenStripXP = 0
default redStrip = 0
default redStripXP = 0
default yellowStrip = 0
default yellowStripXP = 0
default kimStrip = 0
default kimStripXP = 0
default britneyStrip = 0
default britneyStripXP = 0
default silvaStrip = 0
default silvaStripXP = 0

layeredimage bgStripclub:
    always:
        "bgs/bgClub.jpg"
    if greenStrip == 1:
        "bgs/bar/stripper3.png"
    if greenStrip == 1 and greenStripStage <= 2:
        "bgs/bar/stripper3Clothes.png"
    if redStrip == 1:
        "bgs/bar/stripper2.png"
    if redStrip == 1 and redStripStage <= 2:
        "bgs/bar/stripper2Clothes.png"
    if yellowStrip == 1:
        "bgs/bar/stripper1.png"
    if yellowStrip == 1 and yellowStripStage <= 2:
        "bgs/bar/stripper1Clothes.png"
    if kimStrip == 1:
        "bgs/bar/stripper4.png"
    if kimStrip == 1 and kimStripStage <= 2:
        "bgs/bar/stripper4Clothes.png"

screen menuOptions:
    add "bgs/bar/menu.png"


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("club")

    hbox:
        spacing 10 xpos 190 yalign 0.35
        text "{color=#C91A1A}{font=fonts/freshMarker.ttf}[menuOption1]          $7.00{/font}{/color}"
    hbox:
        spacing 10 xpos 190 yalign 0.4
        text "{size=-15}{color=#C91A1A}Tastes like crap, but you get to see hotties in revealing \noutfits so stop complaining.{/color}{/size}"
    vbox xpos 585 yalign 0.345:
        imagebutton:
            idle "gui/checkBox1.png"
            hover "gui/checkBox1-hover.png"
            if checkMark1 == False:
                action SetVariable("checkMark1", True)
            else:
                action SetVariable("checkMark1", False)
    if checkMark1 == True:
        hbox:
            xpos 595 yalign 0.35
            text "{color=#ffffff}{font=fonts/freshMarker.ttf}V{/font}{/color}"

    hbox:
        spacing 10 xpos 190 yalign 0.55
        text "{color=#C91A1A}{font=fonts/freshMarker.ttf}[menuOption2]{/font}{/color}"
    if menuOption2 != "Locked":
        hbox:
            spacing 10 xpos 190 yalign 0.6
            text "{size=-15}{color=#C91A1A}Our most popular item! Your waitress will bend over, allowing \nyou to slap her ass when she serves you your burger.{/color}{/size}"
        vbox xpos 585 yalign 0.55:
            imagebutton:
                idle "gui/checkBox1.png"
                hover "gui/checkBox1-hover.png"
                if checkMark2 == False:
                    action SetVariable("checkMark2", True)
                else:
                    action SetVariable("checkMark2", False)
        if checkMark2 == True:
            hbox:
                xpos 595 yalign 0.552
                text "{color=#ffffff}{font=fonts/freshMarker.ttf}V{/font}{/color}"

    hbox:
        spacing 10 xpos 190 yalign 0.75
        text "{color=#C91A1A}{font=fonts/freshMarker.ttf}[menuOption3]{/font}{/color}"
    if menuOption3 != "Locked":
        hbox:
            spacing 10 xpos 190 yalign 0.8
            text "{size=-15}{color=#C91A1A}Your waitress will strip down to her underwear and serve you onion \nrings in her undies.{/color}{/size}"
        vbox xpos 585 yalign 0.75:
            imagebutton:
                idle "gui/checkBox1.png"
                hover "gui/checkBox1-hover.png"
                if checkMark3 == False:
                    action SetVariable("checkMark3", True)
                else:
                    action SetVariable("checkMark3", False)
        if checkMark3 == True:
            hbox:
                xpos 595 yalign 0.752
                text "{color=#ffffff}{font=fonts/freshMarker.ttf}V{/font}{/color}"

    hbox:
        spacing 10 xpos 670 yalign 0.35
        text "{color=#C91A1A}{font=fonts/freshMarker.ttf}[menuOption4]{/font}{/color}"
    if menuOption4 != "Locked":
        hbox:
            spacing 10 xpos 670 yalign 0.4
            text "{size=-15}{color=#C91A1A}What's better than nuggets? Nudes, that's what! \nYour waitres will serve these to you topless!{/color}{/size}"
        vbox xpos 1060 yalign 0.35:
            imagebutton:
                idle "gui/checkBox1.png"
                hover "gui/checkBox1-hover.png"
                if checkMark4 == False:
                    action SetVariable("checkMark4", True)
                else:
                    action SetVariable("checkMark4", False)
        if checkMark4 == True:
            hbox:
                xpos 1069 yalign 0.355
                text "{color=#ffffff}{font=fonts/freshMarker.ttf}V{/font}{/color}"

    hbox:
        spacing 10 xpos 670 yalign 0.55
        text "{color=#C91A1A}{font=fonts/freshMarker.ttf}[menuOption5]{/font}{/color}"
    if menuOption5 != "Locked":
        hbox:
            spacing 10 xpos 670 yalign 0.60
            text "{size=-15}{color=#C91A1A}A Royal Goblet... also known as Booby Beer. For a few dollars more,\nyour waitress will dip her titty into your beer when serving.{/color}{/size}"
        vbox xpos 1060 yalign 0.55:
            imagebutton:
                idle "gui/checkBox1.png"
                hover "gui/checkBox1-hover.png"
                if checkMark5 == False:
                    action SetVariable("checkMark5", True)
                else:
                    action SetVariable("checkMark5", False)
        if checkMark5 == True:
            hbox:
                xpos 1069 yalign 0.552
                text "{color=#ffffff}{font=fonts/freshMarker.ttf}V{/font}{/color}"

    hbox:
        spacing 10 xpos 670 yalign 0.75
        text "{color=#C91A1A}{font=fonts/freshMarker.ttf}[menuOption6]{/font}{/color}"
    if menuOption6 != "Locked":
        hbox:
            spacing 10 xpos 670 yalign 0.80
            text "{size=-15}{color=#C91A1A}Enjoy a lapdance from the hottest girls whilst enjoying the \nbest meal this side of Beverly Hills.{/color}{/size}"
        vbox xpos 1060 yalign 0.75:
            imagebutton:
                idle "gui/checkBox1.png"
                hover "gui/checkBox1-hover.png"
                if checkMark6 == False:
                    action SetVariable("checkMark6", True)
                else:
                    action SetVariable("checkMark6", False)
        if checkMark6 == True:
            hbox:
                xpos 1069 yalign 0.752
                text "{color=#ffffff}{font=fonts/freshMarker.ttf}V{/font}{/color}"



image clubMenu = "bgs/bar/menu.png"
image clubMenuStrip = "bgs/bar/menuStrip.png"

default greenStripStage = 0
default redStripStage = 0
default yellowStripStage = 0
default kimStripStage = 0
default britneyStripStage = 0
default silvaStripStage = 0
default dailyHerb = True

screen stripShowScene:
    add "animations/strip/bgStrip.jpg"


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("club")

    hbox:
        spacing 10 xalign 0.95 ypos 20
        text "{size=+12}{font=fonts/freshmarker.ttf}$[cash]{/font}{/size}"

    if greenStrip:
        add "animations/strip/sam.png"
    if greenStripStage == 0 and greenStrip:
        add "animations/strip/outfitSam.png"
    if greenStripStage == 1 and greenStrip:
        add "animations/strip/outfitSam2.png"
    if greenStripStage == 2 and greenStrip:
        add "animations/strip/outfitSam3.png"
    if redStrip:
        add "animations/strip/clover.png"
    if redStripStage == 0 and redStrip:
        add "animations/strip/outfitClover.png"
    if redStripStage == 1 and redStrip:
        add "animations/strip/outfitClover2.png"
    if redStripStage == 2 and redStrip:
        add "animations/strip/outfitClover3.png"
    if yellowStrip:
        add "animations/strip/alex.png"
    if yellowStripStage == 0 and yellowStrip:
        add "animations/strip/outfitAlex.png"
    if yellowStripStage == 1 and yellowStrip:
        add "animations/strip/outfitAlex2.png"
    if yellowStripStage == 2 and yellowStrip:
        add "animations/strip/outfitAlex3.png"
    if kimStrip:
        add "animations/strip/kim.png"
    if kimStripStage == 0 and kimStrip:
        add "animations/strip/outfitKim.png"
    if kimStripStage == 1 and kimStrip:
        add "animations/strip/outfitKim2.png"
    if kimStripStage == 2 and kimStrip:
        add "animations/strip/outfitKim3.png"


    if greenStrip and redStrip and yellowStrip and kimStrip:
        add "animations/strip/crowd.png"

    if yellowStrip:
        vbox xpos 0.6 ypos 0.2:
            imagebutton:
                idle "animations/strip/tipAlex.png"
                hover "animations/strip/tipAlex-hover.png"
                action Play("sound", "audio/sfx/cashRegister.mp3"), SetVariable("yellowStripStage", yellowStripStage + 1), SetVariable("cash", cash - 10)
    if greenStrip:
        vbox xpos 0.65 ypos 0.4:
            imagebutton:
                idle "animations/strip/tipSam.png"
                hover "animations/strip/tipSam-hover.png"
                action Play("sound", "audio/sfx/cashRegister.mp3"), SetVariable("greenStripStage", greenStripStage + 1), SetVariable("cash", cash - 10)
    if kimStrip:
        vbox xpos 0.12 ypos 0.3:
            imagebutton:
                idle "animations/strip/tipKim.png"
                hover "animations/strip/tipKim-hover.png"
                action Play("sound", "audio/sfx/cashRegister.mp3"), SetVariable("kimStripStage", kimStripStage + 1), SetVariable("cash", cash - 10)
    if redStrip:
        vbox xpos 0.25 ypos 0.8:
            imagebutton:
                idle "animations/strip/tipClover.png"
                hover "animations/strip/tipClover-hover.png"
                action Play("sound", "audio/sfx/cashRegister.mp3"), SetVariable("redStripStage", redStripStage + 1), SetVariable("cash", cash - 10)


screen stripShowScene2:
    add "animations/strip/bgStrip.jpg"


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("club")
    hbox:
        spacing 10 xalign 0.95 ypos 20
        text "{size=+12}{font=fonts/freshmarker.ttf}$[cash]{/font}{/size}"

    if britneyStrip:
        vbox xpos 0.12 ypos 0.3:
            imagebutton:
                idle "animations/strip/tipKim.png"
                hover "animations/strip/tipKim-hover.png"
                action Play("sound", "audio/sfx/cashRegister.mp3"), SetVariable("britneyStripStage", britneyStripStage + 1), SetVariable("cash", cash - 10)
    if silvaStrip:
        vbox xpos 0.65 ypos 0.4:
            imagebutton:
                idle "animations/strip/tipSam.png"
                hover "animations/strip/tipSam-hover.png"
                action Play("sound", "audio/sfx/cashRegister.mp3"), SetVariable("silvaStripStage", silvaStripStage + 1), SetVariable("cash", cash - 10)

    if britneyStrip:
        add "animations/strip/britney.png"
    if britneyStripStage == 0 and britneyStrip:
        add "animations/strip/outfitBritney.png"
    if britneyStripStage == 1 and britneyStrip:
        add "animations/strip/outfitBritney2.png"
    if britneyStripStage == 2 and britneyStrip:
        add "animations/strip/outfitBritney3.png"
    if silvaStrip:
        add "animations/strip/silva.png"
    if silvaStripStage == 0 and silvaStrip:
        add "animations/strip/outfitSilva.png"
    if silvaStripStage == 1 and silvaStrip:
        add "animations/strip/outfitSilva2.png"
    if silvaStripStage == 2 and silvaStrip:
        add "animations/strip/outfitSilva3.png"


label club:
    if tod == 2 and task32Stage >= 2:
        menu:
            "Send Sam to work" if greenStrip == 0 and spy1Status == 0:
                $ spy1Status = 1
                $ greenStrip = 1
            "Send Clover to work" if redStrip == 0 and spy2Status == 0:
                $ spy2Status = 1
                $ redStrip = 1
            "Send Alex to work" if yellowStrip == 0 and spy3Status == 0:
                $ spy3Status = 1
                $ yellowStrip = 1
            "Send Kim to work" if kimStrip == 0:
                $ kimStrip = 1
            "Send Britney to work" if britneyStrip == 0 and task26Stage >= 12:
                $ britneyStrip = 1
            "Send Silva to work" if silvaStrip == 0 and socialSilva >= 12:
                $ silvaStrip = 1
            "Watch strip show" if True:
                menu:
                    "Watch podium 1" if True:
                        call screen stripShowScene with fade
                        pause
                        hide screen stripShowScene with fade
                        jump club
                    "Watch podium 2" if True:
                        call screen stripShowScene2 with fade
                        pause
                        hide screen stripShowScene2 with fade
                        jump club
            "View bar" if True:
                pause
                jump club
            "Return to base" if True:

                scene bgBase with fade
                jump base
        jump club
    elif True:
        pass
    hide clubMenu
    if playerMilkshakeLvl >= 1 and tod == 1:
        menu:
            "Serve milkshakes" if playerMilkshakeLvl >= 1 and tod == 1:
                $ playerMilkshake = True
                "You spend the day serving milkshakes."
                scene black with fade
                jump jobReport
            "Visit bar" if True:
                pass
            "Never mind" if True:
                jump worldmap
    scene bgBar
    if playerKarma >= 60:
        $ karmaCash = renpy.random.randint(1,4)
    menu:
        "{color=#EFD66D}Business Meeting!{/color}" if menuTutActive and spyGreenActive and spyRedActive and spyYellowActive:
            jump task22
        "{color=#EFD66D}Build-A-Bar{/color}" if task32Mat and hiredStaff >= 4 and task32Stage == 1:
            jump task32
        "{color=#EFD66D}Build-A-Bar{/color}" if dlc1Active and task30Stage >= 3 and slutLevel >= 4 and task32Stage == 0:
            jump task32
        "{color=#EFD66D}Short on tits{/color}" if dlc1Active and task30Stage == 0 and spyYellowActive and spyRedActive and task3Stage >= 7:
            jump task30
        "Clean the bar" if clubStage <= 3:
            if clubStage <= 3:
                scene black with fade
                "{b}*Splosh* *Splosh* *Splosh*{/b}"
                "You spend the rest of the day cleaning up the place."
                $ clubStage += 1
                show bgBar
                with fade
                if clubStage <= 3:
                    "The bar is looking better than before, but still needs more fixing."
                if clubStage >= 4 and tutorialActive:
                    jump tutStage9
                scene black
                hide bgBar
                with d3
            if tod == 1:
                scene bgMap:
                    xalign 0.0 yalign 0.0 zoom 0.5
                with fade
                pause 0.5
                jump jobReport
            if tod == 2:
                "You decide to head to bed."
                jump nightCycle


        "Give a round (+karma)" if karmaCash == 1:
            $ karmaCash = 0
            $ playerKarma += 1
            "You give a free round on the house. The customers cheer loudly!"
            play sound "audio/sfx/itemGot.mp3"
            "You gained karma."
            jump club
        "Decorate bar" if task30Stage >= 1:
            menu:
                "Put up Aces decoration" if True:
                    scene black with fade
                    $ decorationStyle = 1
                    scene bgBar with fade
                    pause
                    jump club
                "Put up Drift Punk decoration" if True:
                    scene black with fade
                    $ decorationStyle = 2
                    scene bgBar with fade
                    pause
                    jump club
                "Put up Outsider decoration" if True:
                    scene black with fade
                    $ decorationStyle = 3
                    scene bgBar with fade
                    pause
                    jump club
                "Take down decoration" if True:
                    scene black with fade
                    $ decorationStyle = 0
                    scene bgBar with fade
                    pause
                    jump club
        "Business Meeting" if spyGreenActive and spyRedActive and spyYellowActive:
            if spy1Status == 0 and spy2Status == 0 and spy3Status == 0:
                jump clubManagment
            elif True:
                y "Not everyone is available right now."
                jump club
        "Adjust menu" if clubStage >= 4 and tod == 1:
            show clubMenu
            with d2
            call screen menuOptions
        "Social" if task30Stage >= 3 or socialSilva >= 8:
            menu:
                "Talk to Kim" if task30Stage >= 3 and tod == 1:
                    $ kimFace = 1
                    show scene_darkening with d3
                    show kim at ri with d3
                    kim "Hey boss."
                    if task31Stage == 0:
                        jump task31
                    elif True:
                        jump socialKim
                "Talk to Silva" if 8 <= socialSilva <= 11 and tod == 1:
                    jump socialSilva
                "Ask for herbs" if socialSilva >= 10 and tod == 1 and dailyHerb:
                    $ dailyHerb = False
                    show scene_darkening with d3
                    show silvaModel at ri with d3
                    y "Do you have any herbs available?"
                    sil "Of course. What do you need?"
                    menu:
                        "Apple Seed" if True:
                            $ herbHeal += 1
                        "Vigor Leaf" if True:
                            $ herbAphro += 1
                        "Strange Vine" if True:
                            $ herbMutant += 1
                        "Goldthorn" if True:
                            $ herbGold += 1
                        "Whisper Weed" if True:
                            $ herbWhisper += 1
                        "Rebel Weed" if True:
                            $ herbRebel += 1
                    sil "I'm sure I still have one of those around..."
                    call missionRewardItem from _call_missionRewardItem_16
                    hide silvaModel with d3
                    hide scene_darkening with d3
                    jump club
                "Back" if True:
                    jump club
        "Never mind" if True:

            hide bgBar
            if tod == 1:
                jump worldmap
            if tod == 2:
                jump base


label clubManagment:
    y "Business meeting!"
    show scene_darkening
    if spyGreenActive:
        show green g1 at ri with d3
    if spyRedActive:
        show red r1 at ce with d3
    if spyYellowActive:
        show yellow y1 at le with d3
    menu:
        "{color=#EFD66D}The Booty Burger{/color}" if menuOption2 == "Locked" and task5Stage == 8:
            $ menuOption2 = "Booty Burger            $11.00"
            $ checkMark2 = True
            y "All right, I won't sugarcoat things... We're not doing great.{w} We gotta come up with some new ideas to boost income for our bar."
            y "Suggestion lightning round! Sam!"
            s g28 "Err.... well I er...."
            y "Clover!"
            c r10 "You can't just spring this on u-...."
            y "Alex!"
            a y28 "I've got an ide-...!"
            y "Lightning round over!"
            y ".............."
            y "Not a single suggestion. I am very disappointed in you guys."
            a "I actually have an idea!"
            y "Guess I'll have to come up with something myself."
            a y5 "{b}*Pouts*{/b}"
            y "How about... {i}'Booty Burgers'{/i}...!"
            c "What...?"
            y "We'll start selling burgers!"
            s g1 "Oh that's not a bad idea actua-..."
            y "And with each order you get to slap the waitress' ass!"
            play sound "audio/voice/what.mp3"
            s g28 "W-what?!"
            c r11 "I should've known..."
            a "Noooo, leave my tush alone!"
            y "..................."
            y "{size=-12}Well I think it's a good idea....{/size}"
            c "..............."
            s g15 "..............."
            s g42 "I mean.... you've had crazier ideas..."
            s "I'll be honest... I sorta expected the bar to go his way when you first showed off the uniform."
            s "Plus we already have the occasional customer who can't keep his hands to himself."
            s g38 "{b}*Sighs*{/b} Might aswell charge them for it."
            c r12 "Sam, I'm not sure if this is something we really want to do...."
            s g10 "How much did you make last time you worked here?"
            c r11 "Er...."
            s "Exactly. And how expensive is it to buy new outfits and gadgets?"
            c "I get the point..."
            a y33 "I guess we're gonna have to get used to being slapped on the bu-..."
            play sound "audio/sfx/slap.mp3"
            with hpunch
            a y30 "Eeeep!"
            "You slapped Alex's behind."
            y "Your training starts now!"
            "The girls look a little annoyed, but not nearly as much as you expected them to be."
            hide green
            hide red
            hide yellow
            with d3
            show scene_fighting with d3
            "A new menu option has become available. You can choose to turn it on or off by adjusting the menu."
            hide scene_fighting
            hide scene_darkening
            with d3
            jump club
        "{color=#EFD66D}The Undie Onion Rings{/color}" if menuOption3 == "Locked" and daysPlayed >= 50:
            $ menuOption3 = "Undie Onion Rings       $18.00"
            $ checkMark3 = True
            a y28 "I've got an idea! I've got an idea!"
            y "........................."
            y "Against my better judgment... Go for it."
            a y3 "Undie Onion Rings!"
            y "What?"
            s g16 "What?"
            c r41 "What?"
            a y1 "We serve Onion rings..... in our undies!"
            s "Er...."
            c r12 "You can't be serious..."
            y "Alex....{w} That is brilliant!"
            c r18 "Really [playerName]...."
            s g28 "Then why did we even get the uniform?!"
            y "Hm, that's a good point. I'll think about it."
            hide green
            hide red
            hide yellow
            with d3
            show scene_fighting with d3
            "A new menu option has become available. You can choose to turn it on or off by adjusting the menu."
            hide scene_fighting
            hide scene_darkening
            with d3
            jump club
        "{color=#EFD66D}Nudy Nuggets{/color}" if menuOption4 == "Locked" and task32Stage >= 2:
            $ menuOption4 = "Nudy Nuggets         $23.00"
            $ checkMark4 = True
            y "Business meeting time. We need to think of some ideas to draw in customers."
            y "Clover, can you give us a titillating dish name that we can serve to our customers?"
            c r10 "Well to celebrate the new stripclub. Why not go with something nude themed?"
            c "Like er...."
            a y29 "{size=-14}Nudy Nuggets{/size}"
            s g14 "I can't really think of a dish starting with N off the top of my head..."
            a y28 "{size=-10}Nudy Nuggets{/size}"
            y "Noodles? Naked Noodles...?"
            a "{size=+6}Nudy Nuggets!!!{/size}"
            y ".................."
            a y1 "We serve chicken nuggets.... topless!"
            y "That not a bad idea actually."
            y "You're pretty good at coming up with these, Alex."
            y "All right, Nudy Nuggets it is. This was already a sleazy diner, might aswell go all out."
            hide green
            hide red
            hide yellow
            with d3
            show scene_fighting with d3
            "A new menu option has become available. You can choose to turn it on or off by adjusting the menu."
            hide scene_fighting
            hide scene_darkening
            with d3
            jump club
        "{color=#EFD66D}Royal Goblet{/color}" if menuOption5 == "Locked" and task26Stage >= 5:
            $ menuOption5 = "Royal Goblet         $28.00"
            $ checkMark5 = True
            y "........................"
            y "Boobs."
            c r16 "Boobs?"
            y "We need more boobs."
            s g14 "More? You've already got staff and there us three... and we even have Nudy Nuggets as a menu item!"
            y "It's just not enough."
            y "We..."
            y "Need..."
            y "Royal Goblets."
            "...................................."
            c "What's a Royal Goblet...?"
            "The girls grab their phone and look it up."
            s g10 "Wait... that's it?"
            c r1 "That's easy."
            a y1 "Let's call it Booby Beer!"
            y "......................"
            y "You guys seem uncharacteristically fine with this."
            s g3 "I mean... we already serve food naked. This isn't that outrages."
            c r12 "Yeah, it's honestly kind of tame."
            a y29 "Will guys even pay for this? I'd do it for free if they ask nicely."
            y "........................"
            y "It's almost no fun this way..."
            c r3 "Want me to fix you up a Royal Goblet to make you feel better?"
            y "Yes...."
            hide green
            hide red
            hide yellow
            with d3
            show scene_fighting with d3
            "A new menu option has become available. You can choose to turn it on or off by adjusting the menu."
            hide scene_fighting
            hide scene_darkening
            with d3
            jump club
        "{color=#EFD66D}Lapdance Lobster{/color}" if menuOption6 == "Locked" and task26Stage >= 5 and task32Stage >= 2:
            $ menuOption6 = "Lapdance Lobster      $120.00"
            $ checkMark6 = True
            y "Seeing as our customers have plenty of illegally gotten funds. I think we should put something expensive on the menu next."
            s g16 "Like what?"
            y "I don't know. What's expensive?"
            c r18 "Lobster?"
            s g57 "A titty bar selling lobster...?"
            c r12 "We're not exactly a normal bar. This should at least draw in the Aces crowd."
            y "I like it, but we need a sexy spin on it."
            a y29 "A striptease!"
            a "We could call it a Lobster Lapdance!"
            y "That's the stupidest thing I've ever heard.{w} Let's do it!"
            hide green
            hide red
            hide yellow
            with d3
            show scene_fighting with d3
            "A new menu option has become available. You can choose to turn it on or off by adjusting the menu."
            hide scene_fighting
            hide scene_darkening
            with d3
            jump club
        "Never mind" if True:
            y "False alarm."
            hide green
            hide red
            hide yellow
            hide scene_darkening
            with d3
            jump club


default hiredStaff = 0
default dailyStaffReport = False

label hireStaff:
    "Hiring a girl costs $700. How many girls do you want to hire?"
    menu:
        "Hire one ($ 700)" if cash >= 700 and hiredStaff <= 9:
            $ cash -= 700
            $ hiredStaff += 1
            jump worldmap
        "Hire five ($ 3.500)" if cash >= 4000 and hiredStaff <= 5:
            $ cash -= 4000
            $ hiredStaff += 5
            jump worldmap
        "Hire ten ($ 7.000)" if cash >= 7000 and hiredStaff == 0:
            $ cash -= 7000
            $ hiredStaff += 10
            jump worldmap
        "Never mind" if True:
            jump worldmap
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
