label skipIntro:
    $ tutStage = 8
    "Which spy would you like to start with?"
    menu:
        "Sam (spy in green)" if True:
            $ tutorialActive = False
            $ gang1Active = True
            $ spyGreenActive = True
            $ neck1Sam = True
            $ top1Sam = True
            $ bott1Sam = True
            $ shoes1Sam = True

            $ hat2Sam = True
            $ top2Sam = True
            $ bott2Sam = True
            $ shoes2Sam = True

            $ greenOutfit = 0
            $ greenOutfitArms = 0
            $ greenNeck = 1
            $ greenChest = 1
            $ greenBottom = 1
            $ greenShoes = 1
            $ task1Stage = 3
            $ task1Name = "Open for Business (completed)"
            $ task1Text = "Needing a source of income, you've decided to rebuild the milkshake bar and turn it into a sleazy restaurant.\n \n-Fix up the bar by either working on it yourself, sending your spy to clean it for you, or both.\n \n-The bar has been fixed now all that's left to do is pick up a sexy waitress uniform for your spy.\n \n-Task completed!"
            $ mapSpy1Active = True
            $ mallActive = True

            $ mallActive = True

            $ silHair = 2
            $ silOutfit = 2


    jump worldmap

default landgrabMessage = True
label worldmap:
    if landgrabTimer == 23 and task3Stage >= 7 and task26Stage == 0 and landgrabMessage:
        $ landgrabMessage = False
        "The next Landgrab is seven days away. If you want to participate make sure you free some WOOHP agents."
    if landgrabTimer == 30 and task3Stage >= 7 and task26Stage == 0:
        $ landgrabTimer = 31
        $ agentsAvailable = freedAgents
        scene bgMapRaid with fade
        play music "audio/sfx/warzone.mp3"
        play sound "audio/sfx/raid.mp3"
        pause 1.0
        $ landgrabRandomAssist1 = renpy.random.randint(1,2)
        $ landgrabRandomAssist2 = renpy.random.randint(1,2)
        $ landgrabRandomAssist3 = renpy.random.randint(1,2)
        "WARNING: INCOMING LANDGRAB!"
        if freedAgents <= 4:
            "You don't have enough freed agents to participate in the landgrab. Craft Hypno Earrings and capture some agents during missions."
        call screen mapButtonsRaid
    if 30 <= landgrabTimer <= 31 and task3Stage >= 7:
        scene bgMapRaid
        call screen mapButtonsRaid
    if 18 <= task26Stage <= 29:
        scene bgMapRaid
        call screen mapButtonsRaidFinale

    if missionAreaWOOHPActive and missionAreaAchiev == False:
        $ missionAreaAchiev = True
        show expression "gui/achiev/achiev1.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Unlock all mission zones."
        hide expression "gui/achiev/achiev1.png" with d3
    if sexAchiev == False and sexAct6 != "???":
        $ sexAchiev = True
        show expression "gui/achiev/achiev2.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Unlock full nanobot control."
        hide expression "gui/achiev/achiev2.png" with d3
    if month1Achiev == False and month1CardClaimed:
        $ month1Achiev = True
        show expression "gui/achiev/achiev3.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Claim the first ever Jester Card reward."
        hide expression "gui/achiev/achiev3.png" with d3
    if orangeAchiev == False and swCardClaimed:
        $ orangeAchiev = True
        show expression "gui/achiev/achiev4.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Input the Orange Trainer secret code into the ATM."
        hide expression "gui/achiev/achiev4.png" with d3
    if xmasAchiev == False and photoClaus:
        $ xmasAchiev = True
        show expression "gui/achiev/achiev5.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Bang the Slut Shaming Santa's wife during Christmas."
        hide expression "gui/achiev/achiev5.png" with d3
    if tentacleAchiev == False and tentaclePic:
        $ tentacleAchiev = True
        show expression "gui/achiev/achiev6.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Restore Zukkerthroth's shrines and have him violate the girls."
        hide expression "gui/achiev/achiev6.png" with d3
    if moneyAchiev == False and cash >= 10000:
        $ moneyAchiev = True
        show expression "gui/achiev/achiev7.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Get $10.000."
        hide expression "gui/achiev/achiev7.png" with d3
    if brewAchiev == False and playerMilkshakeLvl >= 6:
        $ brewAchiev = True
        show expression "gui/achiev/achiev8.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Learn the secrets of making the perfect milkshake."
        hide expression "gui/achiev/achiev8.png" with d3
    if woohpHQAchiev == False and HQLevelStatus >= 6:
        $ woohpHQAchiev = True
        show expression "gui/achiev/achiev9.png":
            xalign 0.5 yalign 0.4
        with d3
        "Achievement unlocked.{w} Retake all the floors of WOOHP HQ."
        hide expression "gui/achiev/achiev9.png" with d3
    elif True:
        if tod == 1:
            scene bgMap:
                zoom 0.5
        if tod == 2:
            scene bgMapNight:
                zoom 0.5
        if tutStage == 3:
            scene bgMap:
                xalign 0.63 yalign 0.3




    if coverCounter <= 1:
        show scene_darkening with d3
        "ALERT! Your notoriety has dropped to critical levels!"
        "The only way to recover is by sending your girls on a several day crime spree!"
        menu:
            "Send the girls out" if True:
                y "Emergency meeting!"
                if spyGreenActive:
                    show green g30 at ri with d3
                if spyRedActive:
                    show red r30 at ce with d3
                if spyYellowActive:
                    show yellow y30 at le with d3
                y "Drop everything you're doing!!! Go and commit crimes!"
                hide green
                hide red
                hide yellow
                with d3
                "You send your spies out!"
                hide scene_darkening with d3
                $ spy1Status = 10
                $ spy2Status = 10
                $ spy3Status = 10
                $ coverCounter = 50
                $ emergencyCrimeSpree = 3
                jump worldmap
            "Ignore" if True:
                y "(I'm sure it'll be fi-...)"
                play sound "audio/sfx/explosion1.mp3"
                with hpunch
                "???" "This is where they're hiding!"
                y "What the...?!"
                scene bgBase with d3
                show agentModel at le
                show agentModel2:
                    xalign 0.1 xzoom -1
                show agentModel3 at ri
                show agentModel4:
                    xalign 1.2
                with d3
                "Agent" "Suspect found!"
                "Agent" "Get him!"
                y "Uh oh..."
                play sound "audio/sfx/punch1.mp3"
                hide agentModel1
                hide agentModel2
                hide agentModel3
                hide agentModel4
                scene black
                stop music fadeout 5.0
                with hpunch
                pause 2.0
                show text "{size=+1}GAME OVER{/size}" with d10
                pause
                hide text
                $ MainMenu(confirm=False)()

    if landgrabTimer == 30 and daysPlayed >= 32 and task3Stage >= 7:
        $ landgrabTimer = 31
        scene bgMapRaid with fade
        pause 1.0
        "WARNING: INCOMING LANDGRAB!"
        call screen mapButtonsRaid



    if daysPlayed >= 7 and task2Stage == 0 and tod == 1:
        jump task2
    if task2Stage == 15:
        jump task2



    if daysPlayed >= 20 and task2Stage >= 16 and tod == 1 and task4Stage == 0 and spy1Status != 10:
        jump task4

    if task4Stage == 4:
        jump task4



    if task5Stage == 1:
        jump task5



    if task6Stage == 3:
        $ samMood += 25
        $ spy1Status = 2
        $ mapSpy1Selected = False
        $ greenDayJob = 100
        call audioConfirmationSam from _call_audioConfirmationSam_14



    if task7Stage == 3:
        jump task7


    if task8Stage == 0 and task3Stage >= 7 and task4Stage >= 7 and task5Stage >= 8:
        y "Maybe I should go for a walk today."


    if task15Stage == 2:
        jump task15


    if task16Stage == 2:
        jump task16


    if task26Stage == 1:
        jump task26
    if task26Stage == 11:
        jump task26
    if 2 <= task26Stage <= 24 and intel <= 150 and intelWarning == True:
        $ intelWarning = False
        y "We're running low on intel. Best plan some missions to WOOHP HQ and have my spies gather some."



    if hiredStaff >= 1 and spyKimActive == False:
        jump task30



    if month == 12 and day >= 14 and xmasAnnouchment and tutorialActive == False:
        jump christmasUpdate


    call screen mapButtons


label spy1MapSelect:
    if mapSpy1Selected == True:
        $ mapSpy1Selected = False
        jump worldmap
    elif True:
        $ mapSpy2Selected = False
        $ mapSpy3Selected = False
        $ mapSpy1Selected = True
        $ randAud = renpy.random.randint(1, 5)
        if randAud == 1:
            play sound "audio/voice/imHere.mp3"
        if randAud == 2:
            play sound "audio/voice/ready.mp3"
        if randAud == 3:
            play sound "audio/voice/samHere.mp3"
        if randAud == 4:
            play sound "audio/voice/uhhuh.mp3"
        if randAud == 5:
            play sound "audio/voice/yeah.mp3"
        jump worldmap

label spy2MapSelect:
    if mapSpy2Selected == True:
        $ mapSpy2Selected = False
        jump worldmap
    elif True:
        $ mapSpy1Selected = False
        $ mapSpy3Selected = False
        $ mapSpy2Selected = True
        $ randAud = renpy.random.randint(1, 4)
        if randAud == 1:
            play sound "audio/voice/clover/imHere.mp3"
        if randAud == 2:
            play sound "audio/voice/clover/reportingIn.mp3"
        if randAud == 3:
            play sound "audio/voice/clover/waddaYaNeed.mp3"
        if randAud == 4:
            play sound "audio/voice/clover/yeah.mp3"
        jump worldmap

label spy3MapSelect:
    if mapSpy3Selected == True:
        $ mapSpy3Selected = False
        jump worldmap
    elif True:
        $ mapSpy1Selected = False
        $ mapSpy2Selected = False
        $ mapSpy3Selected = True
        $ randAud = renpy.random.randint(1, 4)
        if randAud == 1:
            play sound "audio/voice/alex/yesSir.mp3"
        if randAud == 2:
            play sound "audio/voice/alex/alexHere.mp3"
        if randAud == 3:
            play sound "audio/voice/alex/ready.mp3"
        if randAud == 4:
            play sound "audio/voice/alex/hiya.mp3"
        jump worldmap

label spy4MapSelect:
    if mapSpy4Selected == True:
        $ mapSpy4Selected = False
        jump worldmap
    elif True:
        $ mapSpy0Selected = False
        $ mapSpy5Selected = False
        $ mapSpy6Selected = False
        $ mapSpy4Selected = True
        jump worldmap
label spy5MapSelect:
    if mapSpy5Selected == True:
        $ mapSpy5Selected = False
        jump worldmap
    elif True:
        $ mapSpy0Selected = False
        $ mapSpy4Selected = False
        $ mapSpy6Selected = False
        $ mapSpy5Selected = True
        jump worldmap
label spy6MapSelect:
    if mapSpy6Selected == True:
        $ mapSpy6Selected = False
        jump worldmap
    elif True:
        $ mapSpy0Selected = False
        $ mapSpy5Selected = False
        $ mapSpy4Selected = False
        $ mapSpy6Selected = True
        jump worldmap
label spy0MapSelect:
    if mapSpy0Selected == True:
        $ mapSpy0Selected = False
        jump worldmap
    elif True:
        $ mapSpy0Selected = True
        jump worldmap

label clubMapSelect:
    if mapSpy1Selected:
        if outfitSamUniformActive and clubStage >= 4 and tutStage >= 11:
            if samMood <= 25:
                "Sam's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy1Selected = False
                        jump worldmap

            if samSupLvl == 1:
                $ samMood -= 3
            if samSupLvl == 2:
                $ samMood -= 5
            if samSupLvl == 3:
                $ samMood -= 7

            $ spy1Status = 1
            $ mapSpy1Selected = False
            $ greenDayJob = 4
            call audioConfirmationSam from _call_audioConfirmationSam
            jump worldmap
        if outfitSamUniformActive and tutStage <= 10:
            y "I should probably discuss the situation with her first."
            jump worldmap
        if clubStage <= 3:
            $ greenDayJob = 4
            sM "Sure, I can help clean."
            call audioConfirmationSam from _call_audioConfirmationSam_7

            if samSupLvl == 1:
                $ samMood -= 3
            if samSupLvl == 2:
                $ samMood -= 5
            if samSupLvl == 3:
                $ samMood -= 7

            $ spy1Status = 1
            $ mapSpy1Selected = False
        elif True:
            if outfitSamUniformActive:
                y "I should probably discuss the situation with her first."
                scene black with fade
                scene bgBase with fade
                jump tutStage11
            elif True:
                y "I haven't picked her up a uniform from the mall yet."
            jump worldmap
    if mapSpy2Selected:
        if outfitCloverUniformActive and clubStage >= 4 and tutStage >= 11:
            if cloverMood <= 25:
                "Clover's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy2Selected = False
                        jump worldmap

            if cloverSupLvl == 1:
                $ cloverMood -= 3
            if cloverSupLvl == 2:
                $ cloverMood -= 5
            if cloverSupLvl == 3:
                $ cloverMood -= 7

            $ spy2Status = 1
            $ mapSpy2Selected = False
            $ redDayJob = 4
            call audioConfirmationClover from _call_audioConfirmationClover_3
            jump worldmap
        if outfitCloverUniformActive and tutStage <= 10:
            y "I should probably discuss the situation with Clover first."
            jump worldmap
        if outfitCloverUniformActive and tutStage >= 11:

            if cloverSupLvl == 1:
                $ cloverMood -= 3
            if cloverSupLvl == 2:
                $ cloverMood -= 5
            if cloverSupLvl == 3:
                $ cloverMood -= 7

            $ spy2Status = 1
            $ mapSpy2Selected = False
            $ redDayJob = 4
            call audioConfirmationClover from _call_audioConfirmationClover_4
            jump worldmap
    if mapSpy3Selected:
        if outfitAlexUniformActive and clubStage >= 4 and tutStage >= 11:
            if alexMood <= 25:
                "Alex's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy3Selected = False
                        jump worldmap

            if alexSupLvl == 1:
                $ alexMood -= 3
            if alexSupLvl == 2:
                $ alexMood -= 5
            if alexSupLvl == 3:
                $ alexMood -= 7

            $ spy3Status = 1
            $ mapSpy3Selected = False
            $ yellowDayJob = 4
            call audioConfirmationAlex from _call_audioConfirmationAlex_1
            jump worldmap
        if outfitAlexUniformActive and tutStage <= 10:
            y "I should probably discuss the situation with Alex first."
            jump worldmap
        if outfitAlexUniformActive and tutStage >= 11:

            if alexSupLvl == 1:
                $ alexMood -= 3
            if alexSupLvl == 2:
                $ alexMood -= 5
            if alexSupLvl == 3:
                $ alexMood -= 7

            $ spy3Status = 1
            $ mapSpy3Selected = False
            $ yellowDayJob = 4
            call audioConfirmationAlex from _call_audioConfirmationAlex_2
            jump worldmap
        elif True:
            y "I haven't picked her up a uniform from the mall yet."
            jump worldmap
    jump worldmap

label breakMapSelect:
    if mapSpy1Selected:
        if capturedAgents == 0:
            "There are no captured Agents controlled by nanobots."
            jump worldmap
        elif True:
            $ greenDayJob = 11
            $ spy1Status = 1
            if slutLevel <= 3:
                $ samMood -= 10
            if 4 <= slutLevel <= 6:
                $ samMood -= 7
            if 7 <= slutLevel <= 9:
                $ samMood -= 5
            elif True:
                $ samMood -= 2
            $ mapSpy1Selected = False
            sM "Ugh... I hate this~...."
            jump worldmap
    if mapSpy2Selected:
        if capturedAgents == 0:
            "There are no captured Agents controlled by nanobots."
            jump worldmap
        elif True:
            $ redDayJob = 11
            $ spy2Status = 1
            if slutLevel <= 3:
                $ cloverMood -= 10
            if 4 <= slutLevel <= 6:
                $ cloverMood -= 7
            if 7 <= slutLevel <= 9:
                $ cloverMood -= 5
            elif True:
                $ cloverMood -= 2
            $ mapSpy2Selected = False
            cM "Fine, but they better not get touchy!"
            jump worldmap
    if mapSpy3Selected:
        if capturedAgents == 0:
            "There are no captured Agents controlled by nanobots."
            jump worldmap
        elif True:
            $ yellowDayJob = 11
            $ spy3Status = 1
            if slutLevel <= 3:
                $ alexMood -= 10
            if 4 <= slutLevel <= 6:
                $ alexMood -= 7
            if 7 <= slutLevel <= 9:
                $ alexMood -= 5
            elif True:
                $ alexMood -= 2
            $ mapSpy3Selected = False
            aM "{b}*Gulp*{/b} Well if you say so..."
        jump worldmap

label mallMapSelect:
    if mapSpy1Selected:
        "Give Sam some time off to spend at the mall?"
        menu:
            "Yes ($150)" if cash >= 150:
                $ samMood += 30
                $ cash -= 150
                $ spy1Status = 2
                $ mapSpy1Selected = False
                $ greenDayJob = 100
                call audioConfirmationSam from _call_audioConfirmationSam_2
                jump worldmap
            "Never mind" if True:
                jump worldmap
    if mapSpy2Selected:
        "Give Clover some time off to spend at the mall?"
        menu:
            "Yes ($150)" if cash >= 150:
                $ cloverMood += 30
                $ cash -= 150
                $ spy2Status = 2
                $ mapSpy2Selected = False
                $ redDayJob = 100
                call audioConfirmationClover from _call_audioConfirmationClover_7
                jump worldmap
            "Never mind" if True:
                jump worldmap
    if mapSpy3Selected:
        "Give Alex some time off to spend at the mall?"
        menu:
            "Yes ($150)" if cash >= 150:
                $ alexMood += 30
                $ cash -= 150
                $ spy3Status = 2
                $ mapSpy3Selected = False
                $ yellowDayJob = 100
                call audioConfirmationAlex from _call_audioConfirmationAlex_4
                jump worldmap
            "Never mind" if True:
                jump worldmap

label beachMapSelect:
    if mapSpy1Selected:
        "Give Sam some time off to spend at the beach?"
        menu:
            "Yes ($50)" if cash >= 50:
                $ samMood += 10
                $ cash -= 50
                $ spy1Status = 2
                $ mapSpy1Selected = False
                $ greenDayJob = 101
                call audioConfirmationSam from _call_audioConfirmationSam_1
                jump worldmap
            "Never mind" if True:
                jump worldmap
    if mapSpy2Selected:
        "Give Clover some time off to spend at the beach?"
        menu:
            "Yes ($50)" if cash >= 50:
                $ cloverMood += 10
                $ cash -= 50
                $ spy2Status = 2
                $ mapSpy2Selected = False
                $ redDayJob = 101
                call audioConfirmationClover from _call_audioConfirmationClover_1
                jump worldmap
            "Never mind" if True:
                jump worldmap
    if mapSpy3Selected:
        "Give Alex some time off to spend at the beach?"
        menu:
            "Yes ($50)" if cash >= 50:
                $ alexMood += 10
                $ cash -= 50
                $ spy3Status = 2
                $ mapSpy3Selected = False
                $ yellowDayJob = 101
                call audioConfirmationAlex from _call_audioConfirmationAlex_5
                jump worldmap
            "Never mind" if True:
                jump worldmap

label crimeMapSelect:
    if randNotMission == 10:
        if mapSpy1Selected and nanoLevelSam >= 70:
            if samMood <= 25:
                "Sam's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy1Selected = False
                        jump worldmap
            if 90 <= nanoLevelSam <= 100:
                sM "All right, nobody be a hero!"
            if 80 <= nanoLevelSam <= 89:

                if samSupLvl == 1:
                    $ samMood -= 3
                if samSupLvl == 2:
                    $ samMood -= 5
                if samSupLvl == 3:
                    $ samMood -= 7

                sM "As long as nobody gets hurt."
            if 70 <= nanoLevelSam <= 79:

                if samSupLvl == 1:
                    $ samMood -= 3
                if samSupLvl == 2:
                    $ samMood -= 5
                if samSupLvl == 3:
                    $ samMood -= 7

                sM "If I really have to..."
            $ greenDayJob = 6
            $ spy1Status = 1
            $ mapSpy1Selected = False
            call audioConfirmationSam from _call_audioConfirmationSam_4
            jump worldmap
        elif mapSpy2Selected and nanoLevelClover >= 70:
            if cloverMood <= 25:
                "Clover's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy2Selected = False
                        jump worldmap
            if 90 <= nanoLevelClover <= 100:
                cM "Guns are a girl's best friend~..."
            if 80 <= nanoLevelClover <= 89:

                if cloverSupLvl == 1:
                    $ cloverMood -= 3
                if cloverSupLvl == 2:
                    $ cloverMood -= 5
                if cloverSupLvl == 3:
                    $ cloverMood -= 7

                cM "Fine, but I'm not actually shooting someone!"
            if nanoLevelClover <= 79:

                if cloverSupLvl == 1:
                    $ cloverMood -= 5
                if cloverSupLvl == 2:
                    $ cloverMood -= 7
                if cloverSupLvl == 3:
                    $ cloverMood -= 9

                cM "I really don't want to... Let's just get this over with."
            $ redDayJob = 6
            $ spy2Status = 1
            $ mapSpy2Selected = False
            call audioConfirmationClover from _call_audioConfirmationClover_2
            jump worldmap
        elif mapSpy3Selected and nanoLevelAlex >= 70:
            if alexMood <= 25:
                "Alex's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy3Selected = False
                        jump worldmap
            if 90 <= nanoLevelAlex <= 100:
                aM "I'm gonna shoot somebody!"
            if 80 <= nanoLevelAlex <= 89:

                if alexSupLvl == 1:
                    $ alexMood -= 3
                if alexSupLvl == 2:
                    $ alexMood -= 5
                if alexSupLvl == 3:
                    $ alexMood -= 7

                aM "Okay... but I'm keeping the safety on..."
            if nanoLevelAlex <= 79:

                if alexSupLvl == 1:
                    $ alexMood -= 5
                if alexSupLvl == 2:
                    $ alexMood -= 7
                if alexSupLvl == 3:
                    $ alexMood -= 9

                aM "Rob a store? Well... okay, but only if nobody gets hurt."
            $ yellowDayJob = 6
            $ spy3Status = 1
            $ mapSpy3Selected = False
            call audioConfirmationAlex from _call_audioConfirmationAlex_6
            jump worldmap
        elif True:
            "Your spies nanobot levels are too low for this. Visit the STATUS screen to decide how much or how little they should focus on suppressing them."
            jump worldmap
    elif randNotMission == 9:
        if mapSpy1Selected and nanoLevelSam >= 60:
            if samMood <= 25:
                "Sam's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy1Selected = False
                        jump worldmap
            if 90 <= nanoLevelSam <= 100:
                sM "I love driving cars!"
            if 80 <= nanoLevelSam <= 89:

                if samSupLvl == 1:
                    $ samMood -= 3
                if samSupLvl == 2:
                    $ samMood -= 5
                if samSupLvl == 3:
                    $ samMood -= 7

                sM "Well that'll get us some money I guess."
            if nanoLevelSam <= 79:

                if samSupLvl == 1:
                    $ samMood -= 5
                if samSupLvl == 2:
                    $ samMood -= 7
                if samSupLvl == 3:
                    $ samMood -= 9

                sM "Fine..."
            $ greenDayJob = 10
            $ spy1Status = 1
            $ mapSpy1Selected = False
            call audioConfirmationSam from _call_audioConfirmationSam_13
            jump worldmap
        elif mapSpy2Selected and nanoLevelClover >= 60:
            if cloverMood <= 25:
                "Clover's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy2Selected = False
                        jump worldmap
            if 90 <= nanoLevelClover <= 100:
                cM "Reckless driving for the win!"
            if 80 <= nanoLevelClover <= 89:

                if cloverSupLvl == 1:
                    $ cloverMood -= 3
                if cloverSupLvl == 2:
                    $ cloverMood -= 5
                if cloverSupLvl == 3:
                    $ cloverMood -= 7

                cM "I don't feel right stealing somebody's car... but I did always want to have a pink one."
            if nanoLevelClover <= 79:

                if cloverSupLvl == 1:
                    $ cloverMood -= 5
                if cloverSupLvl == 2:
                    $ cloverMood -= 7
                if cloverSupLvl == 3:
                    $ cloverMood -= 9

                cM "Well if I have to..."
            $ redDayJob = 10
            $ spy2Status = 1
            $ mapSpy2Selected = False
            call audioConfirmationClover from _call_audioConfirmationClover_14
            jump worldmap
        elif mapSpy3Selected and nanoLevelAlex >= 60:
            if alexMood <= 25:
                "Alex's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy3Selected = False
                        jump worldmap
            if 90 <= nanoLevelAlex <= 100:
                aM "Beep! Beep! Outta the way!"
            if 80 <= nanoLevelAlex <= 89:

                if alexSupLvl == 1:
                    $ alexMood -= 3
                if alexSupLvl == 2:
                    $ alexMood -= 5
                if alexSupLvl == 3:
                    $ alexMood -= 7

                aM "Are you sure? I failed my car exam three times."
            if nanoLevelAlex <= 79:

                if alexSupLvl == 1:
                    $ alexMood -= 5
                if alexSupLvl == 2:
                    $ alexMood -= 7
                if alexSupLvl == 3:
                    $ alexMood -= 9

                aM "But that's somebody's car... Well okay..."
            $ yellowDayJob = 10
            $ spy3Status = 1
            $ mapSpy3Selected = False
            call audioConfirmationAlex from _call_audioConfirmationAlex_13
            jump worldmap
        elif True:
            "Your spies nanobot levels are too low for this. Visit the STATUS screen to decide how much or how little they should focus on suppressing them."
            jump worldmap
    elif randNotMission == 8:
        if mapSpy1Selected and nanoLevelSam >= 60:
            if samMood <= 25:
                "Sam's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy1Selected = False
                        jump worldmap
            if 90 <= nanoLevelSam <= 100:
                sM "Time to start an inferno!"
            if 80 <= nanoLevelSam <= 89:

                if samSupLvl == 1:
                    $ samMood -= 3
                if samSupLvl == 2:
                    $ samMood -= 5
                if samSupLvl == 3:
                    $ samMood -= 7

                sM "As long as nobody gets hurt."
            if nanoLevelSam <= 79:

                if samSupLvl == 1:
                    $ samMood -= 5
                if samSupLvl == 2:
                    $ samMood -= 7
                if samSupLvl == 3:
                    $ samMood -= 9

                sM "Well... just a small one, okay?"
            $ greenDayJob = 7
            $ spy1Status = 1
            $ mapSpy1Selected = False
            call audioConfirmationSam from _call_audioConfirmationSam_5
            jump worldmap
        elif mapSpy2Selected  and nanoLevelClover >= 60:
            if cloverMood <= 25:
                "Clover's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy2Selected = False
                        jump worldmap
            if 90 <= nanoLevelClover <= 100:
                cM "♫♪Fire, fire. Burns much brighter, when oxygen is the supplier.♫♪"
            if 80 <= nanoLevelClover <= 89:

                if cloverSupLvl == 1:
                    $ cloverMood -= 3
                if cloverSupLvl == 2:
                    $ cloverMood -= 5
                if cloverSupLvl == 3:
                    $ cloverMood -= 7

                cM "As long as it doesn't spread, it should be fine."
            if nanoLevelClover <= 79:

                if cloverSupLvl == 1:
                    $ cloverMood -= 5
                if cloverSupLvl == 2:
                    $ cloverMood -= 7
                if cloverSupLvl == 3:
                    $ cloverMood -= 9

                cM "Burn somebody's property...? Fine, as long as nobody gets hurt."
            $ redDayJob = 7
            $ spy2Status = 1
            $ mapSpy2Selected = False
            call audioConfirmationClover from _call_audioConfirmationClover_6
            jump worldmap
        elif mapSpy3Selected and nanoLevelAlex >= 60:
            if alexMood <= 25:
                "Alex's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy3Selected = False
                        jump worldmap
            if 90 <= nanoLevelAlex <= 100:
                aM "I was getting cold anyways!"
            if 80 <= nanoLevelAlex <= 89:

                if alexSupLvl == 1:
                    $ alexMood -= 3
                if alexSupLvl == 2:
                    $ alexMood -= 5
                if alexSupLvl == 3:
                    $ alexMood -= 7

                aM "The Outsiders showed me how to do it... Well all right, if I have to..."
            if nanoLevelAlex <= 79:

                if alexSupLvl == 1:
                    $ alexMood -= 5
                if alexSupLvl == 2:
                    $ alexMood -= 7
                if alexSupLvl == 3:
                    $ alexMood -= 9

                aM "A fire?! But that's dangerous!{w} Well just a small one then..."
            $ yellowDayJob = 7
            $ spy3Status = 1
            $ mapSpy3Selected = False
            call audioConfirmationAlex from _call_audioConfirmationAlex_7
        elif True:
            "Your spies nanobot levels are too low for this. Visit the STATUS screen to decide how much or how little they should focus on suppressing them."

    elif 6 <= randNotMission <= 7:
        if mapSpy1Selected and nanoLevelSam >= 50:
            if samMood <= 25:
                "Sam's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy1Selected = False
                        jump worldmap
            if 90 <= nanoLevelSam <= 100:
                sM "Could always use a bit of extra cash~..."
            if 80 <= nanoLevelSam <= 89:

                if samSupLvl == 1:
                    $ samMood -= 3
                if samSupLvl == 2:
                    $ samMood -= 5
                if samSupLvl == 3:
                    $ samMood -= 7

                sM "It's for a good cause."
            if nanoLevelSam <= 79:

                if samSupLvl == 1:
                    $ samMood -= 5
                if samSupLvl == 2:
                    $ samMood -= 7
                if samSupLvl == 3:
                    $ samMood -= 9

                sM "I hope I don't have to hurt anyone..."
            $ greenDayJob = 8
            $ spy1Status = 1
            $ mapSpy1Selected = False
            call audioConfirmationSam from _call_audioConfirmationSam_6
            jump worldmap
        elif mapSpy2Selected and nanoLevelClover >= 50:
            if cloverMood <= 25:
                "Clover's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy2Selected = False
                        jump worldmap
            if 90 <= nanoLevelClover <= 100:
                cM "Could always use some extra Benjamins!"
            if 80 <= nanoLevelClover <= 89:

                if cloverSupLvl == 1:
                    $ cloverMood -= 3
                if cloverSupLvl == 2:
                    $ cloverMood -= 5
                if cloverSupLvl == 3:
                    $ cloverMood -= 7

                cM "I'm sure they won't notice a few bucks missing."
            if nanoLevelClover <= 79:

                if cloverSupLvl == 1:
                    $ cloverMood -= 5
                if cloverSupLvl == 2:
                    $ cloverMood -= 7
                if cloverSupLvl == 3:
                    $ cloverMood -= 9

                cM "Taking money from people feels wrong..."
            $ redDayJob = 8
            $ spy2Status = 1
            $ mapSpy2Selected = False
            call audioConfirmationClover from _call_audioConfirmationClover_9
            jump worldmap
        elif mapSpy3Selected and nanoLevelAlex >= 50:
            if alexMood <= 25:
                "Alex's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy3Selected = False
                        jump worldmap
            if 90 <= nanoLevelAlex <= 100:
                aM "I'm gonna buy candy with this money!"
            if 80 <= nanoLevelAlex <= 89:

                if alexSupLvl == 1:
                    $ alexMood -= 3
                if alexSupLvl == 2:
                    $ alexMood -= 5
                if alexSupLvl == 3:
                    $ alexMood -= 7

                aM "If this is what it takes, then fine."
            if nanoLevelAlex <= 79:

                if alexSupLvl == 1:
                    $ alexMood -= 5
                if alexSupLvl == 2:
                    $ alexMood -= 7
                if alexSupLvl == 3:
                    $ alexMood -= 9

                aM "But that's somebody else's money..."
            $ yellowDayJob = 8
            $ spy3Status = 1
            $ mapSpy3Selected = False
            call audioConfirmationAlex from _call_audioConfirmationAlex_8
        elif True:
            "Your spies nanobot levels are too low for this. Visit the STATUS screen to decide how much or how little they should focus on suppressing them."

    elif 4 <= randNotMission <= 5:
        if mapSpy1Selected and nanoLevelSam >= 40:
            if samMood <= 25:
                "Sam's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy1Selected = False
                        jump worldmap
            if 90 <= nanoLevelSam <= 100:
                sM "Time to bring out my artistic form!"
            if 80 <= nanoLevelSam <= 89:

                if samSupLvl == 1:
                    $ samMood -= 3
                if samSupLvl == 2:
                    $ samMood -= 5
                if samSupLvl == 3:
                    $ samMood -= 7

                sM "I guess spray painting isn't that bad."
            if nanoLevelSam <= 79:

                if samSupLvl == 1:
                    $ samMood -= 3
                if samSupLvl == 2:
                    $ samMood -= 5
                if samSupLvl == 3:
                    $ samMood -= 7

                sM "I hope I won't get in trouble for this."
            $ greenDayJob = 9
            $ spy1Status = 1
            $ mapSpy1Selected = False
            call audioConfirmationSam from _call_audioConfirmationSam_9
            jump worldmap
        elif mapSpy2Selected and nanoLevelClover >= 40:
            if cloverMood <= 25:
                "Clover's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy2Selected = False
                        jump worldmap
            if 90 <= nanoLevelClover <= 100:
                cM "Let's paint the town red... literally!"
            if 80 <= nanoLevelClover <= 89:

                if cloverSupLvl == 1:
                    $ cloverMood -= 3
                if cloverSupLvl == 2:
                    $ cloverMood -= 5
                if cloverSupLvl == 3:
                    $ cloverMood -= 7

                cM "Well I guess it doesn't really hurt anyone.."
            if nanoLevelClover <= 79:

                if cloverSupLvl == 1:
                    $ cloverMood -= 5
                if cloverSupLvl == 2:
                    $ cloverMood -= 7
                if cloverSupLvl == 3:
                    $ cloverMood -= 9

                cM "This stuff better not stain my clothes."
            $ redDayJob = 9
            $ spy2Status = 1
            $ mapSpy2Selected = False
            call audioConfirmationClover from _call_audioConfirmationClover_10
            jump worldmap
        elif mapSpy3Selected and nanoLevelAlex >= 40:
            if alexMood <= 25:
                "Alex's morale is too low to go to work."
                menu:
                    "Order her (-karma)" if True:
                        $ playerKarma -= 1
                    "Never mind" if True:
                        $ mapSpy3Selected = False
                        jump worldmap
            if 90 <= nanoLevelAlex <= 100:
                aM "Gonna let my artistic soul run free!"
            if 80 <= nanoLevelAlex <= 89:

                if alexSupLvl == 1:
                    $ alexMood -= 3
                if alexSupLvl == 2:
                    $ alexMood -= 5
                if alexSupLvl == 3:
                    $ alexMood -= 7

                aM "A little bit of paint never hurt anyone... I think."
            if nanoLevelAlex <= 79:

                if alexSupLvl == 1:
                    $ alexMood -= 5
                if alexSupLvl == 2:
                    $ alexMood -= 7
                if alexSupLvl == 3:
                    $ alexMood -= 9

                aM "Fine... but I won't paint anything scary! Maybe a smiley... or a butterfly!"
            $ yellowDayJob = 9
            $ spy3Status = 1
            $ mapSpy3Selected = False
            call audioConfirmationAlex from _call_audioConfirmationAlex_9
        elif True:
            "Your spies nanobot levels are too low for this. Visit the STATUS screen to decide how much or how little they should focus on suppressing them."
    jump worldmap

label acesMapSelect:
    if mapSpy1Selected == False and mapSpy2Selected == False and mapSpy3Selected == False:
        "No spy selected."
        jump worldmap
    if mapSpy1Selected:

        if task16Stage == 0 and task15Stage >= 3 and acesRep >= 18:
            menu:
                "{color=#EFD66D}'Final Ace up our sleeve'{/color}" if True:
                    jump task16
                "Send undercover" if True:
                    pass
        if task3Stage == 1 and spyYellowActive == True:
            menu:
                "{color=#EFD66D}'Party in Spain'{/color}" if True:
                    jump task3
                "Send undercover" if True:
                    pass
        if task19Stage == 0 and acesRank == 1 and acesRep >= 4:
            menu:
                "{color=#EFD66D}'Introducing the Aces'{/color}" if True:
                    jump task19
                "Send undercover" if True:
                    pass
        if task6Stage == 0 and acesRank >= 2 and acesRep >= 9:
            menu:
                "{color=#EFD66D}'A Foot in the Door'{/color}" if True:
                    jump task6
                "Send undercover" if True:
                    pass
        if task6Stage == 4 and acesRank >= 2 and acesRep >= 18:
            menu:
                "{color=#EFD66D}'A Foot in the Door'{/color}" if True:
                    jump task6
                "Send undercover" if True:
                    pass
        if task6Stage == 6 and acesRank >= 3 and acesRep >= 9:
            menu:
                "{color=#EFD66D}'A Foot in the Door'{/color}" if True:
                    jump task6
                "Send undercover" if True:
                    pass
        if task6Stage == 9 and acesRank >= 3 and acesRep >= 18 and specialMelodyStatus == 1 and specialDragonStatus >= 2 and specialMuffyStatus >= 2:
            menu:
                "{color=#EFD66D}'A Foot in the Door'{/color}" if True:
                    jump task6
                "Send undercover" if True:
                    pass
        if task15Stage == 0 and acesRep >= 9 and acesRank >= 4:
            menu:
                "{color=#EFD66D}'Party till you drop'{/color}" if True:
                    jump task15
                "Send undercover" if True:
                    pass
        if samMood <= 25:
            "Sam's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Sam to work against her will."
                "Never mind" if True:
                    $ mapSpy1Selected = False
                    jump worldmap
        s "On my way!"
        if mapSpy1Selected == True:
            $ spy1Status = 1

            if samSupLvl == 1:
                $ samMood -= 3
            if samSupLvl == 2:
                $ samMood -= 5
            if samSupLvl == 3:
                $ samMood -= 7

            $ randomJobCallSpy = 1
            call randomJobCall from _call_randomJobCall
            $ mapSpy1Selected = False
            $ greenDayJob = 1
            call audioConfirmationSam from _call_audioConfirmationSam_3
            jump worldmap
    if mapSpy2Selected:
        if cloverMood <= 25:
            "Clover's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Clover to work against her will."
                "Never mind" if True:
                    $ mapSpy2Selected = False
                    jump worldmap

        c "Understood!"
        if mapSpy2Selected == True:
            $ spy2Status = 1

            if cloverSupLvl == 1:
                $ cloverMood -= 3
            if cloverSupLvl == 2:
                $ cloverMood -= 5
            if cloverSupLvl == 3:
                $ cloverMood -= 7

            $ randomJobCallSpy = 2
            call randomJobCall from _call_randomJobCall_1
            $ mapSpy2Selected = False
            $ redDayJob = 1
            call audioConfirmationClover from _call_audioConfirmationClover
            jump worldmap
    if mapSpy3Selected:
        if alexMood <= 25:
            "Alex's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Alex to work against her will."
                "Never mind" if True:
                    $ mapSpy3Selected = False
                    jump worldmap

        aM "You got it!"
        if mapSpy3Selected == True:
            $ spy3Status = 1

            if alexSupLvl == 1:
                $ alexMood -= 3
            if alexSupLvl == 2:
                $ alexMood -= 5
            if alexSupLvl == 3:
                $ alexMood -= 7

            $ randomJobCallSpy = 3
            call randomJobCall from _call_randomJobCall_2
            $ mapSpy3Selected = False
            $ yellowDayJob = 1
            call audioConfirmationAlex from _call_audioConfirmationAlex
            jump worldmap

label punkMapSelect:
    if mapSpy1Selected == False and mapSpy2Selected == False and mapSpy3Selected == False:
        "No spy selected."
        jump worldmap
    if mapSpy1Selected:

        if samMood <= 25:
            "Sam's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Sam to work against her will."
                "Never mind" if True:
                    $ mapSpy1Selected = False
                    jump worldmap
        sM "Going incognito!"
        if mapSpy1Selected == True:
            $ spy1Status = 1

            if samSupLvl == 1:
                $ samMood -= 3
            if samSupLvl == 2:
                $ samMood -= 5
            if samSupLvl == 3:
                $ samMood -= 7

            $ randomJobCallSpy = 1
            call randomJobCall from _call_randomJobCall_3
            $ mapSpy1Selected = False
            $ greenDayJob = 2
            call audioConfirmationSam from _call_audioConfirmationSam_10
            jump worldmap
    if mapSpy2Selected:
        if punkRank >= 1 and punkRep >= 5 and task9Stage == 0:
            menu:
                "{color=#EFD66D}'Living in a database'{/color}" if True:
                    jump task9
                "Send undercover" if True:
                    pass
        if punkRank >= 1 and punkRep >= 18 and task10Stage == 0 and task3Stage >= 7 and spyYellowActive:
            menu:
                "{color=#EFD66D}'Living in a database'{/color}" if True:
                    jump task10
                "Send undercover" if True:
                    pass
        if punkRank >= 2 and punkRep >= 8 and task10Stage == 0 and task3Stage >= 7:
            menu:
                "{color=#EFD66D}'Living in a database'{/color}" if True:
                    jump task10
                "Send undercover" if True:
                    pass
        if task17Stage == 7 and punkRank >= 2 and punkRep >= 4 and task24Stage == 0:
            menu:
                "{color=#EFD66D}'Clover the nerd'{/color}" if True:
                    jump task24
                "Send undercover" if True:
                    pass
        if punkRank >= 2 and punkRep >= 18 and task17Stage == 7 and task18Stage == 0 and specialTaliaStatus == 1:
            menu:
                "{color=#EFD66D}'Nourishing Beats...'{/color}" if True:
                    jump task18
                "Never mind" if True:
                    jump worldmap
        if punkRank >= 3 and punkRep >= 4 and task23Stage == 0 and task24Stage == 0:
            menu:
                "{color=#EFD66D}'Clover the nerd'{/color}" if True:
                    jump task24
                "Never mind" if True:
                    jump worldmap
        if punkRank >= 3 and punkRep >= 18 and task23Stage == 0 and specialSebStatus == 1:
            menu:
                "{color=#EFD66D}'God is a DJ'{/color}" if True:
                    jump task23
                "Never mind" if True:
                    jump worldmap
        if task17Stage == 6:
            menu:
                "{color=#EFD66D}'Animo...'{/color}" if True:
                    jump task17
                "Never mind" if True:
                    jump worldmap
        if punkRank >= 2 and punkRep >= 11 and task17Stage == 0 and task3Stage >= 7:
            menu:
                "{color=#EFD66D}'Animo...'{/color}" if True:
                    jump task17
                "Send undercover" if True:
                    pass

        if cloverMood <= 25:
            "Clover's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Clover to work against her will."
                "Never mind" if True:
                    $ mapSpy2Selected = False
                    jump worldmap

        cM "Let's do crime the scientific way!"
        if mapSpy2Selected == True:
            $ spy2Status = 1

            if cloverSupLvl == 1:
                $ cloverMood -= 3
            if cloverSupLvl == 2:
                $ cloverMood -= 5
            if cloverSupLvl == 3:
                $ cloverMood -= 7

            $ randomJobCallSpy = 2
            call randomJobCall from _call_randomJobCall_4
            $ mapSpy2Selected = False
            $ redDayJob = 2
            call audioConfirmationClover from _call_audioConfirmationClover_11
            jump worldmap
    if mapSpy3Selected:
        if alexMood <= 25:
            "Alex's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Alex to work against her will."
                "Never mind" if True:
                    $ mapSpy3Selected = False
                    jump worldmap

        aM "Books check. Beats double check!"
        if mapSpy3Selected == True:
            $ spy3Status = 1

            if alexSupLvl == 1:
                $ alexMood -= 3
            if alexSupLvl == 2:
                $ alexMood -= 5
            if alexSupLvl == 3:
                $ alexMood -= 7

            $ randomJobCallSpy = 3
            call randomJobCall from _call_randomJobCall_5
            $ mapSpy3Selected = False
            $ yellowDayJob = 2
            call audioConfirmationAlex from _call_audioConfirmationAlex_10
            jump worldmap

label harbingerMapSelect:
    if mapSpy1Selected == False and mapSpy2Selected == False and mapSpy3Selected == False:
        "No spy selected."
        jump worldmap
    if mapSpy1Selected:
        if samMood <= 25:
            "Sam's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Sam to work against her will."
                "Never mind" if True:
                    $ mapSpy1Selected = False
                    jump worldmap
        s "Bring out the spray paints!"
        if mapSpy1Selected == True:
            $ spy1Status = 1

            if samSupLvl == 1:
                $ samMood -= 3
            if samSupLvl == 2:
                $ samMood -= 5
            if samSupLvl == 3:
                $ samMood -= 7

            $ randomJobCallSpy = 1
            call randomJobCall from _call_randomJobCall_6
            $ mapSpy1Selected = False
            $ greenDayJob = 3
            call audioConfirmationSam from _call_audioConfirmationSam_11
            jump worldmap
    if mapSpy2Selected:
        if cloverMood <= 25:
            "Clover's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Clover to work against her will."
                "Never mind" if True:
                    $ mapSpy2Selected = False
                    jump worldmap

        cM "Bustin' some heads!"
        if mapSpy2Selected == True:
            $ spy2Status = 1

            if cloverSupLvl == 1:
                $ cloverMood -= 3
            if cloverSupLvl == 2:
                $ cloverMood -= 5
            if cloverSupLvl == 3:
                $ cloverMood -= 7

            $ randomJobCallSpy = 2
            call randomJobCall from _call_randomJobCall_7
            $ mapSpy2Selected = False
            $ redDayJob = 3
            call audioConfirmationClover from _call_audioConfirmationClover_12
            jump worldmap
    if mapSpy3Selected:
        if outsideRank >= 2 and outsideRep >= 18 and task21Stage == 0 and specialFelicityStatus == 1:
            menu:
                "{color=#EFD66D}'Pink is the New Black'{/color}" if True:
                    jump task21
                "Send undercover" if True:
                    pass
        if outsideRank >= 2 and outsideRep >= 9 and task20Stage == 0:
            menu:
                "{color=#EFD66D}'Teenage Angst'{/color}" if True:
                    jump task20
                "Send undercover" if True:
                    pass
        if outsideRank >= 1 and outsideRep >= 6 and task11Stage == 0:
            menu:
                "{color=#EFD66D}'Anarchy Alex'{/color}" if True:
                    jump task11
                "Send undercover" if True:
                    pass
        if outsideRank >= 1 and outsideRep >= 18 and task11Stage == 2:
            menu:
                "{color=#EFD66D}'Anarchy Alex'{/color}" if True:
                    jump task11
                "Send undercover" if True:
                    pass
        if outsideRank >= 3 and outsideRep >= 18 and task25Stage == 0 and specialKandStatus == 1:
            menu:
                "{color=#EFD66D}'The Gathering of Magic'{/color}" if True:
                    jump task25
                "Send undercover" if True:
                    pass
        if outsideRank >= 3 and outsideRep >= 18 and 2 <= task25Stage <= 8 and specialKandStatus == 1:
            menu:
                "{color=#EFD66D}'The Gathering of Magic'{/color}" if True:
                    jump task25
                "Send undercover" if True:
                    pass
        if alexMood <= 25:
            "Alex's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Alex to work against her will."
                "Never mind" if True:
                    $ mapSpy3Selected = False
                    jump worldmap

        aM "Ima bust out my skateboard for this one!"
        if mapSpy3Selected == True:
            $ spy3Status = 1

            if alexSupLvl == 1:
                $ alexMood -= 3
            if alexSupLvl == 2:
                $ alexMood -= 5
            if alexSupLvl == 3:
                $ alexMood -= 7

            $ randomJobCallSpy = 3
            call randomJobCall from _call_randomJobCall_8
            $ mapSpy3Selected = False
            $ yellowDayJob = 3
            call audioConfirmationAlex from _call_audioConfirmationAlex_11
            if task21Stage == 2:
                jump task21
            jump worldmap

label epinesMapSelect:
    if mapSpy1Selected == False and mapSpy2Selected == False and mapSpy3Selected == False:
        "No spy selected."
        jump worldmap
    if mapSpy1Selected:
        if samMood <= 25:
            "Sam's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Sam to work against her will."
                "Never mind" if True:
                    $ mapSpy1Selected = False
                    jump worldmap
        sM "Time to smell the roses."
        if mapSpy1Selected == True:
            $ spy1Status = 1

            if samSupLvl == 1:
                $ samMood -= 3
            if samSupLvl == 2:
                $ samMood -= 5
            if samSupLvl == 3:
                $ samMood -= 7

            $ mapSpy1Selected = False
            $ greenDayJob = 5
            call audioConfirmationSam from _call_audioConfirmationSam_12
            jump worldmap
    if mapSpy2Selected:
        if cloverMood <= 25:
            "Clover's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Clover to work against her will."
                "Never mind" if True:
                    $ mapSpy2Selected = False
                    jump worldmap

        cM "Time to bloom!"
        if mapSpy2Selected == True:
            $ spy2Status = 1

            if cloverSupLvl == 1:
                $ cloverMood -= 3
            if cloverSupLvl == 2:
                $ cloverMood -= 5
            if cloverSupLvl == 3:
                $ cloverMood -= 7

            $ mapSpy2Selected = False
            $ redDayJob = 5
            call audioConfirmationClover from _call_audioConfirmationClover_13
            jump worldmap
    if mapSpy3Selected:
        if alexMood <= 25:
            "Alex's morale is low and she refuses to work."
            menu:
                "Order her (-karma)" if True:
                    $ playerKarma -= 1
                    "You order Alex to work against her will."
                "Never mind" if True:
                    $ mapSpy3Selected = False
                    jump worldmap

        aM "Let's do some buzzing around."
        if mapSpy3Selected == True:
            $ spy3Status = 1

            if alexSupLvl == 1:
                $ alexMood -= 3
            if alexSupLvl == 2:
                $ alexMood -= 5
            if alexSupLvl == 3:
                $ alexMood -= 7

            $ mapSpy3Selected = False
            $ yellowDayJob = 5
            call audioConfirmationAlex from _call_audioConfirmationAlex_12
            jump worldmap


label finaleMapSelect:
    if 1 <= searchTarget <= 4:
        if mapSpy4Selected:
            brit "On my way!"
            $ spy4Status = 1

            $ mapSpy4Selected = False
            jump worldmap
        if mapSpy5Selected:
            kim "Let's have a look around..."
            $ spy5Status = 1

            $ mapSpy5Selected = False
            jump worldmap
        if mapSpy6Selected:
            sil "Peek-a-boo, anyone in zhere...?"
            $ spy6Status = 1

            $ mapSpy6Selected = False
            jump worldmap
        if mapSpy0Selected:
            O5O "DOING AS I'M TOLD!"
            $ spy0Status = 1

            $ mapSpy0Selected = False
            jump worldmap

    $ mapSpy0Selected = False
    $ mapSpy4Selected = False
    $ mapSpy5Selected = False
    $ mapSpy6Selected = False
    $ searchTarget = 0
    call screen mapButtonsRaidFinale





default hackProgress = 0


default vibUpgrade = False
default droneUpgrade = False
default wormUpgrade = False
default flashUpgrade = False
default infraUpgrade = False
default deployUpgrade = False

label hacker:
    $ mathVisit = True
    if mapSpy1Selected and task2Stage >= 12.5:
        if under4Sam or under5Sam or under6Sam:

            sM "Off I go then."
            $ greenOutfit = 0
            $ greenOutfitArms = 0
            $ greenTop = 0
            $ greenBottom = 0
            $ greenShoes = 0
            $ greenNeck = 0
            $ greenHat = 0
            if under4Sam:
                $ greenUnder = 4
            if under5Sam:
                $ greenUnder = 5
            if under6Sam:
                $ greenUnder = 6
            $ greenDayJob = 99
            $ spy1Status = 1
            $ mapSpy1Selected = False
            $ greenDayJob = 99
            call audioConfirmationSam from _call_audioConfirmationSam_8
            jump worldmap
        elif True:
            y "I don't have a swimsuit for her to wear."
            jump worldmap
    if mapSpy2Selected and task2Stage >= 12.5:
        if under4Clover or under5Clover or under6Clover:

            cM "I can't believe I'm going out like this...!"
            $ redOutfit = 0
            $ redOutfitArms = 0
            $ redTop = 0
            $ redBottom = 0
            $ redShoes = 0
            $ redNeck = 0
            $ redHat = 0
            if under4Clover:
                $ redUnder = 4
            if under5Clover:
                $ redUnder = 5
            if under6Clover:
                $ redUnder = 6
            $ redDayJob = 99
            $ spy2Status = 1
            $ mapSpy2Selected = False
            $ redDayJob = 99
            call audioConfirmationClover from _call_audioConfirmationClover_8
            jump worldmap
    if mapSpy3Selected and task2Stage >= 12.5:
        if under4Alex or under5Alex or under6Alex:

            aM "I'm going to the beach!{w} No wait, I'm going to Mathias!"
            $ yellowOutfit = 0
            $ yellowOutfitArms = 0
            $ yellowTop = 0
            $ yellowBottom = 0
            $ yellowShoes = 0
            $ yellowNeck = 0
            $ yellowHat = 0
            if under4Alex:
                $ yellowUnder = 4
            if under5Alex:
                $ yellowUnder = 5
            if under6Alex:
                $ yellowUnder = 6
            $ yellowDayJob = 99
            $ spy3Status = 1
            $ mapSpy3Selected = False
            $ yellowDayJob = 99
            call audioConfirmationAlex from _call_audioConfirmationAlex_14
            jump worldmap
        elif True:
            y "I don't have a swimsuit for her to wear."
            jump worldmap
    if mapSpy2Selected and task2Stage >= 12.5:
        if under6Clover or under7Clover or under8Clover:

            cM "Off I go then."
            $ redOutfit = 0
            $ redOutfitArms = 0
            $ redTop = 0
            $ redBottom = 0
            $ redShoes = 0
            $ redNeck = 0
            $ redHat = 0
            if under6Clover:
                $ redUnder = 6
            if under7Clover:
                $ redUnder = 7
            if under8Clover:
                $ redUnder = 8
            $ redDayJob = 99
            $ spy2Status = 1
            $ mapSpy2Selected = False
            $ redDayJob = 99
            call audioConfirmationClover from _call_audioConfirmationClover_5
            jump worldmap
        elif True:
            "I don't have a swimsuit for her to wear."
            jump worldmap
    if mapSpy3Selected and task2Stage >= 12.5:
        if under6Alex or under7Alex or under8Alex:

            $ yellowOutfit = 0
            $ yellowOutfitArms = 0
            $ yellowTop = 0
            $ yellowBottom = 0
            $ yellowShoes = 0
            $ yellowNeck = 0
            $ yellowHat = 0
            if under6Alex:
                $ yellowUnder = 6
            if under7Alex:
                $ yellowUnder = 7
            if under8Alex:
                $ yellowUnder = 8
            $ yellowDayJob = 99
            aM "Off I go then."
            $ spy3Status = 1
            $ mapSpy3Selected = False
            $ yellowDayJob = 99
            call audioConfirmationAlex from _call_audioConfirmationAlex_3
            jump worldmap
        elif True:
            "I don't have a swimsuit for her to wear."
            jump worldmap
    elif True:
        show scene_darkening
        with d3
        show matModel at ri with d3
        label hackSkipIntro:
            pass
        menu:
            "{color=#EFD66D}'Build-A-Bar'{/color}" if task32Stage == 1 and task32Mat == False:
                $ task32Mat = True
                y "Hey Mathias. Can you help me out?"
                mat "Of course. What do you need?"
                y "I'm trying to get a message out there. Talking about Beverly Hills hottest new stripclub."
                mat "New stripclub...?{w} Wait... don't tell me you're opening one."
                y "Sure am. Can you spread the word a bit?"
                mat "I could...."
                y "You get a free membership to the club."
                mat "Deal!"
                hide matModel
                with d3
                hide scene_darkening
                with d3
                pause 0.5
                y "(That takes care of the advertisement...)"
                jump worldmap
            "{color=#EFD66D}'Double Trouble'{/color}" if task2Stage == 11:
                jump task2
            "Decrypting Process: [hackProgress]%%" if gadgetJetpackActive == False:
                if hackProgress <= 25:
                    mat "Nothing new to report. Decrypting is going as planned."
                    jump hackSkipIntro
                if 26 <= hackProgress <= 75:
                    mat "I've started making progress, but it will take some time until I got anything new for ya."
                    jump hackSkipIntro
                if 76 <= hackProgress <= 99:
                    mat "I'm getting closer to decrypting the next gadget. Check back soon."
                    jump hackSkipIntro
                elif True:
                    show scene_darkening
                    with d3
                    show matModel
                    with d3
                    $ hackProgress = 0
                    $ task2Text = "Discussing the situation, it's become clear that we could use the extra backup to take back Beverly Hills. I should set up a mission and send my spy back to school to capture her friend. \n\n-We brought back a new spy, but the nanobot control seems to be getting worse. I should check my crafting table to see if there's something in WOOHP's database about that.\n\n-I met someone who can hack into the network, but it will take time. I could speed things up by convincing one of my spies to wear a bikini and visit Mathias.\n\n-Craft the V.I.B. via de gadget screen."
                    mat "Good news, my dude. I managed to crack a blueprint inside the database."
                    if task2Stage <= 12.5 and spyRedActive == True:
                        $ task2Stage = 12.6
                    if craftEquip1 != "V.I.B.":
                        if spyRedActive == False:
                            $ hackProgress = 100
                            y "Awesome! What is it?"
                            mat "Erm..."
                            y "Well?"
                            mat "Now where did I keep that USB..."
                            y "....................."
                            mat "Okay... I may have misplaced it for a moment..."
                            y "What?!"
                            mat "Don't panic, I'm sure I'll find it again, come back later and I'll have it for you."
                            y ".........................."
                            hide scene_darkening
                            hide matModel
                            with d2
                            show scene_fighting
                            with d3
                            y "Maybe I should focus on freeing another spy before coming back to Mathias."
                            hide scene_fighting
                            with d3
                            jump worldmap
                        $ craftEquip1 = "V.I.B."
                        mat "It's equipment. Something called the V.I.B. check your crafting bench to make it."
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if gadgetPowderActive == False:
                        $ gadgetPowderActive = True
                        mat "It's a gadget this time. Some sort of distraction powder bomb."
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if craftEquip2 != "Hacking Tool":
                        mat "Looks like some sort of Hacking Tool. Check your craftingbench to begin construction."
                        $ craftEquip2 = "Hacking Tool"
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if gadgetFlashbangBeltActive == False:
                        $ gadgetFlashbangBeltActive = True
                        mat "It's a gadget this time. A flashbang belt that can disorientate enemies."
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if craftEquip3 != "Cyber Infiltration Glasses":
                        mat "Looks like some sort of Infrared Glasses. Check your craftingbench to begin construction."
                        $ craftEquip3 = "Cyber Infiltration Glasses"
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if gadgetDroneActive == False:
                        $ gadgetDroneActive = True
                        mat "It's a gadget this time. A remote controlled drone with a camera. You can use this to see if there are enemies inside a room before you enter."
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if craftEquip4 != "Multitool Revolver":
                        mat "Looks like some sort of Non-leathal gun. Check your craftingbench to begin construction."
                        $ craftEquip4 = "Multitool Revolver"
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if gadgetAfroDartActive == False:
                        $ gadgetAfroDartActive = True
                        $ gadgetStunDartActive = True
                        mat "You're in luck, it's two gadgets this time that go with the Multitool Revolver. The afrodisiac dart makes the target more susceptible to charming and the poison dart disorientates enemies. Making blocking their attacks easier."
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if craftEquip5 != "Grappling Hook":
                        mat "Looks like some sort of Grappling Hook. Check your craftingbench to begin construction."
                        $ craftEquip5 = "Grappling Hook"
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if gadgetStealthActive == False:
                        $ gadgetStealthActive = True
                        mat "It's a gadget this time. It's a stealth bracelet that makes you fade into the background. It's not perfect, but will probably lower your detection rating if you spy gets caught during a mission."
                        mat "If you need any materials to craft it, stop by, all right?"
                        jump hackSkipIntro
                    if gadgetJetpackActive == False:
                        $ gadgetJetpackActive = True
                        mat "It's a gadget this time. A really cool one, it's a jetpack! Use it during missions to fly and skip a few floors."
                        mat "If you need any materials to craft it, stop by, all right?"
                        pause 1.0
                        mat "Looks like those are all the available items in the database, but er... Feel free to keep sending your girls by to model for me, and I'll pay you money!"
                        y "Gotten used to the glamerous lifestyle, eh?"
                        mat "Yeah...."
                        jump hackSkipIntro
                    jump hackSkipIntro
                jump hackSkipIntro
            "Gadget upgrades" if True:
                label gadgetUpgrade:
                    pass
                menu:
                    "Bondage Bug" if vibUpgrade == False and gadgetVIBActive:
                        "Upgrade your V.I.B. to avoid your spies making any sound to give away their position."
                        menu:
                            "Develop the upgrade ($1000)" if True:
                                if cash >= 1000:
                                    $ cash -= 1000
                                    $ vibUpgrade = True
                                    play sound "audio/sfx/itemGot.mp3"
                                    "You develop a new upgrade for your V.I.B.!"
                                    "When using the V.I.B. during missions you no longer alert guards."
                                    jump hacker
                                elif True:
                                    y "I don't have enough money to develop this upgrade."
                                    jump hacker
                            "Back" if True:
                                jump hacker
                    "Hacking worm" if wormUpgrade == False and craftEquip2 == "Hacking Tool":
                        "Upgrade your hacking tool to make hacking easier."
                        menu:
                            "Develop the upgrade ($2000)" if True:
                                if cash >= 2000:
                                    $ cash -= 2000
                                    $ wormUpgrade = True
                                    play sound "audio/sfx/itemGot.mp3"
                                    "You develop a new upgrade for your Hacking Tool!"
                                    "Your Hacking Tool has a higher chance of being succesful during missions."
                                    jump hacker
                                elif True:
                                    y "I don't have enough money to develop this upgrade."
                                    jump hacker
                            "Back" if True:
                                jump hacker
                    "Flash BANG Belt" if flashUpgrade == False and gadgetFlashbangBeltActive:
                        "Upgrade your Flashbang Belt and give it a small chance to instantly defeat agents, instead of just stunning them."
                        menu:
                            "Develop the upgrade ($1.000)" if True:
                                if cash <= 999:
                                    "Not enough money."
                                    jump hacker
                                elif True:
                                    $ cash -= 1000
                                    $ flashUpgrade = True
                                    play sound "audio/sfx/itemGot.mp3"
                                    "Upgrade developed!"
                                jump hacker
                            "Back" if True:
                                jump hacker
                    "Explosive Drone" if droneUpgrade == False and gadgetDroneActive:
                        "Upgrade your AC Drones. They can now be send ahead into a room to take out an enemy, but raising the enemy's Alert Status."
                        menu:
                            "Develop the upgrade ($1.500)" if True:
                                if cash >= 1500:
                                    $ cash -= 1500
                                    $ droneUpgrade = True
                                    play sound "audio/sfx/itemGot.mp3"
                                    "You develop a new upgrade for your AC Drones!"
                                    "Drones can now explode on command to take out agents."
                                    jump hacker
                                elif True:
                                    y "I don't have enough money to develop this upgrade."
                                    jump hacker
                            "Back" if True:
                                jump hacker
                    "Back" if True:
                        jump hacker
            "Buy Materials" if True:
                label hackSkipShop:
                    pass
                menu:
                    "Buy Hydrofluoric Acid ([matsAcid])" if True:
                        menu:
                            "Buy one Hydrofluoric Acid ($140)" if True:
                                if cash <= 139:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 140
                                    $ matsAcid += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy two Hydrofluoric Acid ($280)" if True:
                                if cash <= 279:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 280
                                    $ matsAcid += 2
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy three Hydrofluoric Acid ($420)" if True:
                                if cash <= 419:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 420
                                    $ matsAcid += 3
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy ten Hydrofluoric Acid ($1400)" if True:
                                if cash <= 1390:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 1400
                                    $ matsAcid += 10
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Never mind" if True:
                                jump hackSkipShop
                    "Buy Computer Chip ([matsChip])" if True:
                        menu:
                            "Buy one Computer Chip ($120)" if True:
                                if cash <= 119:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 120
                                    $ matsChip += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy two Computer Chip ($240)" if True:
                                if cash <= 239:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 240
                                    $ matsChip += 2
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy three Computer Chip ($360)" if True:
                                if cash <= 359:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 360
                                    $ matsChip += 3
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy ten Computer Chip ($1200)" if True:
                                if cash <= 1190:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 1200
                                    $ matsChip += 10
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Never mind" if True:
                                jump hackSkipShop
                    "Buy Saltpeter ([matsDust])" if True:
                        menu:
                            "Buy one Saltpeter ($70)" if True:
                                if cash <= 69:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 70
                                    $ matsDust += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy two Saltpeter ($140)" if True:
                                if cash <= 139:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 140
                                    $ matsDust += 2
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy three Saltpeter ($210)" if True:
                                if cash <= 209:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 210
                                    $ matsDust += 3
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy ten Saltpeter ($700)" if True:
                                if cash <= 690:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 700
                                    $ matsDust += 10
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Never mind" if True:
                                jump hackSkipShop
                    "Buy Cooling Agent ([matsGlue])" if True:
                        menu:
                            "Buy one Cooling Agent ($80)" if True:
                                if cash <= 79:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 80
                                    $ matsGlue += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy two Cooling Agent ($160)" if True:
                                if cash <= 159:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 160
                                    $ matsGlue += 2
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy three Cooling Agent ($240)" if True:
                                if cash <= 239:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 240
                                    $ matsGlue += 3
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy ten Cooling Agent ($800)" if True:
                                if cash <= 790:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 800
                                    $ matsGlue += 10
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Never mind" if True:
                                jump hackSkipShop
                    "Buy Valuables ([matsValu])" if True:
                        menu:
                            "Buy one Valuables ($200)" if True:
                                if cash <= 199:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 200
                                    $ matsValu += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy two Valuables ($400)" if True:
                                if cash <= 399:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 400
                                    $ matsValu += 2
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy three Valuables ($600)" if True:
                                if cash <= 599:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 600
                                    $ matsValu += 3
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy ten Valuables ($2000)" if True:
                                if cash <= 1999:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 2000
                                    $ matsValu += 10
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Never mind" if True:
                                jump hackSkipShop
                    "Buy Wiring Kit ([matsWires])" if True:
                        menu:
                            "Buy one Wiring Kit ($40)" if True:
                                if cash <= 39:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 40
                                    $ matsWires += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy two Wiring Kits ($80)" if True:
                                if cash <= 79:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 120
                                    $ matsWires += 3
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy three Wiring Kits ($120)" if True:
                                if cash <= 119:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 120
                                    $ matsWires += 3
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Buy ten Wiring Kit ($400)" if True:
                                if cash <= 390:
                                    y "I don't have enough money for this."
                                    jump hackSkipShop
                                elif True:
                                    $ cash -= 400
                                    $ matsWires += 10
                                    play sound "audio/sfx/cashRegister.mp3"
                                    jump hackSkipShop
                            "Never mind" if True:
                                jump hackSkipShop

                        show screen gadgetButtons
                        call screen deskToolsInterface
                    "Never mind" if True:
                        if tod == 1 and mathVisit == True:
                            jump hackSkipIntro
                        if mathVisit == False:
                            jump desk
                        elif True:
                            jump desk
            "Back" if True:
                $ mathVisit = False
                hide matModel
                hide scene_darkening
                with d2
                jump worldmap

label statusScreen:
    if mapStatusSelect == False:
        $ mapStatusSelect = True
    elif True:
        $ mapStatusSelect = False
    jump worldmap






default picQuest1 = 0
default picQuest2 = 0
default picQuest3 = 0
default picQuest4 = 0
default picQuest5 = 0
default picQuest6 = 0
default picQuest7 = 0
default picQuest8 = 0
default picQuest9 = 0
default picQuest10 = 0
default picQuest11 = 0
default picQuest12 = 0



screen bookStoreQuests:

    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("mall")

    if 0 <= picQuest1 <= 2:
        add "gui/bkStore/bsQMag.png" xalign 0.22 yalign 0.32
        add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.17 yalign 0.45
        if picQuest1 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.36 yalign 0.42
    if 0 <= picQuest2 <= 2:
        add "gui/bkStore/bsQMeds.png" xalign 0.5 yalign 0.32
        add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.425 yalign 0.45
        if picQuest2 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.6 yalign 0.42
    if 0 <= picQuest3 <= 2:
        add "gui/bkStore/bsQCuffs.png" xalign 0.8 yalign 0.32
        add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.68 yalign 0.45
        if picQuest3 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.84 yalign 0.42
    if 0 <= picQuest4 <= 2:
        add "gui/bkStore/bsQCollar.png" xalign 0.2 yalign 0.72
        add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.17 yalign 0.79
        if picQuest4 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.36 yalign 0.78
    if 0 <= picQuest5 <= 2:
        add "gui/bkStore/bsQGag.png" xalign 0.5 yalign 0.72
        add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.425 yalign 0.79
        if picQuest5 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.6 yalign 0.78
    if 0 <= picQuest6 <= 2:
        add "gui/bkStore/bsQPlug.png" xalign 0.8 yalign 0.72
        add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.68 yalign 0.79
        if picQuest6 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.84 yalign 0.78
    if picQuest1 >= 3 and picQuest2 >= 3 and picQuest3 >= 3 and picQuest4 >= 3 and picQuest5 >= 3 and picQuest6 >= 3:
        if 0 <= picQuest7 <= 2:
            add "gui/bkStore/bsQChains.png" xalign 0.22 yalign 0.32
            add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.17 yalign 0.45
        if picQuest7 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.36 yalign 0.42
        if 0 <= picQuest8 <= 2:
            add "gui/bkStore/bsQSybian.png" xalign 0.5 yalign 0.32
            add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.425 yalign 0.45
        if picQuest8 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.6 yalign 0.42
        if 0 <= picQuest9 <= 2:
            add "gui/bkStore/bsQSpreader.png" xalign 0.8 yalign 0.32
            add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.68 yalign 0.45
        if picQuest9 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.84 yalign 0.42
        if 0 <= picQuest10 <= 2:
            add "gui/bkStore/bsQCG.png" xalign 0.22 yalign 0.73
            add "gui/bkStore/bookstoreRwdGraph.png" xalign 0.17 yalign 0.79
        if picQuest10 == 2:
            add "gui/bkStore/bookstoreQDone.png" xalign 0.36 yalign 0.78

    if picQuest1 == 0:
        vbox xalign 0.345 yalign 0.49:
            imagebutton:
                idle "gui/bookstoreButton.png"
                hover "gui/bookstoreButton-hover.png"
                action Jump("bsQMag")
    if picQuest2 == 0:
        vbox xalign 0.59 yalign 0.49:
            imagebutton:
                idle "gui/bookstoreButton.png"
                hover "gui/bookstoreButton-hover.png"
                action Jump("bsQMeds")
    if picQuest3 == 0:
        vbox xalign 0.84 yalign 0.49:
            imagebutton:
                idle "gui/bookstoreButton.png"
                hover "gui/bookstoreButton-hover.png"
                action Jump("bsQMats")
    if picQuest4 == 0:
        vbox xalign 0.345 yalign 0.83:
            imagebutton:
                idle "gui/bookstoreButton.png"
                hover "gui/bookstoreButton-hover.png"
                action Jump("bsQCollar")
    if picQuest5 == 0:
        vbox xalign 0.59 yalign 0.83:
            imagebutton:
                idle "gui/bookstoreButton.png"
                hover "gui/bookstoreButton-hover.png"
                action Jump("bsQGag")
    if picQuest6 == 0:
        vbox xalign 0.84 yalign 0.83:
            imagebutton:
                idle "gui/bookstoreButton.png"
                hover "gui/bookstoreButton-hover.png"
                action Jump("bsQPlug")
    if picQuest1 >= 3 and picQuest2 >= 3 and picQuest3 >= 3 and picQuest4 >= 3 and picQuest5 >= 3 and picQuest6 >= 3:
        if picQuest7 == 0:
            vbox xalign 0.345 yalign 0.49:
                imagebutton:
                    idle "gui/bookstoreButton.png"
                    hover "gui/bookstoreButton-hover.png"
                    action Jump("bsQHerbs")
        if picQuest8 == 0:
            vbox xalign 0.59 yalign 0.49:
                imagebutton:
                    idle "gui/bookstoreButton.png"
                    hover "gui/bookstoreButton-hover.png"
                    action Jump("bsQCoupons")
        if picQuest9 == 0:
            vbox xalign 0.84 yalign 0.49:
                imagebutton:
                    idle "gui/bookstoreButton.png"
                    hover "gui/bookstoreButton-hover.png"
                    action Jump("bsQSpreader")
        if picQuest10 == 0:
            vbox xalign 0.345 yalign 0.83:
                imagebutton:
                    idle "gui/bookstoreButton.png"
                    hover "gui/bookstoreButton-hover.png"
                    action Jump("bsQCG")

    if picQuest1 == 2:
        vbox xalign 0.345 yalign 0.49:
            imagebutton:
                idle "gui/bookstoreButton2.png"
                hover "gui/bookstoreButton2-hover.png"
                action Jump("bsQMag")
    if picQuest2 == 2:
        vbox xalign 0.59 yalign 0.49:
            imagebutton:
                idle "gui/bookstoreButton2.png"
                hover "gui/bookstoreButton2-hover.png"
                action Jump("bsQMeds")
    if picQuest3 == 2:
        vbox xalign 0.84 yalign 0.49:
            imagebutton:
                idle "gui/bookstoreButton2.png"
                hover "gui/bookstoreButton2-hover.png"
                action Jump("bsQMats")
    if picQuest4 == 2:
        vbox xalign 0.345 yalign 0.83:
            imagebutton:
                idle "gui/bookstoreButton2.png"
                hover "gui/bookstoreButton2-hover.png"
                action Jump("bsQCollar")
    if picQuest5 == 2:
        vbox xalign 0.59 yalign 0.83:
            imagebutton:
                idle "gui/bookstoreButton2.png"
                hover "gui/bookstoreButton2-hover.png"
                action Jump("bsQGag")
    if picQuest6 == 2:
        vbox xalign 0.84 yalign 0.83:
            imagebutton:
                idle "gui/bookstoreButton2.png"
                hover "gui/bookstoreButton2-hover.png"
                action Jump("bsQPlug")
    if picQuest6 >= 3:
        if picQuest7 == 2:
            vbox xalign 0.345 yalign 0.49:
                imagebutton:
                    idle "gui/bookstoreButton2.png"
                    hover "gui/bookstoreButton2-hover.png"
                    action Jump("bsQMag")
        if picQuest8 == 2:
            vbox xalign 0.59 yalign 0.49:
                imagebutton:
                    idle "gui/bookstoreButton2.png"
                    hover "gui/bookstoreButton2-hover.png"
                    action Jump("bsQMeds")
        if picQuest9 == 2:
            vbox xalign 0.84 yalign 0.49:
                imagebutton:
                    idle "gui/bookstoreButton2.png"
                    hover "gui/bookstoreButton2-hover.png"
                    action Jump("bsQMats")
        if picQuest10 == 2:
            vbox xalign 0.345 yalign 0.83:
                imagebutton:
                    idle "gui/bookstoreButton2.png"
                    hover "gui/bookstoreButton2-hover.png"
                    action Jump("bsQCG")
        if picQuest11 == 2:
            vbox xalign 0.59 yalign 0.83:
                imagebutton:
                    idle "gui/bookstoreButton2.png"
                    hover "gui/bookstoreButton2-hover.png"
                    action Jump("bsQGag")
        if picQuest12 == 2:
            vbox xalign 0.84 yalign 0.83:
                imagebutton:
                    idle "gui/bookstoreButton2.png"
                    hover "gui/bookstoreButton2-hover.png"
                    action Jump("bsQPlug")

label bsQMag:
    if picQuest1 == 0:
        $ picQuest1Text = "-Take a picture of any of your spies wearing the milkshake uniform."
        "'Take a picture wearing the Mega Milk uniform.\nReward: 3 porn magazines.'"
        menu:
            "Accept" if True:
                $ picQuest1 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    elif picQuest1 == 2:
        show scene_darkening with d3
        show clerk at ri with d3
        $ picQuest1Text = " "
        $ picQuest1 = 3
        $ magazine += 3
        y "Got a picture for you!"
        $ clerkFace = 3
        "Clerk" "Shhh, not so loud...!"
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}3 magazines{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        jump pictureLabel
label bsQMeds:
    if picQuest2 == 0:
        $ picQuest2Text = "-Take a picture of any of your spies in their underwear."
        "Photo of a girl in her underwear\nReward: Blindfolds."
        menu:
            "Accept" if True:
                $ picQuest2 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    elif picQuest2 == 2:
        $ picQuest2Text = " "
        $ picQuest2 = 3
        $ medkit += 2
        show scene_darkening with d3
        show clerk at ri with d3
        y "Got a new picture for you!"
        $ clerkFace = 3
        "Clerk" "Oh, quickly before my manager hears you!"
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Blindfolds{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        jump pictureLabel
label bsQMats:
    if picQuest3 == 0:
        $ picQuest3Text = "-Take a picture of a topless girl, but keep it sexy."
        "Take a picture of a topless girl, but keep it sexy.\nReward: Fuzzy handcuffs."
        menu:
            "Accept" if True:
                $ picQuest3 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    elif picQuest3 == 2:
        $ picQuest3Text = " "
        $ picQuest3 = 3
        $ matsBoost += 1
        show scene_darkening with d3
        show clerk at ri with d3
        y "Got a new picture for you!"
        $ clerkFace = 3
        "Clerk" "Oh, did you get the..."
        $ clerkBlush = 1
        "Clerk" "O-oh wow..."
        y "Told you I'd get it."
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Handcuffs{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        $ clerkFace = 1
        jump pictureLabel

label bsQCollar:
    if picQuest4 == 0:
        $ picQuest4Text = "-Take a picture of a naked girl, but keep it sexy"
        "Take a picture of a naked girl, but keep it sexy.\nReward: Slave Collars."
        menu:
            "Accept" if True:
                $ picQuest4 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    elif picQuest4 == 2:
        $ picQuest4Text = " "
        $ picQuest4 = 3
        show scene_darkening with d3
        show clerk at ri with d3
        "Clerk" "Oh!!"
        $ clerkBlush = 1
        "Clerk" "H-here, please just take the collars before anyone sees..."
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Slave Collars{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        jump pictureLabel
label bsQGag:
    if picQuest5 == 0:
        $ picQuest5Text = "Take a picture of a girl on full display, baring it all."
        "Take a picture of a girl on full display, baring it all.\nReward: Ballgags."
        menu:
            "Accept" if True:
                $ picQuest5 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    elif picQuest5 == 2:
        $ picQuest5Text = " "
        $ picQuest5 = 3
        $ clerkBlush = 1
        show scene_darkening with d3
        show clerk at ri with d3
        "Clerk" "She really took it all off... Oh wow...."
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Ballgags{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        jump pictureLabel
label bsQPlug:
    if picQuest6 == 0:
        $ picQuest6Text = "-Take a picture of one of your spies using her dildo."
        "Take a picture of one of your spies using her dildo.\nReward: Foxtail Buttplugs."
        menu:
            "Accept" if True:
                $ picQuest6 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    if picQuest6 == 2:
        $ picQuest6Text = " "
        $ picQuest6 = 3
        show scene_darkening with d3
        show clerk at ri with d3
        y "You'll be happy to hear that the girls are putting their dildos to good use."
        $ clerkBlush = 1
        $ clerkFace = 2
        "Clerk" "A-and... they were okay with you photographing them...?"
        "Clerk" "H-here, I got your reward. Please take it with you...!"
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Buttplugs{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        jump pictureLabel

label bsQHerbs:
    if picQuest7 == 0:
        $ picQuest7Text = "-Take a picture of one of your spies preforming foreplay."
        "Take a picture of one of your spies preforming foreplay.\nReward: Bondage Chains."
        menu:
            "Accept" if True:
                $ picQuest7 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    if picQuest7 == 2:
        $ picQuest7Text = " "
        $ picQuest7 = 3
        $ herbHeal += 1
        $ herbAphro += 1
        $ herbWeed += 1
        $ herbMutant += 1
        $ herbGold += 1
        $ herbWhisper += 1
        $ herbRebel += 1
        show scene_darkening with d3
        show clerk at ri with d3
        y "This sexy enough for you, perv?"
        $ clerkBlush = 1
        $ clerkFace = 2
        "clerk" "Oh wow! Thank you for sharing this!"
        "Clerk" "H-here, I got your reward. Please take it with you...!"
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Bondage Chains{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        jump pictureLabel

label bsQCoupons:
    if picQuest8 == 0:
        $ picQuest8Text = "-Take a picture of a spy having sex."
        "Take a picture of a spy having sex.\nReward: Sybian."
        menu:
            "Accept" if True:
                $ picQuest8 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    if picQuest8 == 2:
        $ picQuest8Text = " "
        $ picQuest8 = 3
        $ smoothieCoupon += 3
        show scene_darkening with d3
        show clerk at ri with d3
        y "I'm starting to like these challenges more and more! Here's your picture."
        $ clerkBlush = 1
        $ clerkFace = 2
        "Clerk" "A-and... they were okay with you photographing them...?"
        "Clerk" "H-here, I got your reward. Please take it with you...!"
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Sybian{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        jump pictureLabel

label bsQSpreader:
    if picQuest9 == 0:
        $ picQuest9Text = "-Take a picture of a spy having anal sex."
        "Take a picture of a spy having anal sex.\nReward: Leg Spreader."
        menu:
            "Accept" if True:
                $ picQuest9 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    if picQuest9 == 2:
        $ picQuest9Text = " "
        $ picQuest9 = 3
        $ smoothieCoupon += 3
        show scene_darkening with d3
        show clerk at ri with d3
        y "Well ploughed and delivered."
        $ clerkBlush = 1
        $ clerkFace = 2
        "Clerk" "Oh my God... This is so freaking lewd!"
        "Clerk" "Here's your reward! Please come back soon!"
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Leg Spreader{/color}!"
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        jump pictureLabel

label bsQCG:
    if picQuest10 == 0:
        $ picQuest9Text = "-Take a picture of the spies in a foursome."
        "Take a picture of the spies in a foursome.\nReward: ???."
        menu:
            "Accept" if True:
                $ picQuest10 = 1
                play sound "audio/sfx/miscSound1.mp3"
                jump pictureLabel
            "Decline" if True:
                jump pictureLabel
    if picQuest10 == 2:
        label atmBooks:
            pass
        $ picQuest10Text = " "
        $ picQuest10 = 3
        scene bgMall with fade
        show scene_darkening with d3
        show clerk at ri with d3
        y "There you go, three throughly satisfied girls."
        $ clerkBlush = 1
        $ clerkFace = 2
        "Clerk" "Oh my GOD! This is so hot! I want to be living your life!"
        y "Yeah yeah, so what about my reward?"
        "Clerk" "Well... I don't have anymore sex toys...."
        y "......................."
        "Clerk" "But I hope this will do~..."
        play sound "audio/sfx/itemGot.mp3"
        "You traded a picture for: {color=#ffeda6}Photograph{/color}!"
        hide clerk
        show expression "gui/photos/other/picClerk.jpg":
            xalign 0.5 yalign 0.5
        with d3
        pause
        y "Nice~... One more for my collection."
        hide expression "gui/photos/other/picClerk.jpg"
        show clerk at ri
        with d2
        "Clerk" "Oh... how exciting it must be to live a rich sex life~..."
        y "You know... you're welcome to join us sometime."
        $ clerkBlush = 1
        "Clerk" "Thanks, but I don't think I'm ready for that yet.{w} For now I'm sticking to my romance novels and your dirty pictures."
        y "Fair enough."
        hide scene_darkening
        hide clerk
        with d3
        $ clerkBlush = 0
        jump pictureLabel



layeredimage mallBG:
    always:
        "bgs/bgMall.jpg"
    if month == 2 and day <= 14:
        "bgs/bgMallValentine.jpg"
    if month == 4 and 7 <= day <= 21:
        "bgs/bgMallEaster.jpg"
    if month == 10 and 14 <= day <= 31:
        "bgs/bgMallHalloween.jpg"
    if month == 12 and day >= 14:
        "bgs/bgMallXmas.jpg"

label mall:
    if task14Stage == 0 and daysPlayed >= 981:
        menu:
            "{color=#EFD66D}'Getting Ink Done'{/color}" if True:
                jump task14
            "Visit the mall" if True:
                pass
    if task12Stage == 0 and daysPlayed >= 61 and spyYellowActive:
        menu:
            "{color=#EFD66D}'A few snips away of a haircut'{/color}" if True:
                jump task12
            "Visit the mall" if True:
                pass
    if task12Stage == 4:
        menu:
            "{color=#EFD66D}'A few snips away of a haircut'{/color}" if True:
                jump task12
            "Visit the mall" if True:
                pass
    scene mallBG
    menu:
        "{color=#EFD66D}'Open for Business'{/color}" if tutStage == 9:
            jump tutStage10
        "{color=#EFD66D}'Dingalingaling'{/color}" if task5Stage == 2:
            jump task5
        "{color=#EFD66D}'Dingalingaling'{/color}" if task5Stage == 2.5:
            jump task5

        "Smoothie Stall" if smoothieCoupon >= 1:
            "Exchange a Smoothie Coupon for a random smoothie?"
            menu:
                "Yes" if True:
                    $ smoothieCoupon -= 1
                    "You exchange your coupon and get..."
                    play sound "audio/sfx/itemGot.mp3"
                    $ randSmoo = renpy.random.randint(1, 6)
                    if randSmoo == 1:
                        $ kiwiSmoothie += 1
                        "A kiwi smoothie x1!"
                        jump mall
                    if randSmoo == 2:
                        $ strawSmoothie += 1
                        "A {color=#ffeda6}Strawberry Smoothie{/color} x1!"
                        jump mall
                    if randSmoo == 3:
                        $ bananSmoothie += 1
                        "A {color=#ffeda6}Banana Smoothie{/color} x1!"
                        jump mall
                    if randSmoo == 4:
                        $ orangeSmoothie += 1
                        "An {color=#ffeda6}Orange Smoothie{/color} x1!"
                        jump mall
                    if randSmoo == 5:
                        $ pinkSmoothie += 1
                        "A {color=#ffeda6}Dragon Fruit Smoothie{/color} x1!"
                        jump mall
                    if randSmoo == 6:
                        $ avocSmoothie += 1
                        "A {color=#ffeda6}Avocado Smoothie{/color} x1!"
                        jump mall
                "Never mind" if True:
                    jump mall
        "Santa's Crib" if month == 12 and day >= 14:
            call screen xmasOutfitShop
        "Bookstore" if True:
            show scene_darkening with d3
            $ clerkFace = 1
            show clerk at ri with d3
            label bookstore:
                menu:
                    "Shop" if True:
                        label bookstoreShop:
                            pass
                        menu:
                            "Porn Game" if otActive == False and 2 <= task13Stage <= 2.1:
                                $ otActive = True
                                y "........................."
                                "Clerk" "........................."
                                y "So you're telling me this game is called Orange Trainer..."
                                "Clerk" "........................"
                                y "And it's about training alien girls to have sex...?"
                                $ clerkFace = 2
                                "Clerk" "Listen, it's been on the shelves for ages. You can have it for free if you want. Just don't question it."
                                y "Works for me!"
                                play sound "audio/sfx/itemGot.mp3"
                                "You bought {color=#ffeda6}Orange Trainer{/color}."
                                jump bookstoreShop
                            "Medkit ($25)" if True:
                                if cash >= 25:
                                    $ cash -= 25
                                    $ medkit += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    "Bought 1 {color=#ffeda6}Medkit{/color}."
                                    if playerKarma >= 60:
                                        $ karmaCash = renpy.random.randint(1,4)
                                        if karmaCash == 1:
                                            $ medkit += 1
                                            play sound "audio/sfx/itemGot.mp3"
                                            "The bookstore clerk throws in an extra {color=#ffeda6}Medkit{/color} for free.{w} Good karma all the way!"
                                    jump bookstoreShop
                                elif True:
                                    y "I don't have enough money."
                                    jump bookstoreShop
                            "Porn Magazine ($25)" if True:
                                if cash >= 25:
                                    $ cash -= 25
                                    $ magazine += 1
                                    play sound "audio/sfx/cashRegister.mp3"
                                    "Bought 1 {color=#ffeda6}Dirty Magazine{/color}."
                                    if playerKarma >= 60:
                                        $ karmaCash = renpy.random.randint(1,4)
                                        if karmaCash == 1:
                                            $ magazine += 1
                                            play sound "audio/sfx/itemGot.mp3"
                                            "The bookstore clerk throws in an extra {color=#ffeda6}Dirty Magazine{/color} for free.{w} Good karma all the way!"
                                    jump bookstoreShop
                                elif True:
                                    y "I don't have enough money."
                                    jump bookstoreShop
                            "Back" if True:
                                jump bookstore
                    "Pictures" if task5Stage >= 3:
                        label pictureLabel:
                            pass
                        scene bgBookstore
                        call screen bookStoreQuests
                    "Back" if True:
                        hide scene_darkening
                        hide clerk
                        with d3
                        jump mall
        "Threads" if True:
            $ menuSelect = 1
            scene bgShops
            if firstPick == 1:
                $ shopSpyName = "Sam"
                $ shopCurrentSpy = 1
                show green g1:
                    xalign 1.0 yalign -0.7
            if firstPick == 2:
                $ shopSpyName = "Clover"
                $ shopCurrentSpy = 2
                show red r1:
                    xalign 1.0 yalign -0.7
            if firstPick == 3:
                $ shopSpyName = "Alex"
                $ shopCurrentSpy = 3
                show yellow y1:
                    xalign 1.0 yalign -0.7
            $ greenUnder = 1
            $ redUnder = 1
            $ yellowUnder = 1
            call screen bgShop1
            jump mall
        "Ho-Style" if True:
            $ menuSelect = 2
            $ greenHat = 0
            $ redHat = 0
            $ yellowHat = 0
            scene bgShops
            if firstPick == 1:
                $ shopSpyName = "Sam"
                $ shopCurrentSpy = 1
                show green g1:
                    xalign 1.0 yalign -0.7
            if firstPick == 2:
                $ shopSpyName = "Clover"
                $ shopCurrentSpy = 2
                show red r1:
                    xalign 1.0 yalign -0.7
            if firstPick == 3:
                $ shopSpyName = "Alex"
                $ shopCurrentSpy = 3
                show yellow y1:
                    xalign 1.0 yalign -0.7
            call screen bgShop2
            jump mall
        "Tits and Tats" if slutLevel >= 2:






            $ menuSelect = 3
            scene bgShops
            if firstPick == 1:
                $ shopSpyName = "Sam"
                $ shopCurrentSpy = 1
                show green g1:
                    xalign 1.0 yalign -0.7
            if firstPick == 2:
                $ shopSpyName = "Clover"
                $ shopCurrentSpy = 2
                show red r1:
                    xalign 1.0 yalign -0.7
            if firstPick == 3:
                $ shopSpyName = "Alex"
                $ shopCurrentSpy = 3
                show yellow y1:
                    xalign 1.0 yalign -0.7
            call screen bgShop3
            jump mall

            $ menuSelect = 5
            "Not in yet"
            jump mall

            "DEV: WORK IN PROGRESS"
            $ menuSelect = 6
            scene bgShops
            $ shopSpyName = "Sam"
            $ shopCurrentSpy = 1
            show green g1:
                xalign 1.0 yalign -0.7
            call screen bgShop6
        "stoop2low" if task24Stage >= 2:
            if task24Stage == 3:
                $ task24Stage = 4
                show scene_darkening with d3
                pause 0.5
                shopOwner "Thank you again for saving me from the Outsiders. Here's your rewards."
                $ randMoney = 600
                $ cash += randMoney
                call missionRewardMoney from _call_missionRewardMoney_85
                pause 0.7
                y "Okay Clover. We liberated the shop. Now you can buy your-..."
                cM "I'll take the Kobald miniatures, and the dragon and the goblins and the...."
                y "............................"
                hide scene_darkening with d3
                pause 0.5
                call qCompleted from _call_qCompleted_11
            $ menuSelect = 7
            scene bgShops
            $ shopSpyName = "Sam"
            $ shopCurrentSpy = 1
            show green g1:
                xalign 1.0 yalign -0.7
            call screen bgShop7
        "leave the mall" if True:
            jump worldmap




default timesExplored = 0

label explore:
    $ timesExplored += 1
    "You spend the day exploring the city."
    scene black with fade
    $ randomBG = renpy.random.randint(1, 5)
    if randomBG == 1:
        scene bgStreet1
    if randomBG == 2:
        scene bgStreet2
    if randomBG == 3:
        scene bgStreet3
    if randomBG == 4:
        scene bgStreet4
    if randomBG == 5:
        scene bgStreet5
    with fade
    if gang1Active == False and specialCandyStatus == 0:
        $ gang1Active = True
        "Aces introduction here"
        jump jobReport
    if gang2Active == False and timesExplored >= 3 and specialSebStatus == 0:
        $ gang2Active = True
        "After a while you find yourself in the south east of the city."
        "Softly in the distance you hear music playing."
        y "Are they having a party...?"
        "{size=-8}{b}♫*Music*♫{/b}{/size}"
        y "............"
        "{size=-4}{b}♫*Music*♫{/b}{/size}"
        y "Is it getting clos-...?"
        "{size=-1}{b}♫*Music*♫{/b}{/size}"
        with hpunch
        "{size=+14}{b}♫*Music*♫{/b}{/size}"
        "A fleet of trucks is heading your way! In the back are large speaker systems blasting music loudly through the city!"
        menu:
            "Stand in the middle of the road" if True:
                y "........................"
                y "(This is a bad idea....)"
                "{b}*Vrooooooooooooom*{/b}"
                "The cars are closing the distance in a worrying pace."
                y "(Where in life did I go wrong? To believe that standing still in the middle of traffic would be a good idea?)"
                "{b}{size=+6}*Vrooooooooooooom*{/b}{/size}{w} {b}*Skreeeeeeeeeeeee.....*!!!!!!!!!{/b}"
                "Before you are met with your imminent demize, the horde of trucks step on their breaks!"
                y "(Wait! They're stopping! Maybe I {i}'will'{/i} live through this!)"
                "{b}*Skreeeeeeeeeeee~....{w}eeeeeeeeee.....~*{w}eeeeeeee......!!!!!!{/b}"
                "The trucks were driving at such an insane speed, that their break distance is much longer than expected!"
                y "Man, am I glad that you guys stopp-...."
                play sound "audio/sfx/punch1.mp3"
                scene black
                pause 1.0
                "..............................."
                "You got hit by a truck, you dummy."
                scene bgStreet4
                with longFade
                "Drift Punk 1" "{size=-8}Look, he's waking up....{/size}"
                y "Ugh~....."
                "Drift Punk 1" "You okay there, buddy?"
                y "Did anyone get the license plate of the truck that hit me...?"
                "Drift Punk 2" "Yeah I did. It was G-E-T-{w}OFFTHEFUCKINGROAD."
                "Drift Punk 1" "You're pretty wild to stare at oncoming traffic and think you can take it."
                "Drift Punk 1" "Then again, here you are! A little worse for wear, but still in one piece."
            "Quickly move aside" if True:
                "You try to quickly dodge out of the way, but trip over a piece of trash in the road!"
                "You try to catch yourself, but the moment pushes you forth and you accidentally do a sick flip in the middle of the street."
                "Behind you, you hear the trucks screeching to a halt, followed by loud hollaring and applause."
                "Drift Punk 1" "Woah, did you see that?! That old guy just did a sick flip!"
                y "(Old...?!)"
                "Drift Punk 2" "And while our trucks were driving straight at him! This guy's got guts!"
                y "............"
                y "Yes.. I did that on purpose."
                y "....................."
            "Start singing loudly" if True:
                y "{b}*Inhale*{/b} {i}♫♪MY BUNNY LIES OVER THE OCEAN!{w} MY BUNNY LIES OVER THE SEA...!♫♪{/i}"
                y "{i}♫♪MY BUNNY LIES OVER THE OCEAN, PLEASE BRING BACK MY BUNNY TO ME!♫♪{/i}"
                "The cars come to a screeching halt as they stop to listen the weirdo singing loudly in the street."
                "After you're done, they applaud loudly!"
                "Drift Punk 1" "Bravo! Gotta love the classics!{w} Though I'm pretty sure it's suppose to be Bonnie, not Bunny."
                y "It is...?"
                "Drift Punk 2" "I always thought it was {i}'My money lies over the ocean.'{/i}{w} I thought it was about someone losing their wallet..."
                "Drift Punk 3" "Really? And here I thought it was: {i}'My brawny lies over the ocean...'{/i}"
                "Drift Punk 1" "That's not even a word..."
                y "................."
        "Drift Punk 1" "We're Drift Punk, the nerds who own these streets."
        y "Nerds?"
        "Drift Punk 1" "Yeah, people always used to make fun of us and called us nerds, but now it's hot to be a nerd!"
        "Drift Punk 2" "And nobody makes fun of you if you're packing a .9 mm!"
        y "I always knew the nerds who rise up one day. That's why I memorized the script of the Star Wars movies."
        "Drift Punk 1" "Hah! You seem like a pretty cool dude. Wanna come with us?"
        "Drift Punk 1" "We're gonna kidnap some fools and tattoo music sheetpaper on their backs!"
        "Drift Punk 2" "I want to draw Rimsky Korsakov's Flight of the Bumblebee on someone!"
        "Drift Punk 1" "Dude that's sick!"
        y "I sorta already got something going on for me, but I know a girl who could come work for you guys."
        "Drift Punk 1" "A girl?! I dunno...{w} Is she a blonde?"
        "Drift Punk 2" "Dude, what is it with you and blondes?"
        "Drift Punk 1" "Hey I just like blondes, okay?! Don't judge me!"
        "Drift Punk 1" "Send her over sometime, she can come hang with us."
        "Drift Punk 1" "Now if you'll excuse me! It's far too quiet here!"
        "Drift Punk 1" "I NEED NOISE!"
        with hpunch
        "{size=+10}{b}♫*Music*♫{/b}{/size}"
        "The fleet of cars speed off..."
        play sound "audio/sfx/itemGot.mp3"
        "You've unlocked a contact within {color=#ffeda6}Drift Punk{/color}."
        "You can now send your spy to go undercover with them."
        scene bgMap:
            zoom 0.5
        with fade
        pause 0.6
        jump jobReport

    if gang3Active == False and timesExplored >= 6 and specialKandStatus == 0:
        $ gang3Active = True
        "You find yourself to the north east of the city as you walk through graffiti covered streets."
        "???" "N-no please don't hurt me!"
        y "...?"
        "You turn a corner and see a group of punkers surround a local butcher."
        "Outsider" "How many times do we have to tell you....?{w} We're not here to rob you."
        "Butcher" "Please! Just take my money and leave! I don't want any trouble!"
        "Outsider" "Listen you deaf fool, I said we're not after your money!"
        "Butcher" "You ruffians! You fiends! My money not enough for you?! You also want to wreck my shop and defile my daughter?!"
        "The rough looking punk sigh as he sees you approach."
        "Outsider" "Hey, you're one of those WOOHP Agents, right? How you doing man?"
        y "Just peachy. {w}What's going on here?"
        "Outsider" "This fatass thinks we're robbing him..."
        "Butcher" "They were throwing in the windows of shops!"
        "Outsider" "We were only destroying large conglomerate chains!"
        "The butcher flinches and cowers with his hands over his head."
        "Outsider" "{b}*Sighs*{/b} Hey WOOHP Agent, can you give him back his money?"
        "Outsider" "I get the feeling he'll trust someone in a suit more easily."
        y "Sure...."
        menu:
            "Give back the money (+Karma)" if True:
                $ playerKarma += 1
                pass
            "Give back half of it (-Karma)" if True:
                $ playerKarma -= 1
                "When you made sure that no one is watching, you quickly pocket half of the money."
                $ randMoney = 150
                call missionRewardMoney from _call_missionRewardMoney
        "You walk up to the butcher, money in hand."
        y "{b}*Ahem*{/b} Excuse me sir. I believe this belongs to you."
        "Butcher" "Oh! You brought me back my money! Thank you so much!"
        "Butcher" "Those thugs were after blood! Thank you so much for your brave, kind act. They ought to throw that scum in jail and throw away the key!"
        "After you say goodbye to the butcher, you return to the Outsiders."
        y "Well that was odd..."
        "Outsider" "Happens all the time. People see the way we look and freak out."
        y "So... why were you wrecking the stores around this neighborhood?"
        "Outsider" "Well..."
        "Outsider" "Almost all of these shops are owned by the same company. They hired a private security company to 'protect' their investments."
        "Outsider" "These guys go around, harressing and shaking down the kids that nobody cares about."
        "Outsider" "They're scum wearing fancy combat gear. They broke my arm a few months back for skateboarding in the mall."
        y "And now you're fighting back?"
        "Outsider" "Sort of. The cowards ran the moment the fighting broke out in the streets."
        "Outsider" "So hey, thank you for the help back there. I guess not all suits are so bad."
        "Outsider" "If you ever consider dropping the fancy threads, then you can come hang with us."
        y "I don't think my boss will like it if I take this off, but I might know a girl who'd like to meet you guys."
        "Outsider" "As long as she's cool, she's welcome. Don't send us any valley girls, you dig?"
        "The punkers grab their spraycans and stakeboards before heading off."
        play sound "audio/sfx/itemGot.mp3"
        "You've unlocked a contact within the {color=#ffeda6}Outsiders{/color}."
        "You can now send your spy to go undercover with them."
        scene bgMap:
            zoom 0.5
        with fade
        pause 0.6
        jump jobReport

    if gang4Active == False and timesExplored >= 9 and socialSilva <= 7:
        $ silOutfit = 2
        $ silHair = 2
        $ gang4Active = True
        y "Now then, where to begin my-...."
        y "....?"
        y "I don't remember there being this many weeds arounds here..."
        "As you walk into a street, it's completely covered from top to bottom with plants, weeds and vines."
        y "Somehow I can already tell who's behind this~...."
        "You try taking a step forward, but notice you leg being snagged on something."
        stop music fadeout 1.5
        y "!!!"
        "One of the vines has wrapped itself around your ankle!"
        y "Hey! HEY! Get off! Bad plant!"
        play music "audio/music/silva2.mp3"
        show scene_darkening
        with d3
        sil "Who is badmouthing my plants?!"
        show silvaModel at ri with d3
        sil "Oh! It is you. Have you reconsidered my offer~...?"
        y "No you fruity fern! Get your tentacles off of me!"
        sil "Oh if I had a nickle for everytime I hear somebody say zhat~...."
        y "..............."
        sil "Oh fine. You're no fun."
        "Silva lets out a sharp whistle and like a snake, the vine lets go of your leg and slithers over to its master."
        y "Gross."
        sil "So mon ami. Still kicking, I see?"
        y "Yes. Still French I see."
        sil "Oui oui! It is always exciting to see you! Have you come to smell my flowers~...?"
        y "No, I lost my ability to smell after the kindergarden incident."
        sil "The wh-...?"
        y "I'm just having a look around town."
        y "Met with some of the other gangs around. They're actually pretty cool, if you ignore their weird gimmicks."
        sil "Wait, you've actually gone up to ze gangs and chatted with zhem?"
        sil "So brave! Are you not afraid of getting shot?"
        y "I haven't been so far."
        y "Other than that I guess I got a new milkshake bar, which is on neutral ground."
        sil "Milkshake bar? W-wait... neutral ground?"
        y "Anyways, it's been fun talking to you Abegail, but I need to be off. See you around!"
        sil "O-oh right! Do visit sometime!"
        play sound "audio/sfx/itemGot.mp3"
        hide silvaModel
        hide scene_darkening
        with d3
        "You've unlocked a contact within the {color=#ffeda6}Les Épines{/color}."
        "You leave a confused Abegail behind and continue exploring. You don't find much else for the rest of the day and decide to head back home."
        scene bgMap:
            zoom 0.5
        with fade
        pause 0.6
        jump jobReport

    if hackerUnlocked == False and timesExplored >= 4:
        y "Hmm...."
        "You look around at the ravaged buildings."
        y "Looks like this was a bad neighborhood even before the riots."
        "As you look around, you suddenly notice a red dot appear right before your feet."
        y "SNIPER!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        "You dodge out of the way and cover your head with your arms."
        "....................................."
        y "...........?"
        "Carefully peaking through one eye, you see the red dot still appearing on the ground, flashing on and off."
        y "Is that..."
        y "Morse Code?"
        y "On off, on off, on off...."
        y "S.O.S. ... T.R.A.P.P.E.D. ... R.U.B.B.L.E."
        y "!!!"
        "You look around and see a badly damaged building. It looks half collapsed and you see a small lazer dot flicking on and off."
        menu:
            "Run in to help" if True:
                "Without a second thought, you rush inside to see who's signaling you."
                show scene_darkening
                with d3
                y "Hello? Somebody here?"
                "???" "Yes! Over here! I'm stuck underneath the rubble."
                "Following the voice you find a man buried underneath concrete and broken beams."
                y "Hang on, I got you..."
                scene black with fade
                scene bgStreet1 with fade
                show matModel at ri with d3
                pause 0.4
                "???" "Thanks stranger. I'd been buried there since yesterday. I thought I was done for."
                "???" "I'm Mathias. I never expected to be saved by one of you WOOHP agents."
                y "Yeah well... We're full of surprises I guess."
                y "If you're okay, then I'm gonna head off again."
                mat "Hang on, let me give you a reward for rescuing me."
                y "Oh that won't be nec-..."
                play sound "audio/sfx/itemGot.mp3"
                "Mathias hands you a handful of {color=#ffeda6}Valuables{/color}."
                y "Well that's generous. Don't you want to sell these yourself?"
                mat "Their monetary value is lost on me. I use them to craft techno gadgets."
                y "...?"
                mat "I'm a hacker by trade, but earn a little extra selling scrap."
                mat "If you're ever in need of some materials, let me know. All right?"
                y "I certainly will!"
                "After saying your goodbyes, you return to the base."
                $ hackerUnlocked = True
                $ matsValu += 1
            "Leave the area" if True:
                y "Not taking any chances."
                "You quickly move on."
                hide matModel
                scene black
                with fade
                "The rest of the day remains uneventful and you head back to the base."
        scene bgMap:
            zoom 0.5
        with fade
        pause 0.6
        jump jobReport

    if task8Stage == 0 and task3Stage >= 7 and task4Stage >= 7 and task5Stage >= 5:
        jump task8
    elif True:

        $ randomExplore = renpy.random.randint(1, 20)

        if samMiniQ1 == 1:
            pause 0.7
            show scene_darkening
            with d3
            "After a while you come across a destroyed building with an ugly looking statue out front."
            y "Hey, this must have been the gallery Sam was talking about."
            menu:
                "Go in" if True:
                    $ samMiniQ1 = 2
                    "You head into the mostly destroyed museum and have a look around."
                    y "They really did a number on this place..."
                    y "Hm? What's this?"
                    "Under the rubble you find a small figure of... well you can't tell what it's suppose to be. It's modern art after all."
                    y "Sam might like this. I'll bring it to her and see if she knows what it is."
                    "Suddenly you hear a loud crack. Looking up, you notice that the building is about to collapse!"
                    play music "audio/music/sinister.mp3"
                    y "Crap!"
                    "You begin running! You weave past rubble and what you expect might have been art pieces as more and more of the buildings comes tumbling down."
                    "At the end of the hallway you see the exit sign of the gallery!"
                    y "Almost... almost...!"
                    play sound "audio/sfx/punch1.mp3"
                    scene black with hpunch
                    stop music
                    pause 2.5
                    scene white with fade
                    scene bgStreet1 with fade
                    "You made it out just in time!"
                    y "This better have been worth it..."
                    "One near death experience richer, you head back to the base."
                "Leave it be" if True:
                    $ samMiniQ1 = 4
                    "You turn around and leave the building. Suddenly you hear a loud crash and when you turn around, you see part of the roof breaking collapsing."
                    y "Phew! I could have been in there!"
                    "Deciding it's not worth hanging around this place any longer, you head back to the base."
            scene black with fade
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport

        if randomExplore == 1:
            pause 0.7
            show scene_darkening
            with d3
            "Thug 1" "And then I totally dropped the mic!"
            "Thug 2" "And....?"
            "Thug 2" "Was it a success?"
            "Thug 1" "Oh no, I completely flunked it, it felt awful..."
            "Thug 2" "Maybe you you should stop rapping about blueprint layouts, points of entry and camera blindspots, dude."
            "Thug 1" "What?! Are you crazy! Those are my favorite subjects!"
            "Thug 1" "Here listen to this!"
            menu:
                "Continue to listen" if True:
                    "The thug begins an awful rap about unsecured skylights, faulty alarm systems and guard patrol routes."
                    "Thug 2" "God, that {i}'is'{/i} awful! Where do you get this shit?"
                    "Thug 1" "I'm on patrol with those WOOHP Agents. Boring work man... gotta have something to do."
                    y ".............................."
                    $ randIntel = renpy.random.randint(10, 20)
                    call missionRewardInt from _call_missionRewardInt
                    "Thug 2" "Yeah go write about your mom's spagetti or something next time."
                    "Having heard enough, you leave the two alone and continue exploring."
                    hide scene_darkening
                    scene black with fade
                    "The rest of the day is uneventful and when it gets dark, you return to the base."
                    hide scene_darkening
                    with d3
                    if playerKarma >= 60:
                        $ karmaCash = renpy.random.randint(1,4)
                        if karmaCash == 1:
                            $ cash += 10
                            play sound "audio/sfx/itemGot.mp3"
                            "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                    jump jobReport
                "Leave the two alone" if True:
                    y "(Yeah....~{w} no.)"
                    "You get out of dodge before the two decide to spit some fire."
                    hide scene_darkening
                    with d3
                    scene black with fade
                    "The rest of the day is uneventful and when it gets dark, you return to the base."
                    if playerKarma >= 60:
                        $ karmaCash = renpy.random.randint(1,4)
                        if karmaCash == 1:
                            $ cash += 10
                            play sound "audio/sfx/itemGot.mp3"
                            "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                    jump jobReport
        if randomExplore == 2:
            "{b}*Glass shattering*{/b}"
            y "...?"
            "You turn around the corner and see a group of Outsiders throwing in the windows of an office building."
            show scene_darkening
            with d3
            "Outsider 1" "Hell yeah! See how it shatters? That'll teach them!"
            y "What are you doing...?"
            "Outsider 1" "We're throwing in the windows of this fatcat organization!"
            "Outsider 2" "They think they're so big and bad! Think they can get away with anything they like!"
            y "It says here the building is empty and for rent."
            "Outsider 2" "Oh..."
            "Outsider 1" "Maybe we should have checked that before chucking stones at it..."
            y "Oh this is great. I bet Drift Punk will have a good laugh over this!"
            "Outsider 2" "No man! Please don't let this get out! They'll think we're idiots!"
            menu:
                "Share it with Drift Punk" if True:
                    $ punkRep += 1
                    call missionRewardRep from _call_missionRewardRep
                    y "Too late, already posted it to their social media."
                    "Outsiders" "{b}*Groans*{/b} We're never gonna live this down..."
                "Keep the secret" if True:
                    $ outsideRep += 1
                    call missionRewardRep from _call_missionRewardRep_1
                    y "Fine, your secret is safe with me."
                    "Outsider 2" "Thanks man! We owe you one!"
            hide scene_darkening
            with d3
            "You decide to head off and leave the Outsiders behind."
            scene black with fade
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport

        if randomExplore == 3:
            "You quickly find yourself in the fancier part of town, down in the south west."
            "Aces Chick" "Oh my God! You should {i}'totally'{/i} buy this new outfit! It would look {i}'so'{/i} cute on you!"
            "Aces Guy" "I don't know... It's showing off my midriff and I'm not huge on the point shoes either..."
            "Aces Chick" "Don't be silly! It's the latest in the 'Bitch on a leash' fashion line!"
            "Aces Guy" "Yeah you see... I don't know how I feel about that either."
            "Aces Chick" "Oh my God, you are such a whiner! Just go buy the stupid outfit and don't forget the collar!"
            "Aces Chick" "Then afterwards, we're going to dye your hair and as thanks you can come carry our shoppingbags."
            y "Kptshhh! Looks like someone's being pussywhipped!"
            "Aces Guy" "You gotta help me man. This girl wants me to buy a G-string and wear heels!"
            menu:
                "Bail him out" if True:
                    y "Why do you want your boyfriend to look like a cuckhold beta bitch?"
                    "Aces Chick" "Oh, he's not my boyfriend. We're totes besties!"
                    "Aces Guy" "{b}*Groans*{/b}"
                    "Aces Chick" "And I want him to look pretty and cute! It's for {i}'his'{/i} sake, you know! I'm doing him a favor."
                    "Aces Guy" "(Kill me please...!)"
                    y "Okay... I think I see what's going on here."
                    y "First of, stop being such a total pussy and letting this girl boss you around."
                    "Aces Guy" "Wait, now it's my fault?!"
                    y "Just tell this bird that you want to smash, and if she says no then go find somebody else instead of dressing like a gimp."
                    y "And you stop being such a controlling freak and leading him on!"
                    "Aces Chick" "Leading him on?! {b}*Scoffs*{/b} Get real. My little baby just wants to be friends and you're being really rude right n-..."
                    "Aces Guy" "No! He's right!"
                    "Aces Guy" "What happened to me?! I used to be a quarterback in highschool! When did I turn into such a push-over?!"
                    "Aces Guy" "This chick is crazy and I'm getting the fuck out of here. Carry your own damn shopping bags from now on!"
                    "Aces Chick" "B-but...!"
                    "The Aces Guy drops the clothes and walks away."
                    "Aces Chick" "Oh my God... He's never stood up against me before!{w} I so want him right now."
                    "Picking up her clothes, the girl quickly chases after the guy."
                    "Aces Chick" "Wait babe! Wait for meeee~....!"
                    y "...................."
                    y "(Did the world go crazy while I was in jail or is it just this city...?)"
                    hide scene_darkening
                    scene black with fade
                    "The rest of the day is uneventful and when it gets dark, you return to the base."
                    scene bgMap:
                        zoom 0.5
                    with fade
                    pause 0.5
                    if playerKarma >= 60:
                        $ karmaCash = renpy.random.randint(1,4)
                        if karmaCash == 1:
                            $ cash += 10
                            play sound "audio/sfx/itemGot.mp3"
                            "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                    jump jobReport
                "Be open to new experiences" if True:
                    y "What? Your masculinity is tied to your fashion style?"
                    "Aces Guy" "Well... no, but..."
                    y "Give it a try. It could be liberating to be more in touch with your feminine side!"
                    "Aces Guy" "I don't know if I really wan-.."
                    "Aces Chick" "See? What did I tell you? People will sense your confidence when walking around like this!"
                    "Aces Guy" "I guess it does take confidence to carry a ballgag around your neck..."
                    "Aces Guy" "Okay, you know what! Fine! I will try to be more sissy!"
                    "The guy picks up the shopping bags and runs off."
                    y "................."
                    y "You owe me."
                    "Aces Chick" "Hell yeah I do. Here's something for your trouble."
                    $ cash += 100
                    $ randMoney = 100
                    call missionRewardMoney from _call_missionRewardMoney_1
                    "Tucking the money into your hands, she winks at you."
                    "Aces Chick" "Call me~...."
                    hide scene_darkening
                    scene black with fade
                    "The rest of the day is uneventful and when it gets dark, you return to the base."
                    scene bgMap:
                        zoom 0.5
                    with fade
                    pause 0.5
                    if playerKarma >= 60:
                        $ karmaCash = renpy.random.randint(1,4)
                        if karmaCash == 1:
                            $ cash += 10
                            play sound "audio/sfx/itemGot.mp3"
                            "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                    jump jobReport
        if randomExplore == 4:
            y "I wonder what I'll run into toda-..."
            "Suddenly a group of WOOHP Agent turn the corner!"
            y "(Crap..!)"
            show scene_darkening
            show agentModel:
                xalign 0.9 yalign 0.0
            play audio "audio/voice/agent/locknload.mp3"
            "Agent" "Locked and loaded! Ready to cause some destruction, fellow agent?!"
            y "Er...."
            menu:
                "'Always up for some voluntary manslaughter'" if True:
                    "Agent" "That is the right answer! Did you bring your own gun?"
                    y "Actually, I don't have one of those yet."
                    "Agent" "An Agent without a gun, is like a fleshlight without a battery!"
                    y "Did you just say fleshli-...?"
                    "Agent" "I know what I said!"
                    "You join the group of agents as they make their way to city hall."
                    "Agent" "Inside is a militia of citizens that have banded together to fight back!"
                    "Agent" "A tactful elegant solution is required!{w} Which is why we're going to burn down city hall with them inside!"
                    y "!!!"
                    y "(So I'm still one of the good guys, right...?{w} Let me check my moral compass real quick.)"
                    y ".........{w}.........{w}.........{w}"
                    y "(Yeah okay, that's definitely a terrible thing to do. I should stop them.)"
                    y "Now hang on just a moment. Instead of burning them alive..."
                    label randomExplore4:
                        pass
                    menu:
                        "Distract the Agents (-Magazine)" if True:
                            if magazine >= 1:
                                $ freedAgents += 1
                                "Agent" "A copy of the latest iSpy Magazine?!{w} Oh boy! You shouldn't have!"
                                play sound "audio/voice/agent/forTheArt.mp3"
                                "The agents gather around and begin flipping through the magazine."
                                "Agent" "Look at the combat gear on this one! She could poke someone's eye out with those!"
                                "Agent" "This magazine sure is distractin-..."
                                "Agent" "............................"
                                "Agent" "Wait... what am I doing here again?"
                                y "You were about to kill a town center full of people."
                                "Agent" "That is awful! I am a awful being!"
                                y "You could come work for me to redeem yourself."
                                "Agent" "Sounds like a plan! The days of careless disregard for human life are behind me now!"
                                y "Good, head into the milkshake bar and await further orders in the basement."
                                "Agent" "Basements are dark and depressing. Just like my lovelife!"
                                hide scene_darkening
                                hide agentModel
                                with d3
                                "The Agent heads back to the Milkshake Bar."
                                call missionRewardCrew from _call_missionRewardCrew
                                "It soon turns evening as you return to the base."
                                scene bgMap:
                                    zoom 0.5
                                with fade
                                if playerKarma >= 60:
                                    $ karmaCash = renpy.random.randint(1,4)
                                    if karmaCash == 1:
                                        $ cash += 10
                                        play sound "audio/sfx/itemGot.mp3"
                                        "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                                jump jobReport
                            elif True:
                                "You don't have a dirty magazine to distract the Agents with."
                                jump randomExplore4
                        "Try talking to them" if True:
                            y "This sounds like a job for diplomacy!"
                            "Agent" "You were given a diplomacy course by WOOHP?"
                            y "Er...{w} yes."
                            "Agents" "Wow! Us normal grunts normally aren't given something as fancy as 'schooling'. We are in awe and amazed by your superior knowledge!"
                            y "......................"
                            y "Are you being sarcastic right now, ooor...?"
                            "Agent" "Please fellow agent! Show us how diplomacy will solve this situation!"
                            y "................"
                            hide agentModel
                            with d3
                            scene black with fade
                            "You head into the Town Hall."
                            "After explaining how everyone inside is about to die, the militia seems more willing to cooperate as they throw down their weapons and surrender."
                            show bgStreet1
                            with fade
                            "Agent" "It seems that all those expensive lessons have paid off!{w} We even have prisoners now!"
                            y "What are you going to do with them?"
                            "Agent" "We are going to practise our diplomancy on them!"
                            y "Yeah.... I don't wanna know what you mean by that."
                            "Agent" "Farewell fellow agent. You have taught us a lot today!"
                            "You quickly get out of there as the Agents march into city hall."
                            scene black
                            hide scene_darkening
                            hide agentModel
                            with fade
                            "At night you return to the base."
                            scene bgMap:
                                zoom 0.5
                            with fade
                            pause 0.5
                            if playerKarma >= 60:
                                $ karmaCash = renpy.random.randint(1,4)
                                if karmaCash == 1:
                                    $ cash += 10
                                    play sound "audio/sfx/itemGot.mp3"
                                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                            jump jobReport
                        "Run away" if True:
                            y "That sounds like a great idea! {w}....{w} And talking about burning down a house, I think I left the oven on. You guys have fun now!"
                            "You quickly leave the scene before the violence erupts."
                            scene black
                            hide scene_darkening
                            hide agentModel
                            with fade
                            "At night you return to the base."
                            scene bgMap:
                                zoom 0.5
                            with fade
                            pause 0.5
                            if playerKarma >= 60:
                                $ karmaCash = renpy.random.randint(1,4)
                                if karmaCash == 1:
                                    $ cash += 10
                                    play sound "audio/sfx/itemGot.mp3"
                                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                            jump jobReport
                "'Maybe some other time'" if True:
                    y "Yeah~... So I left the oven on aaand~..."
                    "Agent" "That sounds like an excuse!{w} You have received your dosis of nanobots, right?"
                    y "Erm..."
                    "Agent" "Don't worry fellow agent. It won't hurt a bit, and they'll give you a lollipop afterwards."
                    "Agent" "At least they say they will.{w} But they lie."
                    with hpunch
                    "Agent" "{size=+10}THEY LIE!{/size}"
                    y ".........."
                    y "Well, better go get me that injection then!"
                    "Agent" "Let's meet up later and discuss the latest baseball game!"
                    y "Oh yeah... I would love that..."
                    "Agent" "Your sarcasm wasn't lost on me! Take care now, fellow Agent!"
                    "You quickly leave the scene before the violence erupts."
                    scene black
                    hide scene_darkening
                    with fade
                    "At night you return to the base."
                    scene bgMap:
                        zoom 0.5
                    with fade
                    pause 0.5
                    if playerKarma >= 60:
                        $ karmaCash = renpy.random.randint(1,4)
                        if karmaCash == 1:
                            $ cash += 10
                            play sound "audio/sfx/itemGot.mp3"
                            "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                    jump jobReport
            hide scene_darkening

        if randomExplore == 5:
            $ smoothieCoupon += 1
            "You casually walk past through the downtown area. Pretending not to notice the signs of violence and destruction around you."
            y "Dumpty dumpty dum..."
            with hpunch
            "Girl" "Stick 'em up!"
            y "GAH!"
            "Out of nowhere a girl with a loaded shotgun comes at you, holding you at gunpoint."
            y "(Oh crap, oh crap!)"
            show scene_darkening
            with d3
            "Girl" "................................"
            "Girl" "Coupon?"
            y "What...?"
            "Girl" "Would you like a coupon for a free smoothie from the mall?"
            y "Damn it girl! Sure I'll take your coupon, just stop pointing that gun at me!"
            "Girl" "Sorry about that! With people too afraid to leave their house, getting rid of these coupons has been a real pain. I had to change up my tactics a bit!"
            "Girl" "I'm not getting paid for my part-time job unless I hand out 'all' of these coupons, so I have to get creative."
            y "......................."
            "Girl" "{i}'Have a smoothilicious day!'{/i}"
            hide scene_darkening
            with d3
            play sound "audio/sfx/itemGot.mp3"
            "You got {color=C91A1A}Smoothie Coupon{/color} x1."
            scene bgMap:
                zoom 0.5
            with fade
            pause 0.5
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 6:
            "You stumble upon a roadblock. You can find a way around or grab a shortcut through this dark, shady looking alley."
            menu:
                "Go through the alley" if True:
                    "What could possible go wrong? You head into the alley without a care in the world."
                    show scene_darkening
                    with d3
                    "Voice 1" "Pssst, did you get the stuff?"
                    "Voice 2" "Dude, stop calling it 'the stuff'. I brought your stupid Japanese magazine. Now pay up."
                    "Voice 1" "Yes~... Hamdarusojamia-sama might actually touch hands with Ai-san in this chapter!"
                    "Voice 2" "Whatever dude. Didn't they have vigorous sex in like... issue 1?"
                    "Voice 1" "You uncultured swine! Ai-sempai would never do that! That was a mimic sent by hell itself to impregnate girls of questionable age to repopulate hell's army of lolis!!"
                    "Voice 1" "Since then, Hamdarusojamia has gone on a journey of selfdiscovery and they both fell in love, but have been too afraid to tell each other!"
                    "Voice 2" "For over 200 issues?"
                    "Voice 1" "LOVE TAKES TIME YOU INGRATE! YOU CAN'T RUSH LOVE!"
                    "Voice 2" "Whatever dude, just pay me for your Japanese smut so I can get out of here."
                    "You sneak up to the two making the transaction."
                    "Voice 1" "You were followed! {w}SMOKE BOMB!"
                    play sound "audio/sfx/poof1.mp3"
                    with flashbulb
                    "Voice 2" "{b}*Cough* *Cough*{/b} Great job dude, you scared him away!"
                    "Voice 2" "Take the stupid magazine, I'm going back to dealing something less weird."
                    hide scene_darkening
                    with d3
                    y ".............................."
                    play sound "audio/sfx/itemGot.mp3"
                    "You got {color=C91A1A}Dirty Magazine{/color} x1"
                    "The rest of the day is uneventful as you make your way back home."
                    $ magazine += 1
                "Find a way around" if True:
                    y "I've seen Batman. No way am I going to start sneaking through dark alleys."
                    "You decided to take the long way round."
                    show scene_darkening
                    with d3
                    "Angry Man" "ME SMASH!"
                    "Thug 1" "Dude, do you think we gave him too much?"
                    "Angry Man" "ME TAKE OVER WASHINGTON! ME PUSH THROUGH FISCAL REFORMS!"
                    "Thug 2" "I dunno dude, maybe you shouldn't have given him an extra dose of nanobots."
                    "Thug 2" "It says here to not give more than a single dosis at a time. How much did you give him?"
                    "Thug 1" "................................."
                    "Thug 2" "How many....?"
                    "Thug 1" "A dozen....{w} or two."
                    "Thug 2" "Two dozen?! That guy is filled it up to the brim with nanobots now! No wonder he tries to take over the world!"
                    "Angry Man" "DRAIN THE SWAMP! CUT COSTS AND INCREASE SPENDING! ME FOR PRESIDENT!"
                    "Thug 2" "Best get rid of your last injector, we shouldn't be messing around with that stuff."
                    "Thug 1" "What will we do with him?"
                    "Thug 2" "He'll calm down once he finds out that you can't become president without nepotism."
                    "The thugs toss a small injector on the floor and walk off."
                    hide scene_darkening
                    with d3
                    y "Yoink!"
                    play sound "audio/sfx/itemGot.mp3"
                    "You got {color=C91A1A}Small Nanobot Injector{/color} x1"
                    $ injectorSmall += 1
                    "The rest of the day is uneventful as you make your way back home."
            scene bgMap:
                zoom 0.5
            with fade
            pause 0.5
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 7:
            "You pass through the market. It looks deserted with only one of two brave merchants around."
            show scene_darkening
            with d3
            "Milkman" "Come get your milk here!"
            y ".....?"
            "Milkman" "You sir! Finest milk in all of Beverly Hills! Care for a glass?"
            y "You're selling milk at a market?"
            "Milkman" "It's a family tradition! My family has been selling milk on the market for over two hundred years!"
            y "You know there are supermarkets now, right?"
            "Milkman" "{b}*Scoffs*{/b} Supermarkets! They only sell boring old COWMILK!"
            y "Isn't that were milk comes from~...?"
            $ randomMilk = renpy.random.randint(1, 3)
            if randomMilk == 1:
                $ randMilkName = "Blobfish"
            if randomMilk == 2:
                $ randMilkName = "Bearded vulture"
            if randomMilk == 3:
                $ randMilkName = "Manatee"
            "Milkman" "Now if you want to treat yourself, you'll buy some of the finest [randMilkName] milk!"
            y "................"
            menu:
                "Buy milk - $100" if True:
                    if cash <= 99:
                        y "I actually don't have enough money for that."
                        "Milkman" "Oh well! Better lucky next time!"
                    elif True:
                        y "Against my better judgement..."
                        play sound "audio/sfx/itemGot.mp3"
                        "You bought {color=e400c7}Exotic Milk{/color}! Your cooking skill went up by 1"
                        $ exoticMilk += 1
                "Decline" if True:
                    y "That sounds disgusting! Good day sir!"
                    "Milkman" "Oh you'll be back! They'll all be back!"
            hide scene_darkening
            with d3
            "The rest of the day passes uneventful and you decide to return to the base."
            scene bgMap:
                zoom 0.5
            with fade
            pause 0.5
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 8:
            $ medkit += 1
            "You decide to pay a visit to the local hospital."
            y "................"
            y "Who trashes a hospital?! Seriously..."
            show scene_darkening
            with d3
            "Doctor" "Ah welcome to what's left of the Beverly Hills hospital."
            y "You're still here?"
            "Doctor" "We've set up medical tents and scavenged as many supplies as we could."
            "Doctor" "Are you in need of assistance?"
            y "Well I'm not, but the girls working for me might be."
            "Doctor" "I'll give you this medpack. It should fix up any minor injuries your friends might have."
            play sound "audio/sfx/itemGot.mp3"
            "You receive 1 {color=#ffeda6}Medkit{/color}!"
            y "Thanks doc."
            scene bgMap:
                zoom 0.5
            with fade
            pause 0.5
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if 9 <= randomExplore <= 12:
            label exploreLoot:
                pass
            if supplycrateOpen == False:
                show supplycrate:
                    xalign 0.4 yalign 0.75
                with d3
                call screen supplyCrate
            elif True:
                play sound "audio/sfx/supplycrate1.mp3"
                $ randCrate = renpy.random.randint(1,4)
                if randCrate == 1:
                    $ randLoot = renpy.random.randint(7,20)
                    $ resourceFood += randLoot
                    "Digging through the supply crate you find [randLoot] food."
                    "After stashing it, you return to the base."
                    $ randLoot = 0
                if randCrate == 2:
                    $ randLoot = renpy.random.randint(8,21)
                    $ resourceWater += randLoot
                    "Digging through the supply crate you find [randLoot] water."
                    "After stashing it, you return to the base."
                    $ randLoot = 0
                if randCrate == 3:
                    $ randLoot = renpy.random.randint(3,6)
                    $ resourceToys += randLoot
                    "Digging through the supply crate you find [randLoot] toys."
                    "After stashing them, you return to the base."
                    $ randLoot = 0
                if randCrate == 4:
                    $ randLoot = renpy.random.randint(5,13)
                    $ resourceClothes += randLoot
                    "Digging through the supply crate you find [randLoot] clothes."
                    "After stashing them, you return to the base."
                    $ randLoot = 0
            $ supplycrateOpen = False
            hide supplycrate
            hide screen supplyCrate
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 13:
            "You don't find anything interest, but overhear two gangsters talking."
            show scene_darkening with d3
            "Gangster 1" "I hate guard duty!"
            "Gangster 2" "Are... are you serious right now?"
            "Gangster 2" "Guard duty is probably the best thing that could've happened! Haven't you heard what happened to the last supply run team?"
            "Gangster 1" "No, what happened to them?"
            "Gangster 2" "Got chewed up by plants in that forest of the freaky plant lady!"
            "Gangster 1" "Oh God, are they okay?"
            "Gangster 2" "Ever fallen in stinging nettle? Okay, now imagine every inch of you got covered in it."
            "Gangster 1" "Ouch..."
            "Gangster 2" "Told ya guard duty ain't that bad."
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 14:
            "Walking down the road you see a group of gangsters nervously talking to each other."
            show scene_darkening with d3
            "Gangster" "We could really use...{w} Huh?"
            "Gangster" "Hey you're one of those WOOHP agents, right?"
            "Gangster" "We're gonna rob a pawn store, but we're short one person."
            "Gangster" "If you join in, we can promise you a share of the loot."
            menu:
                "Rob the pawn shop (-karma)" if True:
                    $ playerKarma -= 1
                    y "Daddy could use a new pair of shoes!"
                    "Together with the gangsters you storm into the shop."
                    scene black with fade
                    "Gangster" "OKAY, NOBODY MOVE!"
                    pause 0.5
                    scene bgStreet5 with longFade
                    "Gangster" "That went smoothly. Take your pick."
                    menu:
                        "Take the valuables" if True:
                            $ matsValu += 1
                            y "I'll take the valuables."
                            "Gangster" "Fair enough, you've earned you share."
                            call missionRewardItem from _call_missionRewardItem_3
                        "Take the clothes" if True:
                            $ resourceClothes += 10
                            y "I'll take these clothes."
                            "Gangster" "Good choice. There's some good stuff in there."
                            call missionRewardItem from _call_missionRewardItem_4
                        "Take the toys" if True:
                            $ resourceToys += 10
                            y "I'll take those."
                            "Gangster" "Er... sure. Whatever you say."
                            call missionRewardItem from _call_missionRewardItem_5
                "Turn them down" if True:
                    y "Maybe another time."
                    "The gangsters shrug and turn away."
            hide scene_darkening with d3
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 15:
            if gang4Active and socialSilva <= 7:
                play music "audio/sfx/warzone.mp3"
                y "Let's take a nice uplifting walk around downtown."
                "Voice" "You know it's a warzone out here, right?"
                y "Yup, nothing like a walk amongst friendly people to help rejuvenate my faith in humanity."
                "Voice" "Dude, seriously. There's gunfire, take cover or something!"
                stop music fadeout 3.0
                y "Man have you seen the sky? It's a beautiful green color today."
                "Voice" "Gree-...?"
                play music "audio/music/silva2.mp3" fadein 3.0
                scene bgTrip1 with d3
                "Voice" "!!!"
                "Voice" "WHAT?!"
                y "It's been a while since I felt this good~..."
                "Voice" "Are you having an episode?! Why is the sky gree-..."
                scene bgTrip2 with d3
                pause 0.8
                "Voice" "Is that the main menu image?!"
                y "You should relax and take in the atmosphere, man."
                y "Just let it guide you as you drift on by~...."
                sil "{size=-20}Mon ami? Oh non, not you too..!{/size}"
                "Voice" "I'm the voice in your head and even {b}{i}I{/i}{/b} am freaked out right now! Stop being so mellow!"
                y "Heh heh~... {i}'mellow'{/i}. That's a funny word~..."
                sil "{size=-20}Zher is nothing to worry about, I got you..!{/size}"
                y "Hey, I think I'm hearing voices~..."
                "Voice" "YOU THINK?!"
                scene bgTrip3 with d3
                show silvaModel at ri with d3
                y "Oh hey Silva!"
                sil "Sprechen sie Deutsch? Ich bin eine kleine Teetasse!"
                y "Silva speaking German?! Now that's abnormal!"
                "Voice" "Silva?! {w}Wait... Silva... oh no..."
                sil "{size=-20}Here... ze antidote..!{/size}"
                y "What was tha-...."
                stop music fadeout 3.5
                play sound "audio/sfx/punch1.mp3"
                scene black
                pause 1.9
                scene bgStreet2 with longFade
                y "Ugh....~"
                show silvaModel at ri with d3
                sil "Oh mon ami, are you okay? I am so sorry!"
                y "Sil...? What on earth happened...?"
                sil "I may have unleashed a hallucinogenic on the city by mistake~..."
                y "Oh... {w}So I'm not actually crazy?"
                "Voice" "Ugh... I feel sick. What did I miss?"
                y "Nope. Still hearing voices. Still crazy."
                sil "Here~... take my hand. I zhall take you home."
                y "Ich spreche kein Deutsch~..."
                hide silvaModel
                scene bgMap:
                    zoom 0.5
                with d5
                if playerKarma >= 60:
                    $ karmaCash = renpy.random.randint(1,4)
                    if karmaCash == 1:
                        $ cash += 10
                        play sound "audio/sfx/itemGot.mp3"
                        "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                jump jobReport
            elif True:
                "You couldn't find anything interesting and decided to head back to the base."
                if playerKarma >= 60:
                    $ karmaCash = renpy.random.randint(1,4)
                    if karmaCash == 1:
                        $ cash += 10
                        play sound "audio/sfx/itemGot.mp3"
                        "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                jump jobReport
        if randomExplore == 16:
            "You come across a plundered DIY store."
            menu:
                "Peak inside" if True:
                    $ resourceTools += 10
                    y "Anything left....?"
                    "Most of the store is empty, but you find some hammers, screwdrivers and nails."
                    call missionRewardItem from _call_missionRewardItem_6
                    y "Perhaps these will come in useful at one point."
                "Walk by" if True:
                    "You decided to not look inside."
                    "........................"
                    "Shady Man" "Pst, hey buddy."
                    y "...?"
                    "Shady Man" "Wanna buy some...{w} weeeeed?"
                    y "Against my better judgement..."
                    "Shady Man" "I got my hands on some Goldthorn. Thirty bucks."
                    y ".........."
                    menu:
                        "Buy the goldthorn ($30)" if True:
                            if cash <= 29:
                                y "I don't have enough money."
                                "Shady Man" "Better luck next time."
                            elif True:
                                $ cash -= 30
                                $ herbGold += 1
                                play sound "audio/sfx/itemGot.mp3"
                                "You bought {color=#ffeda6}Goldthorn{/color}."
                                "Shady Man" "Pleasure doing business...."
                        "Decline" if True:
                            "Shady Man" "Your loss..."
                    "You decide to head back to the base."
            scene bgMap:
                zoom 0.5
            with fade
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 17:
            $ injectorSmall += 1
            "You come across a plundered pharmacy."
            "Man" "I need... I need....~ !"
            y "Oh man, are you all right?"
            "Man" "It's been three days...."
            y "You poor man! What do you need? Asthma medication? Diabetes insulin?"
            "Man" "I need....{w} MORPHINE!"
            y ".................."
            y "You don't look in pain..."
            "Man" "You don't understand...!"
            "Man" "I plundered this farmacy three days ago, and have swallow, injected and sniffed everything there was on the shelves. Now I have nothing left!"
            y ".............."
            y "Time for a detox my friend. Let me relieve you of anything you have left."
            "Man" "Noooooo!"
            play sound "audio/sfx/itemGot.mp3"
            "You confiscate {color=#ffeda6}Nanobot Injector{/color} x1"
            call missionRewardItem from _call_missionRewardItem_7
            "You decide to head back to the base."
            scene bgMap:
                zoom 0.5
            with fade
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        if randomExplore == 18:
            "You come across a burned down supermarket."
            menu:
                "Scavenge for food" if True:
                    "You risk going into the burned out building in search of food."
                    play sound "audio/sfx/itemGot.mp3"
                    "Most of it seems burned or spoiled, but after a while you find some preserved food!"
                    $ resourceFood += 10
                    call missionRewardItem from _call_missionRewardItem_8
                    menu:
                        "Continue searching" if True:
                            "You brave the ruined building a bit longer."
                            y "I feel like I'm tempting fate here..."
                            "Through the charcoaled ruins you can make out the remains of the deepfreeze section."
                            y "Oh what do we have here..."
                            play sound "audio/sfx/itemGot.mp3"
                            "You find some bottled water!"
                            $ resourceWater += 15
                            call missionRewardItem from _call_missionRewardItem_9
                            "Not wanting to take your chances anymore, you decide to quickly get out."
                        "Quickly get out" if True:
                            "Not wanting to take your chances anymore, you decide to quickly get out."
                    scene bgMap:
                        zoom 0.5
                    with fade
                    if playerKarma >= 60:
                        $ karmaCash = renpy.random.randint(1,4)
                        if karmaCash == 1:
                            $ cash += 10
                            play sound "audio/sfx/itemGot.mp3"
                            "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                    jump jobReport
                "Move on" if True:
                    "You decide not to enter."
                    "As you continue walking you come across a broken vending machine! There still seems to be some bottled water left."
                    $ resourceWater += 10
                    call missionRewardItem from _call_missionRewardItem_10
                    "The rest of the day remains uneventful."
                    scene bgMap:
                        zoom 0.5
                    with fade
                    if playerKarma >= 60:
                        $ karmaCash = renpy.random.randint(1,4)
                        if karmaCash == 1:
                            $ cash += 10
                            play sound "audio/sfx/itemGot.mp3"
                            "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
                    jump jobReport
        if randomExplore >= 19:
            if shrineRestored >= 2:
                if spyGreenActive and spyRedActive and spyYellowActive and slutLevel >= 4 and tentaclePic == False:
                    label atmTentacle:
                        pass
                    scene bgStreet4 with fade
                    y "Look at these shrines! Zukkerthroth must be pleased."
                    show scene_darkening with d3
                    show green g1 at ri
                    show red r1 at ce
                    show yellow y29 at le
                    with d3
                    c "Oh hello there, [playerName]."
                    y "Girls! You're just in time to celebrate our glorious lord's return!"
                    s g16 "Glorious lor-...?"
                    "Zukkerthroth" "{b}*Intergalactic squeels of joy*{/b}"
                    a y30 "W-what was that...?!"
                    y "ZUKKERTHROTH NOW IS THE TIME FOR YOU TO RETURN!"
                    y "I PRESENT YOU WITH THESE THREE YOUNG MAIDENS! DEFLOWER THEM WITH YOUR THOUSAND TENTACLES OF COMPASSION!"
                    a y28 "Deflower...?"
                    s g30 "Tentacles?!"
                    "Zukkerthrot" "{b}*Low roar*{/b}"
                    c r42 "[playerName], what did you do?!"
                    scene black with fade
                    s "What is that thing?!"
                    a "It's got my hair!"
                    c r40 "Put me down!"
                    "What unfurls is a scene straight out of a Japanese porn.{w} You grab your popcorn and your camera."
                    s "Ahh! Ah! Ah! Ahhh! ♥♥♥"
                    c "Oooh yes, Oh my God! ♥♥♥ Ah! Ah! Oh! ♥♥♥♥♥"
                    a "{b}*Muffled*{/b} I can't fit any more!"
                    a "Well okay... maybe one mo-... AHHH! ♥♥♥♥♥"
                    y "Neat."
                    if tentaclePic == False:
                        $ tentaclePic = True
                        show white
                        play sound "audio/sfx/camera.mp3"
                        hide white with d3
                        pause 0.5
                        show picTentacle:
                            xalign 0.5 yalign 0.5
                        with dissolve
                        pause
                        play sound "audio/sfx/itemGot.mp3"
                        "A new photo has been added to your photoalbum."
                        hide picTentacle with d3
                        scene bgMap:
                            zoom 0.5
                        with fade
                        jump jobReport
                elif True:
                    "You couldn't find anything of interest."
                    scene bgMap:
                        zoom 0.5
                    with fade
                    jump jobReport
            "You come across a desecrated shrine."
            y "It couldn't possibly be..."
            y "A shrine to Zukkerthroth, destroyer of moons!{w} So there {i}'are'{/i} other believers in this city!"
            menu:
                "Fix up the shrine" if True:
                    $ shrineRestored += 1
                    "You spend some time cleaning up the shrine and putting back the miniature tentacle monsters right side up."
                    y "There we go..."
                    "{b}*Grateful noises from beyond time and space.*{/b}"
                    scene bgMap:
                        zoom 0.5
                    with fade
                    jump jobReport
                "Head back home" if True:
                    y "Oh well, I'll deal with this later."
                    "You decide to head back home instead."
                    scene bgMap:
                        zoom 0.5
                    with fade
                    jump jobReport
        jump worldmap

default spiritEncounter = 0
image spiritPumpkin = "gui/itemUI/items/itemTreatBag2.png"
label halloweenEvent:
    if spiritEncounter == 0:
        stop music fadeout 2.0
        $ spiritEncounter = 1
        pause 0.3
        scene black with fade
        pause 0.5
        scene bgStreet4 with fade
        pause 1.0
        y "......................."
        show scene_darkening
        show scene_fighting
        with d3
        play music "audio/music/stealth1.mp3" fadein 3.0
        "???" "OooooOOOOOOooooooo~...."
        y "....?"
        show spirit at ri with d10
        "???" "OOOOOooooooOOOOOOooooo~.....!{w} I'm a ghoooooooost!"
        y "..............."
        y "Ironically not the craziest thing I've seen today."
        "???" "I am the ghost of Christmas long long ago, in a galaxy far far awaaaaay~......"
        y "Okay, just to be sure. Are you a {i}'real'{/i} ghost or another one of my hallucinations?"
        "Spirit" "Fucked if I knoooooOOOOOooooOOOow~...."
        y "..........."
        "Spirit" "I've come to show you the error of your ways and show you the true meaning of Christmaaaaaaaas~...."
        y "It's October."
        "Spirit" "What?"
        y "It's October. {w}You're early."
        "Spirit" "..............."
        "Spirit" "I travelled all this way and showed up at the wrong time?{w} Next you'll be telling me your name isn't Harold."
        y "..........................."
        "Spirit" "You're not Harold, are you...?"
        y "Sorry buddy, this just isn't your day."
        y "Best go back to the afterlife or something."
        "Spirit" "Oh I'm not dead, I just say that to mess with people."
        y "..........................."
        "Spirit" "I'm just really bored, okay? I'm stuck floating through space without anyone to talk to!"
        "Spirit" "For all I know, you might just be a figment of my imagination!"
        y "You could be one of mine!"
        "Spirit" "..........................."
        y "........................."
        y "So you wanna go play cards or something?"
        "Spirit" "Yeah okay."
        hide scene_darkening
        hide spirit
        with d3
        scene black with fade
        "You spend the rest of the day playing cards with your new ghost buddy."
        "Spirit" "You've activated my trap card!"
        y "We're playing UNO!"
        pause 1.0
        "In the evening you decide to go back to the base."
        if playerKarma >= 60:
            $ karmaCash = renpy.random.randint(1,4)
            if karmaCash == 1:
                $ cash += 10
                play sound "audio/sfx/itemGot.mp3"
                "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
        jump jobReport
    if spiritEncounter == 1:
        $ spiritEncounter = 2
        pause 0.3
        scene black with fade
        pause 0.5
        scene bgStreet4 with fade
        pause 1.0
        y "......................."
        show scene_darkening
        show scene_fighting
        with d3
        "Spirit" "OooooOOOOOOooooooo~...."
        show spirit at ri with d3
        "Spirit" "OooooOOOO-....{w} Oh, it's you again."
        y "Hey. Still here?"
        "Spirit" "Yeah I tried calling my travel agent.{w} Then I realized I didn't have a travel agent, so I've just been busy knocking over trashcans and scaring dogs."
        y "Wanna play cards?"
        "Spirit" "Yes...."
        hide spirit
        hide scene_darkening
        hide scene_fighting
        with d3
        scene black with fade
        "You spend the day playing games with the spirit."
        pause 1.5
        scene bgStreet4
        show scene_darkening
        show scene_fighting
        with d3
        y "Checkmate!"
        show spirit at ri with d3
        "Spirit" "Man I suck at monopoly...!"
        "The spirit throws away his 20-sided dice."
        y "So what do you wanna play next?"
        "Spirit" "How about some Pazaak?"
        y "............"
        y "What?"
        "Spirit" "Oh you might not have that over here."
        "Spirit" "Do you have podracing on this planet?"
        y "..................."
        "Spirit" "Stripclubs?"
        y "We have those!"
        "Spirit" "Hell yeah!"
        hide spirit
        hide scene_darkening
        hide scene_fighting
        scene black
        with d3
        "You spend the rest of the day with the spirit."
        pause 1.5
        "In the evening you say goodbye and return to the base."
        if playerKarma >= 60:
            $ karmaCash = renpy.random.randint(1,4)
            if karmaCash == 1:
                $ cash += 10
                play sound "audio/sfx/itemGot.mp3"
                "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
        jump jobReport
    if spiritEncounter == 2:
        $ spiritEncounter = 3
        pause 0.3
        scene black with fade
        pause 0.5
        scene bgStreet4 with fade
        show scene_darkening
        show scene_fighting
        show zukker:
            xalign 0.5 yalign 0.0
        with d3
        y "So you see ZUKKERTHROTH, Destroyer of Moons, this is how you set up your dating profile. I don't think you have a creditcard, so I gave you mine. Don't go too crazy with it, all right?"
        y "Now remember that most humans can't see you, so don't be disappointed if they ghost you.{w} Also stay away from anime chicks, they only want you for your tentacles."
        show spirit at ri with d3
        "Spirit" "Hey again. I was hoping to find you he-....{w}ARGHHH!!!!"
        with hpunch
        "Spirit" "WHAT IS THAT?!"
        y "Huh?"
        "Spirit" "THAT! That dripping thing with the thousand arms and eyes!"
        y "{b}*Gasp!*{/b}{w} ZUKKERTROTH, He can see you!"
        "Zukkerthroth" "{b}*Happy puppy noices*{w} *followed by the screams of a billion damned souls*"
        "Spirit" "You know this thing...?"
        y "Of course, I've been a long time acolyte of the Tentacle Cult.{w} We have a bookclub."
        "Spirit" "Er.... It's nice to meet you...."
        "Spirit" "Not sure if I'm willing to become a cultist just yet though..."
        y "He sometimes grands his followers powers. Like turning invisible and sneaking into the girl's lockerroom."
        with hpunch
        "Spirit" "HALLELUJA, I'VE FOUND MY GOD!"
        hide zukker
        hide spirit
        hide scene_darkening
        hide scene_fighting
        scene black
        with fade
        pause 0.3
        "The three of you spend the rest of the day sneaking into lockerrooms and playing pranks on unsuspecting victims."
        pause 1.5
        "In the evening you say goodbye and return to the base."
        if playerKarma >= 60:
            $ karmaCash = renpy.random.randint(1,4)
            if karmaCash == 1:
                $ cash += 10
                play sound "audio/sfx/itemGot.mp3"
                "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
        jump jobReport
    if spiritEncounter == 3:
        if swCardClaimed and spyGreenActive:
            label eventHall1:
                pass
            if greenOutfit == 1:
                $ greenOutfit = 0
                $ greenOutfitArms = 0
            $ tattoo15Sam = True
            $ greenChest = 8
            $ greenBottom = 8
            $ greenHair = 8
            $ greenAcces1 = 0
            $ greenShoes = 0
            $ greenUnder = 0
            $ greenHat = 0
            $ spiritEncounter = 4
            scene black with fade
            pause 0.5
            scene bgStreet4
            show scene_darkening
            show scene_fighting
            with fade
            pause 0.4
            show spirit at ce
            with d3
            pause 0.3
            stop music fadeout 3.0
            y "Hey man, how've you been?"
            "Spirit" "Same old. I'm pretty sure I gave someone a heartattack earlier."
            y "You gotta be careful with tha-..."
            s "[playerName], there you are!"
            y "....?"
            y "Oh that's one of the spies I talked to you about. Sam, over here!"
            play music "audio/music/ahsoka.mp3" fadein 1.0
            show green g28:
                xalign 1.1 yalign 0.0
            show spirit at ce:
                xzoom -1
            with d3
            pause 0.1
            show spirit:
                xalign 0.5 yalign 0.0
                linear 0.1 xalign 0.4
            pause 0.4
            "Spirit" "!!!"
            "Spirit" "Ahso-....?"
            "Spirit" "........................."
            s " Is... is that a ghost...?!"
            y "He's my new friend!"
            s g30 "O-oh... er... nice to meet you...?"
            "Spirit" "....................."
            s g16 "......?"
            s g29 "Are you...{w} sad...?"
            pause 1.2
            "Spirit" "..................."
            "Spirit" "You remind me of an old friend...{w} One I haven't seen in a very long time..."
            "Spirit" "I'm sorry...{w} I don't feel like hanging out today."
            hide spirit with d10
            pause 0.5
            s "He-... He disappeared...."
            s "Was it something I said...?"
            y "I don't know..."
            y "......?"
            y "Hey what's this...?"
            hide green with d3
            $ hallCandy += 1
            show bgRewardHall with d3
            show spiritPumpkin:
                xalign 0.5 yalign 0.4
            with d3
            pause
            play sound "audio/sfx/unpack.mp3"
            hide spiritPumpkin
            with d3
            show tattoo:
                xalign 0.5 yalign 0.45 zoom 0.8
            with d3
            "You find a new tattoo design."
            hide tattoo
            with d3
            show hallCandy:
                xalign 0.5 yalign 0.5
            with d3
            "You find a pile of candy."
            hide hallCandy
            hide bgRewardHall
            with d3
            pause 0.3
            y "There's a note here aswell..."
            y "{i}'Hey buddy, if you're reading this, then I've gone back to my own galaxy.{w} In the spirit of things, I've left you some tattoo designs for your girls.{w} I hope we'll meet again some day, for now I must say farewell. I have an orange friend to find.'{/i}"
            y "{i}'-Spirit of Christmas Past'{/i}"
            y "............................."
            show green g16 at ri with d3
            s "He's gone....?"
            if samSocial >= 40:
                menu:
                    "Hug Sam" if True:
                        with hpunch
                        s "!!!"
                        s "Heh... [playerName]. What was that all about?"
                        y "I don't know..."
                        y "Well regardless, it's getting late. Let's head back to the base."
                    "Don't hug Sam" if True:
                        s "You think that he lost someone...?"
                        y "I don't know..."
                        y "Well regardless, it's getting late. Let's head back to the base."
            elif True:
                y "I guess so..."
                y "Come, let's go back to the base."
            stop music fadeout 3.5
            hide green
            hide scene_darkening
            hide scene_fighting
            scene black
            with longFade
            pause 0.5
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        elif True:
            $ tattoo15Sam = True
            $ greenChest = 8
            $ greenBottom = 8
            $ spiritEncounter = 4
            scene black with fade
            pause 0.5
            scene bgStreet4
            show scene_darkening
            show scene_fighting
            with fade
            pause 0.4
            show spirit at ri
            with d3
            pause 0.3
            y "Hey man, how've you been?"
            "Spirit" "Not bad. Have you run into the chick handing out coupons yet? She tried to threaten me with a gun!"
            "Spirit" "When I told her I was the ghost of Christmas past, she mistook me for Santa Claus and gave me her wishlist...."
            y "Yeah we got a bit of a gang problem over here..."
            y "Up for having some fun? I heard a new tiddie bar opened up recently."
            "Spirit" "Hell yeah!"
            hide spirit
            scene black
            with fade
            pause 0.4
            scene bgBar
            hide scene_darkening
            with fade
            pause 0.2
            show scene_darkening
            with d3
            show spirit at ri
            with d3
            "Spirit" "Hey... isn't this {i}'your'{/i} bar?"
            y "It sure is! And I don't have to pay to eat here!"
            "Spirit" "So I'm a bit light on this universe's currency, soooo...."
            y "No worries, I'll spot you."
            $ greenChest = 2
            $ greenBottom = 2
            $ greenShoes = 2
            $ greenHat = 2
            show green g14 at ce
            with d3
            s "Welcome to MEGA MILK, how may I serv-..."
            s g1 "Oh, hi [playerName]. "
            if greenDayJob != 4:
                y "Sam? Didn't I send you off on a different job?"
                s "Yeah, I'll go in a minute, I still have some things to take care off around the...{w} bar....?"
            elif True:
                y "Hey Sam. How's the bar been today?"
                s "Hm, it's fine. Nothing much to....{w} report...?"
            hide green with d2
            show green g30 at ce:
                xzoom -1
            with d3
            "Spirit" "Hey."
            hide green
            show green g28 at ce:
                xalign 0.5 yalign 0.0 xzoom -1
                linear 0.1 xalign 0.4
            s "Is that a ghost?!"
            y "Oh right, Sam, meet the Ghost of Christmas past.{w} Ghost of Christmas Past, this is Sam."
            s g30 "A p-pleasure to meet you...?"
            "Sam takes your order and heads off."
            hide green with d3
            pause 0.1
            y "Can you even eat in your ghost form?"
            "Spirit" "Guess we're about to find out!"
            "Spirit" "Even then, just the sight of food will be welcome. The place I'm at doesn't really have....{w} Anything."
            y "Sounds awful. Doesn't your galaxy have fast food?"
            "Spirit" "Oh yeah we do. I'm even friends with the galaxy 6th largest supplier of fast food... {w}or... {i}'was'{/i} friends with her, I should say."
            "Spirit" "I sorta helped this crazy redhead blow her up in a firey explosion...."
            y ".................."
            y "So where are you now?"
            "Spirit" "On my space station. Or what's left of it. Trying desperately to repair it...{w} By myself."
            y "And how's that coming along?"
            "Spirit" "..........................."
            "Spirit" "You wouldn't so happen to know anything about hyperdrive technology, would you...?"
            y "Nope."
            "Spirit" "In that case, it's going pretty terrible."
            "Spirit" "I might have to give up the dream of being a criminal kingpin. Go back to smuggling, maybe go see some old friends."
            "Spirit" ".............................."
            "Spirit" "Man, it's been so long. I wonder how she's been..."
            y "She?"
            "Spirit" "It's a long story..."
            "Spirit" "Hey buddy... I think... I think it's time for me to go back to my own galaxy."
            y "You're leaving already?"
            "Spirit" "Yeah, I can't keep running away from my problems. It's been fun, but tensions are rising in my galaxy..."
            "Spirit" "Tell Zukkerthroth I said goodbye, all right?"
            y "I'm sorry to see you go, man."
            "Spirit" "Me too, but I'm sure we'll bump into eachother again someday. Take care, all right?"
            y "........................"
            y "Okay buddy. Take care."
            "Spirit" "And remember, the joy of Christmas lives inside you! {size=-5}Something something Tiny Tim{/size}, {size=-10}someting something giant turkey{/size}{size=-15}, something something God bless us all or whatever....{/size}"
            hide spirit with d10
            pause 1.0
            y "................................................."
            hide scene_darkening
            scene black
            with longFade
            scene bgMap:
                zoom 0.5
            with fade
            jump worldmap

    if spiritEncounter == 4:
        scene bgStreet4 with fade
        pause 0.8
        y "....................................."
        "There's nobody here."
        scene bgMap:
            zoom 0.5
        with d3
        jump worldmap

default xmasUpdateStage = 0
image santa = "models/santa/santa.png"
label christmasUpdate:
    if xmasUpdateStage == 0:
        $ xmasUpdateStage = 1
        $ xmasAnnouchment = False
        scene bgBase with fade
        show scene_darkening with d3
        if spyGreenActive:
            show green g1 at ri with d3
        if spyRedActive:
            show red r1 at ce with d3
        if spyYellowActive:
            show yellow y1 at le with d3
        y "Good morning gir-...."
        with hpunch
        "Girls" "It's Christmas!!!!"
        y "Er...!!!"
        "{b}♫♪*Loud Christmas music blaring*♫♪{/b}"
        y "!!!"
        y "Okay okay! Go have a merry old time somewhere else! {w}Humbug!"
        if spyGreenActive:
            s "Don't forget to check out the mall for some seasonal outfits!"
        elif spyRedActive:
            c "Don't forget to check out the mall for some seasonal outfits!"
        elif spyYellowActive:
            a "Don't forget to check out the mall for some seasonal outfits!"
        hide green
        hide red
        hide yellow
        with d3
        show bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if xmasUpdateStage == 1:
        $ xmasUpdateStage = 2
        scene bgStreet3 with fade
        pause 0.8
        y "Bah.... Humbug... What's so good about Christmas anyways...?"
        "{size=-16}{b}*Whisper*{/b} Ho Ho Ho {b}*Whisper*{/b}{/size}"
        y "....?"
        "{size=-12}{b}*Whisper*{/b} Ho Ho Ho {b}*Whisper*{/b}{/size}"
        y "Is somebody there...?"
        with hpunch
        "{size=+8}{b}*Whisper*{/b} Ho Ho Ho {b}*whisper*{/b}{/size}"
        show scene_darkening
        show santa:
            xalign 0.9 yalign 0.0
        with d3
        y "AHH!{w} Oh.... You're just some kind of mall santa..."
        santa "YOUR MOTHER IS A HOE!"
        y "What the...?!"
        santa "I am the Slut Shaming Santa! I have my naughty list of {size=+6}{b}SLUTS{/b}{/size}. {w}Your mother is on there."
        santa "And you better believe I checked it twice, cause your momma is HOT!"
        y "Listen, I don't know who you are but..."
        santa "Now let's have a look at Sam, Clover and Alex now, shall we?!"
        y "Wait how do you know....?"
        santa "................."
        if slutLevel <= 3:
            $ injectorSmall += 1
            santa "Hm... the list says they're not slutty at all!"
            y "Tell me about it."
            santa "Well this is no good at all! How can I slut shame them if they're all a bunch of stuck up prudes!"
            santa "Come, sit on my lap and tell uncle Santa about it."
            y "I don't really want t-...."
            with hpunch
            santa "{size=+10}LAP!{/b}"
            y "Ahh!"
            hide santa
            scene bgStreet3
            with fade
            "A quick explaination later."
            show santa:
                xalign 0.9 yalign 0.0
            with d3
            santa "It sounds like your spies are slut material, but they haven't reached their peak-thotness yet."
            santa "Know what they need. A little bit of....{i}'Holiday Spirit'{/i}"
            "The Slut Shaming Santa hands you a syringe."
            y "................"
            y "Is this heroine?"
            santa "NO YOU IDIOT!"
            santa "Trust me, give this to your girls and it will bring out their inner SLUT!"
            y "Er.. well thank y-..."
            santa "LIKE YOUR MOMMA!"
        if slutLevel >= 3:
            santa "As I thought, they've begun on their journey of sluttiness!"
            y "If you say so..."
            y "(Weirdo)."
            y "Wait, aren't you the Slut Shaming Santa? Shouldn't you be opposed to them being slutty?"
            santa "Without sluts I'd be out of a job! The more sluts the more I get to shame, so it's a win-win for me."
            santa "You deserve a reward for your dilligent slutiness training. Here!"
            "The santa hands you a box filled with gadget materials."
            y "Oh... Thanks, this will actually really help."
            santa "Don't thank me. I'm off to visit YOUR MOTHER now! That fucking slut!"
            y "Stop talking about my mother!"
        santa "Now I must be off, there are many more sluts that need shaming!"
        show santa:
            linear 0.1 xalign 0.91 yalign 0.0
            linear 0.1 xalign 0.90 yalign 0.0
            linear 0.1 xalign 0.91 yalign 0.0
            linear 0.1 xalign 0.90 yalign 0.0
            linear 0.1 xalign 0.91 yalign 0.0
            linear 0.1 xalign 0.90 yalign 0.0
            linear 0.1 xalign 0.9 ypos -600
        pause 1.5
        hide santa
        y "....."
        y "He flew off...."
        y "Sometimes I wonder if I really am crazy, or if the world went insane when I was locked up."
        if slutLevel <= 3:
            "Voice" "Best not to think about it too much.{w} So what's in that syringe?"
            y "...?"
            y "Hey is this...?"
            show scene_fighting with d2
            show tutDart:
                xalign 0.5 yalign 0.5
            with d3
            pause
            hide tutDart with d3
            y "It's a nanobot injector.{w} This might come in handy."
            "You put away the syringe and spend the rest of the day being grumpy about Christmas."
            "When it gets late you head back to the base."
            hide scene_darkening with d3
            scene bgMap:
                zoom 0.5
            with d3
            if playerKarma >= 60:
                $ karmaCash = renpy.random.randint(1,4)
                if karmaCash == 1:
                    $ cash += 10
                    play sound "audio/sfx/itemGot.mp3"
                    "On your way back you find {color=#ffeda6}$ 10,-{/color} on the street! {w}That's what you get from having good karma."
            jump jobReport
        elif True:
            "Voice" "Well at least you got some free gadget materials out of it."
            y "True."
            scene bgMap:
                zoom 0.5
            with d3
            jump jobReport
    if xmasUpdateStage == 2:
        $ xmasUpdateStage = 3
        scene mallBG with fade
        pause 0.8
        y "............."
        y "Look at all these wasteful decorations. The bright colors hurt my eyes. The candy canes are giving me cavities just by looking at them!{w} Bah, humbug!"
        "You angerly walk into the bookstore."
        show scene_darkening with d3
        $ clerkFace = 2
        show clerk at ri with d3
        "Clerk" "Welcome to the store! Happy Holida-..."
        y "HUMBUG!"
        $ clerkFace = 1
        "Clerk" "..........."
        "Clerk" "Not a fan of the holidays then?"
        y "I don't like this stupid holiday. The hats, the trees, the.... everything."
        $ clerkFace = 2
        "Clerk" "Maybe you should visit the mall Santa we hired this year! I think I hear him now!"
        "???" "Hoe hoe hoe!"
        y "Uh oh, not him again..."
        show santa at le with d2
        santa "BOOK STORE CASHIER GIRL!"
        "Clerk" "Oh hi san-..."
        santa "YOU'RE A HOE!"
        "Clerk" "What...?"
        santa "YOU'RE A HOE AND YOU SELL HOE BOOKS!"
        santa "HOE TOYS, HOE OUTFITS TO YOUR HOE CUSTOMERS!"
        $ clerkFace = 1
        "Clerk" "Well I mean... you're not wrong, bu-..."
        santa "YOU'RE GOING TO DIE ALONE AND SAD, WISHING YOU HADN'T BEEN SUCH A HOE IN LIFE!"
        $ clerkFace = 2
        "Clerk" "B-but....!"
        santa "AND NAUGHTY GIRLS GET COAL!"
        with hpunch
        "The Santa dropped a sack of coal all over the floor."
        "Clerk" "Hey!"
        santa "NOW TRY TO BE LESS OF A HOE NEXT YEAR!"
        santa "SANTA AWAY!"
        show santa at le:
            linear 0.5 xalign -1.0 yalign 0
        pause 1.5
        $ clerkFace = 1
        "Clerk" "....................."
        "Clerk" "I think I lost my holiday spirit as well now...{w} Humbug..."
        hide clerk with d3
        hide scene_darkening with d3
        jump jobReport
    if xmasUpdateStage == 3:
        if gang4Active or socialSilva >= 8:
            $ xmasUpdateStage = 4
            scene bgStreet2 with fade
            pause 0.8
            y "Let's see what Sil is up to today..."
            pause 0.3
            show scene_darkening with d3
            "???" "Hoe hoe hoe~...."
            y "Oh no, not here too!"
            show silvaModel at ri with d3
            sil "Oh, bonjour mon ami."
            y "Sil...? What are you doing?"
            sil "Oh not much, I am just trying out my new hoe to till the soil."
            y "...................."
            y "Well at least there's no Christmas decorations over here."
            sil "Oh, but you'd be wrong! I'm planting a pine tree right now!"
            sil "I don't really like humans, but even I love human traditions like Christmas!"
            sil "Want to help me decor-....?"
            y "Shh!{w} You hear that...?"
            "{size=-16}{b}*Whisper*{/b} Ho Ho Ho {b}*Whisper*{/b}{/size}"
            y "Oh no..."
            sil "What iz zhat?"
            santa "HOE HOE HOE!"
            with hpunch
            show santa at le with d2
            santa "AND WHAT DO WE HAVE HERE?! SOME KIND OF VEGAN PROSTITUTE?!"
            sil "I'm sorry, what?!"
            santa "IF THERE'S ONE THING THAT I HATE MORE THAN HOES, IT'S HIPPY HOES!{w} GET A JOB HIPPY!"
            sil "Iz this a friend of yours?"
            y "No, he's been terrorizing the town for a while now."
            sil "In that case, I might introduce him to my plants...."
            santa "I HEARD PLANTS GROW BETTER IF YOU TALK TO THEM!{w} BUT I BET YOU JUST MOAN AT THEM WHILE YOU JERK OFF TO IMAGES OF SPINAGE!"
            sil "{b}*Gasp*{/b}! Don't zay such unseemly things in front of ze young buds!"
            santa "NO WONDER YOU LIKE PLANTS! I KNOW WHAT YOU DO TO THOSE EGGPLANTS!!!"
            sil "Zhat is it! No more Ms. Nice Gal! {w}Plants, eat zhat uncouth mad man!"
            santa "HAH! YOU CAN'T KILL SANTA CLAUSE! SANTA AWAAAAAAY!"
            hide santa with d2
            pause 1.5
            sil "................."
            y ".................."
            y "You still want my help decorating your Christmas tree?"
            sil "No, Christmas is stupid!{w} Now if you will excuse me, I'm going to cry into a lettuce..."
            hide silvaModel
            hide scene_darkening
            with d3
            jump jobReport
        elif True:
            y "Maybe I should do some exploring to get my head off of things."
            jump worldmap
    if xmasUpdateStage == 4:
        if hackerUnlocked:
            $ xmasUpdateStage = 5
            scene bgStreet2 with fade
            pause 0.8
            y "Let's see what Mathias is up to to-...."
            "You cautiously look around."
            y "...up to today."
            show scene_darkening with d3
            pause 0.3
            show matModel at ri with d3
            y "Hey Mathias, what's going on with you today?"
            mat "Oh hey, not much. I made a new frien-..."
            y "Is it Santa Claus?"
            mat "Er... How did you kno-...?"
            santa "HOE HOE HOE!"
            show santa at ce
            with hpunch
            santa "FANCY SEEING YOU HERE!"
            y "Oh goddamn it. Can you get out of here already?"
            santa "NOT AS LONG AS THERE ARE SLUTS WORTH SHAMING!{w} TAKE THIS GUY FOR EXAMPLE! HE HAS ENTIRE HARDDRIVE FULL OF SLUTS!"
            mat "Er...."
            santa "HE HAS SO MANY SLUTS, I'M SURPRISED HE'S NOT ONE HIMSELF!"
            mat "I could get a girlfriend if I wante-..."
            santa "BUT HE'S TOO MUCH OF A SCARED PUSSY TO ASK A GIRL OUT ON A DATE!"
            mat "Dude! Not cool!"
            santa "WELL I'LL LEAVE YOU TWO LOSERS TO CRY IT OUT WHILE I GO AND DO SOMETHING THAT'S ACTUALLY IMPORTANT!"
            y "Like shame sluts?"
            santa "EXACTLY! SANTA AWAAAAAY~....!"
            show santa:
                linear 0.3 xalign 0.5 yalign 0.5 rotate 360
                linear 0.3 xalign 0.5 yalign 0.5 rotate 720
                linear 0.3 xalign 0.5 yalign 0.5 rotate 1080
            pause 0.9
            hide santa
            pause 0.3
            y "......................"
            mat "...................."
            mat "I could totally get a girlfriend..."
            mat "Man this is the worst Christmas ever...."
            hide matModel with d3
            pause 0.6
            y "(This Santa is really getting on everyone's nerves.)"
            y "(I think it's time to put a stop to him...)"
            hide scene_darkening with d3
            jump jobReport
        elif True:
            y "Hm... No Santa around today. I might have to do some more exploring."
            jump worldmap
    if xmasUpdateStage == 5:
        $ xmasUpdateStage = 6
        $ photoClaus = True
        scene bgStreet1 with fade
        pause 0.8
        show scene_darkening with d3
        y "Plane Ticket: {w}Check."
        y "Warm clothing:{w} Check."
        y "Camera:{w} Check."
        show santa at ri with d2
        santa "GOING SOMEWHERE FUCKBOY?!"
        y "Yes, as far away from you as possible."
        santa "HAH! RUN ALL YOU WANT, I'LL BE HERE WAITING FOR YOU WHEN YOU COME BACK!"
        y "(I'm counting on it.)"
        hide santa
        scene black
        hide scene_darkening
        with fade
        pause 1.0
        "Now leaving for destination: The North Pole."
        play sound "audio/sfx/ship.mp3"
        pause 1.0
        "???" "Oh! Who are you?"
        "???" "Oh my~.... {b}*Giggles*{/b}"
        "???" "Yes! Harder, harder! Ahhh!"
        "???" "Oohh! Ooohhhh! Ooooooohhh! ♥♥♥♥♥♥"
        pause 2.0
        play sound "audio/sfx/ship.mp3"
        scene bgStreet1 with longFade
        pause 0.8
        show scene_darkening with d3
        show santa at ri with d2
        santa "LOOK WHO'S BACK! ENJOYED YOUR LITTLE HOLIDAY?!"
        y "Sure did."
        santa "AND NOW YOU'RE BACK! JUST LIKE I PREDICTED! I WENT BY YOUR MOMMA'S HOUSE AT LEAST TWICE WHILE YOU WERE AWAY!"
        y "That's nice."
        santa "WHERE DID YOU GO ANYWAYS?"
        y "The North Pole."
        santa "THE WHAT?!"
        y "Yeah, very rude of you to leave your wife all alone on Christmas. Luckily I was there to show Mrs. Claus the true meaning of Christmas."
        "You show Santa the picture you took of Mrs. Claus."
        show expression "gui/photos/other/picClaus.jpg":
            xalign 0.5 yalign 0.5
        with d3
        pause
        hide expression "gui/photos/other/picClaus.jpg" with d3
        santa "THAT HOE!"
        santa "DON'T THINK THIS IS OVER! YOU HAVEN'T SEEN THE LAST OF MEEEEEE!"
        show santa:
            linear 0.15 xalign 0.9 zoom 0.01
        pause 0.2
        hide santa
        pause 1.5
        if firstPick == 1:
            show green g1 at ri with d3
            s "Oh, [playerName] there you are!"
            s "I was wondering where you were! Where did you go?"
            y "To find the true meaning of Chrismas."
            s "And did you find it?"
            y "I sure did. Come, let's decorate the bar."
            s "{b}*Cheers*{/b}"
            hide green with d3
        if firstPick == 2:
            show red r1 at ri with d3
            c "Oh, [playerName] there you are!"
            c "I was wondering where you were! Where did you go?"
            y "To find the true meaning of Chrismas."
            c "And did you find it?"
            y "I sure did. Come, let's decorate the bar."
            c "{b}*Cheers*{/b}"
            hide red with d3
        if firstPick == 3:
            show yellow y1 at ri with d3
            a "Oh, [playerName] there you are!"
            a "I was wondering where you were! Where did you go?"
            y "To find the true meaning of Chrismas."
            a "And did you find it?"
            y "I sure did. Come, let's decorate the bar."
            a "{b}*Cheers*{/b}"
            hide yellow with d3
        pause 0.4
        play music "audio/music/xmas.mp3" fadein 1.0
        scene white with dissolve
        pause 0.5
        scene bgXmas with dissolve
        pause
        jump jobReport
    elif True:
        call screen mapButtons

label finaleAirportAssault:
    if mapSpy4Selected:
        $ spy4Status = 1
        $ mapSpy4Selected = False
    if mapSpy5Selected:
        $ spy5Status = 1
        $ mapSpy5Selected = False
    if mapSpy6Selected:
        $ spy6Status = 1
        $ mapSpy6Selected = False
    if mapSpy0Selected:
        $ spy0Status = 1
        $ mapSpy0Selected = False
    call screen mapButtonsRaidFinale

"ERROR. You're not suppose to read this. worldmap.rpy - end of script detected"
jump jobReport
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
