


default skillTakedown = 0
default skillHack = 0
default skillSecondChance = 0

screen skillScreen:
    add "gui/skills/skillScreen.jpg"

label skills:
    if tutStage <= 7:
        y "I better get busy exploring."
        jump worldmap
    show screen skillScreen
    pause
    "Not yet in"
    hide screen skillScreen
    if tutStage == 3:
        jump checkthisoutlater
    elif True:
        jump worldmap

label status:
    if tutStage == 3:
        y "I'll check this out later."
        jump worldmap
    elif True:
        scene bgStatus
        if nanoLevelSam >= 100:
            $ nanoLevelSam = 100
        if nanoLevelClover >= 100:
            $ nanoLevelClover = 100
        if nanoLevelAlex >= 100:
            $ nanoLevelAlex = 100
        call screen status
        jump worldmap


label checkthisoutlater:
    scene bgMap:
        xalign 0.63 yalign 0.3 zoom 1.0
    call screen mapButtons


label lore:
    if tutStage == 3:
        y "I don't have time for that right now."
        jump checkthisoutlater
    elif True:
        scene bgLore
        call screen bgLore
        jump worldmap

label itemsScreen:
    if tutorialActive:
        "Not yet in"
        jump checkthisoutlater
    "Show items screen here. NOT IN YET"
    jump worldmap

label exploreMap:
    if tod == 1:
        if tutStage == 3:
            jump tutStage4
        if tutStage == 7 and spyGreenActive and greenDayJob == 0 or tutStage == 7 and spyRedActive and redDayJob == 0 or tutStage == 7 and spyYellowActive and yellowDayJob == 0:
            y "I should probably send my spy out to bring back some intel first."
            call screen mapButtons
        elif True:
            jump explore
    elif True:
        y "I'll wait until tomorrow morning to explore the city."
        jump worldmap












default picQuest1Text = ""
default picQuest2Text = ""
default picQuest3Text = ""
default picQuest4Text = ""
default picQuest5Text = ""
default picQuest6Text = ""
default picQuest7Text = ""

screen picQuestText:
    hbox:
        spacing 10 xalign 0.5 ypos 30 xsize 770
        text "[picQuest1Text]"
    hbox:
        spacing 10 xalign 0.5 ypos 100 xsize 770
        text "[picQuest2Text]"
    hbox:
        spacing 10 xalign 0.5 ypos 170 xsize 770
        text "[picQuest3Text]"
    hbox:
        spacing 10 xalign 0.5 ypos 240 xsize 770
        text "[picQuest4Text]"
    hbox:
        spacing 10 xalign 0.5 ypos 310 xsize 770
        text "[picQuest5Text]"
    hbox:
        spacing 10 xalign 0.5 ypos 380 xsize 770
        text "[picQuest6Text]"
    hbox:
        spacing 10 xalign 0.5 ypos 450 xsize 770
        text "[picQuest7Text]"

label quests:
    if tutStage == 3:
        y "I'll check this out later."
        jump worldmap
    scene missionScreenBG
    menu:
        "{color=#EFD66D}[task7Name]{/color}" if True:
            show screen task7Text
            pause
            hide screen task7Text
            jump quests
        "[task1Name]" if 1 <= task2Stage <= 2:
            show screen task1Text
            pause
            hide screen task1Text
            jump quests
        "[task2Name]" if 1 <= task2Stage <= 14:
            show screen task2Text
            pause
            hide screen task2Text
            jump quests
        "[task4Name]" if 1 <= task4Stage <= 6:
            show screen task4Text
            pause
            hide screen task4Text
            jump quests
        "[task6Name]" if 1<=  task6Stage <= 13:
            show screen task6Text
            pause
            hide screen task6Text
            jump quests
        "[task5Name]" if 1 <= task5Stage <= 7:
            show screen task5Text
            pause
            hide screen task5Text
            jump quests
        "[task10Name]" if 1 <= task10Stage <= 3:
            show screen task10Text
            pause
            hide screen task10Text
            jump quests
        "[task11Name]" if 1 <= task11Stage <= 3:
            show screen task11Text
            pause
            hide screen task11Text
            jump quests
        "[task12Name]" if 1 <= task12Stage <= 4:
            show screen task12Text
            pause
            hide screen task12Text
            jump quests
        "[task13Name]" if 1 <= task13Stage <= 4:
            show screen task13Text
            pause
            hide screen task13Text
            jump quests
        "[task15Name]" if 1 <= task15Stage <= 2:
            if task15Fireworks and task15Music and task15Girls and cash >= 2000:
                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n\n-Plan a mission to the Amusement Park for fireworks.\n-Plan a mission to Punk Web and steal the hottest mixtape.\n-Pick up some thots at school.\n-Have at least $2.000.\n\n-Visit Sam to start the party.")
            show screen task15Text
            pause
            hide screen task15Text
            jump quests
        "[task17Name]" if 1 <= task17Stage <= 6:
            show screen task17Text
            pause
            hide screen task17Text
            jump quests
        "[task18Name]" if 1 <= task18Stage <= 2:
            show screen task18Text
            pause
            hide screen task18Text
            jump quests
        "[task32Name]" if 1 <= task32Stage == 1:
            show screen task32Text
            pause
            hide screen task32Text
            jump quests
        "[task21Name]" if 1 <= task21Stage <= 6:
            show screen task21Text
            pause
            hide screen task21Text
            jump quests
        "Picture Quests" if 1 <= picQuest1 <= 2 or 1 <= picQuest2 <= 2 or 1 <=  picQuest3 <= 2 or 1 <=  picQuest4 <= 2 or 1 <= picQuest5 <= 2 or 1 <=  picQuest6 <= 2 or 1 <= picQuest7 <= 2:
            show screen picQuestText
            pause
            hide screen picQuestText
            jump quests
        "Completed tasks" if True:



            menu:
                "[task1Name]" if task1Stage >= 3:
                    show screen task1Text
                    pause
                    hide screen task1Text
                    jump quests
                "[task2Name]" if task2Stage >= 15:
                    show screen task2Text
                    pause
                    hide screen task2Text
                    jump quests
                "[task4Name]" if task4Stage >= 7:
                    show screen task4Text
                    pause
                    hide screen task4Text
                    jump quests
                "[task5Name]" if task5Stage >= 8:
                    show screen task5Text
                    pause
                    hide screen task5Text
                    jump quests
                "[task6Name]" if task6Stage >= 14:
                    show screen task6Text
                    pause
                    hide screen task6Text
                    jump quests
                "[task10Name]" if task10Stage >= 3:
                    show screen task10Text
                    pause
                    hide screen task10Text
                    jump quests
                "[task11Name]" if task11Stage >= 4:
                    show screen task11Text
                    pause
                    hide screen task11Text
                    jump quests
                "[task12Name]" if task12Stage >= 5:
                    show screen task12Text
                    pause
                    hide screen task12Text
                    jump quests
                "[task15Name]" if task15Stage >= 3:
                    show screen task15Text
                    pause
                    hide screen task15Text
                    jump quests
                "[task17Name]" if task17Stage >= 7:
                    show screen task17Text
                    pause
                    hide screen task17Text
                    jump quests
                "[task18Name]" if task18Stage >= 3:
                    show screen task18Text
                    pause
                    hide screen task18Text
                    jump quests
                "[task21Name]" if task21Stage >= 7:
                    show screen task21Text
                    pause
                    hide screen task21Text
                    jump quests
                "[task32Name]" if task32Stage >= 2:
                    show screen task32Text
                    pause
                    hide screen task32Text
                    jump quests
                "Back" if True:
                    jump quests
        "Back" if True:
            jump worldmap



default task1Name = ""
default task1Text = ""
default task1Stage = 0

screen task1Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task1Text]"




default task2Name = ""
default task2Text = ""
default task2Stage = 0
default task2Target = 0

image agentDistractCin = "mission/enemy/agentDistractCin.png"
image bg1JumpSpecial = "mission/jumps/bg1Jump3.png"

layeredimage spyCrouchCornerTask2:
    always:
        "mission/models/spyHidingCrouch1.png"
    if activeSpy == 3:
        "mission/models/sam/spyCrouchingSuit1.png"
    if activeSpy == 3:
        "mission/models/sam/spyCrouchingHair1.png"
    if activeSpy == 3:
        "mission/models/sam/spyCrouchingFace1.png"
    if activeSpy == 1:
        "mission/models/clover/spyCrouchingSuit1.png"
    if activeSpy == 1:
        "mission/models/clover/spyCrouchingHair1.png"
    if activeSpy == 1:
        "mission/models/clover/spyCrouchingFace1.png"
    if activeSpy == 2:
        "mission/models/alex/spyCrouchingSuit1.png"
    if activeSpy == 2:
        "mission/models/alex/spyCrouchingHair1.png"
    if activeSpy == 2:
        "mission/models/alex/spyCrouchingFace1.png"


screen task2Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task2Text]"

label task2:
    if task2Stage == 0:
        $ task2Stage = 1
        $ task2Name = _("Double Trouble")
        $ task2Text = _("Discussing the situation, it's become clear that we could use the extra backup to take back Beverly Hills. I should set up a mission and send my spy back to school to capture her friend.")
        $ task7Text = _("After my spy returned from her first mission we figured out oxytocin seems to help suppress the nanobots. We can capture agents and use sex to break the control over them. Then use them to help liberate Beverly Hills.\n\nWe will need money and intel to go on future mission, so I should send my spy out to go undercover and collect some intel with the different gangs around town.\n\n{color=#A3A3A3}- with one of the gangs in town.{/color} \n\n{color=#A3A3A3}-Clean up the milkshake bar and convince your spy to work there.{/color}\n\n-???")
        pause 0.5
        scene bgBase with fade
        show scene_darkening
        with d3
        if spyGreenActive:
            y "Okay [greenName]. Today I'm sending you to..."
            y "..............."
            y "[greenName]?"
            show green g19 at ri with d3
            s "Hey [playerName]. Sorry I'm just feeling a bit distracted."
            y "It better not be the nanobots acting up again! You {i}'have'{/i} been suppressing them, right?"
            s g18 "Yeah... well sort of."
            y "Sort of...?"
            s "Anyways, that's not why I was distracted. I was wondering if my friends are doing all right."
            y "The other spies?"
            s g38 "Uhuh. I haven't seen them in days and I'm worried for them..."
            s g14 "Are you sure we can't bring them back here?"
            y "We could... But we'd risk them exposing our plans."
            s g32 "Not if we break their nanobot control!"
            y "Well we could use an extra pair of hands around here. Fine, I'll set up a mission and you can go and find them."
            y "Any idea where they're at?"
            s g37 "Well... Clover is probably still at the school.{w} I don't know of Alex her whereabouts."
            y "We'll worry about her later. For now let's go for the blonde one."
            $ task2Target = 2
            y "I'll set up a mission and you can go after her."
            s g1 "Understood!"
            hide green
            with d3
            hide scene_darkening
            with d3
            call qAccept from _call_qAccept_1
            scene bgMap:
                zoom 0.5
            with fade
            jump worldmap
    if task2Stage == 2:
        $ randomObst2 = 0
        hide obst2
        hide screen equipmentMenu
        $ missionProgression = 0
        show globalImage:
            zoom 0.25
        hide screen interactScreen
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        $ randomExit = 1
        $ currentPosition = 0
        $ randomCover2 = 1
        $ randomCover1 = 1
        $ randomBackground = 1
        $ spyRedActive = True
        show spyReadyTut:
            xalign 0.655 yalign 0.488 zoom 0.21 rotate 5
        show agentDistractCin:
            xalign 0.63 yalign 0.5 zoom 0.28 rotate 5
        with fade
        if spyGreenActive:
            pause 1.0
            show scene_darkening
            with d3
            show agentModel:
                xalign 0.3 yalign 0.0 xzoom -1
            with d3
            pause 0.3
            if hiddenStatus == 0:
                "Agent" "There's no sign of her. Should we keep looking?"
            elif True:
                "Agent" "We've spotted her! She has to be around here somewhere!"
            $ redFace = 100
            $ redOutfit = 1
            $ redOutfitArms = 1
            $ redChest = 0
            $ redBottom = 0
            $ redShoes = 0
            show red:
                xalign 0.7 yalign 0.0
            with d3
            c r11 "Oh she's here all right~...."
            c r23 "She might even be listening to us as we speak..."
            c "...................."
            c r10 "Stay on your guard. She'll be back."
            "Agent" "Yes ma'am!"
            hide red
            hide agentModel
            with d3
            hide scene_darkening
            with d3
            pause 0.3
            hide spyReadyTut
            with d3
            hide agentDistractCin
            with d3
            sM "I spotted her, [playerName]."
            y "Yeah I saw. Try getting her back, but stay on your guard."
            sM "Right."
            scene black with fade
            jump missionBegin
    if task2Stage == 3:
        $ randomObst1 = 0
        $ randomObst2 = 0
        $ randomObst3 = 0
        $ randomObst4 = 0
        hide obst1
        hide obst2
        hide obst3
        hide obst4
        hide screen equipmentMenu
        $ missionProgression = 0
        $ task2Stage = 4
        show globalImage:
            zoom 0.25
        hide screen interactScreen
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        $ randomExit = 2
        $ currentPosition = 0
        $ randomCover2 = 1
        $ randomCover1 = 1
        $ randomBackground = 1
        show spyReadyTut:
            xalign 0.67 yalign 0.485 zoom 0.25 rotate 3
        with fade
        pause 0.5
        if spyGreenActive:
            show scene_darkening
            with d3
            show red r12:
                xalign 0.1 yalign 0.0 xzoom -1
            with d3
            c "You don't have to hide anymore... I know you're there."
            $ greenOutfit = 1
            $ greenNeck = 0
            $ greenHead = 0
            $ greenBottom = 0
            $ greenChest = 0
            $ greenShoes = 0
            $ greenOutfitArms = 1
            show green g34 at ri with d3
            s "Clover, listen I've come to get you out of here."
            c r22 "Oh... I certainly like to see you try."
            c "Guards!"
        stop music fadeout 0.5
        hide scene_darkening
        hide red
        hide green
        with d3
        play music "audio/music/crisis.mp3"
        $ randomObst1 = 1
        $ randomObst2 = 1
        $ hiddenStatus = 2
        show obst1:
            xalign 0.365 yalign 0.43 rotate 2 zoom 0.48 xzoom -1
        with d3
        show obst2:
            xalign 0.623 yalign 0.49 rotate 2 zoom 0.30 xzoom -1
        with d3
        c r12 "Deal with her."
        $ CoS1 = 100
        $ CoS2 = 100
        $ CoS3 = 100
        hide spyReadyTut
        with d3
        call screen interactScreen
    if task2Stage == 5:
        hide screen equipmentMenu
        $ task2Stage = 6
        $ missionProgression = 0
        show globalImage:
            zoom 0.25
        hide screen interactScreen
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        $ randomExit = 1
        $ currentPosition = 0
        $ randomCover2 = 1
        $ randomCover1 = 1
        $ randomBackground = 1
        $ _skipping = True
        show spyReadyTut:
            xalign 0.57 yalign 0.48 zoom 0.35 rotate 3
        with fade
        show scene_darkening
        show red r12:
            xalign 0.0 yalign 0.0 xzoom -1
        with d3
        pause 0.5
        c "................"
        show green g31 at ri with d3
        s "Willing or not, you're coming with me, Clover!"
        c "Fine, I'll deal with you myself..."
        s g8 "Listen to me, I don't want to hurt you!"
        y "Now's your chance, [greenName]. Knock her out and bring her back to the base."
        s g29 "But she's my friend! I can't fight her!"
        c r22 "Remember that one time you left your diary open and said all those embarrassing things?{w} I told everyone about that..."
        s g28 "Oh that bitch....!"
        y "[greenName] there are more Agents on their way. This is the only chance you'll get. Now knock out that blonde and that's an order!"
        s "B-but...!"
        play sound "audio/sfx/shockcrash.mp3"
        pause 0.7
        hide green
        show white
        pause 0.05
        hide white
        show bgControl
        show green g100 at ri
        pause 0.6
        hide bgControl
        pause 0.2
        s "I obey..."
        $ _skipping = False
        hide scene_darkening
        hide green
        hide red
        with d3
        hide spyReadyTut
        show spyFightTut:
            xalign 0.57 yalign 0.48 zoom 0.35 rotate 4
        with d3
        call screen interactScreenSpecial1
    if task2Stage == 7:
        $ task2Stage = 8
        hide spyCorner
        with d1
        play sound "audio/sfx/punch1.mp3"
        hide spyFightTut
        show spyGuardTut:
            xalign 0.575 yalign 0.485 zoom 0.32 rotate 4
            linear 0.1 xalign 0.58
            linear 0.1 xalign 0.575
            linear 0.1 xalign 0.58
            linear 0.1 xalign 0.575
            linear 0.1 xalign 0.58
            linear 0.1 xalign 0.575
            linear 0.1 xalign 0.58
            linear 0.1 xalign 0.575
        show spyCombat2:
            xalign 0.51 yalign 0.49 zoom 0.33 rotate 4
        with d1
        pause 0.1
        hide spyCombat2
        play sound "audio/sfx/punch1.mp3"
        show spyCombat3:
            xalign 0.51 yalign 0.47 zoom 0.37 rotate 4
        with d1
        pause 0.1
        hide spyCombat3
        play sound "audio/sfx/punch1.mp3"
        show spyCombat1:
            xalign 0.51 yalign 0.43 zoom 0.41 rotate 4
            linear 0.5 yalign 0.41
        with d1
        pause 0.3
        play sound "audio/sfx/punch1.mp3"
        hide spyCombat1
        hide spyReadyTut
        scene black
        with hpunch
        pause 1.0
        $ _skipping = True
        if spyGreenActive:
            "Sam wrestles Clover to the ground with ferosity!"
            "She grabs her wrists and pins her to the ground."
            sM "Target subdued sir!"
            y "Awesome!"
            y ".................."
            y "Now kiss."
            sM "Yes sir."
            "Without hesitation Sam deeply kisses the blonde spy!"
            scene kiss1 with fade
            pause
            c "Mhmp!!"
            c "Mphm~..."
            c "......................"
            scene black with fade
            $ greenFace = 1
            $ redFace = 1
            show globalImage:
                zoom 0.25
            with d5
            pause 0.5
            show scene_darkening
            with d4
            pause 0.5
            show red r29:
                xalign 1.0 yalign 0.0
            show green g14 at le
            with d3
            c "Sam...."
            c "What happened....?"
            s "I don't know... I just..."
            y "Woah you actually did it! Damn [greenName] I didn't expect that from you."
            s g28 "Y-you...! It's not what it seems!"
            y "Save it for later girls, you two need to get out of there now!"
            hide scene_darkening
            hide red
            hide green
            with d2
        $ missionProgression = 6
        $ hiddenStatus = 1
        $ randomObst1 = 1
        $ randomObst2 = 1
        show obst1:
            xalign 0.365 yalign 0.43 rotate 2 zoom 0.48
        with d3
        show obst2:
            xalign 0.623 yalign 0.49 rotate 6 zoom 0.30
        with d3
        "Agent" "I sure love going on patrol!"
        "Agent" "Wait you're that intruder!"
        y "Get to the entrance of the school, I'll pull the two of you out of there!"
        play sound "audio/voice/onIt2.mp3"
        stop music fadeout 2.0
        sM "On our way!"
        $ _skipping = False
        hide obst1
        hide obst2
        scene black
        with d2
        $ hiddenStatus = 2
        play music "audio/music/sneaking1.mp3" fadein 1.0
        $ backupCloverActive = True
        jump missionBegin
    if task2Stage == 8:
        hide screen equipmentMenu
        $ task2Stage = 9

        $ frontExit = 0

        $ randomExit = 3
        $ _skipping = True
        $ currentPosition = 0
        $ randomCover2 = 1
        $ randomCover1 = 1
        $ randomBackground = 1
        show globalImage:
            zoom 0.25
        with d3
        hide screen interactScreen
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        show spyCrouchCornerTask2:
            xalign 0.96 yalign 1.35 zoom 0.57 rotate 6 xzoom -1
        with d3
        $ spyRedActive = True
        if activeSpy == 1:
            $ spyRedActive = True
            s "It looks clear."
            c "Hang on..."
        if activeSpy == 2:
            $ spyYellowActive = True
            c "It looks clear."
            a "Hang on..."
        if activeSpy == 3:
            $ spyGreenActive = True
            a "It looks clear."
            s "Hang on..."
        show obstHulk:
            xalign 0.67 yalign 0.5 zoom 0.2
        with d3
        pause 0.5
        hide obstHulk
        with d3
        pause 0.3
        show obstHulk:
            xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
        with d3
        "Agent" "I'm guarding this exit like a chump!"
        if activeSpy == 1:
            s "Woah!"
            c "Yeah he's gonna be tough to slip past. We're gonna have to fight him."
            c "I'm gonna find a more advantages spot. Use your compowder to call in backup and I'll help you fight it."
        if activeSpy == 2:
            c "Woah!"
            a "Yeah he's gonna be tough to slip past. We're gonna have to fight him."
            a "I'm gonna find a more advantages spot. Use your compowder to call in backup and I'll help you fight it."
        if activeSpy == 3:
            a "Woah!"
            s "Yeah he's gonna be tough to slip past. We're gonna have to fight him."
            s "I'm gonna find a more advantages spot. Use your compowder to call in backup and I'll help you fight it."

        $ randomObst1 = 0
        $ randomObst2 = 0

        $ backup1 = 6
        $ backup2 = 6
        $ backup3 = 6
        $ bagRadioName = "Backup"
        hide spyCrouchCornerTask2
        with d2
        $ _skipping = False
        play sound "audio/sfx/compowder.mp3"
        show screen equipmentMenu
        call screen interactScreen
    if task2Stage == 9:
        $ task2Stage = 10
        $ task2Text = _("Discussing the situation, it's become clear that we could use the extra backup to take back Beverly Hills. I should set up a mission and send my spy back to school to capture her friend. \n\nWe brought back a new spy, but the nanobot control seems to be getting worse. I should check my crafting table to see if there's something in WOOHP's database about that.\n\n-Check the Equipment tab in your workbench.")
        $ tod = 2
        stop music fadeout 1.5
        scene black with fade
        scene bgBase with fade
        pause 0.5
        show scene_darkening
        with d3
        play music "audio/music/nighttime.mp3" fadein 1.5

        if firstPick == 0:
            $ firstPick = 1
        if firstPick == 1:
            $ greenShoes = 0
            $ greenNeck = 0
            $ greenChest = 0
            $ greenBottom = 0
            $ greenOutfit = 1
            $ greenOutfitArms = 1
            $ redChest = 0
            $ redBottom = 0
            $ redOutfit = 1
            $ redOutfitArms = 1
            show green g34 at ri with d3
            s "We're back."
            y "So you are..."
            show red r14:
                xalign 0.2 yalign 0.0 xzoom -1
            with d3
            c "Ngh~...."
            y "And this must be Clover."
            c r30 "Wha-.... Who are you?"
            s g11 "It's a long story..."
            hide green
            hide red
            with d3
            "You quickly bring Clover up to speed."
            show green at ri
            show red r29:
                xalign 0.2 yalign 0.0 xzoom -1
            with d3
            c "So like... It's just us left?"
            s "Looks like it."
            c r11 "That's like... so not cool. I hate working overtime. It gets in the way of my beauty sleep..."
            y "I think we've got more important things to worry about than your sleep schedule."
            y "Like the fact that you're pumped full of nanobots and just being here is a risk to this operation."
            c r38 "{b}*Scoffs*{/b} Oh please, Sam seemed to have...{w} {i}'fixed'{/i} that issue. I feel absolutely fine!"
            y "Oh can't I? {w}Sam, I 'order' you to put Clover in a cell."
            s g28 "Wha-...!"
            play sound "audio/sfx/shockcrash.mp3"
            pause 0.7
            hide green
            hide red
            show white
            pause 0.05
            hide white
            show bgControl
            show green g100 at ri
            pause 0.3
            hide bgControl
            pause 0.2
            s "I obey..."
            hide green
            hide red
            with d3
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            "Sam jumped on Clover!"
            c r28 "Ow, Sammy~....!"
            "After a short struggle, Sam drags Clover to one of the unoccupied cells and shoves her in."
            show green g100 at ri with d3
            s "Orders complete."
            y "........................"
            s g15 "........"
            s g28 "{b}*Blinks*{/b} What just happened...?"
            y "I just tried something...."
            y "Remember when I ordered you to fight Clover back at the university?"
            s g16 "Er...."
            y "And just now... I ordered you to put her in a cell."
            s "You're saying....?"
            y "That I can control your nanobots!"
            y "And although I'm ecstatic at the thought that I can make you do my laundry. I am a little curious about something~...."
            y "Saaaam~....."
            s g11 "..................."
            y "Have you kept up with the supression of your nanobots~....?"
            s g12 "{size=-10}I....{w} I may have forgotten about it....{/size}"
            y "You forgot about it...."
            s g40 "I was embarrassed, okay?! Plus I was feeling fine, I didn't think I was still being controlled!"
            y "Oh no, I can totally understand that. No hard feelings."
            y "Now I order you to do a handstand."
            s g28 "N-no wait...!"
            hide green
            with d3
            "In the blink of a second, Sam's eyes turn red again as she gets down to do a handstand!"
            $ greenArms = 0
            $ greenOutfitArms = 0
            show green:
                xalign 1.4 yalign -0.08 rotate 180 xzoom -1
            with d3
            pause 0.5
            y "Yeah you're right Sam. I don't see what could {i}'possibly'{/i} go wrong."
            s "I'm sorry~....! I'll keep them suppressed from now on. I promise!"
            menu:
                "Be strict with her" if True:
                    y "You promise?"
                    s "I do!"
                    y "I'm pretty sure you {i}'promised'{/i} last time."
                    s "It's different now, really!"
                    s "..................."
                    s "Can I please stand up now? I'm getting dizzy."
                    y "First go make me a sandwich."
                    s "On my hands?!"
                    y "Yes, and then go clean the tables in the milkshake bar."
                    s "B-but...!"
                    y "Unless you want me to order you?"
                    s "N-no...!"
                    pause 0.2
                    hide green with d3
                    "Gracefully, Sam walks out of the room on her hands."
                    y "......................"
                    "You go play your gameboy for a while until she returns."
                    pause 0.3
                    hide scene_darkening with d3
                    scene black with fade
                    pause 0.3
                    scene bgBase with fade
                    pause 0.3
                    show scene_darkening with d3
                    show green:
                        xalign 1.4 yalign -0.08 rotate 180 xzoom -1
                    with d3
                    s "Your... sandwich is ready..."
                    y "Hang on, I just gotta finish this level first."
                    s "[playerName] please!"
                "Be lenient" if True:
                    y "Well I guess this is an uncoventional request. Still I need to know that you won't turn on me at any moment."
                    y "I am going to preach to you for a while though."
                    s "Is that really necessary...?"
                    "You grab the WOOHP Guidelines and begin to read."
                    y "{b}*Ahem*{/b} "
                    y "{i}'It is important to remember your betters. When you're in distress or confused, look towards those outranking you and follow their orders to the letter.'{/i}"
                    s "[playerName] please... the blood is rushing to my head."
                    y "{i}'There may come a time when you think to yourself: 'I am not sure if I'm okay with commiting these warcrimes.'{w} Just remember that your superiors know what they are doing and that there is only a small chance that you will be scapegoated for these event.'{/i}"
                    y "(Warcrimes...?)"
                    y "{i}'When you are setting fire to an orphanage, take comfort in the fact that your officer made an informed decision to do so. Afterall... Any one of these orphans could grow up to become Hitler! '{/i}"
                    y "Wow, WOOHP is kind of messed up."
                    s "[playerName] I'm getting dizzy~...!"
                "Say something insane" if True:
                    stop music fadeout 1.0
                    show redScr:
                        alpha 0.0
                        linear 10 alpha 1.0
                    y "No Sam! You have betrayed my trust and put the entire world in danger!"
                    play music "audio/music/sinister.mp3" fadein 4.5
                    y "Your transgression is so vile, it can no longer be judged by mortal means!"
                    y "All you had to do is keep yourself in check and spare the world a horrible fate of being plundged into chaos."
                    y "Yet you, thinking only about yourself, disregarded this responsibility and followed your own selfish instincts!"
                    y "I therefor summon you! You mighty! You infinite! You, master of all time! {w}Of all space!"
                    show zukker:
                        xalign 0.5 alpha 0.0
                        linear 12 alpha 1.0
                    y "You the bringer of the endtimes! {w}The all-father!{w} You who's name is only said in whispers!"
                    y "ZUKKERTHROTH, DESTROYER OF MOONS! I CALL UPON YOU TO JUDGE THIS FEEBLE MORTAL WOMAN!"
                    hide scene_darkening
                    hide redScr
                    stop music
                    hide zukker
                    s "..........."
                    s "Erm... Can I please stand up now?"
                    show redScr
                    play music "audio/music/sinister.mp3"
                    show zukker
                    y ".............................."
                    y "Wait..."
                    y "Are you not seeing Zukkerthroth, immortal being of infinite wisdom and lubed tentacles?"
                    hide redScr
                    stop music
                    hide zukker
                    s "No....~?"
                    show redScr
                    play music "audio/music/sinister.mp3"
                    show zukker
                    y "......................."
                    hide redScr
                    stop music
                    hide zukker
                    s "Please, the blood is rushing to my head~...."
                    show redScr
                    play music "audio/music/sinister.mp3"
                    show zukker
                    y "(Sorry Zukkerthroth, she's an unbeliever. {w}Better luck next time, eh?)"
                    "Zukkerthroth, destroyer of moons" "{b}*Dejected whining of the infinite*{/b}"
                    hide redScr
                    stop music fadeout 3.0
                    hide zukker
                    with d5
                    pause 0.5
            y "Okay fine, you can stand up again."
            hide green
            with d3
            $ greenArms = 1
            $ greenOutfitArms = 1
            show green g10 at ri with d3
            y "Still, the fact I can order you around probably means that the other agents can do it too."
            y "Do you want that, Sam? Being ordered around? Be somebody else's puppet?"
            s g11 "No~..."
            y "To be somebody's plaything and commit acts of tyranny and chaos?"
            s g11 "No I don't~...."
            y "To steal from old ladies? Beat up old ladies? Help old ladies cross the street{w} only to run away half way through, leaving them behind in the middle of the crosswalk as the cars menacingly rev their engines?"
            s g14 "Okay, okay I get it. No, I don't want that, [playerName]!"
            y "THEN GO FUCK YOURSELF!"
            s g30 "!!!"
            y "Literally in this case."
            s g15 "I will! All right? I'm sorry, I made a mistake!"
            s "It won't happen again..."
            y "Well let's make sure of that."
            s g18 "...?"
            y "I'm going to need a way to measure your oxytocin levels. WOOHP might have something in their database."
            s "Ah okay. Well you can always check the Equipment tab at your workbench."
            y "I think I'll do that.{w} Oh and Sam...."
            s "Yeah...?"
            y "I order you to...."
            s g28 "No no no no!"
            y "Handstand!"
            s "Aaah!"
            hide green
            with d2
            pause 0.01
            $ greenArms = 0
            $ greenOutfitArms = 0
            show green:
                xalign 1.4 yalign -0.08 rotate 180 xzoom -1
            with d2
            pause 0.3
            s "[playerName]!"
            pause 0.4
            hide green
            hide scene_darkening
            with d3
            $ greenArms = 1
            $ greenOutfitArms = 1
            $ spyRedActive = True
            $ mapSpy2Active = True
            $ greenChest = 1
            $ greenBottom = 1
            $ greenOutfit = 0
            $ greenOutfitArms = 0
            $ redChest = 1
            $ redBottom = 1
            $ redOutfit = 0
            $ redOutfitArms = 0
            $ mainQuestUpdate = True
            call qUpdated from _call_qUpdated_1
        scene bgMap:
            zoom 0.5
        with fade
        play sound "audio/sfx/owl.mp3"
        $ tod = 2
        pause 0.5
        scene bgMapNight:
            zoom 0.5
        with d10
        pause 0.6
        play music "audio/music/nighttime.mp3" fadein 1.5
        scene black with fade
        scene bgBase with fade
        jump base

    if task2Stage == 10:
        $ task2Stage = 11
        $ task2Text = _("Discussing the situation, it's become clear that we could use the extra backup to take back Beverly Hills. I should set up a mission and send my spy back to school to capture her friend. \n\nWe brought back a new spy, but the nanobot control seems to be getting worse. I should check my crafting table to see if there's something in WOOHP's database about that.{color=#b5b5b5}\n\n-Check the Equipment tab in your workbench.{/color}\n\n-The Database seems protected. It's going to require someone with computer skills to access it.")
        y "Let's see what what we can make here..."
        "{b}*Bleep*{/b}"
        "Error: Database Protected."
        y "...?"
        "{b}*Bleep*{/b}"
        "Error: Database Protected."
        "{b}*Bleep* *Bleep* *Bleep*{/b}"
        "Error: Database Protected."
        y "Yeah this isn't going anywhere."
        y "(I'm going to have to find a way to restore the database.)"
        if hackerUnlocked == False:
            y "(Perhaps doing some exploring around will help with this.)"
        elif True:
            y "(Maybe Mathias will be able to help me with this.)"
        if tod == 1:
            scene bgMap:
                zoom 0.5
            with d3
            jump worldmap
        if tod == 2:
            scene bgBase with d3
            jump base

    if task2Stage == 11:
        $ task2Stage = 12
        $ task2Text = _("Discussing the situation, it's become clear that we could use the extra backup to take back Beverly Hills. I should set up a mission and send my spy back to school to capture her friend. \n\nWe brought back a new spy, but the nanobot control seems to be getting worse. I should check my crafting table to see if there's something in WOOHP's database about that.\n\nI met someone who can hack into the network, but it will take time. I could speed things up by convincing one of my spies to wear a bikini and visit Mathias.\n\n-(optional) Buy a bikini and send your spy to work at Mathias.")
        y "Hey Mathias, could you hack into a database for me?"
        mat "I could. Whadda ya need?"
        y "Acces to secured files in the WOOHP network."
        mat "The WOOHP Network?!{w} That's risky man..."
        y "You can't do it?"
        mat "Of course I can do it, but it'll take time and I got other priorities right now."
        y "............."
        y "Okay, how much?"
        mat "How much what?"
        y "Money. How much money do you want for it?"
        mat "Hah! I'll do it for free my dude, but you gotta be patient."
        y "Patience is not my strongsuit. Is there something else you want?{w} Some dirty mags maybe?"
        mat "I got the internet y'know...."
        y ".........."
        mat "If you can get a bikini model to show up at my front door, I promise to move you to the priority list. Else you're gonna have to be patient."
        y "........"
        y "A bikini model?{w} I could probably convince my spy to wear a bikini..."
        mat "....?"
        y "He doesn't have to know that I'm not actually part of WOOHP and that we're trying to take back the city to restore order."
        mat "Err...."
        y "Yeah, that sounds like a great idea! I'll have my spy show up here wearing a bikini, have him hack into the WOOHP mainframe and get those database entries!"
        mat "Dude..."
        y "Meanwhile keeping him completely in the dark! No need to drag this kid into a war between the forces of good and evil!"
        mat "You know I can hear everything you're saying, right?"
        y "....."
        y "Did I say all of that out loud?"
        mat "Pretty much."
        y "Damn it. I need to be more careful in the future.{w} I might make this kid an accomplice in our borderline illegal plot to re-take the city!"
        mat "Still talking out loud....."
        y "(CRAP!)"
        y "Okay... You get busy hacking the WOOHP network. If I can get you a bikini model, you'll speed things up?"
        mat "You got a deal, see ya dude."
        y "Laters."
        hide scene_darkening
        hide matModel
        with d3
        call qUpdated from _call_qUpdated_2
        jump worldmap

    if task2Stage == 12.5 or task2Stage == 12:
        if firstPick == 0:
            $ firstPick = 1
        y "(As long as I got some bikinis, I could send someone over to Mathias for a research boost.)"
        y "Girls, could you come out here for a second?"
        if spyGreenActive:
            show green g1 at ri with d3
        if spyRedActive:
            show red r1 at le with d3
        if spyYellowActive:
            show yellow y1 at ri with d3
        y "Soooooo~....."
        if firstPick == 1:
            s "[playerName]~.....?"
            s g18 "It sounds like you're about to ask us to do something."
            y "........."
            y "Put on a bikini."
            s g28 "Huh? You... want me to...? What?"
            y "Put on a bikini and head to this address.{w} Don't ask why."
            s "Are you kidding?! Of course I'm gonna ask why!"
            y "There's this guy who promised to hack into the WOOHP network, but only if he gets a bikini model."
            s g9 "....................."
            s g40 "And what about the fact that I'm not a model..."
            y "Are you joking? Anyone can be a model now-a-days! Just put on a bikini and take a few pictures of yourself!"
            s g8 "[playerName] I don't appreciate you renting me out like this!"
            c r12 "I got excited for a moment there when you talked about being a model..."
            c r14 "Being a stripper for some sweaty nerd to ogle at is {i}'so'{/i} not glamorous!"
            s "What are we even suppose to do once we get there?"
            y "I dunno. Stand around looking hot, do some poses, compliment the guy on his collection of harddrives. Get creative!"
            s g38 "Well I appreciate the suggestions, but I will not be doing it."
            s "I've already been embarrassed enough over these last few days, I don't want to turn into a sex object for people to gawk at."
            y "............"
        if firstPick == 2:
            c "[playerName]?"
            c r18 "What's this all about...?"
            y "........."
            y "Put on a bikini."
            cr28 "A bikini? This better involve some hot guys, [playerName]!"
            y "Put on a bikini and head to this address.{w} Don't ask why."
            c "........."
            c "That's like... totally sketchy."
            y "There's this guy who promised to hack into the WOOHP network, but only if he gets a bikini model."
            c r9 "Ew, a hacker? Those are usually totally growdy nerds!"
            c r8 "Are you just going to rent us out like that...?!"
            a "I hoped that we were going to the beach..."
            a "Going to some hacker's underground basement sounds like the opposite of that."
            c "What are we even suppose to do once we get there?"
            y "I dunno. Stand around looking hot, do some poses, compliment the guy on his collection of harddrives. Get creative!"
            c r38 "Okay... first of all that's not how you get a guy interested in you. And second of all my youthful beauty is wasted on geeks like that."
            a "But I thought you liked being ogled and admired, Clover?"
            c "Only by hot guys!"
            y "............"
        if firstPick == 3:
            a "[playerName]?"
            a y18 "What can we do for you?"
            y "........."
            y "Put on a bikini."
            c r28 "A bikini? Are we going to the beach?"
            y "No.{w} Put on a bikini and head to this address.{w} Don't ask why."
            a "........."
            a "W-...{w}waterpark then?"
            y "There's this guy who promised to hack into the WOOHP network, but only if he gets a bikini model."
            a y9 "{b}*Disappointed*{/b} No waterpark then...."
            s g8 "Are you just going to rent us out like that...?!"
            s "What are we even suppose to do once we get there?"
            y "I dunno. Stand around looking hot, do some poses, compliment the guy on his collection of harddrives. Get creative!"
            a "Stand around and look hot...?"
            a "I dunno [playerName]. I totally saw this documentary about a group of people who got kidnapped like that once!"
            y "............"
        if firstPick == 1:
            label vibMenuJump:
                pass
            menu:
                "Appeal to reason" if True:
                    $ hackProgress = 80
                    $ task2Stage = 12.6

                    if samSupLvl == 1:
                        $ samMood -= 3
                    if samSupLvl == 2:
                        $ samMood -= 5
                    if samSupLvl == 3:
                        $ samMood -= 7


                    if cloverSupLvl == 1:
                        $ cloverMood -= 3
                    if cloverSupLvl == 2:
                        $ cloverMood -= 5
                    if cloverSupLvl == 3:
                        $ cloverMood -= 7

                    y "Sam... he's going to help us break into the WOOHP Database.{w} With his help, we'll have acces to new gadgets and equipment."
                    y "It'll make missions a lot easier to have some extra tech on our side."
                    s "{b}*Hmph*{/b}~..."
                    s "So you expect me to entertain some nerdy loner by shaking my ass a bit?"
                    s "I find this very disrespectful, [playerName]!"
                    c r38 "You said it, Sammy!"
                    s g11 "................"
                    s "But...."
                    s g12 "But if it'll help us take back WOOHP.... I guess I'll do it."
                    c r11 "Hmph~...."
                    s "Just think about it Clover. What if they start bringing out their big guns? We need gadgets to stand a chance."
                    s "I don't like it, [playerName]. But for the safety of the world. I'll do it."
                    c "............."
                    c r38 "Gah! Fine!{w} As long as he doesn't take picture and upload them to his blog or something. I can't be seen around people like him, it would ruin my reputation!"
                    y "That's the spirit! I might send you out tomorrow."
                    y "Oh and Sam...."
                    s g10 "Hm?"
                    y "It wouldn't hurt to smile once you get there."
                    s g33 "{b}*Sighs*{/b} Fine..."
                "Bribe her ($100,-)" if True:

                    if samSupLvl == 1:
                        $ samMood -= 3
                    if samSupLvl == 2:
                        $ samMood -= 5
                    if samSupLvl == 3:
                        $ samMood -= 7


                    if cloverSupLvl == 1:
                        $ cloverMood -= 3
                    if cloverSupLvl == 2:
                        $ cloverMood -= 5
                    if cloverSupLvl == 3:
                        $ cloverMood -= 7

                    y "You wouldn't even do it for Mr. Benjamin...?"
                    c r7 "!!!"
                    s g8 "[playerName]! I am {b}'not'{/b} a prostitute!"
                    s "I can't believe that you think so little of me! I am not going and that's final!"
                    y "But...!"
                    c r40 "I can't believe you're trying to bribe us with one Benjamin!"
                    y "How about two?"
                    c r23 "Well....~"
                    s "CLOVER, NO!"
                    jump vibMenuJump
                "Order her (-Karma)" if True:
                    $ hackProgress = 80
                    $ playerKarma -= 5

                    if samSupLvl == 1:
                        $ samMood -= 3
                    if samSupLvl == 2:
                        $ samMood -= 5
                    if samSupLvl == 3:
                        $ samMood -= 7


                    if cloverSupLvl == 1:
                        $ cloverMood -= 3
                    if cloverSupLvl == 2:
                        $ cloverMood -= 5
                    if cloverSupLvl == 3:
                        $ cloverMood -= 7

                    $ task2Stage = 12.6
                    y "Sam... Clover..."
                    s g18 "Hm?"
                    y "I {b}'order'{/b} you two to put on a bikini and head to Mathias."
                    s g28 "W-wait...!"
                    c r29 "What?!"
                    play sound "audio/sfx/shockcrash.mp3"
                    pause 0.7
                    hide green
                    hide red
                    show white
                    pause 0.05
                    hide white
                    show bgControl
                    show green g100 at ri
                    show red r100 at le
                    pause 0.6
                    hide bgControl
                    s g39 "Yes sir! Seduction mission is a go!"
                    c r8 "Shedding some clothes for the glory of WOOHP is but a small price to pay!"
                    y "That's better! I might send you two out during the day to visit Mathias."
                    "Both girls" "Yes sir!"
            hide green with d3
            hide red with d3
            "You can now send girls to Mathias during the day to boost his research. Only spies that have a swimsuit available can go."
            "This is entirely optional however. Mathias will continue to work on hacking the database, even without the spies visiting him."
            hide scene_darkening with d3
            jump base

    if task2Stage == 13:
        $ gadgetVIBActive = True
        $ task2Stage = 14
        $ task2Text = _("Discussing the situation, it's become clear that we could use the extra backup to take back Beverly Hills. I should set up a mission and send my spy back to school to capture her friend. \n\n-We brought back a new spy, but the nanobot control seems to be getting worse. I should check my crafting table to see if there's something in WOOHP's database about that.\n\n-I met someone who can hack into the network, but it will take time. I could speed things up by convincing one of my spies to wear a bikini and visit Mathias.\n\n-Discuss using the V.I.B. with the girls.")
        image vibComplete = "gui/gadgets/equipment/vibComplete.png"
        show vibComplete:
            xalign 0.453 ypos 0.020
        pause 0.2
        play sound "audio/sfx/itemGot.mp3"
        pause 0.7
        "The Vitals Indication Bug aka V.I.B. unlocked!"
        "The V.I.B. will messure a spy's oxytocin levels and nanobots control via the STATUS screen."
        "It can also be used during missions to make a nanocontrolled spy come to her senses."
        "Careful however! Using the V.I.B. during missions can give away the spies location."
        y "I bet the girls are gonna love this..."
        y "Once I have a moment, I should go talk to them."
        pause 0.2
        call qUpdated from _call_qUpdated_3
        hide screen equip1VIB
        scene black
        with fade
        if tod == 1:
            scene bgMap:
                zoom 0.5
            with fade
            jump worldmap
        if tod == 2:
            scene bgBase
            jump base
        elif True:
            jump worldmap


    if task2Stage == 14:
        $ task2Stage = 15
        $ redChest = 1
        $ redBottom = 1
        $ task2Name = "Double Trouble (Complete)"
        $ gadgetVIBActive = True
        $ task2Text = _("{size=-5}-The girls have reluctantly agreed to wear their V.I.B. from now on. Their vital signs can be read via the STATUS screen. However with power comes responsibility. How will I treat my spies?{/size}")
        y "{b}*Deep breath*{/b}"
        y "Okay, how am I going to tell them...."
        "Inner Voice" "Be honest and straight forward with them."
        y "I know I should, voice in my head. But you know how they're going to react."
        "Inner Voice" "They will probably say some nasty things to you, but just remember:{w} {i}I am a strong independent man and my ego is strong enough to handle some mean remarks by teenage girls.{/i}"
        y "Yeah... Thanks voice."
        y "......................."
        y "By the way....{w} Are you suppose to be my conscious or something?"
        "Inner Voice" "Also if the girls refuse and say mean things to you, you should strap them down to a bed and preform Chinese water torture on them."
        y "....................."
        y "Definitely not my conscious."
        show scene_darkening
        with d3
        if firstPick == 1:
            show green g1 at ri with d3
            s g18 "[playerName]? Did I hear you talking to someone...?"
            show red r1 at le with d3
            y "Girls, I figured out a solution to our little nanobots problem."
            y "I present you with...{w} THE V.I.B.!"
            "You hold up two toys to the girls."
            c r18 "Is that...?"
            s g16 "A toy? I don't see how this is going to help us, [playerName]."
            c r35 "Er... Sam...."
            "Sam picks up the toy and inspects it."
            s g41 "So is this like a gadg-...?"
            play sound "audio/sfx/vib.mp3"
            "{b}*Vibrates*{/b}"
            s g16 "Why is it vibrating...?"
            c "......................"
            y "......................"
            s "................"
            s g28 "!!!"
            s g30 "NO! NO WAY!"
            s "Is this...?! We're suppose to...?! You expect us to...?!"
            s "I... I...! Clover! Say something!"
            c r23 "Oooh~... it has five higher settings~...."
            s g8 "Clover!"
            c r3 "Oh Sam, calm down. It's just a vibrator."
            s g4 "B-but...!"
            s "{size=-10}But it's naughty...!{/size}"
            c r38 "Listen Sam..."
            c "We're not little girls anymore. We're full blown spies, working for one of the most powerful organizations on earth."
            c "If anything, I'm surprised we haven't run into anything like this before."
            s "{size=-10}But...{/size}"
            c r12 "I mean, don't get me wrong...{w} Did you have to go with such a gaudy pink, [playerName]? That's like... {i}'so'{/i} not fashionable!"
            s g11 "............"
            c "Just deal with it Sam. It's not like he's going to ask us to wear it to missions."
            y "........................"
            c r16 "Right?"
            y "........................"
            c "Right....~?"
            s g28 "[playerName]...! This is not funny!"
            y "Not only will you wear it on missions."
            y "You will also wear it when going undercover."
            s g30 "!!!"
            c r30 "!!!"
            y "And when you're at the base."
            c "T-that's...!"
            y "And not only that..."
            s "There's more...?"
            "{b}*Bleep*{/b}"
            play sound "audio/sfx/vib.mp3"
            c r29 "...............!"
            s g28 "It's remote controlled...?!"
            y "Whenever I suspect any of you to turn traitorous, I can use this to snap you out of it."
            c r11 "......"
            c r12 "He has a point..."
            s g9 "Clover! Don't give in so easily!"
            c "It's either this or helping in overthrowing the world."
            s g40 "There has to be another way!"
            y "I'm sure there is, but we're sorta on a tight deadline here."
            s g31 "Well we could...! {w} How about instead we...{w} I'm sure that if we..."
            s g33 ".............................."
            c r22 "Gimme one of those..."
            hide red with d3
            "Clover takes one of the V.I.B.s and heads into a nearby room."
            y "........................"
            s "........................"
            s g38 "This is stupid, you can't just order us around like this."
            y "I'm your boss, I'm pretty sure I can."
            s g40 "No, you can't! We're not your slaves!"
            c "We might as well be at this point."
            $ redOutfit = 0
            $ redChest = 0
            $ redBottom = 0
            $ redOutfitArms = 0
            $ redShoes = 0
            $ redUnder = 1
            show red r11 at le with d3
            s g29 "C-clover...!"
            c "If we're going to save this world. Like it or not we need him."
            s g30 "But..."
            c "And he knows it. He can ask us to do whatever he wants."
            y "..................."
            s "You... you wouldn't do that!"
            s "............."
            s g29 "Would you...?"
            menu:
                "We're in this together" if True:
                    y "I just wanted to let you two know that we're all in the same boat."
                    y "I know that things look bleak right now, but you can trust me."
                    s g1 "We can...?"
                    y "......................"
                    y "Okay you can {i}'probably'{/i} trust me."
                    y "Most likely."
                    s g10 "................"
                    y "Potentially."
                    y "Possibly..."
                    y "......................."
                    y "I'd say about 50/50."
                    s g12 "Great, that {i}'really'{/i} set my mind at ease..."
                "You two are my slaves now (-Karma)" if True:
                    $ playerKarma -= 5
                    y "YES! I got bitches!"
                    y "Time to feed me my grapes slaves~.... ♥♥♥"
                    c "Told ya."
                    play sound "audio/voice/what.mp3"
                    s g28 "W-what! No! I'm nobody's slave!"
                    c "All right Sam, then how about you leave and join the rest of the mindcontrolled masses?"
                    s "But... but...!"
                    "Sam looks around desperately."
                    s g9 "..................."
                    s g15 "There's really no alternative. Is there...?"
                    c "Now you're getting it."
                "Say something crazy" if True:
                    y "I could order you to do all kinds of sick things!"
                    s g30 "!!!"
                    y "I mean I wouldn't, but I could."
                    s g29 "Oh..."
                    y "At least I probably wouldn't...."
                    s g31 "[playerName]..."
                    y "Nah, okay real talk. I would {i}'totally'{/i} make you do all the weird stuff."
                    show cellNeutral with d5
                    y "I could turn your cell into a dungeon..."
                    show cellDungeon with d5
                    s g28 "No!"
                    y "Or more likely, just have you do all my boring stuff, like file my taxes."
                    s g10 "............"
                    s g12 "I still don't like it..."
                    hide cellNeutral
                    hide cellDungeon
                    with d3
            c r38 "Like it or not. We're at his whims and it's going to be up to him to decide how he treats us."
            c r11 "[playerName].... You got a lot of power over us now, okay?"
            c "But we're still people. Forcing us to do things we don't want to, will have a negative impact. Plus, treating us like slaves and over-working us will affect our mood."
            s g29 "Now hang on a minute! You don't {i}have{/i} to treat us like slaves."
            s g1 "I bet we could become great friends if you don't abuse your power too much."
            y "I guess we'll see. For now, go put on the V.I.B."
            s g11 "Fine...."
            hide green with d3
            pause 0.8
            c "............"
            c "So you found this thing in the WOOHP database?"
            y "Yup."
            c r23 "Always knew that Jerry was secretly a perv."
            y "Jerry is the founder of WOOHP, right?"
            c r49 "Yeah. The fact that we haven't heard anything about him makes me sorta worried."
            c "I hope that nothing bad happened to him..."
            $ greenOutfit = 0
            $ greenOutfitArms = 0
            $ greenChest = 0
            $ greenBottom = 0
            $ greenShoes = 0
            $ greenUnder = 1
            show green g39 at ri with d3
            s "................."
            y "Got it sorted?"
            s "What do you think...?"
            y "Good! Let's test these things out!"
            "{b}*Bleep*{/b}"
            play sound "audio/sfx/vib.mp3"
            s g28 "!!!"
            c r28 "!!!"
            y "........."
            y "Judging by your reaction, it looks like they work."
            c r19 "A-and... these will measure our vital signs?"
            y "Yup. I got them right here!"
            y "................."
            y "It says you're aroused."
            c "................"
            s g30 "[playerName]...! Can you pl-please turn it off now?!"
            y "Oh right, sorry."
            "{b}*Bleep*{/b}"
            y "All right, well done girls."
            y "Head back to your cells for now. We got a busy day tomorrow."
            "The girls nod and take their leave."
            $ task7Text = _("We liberated Clover who has joined us at the base. We also figured out a way to gain intel by going undercover with the gangs around town and money by working at the milkshake bar. We're a little closer in our goal to liberate Beverly Hills.\n\n-Reach rank 2 with the Aces.")
            hide green
            hide red
            with d3
            hide scene_darkening
            with d3
            call qCompleted from _call_qCompleted_1
            call greenOutfitSet from _call_greenOutfitSet
            $ redChestSet = 1
            $ redBottomSet = 1
            $ redUnderSet = 1
            $ redShoesSet = 1
            call redOutfitSet from _call_redOutfitSet
            jump base
    if task2Stage == 15:
        $ task2Stage = 16
        pause 0.5
        show scene_darkening with d3
        pause 0.3
        show red at ri with d3
        y "Good morning Clover. How are you liking sleeping in an asylum?"
        c r42 "Not as bad as I thought, but like... HEL-LO, hang up a mirror or something."
        c "I simply can't operate without my hair looking in peak condition."
        y "Noted."
        c r18 "So what do you have planned for today?"
        y "Well I've been sending Sam undercover at the different gangs around town."
        y "I figured you'd do the same."
        if gang2Active:
            c r1 "Ooooh! I can't wait to go undercover with the Aces!"
            c "All those fashionable clothes, the fast cars, the big boats!"
            y "............."
            y "Actually I was thinking of sending you undercover at the Drift Punks."
            play sound "audio/voice/clover/what.mp3"
            play sound "audio/voice/clover/what2.mp3"
            c r17 "W-what?! Those nerds?!"
            c r5 "Please [playerName] have mercy! I can't be seen around those kinds of people. It will ruin my reputation!"
            y "They seem to have a thing for blondes. I bet you'd fit right in."
            c "Please just send me anywhere but there!"
            y "..............."
            y "I'll think about it."
        elif True:
            c r1 "Ooooh! I can't wait to go undercover with the Aces!"
            c "All those fashionable clothes, the fast cars, the big boats!"
            y "............."
            y "It's too bad we don't have a contact within the Drift Punks yet. I was hoping to send you there."
            play sound "audio/voice/clover/what.mp3"
            play sound "audio/voice/clover/what2.mp3"
            c r17 "W-what?! Those nerds?!"
            c r5 "Please [playerName] have mercy! I can't be seen around those kinds of people. It will ruin my reputation!"
            c "Send me anywhere but there!"
            y "..............."
            y "I'll think about it."
        hide scene_darkening
        hide red
        with d3
        jump worldmap

    if task2Stage == 16:
        $ redDayJob = 0
        $ task2Stage = 17
        show scene_darkening with d3
        show red r10 at ri with d3
        $ punkRep += 1
        c "I'm back from working at Drift Punk..."
        y "Let me guess. It was hell and you're never going back there."
        c r11 "{b}*Scoffs*{/b} It wasn't {i}'that'{/i} bad. It was just really boring."
        y "Boring?"
        c r12 "Yeah... Turns out they make most of their money hacking into bank accounts. Which... isn't exactly the most exciting way to commit a crime..."
        c "They tried to teach me, but I didn't really end up accomplishing much. I guess they were nice enough about it though. Even gave me this for my efforts."
        $ cash += 50
        $ randMoney = 50
        call missionRewardMoney from _call_missionRewardMoney_8
        c "But what's there to say really... It's a place full of nerds, committing nerd crimes."
        y "Any hint of who's running the operation?"
        c r10 "No, not yet, but I feel like they wouldn't let me in on that kind of data on the first day."
        y "All right well done. I'll be sure to send you back from time to time."
        c r12 "I still rather go to the Aces..."
        y "Yeah yeah, less complaining."
        y "Head back to your cell for now."
        hide red with d3
        "Clover shrugs and heads back to her cell."
        hide scene_darkening with d3
        jump nextReport

default task3Stage = 0
default firstLandgrab = False

label task3:
    if task3Stage == 0:
        "INACCESIBLE, PLAYERS CAN'T SEE THIS."
    if task3Stage == 1:
        $ task3Stage = 2
        $ spy1Status = 10
        show scene_darkening
        with d3
        y "All right, head to the Aces today."
        sM "............................"
        y "No...?"
        sM "No it's fine. It's just that they're having a party today."
        y "Oh that doesn't sound so bad."
        sM "No no, it's not, but..."
        sM "Well... I don't normally go to parties.{w} I prefer to stay at home and do some reading."
        y "................"
        sM "So er... Got any tips for me?"
        y "Look at you, being a social shutin."
        sM "[playerName]... I'm serious."
        y "Just relax and have a good time. Do some socializing. It's much easier to gather intel from someone while they're drunk."
        sM "And what if someone tries to make a move on me?"
        y "Huh?"
        sM "You know... What if someone tries to get touchy or tries to... y'know...{w} kiss..."
        show scene_fighting with d3
        y "(Hm...)"
        y "(On one hand, being slutty might make things easier for us. Sam is a bit of a prude and getting her more in touch with her slutty side could lead to more money and intel in the future.)"
        y "(On the other hand, do I really want my spies to go sleeping around with the rest of the world...?)"
        hide scene_fighting with d3
        menu:
            "Encourage sluttiness" if True:
                $ slutPublic += 1
                y "Well..."
                y "Being a little flirty might loose some lips."
                sM "But I wouldn't want to go too far of course."
                y "Of course."
                sM "I'll give it a try... I'll just flutter my eyelashes, smile coyly at them and have them buy me a drink."
                sM "Then when I got what I need, I'll figure out an excuse to get out of there.{w} I've seen Clover do it plenty of times."
            "Discourage sluttiness" if True:
                y "Absolutely not! No promiscuity!"
                sM "Oh! I'm surprised. I figured you'd encourage it."
                sM "Well okay then. I'll make sure to keep my guard up."
        sM "Okay, got it! Thanks for the advice, [playerName]."
        hide scene_darkening with d3
        "Sam leaves for the Aces party."
        $ mapSpy1Selected = False
        jump worldmap

    if task3Stage == 2:
        $ task3Stage = 3
        pause 1.0
        show scene_darkening with d3
        pause 0.3
        $ greenChest = 1
        $ greenBottom = 1
        $ greenShoes = 1
        $ greenNeck = 1
        "Incoming transmission."
        y "...?"
        "{b}*Bleep*{/b}"
        stop music fadeout 3.0
        scene bgCastle
        show green g31 at ri
        show scene_camera
        with fade
        s "[playerName]..? Are you there?"
        y "Hey Sam, enjoying the party?"
        s g34 "I'm in Spain."
        play music "audio/music/ambient1.mp3" fadein 3.0
        y "!!!"
        y "SPAIN?!"
        y "AS IN THE COUNTRY?!"
        s "Yes."
        y "..................."
        y "WHAT ARE YOU DOING IN SPAIN?!"
        s g37 "So it turns out these guys don't do things half way... big surprise."
        s g32 "I'm in a privately owned castle off the coast of Valencia. They flew me out here to come party with them."
        s "I can't talk for long, I'll be back tomorrow with a full report.{w} Sam out."
        stop music fadeout 2.5
        scene bgBase
        hide green
        hide scene_camera
        hide scene_darkening
        with fade
        pause 0.4
        y ".........."
        y "A private castle in Spain...{w} Those rich bastards..."
        play music "audio/music/nighttime.mp3" fadein 2.0
        jump base

    if task3Stage == 3:
        $ acesRank = 2
        $ acesRep = 0
        $ missionAreaCastleActive = True
        $ task3Stage = 4
        $ specialMaggieStatus = 1
        pause 0.5
        show scene_darkening
        with d3
        show green g1 at ri with d3
        $ mainQuestUpdate = True
        $ task7Text = _("We've located one of the Aces lieutenants hiding out at the Aces Castles. Our top priority should be to capture her and bring her back for questioning.\n\n-Plan a mission to the Aces castle and capture Maggie T.")
        s "Hola."
        y "Hola to you too.{w} How was the Mediterranean?"
        s g28 "It...{w} was...{w} AMAZING!"
        y "Oh, you liked the party?"
        s g29 "Oh right, I forgot about the party. No I mean Valencia was amazing!"
        s "All the little nooks and crannies, the architecture, the culture!"
        y "................."
        s "They had museums and the castle I was staying at dated back to the 13th century!"
        s g28 "They had a painting there that was over 300 years old!!!"
        y "Okay... But did you learn anything?"
        s g31 "Huh? Oh right..."
        s "Yes, I did."
        s "Whoever was hosting the party is a bigshot within the Aces. He finances them and invites their top brass out to Spain on a regular basis."
        y "Any idea who it is?"
        s g32 "No... I wasn't allowed to go see him, but I did see an old familiar face..."
        s "Maggie T."
        y "Maggie T?"
        s "We've fought her before. She's just an interior designer, but got famous after trying to assassinate the US President."
        s "She's been rolling in money ever since. The Aces are probably offering her a position on their gang in return for funding."
        s "Meanwhile I had other things to worry about."
        s g37 "Namely boys..."
        y "Boys? Sam, I am disappointed in you. To prioritize boys over your mission!"
        y "I mean Clover? Sure, I can see her doing it, but you?"
        s g28 "N-no! It's not what you think. I was busy keeping them off of me!"
        y "Huh?"
        if slutPublic >= 1:
            s g37 "You know how you suggested to be more flirty?"
            s "Well I tried. Which by the way...{w} I'm not very good at."
            s "But anyways I flirted around with a few guys, then more and more started showing up!"
            s g15 "I spent most my time hiding! How does Clover do it...?!"
            s g1 "I mean it wasn't all bad. I gathered some good intel...{w}{size=-10} And the attention was kind of nice...{/size}"
            s "Here... this is what I've learned."
            $ randIntel = 100
            call missionRewardInt from _call_missionRewardInt_4
        if slutPublic == 0:
            s g38 "As you suggested, I wouldn't be flirty and kept everyone who approached me at arm's length."
            s "But they just saw that as playing hard-to-get!"
            s "It wasn't made any easier by some jealous girls who thought I was hitting on their men!"
            s g10 "Eventually I just ended up hiding for most of the party instead of gathering intel."
        y "Well it's good to have you back State side. I might send you girls out to do some missions at the castle from now on."
        s g1 "{b}*Nods*{/b} I was thinking the same thing. Let's catch the creep who's supplying them money!"
        $ spy1Status = 0
        hide green
        hide scene_darkening
        with d3
        play sound "audio/sfx/itemGot.mp3"
        "You've unlocked {color=#ffeda6}Castle Fiebre del Oro{/color}. You can now sent your spies there for missions."
        "New clothing options for Sam are availabe at the Mall."
        jump nextReport

    if task3Stage == 4:

        $ _skipping = True
        $ task3Stage = 5
        hide interactScreen
        scene black
        hide spyCombat2
        hide obstMaggie
        hide screen equipmentMenu
        with fade
        pause 1.0
        play sound "audio/sfx/running1.mp3"
        pause 1.5
        $ randomExit = 0
        show globalImageCastle:
            zoom 0.25
        with fade
        pause 1.0
        show obstMaggie:
            xalign 0.62 yalign 0.49 rotate 3 zoom 0.21
        sM "Nowhere left to run, Maggie!"
        mag "You pesky girls!{w} Guards get them!"
        mag ".............."
        mag "Guards?"
        y "We got her n-..."
        y "Wait...{w} Her eyes are red."
        cM "Is she... under nanobot control aswell?"
        y "Only one way to find out. Take her in and we'll interrogate her at the base."
        sM "Got it!"
        mag "Uh oh..."
        play sound "audio/sfx/punch1.mp3"
        hide globalImageCastle
        hide obstMaggie
        scene black
        with hpunch
        pause 1.0
        $ loot1 += 1
        $ loot2 += 1
        $ loot3 += 1
        $ loot5 += 1
        jump missionComplete

    if task3Stage == 5:
        $ task3Stage = 6
        pause 1.0
        show scene_darkening with d3
        show red r34 at ce with d3
        $ task7Text = _("We've located one of the Aces lieutenants hiding out at the Aces Castles. Our top priority should be to capture her and bring her back for questioning. We captured Maggie and locked her up, now all that's left to do is interrogate her.\n\n-Visit Maggie at her cell and interrogate her.")
        c "We're back."
        y "Good, just put her in one of the empty cells. I'll go talk to her when I'm ready."
        c "Understood. Don't wait too long before questioning her."
        hide scene_darkening
        hide red
        with d3
        $ prisonersNew = True
        jump base

    if task3Stage == 6:
        $ task3Stage = 7
        $ maggieSocial = 1
        $ specialMaggieBounty = True
        $ specialMaggieStatus = 3
        pause 0.5
        show scene_darkening with d3
        pause 0.4
        y "Well well well... If it isn't the infamous Maggie T. IF THAT IS YOUR REAL NAME!"
        mag "................."
        y "............."
        y "Odd, I expected an evil monologue or something."
        show green g31 at le with d3
        s "Hey, [playerName]... There's something off about her. See her eyes?"
        y "They're red... Does that mean...?"
        s "She's being controlled by nanobots aswell!"
        mag "Soon the world will fall under the control of the mastermind, and there's nothing you can d-...."
        "{b}*Zip*{/b}"
        mag "Why are you unzipping your pants...?!"
        s g28 "[playerName]! You can't do that against her will! We're the good guys, remember?"
        y "Who said anything about doing it against her will?"
        y "Hey Maggie, you're currently being controlled by nanobots, but we can break you out of it."
        mag "What?! Nobody is controlling the great Maggie Trendset!"
        y "We can prove it, but we'll have to break you out of it with a quick fuc-.... {w}Wait the T. stands for Trendset?"
        y "That's a stupid name."
        mag "Hey!"
        mag "Fine... I've been feeling more... murderous than usual. If you say a quick shag will break me out of it, then I'm willing to give it a try..."
        s g33 "I don't wanna watch this...."
        hide green
        hide scene_darkening
        with d3
        scene black with fade
        pause 0.5
        mag "Oh! Oh! Oh!"
        mag "Oooh yes, I'm feeling better already!"
        mag "In my {i}'what'{/i}?! Well just this once then~... ♥"
        mag "Ahh! Ahhhhhh! ♥♥♥"
        y "Say cheese..."
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d3
        pause 0.5
        show picMaggie:
            xalign 0.5 yalign 0.5
        with dissolve
        pause
        play sound "audio/sfx/itemGot.mp3"
        "A new photo has been added to your photoalbum."
        hide picMaggie
        scene bgPrison
        with fade
        show scene_darkening with d3
        mag "I... I can't believe they were controlling me..."
        y "You've been working as a lieutenant for a gang here in town all this time."
        mag "To use me like a puppet! I'll get them for this!"
        mag "I WILL TEACH THEM NOT TO MESS WITH MAGGIE TRENDSET!"
        y "Okay okay, calm down. If it's revenge you want, we can help you with that, but first you need to tell us everything you know."
        mag "Well..."
        scene black with fade
        scene bgMap:
            xalign 0.0 yalign 0.0 zoom 0.5
            pause 1.0
            linear 1.5 xalign 0.0 yalign 0.25 zoom 1.0
        with fade
        $ renpy.pause(2.5, hard='True')
        show expression "gui/landgrabTut1.png":
            xalign 0.2 yalign 0.4
        show expression "gui/mapUILieutenant.png":
            xalign 0.22 yalign 0.6
        show expression "gui/mapUILieutenant2.png":
            xalign 0.28 yalign 0.6
        show expression "gui/mapUILeader.png":
            xalign 0.34 yalign 0.6
        with d5
        mag "The Aces, like most big gangs around town have two lieutenants. Only one now that you've freed me from the nanobot control."
        hide expression "gui/mapUILieutenant.png"
        show expression "gui/mapUIMaggie.png":
            xalign 0.22 yalign 0.6
        with d5
        mag "If you want to bring down the gang, you're going to have to capture the other officer and then confront the gangleader."
        y "And how do we do that?"
        mag "The lieutenants will stay hidden for the most part. You need to draw them out."
        hide expression "gui/landgrabTut1.png"
        hide expression "gui/mapUIMaggie.png"
        hide expression "gui/mapUILieutenant.png"
        hide expression "gui/mapUILieutenant2.png"
        hide expression "gui/mapUILeader.png"
        show bgMap:
            linear 1.0 xalign 0.0 yalign 0.0 zoom 0.5
        pause 1.3
        play sound "audio/sfx/raid.mp3"
        play music "audio/sfx/warzone.mp3" fadein 2.0
        show scene_darkening
        with d3
        mag "Every 30 days, there is something called a {color=#ffeda6}'Landgrab'{/color}.{w} The gangs will fight amongst each other for control over different neighborhoods."
        show expression "gui/mapUILandgrabTarget.png":
            xalign 0.1 yalign 0.25
        with d3
        show expression "gui/mapUILandgrabTarget2.png":
            xalign 0.9 yalign 0.85
        with d3
        show expression "gui/mapUILandgrabTarget3.png":
            xalign 0.9 yalign 0.05
        with d3
        pause 1.0
        mag "You need to capture Agents to fight for you during the landgrab."
        y "We can make {color=#ffeda6}Hypno Earrings{/color} and use those to capture Agents during missions."
        mag "Once a gang begins to lose a lot of ground, their lieutenants will reveal themselves. If your reputation in the gang is high enough, you might get close enough to capture them."
        y "So keep sending my spies undercover and once every 30 days fight in a Landgrab?"
        y "Do I have to wait that long?"
        mag "You can skip to the next Landgrab via the Agents button."
        show expression "gui/agentCounter.png":
            xalign 0.65 yalign 0.0
        with d3
        mag "You're going to have to build up an army though. These Landgrabs can get pretty hairy and you'll loose agents to nanobot control."
        y "Gather more WOOHP agents and break them out of their nanobot control in the basement. Got it."
        hide expression "gui/mapUILandgrabTarget.png"
        hide expression "gui/mapUILandgrabTarget2.png"
        hide expression "gui/mapUILandgrabTarget3.png"
        hide expression "gui/agentCounter.png"
        stop music fadeout 1.0
        scene black with fade
        scene bgPrison with fade
        pause 1.0
        mag "......................"
        mag "So......"
        mag "I'd say I helped you out quite a bit...{w} Any chance of letting me go?"
        y "Not a chance."
        mag "Curses...."
        label testMe:
            pass
        hide scene_darkening
        show scene_fighting
        with d3
        pause 0.5
        show scene_fighting with d10
        if 21 <= landgrabTimer <= 30:
            $ landgrabTimer = 20
        $ timetograb = 30 - landgrabTimer
        "Landgrabs happen ever 30 days. Currently it's [timetograb] more days until the next one."
        "During a Landgrab, you can send freed WOOHP agents to fight for you in the streets and try to bring enemy lieutenants out of hiding."
        "However, you can lose agents during the fight. Agents can be captured by planning missions and using the {color=#ffeda6}Hypno Earring{/color} gadget."
        "After they've been captured and send to the base, you can break them out of their nanobot control by throwing down dirty magazines into the basement."
        scene skipLandgrabTut with fade
        "You can see when the next landgrab is by clicking on the 'Agents' button at the top of the screen. Here you can also choose to skip to the next Landgrab in case you don't want to wait."
        "Spies send undercover during a Landgrab earn a reputation boost, but risk getting hurt on the job."
        scene orderOfCaptureTut with fade
        "Some missions will not become available until you've captured certain gangleaders. Therefor the best order would be to capture the first Lt. of each gang, before moving on to the second."
        pause
        $ mainQuestUpdate = True
        $ task7Text = _("We found a way to get gangleaders out of hiding. If we mess enough with their gang during Landgrabs they'll show themselves.\n\nThen, if our reputation is high enough, we can get close to these lieutenants and try to capture them.\n\n-Free at least 5 WOOHP Agents\n-Assault the Aces during the next Landgrab.\n\nTip: Remember, you can capture more agents by using {color=#ffeda6}Hypno Earrings{/color} during missions.")
        hide scene_fighting with d3
        pause 0.5
        scene black with fade
        pause 0.5
        scene bgBase with fade
        jump base
    if task3Stage == 7:
        $ task3Stage = 8
        pause 0.5
        scene black with fade
        pause 0.5
        scene bgClub1 with fade
        pause 0.5
        show scene_darkening with d3
        y "Company meeting!"
        show yellow at le
        show red at ce
        show green g1 at ri
        with d3
        y "Today I wanted to talk abou-..."
        "{b}*Ting* *Ting*{/b}"
        "???" "Hello?"
        y "Sorry, we're not open ye-...."
        show yellow y54:
            xalign 0.0 yalign 0.0 xzoom -1
            linear 0.2 xalign -0.2 xzoom -1
        show green g54:
            xalign 1.0 yalign 0.0
            linear 0.3 xalign 0.2
            xzoom -1
        show red r54:
            xalign 0.5 yalign 0.0
            linear 0.3 xalign 0.0
            xzoom -1
        pause 0.3
        show agentModel2:
            xalign 0.9 yalign 0.0
        with d3
        "Agent 1" "What a lovely milkshake bar you have here!"
        y "Er..."
        show agentModel3:
            xalign 1.1 yalign 0.0
        with d3
        "Agent 2" "Quite the milkshake bar you found here fellow agent!"
        y ".................."
        show agentModel4:
            xalign 1.3 yalign 0.0
        with d3
        "Agent 3" "A charming little milkshake bar?! How quaint! Surprising how it survived the chaos this long!"
        y "Heh heh~... yeah big surprise~..."
        "Agent 1" "........................."
        "Agent 1" "Wait... Something's not quite righ-...."
        y "GET 'EM!"
        hide green
        hide red
        hide yellow
        show yellow y54:
            xalign 0.2 yalign 0.0 xzoom -1
            linear 0.1 xalign 0.84
        show green g54:
            xalign 0.3 yalign 0.0 xzoom -1
            linear 0.1 xalign 0.83
        show red r54:
            xalign 0.3 yalign 0.0 xzoom -1
            linear 0.1 xalign 0.82
        pause 0.15
        hide green
        hide red
        hide yellow
        hide agentModel2
        hide agentModel3
        hide agentModel4
        hide scene_darkening
        scene black
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        scene bgClub1 with fade
        show scene_darkening
        show red r50:
            xalign 1.1 yalign 0.0
        show yellow y45:
            xalign 0.9 yalign 0.0 xzoom -1
        show green g43:
            xalign 1.3 yalign 0.0
        with d3
        a y28 "WOOHP Agents!"
        s g29 "That was close...!"
        c r37 "We can't have them reporting back to WOOHP and blow our cover. Luckily it was only three this time."
        a y49 "What do we do with them...?"
        y "I don't know. I've never hid a body before!{w} Put them downstairs in the basement I guess."
        a "{b}*Nods*{/b}"
        hide yellow with d3
        pause 0.5
        y "And now we have a couple of mindcontrolled agents in the base...."
        c r1 "This works in our favor! If we break their nanobot control, we can use them in the next Landgrab!"
        y "That's what I was thinkin-..."
        a "Eep!"
        play sound "audio/voice/agent/daylightStingsMyEyes.mp3"
        "???" "Daylight stings my eyes!"
        y "!!!"
        show yellow at le with d3
        a y29 "Er... [playerName]? There's already an agent downstairs."
        y "............................."
        show agentModel:
            xalign 0.0 yalign 0.0 xzoom -1
        with d3
        "Agent" "Hi! I'm still here!"
        y "Are you that agent we captured during the first mission...?"
        y "How did you survive down there for all this time...?"
        "Agent" "My undying dedication to the mission!"
        y "........"
        y "Suuure~...{w} Say... Do you want to help us retake Beverly Hills?"
        "Agent" "Boy do I! I can't wait to deal out some justice!{w} Preferably with my fists!"
        y "Oh easy there. We're gonna send you out during the next Landgrab."
        s g31 "If we can break the nano-control over these other agents, we could use them to help."
        y ".........................."
        s g18 "What?"
        y "You know what is needed to break agents out of their control, right?"
        $ greenBlush = 1
        s "Well... yeah. We have to increase their oxytocin levels~..."
        y "And how do we do that~...?"
        s ".........................."
        s g19 "{size=-10}By having sex..."
        y "Exactly! Time to get naked!"
        s g28 "N-now wait a minute!"
        c r31 "We're not gonna start showing off our naked bodies to every member of WOOHP. One is enough."
        a y29 "We could just buy some dirty magazines."
        y "Dirty magazines...?"
        a y1 "Yeah, we can just buy some magazines with those dirty pictures from the bookstore at the mall."
        a "If we throw a few of those down into the basement, I bet that will break the agents from their trance!"
        y "It'll cost us some money, but that's a good alternative."
        pause 0.4
        show scene_fighting with d3
        pause 0.4
        "You captured a few more WOOHP Agents and it's time to free them from their nanobot control."
        "Luckily breaking the nanobot control over captured agents isn't that hard. Visit the bookstore to buy cheap porn magazines and give them to the captured agents in your basement."
        "Once agents have been freed, they can participate in Landgrabs and help liberate Beverly Hills."
        hide scene_fighting with d3
        y "Okay, let's wrap this up. We've got quite a day ahead of us."
        "Agent" "What should I do?!"
        y "Er... You...{w} Here. Put this one."
        show expression "models/agent/cook.png":
            xalign -0.24 yalign 0.1 xzoom -1
        y "You are now a chef."
        "Agent" "An important job! I will not disappoint you!"
        $ capturedAgents += 3
        hide red
        hide green
        hide yellow
        hide agentModel
        hide expression "models/agent/cook.png"
        hide scene_darkening
        with d3
        $ greenBlush = 0
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task3Stage == 9:
        stop music fadeout 2.0

        scene black with longFade
        $ task3Stage = 10
        scene bgStreet2
        show scene_darkening
        with fade
        play music "audio/music/ambient1.mp3" fadein 2.0
        mel "What's going on out here?!"
        "Aces gangster" "We're under attack from all sides! We've got Punks on our left, Outsiders on our right and WOOHP agents fighting us from our front!"
        mel "WOOHP Agen-...?"
        "Outsiders Chick" "More Aces, get them!"
        mel "Fine... I'll show you how it's done."
        play sound "audio/sfx/laser1.mp3"
        show white
        pause 0.05
        hide white
        pause 0.4
        play sound "audio/sfx/laser1.mp3"
        show white
        pause 0.05
        hide white
        scene black with longFade
        scene bgBase with fade
        pause 0.4
        show scene_darkening with d3
        pause 0.4
        show green at ri
        show red at ce
        if spyYellowActive:
            show yellow at le
        with d3
        y "Okay girls, I received intel that a new Lieutenant has shown herself."
        y "Her name is Melody von...{w} Guggen..."
        y "That's a pretty crazy last name..."
        if spyYellowActive:
            a y29 "Wait, did you say von Guggen?"
        y "That name ring a bell?"
        c r34 "We fought a Helga von Guggen a long time ago."
        s g43 "Could be her granddaughter. She's probably after revenge."
        y "Reports are saying she's hanging out at the Aces Castle, but security is ramped up. You're going to have to get closer before you have a chance to capture her."
        if specialMaggieStatus <= 1 or specialDragonStatus <= 1 or specialMuffyStatus <= 1:
            s "Make sure to focus on capturing the first Lieutenant of each gang first."
            s "We can't risk one gang getting the upperhand over the others."
        elif True:
            y "I'm gonna keep sending you undercover with the Aces. Hopefully we'll get a chance to take her in."
        "The girls nod and leave for their cell."
        stop music fadeout 3.0
        $ mainQuestUpdate = True
        hide green
        hide red
        hide yellow
        with d3
        hide scene_darkening
        with d3
        play music "audio/music/nighttime.mp3" fadein 3.0
        $ task7Text = _("We found a way to get gangleaders out of hiding. If we mess enough with their gang during Landgrabs they'll show themselves.\n\nThen, if our reputation is high enough, we can get close to these lieutenants and try to capture them.\n\n-Reach rank 2 with Drift Punk and the Outsiders.\n-Capture the first Lieutenant of Drift Punk and the Outsiders.")
        jump base

screen task4Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task4Text]"

default task4Stage = 0
default task4Name = ""
default task4Text = ""
default task4Timer = 0
label task4:
    if task4Stage == 0 and task3Stage != 3:
        $ mainQuestUpdate = True
        $ task4Text = _("The girls ran into the final spy and found out about a meeting being held at the school. It appears our cover hasn't been blown yet. I could send the girls out to gather some more information on what's going on and possibly get the yellow spy out.\n\n-Top priority: Visit the school.")
        $ task4Stage = 1
        if firstPick == 1:
            $ task4Name = "Spy in Yellow"
            pause 1.0
            scene bgClub1 with fade
            pause 0.3
            show scene_darkening with d3
            show red r32 at le with d2
            show green g31 at ri with d2
            s "[playerName]! There you are!"
            y "Huh?"
            c "We found Alex! She's going to be at the school."
            y "How do you know?"
            s g33 "Well cause..."
            c "She told us."
            y "Alex told you?"
            c "Yeah~..."
            s g31 "We came across her during our last undercover operation.{w} She's still under WOOHP's control, but she gave us some new intel."
            c r33 "Apparently they still think Sam and I are under nanobot control, but they're starting to have doubts."
            c "Alex said that we are to report to the school. Some big shot is going to make an announcement."
            y "The mastermind?"
            c r37 "Maybe."
            y "I'd say we check it out."
            s g38 "I'd say we check it o-...{w} What you said."
            s "Though we can expect security to be better than before. Even if we're not sneaking in this time, we'd best be prepared."
            if gadgetPowderActive == False:
                s "You should-..."
                y "I should craft you some new gadgets."
                s g29 "Y-yeah... I was thinkin-..."
                y "Maybe try to unlock some new ones."
                s g10 "{b}*Grumbles*{/b} Yeah.... We could really us-..."
                y "Maybe some kind of distraction device that makes agents turn the other way."
                s g4 "{b}*Pouts*{/b}"
                y "Then you can attend the meeting, figure out who's behind all this hallebelu and maybe even rescue Alex!"
                y "...."
                y "What's with the long face?"
                c r24 "Oh don't mind her. Sam had the same idea and just wanted to show off."
                s g40 "{b}*Sputters*{/b} Y-yeah well... I'm glad to see we're all in agreement! The meeting is soon so send us over whenever you're ready, [playerName]."
            elif True:
                s "We coul-..."
                y "We could use that new distraction powder gadget."
                s g29 "Y-yeah that's what I was thinking."
                s "If we get some of those, it's sure to make life easier for us. Even if w-..."
                y "Even if you don't go on a mission, it's good to have some on you at all times."
                s g10 "{b}*Grumbles*{/b} Yes exactly. That's what I was gonna say."
                s "Using the dis-..."
                y "By using the distraction powder, you could have guards turn the other way, allowing you to sneak up on them more easily."
                s g4 "{b}*Pouts*{/b}"
                y "Then you can attend the meeting, figure out who's behind all this hallebelu and maybe even rescue Alex!"
                y "...."
                y "What's with the long face?"
                c r24 "Oh don't mind her. Sam had the same idea and just wanted to show off."
                s g40 "{b}*Sputters*{/b} Y-yeah well... I'm glad to see we're all in agreement! The meeting is soon so send us over whenever you're ready, [playerName]."
            hide green
            hide red
            hide scene_darkening
            with d3
            pause 0.5
            call qAccept from _call_qAccept_2
            scene bgMap:
                zoom 0.5
            with fade
            y "Checking out this meeting at the school should be our top priority...."
            play sound "audio/sfx/drama1.mp3"
            jump worldmap
    if task4Stage == 1:
        if spy1Status == 0 and spy2Status == 0 and spy3Status == 0:
            $ greenHat = 0
            $ redHat = 0
            $ redOutfit = 1
            $ redOutfitArms = 1
            $ greenOutfit = 1
            $ greenOutfitArms = 1
            $ greenNeck = 0
            $ redChest = 0
            $ redBottom = 0
            $ greenChest = 0
            $ greenBottom = 0
            $ greenShoes = 0
            $ redShoes = 0
            $ yellowOutfit = 1
            $ yellowOutfitArms = 1
            scene bgBase with fade
            show scene_darkening with d3
            y "Everyone ready?"
            show green g1 at ri
            show red r1 at le
            with d3
            c "Yes, let's visit the school and get Alex back!"
            if gadgetPowderActive == True and gadgetPowder >= 1:
                s "We have some new gadgets, so I'm sure we'll be fine."
            elif True:
                s "We don't have any new gadgets yet, but I'm sure we'll be fine."
            y "Let's go over the plan one more time."
            s g32 "Right."
            s "Clover and I will head to the school to attend this meeting. Our first objective is to rescue Alex and bring her back to the base."
            s "Our second objective will be to gather new intel and figure out who's running this operation."
            y "With a little luck we might even avoid confrontation."
            menu:
                "Go to the meeting" if True:

                    $ task4Text = _("The girls ran into the final spy and found out about a meeting being held at the school. It appears our cover hasn't been blown yet. I could send the girls out to gather some more information on what's going on and possibly get the yellow spy out.\n\nYou got Alex out in one piece and found out about one of the guys in charge of the WOOHP rebellion Tim Scam, a former WOOHP scientist.\nWith her freed up, I should try sending her out to the Outsiders.")
                    $ task4Stage = 2
                    y "Get ready, I'm sending you two out."
                    c r13 "We're like... totally gonna ace this!"
                    s g33 "We'll bring some spy cameras so you can see what's going on."
                    hide green
                    hide red
                    hide scene_darkening
                    with d5
                    stop music fadeout 2.0
                    scene black with fade
                    $ missionSetting = "School"
                    show text _("Launching mission.\nLocation: Malibu University.")
                    with d5
                    pause 1.5
                    hide text
                    with d5
                    scene bgSchool1 with fade
                    show scene_darkening with d3
                    show agentModel:
                        xalign 0.0 yalign 0.0 xzoom -1
                        linear 2.8 xalign 1.7
                    show agentModel2:
                        xalign 0.05 yalign 0.0 xzoom -1
                        linear 2.8 xalign 1.7
                    show agentModel3:
                        xalign 0.2 yalign 0.0 xzoom -1
                        linear 2.8 xalign 1.9

                    show agentModel4:
                        xalign 0.8 yalign 0.0
                        linear 2.8 xalign -1.6
                    show agentModel5:
                        xalign 1.0 yalign 0.0
                        linear 2 xalign 0.0
                        linear 0.1 yalign 0.2
                        linear 0.1 yalign 0.0
                        xzoom -1
                        linear 1.5 xalign 1.7
                    show agentModel6:
                        xalign 0.9 yalign 0.0
                        linear 2.8 xalign -1.6
                    with d2
                    pause 3.5
                    hide agentModel1
                    hide agentModel2
                    hide agentModel3
                    hide agentModel4
                    hide agentModel5
                    hide agentModel6
                    pause 0.5
                    show red:
                        xalign -0.2 yalign 0.0 zoom 0.9 xzoom -1
                    show green:
                        xalign 0.1 yalign 0.0 zoom 0.9
                    with d3
                    c ".................."
                    s g30 "There sure are a lot of agents here..."
                    c "Could be a trap."
                    s g32 "Yeah... stay on your guard."
                    "Microphone" "{b}*Feedback*{/b}"
                    show red:
                        linear 0.3 xalign -0.3 yalign 0.0
                    show green:
                        xzoom -1
                        linear 0.4 xalign -0.1 yalign 0.0
                    s "They're about to give a speech!"
                    show agentModel:
                        xalign 0.1 yalign 0.0 xzoom -1
                    show agentModel3:
                        xalign 0.2 yalign 0.0 xzoom -1
                    show agentModel6:
                        xalign -0.3 yalign 0.0 xzoom -1
                    show agentModel2:
                        xalign 0.3 yalign 0.0 xzoom -1
                    show agentModel4:
                        xalign 0.0 yalign 0.0 xzoom -1
                    show agentModel5:
                        xalign 0.35 yalign 0.0 xzoom -1
                    with d3
                    c r12 "I can't see anything!"
                    c "Hang on, I'm gonna find a place up high. Just call me if you need backup."
                    show red:
                        linear 0.2 xalign -0.7 yalign 0.0
                    pause 0.5
                    "Microphone" "....................."
                    show O5O at ri with d3
                    pause 0.3
                    "Agent O5O" "{b}*Taps microphone*{/b}"
                    y "Oh no...."
                    with hpunch
                    "Agent O5O" "Mic: ATTENTION VALUED EMPLOYEES OF WOOHP!"
                    with hpunch
                    "Agent O5O" "Mic: FOR THOSE WHO ARE NEW HERE, I AM AGENT {i}O5O{/i}."
                    with hpunch
                    "Agent O5O" "IT IS{size=+4} SO NICE{/size}{size=+8} TO SEE{/size} {size=+14}YOU ALL AGAIN!{/size}"
                    "WOOHP Agent" "{size=-4}Sir! My eardrums are bleeding!{/size}"
                    with hpunch
                    "Agent O5O" "Mic: SORRY I CAN'T HEAR YOU! YOU'LL HAVE TO SPEAK... {w}{size=+10}{b}LOUDER!!!{/b}{/size}"
                    "WOOHP Agent" "Argh!"
                    show agentModel5:
                        linear 0.1 xalign 0.36
                        linear 0.1 xalign 0.35
                        linear 0.1 xalign 0.36
                        linear 0.1 xalign 0.35
                        linear 0.1 xalign 0.36
                        linear 0.1 xalign 0.35
                        pause 0.1
                        linear 0.2 yalign -5.5
                    pause 1.2
                    hide agentModel5 with d2
                    "Agent O5O" "JUST FOR THIS SPECIAL OCCASSION, I'VE PREPARED A LITTLE SPEECH!"
                    "Agents" "{b}*Groan*{/b}"
                    s ".............."
                    cM "Pst Sam, can you hear me? Look past the crowd, to your left."
                    s "....?"
                    $ spyYellowActive = True
                    $ yellowOutfit = 1
                    $ yellowOutfitArms = 1
                    show yellow y52:
                        xalign 0.2 xalign 0.0 zoom 0.9 xzoom -1
                    with d3
                    pause 0.3
                    s g29 "(Alex!)"
                    "Just in time you notice the spy in yellow walking by and heading off into a nearby corridor."
                    hide yellow
                    with d3
                    s "([playerName], Clover. I'm going after her.)"
                    cM "(Roger that, I'll come with you.)"
                    y "(Be careful, this could still be a trap.)"
                    hide agentModel
                    hide agentModel2
                    hide agentModel3
                    hide agentModel4
                    hide agentModel6
                    hide O5O
                    hide green
                    hide scene_darkening
                    with d3
                    scene black with fade
                    $ missionProgression = 0
                    show globalImage:
                        zoom 0.25
                    hide screen interactScreen
                    $ activeSpy = 1
                    $ backupCloverActive = True
                    $ backup2 = 6
                    show spyCorner:
                        xalign 0.90 yalign 0.83 zoom 0.78
                    $ randomExit = 1
                    $ currentPosition = 0
                    $ randomCover2 = 1
                    $ randomCover1 = 1
                    $ randomBackground = 1
                    $ randomBoss = 0
                    $ randomObst1 = 0
                    $ randomObst2 = 1
                    $ randomAgent2 = 1
                    $ obst2FoV = 3
                    $ CoS2 = 100
                    $ disableScreen = False
                    show spyReadyYellow:
                        xalign 0.655 yalign 0.488 zoom 0.21 rotate 5
                    show agentDistractCin:
                        xalign 0.623 yalign 0.49 rotate 6 zoom 0.30
                    s "There she is..."
                    cM "She's talking to a WOOHP agent though... You think she spotted us?"
                    y "Best to not take any chances. Follow that spy and knock out any agents along the way. Clover will provide backup."
                    play sound "audio/voice/onIt1.mp3"
                    s "On it!"
                    stop music fadeout 1.0
                    if gadgetEarrings >= 1:
                        $ missionScreenGadget1Select = 1
                    if gadgetPowder >= 1:
                        $ missionScreenGadget2Select = 2
                    $ missionScreenGadget2Select = 2
                    play music "audio/music/stealth2.mp3"
                    hide spyReadyYellow with d5
                    hide agentDistractCin
                    show obst2:
                        xalign 0.623 yalign 0.49 rotate 6 zoom 0.30
                    $ _skipping = False
                    $ disableScreen = False
                    show screen equipmentMenu
                    $ disableScreen = False
                    $ missionProgression = 0
                    call screen interactScreen
                "Wait a while longer" if True:
                    y "There's still some time, make sure that you're prepared."
                    c "All right, [playerName]. Don't wait too long though."
                    hide green
                    hide red
                    with d3
                    call greenOutfitSet from _call_greenOutfitSet_2
                    call redOutfitSet from _call_redOutfitSet_2
                    hide scene_darkening
                    scene bgMap:
                        zoom 0.5
                    with fade
                    jump worldmap
        elif True:
            y "I'll have to make sure everyone's available first."
            jump worldmap
    if task4Stage == 2:
        hide screen gadgetMenu
        $ task4Text = _("The girls ran into the final spy and found out about a meeting being held at the school. It appears our cover hasn't been blown yet. I could send the girls out to gather some more information on what's going on and possibly get the yellow spy out.\n\nYou got Alex out in one piece and found out about one of the guys in charge of the WOOHP rebellion Tim Scam, a former WOOHP scientist.\n\nWith her freed up, I should try sending her out to the Outsiders sometime.")
        $ task4Name = _("Spy in Yellow")
        $ task4Stage = 3
        hide screen equipmentMenu
        show globalImage:
            zoom 0.25
        with fade
        hide screen interactScreen
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        $ randomExit = 2
        $ currentPosition = 0
        $ randomCover2 = 2
        $ randomCover1 = 2
        $ randomBackground = 1
        $ randomObst1 = 1
        $ obst1FoV = 1
        $ activeSpy = 1
        $ missionProgression = 0
        $ backupCloverActive = True
        show obst1:
            xalign 0.365 yalign 0.43 rotate 2 zoom 0.48
        $ randomObst2 = 0
        show spyFlirt1Yellow:
            xalign 0.32 yalign 0.48 zoom 0.425
        with d3
        a "Oooooh, have you been working out?~"
        "Agent" "I am so happy you noticed!"
        a "You know~... Maybe you and I should slip away and {b}*Whisper* *Whisper* *Whisper*{/b}"
        "Agent" "Such suggestions made me detect an anomaly.... in my pants!"
        "Agent" "............................"
        "Agent" "Funny! My desire to burn a dumpster or kick a puppy have suddenly left me completely!"
        s "....?"
        a "See you soon~..."
        $ CoS1 = 100
        hide spyFlirt1Yellow
        with d3
        pause 0.5
        show scene_darkening
        show green at ri with d3
        s "(Did you see that, [playerName]?)"
        y "Yeah, she's up to something."
        s "(Okay, I'm going to keep following he-...)"
        s g9 "Ngh~...!!!"
        y "Sam?"
        s "Use... the... V.I.B....!"
        play sound "audio/sfx/shockcrash.mp3"
        pause 0.7
        hide green
        show white
        pause 0.05
        hide white
        hide screen equipmentMenu
        show bgControl
        show green g100 at ri
        pause 0.6
        hide bgControl
        hide green
        hide scene_darkening
        with d3
        pause 0.4
        show scene_fighting with d3
        "It's time to use your equipment. Your spies are each equipped with a V.I.B. which can be used to break them out of Nanobot control."
        "Use the V.I.B. by {b}pressing 1{/b} on your keyboard to equip it. But be warned, using the V.I.B. for too long can give away a spy's location."
        "You can stop the V.I.B. by {b}pressing 1{/b} again."
        hide scene_fighting with d2
        show screen gadgetMenu
        $ renpy.pause(hard='True')
        call screen interactScreen
    if task4Stage == 3:
        hide screen equipmentMenu
        $ spyYellowActive = True
        $ task4Stage = 4
        hide screen gadgetMenu
        if firstPick == 1:
            $ activeSpy = 1
            $ randomObst1 = 0
            $ randomObst2 = 0
            hide obst1
            hide obst2
            show globalImage:
                zoom 0.25
            with fade
            show spyReadyYellow:
                xalign 0.655 yalign 0.488 zoom 0.21 rotate 5
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            $ randomExit = 0
            $ currentPosition = 0
            with d3
            hide screen interactScreen
            $ _skipping = True
            sM "It's a dead-end... We got her now!"
            y "Great."
            y "......................"
            y "So how are you going to break the nanobot control over her?"
            sM "O-oh! Well... I...!"
            show scene_darkening with d3
            show yellow at le with d3
            a y16 "Is someone there...?"
            y "Kiss her! It worked last time!"
            s g30 "Nooo~... Alex is my friend. It'd be super awkward!"
            y "......."
            cM "I'll do it!"
            show spyFallingTut:
                xalign 0.63 yalign -0.5 zoom 0.20
                linear 0.32 xalign 0.63 yalign 0.49
            pause 0.34
            play sound "audio/sfx/punch1.mp3"
            stop music fadeout 2.0
            hide screen equipmentMenu
            scene black
            hide spyFallingTut
            hide spyReadyYellow
            hide globalImage
            pause 0.5
            "Out of nowhere, Clover jumps on Alex, pins her to the ground and kisses her deeply!"
            scene kiss2 with fade
            pause
            a "Mpffhh!!!"
            a ".................."
            c ".................."
            scene black with fade
            a "Oh hi Clover!"
            c "...?"
            show globalImage:
                zoom 0.25
            with fade
            show scene_darkening
            with d3
            show yellow y55 at le
            show red r29:
                xalign 0.8 yalign 0.0
            show green g16:
                xalign 1.1 yalign 0.0
            with d3
            s g16 "Alex...?"
            a "Oh Sam, you're here too!"
            y "Is she... not being controlled?"
            c r10 "Alex we've been looking for you. Are you okay?"
            a y28 "I think so. I'm so glad I'm not the only one who hasn't gone crazy!"
            s g29 "But how did you break the nanobot control...?"
            a y23 "Oh er... Well I might've stumbled into the male WOOHP changing room by accident..."
            a y1 "After that I've been back to normal.. for the most part."
            a "What about you two?!"
            s g29 "It's a long story. We'll tell you later. For now, we-..."
            stop music fadeout 3.0
            hide green
            hide red
            hide yellow
            with d3
            "Intercom" "I'M SORRY TO CUT MY SPEECH SHORT, I KNOW YOU WERE ALL DYING TO HEAR IT, BUT I HAVE AN IMPORTANT MESSAGE FROM ONE OF THE HIGHER UPS."
            "Intercom" "PUTTING IT ON SCREEN NOW!"
            "Suddenly the hallway screens flicker to life."
            play music "audio/music/ambient1.mp3" fadein 3.0
            hide globalImage
            hide scene_darkening
            hide screen equipmentMenu
            with d10
            pause 2.0
            scene bgWOOHP
            show scene_camera
            with d5
            pause 0.5
            hide scene_camera
            show timModel at ce
            show scene_camera
            with d10
            pause 0.5
            "???" "Attention WOOHP Agents..."
            sM "(That voice...!)"
            cM "Is that...?"
            hide timModel
            with d3
            $ timHidden = False
            hide scene_camera
            show timModel at ce
            show scene_camera
            with d3
            "I have an important announcement for you all..."
            cM "Tim!"
            y "Tim...?"
            cM "Sam's ex-boyfriend. We've fought him before."
            sM "He's not my ex-boyfriend!"
            aM "Shhhh."
            tim "There have been reports of desertion amongst our ranks. Dissension will not be tolerated and those who leave our cause will be dealt with."
            tim "We will be keeping closer tabs on everyone from now on.{w} If we find some of you lacking in your devotion to the mission, know that {i}'correction'{/i} will be swift and without mercy."
            tim "Tim Scam out."
            hide scene_camera
            hide timModel
            scene black with fade
            pause 1.0
            show globalImage:
                zoom 0.25
            show yellow at le
            show red:
                xalign 0.8 yalign 0.0
            show green g33:
                xalign 1.1 yalign 0.0
            with d3
            s "..............."
            c r32 "Should've known that Tim was behind this whole thing. He's got a bone to pick with WOOHP."
            a "And he probably wants to get revenge on his ex-girlfriend!"
            s g40 "I am {b}not{/b} his ex-girlfriend!"
            y "I think this is a good time for me to pull you three out. Meet me back at the base."
            hide globalImage
            hide yellow
            hide red
            hide green
            with d3
            scene black with fade
            pause 1.5
            scene bgBase
            with d3
            stop music fadeout 1.5
            pause 0.5
            "{b}*Ssssssswooosh!*{/b}"
            show scene_darkening
            with d3
            with hpunch
            show green g39 at le
            show red r11 at ri
            show yellow y15 at ce
            with d3
            play music "audio/music/nighttime.mp3" fadein 1.5
            y "......................."
            y "So I feel like I need to be informed."
            s ".............."
            c r33 "Tim Scam is a former WOOHP scientist who went rogue. Selling his tech to the highest bidder. We fought him a few years ago."
            a y28 "Yeah, we went to space! It was crazy!"
            y "And he's Sam's ex?"
            s g12 "No!{w} Listen, it's complicated..."
            c r22 "She had a huge crush on him and he on her."
            s g17 "Guys....!!!"
            s "It never went anywhere, okay?! Him turning out to be evil was a huge turn-off!"
            a y18 "We didn't know him as Tim Scam back then... but as Mac Smit.{w} Looking back on it, it's amazing that he managed to trick the world's largest anti-terrorist organization just by spelling his name backwards."
            c r12 "Yeah, not one of WOOHP's finest moments."
            y "So is Sam's relation with him going to be an problem for our mission?"
            s g38 "No. I'm completely over him.{w} Right girls?"
            c r10 "..........................."
            a y35 "..........................."
            s g28 "Oh come on! Atleast you know I won't take some boy over you guys, right?"
            a y55 "That's true..."
            c "All right Sammy, we trust you on this one."
            y "There's one other thing..."
            y "His warning about keeping a closer eye on everyone. If he finds you serving milkshakes at a diner, he might become suspicious."
            y "Going undercover and causing chaos with the different gangs in town will help a little, but if we want to stay under the radar, we might have to one-up it a bit."
            y "Let's keep track of our notoriety from now on. I'm sure we'll find a way to boost it and keep any suspicion off of us."
            a y29 "Notoriety...?"
            s g4 "We're gonna have to commit more crimes?"
            y "Just think of the end-goal here. We gotta free the city and if we have to break a few windows to do so, then so be it."
            s "I guess."
            c r13 "Plus! I'm sure WOOHP has insurance. We might piss off some people now, but it'll sort itself out later down the line!"
            y "All right. You two fill Alex in on what's been happening here. Good work out there girls."
            "The girls nod and head off to the detention area."
            hide scene_darkening
            hide green
            hide red
            hide yellow
            with d5
            pause 0.5
            $ yellowChestSet = 1
            $ yellowBottomSet = 1
            $ yellowShoesSet = 1
            $ yellowUnderSet = 1
            $ samHealth = 3
            $ cloverHealth = 3
            jump jobReport

    if task4Stage == 4:
        $ task4Stage = 5
        if firstPick == 1:
            $ mapSpy3Active = True
            pause 0.5
            show scene_darkening
            with d3
            pause 0.3
            show yellow y1 at ri
            with d3
            a "Morning [playerName]!"
            y "Alex, are you okay?"
            a "Yeah totally. What can I do to help?"
            y "Well...."
            y "I want you to go undercover with the Outsiders."
            if gang3Active == False:
                y "I'm just going to need a contact, but I'm sure I'll get one if I keep exploring around."
            a y29 "The Outsiders...?"
            a y28 "Wait those are those goths and punkers! I don't wanna go there!"
            y ".................."
            a y29 "They're scary!"
            y "Scary?"
            a "With all those black clothes and spikes! They're spooky!"
            a "And I'm pretty sure that they're....{w}{size=-10}vampires{/size}"
            y "You'll be fiiiine."
            a y4 "{b}*Pouts*{/b}"
            hide yellow
            hide scene_darkening
            with d3
            call qUpdated from _call_qUpdated_4
            jump worldmap
    if task4Stage == 5:
        $ task4Stage = 6
        if firstPick == 1:
            pause 1.0
            $ task4Text = _("The girls ran into the final spy and found out about a meeting being held at the school. It appears our cover hasn't been blown yet. I could send the girls out to gather some more information on what's going on and possibly get the yellow spy out.\n\nYou got Alex out in one piece and found out about one of the guys in charge of the WOOHP rebellion Tim Scam, a former WOOHP scientist.\nWith her freed up, I should try sending her out to the Outsiders sometime.\n\nAlex is going to need some time to fit in with the Outsiders, but contact has been made. I should send her out again.")
            $ task4Name = _("Spy in Yellow")
            y "............................"
            y "Where's Alex...?"
            "{b}*Beep* *Beep* *Beep*{/b}"
            y "...?"
            scene black
            show yellow y30 at ri
            show scene_camera
            with fade
            pause 0.5
            y "Alex? Where are you?"
            a "I'm hiding!"
            y ".........."
            y "From what?"
            a "From the vampires! It's full of monsters here!"
            a y28 "I saw a guy wearing black lipstick and a girl with a spiked dog collar around her neck!"
            y "............"
            a "Did you know their base is at a haunted amusement park?! There's for real ghosts in this place!"
            y "Alex..."
            a y42 "I've been hiding in the hotdog stand all day!"
            a "Please get me out of here, [playerName]~....!"
            y "All right you scaredy cat... I'll use the tunnel network..."
            show yellow:
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.15 yalign 1.0 yalign 6.5
            pause 1.7
            hide scene_camera
            scene bgBase
            with fade
            pause 0.5
            with hpunch
            show scene_darkening with d3
            show yellow y14 at ri with d3
            pause 0.5
            a "Oof~..."
            y "Welcome back Alex."
            a y19 "Hey~..."
            y "So...{w} vampires..."
            a y28 "I know right! They're so creepy!"
            a "They're wearing all black or have cut their hair into these evil mohawk shapes! I'm sure they're vampires! And mummies!"
            y ".............."
            a "I saw someone who was so ugly, I'm pretty sure he was a zombie."
            y "You know the Outsiders are just kids dressed up in punk and goth clothing, right?"
            a "I saw one turn into a bat!"
            y "Did you...?"
            a y14 "Well... okay I may have imagined that bit. But they could have!"
            y "Alex..."
            y "I won't deny that they're dangerous, but they're not supernatural. Did you even talk to any of them?"
            a "No... I was too busy hiding."
            y "Did you manage to gather any intel...?"
            a "................"
            y "All right, you're going back tomorrow."
            a y30 "W-what?!"
            y "And this time, you're going to try and blend in, okay?"
            a y29 "But what if they bite me....?"
            y "Then you bite back. Head back to your cell."
            a "But...!"
            y "Cell."
            a y5 "{b}*Whines*{/b}"
            $ spy3Status = 0
            hide yellow
            hide scene_darkening
            with d3
            call qCompleted from _call_qCompleted_2
            jump base
    if task4Stage == 6:
        $ task4Name = "Spy in Yellow (Complete)"
        $ task4Stage = 7
        if firstPick == 1:
            $ greenOutfit = 1
            $ greenOutfitArms = 1
            $ greenArms = 1
            $ greenChest = 0
            $ greenBottom = 0
            $ greenShoes = 0
            $ redOutfit = 1
            $ redOutfitArms = 1
            $ redArms = 1
            $ redChest = 0
            $ redBottom = 0
            $ redShoes = 0
            $ yellowOutfit = 1
            $ yellowOutfitArms = 1
            $ yellowArms = 1
            $ yellowChest = 0
            $ yellowBottom = 0
            $ yellowShoes = 0

            $ greenUnder = 0
            $ redUnder = 0
            $ yellowUnder = 0
            pause 1.0

            $ nanoLevelSam = 10
            $ nanoLevelClover = 10
            $ nanoLevelAlex = 10
            y "............................"
            y "Again no Alex..."
            y "Let's see if I can reach her..."
            y "{b}*Beep*{/b}"
            scene black
            show yellow y43 at ri
            show scene_camera
            with fade
            pause 0.5
            a "I don't know if this is such a good idea..."
            "Outsider" "Relax, we've done it before and it didn't hurt any of us."
            "Huge Outsider" "IT MAKE ME BIG! AND MAKE ME DREAM BIG! ME FOR PRESIDENT!"
            "Outsider" "Okay so it might have some side effects if you use too many at once..."
            "Outsider" "But it's fine in small dosis. Plus it will really give us a leg up on the rival gangs."
            "Outsider" "Here you go, this one's free. Try it and see if you like it."
            a y37 "Okay~...."
            y "Pst... Alex!"
            a "...?"
            a y1 "Oh hello tiny [playerName]. I was just on my way back."
            y "What was that all about?"
            a "They gave me a nanobot injector. I'll tell you more once I get back to the base."
            show yellow:
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.1 xalign 1.01 yalign 0.0
                linear 0.1 xalign 1.0 yalign 0.0
                linear 0.15 yalign 1.0 yalign 6.5
            pause 1.7
            hide scene_camera
            scene bgBase
            with fade
            pause 0.5
            with hpunch
            show scene_darkening with d3
            show yellow y14:
                xalign 1.2 yalign 0.0
            with d3
            pause 0.5
            a "Oof~...!"
            a "Well that was fast..."
            y "So, what did you find out?"
            a y1 "Well...!"
            a y29 "Wait, do I get a cookie for doing a good job?"
            y "..............."
            menu:
                "What are you? A puppy?" if True:
                    a y1 "I can be! {b}*Wraf* *Arf*{/b}"
                    y ".........................."
                    y "Oh my god, this is actually happening!"
                    y "Alex, give paw!"
                    "The spy plays along and gives you her hand."
                    y "This is amazing!"
                    y "Alex, roll over!"
                    with vpunch
                    y "Hah! Okay okay, one more. Alex....{w} stop messing around and tell me what you found out already."
                    a y29 "{b}*Warf* *Wa-*{/b}.... Oh...{w} Sorry, I sometimes get a bit too carried away!"
                    y "(Weirdo)."
                "Order Alex to report (-Karma)" if True:
                    $ playerKarma -= 5
                    y "Alex, I order you to report."
                    a y29 "N-no I was just kid-...."
                    "....................."
                    a y39 "Reporting as ordered, sir....~"
                "Say something insane" if True:
                    y "D-...{w}does someone want a Scooby Snack....?"
                    a y16 "I'm not a dog, [playerName]~...."
                    y "What about....{w}{b}2{/b} Scooby Snacks?"
                    a y8 "[playerName]! Those are dog treats! Stop pretending that I'm a dog!"
                    y "Okay okay...."
                    y "....................."
                    a y10 "....................."
                    y "What about {b}THREE{/b} Scooby Snacks?!"
                    a y40 "Argh! Never mind, I'll tell you all ready!"
            a "So where to begin..."
            a "So the vampires found out-..."
            y "Vampires? Still on that?"
            a y39 ".................."
            a "So the {i}'alternative crowd'{/i} kids told me something about the nanobots."
            a y29 "Apparently there are special nanobot injections that gives bonuses and secret powers which boost your natural abilities."
            y "Natural abilities?"
            a "Yeah, y'know. Run faster, jump higher....{w} turn invisible."
            y "Wait, what was that last one?"
            a "I know, right! Inject enough nanobots and you get super cool new abilities!"
            a "Here...{w} They gave me an injector so I could try it out."
            pause 0.5
            show scene_fighting with d5
            "You have unlocked the ability of boosting your spies' skills by injecting nanobots."
            hide scene_fighting
            show bgNanoTut
            with d5
            "Check your inventory for nanobot injectors. Using an injector will take you to the Injector screen."
            hide bgNanoTut
            show bgNanoTut2
            with d5
            "Injecting your spies with nanobots will upgrade their skills when doing missions. Such as higher take-down chance or better hacking."
            "Be warned however. If your spies nanobot control gets too high, it may bring unwanted side-effects with it."
            "Spies will begin stealing money from their dayjobs, more easily get controlled during missions and might even decide to go AWOL for a few days."
            "You can suppress a girl's nanobot control by having them preform sexual acts or adjusting their nanobot control levels via the STATUS screen."
            hide bgNanoTut2 with d5
            "......................."
            a "But.."
            y "But...?"
            a y19 ".................."
            a "{size=-6}I don't like needles...{/size}"
            y "........................."
            y "Get over here, I'll Inject you myself."
            a y29 "Noooo!"
            y "Alex, get over here!"
            a y28 "NOOOOOOO!"
            "You try grabbing the spy, who struggles to get away from you like a mange cat."
            with hpunch
            a "{size=+6}{b}NOOOOOOOOOOOO!{/b}{/size}"
            show green g17 at ri with d3
            s "What's going on in here...?"
            show yellow:
                linear 0.1 xalign 1.1 yalign 0.0
            a "Sam! Save me!!!"
            with hpunch
            s g30 "H-hey, hey!{w} OW!"
            "You accidentally injected Sam!"
            s g8 "Ow... What was that all abou-...."
            s "!!!"
            play sound "audio/sfx/shockcrash.mp3"
            pause 0.7
            hide green
            show white
            pause 0.05
            hide white
            show bgControl
            stop music fadeout 1.5
            show green g100:
                xalign 1.0 yalign 0.0
            pause 0.6
            hide bgControl
            play music "audio/music/ambient1.mp3" fadein 1.5
            s "All hail the mastermind! {w}Down with WOOHP!{w} DESTROY ALL OPPOSITION!"
            y "Okay Sam... I know that you're currently feeling the need to overthrow the Norwegian monarchy or something, but you gotta focus..."
            y "................."
            y "I need you to turn invisible!"
            s "{b}*Growls*{/b}"
            y "So you see, that's not actually a confirma-...."
            hide yellow
            hide green
            with d2
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            "Sam attacked you!{w} ...........{w} Again..."
            y "Oh crap! Alex, quickly break her out of her trance!"
            a "S-sure...!"
            hide green
            hide yellow
            scene black
            with fade
            "Alex firmly grabs Sam by her hair and pulls on it before kissing her tenderly on the lips."
            a "Hmm~.... ♥"
            "............................................."
            show green g100 at ri with d3
            y "Phew~... Disaster avoided. I was worried there for a secon-...."
            hide green with d2
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            "Sam attacked again!"
            y "Argh...!"
            "The spy jumps on top of you and begins wailing away."
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            pause 0.5
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            y "Ow! Aow! Alex, you didn't do it right!"
            aM "I-... I'm sorry!"
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            aM "Although come to think of it...."
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            pause 0.5
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            aM "I do remember the Outsiders warning me about this and how to fix it..."
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            pause 0.5
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            y "Today please, Alex!"
            aM "Some of the Outsiders figured out that oxyto-whatever reduces the nanobot control, but your brain gets used to the feeling after a while!"
            y "What?!"
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            aM "They said that you may have to expose yourself to more risqué things else you stay mindcontrolled."
            y "Risqué? Okay quickly! {w}Alex, show your boobs!"
            aM "What? No way!"
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            y "Alex! I'm starting to see in black and white, you gotta do it now!"
            aM "But...! I don't wanna show you my titties!{w} My mom always says: {w}''Alex, if a co-worker asks you to show your breasts, firmly tell them {b}no{/b}.''"
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            pause 0.5
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            y "ALEX! I'M STARTING TO TASTE COLORS, DO IT NOW!"
            aM "........................."
            aM "Well... Okay fine. Just don't tell my momma, okay?"
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            pause 1.0
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            y "{b}*Gstfs~.... =(*{/b}"
            $ yellowArms = 3
            $ yellowOutfit = 2
            $ yellowOutfitArms = 3
            play sound "audio/sfx/cloth.mp3"
            show yellow y19:
                xalign 0.8 yalign 0.0
            with d2
            show green g100 at le:
                xzoom -1
            with d3
            s "I'm going to take you down....{w} I'm going to tie you up over a roaring fire...{w} And then I'm going to cannibalise you!"
            hide green with d2
            show green g100 at le with d2
            s "Then... I'm.... going...{w} to....{b}{w}*Blinks*"
            stop music fadeout 1.5
            hide green with d2
            show green g28 at le with d3
            pause 0.3
            s g29 "Alex...?"
            s g28 "Oh no, [playerName]!"
            show red r16:
                xalign 1.2 yalign 0.0
            with d3
            c "What's going on in here...?"
            c r51 "Er... Alex...{w} Your tits are out...{w} And what happened to [playerName]?!"
            y "{b}*gsfsfstfzle~....*{/b}"
            s g42 "I... I attacked him again...! I'm so sorry, [playerName]!"
            hide yellow
            with d2
            $ yellowOutfit = 1
            $ yellowArms = 1
            $ yellowOutfitArms = 1
            show yellow:
                xalign 0.8 yalign 0.0
            with d2
            a y29 "Is he going to be all right...?"
            y "I wanna {size=+6}go{/size}{size=+10}to{/size}{size=+6}DISNEYLAND{/size}{size=+6}and{/size}see{size=-4}the{/size}{size=-10}elepha-....{/size}"
            play sound "audio/sfx/punch1.mp3"
            hide green
            hide red
            hide yellow
            stop music
            scene black
            with hpunch
            pause 1.0
            "You passed out."
            $ task5Stage = 1
            pause 1.0
            jump nightCycle




default task5Stage = 0
default task5Name = ""
default task5Text = ""
default task5Insane = True
default task5Nudes = False
default task5DildoPrice = 100
default task5Pics = False

screen task5Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task5Text]"

label task5:
    if task5Stage == 1:
        $ task5Stage = 2
        pause 1.0
        y "Ugh... My head~..."
        pause 0.3
        show scene_darkening with d3
        show green g42 at ri with d3
        s "Good morning, [playerName]. Sorry about yesterday... Are you all right?"
        y "Yeah... It was a stupid idea of me to inject you guys with {i}'more'{/i} nanobots anyways."
        s g19 "Well.....{w} Maybe not entirely stupid."
        y "...?"
        s "After you passed out, I did some self-analysis and we did notice a difference in our skills..."
        y "You did?"
        s "Yeah, it seemed to have boosted my strength considerably. "
        s "So taking down obstacles during missions should be easier now."
        y "It's no invisibility, but it's something."
        s "There's a risk though. The more nanobots we inject, the more likely we are to being taken over."
        s "Which means more serious ways of suppressing our nanobots."
        y "Interesting... we should keep our eyes out for these special injectors."
        y "So you're saying you really got stronger, just by injecting a syringe of nanobots?"
        play sound "audio/voice/yeah2.mp3"
        s g1 "Yeah! Here I'll show you."
        y "No no n-..."
        hide screen skillScreen
        play sound "audio/sfx/punch1.mp3"
        scene black with hpunch
        stop music fadeout 2.0
        pause 2.0
        show text _("The night passes and all is....")
        with d5
        pause 2.5
        y "Gah!" with hpunch
        hide text
        scene bgBase with d3
        show scene_darkening with d3
        show red r16 at le
        show green g28 at ri
        with d3
        c "He's waking up!"
        y "Ugh~...."
        s "Are you okay, [playerName]...?"
        y "................."
        y "Yeah I'd say you're {i}'definitely'{/i} stronger."
        y "This is great news!"
        play music "audio/music/daytime.mp3" fadein 3.0
        s g19 "........................................"
        c r32 "[playerName]....."
        c r31 "You've been out for 24 hours."
        y "!!!"
        c "And Sam here hasn't really been feeling herself as of late. Have you Sam...?"
        s ".........................."
        y "What happened?"
        c "The nanobot injector seems to have boosted Sam's abilities, but she's much more prone to getting controlled now."
        y "Can't we just have Alex show her tits again?"
        s "It helps... but only a little..."
        s "We might have to think of a more effective way..."
        y ".........................."
        label task5Menu1:
            pass
        menu:
            "Dildos" if True:
                y "I'm gonna buy you three a dildo."
                s g28 "A what?!"
                c r18 "A dildo...?"
                y "Yeah, it seems like a good first step. It should keep your nanobots suppressed for a while if you use one."
                s g30 "First step...?"
                c r48 "Er... heh heh~... erm... I guess so...."
                show yellow:
                    xalign 1.2 yalign 0.0
                with d3
                a "[playerName] you woke up!"
                a "What are you all talking about?"
                y "Dildos."
                a y18 "....?"
                a "What's that?"
                hide green with d2
                show green g32:
                    xalign 1.0 yalign 0.0 xzoom -1
                with d2
                s "{b}*Whisper* *Whisper* *Whisper*{/b}"
                a y29 "Oooooh.....{w}.........{w} Why are we talking about that?!"
                y "I'm buying all three of you a dildo."
                "..................."
                "The three girls all look nervous, but not reluctant. {w}Maybe even.... excited...?"
                y "I'm gonna go find you girls some toys. If Sam goes crazy again, you know what do do."
                "The girls nod and head back to their cells."
                hide green
                hide yellow
                hide red
                with d3
                hide scene_darkening
                with d3
                pause 1.0
                y "(The mall is probably a good place to look...)"
                call qAccept from _call_qAccept_3
                $ slutLevel = 1
                $ task5Name = _("Dingalingaling")
                $ task5Text = _("The nanobot control of the spies is getting stronger and I'm going to have to figure out a way to reduce it. I should probably stop by the mall to pick them up some dildos.")
                scene bgMap with fade:
                    zoom 0.5
                jump worldmap
            "Shower curtains" if task5Nudes == False:
                $ task5Nudes = True
                y "Let's remove your shower curtains."
                play sound "audio/voice/what.mp3"
                s g16 "W-what...?!"
                c r18 "You mean in our cells?"
                y "Yup."
                s g17 "B-but what if we want to take a shower?!"
                y "................."
                s g19 "Oh... That's kinda the point... okay got it."
                c r23 "Well... I guess showing ourselves off a little bit from time to time isn't gonna hurt...."
                c "We've seen eachother naked before after all."
                s g32 "T-that's not the problem..."
                "The spies look at you."
                y "The problem is I. {w}I am the problem."
                c r10 "............."
                s "............."
                y "It'll be a good way to help reduce the nanobot control. Plus, I get to see you guys naked from time to time! It's a win/win!"
                s "[playerName]....."
                c r12 "He might have a point, Sam..."
                c "So what... he'll be able to sneak a peak at us while showering. Let him, it's not the end of the world."
                s g29 "B-but....!"
                c "It's fine. We've got nothing to be ashamed of and I'm sure he won't be a perv all the time, right [playerName]?"
                y "I make no promises."
                s g39 "................."
                s g38 "{size=-8}Fine...{/size}"
                s "{size=-8}I... I don't like it, but I think it's a good idea...{/size}"
                c "Fine, [playerName], feel free to remove our shower curtains if you want."
                s g37 "But...."
                s "I don't think that's going to completely solve this nanobot problem..."
                c "Yeah...."
                jump task5Menu1
            "Unzip your pants" if True:
                s g30 "!!!!"
                c r30 "H-HEY!!!"
                y "................"
                y "Sorry, I may have gotten a bit too excited."
                s g8 "We're not sleeping with you, if that's what you're implying!"
                y "What?! That's not at all what I was implying!"
                s g19 "O-oh... Sorry, I thought that y-..."
                c r12 "Sam... that's {i}'exactly'{/i} what he's implying."
                y "{b}*Smirk*{/b}"
                s g8 "I-.. I knew that!{w} Don't you even think about it, [playerName]!"
                c "We're not sleeping with you."
                y "Ahw...."
                c "Now let's think of an actual idea."
                jump task5Menu1
            "Say something insane" if task5Insane:
                $ task5Insane = False
                y "I have a great idea! We should-...{w}{b}*Hmpf!*{/b}"
                "Clover put her hand over your mouth!"
                c r10 "Before you say anything, ask yourself: {i}'Am I going to say something insane?'{/i} and then ask yourself {i}'Is this in any way going to improve our situation?'{/i}"
                y "R-....{w}Rhinos..."
                c "[playerName]~...."
                y "Okay fine... Rhinos might not be the solution....{w} At this time...."
                y "Oh! But we cou-...."
                c "We can't call the Justice League either."
                y "Oh...."
                y "B-..."
                c "And neither can we call the Avengers."
                y "I'm out of ideas."
                jump task5Menu1
    if task5Stage == 2:
        $ sexAct1 = "Camera"
        y "(Dildos.... dildos...{w} Where can I find those...?)"
        y ".................................."
        show scene_darkening with d3
        pause 0.5
        $ clerkFace = 2
        show clerk at ri with d3
        "Clerk" "Hello sir, welcome to the stor-....{w} You again?"
        y "Yes! I have an urgent need for dildos!!!"
        $ clerkFace = 1
        "Clerk" "........................."
        if uniformLoan == 1:
            "Clerk" "Okay.... after you give me what you owe."
            y "Owe?"
            "Clerk" "You... You promised me pictures!"
            y "Riiiiight~...."
            "Clerk" ".........................."
            y "..............................."
            "Clerk" "You don't have them, do you?"
            y "I may have forgotten~...."
        if uniformLoan == 2:
            $ task5DildoPrice += 100
            "Clerk" "And are you going to steal them like you did the waitress uniform?"
            y "Steal?! There must be some kind of mistake! I didn't steal the uniform....!"
            y "I er...."
            y "Borrowed it for Marketing Purposes.....~"
            "Clerk" "................................"
            y "Okay fine... maybe we can work out a deal...."
        "Clerk" "Fine...."
        "Clerk" "You can either pay me $[task5DildoPrice] or...."
        y "........................"
        "Clerk" "Erm....."
        "Or you can send me pics....."
        pause 0.4
        hide scene_darkening
        show scene_fighting
        with d3
        "You have unlocked the ability to take photos of your spies!"
        "At night you can ask your spy to pose for you. Taken pictures will be added to your inventory."
        "Getting photographed slightly lowers a spy's nanobot control, but also lowers their morale."
        "Pictures can be traded with the female store Clerk for kinky gear and toys."
        pause 0.3
        hide scene_fighting
        hide clerk
        show scene_darkening
        show clerk at ri
        with d3
        pause 0.1
        $ clerkFace = 2
        "Clerk" "So? What will it be?"
        menu:
            "Return with pictures" if True:
                $ task5Stage = 2.5
                y "I'll be back!"
                hide scene_darkening
                hide clerk
                with d3
                scene bgMap:
                    zoom 0.5
                with d3
                jump worldmap
            "Pay the $[task5DildoPrice]" if True:
                if cash < task5DildoPrice:
                    y "(Dang, I don't have enough money!)"
                    $ clerkFace = 1
                    "Clerk" "..........................."
                    y "I seem to be light on money...{w} again..."
                    y "I'll return later!"
                    hide scene_darkening with d3
                    scene bgMap:
                        zoom 0.5
                    with d3
                    jump worldmap
                elif True:
                    $ task5Stage = 3
                    $ cash -= task5DildoPrice
                    $ clerkFace = 2
                    "Clerk" "Pleasure doing business with you...."
                    "Clerk" "Please follow me."
                    hide scene_darkening with d3
                    jump task5
    if task5Stage == 2.5:
        $ clerkFace = 2
        show scene_darkening
        show clerk at ri
        with d3
        "Clerk" "Oh you're back."
        menu:
            "Trade pictures" if task5Pics:
                $ task5Stage = 3
                $ samPics = 0
                $ cloverPics = 0
                $ alexPics = 0
                y "Here you go, you perv."
                $ clerkFace = 1
                "Clerk" "Takes one to know one."
                $ clerkFace = 2
                "Clerk" "All right, let's get you some dildos."
                jump task5
            "Pay [task5DildoPrice]" if cash >= task5DildoPrice:
                $ task5Stage = 3
                $ cash -= task5DildoPrice
                "Clerk" "Fair enough. All right, this way. We keep them in the Dicktionary section."
                y "All right!{w} ...... wait what?"
                $ clerkFace = 1
                "Clerk" "You heard what I said...."
                jump task5
            "Come back later" if True:
                hide scene_darkening
                hide clerk
                with d3
                scene bgMap:
                    zoom 0.5
                with d3
                jump worldmap
    if task5Stage == 3:
        $ task5Stage = 4
        scene bgMall with fade
        show scene_darkening with d3
        show clerk at ri with d3
        "Clerk" "What kind do you want?"
        y "What kind?"
        "Clerk" "Yeah, we've got small ones, big ones... gigantic ones."
        "Clerk" "Ones that vibrate, ones that sparkle... {w}ones that call you a whore."
        y "I never knew there were so many options...."
        "Clerk" "Ones that go in both holes, ones labelled 'friendzone'.... those are for decoration only."
        y "I just want three normal ones."
        $ clerkFace = 1
        "Clerk" "Boring...."
        "Clerk" "I got these ones in green, yellow and red."
        y "Perfect! I'll take 'em."
        "Clerk" "All right, I'll wrap them up for you. Come again...."
        hide clerk with d3
        play sound "audio/sfx/itemGot.mp3"
        "You got {color=#ffeda6}Dildos{/color}!"
        hide scene_darkening with d3
        scene bgMap:
            zoom 0.5
        with d3
        y "(I should talk it over with my spies when I get the chance.)"
        $ task5Text = _("The nanobot control of the spies is getting stronger and I'm going to have to figure out a way to reduce it. I should probably stop by the mall to pick them up some dildos.\n\n-I bought the girls some dildos. Let's see how they react.")
        jump worldmap
    if task5Stage == 4:
        $ sexAct2 = "Dildo"
        $ task5Text = _("The nanobot control of the spies is getting stronger and I'm going to have to figure out a way to reduce it. I should probably stop by the mall to pick them up some dildos.\n\n-The girls reacted better to the dildos than I thought. I can tell them to play with themselves and spy on them via the spy cameras.")
        $ samSupLvl = 2
        $ cloverSupLvl = 2
        $ alexSupLvl = 2

        $ task5Stage = 5
        $ samSpySex = 2
        $ cloverSpySex = 2
        $ alexSpySex = 2
        pause 0.1
        show scene_darkening with d3
        show green g32 at ce
        show red at ri
        show yellow at le
        with d3
        y "Girls! I brought you all a gift!"
        s "......................"
        c r11 "Oh boy...."
        a y16 "Why are they shaped like penises?"
        y "..................."
        y "Alex, I'm revoking your speaking privileges."
        a y30 "....!"
        y "How about you give them a go!"
        c r37 "Er....."
        s g29 "Right now....?"
        a "........?!"
        c r35 "Let's just do it girls. It'll probably knock the nanobot control back quite a bit."
        c "And I'm sure [playerName] won't be there with us. Right [playerName]?"
        y "I... I won't?"
        s g31 "No you won't!"
        a y32 "....!"
        y "Alright fine...."
        s g33 "................."
        s "Well okay then..."
        c r23 "Let's take this baby for a spin!"
        a y2 ".........!"
        hide green
        hide red
        hide yellow
        with d3
        hide scene_darkening with d3
        pause 0.5
        show scene_fighting with d3
        "Inner Voice" "Dude, you gave in way too quick, you should have insisted on staying!"
        y "Spy cameras."
        "Inner Voice" "Oh right.{w} Niiiice~...."
        menu:
            "Spy on Sam" if True:
                jump samSex2
            "Spy on Clover" if True:
                jump cloverSex2
            "Spy on Alex" if True:
                jump alexSex2
        hide scene_fighting with d2
        jump base
    if task5Stage == 6:
        $ nanoLevelSam = 0
        $ nanoLevelClover = 0
        $ nanoLevelAlex = 0
        $ samMood = 10
        $ cloverMood = 10
        $ alexMood = 10
        $ task5Stage = 7
        $ greenOutfit = 0
        $ greenOutfitArms = 0
        $ redOutfit = 0
        $ redOutfitArms = 0
        $ yellowOutfit = 0
        $ yellowOutfitArms = 0
        $ greenUnder = 1
        $ redUnder = 1
        $ yellowUnder = 1
        pause 1.5
        show scene_darkening with d3
        show green g1 at ri
        show yellow at ce
        show red at le
        with d3
        pause 0.3
        y "Now girls. I've checked your nanobots levels and you should spend the evening masturbating again."
        s g15 "................"
        a "Okay..."
        c r11 "That's fine."
        hide green
        hide yellow
        hide red
        with d3
        "The girls return to their cells...."
        pause 1.0
        y ".................."
        hide scene_darkening
        show scene_fighting
        with d5
        pause 0.5
        "Inner Voice" "Spy cameras?"
        y "Hell yeah."
        hide scene_fighting
        show scene_darkening
        with d3
        "{b}*Beep*{/b}"
        a "Ah ah ah- ahh!! ♥"
        y "That's it, ride that cock!"
        "{b}*Beep*{/b}"
        c "Y-yes... ahh ahh mhmmm~...! ♥♥♥"
        y "How you like that you little slut?!"
        "{b}*Beep*{/b}"
        y "Take it you redhead piece of meat!"
        y "...."
        stop music fadeout 5.0
        "Sam's cell appears to be empty."
        y "Where is my redhead piece of meat?"
        s "{b}*Ahem*!{/b}"
        with hpunch
        y "ARGH!"
        show green g7 at ri with d2
        y "O-oh Sam~...! You didn't hear any of that did you....?"
        s g9 "{b}*Inhale*{/b}"
        y "Uh oh...."
        s g8 "{b}OF ALL THE LOWLIFE, GOOD FOR NOTHING, COWARDLY TRICKS THAT WE'VE ENCOUNTERED, YOU'RE THE WORST!{/b}"
        y "Erm... I can explain...!"
        $ redChest = 0
        $ redBottom = 0
        $ redUnder = 1
        $ yellowChest = 0
        $ yellowBottom = 0
        $ yellowUnder = 1.1
        $ yellowArms = 4
        show red r31 at le
        show yellow y29 at ce
        with d3
        a "What's going on?!"
        c "Are we under attack?!"
        s "This pervert was spying on us via the spy cameras!"
        c r30 "What?!"
        a y28 "Nooo my nudies!"
        "The three spies turn to look at you."
        y "................"
        y "I plead the 5th."
        c r31 "[playerName], if you want us to keep our nanobots suppressed, you can't then sneak off to spy on us!"
        s g9 "Yeah, that's a serious breach of privacy!"
        a y42 "I can't believe I showed my nudies to you... again!"
        s "That's it, [playerName]! You've betrayed our trust, now how do you expect us to trust you on missions?!{w} I'm going to bed!"
        a y38 "Me too!"
        c "......................."
        hide green with d3
        hide yellow with d3
        $ yellowArms = 1
        c "So you've been looking at us when we masturbate...?"
        c r12 "Not cool, [playerName]..."
        hide red with d3
        pause 1.0
        y "........................"
        hide scene_darkening
        show scene_fighting
        with d5
        "The girls caught you spying on them and their morale has dropped substantially."
        "When their morale is too low, they may reject working at places unless ordered to. They will also refuse to keep their nanobots suppressed."
        "A good way to improve your spies' mood, is by giving them something fun to do. Like a shopping spree at the mall or some time off at the beach."
        "Giving your spies certain items will also boost their happiness."
        pause 0.5
        y "I guess I ought to make it up to them..."
        $ task5Text = _("The nanobot control of the spies is getting stronger and I'm going to have to figure out a way to reduce it. I should probably stop by the mall to pick them up some dildos.\n\n-{color=#b5b5b5}I bought the girls some dildos. Let's see how they react.{/color}\n\n-I got caught spying on the girls and they're moody about it. I should try raising their morale before taking to them again.")
        "You decide to head to bed."
        jump nightCycle
    if task5Stage == 7:
        $ slutLevel = 2
        $ task5Stage = 8
        if greenChest == 0:
            $ greenChest = 1
            $ greenBottom = 1
        pause 0.4
        show scene_darkening with d3
        pause 0.2
        show green g39 at ri
        show red r39 at ce
        show yellow y39 at le
        with d3
        "................................"
        y "You guys still not talking to me?"
        s "{b}*Sighs*{/b} [playerName]....{w} We've been talking...."
        s g32 "You shouldn't have spied on us the way you did..."
        y "............"
        s g38 "But...{w} We also can't really blame you..."
        s "You got stuck in this mess just as we were and maybe we overreacted.{w} You've helped us a lot and we wouldn't have gotten this far without you..."
        y "I am forgiven?"
        c r13 "You are."
        play sound "audio/voice/clover/erm3.mp3"
        c r14 "Also we... err...{w} noticed our oxytocin levels after your little stunt and well... {w}They were actually really stable."
        y "Wait... so you're saying...?"
        s "That your voyeurism might have had a positive side effect."
        a y1 "Turns out you looking in on us gave us a boost of oxy-whatyamacallit. Preventing our nanobots from acting up!"
        c "[playerName]...."
        c r12 "As stupid as this is...{w} We talked it over and you don't have to spy on us again in the future... {w}You can stay in our cell to watch.... if you want."
        y "..............."
        menu:
            "Apologize (+karma)" if True:
                $ playerKarma += 5
                y "Well I wasn't exacty innocent, so I'm sorry too."
                y "Plus it all turned out for the best!"
                s "For you."
                y "Exactly!"
            "'Jackpot!'" if True:
                y "Hah, I get to look at naked girls getting off {i}'without'{/i} getting into trouble?!"
                c "Pretty much."
                s g14 "Though some professionality from your side would be appreciated!"
                y "Of course.{w} Show me your tits."
                play sound "audio/voice/what.mp3"
                s g28 "W-what?!"
                y "You said it was fine, right? Show me your tits then."
                s g30 "................."
                c r38 "We talked about this. Just get it over with."
                s g15 "Fine..."
                hide green with d2
                play sound "audio/sfx/cloth.mp3"
                $ greenChest = 0
                $ greenUnder = 0
                pause 1.5
                show green g33 at ri with d3
                pause 1.0
                s "..............."
                y "Not gonna lie.{w} I'm loving this."
                s g38 "You know, this is not what I meant when I said professional!"
            "Say something crazy" if True:
                y "Well I-....."
                stop music
                image crazy1 = "bgs/crazy1.jpg"
                show crazy1
                $ renpy.pause(3.0, hard='True')
                hide crazy1
                with hpunch
                play music "audio/music/nighttime.mp3" fadein 4.0
                y "Gah!!!"
                s g29 "[playerName]? What's wrong?"
                y "Er... nothing."
                y "(I think.)"
        c r1 "Anyways, I'm glad that's sorted. Now maybe we can focus on more important matters."
        hide green
        hide yellow
        hide red
        with d3
        hide scene_darkening
        with d3
        pause 0.6
        $ greenChest = 1
        $ greenUnder = 1
        call qCompleted from _call_qCompleted_3
        $ task5Text = _("The nanobot control of the spies is getting stronger and I'm going to have to figure out a way to reduce it. I should probably stop by the mall to pick them up some dildos.\n\n-{color=#b5b5b5}I bought the girls some diildos. Let's see how they react.{/color}\n\n{color=#b5b5b5}-I got caught spying on the girls and they're moody about it. I should try raising their morale before taking to them again.{/color}\n\n-Everything came up Millhouse! I can now stay and watch as the girls masturbate in their cells.")
        $ task5Name = _("Dingalingaling (COMPLETE)")
        pause 1.5
        "New restaurant options are available."
        jump base



default task6Stage = 0
default task6Name = _("A Foot in the Door")
default task6Text = ""

screen task6Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task6Text]"

label task6:
    if task6Stage == 0:
        $ task6Stage = 1
        $ spy1Status = 1
        $ greenDayJob = 1
        $ mapSpy1Selected = False
        $ task6Text = _("You sent Sam out to the Aces.")
        sM "The Aces got a heist planned for today, but I'm pretty sure we can pull it off with nobody getting hurt."
        y "Okay, stay on your guard."
        sM "{b}*Nods*{/b}"
        call qAccept from _call_qAccept_4
        "Sam heads off to the Aces."
        jump worldmap
    if task6Stage == 1:
        $ task6Stage = 2
        $ greenDayJob = 0
        $ coverCounter += 4
        $ spy1Status = 0
        $ task6Text = _("You sent Sam out to the Aces. She said it went fine, but she's acting a bit off. I should check up on her in her cell.")
        pause 0.5
        show scene_darkening with d3
        pause 0.5
        y "Welcome back, Sam. How did the heist go?"
        show green g37 at ri with d3
        s "Well.... Good I guess."
        y "But~...?"
        s g40 "But nothing. It went just fine."
        s "I even brought us back a cut of the profit."
        $ randMoney = 100
        $ cash += 100
        call missionRewardMoney from _call_missionRewardMoney_38
        pause 0.5
        y "Er... are you okay?"
        s g9 "Fine! Just fine, I'm heading to my cell!"
        hide green with d3
        pause 1.0
        y "........................"
        hide scene_darkening with d3
        jump nextReport
    if task6Stage == 2:
        $ task6Text = _("Sam was part of a robbery that went sour. She's going to spend the day at the mall with the Aces.")
        hide screen nanoLevelSam
        $ task6Stage = 3
        show scene_darkening with d3
        show green g4 at ri with d3
        if spyRedActive:
            show red r5:
                xalign 0.5 yalign 0.0 xzoom -1
            with d3
            c "..............."
        y "So... what's wrong?"
        s "........................."
        s "The heist didn't go exactly as planned..."
        s g15 "Someone got shot."
        y "Uh oh..."
        s "During the Heist, another gang showed up called The Glimmers and a firefight broke out."
        s "One of the Glimmers was hit and killed. They pulled back after that, but..."
        s g4 "I feel bad for having been part of it..."
        if spyRedActive:
            c "It's okay Sam... It's not your fault."
        y "Something like this was gonna happen sooner or later. Did you or any of the Aces get hurt?"
        s "{b}*Sighs*{/b} No we made it out unharmed..."
        s "Afterwards, they took me aside to talk things through with them. They weren't being snobbish or elitist for once."
        s "One of them even gave me the number of their therapist..."
        s "They were actually really nice..."
        y "It's not an easy thing to see somebody die."
        s "......................"
        if traitorRandom == 568513:
            s "If I never joined WOOHP this wouldn't have happened..."
        s g5 "The Aces offered to take me shopping. You know... to deal with things."
        y "I think that might be a good idea. Spend tomorrow at the mall, just to be sure."
        s "{b}*Nods*{/b}"
        hide green with d3
        if spyRedActive:
            c r43 "................."
            y "Worried about her?"
            c r37 "A little. Sam's a tough one and I'm sure she'll be fine, but even undercover we're suppose to be part of the good guys."
            c "Even if they're criminals, we're suppose to keep people safe. I think not being able to prevent that death bothers her."
            y "Let's keep an eye on her for now."
            hide red with d3
        hide scene_darkening
        with d3
        jump nightCycle
    if task6Stage == 3:
        $ task6Stage = 4
        $ cellSamChair = 2
        $ cellSamDesk = 2
        $ cellSamLaptop = 2
        $ cellSamPainting = 2
        show scene_darkening with d3
        show green g1 at ri with d3
        y "Welcome back, [greenName]."
        s "Hey [playerName]."
        y "Feeling better?"
        s g2 "Yeah, a little bit. Normally it's Clover who loves going on shopping sprees, but this time I really went all out."
        s "I bought a laptop and some hardware to go with it."
        y "Uh huh..."
        s g1 "Aswell as a desk and a chair."
        y "I see... {w}Anything else?"
        play sound "audio/voice/yeah2.mp3"
        s "Yeah! This painting that I really like...!"
        y "....................."
        y "Okay... {w} How much?"
        s g41 "Huh?"
        y "Give it to me straight, I can handle it. How much was all that?"
        s "Nothing."
        y "Come on, I've been mentally preparing myself for this all day. Just lay it on me!"
        s g1 "I didn't have to pay."
        y "Don't keep me in suspense any longer! My wallet is crying out in agony! Just give it to me!"
        s g10 "[playerName]..."
        s g1 "The Aces paid for it all."
        y "................."
        y "What?"
        s "They paid for every last single thing."
        y "........................"
        y "A gang of violent gangsters brought you on a free shopping spree...?"
        s "Y-yeah... They wouldn't take no for an answer."
        s g13 "I was surprised too. They were really cool about it."
        s "We went into all the expensive shops that I normally can't go into. At no point did they laugh or make fun of my lack of money. They said I was one of theirs now."
        y "That's the benefit of having rich friends I guess..."
        y "Just remember they're not really your friends. They're hardcore villains and gangsters."
        s g11 "I know. Of course, I know that."
        s g2 "But it felt nice to be accepted by the cool kids for once. Instead of being bullied by them."
        hide green with d3
        hide scene_darkening with d3
        pause 0.4
        call qUpdated from _call_qUpdated_7
        pause 0.4
        "New cell decorations are available for Sam."
        "New shopping options are available for Sam at the mall."
        $ task6Text = _("Sam's reputation with the Aces is increasing. Keep building your reputation to get closer to Melody.")
        jump nextReport


    if task6Stage == 4:
        if spyYellowActive == False:
            y "We should really focus on finding a way to free Alex before we do this."
            jump worldmap
        $ task6Stage = 5
        $ spy1Status = 10
        $ mapSpy1Selected = False
        scene bgBar with d3
        pause 0.4
        show scene_darkening with d3
        show green g1 at ri with d3
        y "Okay, [samNick]. Time to go undercover with the Aces again."
        s "Oh.. okay!"
        y "Well you sound excited."
        s g2 "Yeah, they're shooting a music video and told me I could be in it!"
        y "A music video? I never expected you to be interested in something like that."
        s "Heh~... well I wasn't before..."
        s "But they said they couldn't do without me and said I'd be perfect."
        y "High praise indeed."
        s g1 "Yeah that's what I thought!"
        s "I never thought I'd be in a music video!"
        y "Well have fun. Just don't get too excited. Remember that you're suppose to gather intel."
        s "Yeah yeah, don't worry."
        hide green
        hide scene_darkening
        with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap

    if task6Stage == 5:
        $ task6Stage = 6
        call undressSam from _call_undressSam_5
        $ greenUnder = 5
        show scene_darkening with d3
        s "I'm back..."
        y "Welcome back S-..."
        show green g19 at ri with d3
        y "!!!"
        y "You've got my undivided attention."
        s "Heh... Heh~...."
        s g38 "{b}*Ahem*{/b} So we shot the music video today..."
        y "In a swimsuit."
        s g35 "In a swimsuit..."
        s g42 "Okay, so I didn't know this, but all the girls had to wear swimsuits for the shoot."
        y "Uhhuh..."
        s g28 "And... I mean...! Why not? It was really hot out today."
        y "I see..."
        s "And... and there was a pool!{w} I mean we didn't use it, but there was one!"
        y "Riveting."
        s g42 "And... and well! Well...{w} At least they didn't film my butt...!"
        s "{size=-10}I think...{/size}"
        y "Okay... I think I see what's going on here."
        y "You didn't expect to be used as a sex object. {w}Now you're getting flustered and pretend to be shocked and outraged because it clashes with your sense of morality."
        s g11 "........................."
        s "Well...{w} Not exactly..."
        y "...?"
        s "The truth is..."
        hide green
        $ greenBlush = 1
        show green g19 at ri with d2
        s "It was actually kinda fun..."
        y "It was...?"
        s "They were all so nice to me! They noticed I wasn't completely comfortable and they encourages me and said I was talented."
        s "And then the other girls said it wasn't such a big deal and they helped me practise and.. and...!"
        s g15 "................."
        s "And I could keep the bathing suit."
        s g14 "They're really not so bad once you get to know them..."
        y "Sam, they're violent gangsters."
        s "I know, but..."
        if traitorRandom == 568513:
            s "It's just that...{w} They're a lot more fun to hang out with than going on missions for WOOHP all the time..."
        s g15 "....................."
        s "They even gave me this for my work..."
        $ cash += 300
        $ randMoney = 300
        call missionRewardMoney from _call_missionRewardMoney_68
        s g1 "So... today wasn't that bad. Even if I had to wear a swimsuit."
        s "It might've even reduced my nanobot levels a bit."
        y "Hm... that sounds like a pretty succesful day..."
        y "Just don't get in too deep, okay? Remember that these people are not really your friends."
        s "I know, I know."
        hide green
        hide scene_darkening
        with d3
        $ nanoLevelSam -= 5
        $ greenBlush = 0
        $ spy1Status = 0
        $ under5Sam = True
        $ acesRank = 3
        $ acesRep = 0
        "New clothing options for Sam are available at the mall."
        jump nextReport

    if task6Stage == 6:
        if spyYellowActive == False:
            y "We should really focus on finding a way to free Alex before we do this."
            jump worldmap
        $ task6Stage = 7
        $ spy1Status = 10
        $ mapSpy1Selected = False
        scene bgBar with fade
        show scene_darkening with d3
        y "Okay, time to g-..."
        s "{b}*Eeeeee*{/b}!!!"
        y "What the....?"
        show green g1 at ri with d3
        s "Great news, [playerName]! I've been invited back to the Aces castle!"
        y "That {i}'is'{/i} great news! Maybe you'll be able to get close to the next Lieutenant then."
        s g29 "Oh! Right, of course!{w} The Lieutenant."
        y "..................."
        y "Well have fun and be careful out there."
        "Sam nods and heads off."
        hide green with d3
        pause 1.5
        show red r35 at ri with d3
        c "Where is she going?"
        y "Spain."
        c "Spain? On a mission?"
        y "No she got a party invitation."
        c r18 "Again? That girl has been spending a lot of time with the Aces lately."
        y "My thoughts exactly. Do you think we should worry?"
        c r12 "Hmm... Sam normally has her feet planted firmly in reality. I think she'll be fine... {w}I hope."
        c "Just to be sure we should keep an eye on her. She's been speaking much too highly about the Aces lately."
        y "Noted."
        hide red with d3
        hide scene_darkening with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap

    if task6Stage == 7:
        $ task6Stage = 8
        $ spy1Status = 10
        y "Let's see how Sam is getting along..."
        "{b}*Beep* *Beep* *Beep*{/b}"
        call undressSam from _call_undressSam_6
        $ greenUnder = 1.1
        scene bgCastle
        with fade
        show green g2 at ri
        show scene_camera
        with d3
        y "!!!"
        s g1 "Oh, [playerName]! Good to see you! I was just about to..."
        y "About to...?"
        s g19 "W-well...{w} I was dared to show my breasts and..."
        y "And you accepted the dare?"
        s "Heh... heh..."
        s "The other girls are doing it too..."
        s g29 "I already said I'd do it. I can't back out now! They expect me back any second now."
        menu:
            "Go show off your tits" if True:
                $ slutPublic += 1
                "Sam smiles and nods before going through a door."
                show black with fade
                hide green
                hide scene_camera
                $ greenArms = 5
                show green g1 at ce
                show scene_camera
                hide black
                with fade
                "Aces Gangster" "Woooo! Go Sam!"
                "Aces Gangster" "You go girl! Nice tiiiiiiits!"
                $ greenBlush = 1
                s g2 "Heh heh~..."
                "Aces Gangster" "I knew inviting you to this party was a good idea!"
                "Aces Gangster" "Jiggle them a bit!"
                s g1 "L-like this...?"
                "Sam awkwardly jiggles her breasts from side to side."
                "You hear a loud cheering over the phone."
                "Aces Gangster" "YOU'RE THE SEXIEST REDHEAD IN THE ACES!"
                $ randRep = 1
                $ acesRep += 1
                call missionRewardRep from _call_missionRewardRep_17
                pause 0.4
                y "....?"
                menu:
                    "Okay that's enough" if True:
                        s g1 "Hehe, really? Cause I'm willing to go furth-..."
                        y "Sam! I didn't train you to become a slut!"
                        s g29 "But... you always call me a slut when we... {w}y'know..."
                        y "You're a slut. But you're my slut."
                        s g18 "That doesn't make any sense."
                        y "I know it doesn't. Don't you dare take off anymore clothing! And when you're done there, head back to the US."
                        s g11 "Fine~..."
                        show black with fade
                        scene bgBase
                        with fade
                        $ greenArms = 1
                        jump base
                    "Give them a show" if slutLevel >= 3:
                        $ slutPublic += 1
                        play sound "audio/voice/what.mp3"
                        s g29 "A show...? W-what do you mean?!"
                        y "Do some sexy dance moves. Strike some poses."
                        s "But what if they want to touch me...?"
                        y "Do you want them to touch you?"
                        s g28 "No!"
                        s g11 ".........................."
                        s g48 "I mean...{w}{size=-8}maybe a little~....{/size}"
                        y "There you go. Have fun."
                        "The blushing spy nods and begins to put on a preformance."
                        show black with fade
                        hide green
                        hide scene_camera
                        "The camera cuts out..."
                        $ randRep = 1
                        $ acesRep += 1
                        call missionRewardRep from _call_missionRewardRep_18
                        scene bgBase with fade
                        jump base
                    "Time to suck some dick!" if slutLevel >= 4:
                        $ slutPublic += 1
                        play sound "audio/voice/what.mp3"
                        s g28 "W-what..?!"
                        y "Come on, this is the perfect opportunity! If you want to raise your reputation with the gang, you gotta go all out."
                        s g29 "B-but..! There's so many people here~..."
                        y "Encourage the other girls to help you out."
                        s "B-but..!"
                        y "Imagine how popular you'll be!"
                        s "I.. I guess so..."
                        s g48 "{b}*Gulp*{/b} O-okay... let's do it...!"
                        hide green with d3
                        s "Time to kick this party up a notch!"
                        "You hear a loud cheering crowd."
                        hide scene_camera
                        show black
                        with fade
                        $ greenBottom = 0
                        "{b}*Suck* *Suck* *Slobber*{/b}"
                        $ randRep = 2
                        $ greenArms = 1
                        $ acesRep += 2
                        call missionRewardRep from _call_missionRewardRep_19
                        hide black
                        $ greenCum = 1
                        show green g25 at ce
                        show scene_camera
                        with fade
                        pause
                        y "Okay, wrap it up and head back to the US."
                        "The dazed spy nods and staggers offscreen."
                        show black with fade
                        hide scene_camera
                        hide green
                        $ greenCum = 0
                        scene bgBase
                        with fade
                        $ greenArms = 1
                        jump base
            "Don't show off your tits" if True:
                y "What happened to the prude I've come to know and love?"
                s "It's... it's just my tit-...{w} my breasts. I don't know... Everyone just seemed so excited and I didn't want to be left out.."
                y "That's the peer-pressure talking! Don't do it my innocent pure angel!"
                s "I'm pretty sure I lost that innocense when you first told me to take off my top..."
                y "No matter. You tell them {b}'no'{/b}."
                s "Fine..."
                hide green with d3
                "You see Sam puttng her top back on and walk through a door, followed by the dissapointed cries of gangsters."
                show black with fade
                hide scene_camera
                scene bgBase
                with fade
                $ greenArms = 1
                jump base

    if task6Stage == 8:
        $ greenArms = 1
        $ samMood += 10
        $ task6Stage = 9
        $ spy1Status = 0
        $ spy2Status = 0
        $ spy3Status = 0
        $ redDayJob = 0
        $ yellowDayJob = 0
        pause 0.5
        show scene_darkening with d3
        show green g1 at ri with d3
        s "I'm back."
        y "Welcome back Sam. Had fun in Europe?"
        s g2 "Yes~..."
        y "Okay. What's your report?"
        s g29 "Report?{w} Oh er... I was so busy hanging out with the Aces that I didn't really{w} er..."
        y "You didn't actual gather any intel..."
        s g15 "I'm sorry, [playerName]..."
        s g14 "My mind was elsewhere. We went to do so many cool things that I sorta forgot..."
        s g1 "Like... we went skydiving and they all got super scared! Of course I do that like... every other week, so I didn't think it was a big deal."
        s "And they all thought I was a badass!"
        s "I also dragged some of them along to a museum to teach them about historical Spanish art! They were reluctant at first, but were blown away about how much I knew!"
        s g13 "At the end of the day, they all wanted to talk to me and be my friend! And... and...!"
        y "Calm down there [samNick]. You know these are bad people, right?"
        s g2 "I mean sure, but they're not all bad~..."
        y "The Aces have continued terrorizing Beverly Hills when you were away. You seem to forget how dangerous these people actually are."
        s g38 "No... I didn't forget..."
        menu:
            "Warn Sam" if True:
                $ samMood -= 1
                y "Sam, you're going too deep undercover. You're gonna end up as one of these gangsters if you're not careful."
                s g16 "What are you saying, [playerName]?! I know what I'm doing! I'm still working on re-taking this city, you know!"
                s g31 "If anything I'd say I've gone far and beyond. How could you even question me like that?!"
                c "He's not the only one."
                show red r54:
                    xalign 0.5 yalign 0.0 xzoom -1
                with d3
                pause 0.2
                show yellow y19 at le with d3
                s g56 "Girls...?"
                c "You're getting in way too deep, Sam. Stop pretending these guys are your friends."
                a "Yeah! {w}We are your friends..."
                s g30 "!!!"
                s "Are you...! {w}Are you jealous?!"
                c "That's not what we're saying, Sam."
                s g53 "You are, aren't you?!"
                s "Just because I'm good at my job doesn't mean I'm turning into a gangster!"
                s "So what if I enjoy going undercover with the Aces? At least they're not criticizing me all the time!"
                y "Sam..."
                s g40 "I'm going to unpack. Good night!"
                show green:
                    linear 0.3 xalign 1.7
                "Sam stormed off."
                y ".........................."
                y "Well that could be a problem."
                a y5 "I've never seen her like this..."
                c r11 "Yeah, she's definitely acting odd."
                y "Let's leave her be for now."
                "The girls nod and return back to their cells."
                hide red
                hide yellow
                with d3
                hide scene_darkening
                with d3
                jump nextReport
            "Let her off the hook" if True:
                y "Well I can't really blame you... It's a private castle after all."
                s g1 "Exactly! And we played all kinds of games!"
                y "I could see that."
                $ greenBlush = 1
                s g2 "Oh right~... heh heh~..."
                s g1 "But it was fun. I felt really accepted."
                y "Don't get too friendly with them. Remember they're gangsters."
                $ greenBlush = 0
                s g2 "Yeah I know, but they're the least bad of all the gangs here in town."
                y "............................"
                s "Okay I'm going to unpack. If you need me, I'll be in my cell."
                "Sam picks up her bags and heads out of the room."
                hide green with d3
                pause 1.0
                c r18 "Was that Sam just now?"
                show red r52:
                    xalign 0.5 yalign 0.0 xzoom -1
                with d3
                pause 0.2
                show yellow y19 at le with d3
                y "Yeah she just returned."
                c r11 ".........................."
                y "Something on your mind?"
                c "We think she's getting a little too deep."
                y "Too deep?"
                a y29 "Too deep undercover. We don't want her turning into a gangster..."
                y "You think there is a risk of that?"
                c r12 "I never expected it from Sam, but it's possible."
                c "Let's keep an eye on her for now."
                y "Agreed."
                hide red
                hide yellow
                with d3
                hide scene_darkening with d3
                jump base

    if task6Stage == 9:
        $ task6Stage = 10
        $ spy1Status = 10
        $ mapSpy1Selected = False
        pause 0.5
        scene bgBar with fade
        show scene_darkening with d3
        show green g38 at ri with d3
        s "There was this gem called the Sobhuza Diamond that was stolen from a museum a few months back."
        s "Turns out, it's with the Aces now. They're hosting a party tonight where it will be present."
        s g1 "I know you guys have been worried about me going too deep undercover. So let me get that diamond back to proof that I'm still on your side."
        y "That sounds like a good idea. Okay [samNick], give it your all."
        hide green with d3
        "Sam nods and leaves for the Aces."
        hide scene_darkening with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap

    if task6Stage == 10:
        $ task6Stage = 11
        $ spy1Status = 10
        pause 0.7
        "{b}*Beep* *Beep* *Beep*{/b}"
        y "That must be Sam."
        scene bgFashion
        show green g34 at le
        show scene_camera
        with d3
        pause 0.3
        s "Sam here."
        y "Sam! Where are you?"
        s "I'm at WOOHP HQ. The Aces were invited to host the party here."
        y "That should be a good opperatunity to gather some intel!{w} What about the gemstone?"
        s g3 "They just brought it out. Security is pretty tight, but I think I can steal i-..."
        "???" "Can I have your attention please..."
        hide green with d3
        mel "Welcome all to this auspicious occasion where we celebrate WOOHP and their collaboration with the Aces."
        mel "They've been guarding our castle in Spain, been helping us out here in Beverly Hills and now have even invited us to come to their headquarters."
        mel "We wouldn't be where we are now without them."
        "You hear the crowd cheering."
        mel "That's why it came as a surprise to hear that WOOHP agents attacked us during Landgrabs..."
        mel "Care to shed some light on that, Mr. Scam?"
        hide scene_camera
        show timModel at ce
        show scene_camera
        with d3
        tim "..................."
        mel "Perhaps it's because you're afraid that we're getting too powerful...?{w} Maybe even challenge your organisation?"
        mel "Or maybe you don't have as tight a hold on your agents as you thought..."
        tim "I assure you Melody that we have everything under control."
        mel "Is that so? A little birdy told me there might even be a traitor amongst us right now..."
        y "!!!"
        y "Sam, can you hear me? You've been found out. Get out there!"
        hide tim
        hide scene_camera
        scene black
        pause 0.6
        y "!!!"
        "The lights went out!"
        pause 0.6
        sM "Psst... [playerName]..?"
        y "Sam, are you okay?"
        sM "Yeah, but this wasn't my doing! I think there's another thief here."
        scene bgFashion
        show scene_camera
        with d3
        pause 0.5
        "The lights came back on."
        "Aces Gangster" "The diamond is gone!"
        mel "I knew it! WOOHP is sabotaging us! Get that diamond back!"
        hide scene_camera
        show agentModel3 at le
        show agentModel4 at ri
        show timModel at ce
        show scene_camera
        with d2
        tim "Not so fast Melody. We had nothing to do with this. Your gangsters don't have clearance to the rest of the facility."
        mel "What?! {w}I'll show you what I think of your 'clearance'...!"
        hide agentModel3
        hide agentModel4
        hide timModel
        with d3
        pause 0.5
        sM "I think a fight is about to break out over here."
        sM "I'm going to sneak after the jewel thief. I bet I can still catch them."
        y "Good thinking. Go after them and report back to the base."
        hide timModel
        hide scene_camera
        show black
        with fade
        pause 0.5
        hide black
        scene bgBase
        with fade
        jump base

    if task6Stage == 11:
        $ task6Stage = 12
        $ spy1Status = 0
        pause 0.6
        show scene_darkening with d3
        show green g15 at ce with d3
        y "Sam you're back!"
        s "Er... yeah...{w} without the Sobhuza diamond..."
        y "What happened...?"
        s g11 "Well I found the thief who was making a break for the exit."
        s "I managed to grab him, but Melody caught me."
        y "............."
        s g12 "I had no choice, but to return the diamond to her to uphold my cover."
        y "I bet the Aces liked that."
        s g1 "Yeah I sorta... been... promoted."
        s "The Aces were so happy with me that they threw a party in my honor which lasted all of today."
        s g28 "We got to go to a yacht!"
        y "Okay...?"
        s "We flew paramotors, went diving and partied in a pool they had on the deck!"
        s g1 "They were all so happy with me! I've made so many new friends!"
        s "I talked about the importance of charity and they agreed!{w} I know we think of them as bad guys, but we need to look at them different."
        s "They're good kids with too much money. They only need a little guidance on what to do with that money and they could do some real good in the world!"
        y "Yeah that's what I want. A bunch of coke-head fratboys ruling the world."
        s g18 "Everyone who's running this country 'now' used to, or still is a coke-head fratboy."
        y "........................"
        y "Touché."
        y "Did you at least get some intel?"
        s g29 "Oh!{w} Right...{w} intel... heh heh~..."
        y "......................."
        s "[playerName]... listen."
        y "Sam~...."
        s "No just listen...! Here's what I'm thinking."
        s g1 "Maybe we should spend less time trying to take the Aces down and focus on the other gangs in town."
        s "It would make sense! Taking down all gangs at the same time just leaves us divided. Better to focus our strength!"
        y "Sam~...!"
        s g14 "I bet that by the time we take down the other gangs, the Aces will have seen their flaws and disband themselves!"
        s "They're just dumb kids who made some mistakes! They need love and guidance, not a cold lonely prison cell!"
        s "And-...!"
        with hpunch
        y "SAM!"
        menu:
            "Discipline her" if True:
                y "Have you gone completely crazy?! The Aces are gangsters! The city is burning because of them!"
                s g29 "But...!"
                y "And you've gone way too deep undercover. You're not going there anymore!"
                s g28 "No...!"
            "Talk things over" if True:
                y "Sam...{w} We've told you before... The Aces are dangerous. They're drug dealers, violent robbers and more."
                s g29 "But...!"
                y "You've gone way too deep undercover. Remember that we're working to liberate the city. We can't do that with the Aces running around it."
                y g15 "But... you don't understand..."
        s g15 "The... the Aces..."
        s "They're...."
        s "They..."
        s "{b}*Sniff*{/b} They think I'm cool... They accept me... and they want to be my friend..."
        y "..................."
        s g14 "Do you have any idea how much I've been bullied in my life...? I was never invited to parties...{w} always seen as the weird kid who only studies....!"
        s "Before I met Alex and Clover, I didn't even have any friends! I thought I didn't need friends! I decided to fully commit to WOOHP and being a spy and now...! And now...!"
        s "Now I know what it's like to feel accepted... The people who used to bully me now listen to me and come to me for advice..."
        s g5 "I'm no longer the weirdo. No longer the freak they make fun of...."
        y "................."
        y "Sam... We all make choices in life. They chose to do crime and need to take responsibilty for that."
        s g14 "But...!"
        y "And you chose to be a spy. Now you need to take responsibility for that too."
        s g15 "........................."
        y "This city is relying on you. If you can't be there for them, then you have no business being a spy."
        s "......................."
        show red r57 at ri
        show yellow y57 at le
        with d3
        c "Sam...."
        s "...................."
        s g14 "{b}*Sniff*{/b} Melody trusts me now..."
        s "We can visit the castle and take her in..."
        y "............................"
        s "I'm sorry...."
        a "Sammy..."
        c "Don't be sorry, Sam. We understand."
        s "I'm... {w}I'm going to my cell..."
        hide green with d5
        pause 0.4
        a "........................."
        c "........................."
        y "We should've done something sooner..."
        c r12 "We tried, I don't think this was something we could've prevented..."
        c r34 "There is still a mission that needs completing.{w} Send us to the castle whenever and we will take Melody down."
        y "And Sam?"
        c r37 "We'll talk to her... She knows it's the right thing to do...{w} It's just difficult for her right now."
        hide red
        hide yellow
        with d5
        "Alex and Clover head of to their cells."
        "Sam has won Melody's trust and we can now travel to the castle to take her in."
        "New clothing options are available for Sam at the mall."
        $ task6Text = _("Sam was part of a robbery that went sour. She's going to spend the day at the mall with the Aces.\n\nHaving spend some time with the Aces, Sam has grown closer to their second Lieutenant.\n\n-Plan a mission to the Castle and capture Melody.")
        $ specialMelodyStatus = 1
        hide scene_darkening with d3
        jump base

    if task6Stage == 12:

        $ _skipping = True
        $ task6Stage = 13
        hide interactScreen
        scene black
        hide spyCombat2
        hide obstMaggie
        hide screen equipmentMenu
        with fade
        pause 1.0
        play sound "audio/sfx/running1.mp3"
        pause 1.5
        $ randomExit = 0
        show globalImageCastle:
            zoom 0.25
        with fade
        pause 1.0
        show obstMelody:
            xalign 0.62 yalign 0.49 rotate 3 zoom 0.21
        cM "We got her now!"
        mel ".............."
        mel "Sam..."
        sM ".................."
        mel "How could you...?"
        cM "Don't listen to her, Sam. You did the right thing."
        aM "Yeah! You're coming with us!"
        mel "I'd like to see you tr-..."
        play sound "audio/sfx/punch1.mp3"
        hide globalImageCastle
        hide obstMelody
        scene black
        with hpunch
        "Melody gets instantly overpowered by the three spies."
        pause 1.0
        $ loot1 += 1
        $ loot2 += 1
        $ loot3 += 1
        $ loot5 += 1
        $ prisonersNew = True
        jump missionComplete

    if task6Stage == 13:
        $ task6Name = "A Foot in the Door (Complete)"
        $ task6Stage = 14
        $ melodySocial = 1
        $ specialMelodyBounty = True
        $ specialMelodyStatus = 3
        pause 0.5
        show scene_darkening with d3
        pause 0.4
        y "Well well well, if it isn't Melody G. So nice of you to joi-..."
        y ".............."
        y "Ah let's just skip the dialogue and go straight to the fucking."
        mel "W-what?!"
        y "Yeah you know. Break you out of your nanobot trance, give us the intel we need."
        y "It's sort of par for the course by this point."
        mel "If you lay even a finger on me I swear I'll bite it off."
        y "...........?"
        y "Melody.... your eyes aren't red..."
        mel "Of course they're not. I'm not one of those brainwashed zombies. I don't have nanobots in me!"
        y "Oh...."
        y "Well this is awkward..."
        y "Then why are you out there working for the mastermind?"
        mel "Payback.{w} My grandmother is in jail because of your spies, you know."
        y "Actually... I don't know. Let me get my spies."
        "You call your girls and in a moment they arrive."
        show yellow y34 at le
        show red r12:
            xalign 0.5 yalign 0.0 xzoom -1
        with d3
        c "[playerName] before you offer, we're not going to watch you have sex with her!"
        a "Yeah you voyeuristic weirdo!"
        y "First of all...{w} ouch. That hurt my feelings.{w} Shame on you Alex."
        a y30 "!!!"
        y "Secondly, she's not being controlled by nanobots, so there's no point is sleeping with her."
        c r29 "She's not...?"
        mel "No.. I'm not. Hello Clover... Alex..."
        mel "Your redheaded traitorous friend not joining you?"
        a y32 "You leave Sammie out of this!"
        c r31 "She went through a lot busting your ass."
        mel "...................."
        mel "Question. Do you two remember my grandmother, Helga von Guggen?"
        c "She's hard to forget..."
        a y29 "She shrunk our clothes! It was very embarrassing!"
        c r12 "Not to mention all the other times she tried to get rid of us."
        c "So what? You want revenge for locking up your nana?"
        mel "Yes!"
        mel "................."
        mel "At least at first..."
        y "At first? Not anymore?"
        mel "................."
        mel "I've said enough. You're not getting anything out of me."
        menu:
            "Be friendly" if True:
                y "What's your theme?"
                mel "My... huh?"
                y "You know. Maggie T. was interior design, you must have a theme as well."
                mel "Fashion..?"
                y "Fashion..."
                y "I know nothing of fashing. Clover you're up!"
                c r18 "Up to do what exactly...?"
                y "Appeal to her theme! Make her our friend. Before you know it, she'll tell us everything!"
            "Be mean" if True:
                y "Okay... I didn't want to do this..."
                mel "....................."
                y "You're really leaving me no other choice..."
                mel "...................."
                y "I'm gonna say it....!"
                y "Your hair color makes you look like an old woman."
                mel "........"
            "Say something insane" if True:
                y "Let's see how willing to talk you are....{w} WITHOUT A HEAD!"
                a y30 "!!!"
                c r30 "!!!"
                y "Not very talkative I imagine... {w}due to the 'not having a head' part."
                c "[playerName]...."
        mel "Is he crazy....?"
        c r35 "We're still not entirely sure on that ourselves..."
        y "Would a crazy person do this?!"
        "You begin doing karate chops in the air."
        a y30 "H-hey...! [playerName]! Watch where you're swinging!"
        c r31 "Careful, you're going to end up hurting yours-...."
        play sound "audio/sfx/spank1.mp3"
        with hpunch
        a y28 "!!!"
        c r28 "!!!"
        mel "!!!"
        "You accidentally slapped Melody across the face!"
        y "I'm sorry! I got carried away trying to intimidate you...!"
        mel "......."
        mel "It's fine...."
        a y8 "[playerName]! We don't hurt our prisoners!"
        c r38 "That's not the WOOHP way!"
        y "I'm sorry! I'm sorry, it was an acci-..."
        "Suddenly Melody lets out a mocking laugh."
        mel "{i}Not the WOOHP way?{/i}"
        mel "You stupid girl! Do you have any idea what WOOHP does with its prisoners after you capture them?!"
        a y29 "W-what...?"
        c r32 "Don't listen to her, Alex. She's trying to trick us."
        mel "Oooh, the mighty WOOHP! So righteous! Saving the world from tyranny!"
        mel "Have you {i}'any'{/i} idea what my grandmother went through?!"
        mel "Why she kept wanting to take revenge on your organization?!"
        mel "WOOHP is ten times as tyrannical as the {i}'villains'{/i} it pretends to save the world from!"
        c r31 "WOOHP is keeping the world safe from people like you!"
        a y29 "Yeah!"
        mel "I'm preaching to the choir... {w}You girls are as thick as grandmother descripted you."
        mel "Do with me as you please. You're not getting a word out of me."
        "The atmosphere in the room is tense as the women defiantly glare at each other."
        y ".................."
        y "Alex...{w} Clover..."
        y "Please go get Sam."
        c r8 "We can't bring her here! You saw what the Aces did to her!"
        y "Please go get her and then leave the cell."
        a y4 "But [playerName]~....!"
        y "Now, please."
        c r37 "..........................."
        c "I don't know what you're planning [playerName], but you better have a good reason for it..."
        hide red with d3
        hide yellow with d3
        pause 0.5
        mel ".................................."
        pause 0.7
        "A little while later, Sam enters the cell."
        show green g5 at le with d3
        pause 0.4
        mel "If it isn't the traitor herself..."
        s "............................."
        mel "I really thought you changed..."
        mel "The moment you showed up at our doorstep I knew I had to keep an eye on you..."
        mel "I would've killed you right there and then...{w} If it wasn't for Tim."
        y "Tim? Tim Scam?"
        mel "......................."
        mel "You sure fooled everyone, Sam..."
        mel "Going on missions with us... going to our parties... planning heists together..."
        mel "Even I began to trust you..."
        s "............................"
        mel "Lot of good that did me..."
        s g45 "You had to be stopped Melody...{w} Look what you did to the city..."
        mel "I'm not proud of it.... But if that's what it took to bring down WOOHP, it was worth it."
        s g31 "Why would you want to bring down WOOHP?! Just because we imprisoned your grandmother?! She was evil and needed to be stopped!"
        mel "...................."
        mel "Do you really not know or are you feigning ignorance?"
        s g5 ".........................................."
        mel "WOOHP isn't the good, kind hearted organization you think it is. To think you're still a part of it..."
        mel "We trusted you, Sam... We really did..."
        mel "To see the look on Jerry Lewis' face when he found out his favorite spies helped overthrow his organization. Revenge would've been so sweet..."
        mel "Of course that dream is far gone now...{w} The Aces are in shambles. Their Lieutenants gone, their relation with the Mastermind ruined, their topman turning out to be a undercover spy."
        s g4 "I... I am so-..."
        mel "Ask your questions... {w}There's no point in hiding things anymore and I'm tired of being the villain."
        mel "I'll cooperate..."
        y ".............................."
        hide green
        hide scene_darkening
        with d3
        "Melody gives you all the information she has."
        $ randIntel = 400
        $ intel += 400
        call missionRewardInt from _call_missionRewardInt_31
        pause 1.0
        show scene_darkening with d3
        show green g5 at le with d3
        show scene_darkening with d3
        s "Thank you Melody..."
        mel "Just... leave me alone."
        hide green
        hide scene_darkening
        with d3
        pause 0.8
        "Computer" "Melody G. status: Captured.{w} Allocating resources..."
        $ randMoney = 1200
        $ cash += 1200
        call missionRewardMoney from _call_missionRewardMoney_76
        scene black with fade
        pause 1.0
        scene bgBase with fade
        show scene_darkening with d3
        show red r57 at ri with d3
        show yellow y56 at ce with d3
        show green g4 at le with d3
        pause 0.6
        a "Sammie...?"
        c "Are you okay, Sam?"
        s "Yeah..."
        y "It's been a long day. I vote that we get pizza and call it a night."
        "The girls nod is agreement."
        hide green
        hide yellow
        hide red
        with d3
        hide scene_darkening
        with d3
        pause 0.7
        call qCompleted from _call_qCompleted_4
        $ acesRank = 4
        $ acesRep = 0
        "New clothing options are available for Sam at the mall."
        jump nightCycle



default task7Stage = 0
default task7Name = ""
default task7Text = ""
image whiteBoard = "models/jerry/whiteBoard.png"

screen task7Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task7Text]"

label task7:
    if task7Stage == 1:
        $ HQPrison = True
        $ task7Stage = 2
        scene bgPrison with fade
        pause 0.5
        show scene_darkening with d3
        pause 0.3
        show red r35 at ri
        show green g29 at ce
        if spyYellowActive:
            show yellow y1 at le
        with d3
        s "This place is actually pretty big. This must be where all of WOOHP's crazy inmates were being held."
        y "And now they're roaming Beverly Hills."
        s g19 "Yeah..."
        if spyYellowActive:
            a y29 "I bet Tim was being held here too~...."
        c r22 "Maybe you can find Tim's diary here, Sam. Maybe a hidden letter where he confesses his love to you~..."
        s g9 "TIM AND I ARE NOT A COUPLE!"
        c r24 "Just think about all the lonely nights he's had here, thinking of you~....!"
        if spyYellowActive:
            a y42 "{i}'Oh Sam, my one true love. We were made for each other, but I have chosen the path of evil and our forbidden love must never be!'{/i}"
        y "Hah! Better be careful not to find any crusty socks around here!"
        c r10 "....................."
        if spyYellowActive:
            a y10 "....................."
        $ greenBlush = 1
        s g30 "....................."
        y "What?"
        c r8 "Way to take it too far, [playerName]."
        if spyYellowActive:
            a y42 "Ew, ew, ew! That's an image I didn't want in my mind!"
        hide red
        hide yellow
        with d3
        y "Er... Sam?"
        s g40 "Err... heh heh~..."
        $ greenBlush = 0
        s "{b}*Ahem*{/b} there's one other thing I wanted to discuss with you."
        s "I found this terminal in the cell block. It's an automated WOOHP Bounty board. When criminals escape and are brought back, funds are made available."
        s g1 "Here I'll show you."
        "{b}*Bleep*{/b}"
        "Computer" "Booting up WOOHP Bounty Board..."
        "Computer" "Target: Maggie T.\nStatus: Captured."
        "Computer" "Transferring funds..."
        $ cash += 500
        $ randMoney = 500
        call missionRewardMoney from _call_missionRewardMoney_66
        y "!!!"
        y "Nice!"
        pause 0.4
        show scene_fighting with d10
        "Bringing in gangleaders will not only help you liberate Beverly Hills, it will also offer you bounty rewards. Be sure to check in on the prisons to claim your bounty whenever you capture a new gangleader."
        hide scene_fighting with d5
        y "I wonder how much we'll get if we bring in your boyfriend."
        $ greenBlush = 1
        s g8 "He's not my boyfriend!"
        y "Suuuure~..."
        s g9 "Ugh!"
        hide green with d3
        hide scene_darkening with d3
        scene bgBase with fade
        pause 0.4
        "You decide to head to bed."
        scene black with longFade
        pause 2.0
        jump nightCycle
    if task7Stage == 2:
        stop music fadeout 1.0
        $ task7Stage = 3
        scene bgOffice with fade
        show timModel at ri with d3
        tim "................."
        play music "audio/music/ambient1.mp3" fadein 2.0
        tim "Why did you call me here?"
        "Mastermind" "You wanted proof that we're making the world a better place, right?"
        "Mastermind" "Well here it is..."
        $ jerryFace = 6
        show jerryModel:
            xalign 0.2 yalign 0.0 xzoom -1
        with d5
        tim "............"
        tim "Mr. Lewis..."
        $ jerryFace = 6
        "???" "Tim... I should've known you played a part in all this..."
        "???" "My spies will stop you. Like they did all those other times!"
        tim "Not this time, Jerry. Your spies are under our control and soon they will help us wipe your pathetic organization from the map."
        $ jerryFace = 4
        "Jerry" "Once a villain, always a villain..."
        tim "Don't try to lecture me, Jerry. Don't pretend you haven't done anything shady to get WOOHP to where it is now."
        tim "Your precious spies are living proof of that."
        "Jerry" ".................."
        tim "Where was he hiding?"
        "Mastermind" "He was in Beverly Hills. No doubt looking for his girls."
        "Mastermind" "Luckily one of ours found him before anyone else did."
        show sebModel1:
            xalign 0.0 yalign 0.0
        with d3
        "Mastermind" "Tim, I'd like to introduce you to S-..."
        tim "We've met."
        tim "Figured it'd be you leading Drift Punk."
        "???" "....................................................................."
        hide timModel
        hide sebModel1
        hide jerryModel
        with d3
        stop music fadeout 2.0
        jump nightCycle
    if task7Stage == 3:
        $ samMood = 100
        $ cloverMood = 100
        $ alexMood = 100
        $ task7Stage = 4
        pause 1.0
        show scene_darkening
        with d3
        s "[playerName]!"
        c "Terrible news!"
        a "Poor Jerry!"
        y "What what what?!"
        show green g29 at ri
        show red r32 at ce
        show yellow y5 at le
        with d3
        c "Look at today's most viral video!"
        y "{i}'Old British man tortured violently.'{/i}"
        y ".................."
        "{b}*Bleep*{/b}"
        $ jerryFace = 6
        scene bgOffice
        show jerryModel at ri
        show agentModel2 at le
        show expression "models/agent/hood.png" at le
        show scene_camera
        with fade
        "Agent" "I really don't want to do this Mr. Lewis, but you leave me no choice..."
        jerry "You brute! You monster!"
        "Agent" "Last chance, Jerry...."
        jerry "No matter how much you torture me, I will NEVER talk!"
        "Agent" "Let's see how talkative you are after this...."
        show whiteBoard:
            xalign 0.35 yalign 1.0
        with d3
        "Agent" "Repeat after me, it's spelled HONOR, not HONOUR."
        $ jerryFace = 5
        jerry "NO YOU MADMAN!"
        "Agent" "And it was fully in the colonies right to go independant."
        jerry "NO! NO I CAN'T TAKE IT ANYMORE!"
        "Agent" "Ever been to Boston? I hear the harbor still smells like tea."
        jerry "{b}*Cries*{/b}"
        "Agent" "And up next we're going to discuss the correct pronunciation of aluminium!"
        $ jerryFace = 6
        jerry "AAARGGHHH!"
        hide scene_camera
        hide jerryModel
        hide agentModel5
        scene bgBase
        with fade
        show scene_darkening
        show green g32 at ri
        show red r32 at ce
        show yellow y5 at le
        with d3
        y "........................."
        y "That poor British man..."
        a y28 "We have to save him!"
        c "I recognise the background. They're keeping him at his office."
        y "His office?"
        s g31 "Yeah.. at the top of WOOHP HQ..."
        a y4 "Oh no Jerry..."
        c "The WOOHP HQ is too heavily guarded right now. We'll have to liberate the city first."
        c "Once we've done that, we can lead one final assault and get WOOHP back."
        y "Sounds like a plan. Liberate Beverly Hills and then get your boss out."
        if traitorRandom == 568513:
            $ samMood = 50
            s g11 "...................."
        elif True:
            s g1 "I agree!"

        if traitorRandom == 870803:
            $ cloverMood = 50
            c r11 "..................."
        elif True:
            c r1 "Let's do it!"

        if traitorRandom == 708349:
            $ alexMood = 50
            a y11 ".................."
        elif True:
            a y1 "Yeah!"
        hide scene_darkening
        hide green
        hide red
        hide yellow
        with d3
        pause 0.5
        call qUpdated from _call_qAccept_5
        pause 0.5
        "Your spies' mood has improved!"
        $ samMood += 10
        $ cloverMood += 10
        $ alexMood += 10
        pause 0.4
        scene bgMap:
            xalign 0.0 yalign 0.0 zoom 0.5
        with fade
        jump worldmap

default task8Stage = 0
default task8Name = ""
default task8Text = ""

screen task8Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task8Text]"

label task8:
    if task8Stage == 0:
        $ task8Stage = 1
        scene bgStreet5 with fade
        "{b}*Mumble* *Mumble*{/b}"
        y "...?"
        show agentModel2 at ri
        show agentModel3:
            xalign 0.5 yalign 0.0 xzoom -1
        with d3
        "Agent 1" "What a lovely day we're having! Makes me want to do crime!"
        "Agent 2" "I don't know.. I haven't been feeling like doing crime lately.."
        "Agent 1" "Uh oh! Looks like somebody has a case of the Mondays!"
        "Agent 1" "But you're in luck! They're bringing out a software update which boosts the nanobot corruption!"
        y "!!!"
        "Agent 2" "Oh boy! I can't wait to feel fully energized and ready to rob a bank again!"
        y "(A software upgrade...? I better tell the gir-...)"
        hide agentModel3 with d2
        show agentModel3:
            xalign 0.5 yalign 0.0
        with d2
        "Agent 2" "Hello there fellow agent! Are you excited about the new nanobot upgrade?"
        y "Er..."
        menu:
            "'Sure am!'" if True:
                y "I sure am! Ready to live my life as a mindless drone without having to take responsibilities for my actions!"
                "Agent 1" "See? He gets it!"
                "Agent 2" "I remember the days where my actions had consequences. Those were dark times indeed!"
                "Agent 2" "Just the thought of it makes me want to destroy somebody elses property!"
            "'No, I'm not'" if True:
                y "Are you crazy?! Of course I'm not ready! Has this update even been tested?!"
                "Agent 1" "Don't worry fellow co-worker. I understand if you're afraid of the new, but there's nothing to worry about!"
                "Agent 1" "Best case scenario we'll be rich and living the good life soon! Bad case scenario, we'd all be dead!"
                y "..................."
                y "And you don't see a problem with th-...?"
                "Agent 1" "It's a win/win situation!"
            "Say something insane" if True:
                y "It's all binary, right? Aren't you afraid the 1's and 0's begin to whisper in your ear?"
                "Agent 1" "Wow! {w}That is probably the craziest thing I've ever heard!"
                "Agent 2" "Don't worry co-worker! The data cannot hurt you!"
                "Agent 1" "Unless it glitches out and leads us all to our inevitable doom!"
                y "......................."
        "Agent 1" "Anyways, we should get going. Those jewelers aren't going to rob themselves!"
        hide agentModel2
        hide agentModel3
        with d3
        pause 0.5
        y "........................"
        y "(A software update... Best discuss it with the girls once I get the chance.)"
        "The sun is setting and you quickly make your way back to the base."
        jump jobReport
    if task8Stage == 1:
        $ yellowHair = 1
        $ task8Stage = 2
        $ slutLevel = 3
        $ sexAct3 = "Foreplay"
        show scene_darkening
        show green g16 at ri
        show red r10 at ce
        show yellow y1 at le
        with d3
        pause 0.5
        y "All right girls. We've got a problem on our hands."
        s g16 "A problem?"
        c r18 "What is it this time?"
        y "The nanobots are getting a software update..."
        y "Meaning you three might get controlled again soon."
        a y31 "Mr. Wiggles will protect me!"
        y "Well obviously we can rely on Mr. Wiggles."
        s g37 "........................."
        c r35 "........................."
        y "Who's Mr. Wiggles?"
        c r10 "Her dildo."
        y "Oh..."
        y "Where was I going with this?"
        y "Oh right!"
        play sound "audio/sfx/punch1.mp3"
        show yellow:
            xalign 0.0 yalign 0.0 xzoom -1
            linear 0.07 xalign 0.03
            linear 0.07 xalign 0.0
            linear 0.07 xalign 0.03
            linear 0.07 xalign 0.0
        "You slap Alex's dildo out her hands!"
        a y28 "Mr. Wiggles!"
        hide yellow with d3
        pause 0.4
        y "It means we might have to up your nanobot suppression."
        s g18 "Up it...?"
        c r16 "How?"
        y "By switching from masturbation to foreplay."
        play sound "audio/voice/what.mp3"
        s g29 "W-what?!"
        c r30 "Woah now... easy there buddy! What are you saying?!"
        y "I have two options available."
        y "1. Foreplay."
        c r29 "And the other...?"
        y "You're going to show off your nudity to others."
        c r30 "T-to others...?!"
        s g9 "You've got to be joking, [playerName]!"
        s "Having you present as we're naked is already bad enough! We're not also going to invite others!"
        y "Okay... Let's put it into perspective."
        s g39 "............."
        c r12 "{b}*Scoffs*{/b}"
        y "Either you stop being such stuck up prudes..."
        s g7 "H-hey...!"
        y "Or you're going to spend your life like mindless zombies. {w}Who knows what the mastermind has planned for you after his plan succeeds?"
        c r11 "......................"
        hide red with d3
        s g40 "I still think it's ridiculous. I haven't noticed anything out of the ordinary. I bet you're just trying to take advantage of us!"
        s "Right girls?"
        s g51 "Girls...?"
        stop music fadeout 3.0
        c r29 "Er... Sam, you might want to get over here...!"
        $ yellowHair = 6
        show red r29 at ce with d3
        show yellow y100 at le with d3
        play music "audio/music/sinister.mp3" fadein 1.0
        s "Alex...?"
        a "{b}{size=+8}I WANT.... BLOOD!{w} I WANT DESTRUCTION!{w} I WANT..... TO KILL!"
        y "Okay calm down, Alex. I'm sorry about Mr. Wigg-...."
        hide yellow with d2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        "Alex attacked you!"
        y "Argh! Not again!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        y "A LITTLE HELP HERE, PLEASE!"
        hide red
        hide green
        with d2
        "The two spies rush to your aid, but even with their combined strength they're no match for the crazed Alex!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        y "Ow!"
        y "Alex, listen to me!"
        y "Do you know what a buttjob is?!"
        a "..................."
        a "A what...?"
        "Seeing an opportunity, all three of you jump on the spy in yellow."
        "Quickly looking up the definition of a buttjob you show it to her."
        y "Look! This is a buttjob! And it's what you'll be doing!"
        show yellow y100 at le
        show red at ce
        show green at ri
        with d3
        a "I... I will?"
        s g38 "Yes you will, Alex!"
        $ yellowFace = 1
        a y29 "{b}*Blinks*{/b}"
        a "Oh hey guys. What did I miss?"
        s g16 "Are you back to normal again...?"
        c r38 "Alex... please go to your cell..."
        a y29 "What did I do...?"
        a y5 "{b}*Pouts*{/b}"
        stop music fadeout 2.0
        "Like a scolded child, Alex walks off to her cell."
        play music "audio/music/nighttime.mp3" fadein 3.0
        hide yellow with d3
        $ yellowHair = yellowHairSet
        c r32 "...................."
        s g11 "...................."
        y "So... foreplay. Or do you want to turn into {i}'that'{/i}?"
        s "................."
        c r38 "No...."
        y "Clover, we're going to practise your boobjobs."
        c r28 "B-but... {w}{b}*Sighs*{/b} Fine..."
        y "Sam, you're gonna be studying up on thighjobs."
        s g31 "What even is that...?"
        y "Look it up."
        "Sam grabs her phone and after a few moments finds the description."
        s g30 "!!!"
        s "N-no! I'm not gonna do tha-...."
        hide red
        with d2
        show red r52:
            xalign 0.5 yalign 0.0 xzoom -1
        with d2
        c "Give it a rest, Sam. Yes you're doing that."
        s g53 "N-no, you don't understand! He will actually be rubbing up against my-...!"
        c "Yes he will. Get over it."
        c r32 "Is that all, [playerName]?"
        y "No. I'm still pondering to show you off naked to strangers."
        s g28 "{b}*Sputters*{/b} B-but...!"
        c "Go on."
        y "Instead of breaking captured Agent nanobot control with dirty magazines, I might send you to expose yourself to them to help speed up the process."
        s g40 "Clover...! This is an outrage!"
        c "It sure is. I'm heading to my cell. We'll begin training tomorrow."
        s g28 "BUT...!"
        c r54 "Good night, Sam."
        hide red with d3
        pause 0.7
        s g39 "............................"
        s g19 "{size=-8}But....{/size}"
        y "Are you really so against this?"
        s g43 "........"
        s "I'm just kinda inexperienced with sex..."
        s g15 "But... of course I don't want to end up like Alex either..."
        "Sam sighs in defeat."
        s "Thighjob it is...{w} Let's start tomorrow..."
        hide green with d3
        hide scene_darkening with d3
        pause 0.3
        show scene_fighting with d5
        "Your spies have taken the next step of their training! In order to keep their nanobots controlled you've suggested foreplay to them."
        "This introduces a new way to suppress their nanobots. On top of that, you can now send your girls to break captured Agent's nanobots instead of using magazines."
        hide scene_fighting with d3
        jump nightCycle

default task9Stage = 0
default task9Name = ""
default task9Text = ""

screen task9Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task9Text]"

label task9:
    if task9Stage == 0:
        $ redChest = 0
        $ redUnder = 0
        $ redBottom = 0
        $ redShoes = 0
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ task9Stage = 1
        $ spy2Status = 10
        $ mapSpy2Selected = False
        show scene_darkening
        with d3
        y "Clover, go visit Drift Punk again today."
        cM "Nah, no need. They said they're testing something new today and don't need any help."
        y "......................."
        y "Then I definitely want you to go. What's this new thing they're testing?"
        cM "Er... Actually...{w} I didn't ask... I don't know."
        y "Then we're going to find out what they're up to."
        y "Sneak into their base and report back on what you find."
        cM "Aw... so much for my day off...."
        $ task10Name = _("Living in a database")
        $ task10Text = _("Something is going on with Drift Punk. They're testing out something new so I sent Clover to investigate.")
        call qAccept from _call_qAccept_6
        hide scene_darkening with d3
        jump worldmap
    if task9Stage == 1:
        $ task9Stage = 2
        $ spy2Status = 10
        $ redHat = 0
        pause 1.5
        y "................"
        y "No Clover...?"
        "{b}*Beep* *Beep* *Beep*{/b}"
        y "....?"
        show scene_darkening with d3
        "???" "010000100110111101101111"
        y "What the...?!"
        cM "Scared ya?"
        y "Clover, was that binary? Where are you?"
        cM "Oh you're not gonna believe this..."
        cM "I am inside your phone."
        y "............."
        y "What....?"
        cM "Turn on your spy camera screen."
        y "Why~...?"
        cM "Oh you'll see~...."
        hide scene_darkening with d3
        pause 0.4
        "{b}*Beep*{/b}"
        stop music fadeout 2.0
        scene bgDatabase with fade
        pause 1.0
        y "Woah...!"
        play music "audio/music/ambient1.mp3" fadein 1.0
        pause 0.3
        show scene_darkening with d3
        show red r1 at ri with d3
        c "Welcome to... {w}this... place."
        y "Where are you?"
        c r16 "Remember that new thing Drift Punk was testing? This is it."
        c "It's some kind of cyber world."
        y "A what...?"
        c r18 "A completely digital world. Members digitize themselves and are transported here."
        y "Sounds dangerous. Get out of there and report back."
        c "No not yet! The Punks are showing off this technology to one of their higher ups and I just want to get a good look at them."
        y "Sounds like a good way to get yourself captured, but all right."
        c "Clover out."
        stop music fadeout 3.0
        hide scene_darkening
        hide red
        with d3
        pause 0.5
        scene bgBase with fade
        play music "audio/music/nighttime.mp3" fadein 2.0
        jump nextReport
    if task9Stage == 3:

        $ redUnder = 0
        $ redChest = 0
        $ redBottom = 0
        $ redShoes = 0
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ missionAreaDatabaseActive = True
        pause 0.5
        $ task9Stage = 4
        show scene_darkening with d3
        show red r1 at ri with d3
        y "Clover! You're back!"
        c "Yup, and I got a bunch of new intel!"
        $ randIntel = 150
        call missionRewardInt from _call_missionRewardInt_19
        pause 0.3
        c r14 "So.. Where to begin..."
        c "Drift Punk have set up a high tech cyberworld. They use it for hacking in people's hardware and to lie low when they've got too much heat on them."
        c r31 "Not only that, but I saw the Drift Punk leader!"
        c "I didn't recognize him because he was wearing a helmet though..."
        y "We'll go after him later. So how was the digital world?"
        c r23 "Not gonna lie... It was pretty cool."
        c "Normally I am {i}'so'{/i} not into all this nerdy stuff, but I got to travel the internet!"
        c r22 "I visited social media sites and went through people's private pictures~..."
        y "Naughty. Found any good games while you were at it?"
        c r38 "Tsk... games are for boys. I didn't look at anything like that."
        c "........................"
        c r12 "Well there was this one farming game that looked kind of cute, but I didn't play it."
        c "Anyways, that's my report. We can go on missions there now, and maybe dig up some dirt on Drift Punk."
        call qUpdated from _call_qUpdated_5
        hide red with d3
        play sound "audio/sfx/itemGot.mp3"
        "{color=#ffeda6}Punk Web{/color} has now been unlocked for missions."
        $ spy2Status = 0
        "New shopping options are available for Clover at the mall."
        $ task10Text = _("Drift Punk is working on a digital world where they can lay low and terrorize the world from within a computer.\n\nI should continue sending my spies undercover with Drift Punk and see if we can find out who's in charge.")
        hide scene_darkening with d3
        hide scene_darkening
        hide red
        with d3
        jump base

default task10Stage = 0
default task10Name = ""
default task10Text = ""

image spyHitTask10 = "mission/models/clover/spyHit.png"
image spyAttack1task10 = "mission/models/sam/spyCombat1.png"
image spyAttack2task10 = "mission/models/alex/spyCombat3.png"

screen task10Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task10Text]"

label task10:
    if task10Stage == 0:
        if spyYellowActive == False:
            y "We should really focus on finding a way to free Alex before we do this."
            jump worldmap
        $ task10Stage = 1
        $ spy2Status = 10
        $ mapSpy2Selected = False
        $ task10Name = "Living in a database"
        cM "I'm jacking in today."
        y "Clover! Language!"
        cM "Jacking in.... not jacking off."
        y "Oh..."
        y "What?"
        cM "There were rumors of an important meeting in Punk Web today. I'm gonna do some snooping around."
        y "All right, be careful though."
        cM "Of course!"
        jump worldmap

    if task10Stage == 1:
        $ task10Stage = 2
        $ redUnder = 0
        $ redChest = 0
        $ redBottom = 0
        $ redShoes = 0
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ task10Text = _("We discovered that a former video game programmer called Carla Wong, aka The Dragon Lady, is the lead developer on Punk Web. She's already attacked Clover once, so it's time we brought her in.\n\n-Set up a mission and capture Carla Wong.")
        "{b}*Beep* *Beep* *Beep*{/b}"
        scene bgDatabase with fade
        show scene_darkening with d3
        y "Clover? Are you still in the cyber world?"
        show red r31 at le with d3
        c "Shhh...."
        drag "I see everything is running and is optimized to perfection..."
        c "I know that voice..."
        c r29 "!!!"
        c "Wait! That's Carla Wong...! Well that makes sense."
        y "Carla Wong?"
        c r31 "Hang on I'm coming ba-..."
        drag "Who's there...?!"
        c r30 "Uh oh~... Clover out!"
        hide red with d2
        y "Clover?!"
        y "........................"
        y "She's gone..."
        scene bgBase with fade
        pause 0.3
        show green g28 at ri
        show yellow y29 at le
        with d3
        s "[playerName]? Was that Clover just now?"
        a "Is she in trouble?!"
        y "Maybe. I'm sending you two on a special night time mission to get her back!"
        $ intel += 300
        s g31 "Okay, we won't fail!"
        $ missionScreenCurrentLocation = 3
        $ missionScreenFrontlineSelect = 1
        $ cloverOnMission = True
        $ alexOnMission = True
        $ backupAlexActive = True
        jump missionScreenFinish

    if task10Stage == 2:
        hide screen gadgetMenu
        hide screen interactScreen
        hide screen equipmentMenu
        $ task10Stage = 3
        $ randomBackground = 1
        $ cloverHealth = 0
        $ cloverMood = 20
        play sound "audio/sfx/punch1.mp3"
        show globalImageDatabase:
            zoom 0.25
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        show obstDragon:
            xalign 0.75 yalign 0.51 zoom 0.41 rotate 3
        show obstHulkAttack:
            xalign 0.5 yalign 0.45 zoom 0.53 rotate 3
        show spyHitTask10:
            xalign 0.39 yalign 0.36 zoom 0.35 xzoom -1
            linear 0.4 xalign 0.385 yalign 0.34
        pause 0.7
        hide spyHitTask10
        hide obstHulkAttack
        show obstHulk:
            xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
        with d3
        if activeSpy == 1:
            s "(Clover!)"
        elif activeSpy == 3:
            a "(Clover!)"
        elif True:
            $ activeSpy = 1
            s "(Clover!)"
        drag "Don't you know that curiosity killed the cat?"
        drag "Deal with her, I have an important meeting to attend to."
        hide obstDragon
        with d3
        y "Now is your chance!"
        play sound "audio/voice/onIt2.mp3"
        s "On it!"
        play sound "audio/voice/alex/ready.mp3"
        a "Ready to strike!"
        hide spyCorner
        hide obstHulk
        play sound "audio/sfx/defeatEnemy.mp3"
        show obstHulkHit:
            xalign 0.50 yalign 0.415 zoom 0.52
            linear 0.05 xalign 0.505
            linear 0.05 xalign 0.50
            linear 0.05 xalign 0.505
            linear 0.05 xalign 0.50
        show spyAttack1task10:
            xalign 0.42 yalign 0.48 zoom 0.49
            linear 0.05 yalign 0.39
        show spyAttack2task10:
            xalign 0.60 yalign 0.55 zoom 0.45 xzoom -1
        with d2
        pause 0.3
        hide obstHulkHit
        with d2
        pause 0.5
        hide spyAttack1task10
        hide spyAttack2task10
        with d3
        pause 1.0
        show scene_darkening with d3
        show green g49 at ri
        show yellow y5 at le
        show red r15:
            xalign 0.5 yalign -0.2
        with d3
        pause 0.3
        $ _skipping = True
        a "Clover!"
        s "She's hurt..."
        y "Get out of there and take her back to the base."
        hide globalImageDatabase
        scene black
        stop music fadeout 4.0
        with longFade
        pause 1.0
        scene bgBase
        with fade
        pause 0.5
        show scene_darkening with d3
        "The spies return the wounded Clover back to her cell."
        y "How is she?"
        show green g4 at ri
        show yellow y5 at le
        with d3
        s "She took a nasty hit, but she'll be alright. She needs to rest for now. If you have any medkits, they'd be really good right now aswell."
        menu:
            "Here, give her this (medkit x1)" if medkit >= 1:
                $ cloverMood += 5
                $ cloverHealth = 2
                s "Thanks, that should help a little."
            "I'll keep an eye out for one" if True:
                s "We really should have some on hand."
        s ".................."
        s g32 "Carla Wong is dangerous. Last time we fought her, Alex nearly bit the bullet."
        a y30 "I got trapped inside one of her games..."
        a y29 "I'm afraid she might do the same with Punk Web."
        y "Taking her down should be a priority then. For now let's call it a day. You've all have earned your rest."
        "The girls nod and you head to bed."
        hide green
        hide yellow
        with d3
        pause 0.5
        call qUpdated from _call_qUpdated_6
        hide scene_darkening with d3
        pause 0.5
        show scene_fighting with d3
        "The first Drift Punk lieutenant has shown herself and is available for capture in Punk Web. Set up a mission and have your spies capture her."
        $ specialDragonStatus = 1
        hide scene_fighting with d3
        pause 0.5
        jump nightCycle

    if task10Stage == 3:
        $ task10Stage = 4
        $ specialDragonStatus = 3
        $ carlaSocial = 1
        $ task10Text = _("We discovered that a former video game programmer called Carla Wong, aka The Dragon Lady, is the lead developer on Punk Web. She's already attacked Clover once, so it's time we brought her in.\n\n{color=#b5b5b5}-Set up a mission and capture Carla Wong.{/color}\n\n{color=#b5b5b5}-Interrogate Carla Wong at the base.{/color}")
        $ task10Name = _("Living in a database (complete)")
        y "Let's see what info WOOHP has on you...{w}Carla Wong, aka The Dragon Lady."
        drag "......................."
        y "Your file also says you're a massive nerd who's into video games."
        drag "Hey!"
        y "So tell me Carla...{w} Do you like jewelry?"
        drag "What?"
        show red r16 at le with d3
        c "What are you doing, [playerName]...?"
        y "Hey Clover, feeling better?"
        y "I brough a ton of gifts to raise her affection rating. Then when we're best friends, she'll tell me why she's been working for Drift Punk."
        c r10 "..................."
        c "Her eyes are red. Isn't that usually a sign that she's being controlled by nanobots?"
        y "You're right! Now I just have to boost my relationship rating with her until we can have sex!"
        drag "Wait... I'm being controlled...?"
        c r52 "Yeah. You know those fancy nanobots you started spreading over the population? They infected you aswell."
        drag "Hah! Nobody control the dragon! You're just sore how I had my men beat you!"
        c r53 "Listen here you megalomaniac bitc-....!"
        y "Carla, haven't you been feeling anymore murdery than usual?"
        drag "........................"
        c r31 "We're not gonna get anything useful out of her, [playerName]. Just fuck her like you did Maggie."
        drag "Wait... what..?!"
        c r24 "Oh yeah, you didn't know? Sex reduces the nanobot control.{w} This guy over here is going to blindfold you, tie you up and fuck you until you come to your senses."
        c r22 "Right, [playerName]?"
        drag "N-now wait a minute...!"
        y "Yup! And Clover seems so excited, I bet she'll even join in!"
        c r12 "{b}*Scoffs*{/b} Yeah right..."
        y "Carla, they're controlling you like you control your video game characters. Surely you don't want that."
        drag "..........................."
        drag "And you're saying that having sex will break the nanobot control?"
        c r52 "It has so far."
        drag "Fine, then let's get it over with. I'm nobodys play puppet."
        drag ".........................................."
        drag "Can..."
        y "...?"
        drag "Can you still tie me down and blindfold me...?"
        c r29 "Oh God, she's into it..."
        y "I don't even need to boost your affection rating...? {w}Everything video games taught me about relationships is a lie."
        c r11 "I'll... just leave you two to it then."
        y "You don't wanna watch?"
        c r10 "..............."
        c "I feel like she'd be into that too and I don't wanna give her the pleasure..."
        hide red with d3
        drag "Now where were we~...."
        scene black with fade
        pause 0.4
        drag "Ah! Ahh! Ah!"
        drag "Yes, faster! Ahh~..."
        drag "Give me your joystick! Yes! ♥♥♥♥"
        drag "Oh! Ohhh, yes! Use the extension cord!"
        drag "Ahhhh!!!! ♥♥♥♥♥♥"
        y "Say cheese!"
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d3
        pause 0.5
        show picCarla:
            xalign 0.5 yalign 0.5
        with dissolve
        pause
        play sound "audio/sfx/itemGot.mp3"
        "A new photo has been added to your photoalbum."
        hide picCarla
        scene bgPrison
        with fade
        show scene_darkening with d3
        scene bgPrison with fade
        show scene_darkening with d3
        drag "Oh my...~"
        y "Back to your senses?"
        drag "Yeah... I can't believe I was being controlled..."
        y "Time for payback. Tell us as much as you know."
        drag "Well..."
        scene black with fade
        $ randIntel = 300
        $ intel += 300
        call missionRewardInt from _call_missionRewardInt_15
        play sound "audio/sfx/itemGot.mp3"
        scene bgPrison
        show scene_darkening
        with fade
        drag "That's all I know. Can I go now?"
        y "What? No, of course not. This is a prison we can't just let you go!"
        drag "Oh..."
        drag "I'll suck your dick again if you let me g-..."
        y "No."
        drag "................"
        $ punkRep = 0
        $ punkRank = 2
        hide scene_darkening with d5
        pause 0.8
        show scene_fighting with d3
        "Computer" "Booting up WOOHP Bounty Board..."
        "Computer" "Target: Carla Wong\nStatus: Captured."
        "Computer" "Transferring funds..."
        $ cash += 500
        $ randMoney = 500
        call missionRewardMoney from _call_missionRewardMoney_67
        pause 1.6
        hide scene_fighting with d3
        scene black with fade
        scene bgBase with fade
        jump base

default task11Stage = 0
default task11Name = ""
default task11Text = ""

screen task11Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task11Text]"

label task11:
    if task11Stage == 0:
        $ task11Name = _("Anarchy Alex")
        $ task11Text = _("I sent Alex out to get more comfortable with going undercover with the Outsiders.\n\n-Wait to see how Alex reacts to going undercover with the Outsiders.")
        $ task11Stage = 1
        scene bgBar with fade
        show scene_darkening with d3
        show yellow y1 at ri with d3
        y "Okay Alex. You're heading back to the Outsiders today."
        a y19 "{b}*Whines*{/b} But..."
        y "No buts. Honestly, I expected better from you Alex."
        a y16 "...?"
        y "Judging people on their appearance. Emos deserve love too y'know."
        a "They do?"
        y "......."
        y "Yeah of course. Everyone does."
        a y18 "That's not what WOOHP taught us. We're taught not to feel any sort of pity or remorse for our opponents."
        y "....................."
        y "Okay... that's a little dark."
        a y38 "{i}'If they want to be loved or understood, they should've thought of that before turning evil.'{/i}"
        y "Harsh... Just go over there and hug an emo for me."
        a y15 "Okay~...."
        hide yellow with d3
        hide scene_darkening with d3
        call qAccept from _call_qAccept_7
        pause 0.4
        scene bgMap:
            zoom 0.5
        with d3
        $ mapSpy3Selected = False
        $ spy3Status = 1
        $ yellowDayJob = 3
        jump worldmap
    if task11Stage == 1:
        $ task11Stage = 2
        $ task11Text = _("Alex has taken her first steps of blending in with the Outsiders.\n\n{color=#b5b5b5}-Wait to see how Alex reacts to going undercover with the Outsiders.{/color}\n\n-Raise your reputation with the Outsiders.")
        show scene_darkening with d3
        show yellow at ri with d3
        y "Okay Alex, tell me about your day with the Outsi-..."
        a y40 "NEVERMORE!"
        y ".............."
        y "Wha-...?"
        a y8 "Kaw!"
        y "Alex, you're scaring me. What the hell are you doing?"
        a y1 "Today I learnt a poem about a raven!"
        y "Oh... you're quoting Edgar Allen Poe... Not sure what I expected sending you undercover with goths."
        y "So how was it?"
        a y2 "Well... I tried being more open today and got talking to some of them."
        a "They shared their poetry with me! I tried writing some myself too. A poem I call 'Candy Cavity Calamity'. Want to hear it?"
        y "I'll pass. What did they think?"
        a y1 "Well... someone said it was childish. Then someone else said it was ironic. Then someone else said it was post-ironic."
        a "I don't really understand what they meant, but they seemed to like it. Saying it had much deeper meaning."
        a y18 "I'm still trying to figure out the deeper meaning..."
        y "Well at least you participated in their activities today. I'm going to keep sending you undercover. Try your best to blend in."
        a y40 "NEVERMORE!"
        y "............."
        y "Are you objecting or are you just quot-..."
        a y8 "Quote the Raven, Nevermore!"
        "You sigh and usher the squawking spy to her cell."
        hide yellow with d3
        hide scene_darkening with d3
        jump base

    if task11Stage == 2:
        a "On my way!"
        $ spy3Status = 10
        $ mapSpy3Selected = False
        $ task11Stage = 3
        jump worldmap

    if task11Stage == 3:
        $ task11Stage = 4
        $ missionAreaFaireActive = True
        $ task11Name = _("Anarchy Alex")
        $ task11Text = _("Alex has taken her first steps of blending in with the Outsiders.\n\n{color=#b5b5b5}-Wait to see how Alex reacts to going undercover with the Outsiders.{/color}\n\n-Raise your reputation with the Outsiders and capture Muffy Peprich.\n\nYou can now plan missions to the Carnival.")
        show scene_darkening with d3
        show yellow y4 at ri with d3
        a "{size=-8}I'm back...{/size}"
        y "Alex? How did it go today?"
        a "It went okay..."
        y "......................"
        y "What happened~...?"
        a y5 "{b}*Pouts*{/b}"
        a "I was yelled at today..."
        a "This punker looking girl told me to stop acting like a child..."
        menu:
            "She has a point" if True:
                y "Well then maybe you should stop acting like a 6 year old."
                a y28 "Not you too!"
                y "Alex, going undercover involves actually trying to fit in."
                a y29 "Fit in...?"
                y "Yeah, act like the other gangmembers."
                y "Try being a bit more...{w} 'angsty'."
                a y5 ".................."
                y "Put on some darker make-up, tear some holes in your clothes. Pretend that you understand the world and fight against the {i}'man'{/i}."
            "I like childish Alex" if True:
                a y29 "But I'm not childish..."
                a y38 "Why doesn't anyone take me seriously?!"
                y "Alex... Yesterday when we talked you suggested renting a unicorn to bring in more customers...."
                a y1 "Yeah!"
                y "........................"
            "Say something insane" if True:
                y ".................................."
                y ".................................."
                y "..................................{w} You are baby."
                a y28 "[playerName]!"
                y "Big baby."
                a y28 "I'm not a baby!"
                y "Need pacifier.{w} Big baby."
                a y4 "[playerName]...! {b}*Sniff*{/b}"
                a y42 "Stop bullying me...!"
                y "Small baby?{w} I think not.{w} Big baby."
                a "{b}*Cries*{/b}"
                a "....................."
        a y15 "..............................."
        a "I think I know what you mean....."
        a y38 "All right... I'll try to be more grown up!"
        y "Good."
        a y38 "Fight the establishment!"
        y "Yeah!"
        a "Dye my nails black!"
        y "All right!"
        a "Do my taxes and figure out a good retirement plan!"
        y "Okay... not {i}'that'{/i} grown up."
        a y40 "Also I'm going to their creepy abandoned amusement park!"
        y "................."
        y "What do you mean... {i}'going to'{/i}?"
        y "Haven't you been going undercover there all this time?"
        a y1 "Who me? No way, it was way too scary!{w} I usually just called up the gangsters to go hang out around town."
        y ".............................."
        if specialMuffyStatus >= 1:
            a y3 "I'm pretty sure Muffy Peprich is hanging around the Carnival. I bet we could capture her now!"
        hide yellow with d3
        pause 0.5
        call qCompleted from _call_qCompleted_8
        pause 0.5
        "You can now send your spies on missions to the 'Carnival'. The abandoned amusement park on the edge of town."
        "New clothing options are available for Alex at the mall."
        $ missionAreaFaireActive = True
        $ outsideRank = 2
        $ outsideRep = 0
        hide scene_darkening with d3
        pause 0.3
        jump base

default task12Stage = 0
default task12Name = ""
default task12Text = ""

screen task12Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task12Text]"

label task12:
    if task12Stage == 0:
        pause 0.5
        scene bgMall with fade
        y "Hmmm...."
        y "It's been [daysPlayed] days... I could really use a haircut."
        y "I hope there's still some around...{w} Who am I kidding, this is Beverly Hills. Of course there's still hairdresses around."
        show scene_darkening with d3
        "Barber" "Why helloooo! Did I hear you needed a haircut?"
        y "Erm... yeah, I do. Are you still open?"
        "Barber" "Yeeeees!"
        y "................"
        y "Okay... can you do my hai-..."
        "Barber" "Nooooo!"
        y "........"
        y "Why no-...?"
        "Barber" "You see something terrible has happened! Drift Punk have kidnapped my niece, and I am too worried about her well being to do any hairdressing!"
        y "Let me guess... you want me to get her back?"
        "Barber" "Yeeeeees!"
        y "And you're not gonna pay me for it, are you?"
        "Barber" "Noooooo!"
        y "...................."
        menu:
            "Accept mission" if True:
                $ task12Name = _("A few snips away of a haircut")
                $ task12Text = _("I promised to look into the disappearance of a hairdressers' niece. Apparently she's been kidnapped by Drift Punk, I should begin my search there.\n\nSend a spy undercover with Drift Punk.")
                $ task12Stage = 1
                y "Okay, I'll do it, but you have to tell me why you speak like that."
                "Barber" "What do you meeeeeeeean?"
                y "Okay... Never mind, I'll go get your niece back."
                y "But only if you promise free haircuts for me and my girls after I'm done."
                "Barber" "Yeeeeees!"
                "Barber" "Please bring her back home safely!"
                hide scene_darkening with d3
                call qAccept from _call_qAccept_8
                scene bgMap:
                    zoom 0.5
                with d3
                jump worldmap
            "Decline mission" if True:
                y "You're creepy...."
                "Barber" "Nooooooooo!"
                y "On second thought, I don't think I need a haircut..."
                "You quickly leave the mall."
                scene bgMap:
                    zoom 0.5
                with d3
                jump worldmap
    if task12Stage == 1:
        pause 1.0
        $ task12Stage = 2
        $ task12Text = _("I promised to look into the disappearance of a hairdressers' niece. Apparently she's been kidnapped by Drift Punk, I should begin my search there.\n\n{color=#A3A3A3}Send a spy undercover with Drift Punk.{/color}\n\n-The girl may be held in Punk Web. Set up a mission and get her out.")
        show scene_darkening with d3
        show green at le
        show red r32 at ce
        show yellow y32 at ri
        with d3
        y "So, any news of the hairdresses' niece?"
        c r31 "Nothing. They could be holding her in Punk Web."
        y "We'll have to plan a mission then."
        y "Okay I'll set one up if we got time."
        hide green
        hide red
        hide yellow
        with d3
        hide scene_darkening
        with d3
        jump base
    if task12Stage == 2:
        $ task12Stage = 3
        show globalImageDatabase:
            zoom 0.25
        hide screen interactScreen
        $ randomExit = 0
        $ randomBackground = 1
        $ randomCover2 = 0
        $ randomCover1 = 0
        $ task12Stage = 3
        hide screen equipmentMenu
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        hide black with fade
        "???" "Heeeeeello? is somebody theeeeere...?!"
        y "............."
        "???" "I'm trapped in here, pleeeeeeease get me out!"
        y "Yeah that sounds like the niece we're looking for."
        call screen interactScreenBonus
    if task12Stage == 3:
        $ task12Text = _("I promised to look into the disappearance of a hairdressers' niece. Apparently she's been kidnapped by Drift Punk, I should begin my search there.\n\n{color=#A3A3A3}Send a spy undercover with Drift Punk.{/color}\n\n{color=#A3A3A3}-The girl may be held in Punk Web. Set up a mission and get her out.{/color}")
        $ task12Stage = 4
        play sound "audio/sfx/lock.mp3"
        pause 1.0
        show scene_darkening with d3
        niece "Oh thank you for getting me out!"
        y "Don't mention it. We're getting you back to your uncle."
        niece "Oh yeeeees!"
        scene black with longFade
        jump missionComplete
    if task12Stage == 4:
        $ task12Name = _("A few snips away (complete)")
        $ task12Text = _("We managed to release the barber's daughter from Punk Web and can now get free haircuts at the mall whenever we like.")
        $ task12Stage = 5
        scene black with fade
        scene bgMall with fade
        pause 0.7
        show scene_darkening with d3
        y "We brought back your niece."
        niece "Uncle! Oh yeeeees, it's good to see you!"
        "Barber" "Yeeeeees!"
        y "...................."
        y "So er... about my reward..."
        "Barber" "Oh yeeeees! Haircuts are now free of charge!"
        y "Nice."
        call qCompleted from _call_qCompleted_5
        hide scene_darkening with d3
        jump mall


default task13Stage = 0
default task13Name = ""
default task13Text = ""

screen task13Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task13Text]"

label task13:
    if task13Stage == 0:
        $ task13Stage = 1
        show scene_darkening with d3
        call undressClover from _call_undressClover_4
        $ redChest = 11
        $ task13Text = _("We've begun talking about having sex together, but Sam is still vividly denying it. I should go talk to her in her cell.")
        show red r1 at ce with d5
        c "Oh hey [playerName]. Sorry, just got out of the shower, don't mind me."
        hide red with d5
        pause 0.5
        call undressAlex from _call_undressAlex_5
        $ yellowUnder = 1
        show yellow y1 at ce with d5
        a "Hey [playerName] I need new batteries for Mr. Wiggles. Have you seen any around?"
        hide yellow with d5
        pause 0.5
        call undressSam from _call_undressSam_7
        $ greenArms = 2
        show green g56 at ce with d5
        s "Has anyone seen my underwe-..."
        y "OH COME ON!"
        show yellow at le with d3
        show red at ri with d3
        y "Let me tap that ass!"
        s g29 "!!!"
        a y28 "!!!"
        c r30 "!!!"
        y "It's been [daysPlayed] days since we met and you guys haven't been making it easy on me!"
        s "What do you mea-....?{w} Oh..."
        $ greenArms = 2
        "The girls awkwardly look at each other."
        c r57 "We've talked about this, girls.{w} I think he should know."
        s g38 "I still don't agree with it!"
        y "What are you talking about?"
        c r12 "Well... foreplay is fun and all, but I think we should drop the 'fore' part and focus more on the 'play'...."
        s "Blondie over here seems to think we need to start having sex if we want to control the nanobots!"
        y "That's outrages."
        s g28 "Exactly! That's what I said!{w} Sure, we're being pumped full of nanobots, but we can't keep escalating this."
        y "Of course. Being pumped full of one liquid is bad enough."
        s g31 "E-exactly! We don't need to also... get pumped.... full of...."
        y "{b}*Smirk*{/b}"
        s g34 "We're not having sex with you, [playerName]!"
        c r24 "I might."
        s g31 "CLOVER!"
        a y1 "Is [playerName] going to pound some puss...?"
        s g40 "ALEX!"
        c r55 "Sam, relax."
        c "These nanobot injectors are great for getting new skills, but we've been getting more easily controlled."
        c "Alex here won't even turn back to normal unless we give her a full tongue bath."
        a y29 "Those tickle!"
        c r14 "We need to take control of this situation before it gets worse. That means going down on each other and having sex."
        s "G-going dow-...?!"
        c "And have sex. Yes."
        c r52 "Listen, you can play Ms. Virtuous Maiden as long as you like, but you're just delaying the inevitable."
        c "WOOHP isn't going down if you keep acting like a prude."
        s g43 "Well I...!{w} We should ask [playerName] what he thinks!"
        c r22 "He's a guy. I already know what he thinks."
        s g38 "S-still..!"
        a "Hey [playerName]. Do you want to take cooking lessons and pour our ovens full of baby batter?"
        menu:
            "YES!" if True:
                y "OF COURSE! Let's do it...!{w} Right now!"
                c "Desperate much?"
                y "I've been surrounded by sluts for [daysPlayed] days now!"
                y "I've been waiting for this moment the first time Sam took off her clothes!"
                s g28 "H-hey...!"
            "I mean.. if I have to" if True:
                y "I guess..."
                c r18 "What do you mean, {i}'I guess'{/i}? Three sluts are offering to throw themselves at you!"
                s g29 "S-sluts?!"
                c "Show some balls, [playerName]. You're gonna have sex with us, whether you like it or not."
                y "I don't care much for this sexual intimidating at the workplace...!"
            "Say something insane" if True:
                y "..............................."
                c r16 "Oh no... I know that look on his face."
                y "You ever think we might not be in control of our own destiny?{w} Like some all powerful omnipitant force is writing our words for us?"
                y "Like from one line to the next, we might say something completely crazy and out of characters?"
                a y14 "I believe you're experiencing what is known as Depersonalization Disorder or DPDR. In which the person has a presistent or recurrent feeling of derealization or a disconnect from one's self."
                y ".................."
                y "Yeah you're right. I'm just talking crazy."
        c r24 "So if we're all agreed. [playerName] should have sex with us from now on!"
        s g38 "We're not all agreed!"
        a y29 "Wait... we're still talking about sex?"
        s "I think it's just {i}'you'{/i} who wants sex, Clover!"
        c r17 "Wait... what?!"
        s "I understand being cut off from boys for this long is taxing on you, but you have to control your urges."
        c r38 "That has nothing to do with it!"
        s "You can't blame the nanobots for everything, Clover."
        c r14 "I'm doing this for the mission!"
        s "................................"
        c "................................"
        c r11 "Okay.... well maybe I'm also doing it a little for myself..."
        s g23 "I've known your slutty ass for longer than today."
        c r42 "{b}*Groans*{/b}"
        s g38 "That doesn't excuse this slutty behavior though!"
        s "All three of you should be ashamed of yourselves. We're suppose to saving the world and all you're thinking about is sex!"
        a "Wait...!{w} Are we going to have sex?"
        c r54 "Tsk, hello! Pot calling the kettle black. I've heard you going at it with your dildo, miss perfect. Our cells are right next to each other, remember?"
        c "You're probably the thirstiest of all of us!"
        $ greenBlush = 1
        s g40 "Preposterous!"
        s "Nobody is having sex and that's final!"
        hide green with d3
        pause 0.5
        $ greenBlush = 0
        y "........................."
        y "So about the offer~..."
        c r11 "Sam sorta ruined the mood..."
        y ".........."
        a y1 "She's just being grumpy. Visit her in her cell and talk one to one. She might be more open to you then."
        y "Right...."
        a "Gotta put in the work if you want to get your dick wet, [playerName]!"
        y "Alex... for someone as naive and innocent as you, you sure have a dirty mouth."
        a y29 "Oops...! I should go wash it with soap then...!"
        $ greenArms = 1
        hide yellow with d3
        hide red with d3
        with d3
        hide scene_darkening with d3
        pause 0.5
        call qAccept from _call_qAccept_9
        call greenOutfitSet from _call_greenOutfitSet_7
        call yellowOutfitSet from _call_yellowOutfitSet_4
        call redOutfitSet from _call_redOutfitSet_6
        $ task13Name = "Let's have sex already!"
        jump base

    if task13Stage == 1:
        $ task13Stage = 2
        show scene_darkening with d3
        show green g10 at ri with d3
        $ task13Text = _("Sam has begun to open up about sex, but she wants everyone to be prepared.\n\n-Plan a mission to the school and retrieve Sam's notes from her locker\n-Visit the mall and buy an adult video game for Clover from the bookstore.")
        s g37 "Before you ask. No, I'm not going to sleep with you."
        menu:
            "Appeal to reason" if True:
                y "I don't know what to say. Last time I showed you Alex who turned into a freaking monster."
                y "But Apparently that wasn't enough to convince you."
                s g38 "[playerName]..."
            "Bribe (-$100)" if True:
                y "You wouldn't even do it for a Benja-..."
                s g40 "No!{w} I'm not sleeping with you for money! That would make me...!"
                s g11 "............."
                s "Well you know what that would make me...."
            "Say something insane" if True:
                y "Something insane."
                s "...................."
                s g16 "What?"
                y "Sorry... I just felt the urge to say something insane... so I did."
        s g14 "{b}*Sighs*{/b}"
        s "Sex is a big deal for us, you know.... We can't just start sleeping around like this."
        y "By the sounds of it, it's just a big deal for you. The other two seem ready."
        s g31 "They're just faking it..."
        s "Clover might pretend to be this coy little slut, but I'll let you in on a secret~..."
        s g33 "She never made it past second-base."
        y "No!"
        s g23 "{b}*Smirks*{/b} She always says she's gonna do it, but gets cold feet. She's all talk."
        s g15 "And Alex... she doesn't even know what sex is. She thinks everything is magically going to fade to black and you hear moaning coming out of nowhere."
        y "Like... in a video game...?"
        s "Exactly."
        y "......................."
        s g11 "I know I might sound like the prissy, stuck up bitch of the group, but I'm really just looking out for them."
        y "What about you?"
        s "Well...{w} My relation with sex is difficult..."
        s g15 "I was so desperate for my first-time to be perfect and magical, that I spend too much time preparing."
        s "I read books, did research, made graphs..."
        y "Graphs?"
        s "I spend so much time preparing, that I didn't actually get around to 'doing'."
        s "But it's not just that..."
        y "...?"
        s g14 "WOOHP recruited us when we were very young."
        s "Long story short. We pretty much have to gave up our youth to be spies. Which we happily did, of course."
        s "But..."
        s g43 "I wasn't ready to give up my first time for WOOHP aswell..."
        y "............................"
        s "I know it's silly of me. And I know the risks involved by {i}'not'{/i} doing it.{w} It's just this one little thing in my life that I wanted to decide for myself."
        s "Not WOOHP. Not my overly controlling parents. Nobody, but me...."
        s g5 "................................."
        y "Then maybe we shouldn't do it..."
        s "But we should...{w} You heard Clover, the nanobot control is getting worst day by day."
        s g19 "We just have to do a little preparing... All three of us.{w} Do you think that's okay...?"
        y "Of course, Sam.{w} What do you need?"
        s "Well I've got some ideas..."
        s g38 "I'd like Alex to watch some porn, straight up."
        y "Er..."
        s "She has to know exactly what she's getting herself into."
        s "As for Clover... There this video game I saw at the mall a few days ago. I'd like you to buy it for her."
        y "And you?"
        s g33 "And for me... Well, I kept my notes in my locker. They should still be at school."
        y "Porngame from the mall, research notes from the school and where do we get the porn for Alex...?"
        s g18 "....................."
        s "Er...."
        s "We have internet connection."
        y "Wait....."
        y "You can see porn on the internet?! Why did nobody tell me?! A new world has opened up to me!"
        s g1 "Just don't forget to visit the mall and plan a mission to the school for my notes."
        s "Once we have that...."
        s g19 "Erm... I guess then we can go and do {i}'it'{/i}."
        y "All right, let's do it."
        "You spend a little more time talking to Sam before heading to bed."
        hide green with d3
        hide scene_darkening with d3
        $ task13Name = "Let's have sex already!"
        jump nightCycle

    if task13Stage == 3:
        $ task13Stage = 4
        show scene_darkening with d3
        show green g32 at ce with d3
        y "I think I got everything."
        s "Okay, I'll call the others."
        hide green with d3
        "Sam leaves for the cells and returns with Alex and Clover a moment later."
        show green g32 at ce with d3
        show red r35 at le with d3
        show yellow y1 at ri with d3
        c "What's this all about, Sam?"
        s "............................"
        s "We gotta talk about sex..."
        a y29 "Sex...?"
        c r24 "Oh, have you changed your mind?"
        s "[playerName]..."
        y "I got something for you three to check out."
        "You give Clover the game, Sam the notes and look up a porn website for Alex."
        y "Here..."
        a y1 "Oh! An internet video? Is it about funny cats?!"
        a ".........................."
        a y30 "It's... it's not about cats..."
        c r16 "A video game?"
        c "{b}*Scoffs*{/b} I don't need that! I know all about sex!"
        s g13 "And my notes. Good, I'll make sure to study these!"
        a y29 "Ooooh.... so that goes in there~..."
        c r38 "This is ridiculous..."
        y "You three go prepare yourself. Once I'm confident that you three know what you're doing, we're getting together again."
        "The three girls sorta awkwardly shrug and head to their cells."
        hide red
        hide green
        hide yellow
        with d3
        pause 1.0
        y "I should check with them tomorrow and see how they react."
        "Inner Voice" "That's quite a lot of hoops to jump through before getting any..."
        y "Hey, don't judge me! You're living for free in my head, don't make me evict you!"
        "Inner Voice" "Hah! Good luck!"
        hide scene_darkening with d3
        jump nightCycle

    if task13Stage == 4:
        $ task5Nudes = True
        $ sexAct4 = "Sex"
        $ slutLevel = 4
        $ task13Stage = 5
        show scene_darkening with d3
        show green g1 at ce with d3
        s g1 "............"
        show yellow y1 at le with d3
        a "Hiya, [playerName]!"
        show red r19 at ri with d3
        c "......"
        y "Did you all have time to prepare?"
        s g1 "Yes! I've read and re-read all my notes. I'm ready!"
        a y29 "I stayed up all night watching porn!"
        c r14 "Well... I played your game and..."
        c "................"
        c "Well I'm not sure why it was a sci-fi game set in space with glowing swords and orange bimbos..."
        c "But I think it prepared me to have sex...{w} somehow..."
        y "Well then..."
        y "Sex?"
        "All three of the girls give a determined nod."
        pause 0.3
        show scene_fighting with d3
        pause 0.4
        "The girls have taken their next step in suppressing their nanobots."
        "You can now ask them to have sex in their cells. On top of that, you will occassionally see them going down on each other in their cells."
        hide scene_fighting with d3
        y "Then it's decided! I'll visit your whenever."
        hide green
        hide red
        hide yellow
        with d3
        pause 0.8
        "Inner Voice" "Duuuuuuuuuuude! You scored some Grade A ass! And you didn't even have to emotionally guilt trip them into it!"
        "Inner Voice" "If I wasn't a disembodied voice in your head, I'd high-five you."
        hide scene_darkening with d3
        pause 0.5
        call qCompleted from _call_qCompleted_6
        jump base


        s g18 "You have a point though... We're not defeating WOOHP by doing this half way. Maybe we should go all in...."
        y "Are you saying we should go in....{w} balls-deep?"
        s g11 "........................."
        s g2 "I heh~... I guess I am..."
        y "Seriously?"
        s g1 "If you keep giving us nanobot injections to improve our skills, we are put more and more at risk of turning..."
        s "I guess... I guess it's time for the next step to prevent that from happening..."
        y "So... sex?"
        $ greenBlush = 1
        s g14 "Sex."
        s "I guess... {b}*Gulp*{/b} just come to our cells whenever."
        c r22 "I wouldn't mind if you came by mine first~..."
        hide green
        hide red
        hide yellow
        with d3
        pause 1.0
        "Inner Voice" "Duuuuuuuuuuude! You scored some Grade A ass! And you didn't even have to emotionally guilt trip them into it!"
        "Inner Voice" "If I wasn't a disembodied voice in your head, I'd high-five you."
        hide scene_darkening with d3
        jump base

default task14Stage = 0
default task14Name = ""
default task14Text = ""

screen task14Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task14Text]"

label task14:
    if task14Stage == 0:
        show scene_darkening with d3
        ""

default task15Stage = 0
default task15Name = ""
default task15Text = ""
image task15TextStripe1 = "gui/stripe1.png"
image task15TextStripe2 = "gui/stripe2.png"
image task15TextStripe3 = "gui/stripe3.png"
image task15TextStripe4 = "gui/stripe4.png"
default task15Music = False
default task15Fireworks = False
default task15Girls = False

label task15HireSluts:
    menu:
        "Aces Party Sluts ($1.000)" if True:
            if cash <= 1000:
                y "I don't have enough money for this."
            elif True:
                $ cash -= 1000
                $ task15Girls = True
                play sound "audio/sfx/itemGot.mp3"
                "You hired a bunch of college girls to join the Aces party."
            jump worldmap
        "Never mind" if True:
            jump worldmap

screen task15Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task15Text]"

    if task15Fireworks:
        hbox:
            spacing 10 xalign 0.5 ypos 235 xsize 770
            add "gui/stripe1.png"
    if task15Music:
        hbox:
            spacing 10 xalign 0.5 ypos 300 xsize 770
            add "gui/stripe2.png"
    if task15Girls:
        hbox:
            spacing 10 xalign 0.5 ypos 331 xsize 770
            add "gui/stripe3.png"
    if cash >= 2000:
        hbox:
            spacing 10 xalign 0.5 ypos 367 xsize 770
            add "gui/stripe4.png"

label task15:
    if task15Stage == 0:
        $ task15Name = _("Party till you drop")
        $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n\n-Plan a mission to the Amusement Park for fireworks.\n-Plan a mission to Punk Web and steal the hottest mixtape.\n-Pick up some thots at school.\n-Have at least $2.000.")
        $ task15Stage = 1
        scene bgBar with fade
        pause 0.6
        show scene_darkening with d3
        show green g15 at ri with d3
        s "...................."
        y "What's wrong?"
        s g14 "It's the Aces..."
        s "Things aren't the way they used to be. With their lieutenants locked up, the excitement and high energy in the gang is gone..."
        s "No more parties, everyone just keeps to themselves. It's as if they know the gang doesn't have much life left."
        y "Which is good, right?"
        s g12 "Yeah I guess. A gang with poor morale should be easier to take down."
        s "I'm just feeling a bit nostalgic. I miss how things used to be."
        y "What about the leader of the Aces?"
        if specialCandyStatus >= 1:
            s "Oh you mean Candy? She's as tough as ever."
            s "She's cautious of me. Afterall, her lieutenants have gone missing and she knows who I am. Me and the girls have fought her before."
        elif True:
            s "Whoever is leading the Aces is not showing any signs of weakness."
            s "We'll have to send some more freed WOOHP agents to attack the Aces during the next Landgrab to find out who they are."
        s g10 "I think that as long as the Aces are in a rut, they'll be less of a threat."
        s "But if we can boost their morale, and make them think they're still on top, they could make mistakes."
        y "And we could use those to capture their leader..."
        y "What did you have in mind?"
        s g14 "Erm...."
        y "Yes...?"
        s g1 "I was thinking, let's throw a party. A big one."
        s "That would improve their morale and hopefully get me in the good graces of the leader."
        s g38 "Then when noone suspects a thing, we'll nab them! After that the gang will most likely disband."
        y "And you're okay with that...?"
        s g15 ".............................."
        s g14 "Things have to get back to normal... and they won't with the Aces still around."
        s "I'm gonna miss the lifestyle, but for the sake of Beverly Hills... let's do it."
        y "All right. Party it is!"
        y ".............................."
        y "Er.... what do we need?"
        s g1 "Well first off, we need a place to host it."
        y "The Milkshake bar?"
        s "Exactly. Second we'll need music."
        s g22 "I'm thinking we steal some from Drift Punk as a sign of Aces dominance."
        y "Okay... so plan a mission to Punk Web. What else?"
        s g13 "Fireworks. I'm thinking Outsiders."
        y "Plan mission to Abandoned Amusement park... Anything else?"
        s g14 "Copious amounts of drugs."
        y "Er...."
        s g1 "Don't worry, most of that can be supplied by the Aces."
        s "And finally...."
        y "WHORES AND BLACKJACK!"
        s g29 "Well... yes actually."
        y "Really?"
        s g1 "It's a party. Better go all out."
        s "I bet we can pick up some girls who are interested at the school."
        y "Pick up some thirsty college sluts. Got it."
        y "So... how are we gonna pay for all this?"
        s "I think I can convince the Aces to pay for most of it."
        s "We just gotta worry about the initial payment. Let's say... $1.000?"
        y "Okay so we'll need..."
        y "Music from Punk Web\nFireworks from the Abandoned Amusement Park\nSlutty college girls from the school.\nA budget of 1.000 dollars."
        s "Yup, that's bound to put me in good graces with the gang."
        y "Let's do it then."
        hide green with d3
        hide scene_darkening with d3
        pause 0.8
        call qAccept from _call_qAccept_10
        pause 0.7
        scene bgMap:
            zoom 0.5
        with d3
        jump worldmap
    if task15Stage == 1:
        hide screen nanoLevelSam
        hide screen nanoLevelClover
        hide screen nanoLevelAlex
        call undressSam from _call_undressSam_28
        call greenOutfitSet from _call_greenOutfitSet_9
        $ cash -= 1000
        $ task15Stage = 2
        show scene_darkening with d3
        show green g1 at ri with d3
        y "Okay, I think we have everything we need."
        s "I've already sent word to the Aces! This is gonna be the best party ever!"
        $ redChest = 2
        $ redUnder = 0
        $ redBottom = 2
        $ redShoes = 2
        $ redHead = 0
        $ redOutfit = 0
        $ redOutfitArms = 0

        $ yellowChest = 2
        $ yellowUnder = 0
        $ yellowBottom = 2
        $ yellowShoes = 2
        $ yellowHead = 0
        $ yellowOutfit = 0
        $ yellowOutfitArms = 0
        show red r35 at ce
        show yellow y29 at le
        with d3
        c "Ready as we'll ever be."
        a "I hope they don't ask us to show our underwear..."
        y "Well..."
        a y28 "Cause I'm not wearing any!"
        y "...................."
        "The girls seem ready."
        hide green
        hide red
        hide yellow
        with d3
        stop music fadeout 3.0
        scene black with longFade
        "You get everything ready and soon the Aces come in one by one."
        play music "audio/music/club.mp3" fadein 2.5
        scene bgBarAces with fade
        show disco
        pause 1.0
        "Aces Gangster 1" "Dude, check out the fireworks!"
        "Aces Gangster 2" "No way, I'm dancing to the best beats in town!"
        "Aces Gangster 3" "Who cares about dancing when you're surrounded by the hottest girls in Beverly Hills?!"
        "Aces Gangsters" "Three cheers for Sam!"
        pause 1.0
        $ greenBlush = 1
        show scene_darkening with d3
        show green g22 at ri with d3
        pause 0.3
        y "Hey there [samNick], looks like your party is a success."
        play sound "audio/voice/yeah2.mp3"
        s "Heh~... yeah!"
        y "Easy on the booze there..."
        s "Aw just relax. It's a party! Maybe the last one the Aces will ever have!"
        s g13 "Grab a drink!"
        $ yellowChest = 0
        show yellow at le with d3
        a "This is fun!"
        y "Alex! Where's your top?!"
        a "I lost it in a game of rock-paper-scissors!"
        show red r22 at ce with d3
        c "Not gonna lie... this 'is' a pretty great party."
        s g1 "C'mon [playerName]. Just one drink~..."
        y "Oh well, I guess one can't hurt."
        hide green
        hide red
        hide yellow
        with d2
        "You make your way over to the bar and get a drink....{w} Or two...{w} Maybe three."
        scene black with fade
        "You doze off~..."
        pause 3.0
        scene bgBarAces with fade
        show disco
        y "Ugh~... how long was I out for... {b}*Hic...!*{/b}"
        "Off to the end of the club you see Alex dancing naked on a table!"
        a "Strip teeeeeease.....!"
        show red r22 at ce with d3
        c "You okay there, [playerName]?"
        y "Still fully dressed...?"
        c r24 "Not for long~... I think I'll join Alex. ♥"
        hide red with d3
        y "..........................."
        y "Where did Sam go?"
        "You decide to head outside for some fresh air."
        stop music fadeout 1.5
        scene black with fade
        scene bgStreet1
        show bgNight
        with fade
        pause 2.0
        "???" "It's been a long time, hasn't it?"
        s "Yes... it has..."
        y "...?"
        pause 0.6
        $ greenBlush = 0
        show timModel at ce
        show green g48 at le
        with d10
        s "Heh~... never expected we'd be working together..."
        tim "Yeah..."
        tim "How've you been, Sam?"
        s "Well... you know..."
        s g5 "........................"
        s "I've been okay..."
        tim "....................."
        tim "Just hang in there..."
        tim "I know you're not completely yourself right now, but we're taking WOOHP down for a good reason."
        s "Yeah...."
        tim "......................"
        tim "You don't have to believe me. It's fine."
        tim "You'll see that we did the right thing once that organization is gone."
        s "But....!"
        tim "The gang violence was an unfortune side-effect, but the city will recover."
        s "...................................."
        tim "....................................."
        tim "I missed you, Sam..."
        s "Don't say that..."
        s "We're enemies, remember?"
        tim "Not for long. When WOOHP is gone, I'd like us to try again... {w}for real this time."
        s "........................."
        s "Me too..."
        tim "It's getting cold, let's go back inside."
        pause 0.5
        "The two are coming your way!"
        tim "...?"
        tim "Agent."
        menu:
            "Salute" if True:
                "You quickly stand aside and salute."
                y "Mr. Scam."
                tim "Lay off on the alcohol. You don't want to get too toasty with these gangsters."
                y "Of course, sir!"
            "Nod" if True:
                "You simply nod and turn the other way."
                tim "...?"
                s g56 "C-come on, Tim. Let's get back inside."
            "Say something crazy" if True:
                y "All it well sir, no incidental petrol trucks in sight."
                tim "What...?"
                y "The chance that this party will go up in flames and we'll all die in a fiery explosion is less than 10%%, sir!"
                tim "That's... good to know..."
                s g56 "C-come on, Tim. Let's get back inside."
        hide green
        hide timModel
        with d3
        pause 0.5
        y "......................."
        a "WOOOOOO!"
        "You suddenly see Alex running out holding a T-shirt!"
        call undressAlex from _call_undressAlex_6
        $ redChest = 0
        show yellow y42:
            xalign 1.4 yalign 0.0
            linear 0.5 xalign 0.0
        pause 0.5
        hide yellow with d1
        c "Alex! Give that back!!!"
        show red r53:
            xalign 1.4 yalign 0.0
            linear 0.5 xalign 0.0
        pause 0.5
        hide red with d1
        pause 0.4
        y "Welp... looks like it's a party. Better get back inside."
        scene black with fade
        pause 1.0
        play music "audio/music/club.mp3" fadein 2.5
        "The rest of the night is filled with drinking, partying and lots of naked boobs."
        stop music fadeout 3.0
        jump nightCycle
    if task15Stage == 2:
        $ task15Stage = 3
        $ task15Name = _("Party till you drop (Completed)")
        $ task15Text = _("With the party of the century done, we're one step closer to winning the trust of the Aces leader. All we have to do now is increase our reputation a bit more and hopefully take them down.")
        pause 1.0
        scene bgBar with fade
        show scene_darkening
        show red r15 at le
        with d3
        c "Uuuugh~..."
        y "Good morning."
        c "UUUUUGHH~...."
        show yellow y14 at ce with d3
        a "My head hurts~...."
        show green g33 at ri with d3
        s "Oooof~..."
        s g1 "Good morning guys."
        c "How can you be so chipper...?"
        s g55 "I guess I just didn't drink as much."
        s "What about you two? Do you remember last night?"
        a y12 "It's fuzzy...."
        c r57 "We didn't do anything crazy, did we?"
        s g56 "You....{w} er... you ended up stripping naked and making out with each other as the crowd watched."
        c r14 ".........................."
        a y28 ".........................."
        a "No wonder I can taste your cherry chapstick, Clover!"
        c "I'm going to pretend I didn't hear that.{w} If you need me, I'll be in bed..."
        hide red
        hide yellow
        with d3
        pause 0.5
        y "Looks like your party was a success."
        s g2 "Heh~..."
        s "I've checked my phone and its blown up with messages from the Aces."
        $ acesRep += 4
        call missionRewardRep from _call_missionRewardRep_20
        s "You could say I'm pretty hot right now..."
        if specialCandyStatus >= 1:
            s g1 "I even got a message from Candy, their leader."
            y "Who is this Candy anyways?"
            s "Candy Sweet. Real name is Margaret Nussbaum."
            y "Continuing the crazy last name trend I see..."
            s g32 "She used to be a cheerleader coach, but ended up specializing in hypnosis and brainwashing."
            s "I'm guessing her experience training ditzy rich girls, combined with her talent for brainwashing made her the perfect leader for the Aces."
        y "So... Tim Scam was at the party yesterday."
        s g30 "{b}*Gulp*{/b}"
        s "Y-yeah... he was..."
        y "Something I should worry about?"
        s g33 "No... Don't worry, I'm still going to help bring him down..."
        y "............."
        hide green
        hide scene_darkening
        with d3
        call qCompleted from _call_qCompleted_7
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap

default task16Stage = 0
default task16Name = ""
default task16Text = ""

screen task16Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task16Text]"

label task16:
    if task16Stage == 0:
        $ task16Stage = 1
        $ candyHidden = False
        scene bgBar with d3
        show scene_darkening with d3
        show green g29 at ri with d3
        s "I just got an invitation from the Aces leader to come see her!"
        s "She couldn't say what it was about, but I'm suppose to meet her in Spain."
        y "You're building up some serious frequent flyer miles."
        s g1 "Yeah I know. Valencia is well worth visiting though."
        y "We've taken great strides in taking her down, but the fact that she wants to meet you alone makes me a bit worried."
        y "I'll put the other spies on stand-by just in case."
        s g32 "That's not a bad idea. I've never actually interacted with Candy. If you don't count the times we fought her in the past."
        y "You think it's a trap?"
        s g31 "Only one way to find out..."
        hide green with d3
        "Sam gets ready to leave for Spain."
        pause 0.5
        show yellow y32 at le
        show red r32 at ri
        with d3
        y "Girls, we got a big mission planned. Sam is heading to Spain again to meet with the leader of the Aces."
        y "You're going in after her. Stay to the shadows and only interviene if something goes wrong."
        c r31 "Right."
        $ spy1Status = 10
        $ spy2Status = 10
        $ spy3Status = 10
        $ mapSpy1Selected = False
        $ mapSpy2Selected = False
        $ mapSpy3Selected = False
        hide red
        hide yellow
        with d3
        hide scene_darkening with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task16Stage == 2:
        $ task16Stage = 3
        $ candyHidden = False
        "{b}*Beep* *Beep* *Beep*{/b}"
        show scene_darkening with d3
        cM "[playerName]? We landed in Spain. Sam is already on her way to the Aces head quarters."
        y "Good, keep an eye on her. Is Alex there with you?"
        aM "Hiya!"
        y "Keep me up to date."
        hide scene_darkening with d3
        pause 1.5
        "{b}*Beep* *Beep* *Beep*{/b}"
        show scene_darkening with d3
        sM "[playerName] I'm going in. I'll keep the line open."
        hide scene_darkening
        scene bgCastle
        show scene_darkening
        with fade
        pause 0.5
        show scene_darkening with d3
        show green g55 at le with d3
        $ candyFace = 2
        show candyModel at ri with d3
        "???" "Ah Sam, you made it..."
        s "Candy! It's good to see you!"
        candy "Likewise. I heard you did a lot of good work for the Aces."
        s g57 "Yeah.... listen Candy about before..."
        $ candyFace = 3
        candy "Before? You mean how you girls busted my ass all those years ago?"
        s "..................."
        candy "Water under the bridge. I'd rather have you on our side than as my enemy."
        $ candyFace = 2
        candy "You are on our side, right?"
        s g56 "Of course!"
        candy "Well I'll let your actions speak for themselves.{w} Now it's time we had a little chat..."
        s g57 "A little... chat?"
        stop music fadeout 1.5
        play sound "audio/sfx/static.mp3"
        show scene_static1
        pause 0.4
        hide scene_static1
        pause 0.4
        show scene_static2
        pause 0.4
        hide scene_static2
        pause 0.6
        show scene_static3
        pause 2.0
        y "What the...?"
        y "Girls, I lost connection with Sam! Switching to your camera now."
        stop sound fadeout 3.0
        hide scene_static3
        play music "audio/music/stealth2.mp3" fadein 2.5
        scene black
        with fade
        pause 0.1
        $ missionSetting = "Castle"
        $ randomBackground = 1
        $ missionScreenFrontlineSelect = 2
        $ missionScreenSupportSelect = 3
        $ missionProgression = 0
        show globalImageCastle:
            zoom 0.25
        hide screen interactScreen
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        $ randomExit = 1
        $ currentPosition = 0
        $ randomCover2 = 1
        $ randomCover1 = 1
        $ randomBackground = 1
        $ alexOnMission = True
        $ cloverOnMission = True
        $ backupAlexActive = True
        $ activeSpy = 2
        $ hiddenStatus = 2
        show scene_darkening with d3
        "Intercom: Intruder warning! Switching to high alert."
        y "They know we're here..."
        y "We lost contact with Sam. Fight your way through the castle and get her out of there!"
        cM "Right!"
        hide scene_darkening with d3
        $ specialCandyStatus = 1
        $ specialBossActive = True
        $ randomBossHP = 3
        $ randomBoss = 0
        jump jumpStartScene
    if task16Stage == 4:
        $ task16Stage = 5
        scene black with fade
        stop music fadeout 1.5
        hide globalImage
        hide screen interactScreen
        hide screen equipmentMenu
        scene bgCastle with fade
        show scene_darkening with d3
        show green g15 at ri
        show yellow y57 at le
        show red r56:
            xalign 0.35 yalign 0.0 xzoom -1
        with d3
        $ _skipping = True
        play  music "audio/music/ambient1.mp3" fadein 1.5
        a "Sammy! Are you all right?!"
        s g14 "Y-yeah... I'm fine.{w} We walked right into her trap."
        c r54 "This ends now. With Candy defeated, the Aces will have lost all of their leaders. We'll be rid of the gang once and for all."
        hide green with d3
        $ candyFace = 4
        show candyModel at ri with d3
        candy "{b}*Pant* *Pant*{/b} {w}It seems we've been here before...."
        a y53 "Give up Candy! We're taking you back to prison!"
        candy "That's what you think..."
        candy "*{b}Crack{/b}*"
        hide candyModel with d3
        c r56 "Candy...?"
        "Suddenly the gang boss drops to the ground."
        y "It's a suicide tooth! Quickly help her!"
        s "Candy!"
        scene black with fade
        "The girls tackle Candy and after a short struggle, manage to help her before she ingests too much of the poison."
        show bgCastle
        show scene_darkening
        with fade
        show red at le with d3
        c r14 "She's okay..."
        y "What on earth did WOOHP do to her to make her choose death over imprisonment?!"
        c r32 "I don't know... The poison knocked her out, let's get her back to Beverly Hills."
        y "We can treat her back at the base. You girls head back home."
        "Battered, but victorious, the girls nod and return back to America."
        stop music fadeout 2.5
        scene black with longFade
        pause 0.7
        scene bgBase with fade
        y "Welcome back girls."
        show scene_darkening with d3
        show red r34 at le
        show green g21 at ce
        show yellow at ri
        with d3
        play music "audio/music/nighttime.mp3" fadein 1.5
        s "Margaret regained consciousness during the trip. We put her in one of the cells, but it's not likely she'll cooperate."
        c "Talk to her whenever you have time, [playerName]. She might be able to tell us more about the Mastermind."
        y "Good work girls. Head back to your cells for now."
        hide red
        hide yellow
        with d3
        pause 0.5
        y "Are you all right, [samNick]?"
        s g5 "Yeah... the news of Candy's arrest will spread and the Aces should disband soon..."
        y "No more living the high-life."
        s "Yeah... which is probably a good thing. Thanks for coming to help me, [playerName]."
        y "Don't mention it."
        $ specialCandyStatus = 2
        $ prisonersNew = True
        hide scene_darkening
        hide green
        with d3
        jump base
    if task16Stage == 5:
        $ task16Stage = 6
        show scene_darkening with d3
        y "Are you awake...?"
        $ candyFace = 5
        show candyModel at ri with d3
        candy "I am... let's just get it over with..."
        y "Over with?"
        candy "Don't play coy with me! I remember the last time you captu-....{b}*cough* *cough*{/b}"
        y "Easy there. We nearly lost you to your little stunt. Who still uses suicide teeth now a days?"
        y "................"
        y "Oh right, I work for a spy agency."
        candy "Stop joking around! I know what you're planning!"
        show green g16 at le with d3
        s "How is she doing?"
        y "Well she's awake, but she seems to know I'm gonna bone her."
        s g28 "What?"
        $ candyFace = 6
        candy "What?"
        y "..........."
        y "What?"
        y "That's what you were talking about, right?"
        $ candyFace = 4
        candy "!!!"
        candy "I was talking about the torture!"
        y "Torture? Nobody's getting tortured!"
        candy "Don't lie to me agent. I've already gone through it once when your spies captured me the first time!"
        y "............................"
        y "Sam~...."
        s g29 "I... I don't know what she's talking about!"
        candy "Stop playing games! I know what your organization is really about!"
        candy "Why do you think I was so desperate to take revenge?!"
        s g31 "Don't listen to her, [playerName]. WOOHP doesn't torture its prisoners."
        candy "Of course it does! Why do you think this whole operation got started?! Why do you think all of us want to take revenge so badly?!"
        candy "You even turn on your own friends and allies! That's why she organized this whole take-over."
        s g16 "She?"
        y "The Mastermind is a woman?"
        candy "I've said enough... You won't get a word out of me."
        s "She doesn't seem to be nanobot controlled, [playerName]..."
        y "Yeah... I think it's best if we just leave her be."
        candy "........................................"
        hide scene_darkening
        hide green
        hide candyModel
        with d5
        pause 1.3
        show scene_fighting
        with d5
        "Computer" "Computer: Candy Sweet.\nStatus: Captured."
        "Computer" "Transferring funds..."
        $ cash += 2000
        $ randMoney = 2000
        call missionRewardMoney from _call_missionRewardMoney_84
        pause 0.4
        hide scene_fighting with d3
        "New clothing options for Sam are available at the mall."
        scene bgBase with fade
        pause 0.6
        show green g31 at le with d5
        show red at ce with d5
        show yellow y14 at ri with d5
        pause 0.5
        y "Well... that was interesting."
        s "Don't listen to anything she has to say, [playerName]. She's obviously trying to get to us!"
        a "WOOHP doesn't really torture its prisoners, right...?"
        s g38 "Of course not! It even says so in the WOOHP guidelines."
        c r11 "The guidelines also say that WOOHP doesn't interfere with civillians and we know that's not true. The fact that we're spies is proof of that."
        y ".............................."
        c r10 "What?"
        y "Sam... do you remember when we just moved in here and we checked out the basement...?"
        s g30 "!!!"
        s "Oh no..."
        y "Seems WOOHP might be into some much darker stuff than we thought."
        s "No, Jerry would never allow that!"
        a y38 "Exactly! The bad guys must just be lying to us!"
        y "..........................."
        y "We'll figure it out when we free your boss."
        $ tod = 2
        hide green
        hide red
        hide yellow
        with d3
        scene bgMap:
            zoom 0.5
        show expression "gui/mapGangs/gangRepGraphic.png":
            xpos 120 ypos 130
        show text "{font=fonts/freshmarker.ttf}{size=+20}Aces{/size}{/font}":
            xpos 285 ypos 222
        show expression "gui/mapGangs/acesLt1Cap.png":
            xpos 225 ypos 300
        show expression "gui/mapGangs/acesLt2Cap.png":
            xpos 275 ypos 300
        show expression "gui/mapGangs/acesLt3Cap.png":
            xpos 330 ypos 300
        with longFade
        play sound "audio/sfx/defeatGang1.mp3"
        pause 2.5
        show expression "gui/disbanded.png" at disbanded:
            xpos 210 ypos 190
        play sound "audio/sfx/defeatGang2.mp3"
        pause
        scene bgBase with longFade
        $ specialCandyStatus = 3
        $ gang1Active = False
        jump base

default task17Stage = 0
default task17Name = ""
default task17Text = ""

screen task17Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task17Text]"

label task17:
    if task17Stage == 0:
        $ spy2Status = 1
        $ mapSpy2Selected = False
        $ redDayJob = 2
        $ task17Name = _("Animo...")
        $ task17Text = _("Clover is struggling with going undercover with Drift Punk. I should send her out a few more times to see if things improve.")
        $ task17Stage = 1
        scene bgBar with fade
        pause 0.4
        show scene_darkening with d3
        show red r30 at ri with d3
        c "[playerName] you gotta help me!"
        y "What? What's wrong?"
        c "It's Drift Punk... Some of them have invited me over to play games and watch animo with them!"
        y "That doesn't sound too b-..."
        c "I don't know how to play video games!{w} And I have no idea what animo is!"
        y "Just relax. I'm sure they'll explain everything once you get there."
        c "Ugh... I just know that I'm going to hate this..."
        hide red with d3
        hide scene_darkening with d3
        pause 0.3
        call qAccept from _call_qAccept_11
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task17Stage == 1:
        $ task17Stage = 2
        pause 0.4
        show scene_darkening with d3
        show red r38 at ri with d3
        c "I'm back..."
        y "Had a fun time with the Punks?"
        c r17 "Don't even get me started! It was awful!"
        c r42 "They made me watch Japanese cartoons and play these awful games!"
        y "That doesn't sound so bad."
        c r16 "I mean... It's better than robbing banks, but it was just so nerdy~...!"
        c r11 "..................."
        c "At least some of the game characters looked cool..."
        c r12 "Of course they had to make it weird and said one of the characters looked like me."
        y "Remember, you're undercover. At least pretend to be interested in them."
        c r42 "{b}*Whines*{/b} But one of them showed off his D20 collection!"
        y "D20?"
        c r29 "Er... I mean his dice collection...{w} You know, for playing nerd games."
        y "You poor thing. Okay head back to your cell for now. You're going back tomorrow."
        "Clover nods and returns to her cell."
        hide red with d3
        hide scene_darkening with d3
        pause 0.3
        call qUpdated from _call_qUpdated_8
        jump nextReport
    if task17Stage == 2:
        $ task17Stage = 3
        pause 0.4
        show scene_darkening with d3
        show red r39 at ri with d3
        c "{b}*Grumbles*{/b}"
        y "Uh oh..."
        c "They made me watch anime again..."
        y "Anime?"
        c r12 "Those Japanese cartoons I told you about."
        y "And...?"
        c "I don't know. I was zoning out half of the time."
        c "Something about a magical cat girl or something..."
        c "We also played this tabletop game with miniatures."
        c r10 "............................"
        c "Are you gonna send me back there again...?"
        y "That's the plan."
        c r11 "...................."
        hide red with d3
        hide scene_darkening with d3
        pause 0.3
        jump nextReport
    if task17Stage == 3:
        $ task17Stage = 4
        pause 0.4
        show scene_darkening with d3
        show red r10 at ri with d3
        y "Still watching your animos?"
        c "It's anime...{w} and yes... we're still watching those..."
        y "I'm sorry for putting you through all that."
        c r12 "It...{w} It's fine..."
        y "I mean... having a girl like you play video games and read Japanese comics. It feels almost sadistic of me!"
        c r11 "................"
        y "Putting a Valley girl in a situation like that! Surrounded by strange hobbies and foreign cartoons!"
        y "Okay, I've made up my mind! No more Drift Punk missions. From now on I'll just send you undercover somewhere else."
        c r28 "W-wait... what?"
        y "I know how much you dislike nerdy stuff, so I promise to not send you out there anymore."
        c r30 "N-no...{w} We have to think of the mission...!"
        c r29 "Heh~... Heh~... maybe I was just overreacting a bit...{w} Obviously taking down Drift Punk is much more important. So you can keep sending me undercover there."
        y "...?"
        c r38 "It's a big sacrifice, but I'm willing to make it! For the greater good and for my friends!"
        y "For your friends...?"
        y "Well if you're that dedicated, then I guess I'll send you undercover with them again..."
        c r1 "R-right...!"
        "Clover grabs her things and returns to her cell."
        hide red with d3
        hide scene_darkening with d3
        pause 0.4
        y "...................."
        y "Well that was a little suspicious..."
        jump nextReport
    if task17Stage == 4:
        $ task17Stage = 5
        $ task17Text = _("The more I send Clover undercover with Drift Punk, the stranger she's behaving. For now, I should continue to send her there to see if anything comes from it.")
        pause 0.4
        show scene_darkening with d3
        show red r1 at ri with d3
        y "Clover, welcome back. How did your undercover mission go with Drift Punk?"
        c "Oh! Y-yeah it went great.{w} Y'know... gathered some intel, robbed some bankaccount... the usual..."
        y "Are you hiding something behind your back...?"
        c r30 "N-no! Of course n-..."
        play sound "audio/sfx/lootbox.mp3"
        with hpunch
        "Clover dropped something on the ground."
        y "Are these... sewing manuals?{w} And anime figurines...?"
        c r28 "It's not what it seems!"
        y "I don't even know what it seems!"
        c r29 "I just f-figured I'd do some extra research on Drift Punk culture, you know. So I can more easily talk to them about their hobbies and interests!"
        y "And... those hobbies include sewing...?"
        c r18 "........................{w} Yes."
        y ".................................."
        y "Well alright! I see nothing strange about this! Off you go now."
        "Clover quickly grabs her supplies and rushes off to her cell."
        hide red
        hide scene_darkening
        with d2
        jump nextReport
    if task17Stage == 5:
        $ task17Stage = 6
        $ task17Text = _("The more I send Clover undercover with Drift Punk, the stranger she's behaving. For now, I should continue to send her there to see if anything comes from it.\n\n-Send Clover undercover to Drift Punk and follow her.")
        pause 0.4
        show scene_darkening with d3
        show red r19 at ri with d3
        y "Welcome back C-....{w} What's with that look?"
        c "Can.... can I borrow $100 bucks from you?"
        y "What for...?"
        c "................."
        c "I... er..."
        c "I need to buy some fabrics..."
        y "Fabrics...? What do you need fabrics for...?"
        c r15 "Well I er... actually never mind! I just remembered that I still have enough. Sorry!"
        y "Clover, what are y-...?"
        hide red with d2
        play sound "audio/sfx/cloth.mp3"
        with hpunch
        "Quickly hurried to her cell, but dropped something along the way."
        y "Clover! You dropped your....{w} skirt?"
        y "What's that girl up to....? Maybe I should follow her next time she goes undercover with Drift Punk..."
        hide scene_darkening with d3
        call qUpdated from _call_qUpdated_9
        jump nextReport
    if task17Stage == 6:
        $ task17Stage = 7
        $ task17Text = _("Turns out, Clover is a closet nerd who loves dressing up as her favorite anime and video game characters.")
        $ task17Name = _("Animo... (Complete)")
        cM "Okay, I'll be heading off to the Punks again today!"
        "Clover heads off to the Dift Punks."
        pause 1.0
        y "......................................"
        y "(What are you up to, Clover~....)"
        show bgStreet2 with fade
        pause 1.0
        show red r55:
            xalign 1.1 yalign 0.0 xzoom -1
        with d3
        c "......................................"
        hide red with d5
        pause 0.5
        y "She went into the convention building..."
        scene bgStreet1
        show scene_darkening
        with fade
        pause 0.5
        y "....?"
        y "What the...?"
        "Nerdy Guy" "Season two was {i}so{/i} much better."
        "Nerdy Girl" "Oh please, the quality went down so much after they outsourced the animation to a different company!"
        y "Is this....?"
        "Gamer" "Have you heard about the sequal to the game?"
        "Gamer" "I hear it's going to have jiggle physics!"
        y "It's an anime convention...!"
        y "What is Clover doing here...?"
        scene black
        hide scene_darkening
        with fade
        $ redHair = 6
        $ redChest = 16
        $ redBottom = 16
        $ redShoes = 16
        $ redAcces1 = 16
        $ redHat = 16
        $ redUnder = 0
        $ redNeck = 16
        "You begin looking around for your spy."
        scene bgStreet1
        show scene_darkening
        with fade
        pause 0.5
        show red r30 at ri with d3
        y "Excuse me miss. Have you seen a blonde girl around here? About your height, your eye color, your posture, you're...."
        y "........................"
        y "Clover...?"
        c r28 "Er...! N-no I'm not Clover~....!"
        y "You're into anime?!"
        c r14 "Shhh! Not so loud!"
        c "..............."
        c r15 "{b}*Sighs*{/b} Well.... you caught me."
        y "Clover, what are you doing here...? Aren't you suppose to be undercover with Drift Punk?"
        "Taking off her wig and mask, Clover embarrassingly looks at you."
        hide red with d2
        $ redHair = 4
        $ redBlush = 1
        $ redAcces1 = 0
        $ redHat = 15
        show red r5 at ri with d2
        c "............................."
        c "I... sorta ditched undercover work to come here..."
        y "I thought you hated nerd stuff...?"
        c "Well... that wasn't completely true...{w} actually... I kinda...{w} love it..."
        c r42 "Drift Punk introduced me to this whole new world and... and well... it's really fun."
        c "B-but it would ruin my reputation if anyone knew!"
        c "Please, [playerName]. Don't tell anyone!"
        y "Not even Sam and Alex?"
        c "No, not even them!"
        menu:
            "Promise not to tell" if True:
                y "Okay... I won't tell. But it's just a hobby. Why do you care so much?"
                c r38 "It would ruin my reputation!"
                y "Your reputation..."
                y "Your reputation with who exactly?"
                c "Everone in my school!"
                y "You don't go to school because of this crisis..."
                c "Then everyone in my social circle!"
                y "Okay that's... Sam, Alex, me and whatever staff we have working at the milkshake bar. We don't care."
                c r30 "T-then... what about the customers? They come from all kinds of backgrounds. They might hate me for being nerdy!"
                y "As long as you show your tits, I don't think they really care."
            "Blackmail Clover" if True:

                y "Well then... looks like someone is going to have to {b}pay{/b} me to keep quiet!"
                c r10 "[playerName] any money we make goes directly to you anyways."
                y "Oh right..."
                y "Then I demand sexual favors!"
                c r14 "{b}*Sighs*{/b} We already give you those aswell, remember?"
                y ".........................."
                y "Er... okay fine. Then do the dishes...."
                c r40 "NEVER!"
                y "And my laundry!"
                c "NOT IN A MILLION YEARS!"
                y "And massage my feet!"
                c r11 "...................."
                c "Yeah okay, that's not worth it. I'm just going to let everyone that I like nerdy stuff..."
                y "Trust me. Most people are too busy with themselves to bother judging you. It's just a hobby."
            "Say something insane" if True:
                y "So... {w}anime."
                c r19 "Yup."
                y "And games?"
                c "Also games."
                y "And tabletop roleplaying games...?"
                c "Also those, yes."
                y ".........................."
                play music "audio/music/sinister.mp3" fadein 4.5
                hide red
                show zukker:
                    xalign 0.5 alpha 0.0
                    linear 18 alpha 1.0
                show red r5 at ri
                y "What about interdimensional worship of lustful deities. Often characterized as lubed up tentacle monsters that at the knowledge of their existance cause insanity?"
                y "A being so vigorous and virtile that you loose your virginity, just by looking at it!{w} With power so great, that it could destroy moons!"
                y "A BEING SO GREAT, THAT IT'S NAME IS ONLY EVER BEING SAID IN WHISPERS! THE ARTIST TRYING TO PAINT IT, GOES INSANE BEFORE PICKING UP HIS BRUSH!"
                hide zukker
                stop music
                play sound "audio/voice/clover/what2.mp3"
                c r16 "W-what...? No, that doesn't sound very nerdy at all!"
                y "Oh..."
                y "So you wouldn't so happen to be interested in joining his cult...?"
                c "No....?"
                y "Oh... okay... just asking for a {i}'friend'{/i}."
                play music "audio/music/daytime.mp3" fadein 5.0
                y "All I'm saying is..."
                y "Nobody cares about what hobbies you enjoy. As long as you show your tits, you'll stay popular."
        c r11 ".............................."
        c "Huh...."
        c r12 "I guess nobody really cares..."
        c r1 "Thanks [playerName]... Maybe I should be myself from now on...."
        c r10 "........................"
        c "I'm going to buy so much junk at this convention!"
        y ".........................."
        hide scene_darkening
        hide red
        with d3
        call qCompleted from _call_qCompleted_9
        pause 0.5
        "New cell decorations are now available for Clover."
        $ redHair = redHairSet
        $ redBlush = 0
        $ cellCloverPoster = 1
        $ cellCloverComics = 1
        $ cellCloverGames = 1
        jump jobReport

default task18Stage = 0
default task18Name = ""
default task18Text = ""
default task18SearchTop = True
default task18SearchMid = True

screen task18Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task18Text]"

label task18:
    if task18Stage == 0:
        $ task18Stage = 1
        $ task18Name = _("Nourishing Beats")
        $ task18Text = _("Send Clover to Drift Punk to get closer to Talia Hardwire.")
        show bgBase with fade
        show scene_darkening with d3
        show red at ri with d3
        $ mapSpy2Selected = False
        $ redDayJob = 2
        $ spy2Status = 1
        c "Okay, on my way to Drift Punk."
        c "There's been some new development with Punk Web so I'll probably spend the day in there."
        y "New developments?"
        c r18 "Yeah, one of the Lieutenant is implementing a patch today so we're going to check it out."
        c r1 "I might even be able to get close to her and score some good-girl points."
        c "If we can get her to trust us, it'd be much easier to capture her."
        y "What do you know about her?"
        c r10 "Well... Talia has a striking resemblance to Telly Hardwire. A hacker we brought down a few years ago."
        c "Seeing as they have the same last name, I'm guessing it's his sister."
        y "It would give her a motive at least. Okay, head out and report back what you find."
        "Clover nods and heads out."
        hide red
        hide scene_darkening
        with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task18Stage == 1:
        $ task18Stage = 2
        $ task18Text = _("Talia has been willing to cooperate, but is afraid that Drift Punk will come after her. We just have to get her out and make it seem believable.\n\n-Plan a mission to Punk Web and capture Talia Hardwire.")
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ redDayJob = 0
        $ spy2Status = 0
        pause 1.0
        y "...........?"
        y "Where's Clover?"
        "{b}*Bleep*{/b}"
        scene bgDatabase
        show red r56 at le
        show scene_camera
        with fade
        c r56 "We can use brass rivots for that part. It will look more realistic that way."
        tali "Oh good idea! And I think I still have some zippers we can use in the back."
        y "...............?"
        tali "Wait, I'll go get them."
        y "Psst... Clover...!"
        c r18 "...?"
        c "[playerName]? Oh hey."
        y "Are you with Talia? You didn't report in."
        c r29 "Oh is it that time already? Sorry, me and her got caught up talking about cosplaying."
        y "Cosplaying...?"
        c r1 "Yeah you know. Where you dress up as your favorite character from a movie or video game."
        c "You caught me playing as Princess Hamdarusojamia at the anime convention."
        y "......................"
        c "Turns out, Talia is a massive cosplayer as well. We're discussing techniques on how to make our outfits look better."
        y "Well... at least you managed to get close to her."
        y "How difficult will it be to take her in, you think?"
        c r11 "Well...."
        c r12 "It actually should be fairly easy."
        y "Easy?"
        c r1 "Yeah, she joined the gang to avenge her brother's capture, but quickly found herself in over her head."
        c "She's willing to surrender, but is afraid the gang will come after her.{w} If we plan a mission to take her in, she'll come with us as long as long as we make it look believable."
        y "Plan a mission and take in Talia. Sounds easy enough."
        hide red
        hide scene_camera
        scene bgBase with fade
        jump nextReport
    if task18Stage == 2:
        $ task18Stage = 3
        $ specialTaliaStatus = 3
        $ task18Name = _("Nourishing Beats (Complete)")
        $ task18Text = _("Talia caused some trouble for us, but we managed to capture her.")
        $ punkRep = 0
        $ punkRank = 3
        call undressSam from _call_undressSam_10
        call undressClover from _call_undressClover_7
        call undressAlex from _call_undressAlex_9
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        show scene_darkening with d3
        show red r1 at le with d3
        c r55 "Okay Talia, here we are."
        tali "Here we are indeed..{w} So I'll be safe here?"
        y "For the time being, yeah. You are still a prisoner of course."
        tali "Of course..."
        tali "..................."
        tali "So is Carla locked up in here aswell?"
        c r57 "Carla Wong? Yeah, she's in her cell not far from here."
        c "We'll keep you guys separated, so she'll never know you turned yourself in."
        tali "Right."
        c r1 "Well [playerName]. Her eyes aren't red and she's not showing any signs of aggression. Seems she's not being nano-controlled."
        y "I think we should have sex... just in case..."
        c r10 "[playerName]...."
        tali "Have sex?{w} If we need to have sex to prove that I'm not being controlled, that's fine."
        y "See? She agrees with me!"
        c r38 "Ugh... fine. I'm not gonna be here while you two get it on. Call me if you need me."
        y "Can I call you if we run out of lub-...?"
        c "No."
        hide red with d3
        pause 0.5
        y "Now... where were we...?"
        tali "I believe you and I were about to get better acquainted~..."
        "Talia gets up and seductively walks over to you. Putting her hands on your chest, she presses herself up against you."
        tali "Check me for nanobots... but be sure to be {i}'thorough'{/i}~..."
        menu:
            "Don't mind if I do!" if True:
                tali "It's been so long since I had a good thussle in the sheets~..."
                tali "I bet you can make me scream all night long...."
            "Wait, something is off-..." if True:
                pass
            "Say something insane" if True:
                y "Red is my favorite flavor...."
                tali "Mine too~...."
        "Talia's eyes suddenly turn red!"
        y "Wai-...!"
        play sound "audio/sfx/punch1.mp3"
        hide scene_darkening
        scene black
        with hpunch
        "{b}*Slam!*{/b}"
        "Talia knocked you upside the head!"
        scene bgPrison with d3
        y "Lady..."
        tali "...?!"
        y "I've been getting bumped on the head so much, I feel like I'm becoming immune to it."
        tali "Oh I see... {w}Let me try again."
        y "SPIE-....!!!!"
        play sound "audio/sfx/punch1.mp3"
        hide scene_darkening
        scene black
        with hpunch
        pause 1.5
        a "He's waking up..!"
        scene bgPrison
        show green at ri
        show red r16 at ce
        show yellow y29 at le
        show scene_fighting
        with fade
        c "[playerName]?! Are you okay?"
        y "I feel like this little adventure of ours is going to leave me with permanent brain damage, but at the moment...{w} I'm okay."
        y "Where's Talia?"
        s g39 "We don't know. She smuggled a gadget with her and turned off the lights. She also used it to unlock her cell."
        y "Uh oh..."
        c r21 "It gets worse..."
        s "She also let Carla Wong, the Dragon Lady, out of her cell."
        y "She tricked us..."
        c r42 "I shouldn't have trust her so easily..."
        y "Did she leave the prison area? If she gets in contact with Drift Punk, we'll be in trouble."
        s "No. When the power went off, the elevator to the milkshake bar also stopped working."
        a y30 "Meaning they're still here somewhere!"
        y "Okay, let's split up and start searching!"
        "The girls give you a resolute nod and then scatter in different directions."
        hide yellow with d2
        hide red with d2
        hide green with d2
        pause 0.5
        y "...................."
        label task18SearchMenu:
            pass
        menu:
            "Search the top floor of the prison" if task18SearchTop:
                $ task18SearchTop = False
                play sound "audio/sfx/running1.mp3"
                scene black with fade
                pause 0.5
                hide scene_fighting
                scene bgPrison
                show yellow at ri
                show scene_fighting
                with fade
                y "Any luck?"
                a "Nowhere to be found..."
                a "But I did find this while searching!"
                $ matsAcid += 1
                play sound "audio/sfx/itemGot.mp3"
                "Alex hands you {color=#ffeda6}Hydrofluoric Acid{/color} x1."
                y "All right, let's keep searching."
                hide yellow with d3
                jump task18SearchMenu
            "Search the middle floor of the prison" if task18SearchMid:
                $ task18SearchMid = False
                play sound "audio/sfx/running1.mp3"
                scene black with fade
                pause 0.5
                hide scene_fighting
                scene bgPrison
                show green at ri
                show scene_fighting
                with fade
                y "Sam! Any clue about her whereabouts?"
                s "No, nothing. She must have fled into the lower portion of the compound."
                s "I did find this weird shrine. Dedicated to some kind of tentacle monster..."
                y "Er.... I'll explain later. Let's continue searching for now!"
                hide green with d3
                jump task18SearchMenu
            "Search the bottom floor of the prison" if True:
                play sound "audio/sfx/running1.mp3"
                scene black with fade
                pause 0.5
                hide scene_fighting
                scene bgPrison
                show red at ri
                show scene_fighting
                with fade
                y "Any luck over here?"
                c r31 "Shhh~..."
                "The two of you stay deadly silent..."
                pause 1.3
                c "This way!"
                hide red with d3
                "You quickly call Sam and Alex before chasing after Clover."
        pause 1.5
        drag "Brilliant escape plan, Talia..."
        tali "How could I have known that their lift wouldn't work?! Just stay quiet..."
        "Bzzzzzzt!"
        hide scene_fighting with d5
        pause 0.5
        tali "!!!"
        drag "!!!"
        c r32 "There they are!"
        show red at le
        show green at ce
        show yellow at ri
        with d3
        tali "Uh oh..."
        play sound "audio/sfx/punch1.mp3"
        hide yellow
        hide red
        hide green
        scene black
        with hpunch
        pause 1.0
        "You quickly manage to overpower the two lieutenants and bring them back to their cell."
        scene bgPrison with fade
        show scene_darkening with d3
        pause 0.5
        show red at ri with d3
        c r33 "She's under lock and key..."
        c r5 "................."
        c "I can't believe I let her trick me so easily. It was all just one big plan to break Carla out..."
        y "We've been a bit too lacks on security in general. Don't let it bother you too much."
        c r38 "Hmpf~..."
        y "So yeah... I'm gonna go fuck her now to suppress her nanobots."
        c "............"
        hide red with d3
        scene black with fade
        pause 0.5
        tali "Ooooh! AH! AHH! ♥"
        tali "H-harder...!!!"
        tali "{b}*Moans*{/b} Right there~... ♥♥♥"
        y "Say cheese!"
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d3
        pause 0.5
        show picTalia:
            xalign 0.5 yalign 0.5
        with dissolve
        pause
        play sound "audio/sfx/itemGot.mp3"
        "A new photo has been added to your photoalbum."
        hide picTalia
        scene bgPrison
        with fade
        show scene_darkening with d3
        tali "............"
        y "No longer being controlled?"
        tali "Doesn't matter. Controlled or not, I still hate WOOHP."
        tali "You took away my brother..."
        y "................"
        tali "I know he was suppose to be a {i}'bad guy'{/i}. But he was still my brother, y'know..."
        y "What happened to him?"
        tali "You tell me..."
        tali "................"
        tali "I don't know what happened to him... {w}WOOHP wouldn't let us visit him.{w} I haven't seen him in years."
        y "Years...?"
        tali "Doesn't matter now anyways. Drift Punk said they'd help me find him in return for my technical skills, but all they worry about is their games, cars and music."
        tali "I guess hanging around here is just as productive as being with those guys..."
        tali "Doesn't mean I'm giving up on my brother just yet."
        y "I'll come ask you about him sometime... maybe I can help you find him."
        tali ".................."
        tali "I'd like that..."
        "You leave Talia alone for now."
        hide scene_darkening
        with d3
        pause 1.3
        show scene_fighting
        with d3
        "Computer" "Computer: Talia H.\nStatus: Captured."
        "Computer" "Transferring funds..."
        $ cash += 1200
        $ randMoney = 1200
        call missionRewardMoney from _call_missionRewardMoney_77
        pause 0.4
        hide scene_fighting with d3
        "New clothing options for Clover are available at the mall."
        scene bgBase with fade
        jump base

default task19Stage = 0
default task19Name = ""
default task19Text = ""

screen task19Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task19Text]"

label task19:
    if task19Stage == 0:
        $ task19Stage = 1
        $ spy1Status = 1
        $ acesRep += 1
        scene bgBase with fade
        show scene_darkening with d3
        show green g18 at ri with d3
        $ greenDayJob = 1
        $ mapSpy1Selected = False
        y "Are you getting used to going undercover with the Aces?"
        s "I don't think you can ever get used to the Aces."
        s "The amount of money they have... it's kind of intimidating..."
        s g14 "It goes further than fancy cars or jewelry. These people could buy half of the city if they wanted to."
        s g38 "Which makes it even more disgusting that they seem to get a kick out of stealing instead..."
        y "They're just doing it for the thrill. Let's teach them a lesson and put them behind bars."
        hide green with d3
        "Sam nods and heads out."
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task19Stage == 1:
        $ task19Stage = 2
        $ greenDayJob = 0
        $ acesRep += 1
        pause 0.5
        show scene_darkening with d3
        show green g5 at ri with d3
        s "................"
        y "Sam, you look upset. What happened?"
        s "Well... here..."
        "Sam hands you a $100 dollar bill."
        $ cash += 100
        $ randMoney = 100
        call missionRewardMoney from _call_missionRewardMoney_82
        y "What did you have to do to get this...?"
        s "We went to a fancy restaurant today..."
        s g15 "One of the Aces made an unreasonable demand of our waiter. When he couldn't comply, the Aces dumped their food on him."
        s "They mocked him for being a bad waiter and waved a hundred dollar bill in his face. Told him that this was suppose to be his tip, but they gave it to me instead..."
        y ".............."
        s g14 "So yeah... that happened today..."
        y "Don't let it get to you too much. Head back to your cell for now."
        "Sam slanters off to her cell."
        hide green with d3
        hide scene_darkening with d3
        jump nextReport
    if task19Stage == 2:
        $ task19Stage = 3
        $ greenDayJob = 0
        $ acesRep += 1
        pause 0.5
        show scene_darkening with d3
        show green g18 at ri with d3
        y "Any waiters tormented today?"
        s "No, but we did rob a jewelry store."
        s "It went surprisingly smooth. The jeweler seemed happy to see us."
        y "Happy to see you...?"
        s g16 "Yeah, turns out he insured his entire stock right before the gang uprising so we didn't even have to threaten him."
        s "Before we know it we were outside again, with our arms full of loot."
        s g2 "The Aces threw a hissy fit, saying it wasn't any fun doing it like this."
        s "They gave me their share of the loot and went to sulk."
        play sound "audio/sfx/itemGot.mp3"
        "Sam hands you {color=#ffeda6}Valuables{/color} x1."
        $ matsValu += 1
        y "Ooooh treasure!"
        s g14 "Remember this isn't ours, [playerName]..."
        y "I know I know... but I still like rolling around in it and feel like a sultan!"
        s g35 "................"
        s g2 "Nobody got hurt, no property was damaged and everything was insured. I guess we can keep these valuables to turn into gadgets."
        s g1 "Just this once."
        hide green with d3
        hide scene_darkening with d3
        jump nextReport
    if task19Stage == 3:
        $ task19Stage = 4
        $ greenDayJob = 0
        $ acesRep += 1
        pause 0.5
        show scene_darkening with d3
        show green g29 at ri with d3
        y "Hi Sam, did something interesting ha-..."
        s "I saw Alex!"
        y ".........."
        y "Who...?"
        s g31 "She's a fellow spy and our friend. I saw her walking around town with those WOOHP agents."
        s "If she's being controlled then we should worry. She might be a little ditzy, but she's a great spy."
        s g32 "She disappeared before I could get to her, but maybe some of the Aces know more. It would be best if you kept sending us undercover there, we might be able to find out more."
        y "Keep sending you girls undercover with the Aces. Got it."
        hide green with d3
        hide scene_darkening with d3
        jump nextReport

default task20Stage = 0
default task20Name = ""
default task20Text = ""

screen task20Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task20Text]"

label task20:
    if task20Stage == 0:
        $ task20Stage = 1
        $ yellowDayJob = 0
        $ cellAlexPoetry = 1
        scene bgBar with fade
        show scene_darkening with d3
        show yellow y7 at ri with d3
        a "Grrrrrr!"
        y "Uh oh... Alex are you being controlled again?"
        a y1 "No, I'm channeling my inner teenage angst!"
        y "......"
        y "Okay~....?"
        a "The Outsiders said I need to get angry more. Outraged by the injustice in the world."
        a y28 "Like the rich having all the power, and the poor just being exploited by the upper class!"
        a y8 "And I have to make my voice known! Shout and decry the tyrannical government that just wants to keep us down!"
        y "So how's that going?"
        a y1 "It's going well! They even gave me my own gothic poetry book!"
        a "Wanna read it?"
        menu:
            "Let me read it" if True:
                y "Yeah, I'll read it."
                y "........................."
                y "Well at least you started writing in black ink instead of rainbow crayons."
                y "Let see here..."
                y "{i}'Roses are green, violets are green. I am a monster....{w} and want to eat your spleen.'{/i}"
                y "......................."
                y "Yeah.... that's about the level of literacy I expected from you."
                y "You know neither roses nor violets are green, right?"
                y "But valiant first try I guess."
                a y13 "I feel like I'm going to become a great poet some day!"
            "Get that away from me" if True:
                y "Keep that freaky voodoo away from me."
                a y10 "It's just poetry, [playerName]...."
        a y2 "If I keep this up, I feel like I could really make people feel things, you know!"
        a "Like make people happy or sad!"
        y "Or melancholic."
        a y29 "{b}*Gasp*{/b} I don't even know what that means!"
        y "............."
        y "Just get over to the Outsiders."
        "Alex nods and grabs her poetry book."
        hide yellow with d3
        $ mapSpy3Selected = False
        $ yellowDayJob = 3
        $ spy3Status = 1
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task20Stage == 1:
        $ outsideRep += 1
        $ task20Stage = 2
        $ yellowDayJob = 0
        pause 0.5
        show scene_darkening with d3
        show yellow y5 at ri with d3
        y "Welcome back Alex. How did it go?"
        a "Well... they didn't really like my poem..."
        a y1 "But as we were vandalising a bus stop they gave me some pointers!"
        a "I'm gonna try my best and write something good for tomorrow!"
        y "Okay~.... What about your undercover work?"
        a y41 "Hm? Oh yeah, here's what intel I managed to gather today."
        $ randIntel = 100
        $ intel += 100
        call missionRewardInt from _call_missionRewardInt_32
        "Alex hands you a box full of papers, USB sticks, guard patrol routes and more."
        y "!!!"
        y "That's... a lot of intel. How did you get all of this?"
        a "I just said I needed some black make-up from the command building and they let me in!"
        y "That easily...?"
        a y24 "Yeah. I think they knew better not to get between a goth and her eyeshadow."
        hide yellow with d3
        hide scene_darkening with d3
        jump nextReport
    if task20Stage == 2:
        $ outsideRep += 1
        $ task20Stage = 3
        $ yellowDayJob = 0
        $ spy3Status = 0
        pause 0.5
        show scene_darkening with d3
        show yellow y1 at ri with d3
        y "Okay, I'm eager to hear what you got up to today."
        a "So I wrote another poem! Wanna read it?"
        y "..........."
        "You read the poem Alex wrote. It's filled with spelling errors, ham-fisted metaphors and edgy teenage angst."
        y "Wow....{w} This is trash!"
        a y28 "Hey! I put my heart and soul into that, you know!"
        y "No you didn't."
        a y11 "................"
        a y12 "Okay fine, I wrote it in five minutes during my lunch break. {w}But the Outsiders loved it!"
        a "I just sorta wrote down what I thought a goth would love and they ate it up."
        a y1 "Well... except for one who saw through it... I'm gonna try writing a better poem for him tomorrow."
        y "Still... a gang that's into poetry... Doesn't really match."
        a y14 "{b}*Shrugs*{/b} Drift Punk are a mix between nerds and party people."
        a "And the Aces are a mix between spoiled rich kids and art collectors."
        y "Good point.{w} Beverly Hills has become a breeding ground for weirdos."
        hide yellow with d3
        hide scene_darkening with d3
        jump nextReport
    if task20Stage == 3:
        $ outsideRep += 1
        $ task20Stage = 4
        $ yellowDayJob = 0
        pause 0.5
        show scene_darkening with d3
        show yellow y1 at ri with d3
        y "Okay, I'm eager to hear what you got up to today."
        a "Well I tried writing a poem for that one goth guy at the gang, right? Wanna read it?"
        y "Is it any better than yesterdays poem?"
        a "Here... See for yourself."
        y ".............{w}............{w}..........."
        "The poem..."
        "Is the most heartfelt, genuine and beautiful poem you've ever read!"
        y "................{w}{b}*Sniff*{/b}"
        y "Alex, this is beautiful. Where did you learn to write like this?"
        y "It took me to another world... made me remember the joys of my childhood carefree days.... opened my mind to brand ne-..."
        a y28 "It's about a baby turtle!"
        y "What."
        a y1 "Yeah the goth kid misinterpretated the poem aswell. Thought that it was about the ever onward march of time and the loss of innocents or whatever."
        a "I guess everyone has a different interpretation!{w} But in reality it's about a baby turtle I saw on tv."
        y "........................"
        hide yellow with d3
        hide scene_darkening with d3
        jump nextReport

default task21Stage = 0
default task21Name = ""
default task21Text = ""

screen task21Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task21Text]"

label task21:
    if task21Stage == 0:
        $ task21Name = _("Pink is thew New Black")
        $ task21Text = _("We're going to try and get close to Felicity. I should send Alex out to the Outsiders to see if we can get on her good graces.")
        $ task21Stage = 1
        $ yellowDayJob = 3
        $ spy3Status = 1
        $ mapSpy3Selected = False
        scene bgBar with fade
        show scene_darkening with d3
        show yellow at ri with d3
        y "Okay Alex. We found out who the next lieutenant is for the Outsiders. It's some rich girl called Felicity Fences."
        a y18 "Felicity...."
        a "Why does that name ring a bell...?"
        a y28 "Wait! We fought Felicity some time ago. She's with the Outsiders now?!"
        y "Looks like it. Why?"
        a y37 "Felicity used to be a spoiled brat. A real rich girl. I thought she'd be with the Aces. Not the Outsiders."
        a "She kidnapped professional athletes and had them fight for her in a gladiator arena last we saw her."
        y "Why...?"
        a y1 "Cause she's a rich hoe who gets bored easily."
        y "Alex! Language!"
        a "I'll try to win her trust so we can capture her!"
        a "It'll be easy!"
        y "Well I like your enthusiasm. Head to the Outsiders and report back tonight."
        "Alex nods and heads off."
        hide yellow
        hide scene_darkening
        with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task21Stage == 1:
        $ task21Name = "Pink is thew New Black"
        $ task21Stage = 2
        $ outsideRep += 1
        $ yellowDayJob = 0
        show scene_darkening with d3
        show yellow y20 at ri with d3
        y "Welcome back Alex. Any luck getting on Felicity's good side?"
        a "No... it might be harder than I thought..."
        a "She's not really a gangster in the gang. Instead, she's just a financial backer."
        a "Meaning she's probably not interested in my dark poetry..."
        y "Hm... found out anything else?"
        a y57 "Well she has a good friend inside the Outsiders that she seems to listen to. A total punker."
        a "I bet if we get close to her, she could set up a meeting with Felicity for us."
        y "Sounds like a plan. Try your best to impress her. I'll send you out again tomorrow."
        hide yellow
        hide scene_darkening
        with d3
        jump nextReport
    if task21Stage == 2:
        $ task21Name = "Pink is thew New Black"
        $ task21Stage = 3
        pause 1.5
        scene bgStreet4
        show yellow at ri
        show scene_camera
        with fade
        a "Alex here!"
        y "Whadda ya need my lovable Canary?"
        a y10 "Well first of all you could not call me that..."
        a y1 "But second, we're going to show off our graffiti art skill."
        a "Can I get some money for paints?"
        y "Er... how much do you need?"
        a "About $150. If we don't have enough money then I can borrow some paint from the others, but I kinda want a collection of canisters myself."
        menu:
            "Give $150" if cash >= 150:
                $ cash -= 150
                $ cellAlexPaint = 1
                $ alexMood += 5
                y "Well all right then. I think we can miss it. Show them some true art!"
                a y3 "All right!"
            "Don't give $150" if True:
                $ alexMood -= 1
                y "We don't have any money to spare right now."
                a y5 "Aw..."
                a "That's okay. I can borrow some of the paint from the others."
        y "Oh and Alex..."
        a y1 "Yeah?"
        y "Don't draw any ponies and butterflies, okay?"
        a "No promises!"
        hide yellow
        hide scene_darkening
        hide scene_camera
        with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task21Stage == 3:
        $ task21Name = _("Pink is thew New Black")
        $ task21Text = _("We're going to try and get close to Felicity. I should send Alex out to the Outsiders to see if we can get on her good graces.\n\n-Stalk and kidnap the handsome model on his daily walk on the beach.")
        $ task21Stage = 4
        $ outsideRep += 1
        $ yellowDayJob = 0
        show scene_darkening with d3
        show yellow at ri with d3
        a "I'm back! We went out painting!"
        y "What did you paint?"
        a "A unicorn.... a goth unicorn!"
        a "The punker I mentioned seemed to like it. We got talking and she said Felicity is cautious of me."
        a y12 "Which to be fair... we were the ones to put her in prison a couple of years ago."
        y "Any way we can convince her?"
        a "Well... she's pretty much still up to her old tricks. Kidnapping handsome guys to create her own personal harem of beefcakes."
        a y14 "There's just one guy who keeps eluding her. I bet if we kidnap and deliver him to Felicity, I'd earn some browny points!"
        a "He's a super hot model that's living somewhere in the city."
        y "Not sure if it's right for us to start kidnapping people."
        a "I agree. We can't just take a guy off the streets, deliver him to a life of luxory and all the sex he could ever hope for!"
        y "Actually... {w}That doesn't sound so bad."
        a y29 "But [playerName]! Kidnapping is wrong! Even if he'll enjoy the finest cooking, erotic steamy nights and won't have to lift a finger!"
        a "............."
        a y28 "Wow you're right, that does sound pretty good."
        a "He's usually seen walking near the beach."
        y "Okay, I'll stalk him for a while and when the area is safe, I'll call you to grab him."
        a y1 "Okay!"
        hide scene_darkening
        hide yellow
        with d3
        jump nextReport
    if task21Stage == 4:
        $ task21Name = _("Pink is thew New Black")
        $ task21Stage = 5
        $ task21Text = _("We're going to try and get close to Felicity. I should send Alex out to the Outsiders to see if we can get on her good graces.\n\nThe model has been captured and Alex went off to deliver him.\n\n{color=#A3A3A3}-Stalk and kidnap the handsome model on his daily walk on the beach.{/color}")
        scene bgStreet4 with fade
        model "................"
        y "Target has been spotted..."
        menu:
            "Follow closely" if True:
                y "(Best make sure that I don't lose him...)"
                "You follow the man closely down the street."
            "Follow at a distance" if True:
                y "(Following him at a reasonable distance should allow me to keep track of him without being noticed...)"
                "You wait for the man to begin his morning walk before casually following after him."
            "Follow far away" if True:
                y "(There's no way I want to mess this up. Best be cautious and follow him at a distance.)"
                "You wait for the man to turn a corner before following after him."
        model "................"
        model "Hm...?"
        y "(Crap!)"
        "You quickly duck behind a dumpster."
        y "(Did he see me?)"
        model "....................."
        "After a short while the man turns around and continues walking again."
        menu:
            "Follow closely" if True:
                y "(It's risky, but I can't let him out of my sights...)"
                "You get a little closer and continue following the man."
            "Follow at a distance" if True:
                y "(I can't push my luck. Best follow him at a reasonable distance...)"
                "You wait for the man to cross the street before continuing the persuit."
            "Follow far away" if True:
                y "(He's a keen one. Best not to take any risks and keep my distance.)"
                "You give the man plenty of time to get out of reach before you persue him."
        model "................"
        model "Hm...?"
        y "(Crap!)"
        "You quickly duck behind a tree."
        y "(Did he see me again?! This guy must have the eyes of an eagle and the ears of a... of a.... {w}of a thing that can hear really well.)"
        "After a short break, the man continues walking."
        menu:
            "Follow closely" if True:
                y "(This is it... I just need to get closer and signal Alex to capture him!)"
                "You begin making your way closer and closer to the man."
            "Follow at a distance" if True:
                y "(Slow and steady... I don't want to blow this...)"
                "You give the man some time to continue walking as you pretend to be reading a newspaper...{w} An act which in it self is suspicious. {w}Who still reads newspapers now-a-days...?"
            "Follow far away" if True:
                y "(He must have the trained reflexes of a ninja! I should be extra carefull...)"
                "You wait until there's at least a football field distance between you and the man before continuing."
        model "................"
        model "Hm...?"
        y "(Not again!)"
        y ".........."
        y "Wait...."
        "You walk up to the man."
        y "Erm... Excuse me."
        model "................"
        model "Hm...?"
        y ".................."
        y "Hello...?"
        model "................"
        model "Hm...?"
        y "You can't actually hear me, can you...?"
        y "Can you even see me...?"
        "You wave your hand in front of the man's face."
        "After assessing the situation, you come to the conclusion that the model is both deaf and blind."
        y "..................."
        y "Well that should make this easier... Alex, get him!"
        a "Roger!"
        "Alex jumps off of the roof and lands on the visual and hearing impaired man!"
        show scene_darkening with d3
        show yellow y16 at ce with d3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        a "Well that was easy..."
        y "Take him to the Outsiders and report back later tonight."
        a y1 "Right!"
        $ yellowDayJob = 3
        $ spy3Status = 1
        $ mapSpy3Selected = False
        hide yellow with d3
        hide scene_darkening with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task21Stage == 5:
        $ task21Name = _("Pink is thew New Black")
        $ task21Text = _("We're going to try and get close to Felicity. I should send Alex out to the Outsiders to see if we can get on her good graces.\n\nThe model has been captured and Alex went off to deliver him.\n\nFelicity seemed to have liked our gift.\n\n{color=#A3A3A3}-Stalk and kidnap the handsome model on his daily walk on the beach.{/color}\n\n-Setup a mission to the Carnival and capture Felicity Fences.")
        $ task21Stage = 6
        $ yellowDayJob = 0
        $ spy3Status = 0
        $ mapSpy3Selected = False
        $ coverCounter += 10
        $ task21Stage = 6
        show scene_darkening
        with d3
        show yellow y29 at ri
        with d3
        a "Good news, [playerName]! I spoke to Felicity today."
        y "Did she like our gift?"
        a y1 "I think so... We should be able to get close enough to her now. Set up a mission to the Carnival and we can take her down!"
        hide scene_darkening
        hide yellow
        with d3
        jump nextReport
    if task21Stage == 6:
        $ task21Text = _("We managed to capture and interrogate Felicity. Striking one more lieutenant off the records.")
        $ task21Stage = 7
        $ specialFelicityStatus = 3
        show scene_darkening with d3
        feli "Oh woe is me, captured by commoners!"
        y "Dramaaaaa!"
        feli "...."
        feli "So you're behind the attacks against the Outsiders..."
        y "Yup. And you must be Felicity."
        feli "{b}*Hmph~...*{/b} That's Ms. Fences to you, worm."
        y "................"
        show yellow at le with d3
        a "Oh [playerName], I was just about to introduce you two."
        feli "You....! Just because you brought me a hunky slave, doesn't mean I forgive you for this!"
        feli "You will rue the day you cross path with Felicity Fen-..."
        y "Can I fuck her now?"
        a "Sure!"
        feli "Wait what?!"
        y "You know. Have sex, break the nanobot control over you. It's pretty much par for the course at this point."
        feli "You donkey, I'm not being controlled by nanobots!"
        a y29 "Now that she mentions it... her eyes aren't red."
        y "No person could be this unlikeable without being controlled!"
        feli "Hey!"
        a y2 "Better make sure! Get naked Felicity, [playerName] is going to destroy your puss."
        feli "!!!"
        y "Not so fast, Alex. We're not going to rape her."
        a y28 "But she's so annoying....!"
        y "..................."
        y "You're scary sometimes, you know that?"
        feli "Nobody is raping anyone! I only sleep with the most handsome of guys!"
        y "Handsome?"
        feli "So if you want information out of me, you better bring me a hot stud!"
        y "But Felicity..."
        y "................."
        feli ".....?"
        stop music fadeout 2.0
        hide scene_darkening
        hide yellow
        with d5
        play sound "audio/sfx/wow.mp3"
        show expression "gui/stud.jpg" with qFade
        pause 0.7
        "You" "I {i}am{/i} a hot stud."
        feli "{b}*Gasp*{/b} So beautiful!"
        feli "Okay I changed my mind. We are definitely going to have sex!"
        scene black with longFade
        pause 0.5
        "Felicity" "Ah! Ahh! Ahhhh! ♥♥♥"
        "Felicity" "Yes! Oh God yes!"
        "Felicity" "Oooooh yes, you beautiful creature!! ♥♥♥♥♥"
        y "Say cheese...!"
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d3
        pause 0.5
        show picFelicity:
            xalign 0.5 yalign 0.5
        with dissolve
        pause
        play sound "audio/sfx/itemGot.mp3"
        "A new photo has been added to your photoalbum."
        hide picFelicity
        scene bgPrison
        with fade
        show scene_darkening with d3
        play music "audio/music/nighttime.mp3" fadein 4.0
        feli "Phew~..."
        y "Now how about you share some intel on the Outsiders..."
        feli "Hmm....{w} Oh who cares. I was getting bored with them anyways."
        "Felicity goes into detail about the Outsiders and the state of the gang."
        $ randIntel = 600
        $ intel += 600
        call missionRewardInt from _call_missionRewardInt_33
        play sound "audio/sfx/itemGot.mp3"
        feli "I was never good at keeping secrets anyways."
        y "Doesn't sound like the gang is doing too hot."
        feli "Well you saw to that with your landgrab raids. Taking in the gang leader should be a piece of cake."
        feli "I hear he's into some kind of weird magic shit though."
        y "..................."
        hide scene_darkening with d3
        pause 0.6
        call qCompleted from _call_qCompleted_10
        hide scene_darkening
        with d3
        pause 1.3
        show scene_fighting
        with d3
        "Computer" "Computer: Felicity F.\nStatus: Captured."
        "Computer" "Transferring funds..."
        $ cash += 1200
        $ randMoney = 1200
        call missionRewardMoney from _call_missionRewardMoney_83
        pause 0.4
        $ outsideRep = 0
        $ outsideRank = 3
        "New clothing options for Alex are available at the mall."
        hide scene_fighting with d3
        scene bgBase with fade
        jump base

default task22Stage = 0
default task22Name = ""
default task22Text = ""

screen task22Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task22Text]"

label task22:
    if menuTutActive:
        $ menuTutActive = False
        scene bgBar with fade
        pause 0.4
        show scene_fighting with d5
        "With all the girls unlocked, you can now begin expanding the menu for your bar. When calling a Business Meeting you and the girls will throw out suggestions to add to the menu."
        show bgMenuTut with d5
        "These menu options are often more risqué, causing the customers to pay more for them. Meaning with more menu options, you'll make more money!"
        "New menu options are turned on by default, but you can turn them off if you find them too risqué and prefer your spies do not preform them."
        "To call a business meeting, simply visit the bar during daytime before you send spies out on their daily jobs. Then select the 'Business Meeting' option."
        "If there are no new options for the menu, then train your girls up a bit more. More options are unlocked as your spies get sluttier."
        hide bgMenuTut
        hide scene_fighting
        with fade
        if tod == 1:
            scene bgMap:
                zoom 0.5
            with fade
            jump worldmap
        elif True:
            jump club


default task23Stage = 0
default task23Name = ""
default task23Text = ""
default spyReadyMusicroom = 0

screen task23Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task23Text]"

label task23:
    if task23Stage == 0:
        $ task23Stage = "Drift Punk is using music to hypnotize people. Clover is sent out to investigate."
        $ task23Stage = 1
        scene bgBar with fade
        show scene_darkening with d3
        show red r13 at ce with d3
        "{b}♫♪ *Music* ♫♪{/b}"
        y "Clover."
        "{b}♫♪ *Music* ♫♪{/b}"
        y "Clover..."
        "{b}♫♪ *Music* ♫♪{/b}"
        with hpunch
        y "CLOVER!"
        c r18 "[playerName]? Did you say something?"
        y "Whadda ya listening to?"
        c r1 "This awesome new song that the Drift Punk just released. It's been playing everywhere."
        y "Let me listen to it."
        "Clover hands you her earpods."
        y "......................."
        y "This is pretty good!"
        play sound "audio/voice/clover/yeah1.mp3"
        c "Yeah!"
        y "Makes me want to get up and dance!"
        c "Exactly!"
        y "Makes me want to rob a bank!"
        play sound "audio/voice/clover/what2.mp3"
        c r29 "Ye-... wait, what?"
        y "Didn't you mention that Drift Punk were working on mind controlling music?"
        c "Now that you mention it..."
        y "Time to investigate! Head over to Drift Punk and see what's going on."
        c r31 "Right."
        "Clover nods and heads out."
        hide red with d3
        $ spy2Status = 1
        $ redDayJob = 2
        $ mapSpy2Selected = False
        show bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task23Stage == 1:
        $ task23Stage = "Drift Punk is using music to hypnotize people. Their plan is to hypnotize the entirety of Beverly Hills and we have to stop them.\n\n-Plan a mission to Punk Web and stop the audio transmission."
        $ task23Stage = 2
        show scene_darkening with d3
        show red r10 at ce with d3
        c "Well... I'm back."
        y "And?"
        c "And... it's pretty bad. The Drift Punk plan to play their music over every radio station, intercom and speaker in this city. Telling people to hand over their valuables."
        y "Okay, then we stop them. Right?"
        c r12 "It's not quite that simple. We'd have to go into Punk Web and disable three transmitters which are kept under constant guard."
        c r11 "But... they have to be disabled at the same time."
        y "So you girls will have to split up..."
        y "Best get plenty of gadgets ready, this could be a tough cookie."
        c r34 "Just plan a mission whenever you're ready. We'll take these gangsters down."
        hide red
        hide scene_darkening
        with d3
        $ redDayJob = 0
        jump nextReport
    if task23Stage == 2:
        $ task23Stage = "Drift Punk is using music to hypnotize people. Their plan is to hypnotize the entirety of Beverly Hills and we have to stop them.\n\n-Plan a mission to Punk Web and stop the audio transmission."
        $ task23Stage = 3
        $ backupSamActive = False
        $ backupCloverActive = False
        $ backupAlexActive = False
        show scene_darkening
        with d3
        y "Okay girls, split up."
        if activeSpy == 1:
            y "Sam, head in and find your transmitter room. The other girls won't be available for backup, so be careful."
            sM "Got it."
        if activeSpy == 2:
            y "Clover, head in and find your transmitter room. The other girls won't be available for backup, so be careful."
            cM "Got it."
        if activeSpy == 3:
            y "Alex, head in and find your transmitter room. The other girls won't be available for backup, so be careful."
            aM "Got it."
        scene black with fade
        hide scene_darkening with d3
        jump missionBegin
    if task23Stage == 3:
        $ hackSkillUsed = False
        $ spyReadyMusicroom += 1
        scene bgAudioroom
        show audioroom
        with fade
        pause 1.0
        if activeSpy == 1:
            sM "There it is!"
        elif activeSpy == 2:
            cM "There it is!"
        elif activeSpy == 3:
            aM "There it is!"
        y "Okay good. Try turning it off with your hacking tool."
        label retryHack:
            pass
        $ hackResult = 0
        if activeSpy == 1:
            show expression "mission/models/sam/hacking3.jpg"
        if activeSpy == 2:
            show expression "mission/models/clover/hacking3.jpg"
        if activeSpy == 3:
            show expression "mission/models/alex/hacking3.jpg"
        show screen spyHacking
        with fade
        while hackResult < 90:
            $ hackResult += 1
            pause 0.003
        pause
        if hackResult >= 100:
            if activeSpy == 1:
                sM "I'm in!"
        elif True:
            y "Try again. Don't forget to use your boost."
            scene black
            $ hackSkillUsed = False
            jump retryHack
        if spyReadyMusicroom <= 2:
            y "Okay, standby. I'm switching camera."
            hide screen spyHacking
            scene black
            with fade
            if activeSpy == 1:
                $ activeSpy = 2
            elif activeSpy == 2:
                $ activeSpy = 3
            elif activeSpy == 3:
                $ activeSpy = 1
            $ missionProgression = 0
            $ controlCountDown = 4
            jump missionBegin
        elif spyReadyMusicroom == 3:
            y "Okay, stand by for my signal. Then all three turn off the transmission."
            hide expression "mission/models/sam/hacking3.jpg"
            hide expression "mission/models/clover/hacking3.jpg"
            hide expression "mission/models/alex/hacking3.jpg"
            hide screen spyHacking
            with d3
            pause 0.5
            y "Three...... Two...... One......"
            pause 0.5
            "???" "Not so fast..."
            cM "{b}*Yelp*!{/b}"
            y "Clover?!"
            sM "[playerName]! What's going on?!"
            aM "Is Clover okay?!"
            "Suddenly a nearby tv screen turns on..."
            hide screen equipmentMenu
            scene black
            with fade
            show expression "mission/database3Var1.jpg":
                zoom 0.4
            show sebModel1 at ce
            show scene_camera
            with fade
            "???" "Well well well, ain't this a surprise..."
            aM "{b}*Gasp*{/b} That voice...!"
            sM "Sebastian Saga..."
            hide sebModel1 with d2
            hide scene_camera
            show sebModel2 at ce
            show scene_camera
            with d4
            seb "So nice to see you girls again. Up to the same tricks as usual I presume?"
            sM "What have you done to Clover?!"
            seb "Why don't you come and find out..."
            scene black with fade
            "The transmission cut out."
            scene bgAudioroom with fade
            sM "Sounds like he was expecting us..."
            y "You know him?"
            aM "We fought him a few times. He's caused riots in Beverly Hills before."
            sM "We managed to stop him then and we'll do it again! He was transmitting from this location, meet me there Alex."
            aM "Roger!"
            scene black with fade
            $ missionProgression = 6
            $ activeSpy = 1
            $ task23Stage = 4
            $ specialBossActive = True
            $ chanceOfControl = 0
            jump missionBegin

    if task23Stage == 4:
        $ task23Stage = 5
        hide spyCorner
        hide screen equipmentMenu
        show scene_darkening with d3
        show sebModel2:
            xalign 0.5 yalign 0.15 zoom 1.05
        with d3
        show green at le
        show yellow y31 at ri
        with d3
        a "There you are!"
        s "What did you do to Clover?!"
        seb "Clover? Oh she's right here..."
        hide sebModel2 with d3
        show red r100 at ce with d3
        pause 0.4
        a y28 "Clover! You're okay!"
        c "Y O U - A R E - S E B A S T I A N - A N D - Y O U - A R E - M Y - M A S T E R...."
        y "That doesn't sound good..."
        s g32 "We've seen this before! He's mind controlled her with his music!"
        a "Snap out of it, Clover!"
        c "I - W I L L - O B E Y - A N D - S P R E A D - D I S A S T E R....."
        hide red
        hide green
        hide yellow
        with d3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        "Clover attacks!"
        scene black
        $ randomBackground = 1
        $ interact2 = 0
        $ frontExit = 0
        hide obst1
        hide obst2
        $ randomObst1 = 0
        $ randomObst2 = 0
        $ backupAlexActive = True
        show globalImageDatabase:
            zoom 0.25
        show bossSeb:
            xalign 0.48 yalign 0.48 zoom 0.45 rotate 3
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        $ randomBossHP = 3
        with fade
        y "She's being controlled. Attack and break her free!"
        jump jumpStartScene

    if task23Stage == 5:
        $ _skipping = True
        scene bgDatabase with fade
        play music "audio/music/techdungeon.mp3"
        $ task23Stage = 6
        $ specialSebStatus = 2
        $ prisonersNew = True
        $ specialBossActive = False
        pause 1.0
        show scene_darkening with d3
        show green g31 at le
        show red r39 at ce
        show yellow y34 at ri
        with d3
        s "Clover...? Are you with us again?"
        c "Yeah... I think so."
        a y31 "That's enough Sebastian! You're going dow-...!"
        a y29 "...?"
        a "Where did he go?"
        c r32 "He must've ran away when we were fighting."
        a y28 "Nooo! We were so close to capturing him!"
        s g33 "I guess it's a mission failed then..."
        c r49 "................"
        y "Actually, I've got an idea..."
        y "We still have to shut down the signal. Everyone get to your stations and wait for my command."
        "The girls nod and return to the signal rooms."
        hide red
        hide green
        hide yellow
        with d3
        hide scene_darkening with d3
        scene black with fade
        stop music fadeout 2.0
        pause 0.4
        scene bgAudioroom
        show audioroom
        with fade
        play music "audio/music/ambient1.mp3" fadein 2.0
        sM "Sam, in position."
        aM "Alex here. Ready when you are."
        cM "What was this idea you had, [playerName]?"
        y "Here... instead of shutting down the signal, I've changed it a bit."
        cM "Changed it...?"
        y "You'll see~...."
        y "Okay get ready. On three...\nTwo....\nOne..."
        "{b}*Bleep*{/b}"
        "The girls change the signal at the same time."
        sM ".............."
        sM "Did it work...?"
        "???" "{b}*Groans*{/b}"
        sM "What was that?!"
        $ sebFace = 2
        show scene_darkening with d3
        show sebModel2 at ce with d3
        seb "I - A M - D R I F T - P U N K - A N D - I - P R O M I S E - T O - T U R N - M Y S E L F - I N~....."
        aM "!!!"
        aM "Sebastian...?"
        y "I changed the hypnotic message of the signal. The Drift Punk should be a lot more agreeable now."
        cM "Well done, [playerName]. We'll take Sebastian back to the base."
        seb "C O M E - V I S I T - M E G A - M I L K - F O R - 10 P E R C E N T - O F F - ON - M I L K S H A K E S~....."
        hide sebModel2
        hide scene_darkening
        with d3
        jump missionComplete
    if task23Stage == 6:
        $ task23Stage = 7
        $ specialSebStatus = 3
        $ sebFace = 1
        show green g54 at le with d3
        show sebModel2:
            xalign 0.5 yalign 0.15 zoom 1.03
        with d3
        seb "D R I F T - P U N K - I S - L A M E - A N D - I - H A VE - A - S M A L L - P E~....."
        $ sebFace = 2
        seb "{b}*Blinks*{/b}"
        seb "..........................."
        y "Back to normal?"
        seb "{b}*Ahem*{/b} So it would seem..."
        seb ".........................................."
        seb "Where the hell am I?"
        y "You're in the WOOHP detention area in Beverly Hills. See? All your friends are here!"
        tali "Hey."
        drag "Good to see you again, Seb."
        seb "..............................."
        seb "I was wondering where you two went..."
        seb "As for you my friend, I'm afraid you haven't accomplished much."
        seb "Drift Punk is made to last. We'll come back around when the backups kick in."
        y "And what makes you so sure about that?"
        seb "She guarantees it."
        y "She?"
        if specialCandyStatus == 3:
            s g53 "The Mastermind?"
        $ sebFace = 1
        seb "Oh? You haven't figured out who it is yet? Well don't let me spoil it for you~..."
        s g54 "Tell us Sebastian! The gig is up. We have ways of making you talk!"
        y "I'm not sleeping with him, if that's what you're suggesting!"
        seb "I didn't break the first time you girls caught me. Nor did I break the second time. You should already know torture doesn't work on me."
        s g52 "........................."
        s "WOOHP doesn't torture..."
        seb "Nice try Ms. Simpson. But we both know that isn't true."
        y "Simpson? You're last name is Sim-...?"
        seb "If you're unsure, why not check the WOOHP prison logs. I'm sure they'll clearify a lot."
        y "I don't think we'll get much out of this guy. Let's go Sam."
        hide scene_darkening
        hide green
        scene bgBase
        with fade
        show scene_darkening with d3
        show green g37 at le
        show red r16 at ce
        show yellow y33 at ri
        with d3
        c "What did he say?"
        s "..........................."
        y "He's not cooperating. Though he said something about torture."
        c "Torture?"
        if specialCandyStatus == 3:
            a y28 "Candy said the same thing!"
        s g40 "That's ridiculous! WOOHP does not torture its prisoners!"
        s g9 "I bet they all got together to make up this story to confuse us if they ever got captured!"
        c r10 "I dunno... We've seen WOOHP do some creepy stuff in the past."
        c "Remember that Jerry tied us up over burning lava and slowly lowered us down?"
        s g29 "But that was just a training mission! He wouldn't actually have killed us!"
        a y5 "Yeah... It's still a bit messed up how he paid an actor to be my boyfriend..."
        c r30 "And remember that time we had to sneak around the WOOHP HQ at night? That was super creepy!"
        s g38 "Well true, but..."
        s g39 "..........................."
        y "I guess Jerry has a few questions to awnser once we rescue him."
        y "Any idea who the 'she' is that Sebastian was talking about?"
        a "Could be anyone. We fought a lot of crazy villains in our day."
        y "Let's try capturing more gang leaders and see if that shines a light on things."
        y "Good work spies."
        s g1 "Heh, you kinda sound like Jerry when you say that."
        a y28 "He's sorta Jerry 2.0!"
        c r12 "Without the... 'tying up above burning lava' thing."
        y "Oh you'll be tied up soon enough."
        s g30 "Wha-...?"
        y "Goodnight ladies!"
        hide green
        hide red
        hide yellow
        with d3
        hide scene_darkening with d3
        pause 1.0
        "Computer" "Booting up WOOHP Bounty Board..."
        "Computer" "Target: Sebastian Saga\nStatus: Captured."
        "Computer" "Transferring funds..."
        $ cash += 1000
        $ randMoney = 1000
        call missionRewardMoney from _call_missionRewardMoney_96
        pause 1.0
        scene bgMap:
            zoom 0.5
        show expression "gui/mapGangs/gangRepGraphic.png":
            xpos 720 ypos 430
        show text _("{font=fonts/freshmarker.ttf}{size=+20}Drift Punk{/size}{/font}"):
            xpos 885 ypos 522
        show expression "gui/mapGangs/punkLt1Cap.png":
            xpos 825 ypos 600
        show expression "gui/mapGangs/punkLt2Cap.png":
            xpos 875 ypos 600
        show expression "gui/mapGangs/punkLt3Cap.png":
            xpos 930 ypos 600
        with longFade
        play sound "audio/sfx/defeatGang1.mp3"
        pause 2.5
        show expression "gui/disbanded.png" at disbanded:
            xpos 810 ypos 490
        play sound "audio/sfx/defeatGang2.mp3"
        pause
        scene bgBase with longFade
        $ gang2Active = False
        pause 0.5
        "New clothing options for Clover are available at the mall."
        jump base

default task24Stage = 0
default task24Name = ""
default task24Text = ""
image task24Door = "mission/extra/task24Door.png"

screen task24Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task24Text]"

label task24:
    if task24Stage == 0:
        $ task24Stage = 1
        show bgBase with fade
        show scene_darkening with d3
        show red r11 at ri with d3
        y "The reports of gang attacks from the Drift Punks seem to have gone down."
        c "Yeah..."
        y "And there's been fewer digital hacks lately!"
        c "Mhm hm..."
        y "Not to mention they haven't been playing their music too loudly at night!"
        c "Yes, hm, okay..."
        y "Also I'm selling you as a slave to a Nigerian warlord."
        c "Uh huh, yeah..."
        y "....................."
        y "Are you even listening to me?"
        c r29 "Huh? Oh sorry, [playerName]. I'm a bit distracted."
        c "I keep thinking of....{w} Kobolds."
        y "What?"
        c r1 "Kobolds. They're little creatures we came across in our last D&D session."
        y "You play D&D...?"
        c "I told you I was into nerdy stuff. I've been playing tabletop games with some people from Drift Punk."
        c r12 "My dungeon master mentioned wanting to get some Kobold miniatures, but couldn't because the guy that used to sell them is being held prisoner by the Outsiders."
        y "Wait... what was this about a dungeon master? Are you getting up to some freaky sex stuff..?"
        c r1 "If we plan a mission to the Carnival, I bet we could free him! I would buy so much junk for my cell from him!"
        c "Please send us on a mission, [playerName]!"
        y "I still don't understand everything you're saying, but if the Outsiders are holding a hostage, then I'm sure we can free him."
        "Clover squees and gives you a hug."
        hide red with d3
        hide scene_darkening with d3
        pause 0.3
        call qAccept from _call_qAccept_13
        pause 0.3
        scene bgMap:
            zoom 0.5
        with fade
        $ task24Stage = 1
        "A hostage is available for rescue at the Carnival."
        jump worldmap
    if task24Stage == 1:
        with fade
        $ task24Stage = 2
        $ randomBackground = 10
        show globalImageFaire:
            xalign 1.0 yalign 0.75 zoom 0.36
        show task24Door:
            xpos 130 ypos 52
        hide screen interactScreen
        $ randomExit = 0
        $ randomCover2 = 0
        $ randomCover1 = 0
        hide screen equipmentMenu
        show spyCorner:
            xalign 0.97 yalign 1.0 zoom 0.78
        hide black with fade
        "{b}*Knock* *Knock* *Knock*{/b}"
        "???" "Let me out, you hear! You'll be hearing from my lawyer!"
        y "That could be the store owner. Get him out of there."
        call screen interactScreenBonus
    if task24Stage == 2:
        $ task24Stage = 3
        play sound "audio/sfx/lock.mp3"
        show scene_darkening with d3
        shopOwner "Gah finally. The fools locked me up to paint the inside, but there were no open windows! I nearly sufficated on the paint fumes!"
        y "We've come to get you out."
        shopOwner "Wonderful, then I can finally get back to my store. Visit me at the mall and I'll have a reward for you."
        y "Okay, we can pull out now or continue."
        menu:
            "Continue mission" if True:
                hide task24Door
                hide scene_darkening
                show screen interactScreen
                show screen equipmentMenu
                $ missionProgression = 7
                scene black with qFade
                jump missionBegin
            "Pull out" if task25Stage == 0:
                hide task24Door
                hide scene_darkening with d3
                jump missionComplete


default task25Stage = 0
default task25Name = ""
default task25Text = ""
default vialActive = 0
screen potionsScreen:
    if vialActive == 1:
        add "bgs/ghosts.png"

screen task25Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task25Text]"

label task25:
    if task25Stage == 0:
        $ task25Stage = 1
        scene black with fade
        scene bgFaire
        show yellow y18 at ri
        show scene_camera
        with fade
        pause 0.6
        a "[playerName]? Alex here."
        a "There's... nobody at the amusement park."
        y "Nobody?"
        a y21 "No, it's completely empty. Kind of creepy..."
        a "I only found these strange bottles..."
        show scene_fighting with d3
        show screen potionsScreen
        show expression "gui/potions.png":
            xalign 0.5 yalign 0.45
        with d3
        pause 0.4
        y "Bottles...?"
        y "........................"
        y "They look like potions."
        a "Potions?"
        y "Yeah like magical alchemy drinks."
        label task25PotionDrink:
            pass
        menu:
            "Try the red one" if True:
                "Alex takes a sip of the red vial."
                "Nothing seems to happen."
                jump task25PotionDrink
            "Try the blue one" if True:
                "Alex takes a sip of the blue vial."
                "Nothing seems to happen."
                jump task25PotionDrink
            "Try the green one" if True:
                hide scene_fighting
                hide expression "gui/potions.png"
                with d3
                "Alex takes a sip of the green vial."
                with d3
        pause 0.5
        a y30 "!!!"
        y "Alex? Are you oka-...?"
        a y28 "GHOSTS!"
        y "Now Alex calm down, there's no such thing as g-..."
        a y42 "Eeeeeeeeeeh!"
        show yellow:
            linear 0.5 xalign -1.0 yalign 0.0
        pause 0.5
        "Alex ran away."
        y "..........................."
        hide yellow
        $ yellowDayJob = 3
        $ spy3Status = 1
        $ mapSpy3Selected = False
        hide screen potionsScreen
        scene black
        with fade
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task25Stage == 1:
        show scene_darkening with d3
        $ task25Stage = 2
        show yellow at ri
        with d3
        a y28 "[playerName]! Ghosts!"
        y "Alex are you okay...?"
        a "I'M SERIOUS!"
        show green at le
        show red at ce
        with d3
        s "What's going o-... Alex? You look like you've seen a g-"
        a "GHOST!"
        y "..................."
        c r16 "Alex, there's no such thing as ghosts."
        a y29 "But I saw them! A lot of them!"
        a "All the Outsiders turned into ghosts!"
        y "Okay, just relax. You're going back tomorrow. Maybe everyone was just out on a heist of something."
        a "But....!"
        y "If you're so worried, I'll send Sam and Clover along with you."
        a y5 "{b}*Whines Softly*{/b}"
        hide yellow with d3
        pause 0.4
        y "Wow.... I knew Alex was a scaredy cat, but she looks terrified."
        c r10 "Yeah... maybe she really did see something."
        s g12 "Tsk, she's just getting spooked by her own shadow again. Let's check it out tomorrow and see what's going on."
        hide red
        hide green
        with d3
        hide scene_darkening
        with d3
        "The girls head back to their cells for the night."
        jump base
    if task25Stage == 2:
        $ vialActive = 0
        if spy1Status != 0 and spy2Status != 0:
            "The other spies are not available and Alex refuses to go back alone."
            jump worldmap
        elif True:
            $ task25Stage = 3
            scene bgFaire
            show scene_darkening
            show yellow y30 at ri
            show red at ce
            show green g1 at le
            show screen potionsScreen
            show scene_camera
            with fade
            pause 0.5
            s "Now you see Alex. There's nothing to be afraid of."
            with d3
            a "A-are you guys not seeing them?!"
            c r16 "Seeing who?!"
            y "Wait a moment..."
            show scene_fighting with d3
            show screen potionsScreen
            show expression "gui/potions.png":
                xalign 0.5 yalign 0.45
            with d3
            pause 0.4
            "You grab the potions that Alex brought back with her."
            y "I wonder..."
            "You take a sip of the green one."
            hide scene_fighting
            show screen potionsScreen
            hide expression "gui/potions.png"
            pause 0.5
            $ vialActive = 1
            with d3
            pause 0.5
            y "!!!"
            y "Ghosts!"
            s g28 "Not you too, [playerName]!"
            a y28 "See? I told you!"
            "Agent" "Aaaahhh! Ghosts!"
            y "Sounds you're not entirely alone. Get busy investigating!"
            "The girls nod and get ready."
            hide red
            hide green
            with d3
            a y15 "{b}*Whines*{/b}"
            $ backupCloverActive = True
            $ backupAlexActive = True
            $ vialActive = 0
            hide yellow with d3
            scene black with fade
            pause 0.5
            $ missionScreenFrontlineSelect = 1
            $ hiddenStatus = 2
            $ intelCost = 0
            $ missionScreenCurrentLocation = 4
            jump missionScreenFinish
    if task25Stage == 3:
        $ task25Stage = 4
        $ randomCover1 = 0
        show globalImageFaire:
            zoom 0.25
        "Database" "Facial recognition complete. The Great Kand-..."
        hide kandModel with d5
        pause 0.3
        "Database" "Facial recognition lost."
        y "???"
        y "Where'd he go?"
        $ blueMagicBlock = True
        show magicwall with d3
        pause 0.3
        y "What the...?!"
        if activeSpy == 1:
            sM "It's... some kind of barrier."
        if activeSpy == 2:
            cM "It's... some kind of barrier."
        if activeSpy == 3:
            aM "It's... some kind of barrier."
        y "What is this voodoo shit?! There's no such thing as magic!"
        if activeSpy == 1:
            sM "Okay [playerName]. Calm down..."
        if activeSpy == 2:
            cM "Okay [playerName]. Calm down..."
        if activeSpy == 3:
            aM "Okay [playerName]. Calm down..."
        y "It's all just smoke and mirrors!"
        sM "Or... hallucinogens..."
        aM "Hallu-whatcha?"
        sM "We might be seeing things that aren't there. Remember those potions you found? I bet they're the cure."
        "Potions have been added to the Compowder menu."
        hide screen glassScreen with d2
        hide screen gadgetMenu
        $ glassMissActive = False
        $ bagItemsName = "Potions"
        $ blueMagicBlock = True
        show screen equipmentMenu
        $ renpy.pause(hard='True')
    if task25Stage == 4:
        $ task25Stage = 5
        y "It worked!"
        $ missionProgression = 5
        y "Go after him and bring him in!"
        scene black with fade
        jump missionBegin
    if task25Stage == 5:
        $ task25Stage = 6
        $ redMagicBlock = True
        $ kandHidden = False
        $ randomCover1 = 0
        show globalImageFaire:
            zoom 0.25
        show magicwall2 with d3
        pause 0.6
        y "Darn it. More smoke and mirrors! Pick the right potion and continue on!"
        hide screen glassScreen with d2
        hide screen gadgetMenu
        $ glassMissActive = False
        show screen equipmentMenu
        $ renpy.pause(hard='True')
    if task25Stage == 6:
        $ task25Stage = 7
        hide magicwall2 with d3
        if activeSpy == 1:
            sM "[playerName]. I don't think-..."
        if activeSpy == 2:
            cM "[playerName]. I don't think-..."
        if activeSpy == 3:
            aM "[playerName]. I don't think-..."
        y "SMOKE AND MIRRORS!"
        scene black with qFade
        show screen equipmentMenu
        jump missionBegin
    if task25Stage == 7:
        $ task25Stage = 8
        show magicwall3 with d3
        pause 0.6
        hide screen glassScreen with d2
        hide screen gadgetMenu
        $ glassMissActive = False
        y "Oh come on... another barrier? Switch it up a bit man."
        "???" "As you wish."
        scene bgBase
        y "AHH!"
        y "Who said that?!"
        with hpunch
        show expression "mission/fx/hall1.png":
            xalign 1.1 yalign 0.5
            linear 0.3 xalign 0.5 yalign 0.4
            linear 0.3 xalign 0.0 yalign 0.5
            alpha 0.0
        pause 0.3
        with hpunch
        show expression "mission/fx/hall2.png":
            xalign 1.1 yalign 0.5
            linear 0.3 xalign 0.5 yalign 0.4
            linear 0.3 xalign 0.0 yalign 0.5
            alpha 0.0
        pause 0.3
        with hpunch
        show expression "mission/fx/hall3.png":
            xalign 1.1 yalign 0.5
            linear 0.3 xalign 0.5 yalign 0.4
            linear 0.3 xalign 0.0 yalign 0.5
            alpha 0.0
        pause 0.8
        y "AHHH! I'm being haunted by the Halloween decorations!{w} THE IRONY IS NOT LOST ON ME!"
        scene black with qFade
        $ randomExit = 1
        $ currentPosition = 0
        $ randomCover2 = 1
        $ randomCover1 = 0
        $ randomBackground = 3
        show globalImageFaire:
            zoom 0.25
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
        with fade
        if activeSpy == 1:
            sM "Sounds like [playerName] has his hands full aswell. Let's finish this quick!"
        if activeSpy == 2:
            cM "Sounds like [playerName] has his hands full aswell. Let's finish this quick!"
        if activeSpy == 3:
            aM "Sounds like [playerName] has his hands full aswell. Let's finish this quick!"
        show kandModel:
            xalign 0.6 yalign 0.45 rotate 0.7 zoom 0.3
        with d3
        pause 0.4
        kand "Agreed. Let's get this over with..."
        $ randomBossHP = 3
        $ bagItemsName = "Potions"
        $ backupSamActive = True
        $ backupCloverActive = True
        $ backupAlexActive = True
        if activeSpy == 1:
            $ backupSamActive = False
        if activeSpy == 2:
            $ backupCloverActive = False
        if activeSpy == 3:
            $ backupAlexActive = False
        show shield1:
            xalign 0.58 yalign 0.44 rotate 0.7
        with d3
        $ blueMagicBlock = True
        show screen equipmentMenu
        call screen interactScreenBonus
    if task25Stage == 8:
        $ task25Stage = 9
        jump task25
    if task25Stage == 9:
        $ task25Stage = 10
        $ prisonersNew = True
        scene bgBase
        show scene_fighting
        show expression "mission/fx/hall1.png":
            xalign 0.5 yalign 0.5
        with fade
        y "Begon demon!"
        with hpunch
        show expression "mission/fx/hall1.png":
            linear 0.25 xalign 0.5 yalign 1.3
        pause 1.2
        hide scene_fighting with d3
        pause 0.6
        show scene_darkening with d3
        show green g32 at ri
        show red at ce
        show yellow at le
        with d3
        s "We're back."
        c r29 "What happened to the Halloween supplies?"
        a y28 "Did Kandinsky put a spell on them?!"
        y "There's no such thing as magic...! He must've... used slight-of-hand somehow...!"
        y "Smoke and mirrors!"
        c r12 "Well anyway... we put Kandinsky in a cell. Don't wait too long before interrogating him."
        hide green
        hide red
        hide yellow
        with d3
        "The girls return to their cell."
        $ bagItemsName = "Items"
        hide scene_darkening with d3
        $ specialKandStatus = 2
        jump base
    if task25Stage == 10:
        $ task25Stage = 11
        call undressSam from _call_undressSam_37
        call undressAlex from _call_undressAlex_29
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        show scene_darkening with d3
        show kandModel at ri with d3
        y "Okay magic man, the gig is up!"
        y "No more spells! No more magic! And no more tricks!"
        kand "Oh tricks? My spells are tricks to you?"
        show yellow y52 at le with d3
        a "Kandinsky! The gig is up!"
        y "Alex... I already said that..."
        kand "Oh to think the mighty Outsiders fell to a group of jokers like you..."
        kand "I'm not that surprised really. They weren't that threatening of a gang to begin with."
        y "Then why did the Mastermind bring them to Beverly Hills?"
        kand "Oh she didn't. They were always here."
        kand "She just boosted the ranks a bit and gave them funding, but it looks like the gang will fall apart soon without its leaders."
        show green g54:
            xalign 0.5 yalign 0.0 xzoom -1
        with d3
        s "The gig is up Kandinsky!"
        y "Sam... we already said that..."
        kand "Surely you didn't capture me just to put me in jail. I bet you want information."
        y "Yes! Tell us everything you know or we might get rough!"
        kand "Okay, here you go."
        $ randIntel = 600
        $ intel += 600
        call missionRewardInt from _call_missionRewardInt_21
        y "........................"
        y "That was easy..."
        kand "Oh please... I just ran that gang as a favor for the Mastermind for getting me out."
        kand "Honest, you did me a favor for getting rid of them."
        y "Yeah right... you forget that we captured you and put you back behind bars, Kandinsky."
        kand "Oh did you?"
        scene bgStreet2
        show yellow at le
        show green:
            xalign 0.5 yalign 0.0 xzoom -1
        show kandModel at ri
        with d5
        pause 0.3
        y "!!!"
        y "What the?!"
        y "GET HIM!"
        kand "Not so fast..."
        hide green
        hide yellow
        with d1
        $ greenOutfit = 0
        $ greenOutfitArms = 0
        $ yellowOutfit = 0
        $ yellowOutfitArms = 0
        $ greenUnder = 0
        $ yellowUnder = 0
        show yellow at le
        show green:
            xalign 0.5 yalign 0.0 xzoom -1
        with d3
        pause 0.7
        $ yellowArms = 2
        a y28 "Eeeeeh!"
        $ greenArms = 2
        s g29 "Eeeeeeeh!"
        y "What the...?!"
        y "Gotta admit... you're really good with those smoke and mirrors..."
        s "[playerName]! Get him!"
        kand "I will be taking my leave now... Goodbye everyone."
        kand "Until we meet again~...."
        hide kandModel with d5
        pause 0.5
        y "He... disappeared..."
        scene bgMap:
            zoom 0.5
        show expression "gui/mapGangs/gangRepGraphic.png":
            xpos 920 ypos 130
        show text _("{font=fonts/freshmarker.ttf}{size=+20}Outsiders{/size}{/font}"):
            xpos 1100 ypos 222
        show expression "gui/mapGangs/outsidersLt1Cap.png":
            xpos 1025 ypos 300
        show expression "gui/mapGangs/outsidersLt2Cap.png":
            xpos 1075 ypos 300
        show expression "gui/mapGangs/outsidersLt3Cap.png":
            xpos 1130 ypos 300
        with longFade
        play sound "audio/sfx/defeatGang1.mp3"
        pause 2.5
        show expression "gui/disbanded.png" at disbanded:
            xpos 1010 ypos 190
        play sound "audio/sfx/defeatGang2.mp3"
        pause
        $ specialKandStatus = 3
        $ gang3Active = False
        scene bgStreet2
        show green g39 at ce
        show yellow y14 at le
        with longFade
        y "Well... with their leaders gone. I don't think the Outsiders will give us anymore trouble."
        s g38 "Can we go home now, please?!"
        a y29 "Yeah, my nipples are hard enough to cut glass!"
        y "......................."
        y "All right, let's go."
        scene black with fade
        "You quickly make your way back to the base."
        scene bgBase with fade
        show scene_darkening with d3
        pause 0.5
        show green g54:
            xalign 0.5 yalign 0.0 xzoom -1
        show yellow y52 at le
        show red r56 at ri
        with d3
        c "What happened to you guys?!"
        s "Don't ask..."
        hide green
        hide yellow
        with d3
        pause 0.5
        y "It's a long story."
        c r16 "Does it so happen to involve Kandinsky? Cause... he escaped..."
        y "Yup..."
        y "He pulled his little slight-of-hand trick and took off."
        c r10 "Are you still saying it's just smoke and mirr-..."
        y "Yes!"
        c "................"
        c r12 "So what about the Outsiders?"
        y "With Kandinsky gone, they will fall apart soon enough. Looks like they'll disband."
        c r1 "Well that's one less gang to worry about..."
        hide red with d3
        hide scene_darkening with d3
        jump base

default task26Stage = 0
default task26Name = ""
default task26Text = ""
default intelWarning = True

screen task26Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task26Text]"

label task26:
    if task26Stage == 1:
        $ task26Stage = 2
        pause 0.7
        show scene_darkening with d3
        "???" "{b}*Static*{/b} ...you read me? Thi-....{b}*Static*{/b}"
        "???" "{b}*Static*{/b} ...-aptured. Held in the WOOHP HQ. I need h-...{b}*Static*{/b}"
        y "...?"
        scene bgBase with fade
        show scene_darkening with d3
        pause 0.3
        show yellow y28 at ri
        show red r32 at ce
        show green g31 at le
        with d3
        pause 0.5
        y "Did you girls hear that?"
        c "Yes. It sounded like..."
        s "Like..."
        a "Like Britney!"
        s g29 "Yes! It did sound like her!"
        y "Who?"
        c r14 "She's a fellow spy and a friend of ours."
        a y5 "It sounded like she was in trouble."
        y "..............................."
        y "I mean...."
        y "You know this is a trap, right?"
        c r10 "Oh yeah."
        s g14 "Definitely."
        a y2 "No question."
        y "............................."
        y "How hot is she?"
        c r22 "Flamin'."
        y "Let's go rescue her!"
        s g15 "{b}*Sighs*{/b}"
        hide green
        hide red
        hide yellow
        with d3
        hide scene_darkening
        with d3
        pause 0.3
        call qUpdated from _call_qAccept_14
        scene bgMap:
            zoom 0.5
        with fade
        $ task26Stage = 2
        show expression "gui/woohpIcon.png":
            xalign 0.2 yalign 0.1
        with d5
        pause 0.5
        $ mainQuestUpdate = True
        jump worldmap
    if task26Stage == 2:
        $ HQLiberated = 0
        $ task26Stage = 3
        pause 0.7
        show scene_darkening with d3
        show agentModel2:
            xalign 0.6 yalign 0.0
        show agentModel3:
            xalign 0.8 yalign 0.0
        show agentModel4:
            xalign 1.0 yalign 0.0
        y "Quickly! Set up in the basement. They don't know we're here yet."
        play sound "audio/voice/agent/doingAsImTold.mp3"
        "Agent" "Doing as I'm told!"
        hide agentModel2
        hide agentModel3
        hide agentModel4
        with d3
        pause 0.5
        call undressSam from _call_undressSam_15
        call undressClover from _call_undressClover_10
        call undressAlex from _call_undressAlex_14
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        show green g32 at ri
        show red r32 at ce
        show yellow y32 at le
        with d3
        pause 0.3
        y "Okay, it's time we begin the take over of WOOHP."
        y "The WOOHP HQ consists of multiple floors that we need to take back."
        a y16 "How are we going to do that...?"
        y "We can spend intel to figure out what's on the floor above us. Then we can send freed WOOHP agents to lead the assault."
        s g20 "Getting intel is probably going to prove difficult with the other gangs out of commission."
        y "That's where you three come in. We have a new mission area. The WOOHP HQ."
        y "I will plan missions for you girls. {w}Sneak through the headquarters and bring back as much intel as you can."
        c r18 "What about Britney?"
        y "She's probably being held on one of these floors. If we have enough intel we'll launch an assault and take back the building floor by floor."
        "The girls nod and get ready."
        $ missionAreaWOOHPActive = True
        hide red
        hide yellow
        hide green
        hide scene_darkening
        with d3
        call screen HQButtons
    if task26Stage == 3:
        $ task26Stage = 4
        scene bgPrison with fade
        show scene_darkening with d3
        show red r32 at ce
        show yellow y32 at le
        show green g32 at ri
        with d3
        pause 0.3
        y "It's.. a prison."
        s g16 "Yeah, the WOOHP asylum under the milkshake bar is tiny compared to this one..."
        a y28 "Look!"
        hide red
        hide green
        hide yellow
        with d3
        $ britneyHidden = False
        show britney b39 at ce with d5
        "Girls" "Britney!"
        brit b32 "Ugh....."
        c "Britney...?"
        brit b7 "...!"
        stop music fadeout 2.0
        hide britney with d2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        "Britney attacked! {w}... and was then prompty overpowered by your spies."
        show britney b29 at ce
        show yellow y54 at ri
        show red r54 at le
        with d3
        brit "W-what..?!"
        y "Oh come on, we knew it was a trap so we prepared."
        a y28 "Don't worry Britney! We'll have you back to normal in no time!"
        c r53 "Don't resist, you'll just have to come with us."
        brit b9 "........................"
        play music "audio/music/crisis.mp3" fadein 1.0
        brit b22 "{b}*Smirks*{/b}"
        c r56 "Britney...?"
        hide britney
        hide yellow
        hide red
        with d2
        with hpunch
        "Britney threw the spies off of her like they weigh nothing!"
        y "Uh oh...! Agents...!"
        show britney b24 at le
        show agentModel2:
            xalign 0.6
        show agentModel3:
            xalign 0.8
        show agentModel4:
            xalign 1.0
        with d3
        "Agent" "Hop! Hop! Hop! Hop!"
        show agentModel2:
            linear 0.4 xalign 0.1
        show agentModel3:
            linear 0.4 xalign 0.1
        show agentModel4:
            linear 0.4 xalign 0.1
        pause 0.4
        with hpunch
        show agentModel2:
            linear 0.35 xpos 1300 rotate 25
        show agentModel3:
            linear 0.35 xpos 1300 ypos -200 rotate 30
        show agentModel4:
            linear 0.35 xpos 1300 rotate 25
        pause 0.5
        y "Hey!"
        "Britney pulls out a dart gun and fires!"
        hide britney with d3
        "Girls" "Ow!"
        "Everyone of your girls got hit by a nano injector!"
        y "That can't be good..."
        sM "[playerName]...! Pull back!"
        show britney b22 at ce
        y "This isn't over yet!"
        brit "I'll be waiting..."
        hide britney with d5
        scene black with longFade
        pause 1.0
        scene cellNeutral with fade
        show green at le with d3
        y "In you go!"
        hide green with d3
        show screen cellDoor
        with d2
        pause 0.4
        "You shove the girls into their cells and lock the door."
        "Inside you see their eyes turning red as they glare at you through the glass."
        y "............."
        y "That might be a problem..."
        y "You girls hang in there! I'll break you out of your trance!"
        stop music fadeout 3.0
        scene black
        hide screen cellDoor
        with fade
        scene bgBase with fade
        $ spy1Status = 10
        $ spy2Status = 10
        $ spy3Status = 10
        $ task7Text = _("The conquest of WOOHP HQ has begun, but a spy in blue stands in your way. She has infected with the girls with a powerful new set of nanobots that require some extra dedication to break.")
        $ task26Stage = 4
        jump base
    if task26Stage == 4:
        $ slutLevel = 5
        $ sexAct5 = "Anal"
        $ task26Stage = 5
        scene cellNeutral
        show green g100 at ce
        show screen cellDoor
        with fade
        pause 0.7
        y "Well hello there Sam. You're looking nice and...{w} murdery."
        s "{b}*Growl*{/b}"
        y "So I'm just gonna assume that to break you out of it, we're just going to have sex again."
        y "However... my father taught me never to stick my dick in crazy.{w} At least not without proper protection!"
        s ".....?"
        "You take out a rope."
        y "Okay now I'm going to open the cell...~"
        hide screen cellDoor with d3
        y "Okay good... easy no-...."
        hide green with d2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        y "Ow! You brat!"
        "Sam bit you!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.4
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        "After a short struggle you manage to get the upper hand on Sam and tie her up!"
        y "Okay Sam listen! I know you're not yourself right now...{w} but I'm going to fuck you in the butt."
        s "!!!"
        y "You can get mad at me later."
        scene black with fade
        jump samSex5
    if task26Stage == 5:
        $ task26Stage = 6
        scene black with fade
        pause 0.5
        scene cellNeutral with d3
        show scene_darkening with d3
        pause 0.4
        call undressSam from _call_undressSam_17
        show green g14 at ce with d3
        pause 0.6
        y "Saaaam...?"
        s "..................................."
        s "Did we just....?"
        y "Yup."
        s "In the..."
        y "In the butt. Yes."
        s g11 "..............."
        s "That was...."
        y "................"
        s g13 "That was the hottest thing I've ever done."
        y "Wait... I'm not in trouble?"
        s g1 "Of course not! I was in trouble and you figured out the best way to get me back to my sense."
        s "We should quickly move on to the other girl-...{w} Ow ow ow~...."
        y "I'll handle them. You should maybe grab a shower... and not sit down for a while."
        s g5 "......................."
        "Sam rubs her butt with a pained expression."
        hide green
        hide scene_darkening
        with d3
        pause 0.8
        "Cell Next Door" "LET ME OUT! I WANT TO PLAN A COUP IN SWAZILAND!"
        y "Calm your horses! The country isn't even called that anymore!"
        scene black with fade
        "You quickly move on to the other girls and after a long night of buttfuckin' everyone is back to their senses."
        y "Phew~... still got it in me."
        "Tired, but thoroughly satisfied, you head to bed."
        $ sexAct5 = _("Anal")
        $ task7Text = _("The conquest of WOOHP HQ has begun, but a spy in blue stands in your way. Continue liberating WOOHP and capture her!")
        jump nightCycle
    if task26Stage == 6:
        $ task26Stage = 7
        scene bgEngineer with fade
        pause 0.5
        show scene_darkening with d3
        show yellow y52 at le
        show red r54:
            xalign 0.2 yalign 0.0 xzoom -1
        show green g54:
            xalign 0.4 yalign 0.0 xzoom -1
        with d3
        play music "audio/music/daytime.mp3" fadein 2.0
        y "Hah! Level two! Now to get that flaming hot piece of ass~...."
        show O5O at ri with d3
        O5O "RIGHT HERE!"
        y "................"
        y "You're not the hot piece of ass I'm looking for.{w} Who are you?"
        O5O "AGENT O5O! YOU REMEMBER ME!"
        y "Er...."
        O5O "I'M A MAIN ANTAGONIST!"
        y "..............."
        menu:
            "'I remember you!'" if True:
                y "You were at the base before this whole mess began!"
                y "Man, how could I ever forget you Agent O5O, you've played such an important role so far."
                y "Remember that one time we went to liberate Alex from the school and you were there?"
                y "Ah yes, good old Agent O5O. Everyone's favorite agent and {i}'definitely'{/i} not completely forgotten by Exiscoming."
            "'I don't remember you.'" if True:
                O5O "HOW COULD YOU FORGET ME?! I'M THE MOST LOVABLE SIDE CHARACTER IN THE STORY!"
                O5O "REMEMBER WHEN YOU FIRST BROKE OUT? I WAS THERE!"
                O5O "AND WHEN YOU WENT TO RESCUE YOUR SPY IN YELLOW. I WAS GIVING A SPEECH AT THE SCHOOL THAT DAY!"
                y "................................."
                O5O "YOU DON'T REMEMBER ME, DO YOU...?"
                y "I don't even think Exiscoming remembered you."
        s g16 "You know this agent, [playerName]?"
        O5O "OH YES, ME AND HIM GO WAY BACK!{w} I WAS THERE WHEN HE WAS STILL A WOOHP INMATE!"
        c r56 "A what?"
        y "Oh no no no, we don't have to go into th-..."
        O5O "LOOKING ALL COOL AND EDGY IN HIS PRISONER UNIFORM. I REMEMBER IT LIKE IT WAS YESTERDAY!"
        a y29 "Prisoner uniform...?"
        y "Dude, shutupshutupshutup!"
        O5O "MAN I REMEMBER THE DAY THEY LOCKED YOU UP! YOU WERE SUCH A MENACE TO SOCIETY!"
        O5O "JUST SEEING YOU WALK AROUND FREE MAKES ME NERVOUS!"
        s g31 "What is he talking about, [playerName]?"
        y "Oh well you see, I....{w} HE'S GOT A GUN, GET HIM!"
        O5O "W-WHA-....?"
        show red r34:
            linear 0.15 xalign 0.9
        show green g32:
            linear 0.15 xalign 0.9
        show yellow y31:
            linear 0.15 xalign 0.9
            pause 0.4
        with hpunch
        hide O5O
        hide green
        hide red
        hide yellow
        with d2
        pause 0.8
        show yellow y38 at le
        show red r18 at ce
        show green at ri
        with d3
        a "Target restrained!"
        y "Good work girls. That opens up the second level of the WOOHP HQ. Only a few more levels and we'll take this place back for good!"
        c r18 "So [playerName]... what was this thing about you being a pri-..."
        y "Yes indeed! With some elbow grease and a 'Can do!' attitude we'll make it through here!"
        s g10 "[playerName]...."
        y "High fives all around! We'll take back WOOHP and then be on our merry way!"
        a y5 "[playerName]...."
        a "Are you a badguy?"
        y "........................"
        show agentModel4:
            xpos -550 yalign 0.2 xzoom -1
            linear 0.9 xpos -480 rotate 7
        show agentModel3:
            xpos 800 yalign 0.2
            linear 0.9 xpos 700 rotate -7
        pause 0.9
        y "Shhh, not in front of the agents."
        stop music fadeout 2.0
        y "We'll talk back at the base..."
        play music "audio/music/nighttime.mp3" fadein 1.0
        scene black with fade
        scene bgBase with longFade
        jump base
    if task26Stage == 7:
        $ task7Text = _("The conquest of WOOHP HQ has begun, but a spy in blue stands in your way. Continue liberating WOOHP and capture her!")
        $ task26Stage = 8
        if HQLiberated >= 3:
            $ HQLiberated = 2
        show scene_darkening with d3
        show green g32 at ri
        show red r32 at ce
        show yellow y32 at le
        with d3
        y ".............................."
        y "Okay.... so I can explain..."
        c r31 "You're a WOOHP inmate?"
        menu:
            "'Yes, I am'" if True:
                y "Yes."
                c "................"
                c r11 "Well at least he's honest about it..."
                s g38 "Almost confident."
                a y28 "Are you proud of it?!"
                y "Not gonna lie. I'm a little proud of fooling everyone for this long."
                c r10 "............................"
                c "Okay... fair enough."
            "'No, I'm not'" if True:
                y "No. I'm not."
                "Inner Voice" "(You know you're just digging your grave deeper and deeper~....)"
                s g18 "You're not?"
                y "......................"
                y "Okay I cave easily under pressure!{w} I am a phony!"
            "...................." if True:
                y "(Maybe if I stay very still they won't see me...)"
                s g10 "[playerName]...?"
                y "(I think it's working...)"
                c r11 "......................"
                play sound "audio/sfx/punch1.mp3"
                with hpunch
                "Alex kicked you in the shin!"
                y "Ow! Okay okay, I'm sorry. Yes I sorta... neglected to tell you I was an inmate."
        a y28 "I can't believe it...{w} I got my pussy pounded by a perverted punk penetrating perpetrator!"
        y ".................."
        c r11 "{b}*Sighs*{/b} Not now Alex...."
        y "Now before you guys get too mad. I've got a good explaination!"
        s g10 "Yeah? Let's hear it."
        y "............................."
        y "I needed a suit for a job interview."
        s "..........................."
        c "..........................."
        a "..........................."
        y "............................"
        s g18 "You... expect us to believe that...?"
        c r24 "I believe him. That's one of the less crazy things he's done so far."
        a y1 "Yeah that sounds pretty in character for him."
        s g39 "..............."
        s g38 "[playerName]..."
        s "I hate to admit it, but..."
        s g10 "We wouldn't have made it this far without you."
        s g1 "Despite this one little 'oversight'. You've been with us all the way."
        s "You might be a crazy pervert, but that's exacly what we needed..."
        s g13 "So no worries. We'll talk to Jerry once this is done and make sure he grants you a pardon."
        y ".........."
        c r16 "What were you in for anyways?"
        y "I have a habit of causing large iceberg related incidents."
        c r10 "..............."
        c r12 "I'm not sure why I asked..."
        hide red
        hide yellow
        hide green
        with d3
        hide scene_darkening with d3
        pause 0.5
        y ".........................."
        "Inner Voice" "That could have gone worse."
        y "Yeah they were surprisingly understanding."
        "Inner Voice" "We seem to have a good thing going here. Please, no more iceberg incidents, okay?"
        y ".........................."
        jump base
    if task26Stage == 8:
        $ task26Stage = 9
        $ freedAgents -= 10
        call undressSam from _call_undressSam_19
        call undressClover from _call_undressClover_13
        call undressAlex from _call_undressAlex_17
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        $ task7Text = _("Britney is proving to be a challenge to bring in. We'll have to deal with this problem head on.\n\n-Plan a mission to WOOHP HQ to bring back Britney.")
        scene bgPropaganda with fade
        show scene_darkening with d3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        show agentModel4:
            xpos -350 yalign 0.1
            linear 0.7 xpos 1950 rotate 55
        pause 0.7
        show agentModel5:
            xpos -350 yalign 0.1
            linear 0.7 xpos 1950 yalign 1.0 rotate 45
        pause 0.7
        show agentModel3:
            xpos -350 yalign 0.1
            linear 0.7 xpos 1950 yalign 1.0 rotate 80
        pause 1.4
        show britney b54 at le with d3
        pause 0.2
        brit "Grrr...."
        y "We meet again..."
        y "This time I came prepared!"
        y "{b}*Click* *Click*{/b}"
        show green g17 at ri with d3
        s "You brought a gun?!"
        y "Yeah! It's funny how we always try the best solutions last, isn't it?"
        s g40 "We're not shooting her!"
        y "We're not...?"
        show red r18:
            xalign 1.1 yalign 0.0
        with d3
        c "Can't you just buttfuck her to bring her back to her senses?"
        y "............................"
        y "Oh right, I forgot that was an option."
        s g9 "How did you forget that...?"
        c r57 "Britney listen...! We're here to get you ou-..."
        show britney:
            linear 0.2 xalign 0.9
        pause 0.2
        hide red
        hide green
        hide britney
        with d1
        "Britney attacked your spies!"
        y "Yeah! Go girls, you've got this!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        s "Ow!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        c "No no no, not my hair!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        a "She bit me!"
        y "Y-yeah... go girls... you can do it~...."
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.5
        "All your spies were knocked out."
        show britney at ri with d3
        y "......................"
        y "Truce?"
        play sound "audio/sfx/punch1.mp3"
        scene black
        with hpunch
        pause 1.5
        scene bgPropaganda with longFade
        show scene_darkening with d3
        show green g32 at ri
        show red r33 at ce
        show yellow y29 at le
        with d3
        a "He's waking up..."
        y "................................"
        y "I take it we didn't win?"
        c "Depends what you mean by winning..."
        s g31 "The floor is ours, but Britney retreated higher into the building."
        s "She took out nearly a dozen of our agents in the process."
        y "That sounds like something we need to deal with before capturing the next floor."
        s g32 "Agreed. Plan a mission to the WOOHP HQ and we'll bring her back!"
        a y1 "Yeah! Then you can buttfuck her!"
        y "All right, sounds like a plan."
        hide green
        hide yellow
        hide red
        hide scene_darkening
        with d3
        pause 0.5
        "You're getting closer to capturing Britney. She fled higher up into the building. Plan a mission for the girls to get her back."
        scene black with fade
        jump jobReport
    if task26Stage == 9:
        $ task26Stage = 10
        call undressSam from _call_undressSam_20
        call undressClover from _call_undressClover_14
        call undressAlex from _call_undressAlex_18
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        $ task7Text = _("Britney has been captured! I should visit her in her cell to break her nanobot control.")
        pause 1.0
        show scene_darkening with d3
        show yellow y57 at le
        show red r15 at ce
        show green g14 at ri
        with d3
        s "We put her in a cell."
        y "Are you guys all right?"
        s g18 "A little bruised, but okay.{w} Are you going to... y'know."
        y "Fuck her silly. Yup, that's the plan."
        a y1 "I brought you a condom you can use!"
        y "........................"
        y "Oh right... condoms...{w} I forgot these things were a thing... {w}Remind me to buy pregnacy tests for you girls."
        c r30 "O-oh... right..."
        hide green
        hide red
        hide yellow
        with d3
        $ prisonersNew = True
        jump base
    if task26Stage == 10:
        $ task26Stage = 11
        pause 0.4
        show scene_darkening with d3
        show britney b12 at ri with d3
        $ task7Text = _("Britney's control has been broken, she can now help us liberate the rest of WOOHP HQ and is available as a new Backup option during missions.")
        brit "So this is where you've been hiding? This is a pretty shitty base."
        y "Hey, don't talk bad about my base!"
        brit b18 "And what's with these cells? Don't tell me you guys actually sleep in one aswell."
        y "Well..."
        brit b38 "Gawd, I'm glad there's no ugly wallpaper, else I'm sure it'd be peeling off. This place is a dump."
        brit "And what's with those decorations in the bar? Lame~...."
        y "Well aren't you just a joy to talk to.{w} Hang on a minute."
        brit b11 "And it smells in here. Ever heard of an air purifier?"
        brit "Also, who takes [daysPlayed] days to accomplish their mission? You guys are seriously so slo-..."
        $ britGag = True
        brit b29 "Mph!"
        y "There we go. Some peace and quiet."
        brit b7 "{b}*Angry Muffled Noises*{/b}"
        y "And just to make sure you don't attack me, I brought some ropes!"
        brit b29 "{b}*Muffled*{/b}?"
        y "Yes, ropes. For all the sex we'll be having!"
        brit "!!!"
        scene black with longFade
        brit "Mphff! Mhfp! Mhp!!!"
        brit "Umpfh! Mphf! Mphf!"
        brit "Mhmh!! ♥♥♥"
        y "And one more for the photobook~..."
        play sound "audio/sfx/camera.mp3"
        hide white with d2
        show expression "gui/photos/other/picBritney.jpg":
            xalign 0.5 yalign 0.5
        pause
        hide expression "gui/photos/other/picBritney.jpg"
        with d3
        "A new photo has been added to your photoalbum."
        $ britSuit = 0
        scene bgPrison with fade
        show scene_darkening with d3
        show britney b38 at ri with d3
        $ backupBritneyActive = True
        y "There we go, all better!"
        brit "{b}*Mphffh~...*{/b}"
        y "Oh right, let me untie you."
        "............{w}............{w}............"
        $ britGag = False
        y "There you go! Welcome to the family."
        brit b11 "............."
        brit b12 "My butt hurts."
        y "Er... sorry about that."
        show yellow y56 at le
        show red r55:
            xalign 0.3 yalign 0.0 xzoom -1
        show green g55:
            xalign 0.5 yalign 0.0 xzoom -1
        with d3
        a "Britney!"
        s "Are you okay? I hope [playerName] wasn't too rough with you."
        brit b55 "It's the more... unorthodox way of interrogation, I'll give him that."
        brit "I'm okay though. I'm guessing you guys are the resistance?"
        y "I guess you could call it that. We're working on taking back WOOHP and liberating the city."
        brit "By.... buttfucking?"
        y "No...{w} Well yes...{w} I mean that's part of it... it's complicated!"
        s g54 "We're slowly making our way up WOOHP HQ. We're working on figuring out who the mastermind is and put a stop to them!"
        brit "Wait... you guys don't know who the mastermind is?"
        y "Er... no. None of the gangleaders told us."
        brit "..........................."
        brit b52 "Okay girls... you might want to sit down for this..."
        stop music fadeout 2.0
        scene black with longFade
        $ britSuit = 1
        scene bgWOOHP
        show gladis:
            xalign 0.5 yalign 0.0
        with fade
        brit "The mastermind is someone we used to know..."
        brit "And... I can sort of empathise with her and her reasons for taking over WOOHP..."
        a "Who? Who is it?!"
        brit "Girls... It's..."
        play music "audio/music/sinister.mp3"
        brit "It's GLADIS."
        hide gladis with d2
        $ gladisHidden = False
        scene bgWOOHP2
        show scene_darkening
        show gladis:
            xalign 0.5 yalign 0.0
        with d5
        pause
        scene bgBase
        show britney at ri
        show yellow y56 at le
        show red r56:
            xalign 0.3 yalign 0.0 xzoom -1
        show green g56:
            xalign 0.5 yalign 0.0 xzoom -1
        with fade
        s "!!!"
        c "!!!"
        a "!!!"
        y "!!!"
        y "Not GLADIS!"
        y ".............."
        y "Who's GLADIS?"
        c r29 "She's an AI... an old friend of ours."
        a y28 "She used to give us our gadgets!"
        s g30 "We... never really found out what happened to her. Just that Jerry got fed up with her bossy personality."
        brit b52 "He had her recycled."
        s g56 "But...! GLADIS is a fully aware and functional AI! That's like killing her!"
        brit "Exactly."
        a y5 "Jerry had GLADIS killed...?"
        brit "Tried to."
        brit "One of the original designers of GLADIS was afraid something like this could happen and programmed in a backdoor."
        a y56 "That must've been one clever scientist!"
        brit "You know him well..."
        brit "It was Tim Scam."
        s g52 "!!!"
        s "Tim worked on GLADIS?!"
        a "He was the one to save her?!"
        c r57 "But that's good! {w}...Right?"
        brit "Her consciousness was automatically transfered to the WOOHP database when they disassembled her."
        brit "But she now had acces to all of WOOHP's top secret information."
        brit "It seems WOOHP has been up to some less than honest business."
        s g57 "What do you mean...?"
        $ jerryFace = 1
        $ jerryArms = 1
        scene bgOffice
        show jerryModel at ce
        with fade
        brit "Gerald James Lewis. Better known as Jerry, is the founder of the World Organization Of Human Protection."
        brit "In a few decades he turned his company into the number one private anti-terror organization in the world. Complete with a full private military and an arsenal of missles."
        scene bgBase with fade
        show yellow:
            xalign -0.2 yalign 0.0 xzoom -1
        show red:
            xalign 0.0 yalign 0.0 xzoom -1
        show green:
            xalign 0.2 yalign 0.0 xzoom -1
        show britney at ri
        with d3
        a y28 "Oh I remember that! We almost started a new world war during Christmas because of that."
        brit "Jerry has been getting his funding from countries around the world, but the way he went about it was shady to say the least."
        brit "In return for keeping the world safe, WOOHP was allowed to operately entirely outside of the law."
        s g53 "But Jerry would never do anything Illegal!"
        c r54 "........................"
        c "Sam, he kidnapped us and then forced us to join WOOHP as spies. We were sixteen when we joined!"
        a y53 "Yeah, and he spies on us 24/7!"
        brit b52 "Same goes for all of us. His little spy project recruits young teens and turns them into anti-terror agents."
        s g40 "Well... okay that's pretty bad, but we {i}want{/i} to be spies!"
        s "And I have never heard anyone say a bad word about WOOHP!"
        brit "Never?"
        s "Never!"
        brit "And you don't find that frightening?"
        s g57 "What do you mean...?"
        c r18 "Now that you mention it... How come WOOHP is allowed to do this without any opposition?"
        s g31 "Cause WOOHP is a force for good in the world!"
        c "And there is not a single person who worries about giving a privately owned company this much power?"
        brit "Any political critique is quickly silenced."
        s g54 "You mean... WOOHP bribes politicians?"
        brit "In the good cases, yes.{w} Some of them are simply blackmailed or threatend."
        s "....................."
        brit "Not to mention their weapon development branch. Those gadgets we use are cute and handy when we use them, but can easily be turned into weapons."
        s g57 "......................"
        brit "GLADIS saw everything this company was up to. The bribes, the kidnappings, the blackmail and concluded that WOOHP is basically holding the world hostage."
        brit "That's why she planned an attack on WOOHP. To get rid of Jerry and this company once and for all."
        c r53 "But something doesn't add up..."
        c "If GLADIS sees WOOHP as dangerous, why would she use gangs and criminals to help overthrow it? Doesn't that just make the world more volatile?"
        brit "Do you see any gangs around?"
        play sound "audio/voice/clover/erm3.mp3"
        c r56 "Yeah of course there's the... erm..."
        c r57 "..................."
        c "No, I think we disbanded all of the gangs..."
        brit "Exactly. She expected there to be a resistance to fight back. Basically she killed two birds with one stone."
        brit "Take WOOHP out of the picture and destroy the largest gangs in the USA."
        c ".................."
        c "So she played us? All of us?"
        s g56 "But what about re-taking the WOOHP HQ? We're getting closer and closer to freeing Jerry. Was that her plan aswell?"
        brit "Maybe.{w} I don't know what she's planning now."
        y "............................"
        y "I don't like this. It smells like a trap. If we've been playing into her hands all this time, who knows what she has waiting for us at the top of WOOHP HQ..."
        brit b45 "That's why I want to help you... I'm partically responsible for this mess..."
        y "...................."
        y "I bet you'd look pretty cute in a waitress uniform."
        s g8 "[playerName]!"
        brit b1 "No he's right. I'm happy to help you guys out and it would help my nanobot suppressed by working here."
        y "In that case... Alex go find her a uniform that fits."
        a y1 "Okidokie!"
        hide yellow
        hide britney
        with d3
        pause 1.0
        c r11 ".............................."
        s g15 ".............................."
        s "Tim saved GLADIS...?"
        s g14 "I... I need some time to process this..."
        y "We'll continue doing what we have been doing. With Britney by our side, we should be able to continue freeing the WOOHP HQ."
        c r10 "And what if it's a trap?"
        y "We'll deal with anything this GLADIS throws at us."
        y "For now get some rest. We'll continue this again tomorrow."
        "The girls nod and head back to their cells."
        hide green
        hide yellow
        hide red
        with d3
        hide scene_darkening with d3
        pause 0.6
        call qUpdated from _call_qUpdated_10
        jump base
    if task26Stage == 11:
        pause 0.5
        $ task26Stage = 12
        $ britSuit = 2
        scene bgBar with fade
        show scene_darkening with d3
        show britney b49 at ri with d3
        pause 0.4
        $ task7Text = _("Britney has told us about the Mastermind. Someone or something called GLADIS. Not far to go now. We should continue taking back floors of the WOOHP HQ.")
        brit b49 "Well.... this is more revealing than I'm used to..."
        show yellow y55 at le with d3
        a "You'll get used to it!"
        play sound "audio/sfx/slap.mp3"
        with hpunch
        brit b30 "!!!"
        "Alex slaps Britney's butt cheerfully."
        scene black with fade
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap
    if task26Stage == 12:
        pause 0.5
        $ task26Stage = 13
        scene bgFashion with fade
        pause 0.5
        call undressSam from _call_undressSam_32
        call undressClover from _call_undressClover_21
        call undressAlex from _call_undressAlex_25
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        show scene_darkening with d3
        show green g43 at ri
        show red r10 at ce
        show yellow y1 at le
        with d3
        pause 0.5
        y "Hey, I recognise this place!"
        s g5 "Yeah I had a mission here."
        y "Oh right, this is where that Melody chick was having her party."
        s "Yeah..."
        y "Still hung up about that?"
        s g43 "A little......"
        s g45 "The Aces really had become friends at this point. Betraying her felt... bad."
        y "Take comfort in the fact that you made this world a safer place with her behind bars."
        s g5 "Yeah I guess...."
        c r31 "Doesn't look like this floor was guarded. Only two more to go."
        y "All right, let's go!"
        c r37 "......................"
        y "No?"
        c r12 "[playerName]... We've been thinking."
        c "If we get nanocontrolled again, there's a good chance this entire mission will fail."
        y "I'll just fuck you guys back to your senses!"
        s g4 "Well... true, but with all the nanobot updates..."
        a y29 "You'd have to fuck us a lot to keep us in check!"
        y "..........................."
        y "Again... I don't see the problem here."
        s g14 "All we're saying is... that..."
        c r24 "There might be a way to reduce all of our nanobot levels at the same time."
        y "How'd we do that? I can only have sex with you one... at... a... ...."
        y "Wait....! Are you suggesting...?!"
        y "A hot~..."
        s g1 "{b}*Nods*{/b}"
        y "Sweaty~...."
        c r22 "He's getting there..."
        y "Messy~...."
        a y25 "FOURSOME!"
        y "....................."
        y "{b}*Sniff*{/b} You girls are too good to me... What have I done to deserve this?"
        s g38 "We're doing this for the safety of the mission of course."
        s g19 ".................."
        $ greenBlush = 1
        s g48 "But we're also kind of doing it as a way to say {i}'thank you'{/i}."
        c r3 "For all the trouble you've been through and all the help you've given us."
        a y1 "It's the least we could do!"
        y "You girls~...."
        y "Wait...! Can I make one more request?"
        c "Sure."
        y "Can you keep your suits on...?"
        c r18 "Our... suits?"
        s g16 "But how would you... y'know...?"
        y "Oh you'll see~...."
        y "For now head back to the base!"
        hide red
        hide yellow
        hide green
        scene black with fade
        scene bgMap:
            zoom 0.5
        with fade
        $ sexAct6 = "Foursome"
        $ greenBlush = 0
        jump jobReport
    if task26Stage == 13:
        $ task7Text = _("Capture Tim Scam!")
        stop music fadeout 1.0
        pause 0.5
        $ task26Stage = 14
        scene bgIntel with fade
        pause 0.5
        show scene_darkening with d3
        show agentModel2:
            xalign 0.0 yalign 0.0 xzoom -1
        show agentModel3:
            xalign 0.2 yalign 0.0 xzoom -1
        show agentModel4:
            xalign 0.5 yalign 0.0 xzoom -1
        play music "audio/music/sinister.mp3"
        "Agent" "One... two... three!"
        show agentModel2:
            linear 0.5 xalign 1.7
        show agentModel3:
            linear 0.5 xalign 1.7
        show agentModel4:
            linear 0.5 xalign 1.7
        pause 1.0
        play sound "audio/sfx/laser1.mp3"
        with flashbulb
        pause 0.4
        play sound "audio/sfx/laser1.mp3"
        with flashbulb
        "Agents" "AAHHHH!"
        hide agentModel2
        hide agentModel3
        hide agentModel4
        show agentModel2:
            xalign 1.7 yalign 0.0
            linear 0.5 xalign 0.0
        show agentModel3:
            xalign 1.7 yalign 0.0
            linear 0.6 xalign 0.1
        show agentModel4:
            xalign 1.7 yalign 0.0
            linear 0.7 xalign 0.05
        pause 0.7
        show agentModel2:
            linear 0.1 xalign -1.7 yalign 1.9 rotate -20
        show agentModel3:
            linear 0.1 xalign -1.5 yalign 2.0 rotate -30
        show agentModel4:
            linear 0.2 xalign -1.3 yalign 2.5 rotate 10
        pause 0.1
        play sound "audio/sfx/explosion1.mp3"
        hide agentModel2
        hide agentModel3
        hide agentModel4
        with flashbulb
        pause 0.6
        show timModel at ce with d3
        tim "......................."
        y "TIM! We're taking you in!"
        tim ".............."
        tim "And you are...?"
        y "Oh.... right.{w} We haven't met yet."
        call undressSam from _call_undressSam_21
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        show green g54 at le with d3
        s "............................"
        tim "...................."
        tim "I should have known..."
        s "It's over Tim. Please come quietly."
        tim "If you knew only half of the things WOOHP gets up to, you would not be my enemy, Sam."
        s "We know. Britney told us."
        s "But you're still a renegade agent and brought Beverly Hills to its knees."
        tim "......................"
        s "It's over Tim. Come with us."
        tim "It's not over yet.{w} GLADIS!"
        hide green
        play sound "audio/sfx/doorClose.mp3"
        show expression "gui/metalDoor.jpg":
            xalign 0.5 ypos -720
            linear 0.3 ypos 0
        show green g54 at le
        s g29 "!!!"
        "An emergency door suddenly closes between Tim and the girls."
        y "Oh come on, we were so close! Get after him!"
        hide green
        with d3
        hide scene_darkening with d3
        scene black with fade
        $ missionScreenFrontlineSelect = 1
        $ missionScreenSupportSelect = 2
        $ missionScreenDistractSelect = 3
        $ missionScreenBackup1Select = 2
        $ missionScreenCurrentLocation = 5
        $ missionSetting = "WOOHP"
        $ specialBossActive = True
        $ missionProgression = 0
        $ randomBossHP = 3
        jump missionScreenFinish
    if task26Stage == 15:
        $ task7Text = _("Tim Scam has been captured, now all that's left is to bring down GLADIS.")
        $ task26Stage = 16
        stop music fadeout 1.0
        scene bgIntel with fade
        show scene_darkening with d3
        show timModel at ri
        play music "audio/music/sinister.mp3" fadein 2.0
        tim "A little help here GLADIS! I'm running out of nets!"
        "........................."
        tim "GLADIS...?"
        show yellow y53:
            xalign 0.0 yalign 0.0 xzoom -1
        show red r54:
            xalign 0.2 yalign 0.0 xzoom -1
        show green g54:
            xalign 0.5 yalign 0.0 xzoom -1
        with d3
        hide timModel
        show timModel at ri
        a "Nowhere left to run Tim!"
        c "We've got you now!"
        tim "................."
        "{b}*Click* *Click*{/b}"
        tim "...?"
        s g56 "What was that...?"
        "All of you carefully look up and see..."
        y "Gun turrets!"
        tim "GLADIS! STOP!"
        show timModel:
            linear 0.1 xalign 0.5
        pause 0.1
        play sound "audio/sfx/laser1.mp3"
        hide green
        hide red
        hide yellow
        hide timModel
        with flashbulb
        y "Clover! Hack into those turrets!"
        cM "On it!"
        pause 0.5
        y "Are you two all right?"
        show green at le
        show timModel at ce
        with d3
        s g38 "I'm fine. Tim pushed me out of the way just in time."
        s g56 "You... saved me."
        show red at ri with d3
        c r17 "Turrets are down. Let's grab this trenchcoat wearing creep and get out of here!"
        tim "....................."
        hide green
        hide red
        hide timModel
        with d3
        hide scene_darkening with d3
        pause 0.4
        $ tod = 2
        scene black with fade
        $ prisonersNew = True
        jump missionComplete
    if task26Stage == 16:
        $ task26Stage = 17
        show scene_darkening with d3
        show timModel at ri
        show green g54 at le
        with d3
        $ task7Text = _("With Tim Scam in custody it's time to move on to the final level of the WOOHP HQ and take down the mastermind!")
        tim "........................"
        s "......................."
        y "......................."
        menu:
            "Cut the tension" if True:
                y "I expected this to get awkward, so I prepared!"
                "You pull out a big-fuckoff-knife."
                s g28 "!!!!"
                s "[playerName]! What's that for?!"
                y "It's a knife... {w}It cuts things."
                y "It's gonna cut this tension!{w} Get it?"
                s g38 "{b}*Sighs*{/b} Anyways, where were we..."
            "..............................." if True:
                y "......................................"
                y "Chirp, chirp, chirp...."
                y "Get it? It's like cricket nois-..."
        s g53 "Why the hell did you save me from those turrets?!"
        tim "I don't know."
        s "We're enemies! Why are you pulling shit like this?!"
        tim "You'd rather I have you die?"
        s g52 "It'll certainly be less confusing!"
        s g38 "Tim. What we are... what we had... it ended when you tried killing Jerry all that time ago."
        s g53 "Stop pretending to care about me!"
        tim "............................"
        s g52 "We're enemies Tim Scam. You've proven that over and over again."
        s "You expect me to suddenly forgive you, just because you saved my life?"
        tim "No. I expect you to try and see things from my point of view for once."
        tim "Jerry is dangerous. WOOHP is dangerous. This world would be better off without them."
        s g53 "By setting Beverly Hills on fire...?!"
        tim "Look around you! The gangs are gone. WOOHP public image is ruined. Buildings can be rebuild, shops can be restocked and order can be restored."
        tim "I am trying to show you a world without a tyrant at the top!"
        s "Jerry is not a tyrant!"
        tim "He's no a saint either!"
        s g54 "............................."
        tim "................................."
        y "........................"
        y "I hate to interrupt your little lovers quarrel, but we have a headquarters to liberate."
        tim "........."
        y "Tim, your rebellion is over. We just need to get to GLADIS."
        y "We need to know what's waiting for us on that top level."
        tim "......................."
        tim "Nothing."
        y "Nothing?"
        tim "Yeah... Nothing."
        y "No more super spies in colorful outfits? No more death traps? No more surprise nanobot injections?"
        tim "She's only a robot and we've already thrown everything we had at you."
        y ".............................."
        tim "I don't know who you are, but freeing Jerry is a mistake."
        tim "Things will just go back to how they used to be. Prisoners are put away without trial. Politicians will continue to be held in WOOHP iron grip and you will have taken away the only people who could stand against him."
        s g12 "Don't listen to his garbage, [playerName]. Once we free Jerry, we can finally begin to bring some sanity to this world."
        s "You're insane Tim, to think all this violence and chaos is for the betterment of the world."
        hide green with d3
        tim "........................."
        scene bgBase with fade
        $ britSuit = 1
        show scene_darkening with d3
        show red at ce
        show yellow at le
        show britney at ri
        with d3
        c r18 "And?"
        y "Seems the way is clear. We only need to capture the top floor and free the WOOHP HQ."
        c r42 "I can't believe it's finally over..."
        brit b31 "It's not over yet. [playerName] we're with you. Once you launch the final attack on the HQ, we'll finally be able to restore order to this city."
        hide britney
        hide yellow
        hide red
        with d3
        hide scene_darkening with d3
        $ tod = 2
        jump base
    if task26Stage == 17:
        play music "audio/music/ambient1.mp3" fadein 1.0
        $ task7Text = _("Send the last of your loyal followers out to look for Mathias.")
        $ task26Stage = 18
        call undressSam from _call_undressSam_23
        call undressClover from _call_undressClover_16
        call undressAlex from _call_undressAlex_20
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        scene bgOffice with fade
        show scene_darkening with d3
        show green g32 at ri
        show red r32 at ce
        show yellow y32 at le
        with d3
        s "GLADIS! We've come to stop you!"
        c r8 "Yeah what's the big idea?! You tried to kill Sam!"
        a y14 "And the city is on fire! So many innocent people got hurt!"
        hide green
        hide red
        hide yellow
        with d3
        show gladis at ce with d3
        GLA ".........................................................."
        y "Don't give us the silent treatment, missy!"
        GLA ".........................................................."
        sM "GLADIS....?"
        y "Erm..."
        y "Anyone home...?"
        "You walk up to the robot and poke it with your finger."
        y "{b}*Poke* *Poke*{/b} She's not responding...."
        cM "But... how?!"
        "???" "It's quite simple really."
        stop music fadeout 3.0
        hide gladis with d3
        show jerryModel at ce with d3
        "Girls" "Jerry!"
        y "Jerry!"
        play music "audio/music/stealth1.mp3" fadein 1.0
        y "............"
        y "Jerry?{w} Weren't you being held hostage?"
        jerry "Oh I was, but my captors underestimated my love for the Queen."
        show agentModel2 at le
        show expression "models/agent/hood.png" at le
        with d3
        "Torturer" "♫♪ God save our gracious Queen, long live our noble Queen, God save the Queen! ♫♪"
        hide agentModel2
        hide expression "models/agent/hood.png" at le
        with d3
        jerry "I just needed a distraction, so when you lot came in, I managed to cut off power to GLADIS."
        jerry "I am so happy to see you girls again!"
        y "........................"
        show red r55 at le
        show yellow y55:
            xalign 1.2
        show green g55:
            xalign 0.9 yalign 0.1
        with d3
        a "We're happy to see you again, Jer!"
        c r56 "We were worried sick!"
        s "We spend months planning your escape!"
        y "Yeah... this almost feels a little anti-climactic."
        jerry "..........................."
        jerry "And... you are?"
        y "Oh right... erm..."
        y "I'm sorta... an inmate."
        jerry "Is that so...?"
        c r55 "It's okay Jer, he's one of the good guys. He helped us free you."
        s g56 "Yeah, he freed us from our nanobot control and helped fight our way to the top of WOOHP HQ!"
        jerry "Interesting..."
        y "I've been hoping to go on the straight and narrow! So I'd like to apply for a job!"
        y "My resume includes working as a zoo keeper, a daycare worker and a prison guard!{w} And... y'know. The entire liberation of Beverly Hills and WOOHP."
        jerry "That's an impressive resume indeed. Let's see... I think i've got a contract for you in my desk."
        hide jerryModel with d3
        "Jerry turns his back to you and walks over to his desk as you glance at the girls."
        s g1 "You deserve it, [playerName]."
        c r1 "Yeah, we wouldn't have gotten this far without you."
        a y1 "You could be a spy! Or a security manager! {w}Or even a janitor!"
        y "Yeah..."
        "You carefully throw a glance around the room."
        y ".............................."
        jerry "{b}*Ahem*{/b} So I take you you've already seen the entire facility?"
        y "Yup. Top to bottom."
        jerry "I see..."
        "Jerry bends over his desk and opens a cupboard."
        y "I saw where you make the gadgets, the hidden civilian surveillance, the prisons, the propaganda center..."
        y "..................."
        y "On second thought. I probably didn't have clearance to see those..."
        jerry "Correct."
        y "Oh well. I guess you don't have a choice but to hire me now!"
        jerry "No choice indeed..."
        hide red
        hide green
        hide yellow
        with d3
        "{b}*Click* *Click*{/b}"
        play sound "audio/sfx/drama1.mp3"
        show drama3:
            xalign 0.0 yalign 0.2
        show dramaJerry
        pause 0.8
        stop music
        play sound "audio/sfx/gunshot1.mp3"
        scene white
        pause 0.2
        scene bgGunshot
        pause 1.5
        show black:
            alpha 0.0
            linear 8 alpha 1.0
        s "[playerName]!"
        c "{size=-8}Jerry stop!{/size}"
        a "{size=-14}Oh no [playerName]...!{/size}"
        $ renpy.pause(10, hard='True')
        hide black
        show bgSky:
            pause 0.5
            yalign 0.0
            linear 0.7 yalign 0.2
            pause 1.5
            linear 0.7 yalign 0.4
            pause 1.5
            linear 0.7 yalign 0.6
            pause 1.5
            linear 0.7 yalign 0.8
            pause 1.5
            linear 0.7 yalign 1.0
        with fade
        pause 5.0
        O5O "I'M FINALLY AN IMPORTANT CHARACTER!"
        brit "Shhh! Not so loud! We're almost there..."
        scene black with fade
        pause 3.0
        "He's waking up...!"


        play music "audio/music/stealth1.mp3" fadein 2.0
        scene bgBasement with fade
        pause 0.5
        show scene_darkening with d3
        show O5O at le
        show britney at ri
        with d3
        y "Uuuuuuuugh......"
        y "What.... happened?"
        brit "You were shot. Try not to move too much."
        y "Shot....?{w} SHOT!{w} I was shot by that old geezer!"
        brit "Calm down, you don't want your wounds to open again."
        O5O "THERE WAS SO MUCH BLOOD! YOU HAVE A LOT OF BLOOD MY FRIEND!"
        y "But... why?! I got him back his stupid organization! Why would he turn on me like that?!"
        brit "He didn't. {w}GLADIS did."
        brit "Jerry is being controlled by nanobots. We walked right into a trap."
        y "But... GLADIS was offline...?"
        brit "And came back online after you were shot. It was all a ruse. She is very much still active and took control of Jerry and the spies."
        y "The girls! What happened?!"
        O5O "THEY'RE STILL WITH WOOHP."
        brit "The update hit them hard and they've all been controlled again."
        y "Oh no... I led them straight into that trap..."
        y "Well we're still alive! I'm sure with a can-do attitute and some elbow grease we can-.."
        O5O "IT GETS WORSE!"
        y "Ooofcourse it does."
        brit "GLADIS is preparing to launch WOOHP missle arsenal."
        y "At...?"
        brit "At... at well... everything. The entire city."
        y "..............."
        y "Two questions."
        y "One. Why does WOOHP have enough missles to lay waste to an entire city?"
        y "Two. I thought GLADIS only wanted to get rid of WOOHP? Not the entire city?"
        brit "True, but..."
        O5O "WOOHP HAS TUNNELS ALL OVER THE CITY!"
        y "Tunnels?{w} Wait... the emergency tunnel network?"
        O5O "EXACTLY!"
        brit "For some reason, she considers all those tunnels to be part of WOOHP and after we broke into her office, she now plans to destroy every hint of the organization. No matter the cost."
        y "But that's crazy!"
        y "........................"
        if task30Stage >= 3:
            y "What about Kim?"
            brit "She's fine. She's hiding out nearby."
        if socialSilva >= 12:
            y "What about Silva?"
            brit "Silva is being hunted by agents, but she is hiding out nearby."
        brit "What do you think we should do...?"
        y "......................................."
        label endgameMenu1:
            pass
        menu:
            "Fight back" if True:
                y "We can't let her win! What do we have left? Can we-...{w} argh...!"
                brit "Easy there! You're still wounded."
                y "Britney we got so close. No way am I giving up now."
                O5O "AND YOU'VE GOT ME!"
            "Give up" if True:
                y "Whelp, it was nice while it lasted."
                brit "You're... giving up?"
                y "Yup. It seems like the right time for me to move on. The secret agent lifestyle was never for me."
                brit "I guess I can't blame you..."
                brit "You're still wounded, but I think I can smuggle you out of the city."
                brit "Are you sure you want to leave it all behind...?"
                menu:
                    "Yes" if True:
                        brit "All right, then let's make preparations for getting us out of here."
                        scene black with longFade
                        pause 1.0
                        "And so you decided to leave Beverly Hills to its fate."
                        "Soon after you evacuated, the US Military moved in and GLADIS launched her missle arsenal. Leaving the city and WOOHP in ruins."
                        show text _("Game Over") with dissolve
                        pause
                        $ MainMenu(confirm=False)()
                    "What am I saying?! Of course not!" if True:
                        jump endgameMenu1
            "Say something insane" if True:
                y "Did Napoleon give up when he was banished by the Spanish inquisition?!"
                brit ".....{w} Wait what...?"
                y "Did the Mongols give in when the British army burned their villages?!"
                brit "What are you even say-...?"
                y "Did the three-hundred Spartans flee when put up against the countless numbers of the Zulu warriors?!"
                brit "I think you're getting your history mixed u-..."
                y "When Albert Einstein said: ''WE WILL FIGHT THEM ON THE BEACHES!'' He never gave up! He never gave in!"
                y "And I tell you now...!{w} I will never surrender! I have worked hard to get this close and I'll be damned if a mechanical cyclopse is getting in my way!"

        y "I think the first matter of business is taking back the Milkshake Bar."
        y "We'll have to contact our potential allies in the area and most importantly... get in touch with Mathias."
        brit "The hacker kid? {w}What are you planning?"
        y "Mathias can he-...{w} ugh...~"
        O5O "EASY THERE FELLOW AGENT! YOU'VE BEEN SHOT REMEMBER?"
        O5O "LET US HANDLE IT! WE'LL TRACK DOWN YOUR MISSING ALLIES FOR YOU!"
        y "............................."
        stop music fadeout 2.0
        y "Fine... let's go check up on the situation outside."
        scene black with fade
        scene bgMapRaid with fade
        play music "audio/sfx/warzone.mp3"
        play sound "audio/sfx/raid.mp3"
        pause 1.0
        "DAYS UNTIL MISSILE LAUNCH: [daysTillMissle]"
        pause 1.0
        show scene_darkening with d3
        y "That's... pretty bad."
        brit "GLADIS has taken over everything..."
        O5O "BEVERLY HILLS IS BACK TO BEING A WARZONE!"
        y "Okay, there isn't alot of time. You two go scout the city and try to bring back allies that can help us."
        $ spy5Status = -1
        $ spy6Status = -1
        hide scene_darkening with d3
        call screen mapButtonsRaidFinale
    if task26Stage == 18:
        play music "audio/music/ambient1.mp3" fadein 1.0
        $ task26Stage = 19
        show matModel at ce with d3
        y "Mathias!"
        mat "My dude!"
        mat "Wait... did you get shot?!"
        y "Not important. The city is about to be blown to kingdom come!"
        mat "Narly."
        y "And you're going to help me stop it!"
        mat "My dude. Hacking into a database is one thing. Hacking into a missile system is on a whole nother level!"
        y "That's why you're not hacking into the missile system.{w} I need you to hack into cells beneath the milkshake bar."
        mat "The cells...?"
        y "Yes. Can you open the cell doors remotely?"
        mat "But that will release all the prisoners!"
        y "Exactly."
        mat "...................."
        mat "I guess I could, but it sounds pretty crazy."
        menu:
            "'Can you do it?'" if True:
                y "Crazy or not, do you think you can do it?"
                mat "I guess so. So why am I doing this...?"
            "'Crazy is my middle name!'" if True:
                y "You're not the first one to call me that, but it's worked out so far!"
                mat "The city is facing imminent destruction."
                y "Oh.......{w} right."
                y "Just trust me okay?"
                mat "So why am I doing this...?"
            "Say something insane" if True:
                y "{i}'When the spools of cotton all unwind and the lions rest after their feast, we too shall know the leisure of cessation.'{/i}"
                mat "That's... so profound. Who are you quoting?"
                y "Quoting? It just came to my mind!"
                mat "Oh! I didn't know you were a poet! What does it mean?"
                y "........................."
                y "{i}Stuff....{/i}"
                mat "Oh right.. I keep forgetting how crazy you really are..."
                mat "So why am I doing this...?"
        y "To save the city from destruction of course!"
        mat "No no no, I mean... Why am {i}'I'{/i} doing this?{w} What do I get out of it?"
        y "......................"
        y "You greedy little punk.{w} Fine... {i}'one'{/i} date with Clover."
        mat "DEAL!"
        y "Now get busy!"
        hide matModel
        hide O5O
        hide silvaModel
        hide kim
        with d3
        stop music fadeout 3.0
        scene black with fade
        show text _("Despite the chaos, you manage to get some rest.")
        with d5
        pause 1.5
        hide text
        with d5
        scene bgMapRaid with fade
        play music "audio/sfx/warzone.mp3"
        play sound "audio/sfx/raid.mp3"
        pause 1.0
        $ daysTillMissle -= 1
        "DAYS UNTIL MISSILE LAUNCH: [daysTillMissle]."
        pause 1.0
        y "........................."
        y "Mathias is everything ready?"
        mat "Ready as it'll ever be.{w} Just give the word and I'll open all of the cell doors."
        y "Do it."
        stop music fadeout 2.0
        scene black with fade
        scene bgPrison with fade
        pause 1.0
        show scene_darkening with d3
        show agentModel3 at le
        show agentModel4 at ri
        with d3
        "Agent 1" "Why! I sure am glad we're out here and those criminals are in there!"
        "Agent 2" "You said it fellow agent! Can you even begin to imagine what they'd do to us if the gates were unlocked?!"
        play sound "audio/sfx/defeatGang1.mp3"
        "Rrrrrrrrrrrr~...."
        "Agent 1" "Oh my! Do you hear that ringing sound fellow agent?!"
        "Agent 2" "Yes I do! It's the distinct and unmistakable sound of a prison door opening!"
        "Agent 1" "..............................."
        "Agent 2" "..............................."
        "Agents" "AAAAAAAHHHHH!"
        play music "audio/music/ambient1.mp3" fadein 1.5
        hide agentModel3
        show agentModel3:
            linear 0.3 xalign -0.9
        show agentModel4:
            linear 0.4 xalign -0.8
        pause 1.5
        $ candyFace = 2
        $ sebFace = 3
        show timModel at ce
        show candyModel at le
        show timModel at ce
        show candyModel at le
        show sebModel2 at ri
        with d3
        pause 0.5
        tim "....................................."
        seb "The doors opened! Let's get out of here."
        candy "A stroke of good luck~..."
        tim "We've been given a second chance. We can sti-..."
        seb "Are you insane?! Your plan failed Tim, I'm getting out of here."
        $ candyFace = 4
        candy "It was a stupid plan to begin with. I'm going back to creating robot cheerleaders to overthrow the world."
        hide sebModel2
        hide candyModel
        with d3
        pause 0.5
        tim "............................."
        "{b}*Beep* *Beep* *Beep*{/b}"
        tim "...?"
        y "{b}*Static*{/b} Attention WOOHP inmates! Before you all escape and run of-..."
        tim "They're all gone."
        y "..........."
        y "Crap.{w} It's just you?"
        tim "Just me. Did you let us out of our cells?"
        y "Yes. It's a long story, but the short of it is... GLADIS is preparing to nuke the entire city."
        y "We need your help taking back the milkshake bar. Then we can make a plan on how to stop her."
        tim "And if I do? You're just going to throw me back in my cell."
        y ".........................."
        menu:
            "I promise to let you go (+Karma)" if True:
                $ playerKarma += 10
                y "......................"
                y "Way to twist my arm..."
                tim "You want your base back or not?"
                y "Fine....... I promise to let you go after this is all over..."
                tim "That's more like it."
            "Lie about letting him go (-Karma)" if True:
                $ playerKarma -= 10
                y "N-noooooo.... I wouldn't do {i}thaaaat{/i}...!"
                tim ".........................."
                y "You know...! I would never!"
                y "Infact! The very idea you brought it up is INSULTING!"
                y "You have deeply insulted me good sir! To take my good name into question!"
                tim "We know you're lying......."
                y "...................."
                y "Okay fine...{w} if you help us out, you're free to go..."
                tim "That's better."
            "Say something insane" if True:
                y "Voice in my head, what should I do?!"
                "Inner Voice" "Heeeey it's me. Haven't heard from me in a while!"
                y "I could use some advice here..."
                "Inner Voice" "Since when did I start giving good advice? I thought Chineese waterboard torture was a legit solution to bullying!"
                tim "Who are you talking to...?"
                y "Hush. I'm in a conversation here."
                tim "......................."
                "Inner Voice" "Just admit it... You're going to need him."
                "Inner Voice" "Whatever crimes he's committed, he can redeem himself by helping you save the city."
                y "And what if he betrays me?"
                "Inner Voice" "It's just the risk you're going to have to take."
                y "........................."
                y "Okay fine. Help us out and I promise to let you go afterwards."
                tim "That's more like it."
        y "........................."
        tim "I'll begin the attack. Just wait for the signal."
        y "Signal?"
        tim "Tim signing out."
        stop music fadeout 3.0
        hide timModel
        hide melodyModel
        hide taliaModel
        with d3
        hide scene_darkening with d3
        scene black with fade
        pause 0.5
        scene bgMapRaid with fade
        play music "audio/sfx/warzone.mp3"
        pause 1.0
        brit "Are you sure you can trust him?"
        y "No. Infact, I'm pretty sure he'll betray us the moment he gets the chance."
        y "..............................."
        y "Just keep him away from any firearms. I don't want to get shot a second time."
        y "We're going to have to wait for his signal..."
        brit "Signal?{w} What's the signal?"
        y "I... don't know."
        play sound "audio/sfx/explosion2.mp3"
        with hpunch
        "{b}*BOOOOOM!*{/b}"
        O5O "HOLY MOLY!"
        brit "That was coming from the milkshake bar!"
        y "That must be the signal. Let's go!"
        call screen mapButtonsRaidFinale
    if task26Stage == 19:
        $ freedAgents = 0
        $ capturedAgents = 0
        $ task26Stage = 20
        stop music fadeout 2.0
        scene black with fade
        scene bgClub1 with fade
        pause 0.5
        show agentModel5:
            xalign 0.5 yalign 0.0
            linear 0.5 xalign 0.47
            xzoom -1
            linear 0.5 xalign 0.53
            xzoom 1
            linear 0.5 xalign 0.47
            xzoom -1
            linear 0.5 xalign 0.53
            xzoom 1
            linear 0.5 xalign 0.47
            xzoom -1
            linear 0.5 xalign 0.5
            xzoom 1
        play music "audio/music/ambient1.mp3" fadein 4.0
        "Agent" "Uh oh! Uh oh! Uh oh!"
        show britney at ri
        show timModel at le
        with d3
        "Agent" "......................"
        tim "Run."
        "Agent" "AAAAAAAAAHHHH!"
        show agentModel5:
            xzoom -1
            xalign 0.5 yalign 0.0
            linear 0.4 xalign 1.8
        pause 1.0
        y "The bar is ours aga-...{w} Ow...."
        tim "......................."
        tim "What happened to you?"
        y "Gunshot."
        tim "Gunshot?"
        y "Jerry."
        tim "Jerry shot you...?"
        brit b54 "Jerry is being controlled with nanobots. GLADIS has fully taken over."
        tim "I see..."
        tim "What about Clover, Sam and Alex?"
        y "Controlled aswell. Together with my army of freed WOOHP agents."
        tim "................."
        tim "Do you have a plan?"
        y "Sorta..."
        y "Seeing as you worked on GLADIS, I figured you might know how to disable her."
        y "Now I know we are enemies, but this is for real! If you don't help us the whole city will be destroyed!"
        tim "I'll help."
        y "Have a heart! I can understand your hesitation, but please for everything that's holy, help us!"
        tim "I said I'll hel-."
        y "I know we haven't always seen eye to eye, but there's people in dang-..."
        if task30Stage >= 3:
            kim "{b}*Slaps you on the back of the head.*{/b}"
        tim "I can't believe we lost to an idiot like you..."
        tim "If we want to disable GLADIS, we need to get close to her. There's an emergency incapacitate clasp that can shut her down."
        y "....................."
        y "An off switch?"
        tim "Yes, the challenge will be getting close."
        y "We need the spies..."
        y "Too bad they're off to God-knows-where. It's going to take weeks to find them!"
        tim "....................."
        tim "Maybe not.{w} Here..."
        "Tim hands you a piece of paper with a number on it."
        y "You're giving me your phone number?"
        tim "Not {i}my{/i} number..."
        tim "Call it... I trust her."
        y "......................"
        "{b}*Beep* *Beep*{/b}"
        "You call the number...."
        scene black with fade
        scene bgMapRaid with fade
        pause 0.5
        "...........{w}...........{w}..........."
        mel "Hello...?"
        y "Wait... I recognize that voice...!"
        mel "Who is this...?"
        y "Not important. Listen...! Sam is in trouble and I need your help!"
        mel "Is this that insane idiot that imprisoned me?"
        menu:
            "Yes, that's me" if True:
                y "Yup."
                mel "................................."
                mel "Well at least you're an honest idiot..."
            "No, I'm not" if True:
                y "I don't know what you're talking about!"
                mel "It is you, isn't it...?!"
            "Say something insane" if True:
                y "Yes it's me. Let bi-gongs be bi-gongs!"
                mel "...................."
                mel "Do you mean bygones?"
                y "Bygones...? That makes so much more sense!"
                y "No wonder people gave me funny looks whenever I said it..."
                mel "Yes, you are definitely the crazy idiot..."
        mel "What was this about Sam?"
        y "Sam is back to being nanobot controlled! I know she betrayed you and everything, but we have to free her or she's going up in smoke with the rest of the city!"
        mel "......................."
        y "Come on Melody... Name your price!"
        mel "......................."
        mel "Sam's a good kid..."
        mel "Even if we were on different sides the whole time, she doesn't deserve this."
        y "So you'll help...?"
        mel "Fine... what do you need?"
        y "She's missing. We're looking for her."
        mel "Missing? Hang on... I think I know where to find her. If she's being controlled by nanobots, you better have something to break her out of it though."
        mel "I'm sending you the coordinates."
        y "Oh and Melody...!"
        mel "Yeah?"
        y "Thanks...."
        mel "....................................."
        scene black with fade
        scene bgClub1 with fade
        pause 0.5
        show scene_darkening with d3
        pause 0.5
        show timModel at le
        show matModel at ce
        with d3
        mat "So what do you think?"
        tim "Onorthodox... but it could work."
        y "You gave me Melody's number?!"
        tim "Yeah. What did she say?"
        y "She's giving me the coordinates of where she thinks Sam is."
        y "You could have told me who I was calling though!"
        tim "Was is awkward?"
        y "Yes!"
        tim "Good."
        y ".............................."
        mat "And speaking of awkward~...."
        mat "Tim and I came up with a little something to help break the nanobot control of the girls."
        "Mathias hands you a sketch of a latex body suit."
        y "Wow... I didn't know you were into this kind of thing Mathias!"
        mat "Well... I'm not really..."
        y "..............."
        tim "Don't look at me."
        y "If it wasn't your idea and not Mathias... who came up with it...?"
        mat "Well... I met this one girl who seemed super into it...{w} She gave me the sketch."
        y "............................"
        y "Black hair, glasses, looks like a librarian?"
        mat "Yes! You know her?"
        y "Yup. She works at the mall.{w} She's a perv, but it's good to know she's okay."
        tim "Mathias and I came up with gadget. If you throw it at a spy, the suit will automatically wrap itself around them."
        mat "Not only trapping, but breaking their nanobots at the same time!"
        mat "It has to be thrown from quite close though... So it would be best if the girl was distracted."
        y "Well... if Melody was right, we'd soon be able to test it out on Sam..."
        y "Good work everyone!"
        scene bgMapRaid with fade
        play music "audio/sfx/warzone.mp3"
        play sound "audio/sfx/raid.mp3"
        call screen mapButtonsRaidFinale

    if task26Stage == 20:
        $ task7Text = _("Soft your followers out to soften up the airport's defenses and bring Sam back home.")
        $ task26Stage = 21
        scene bgClub1 with fade
        pause 0.5
        show scene_darkening with d3
        pause 0.5
        if task30Stage >= 3:
            show kim:
                xalign 1.2 yalign 0.0 zoom 0.9
            with d3
        if socialSilva >= 12:
            show silvaModel:
                xalign 0.85 yalign 0.0 zoom 0.9
            with d3
        show O5O at ce
        show britney at ri
        with d3
        y "All right everyone. We got a report that Sam is hiding out at the airport."
        y "From what I've gathered, the place is heavily guarded, so I'm sending you out to soften up their defenses."
        y "Once those are down, we can move in and capture Sam."
        $ tod = 1
        hide kim
        hide silvaModel
        hide O5O
        hide britney
        with d3
        scene bgMapRaid with fade
        call screen mapButtonsRaidFinale
    if task26Stage == 21:
        $ task26Stage = 22
        pause 0.5
        show scene_darkening with d3
        pause 0.5
        show O5O at ce
        show britney at ri
        with d3
        brit "We're back."
        y "So you are. And the airport?"
        brit b39 "We cleared out the guards. No sign of Sam though."
        y "............"
        O5O "BUT WE DID SEE SOMEONE ELSE!{w} THE SILVER HAIRED GIRL IN THE RED DRESS!"
        y "Melody? She was there?"
        brit b31 "Yeah. We don't know what she's up to."
        y "..................."
        y "All right, let's not waste any time.{w} Tim, is the bondage suit ready?"
        show timModel at le with d3
        tim "Ready but untested."
        y "Then this seems like an excellent opportunity for it!"
        tim "Remember that you have to get close. You'll have to distract her before springing the trap."
        y "Right..."
        O5O "WHAT ARE YOU ORDERS?!"
        menu:
            "Let's go now" if True:
                brit "Agreed. The airport will not be vulnerable for long. We have to move now."
            "Let's wait till tomorrow" if True:
                y "I'm feeling kind of lazy. Let's go tomorrow."
                brit "With all due respect, the airport is vulnerable to attack now."
                brit "We don't have time to wait.{w} Don't forget there's missiles on the way."
                y "............................"
                brit "You forgot, didn't you....?"
                y "Not so much forgot as... 'slipped my mind'."
            "I'm having second thoughts" if True:
                y "Actually... the news about Melody being there sounds a bit suspicious to me."
                y "Tim, you told me to contact her. Do you know anything about this?"
                tim "I know as much as you do."
                O5O "MAYBE SHE'S SETTING A TRAP!"
                tim "Or she's trying to help out a friend."
                y "...................."
                brit "Either way, the airport is vulnerable to attack now."
                brit "We don't have time to wait."
        scene black with fade
        "You pack your things and together you make your way to the airport."
        "Half way there, you stop the group after hearing a peculiar sound..."
        scene bgStreet2 with fade
        show britney at ri with d3
        y "...?"
        brit "Why are we stopping? We're not there ye-..."
        y "Shh. Listen."
        "You all fall quiet and listen intensely."
        "???" "{b}*Moans*{/b}"
        y "........................"
        brit "What... what's that...?"
        y "It's coming from over here."
        "You carefully creep closer to where the sound is coming from..."
        mel "Go on bitch. You're not a real Ace until you learn how to lick pussy."
        y "............................."
        y "{b}*Low*{/b} Well now I'm curious....!"
        brit "{b}*Low*{/b} Shhh~..."
        "You creep a little closer and turn the corner....."
        scene black with fade
        pause 0.5
        y "HOLY....!"
        show picMelody:
            xalign 0.5 yalign 0.5
        with dissolve
        pause
        y "Awww yeeeeeeah."
        s "{b}*MUFFLED CURSES*{/b}!"
        y "Say cheese ladies."
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d3
        pause 0.5
        play sound "audio/sfx/itemGot.mp3"
        "A new photo has been added to your photoalbum."
        scene bgStreet2 with fade
        mel "About time you showed up!"
        y "Melody! What are you doing here?"
        mel "What does it look like? Breaking this bitch out of her trance!"
        y "Aww... you came back and risked getting captured again just to rescue Sam?"
        mel "Just tell me you brought something to restrain her..."
        y "Oh right! The suit..!{w} Here... Melody, stand clear."
        with hpunch
        "You throw the gadget Tim and Mathias came up with and..."
        call undressSam from _call_undressSam_24
        play sound "audio/sfx/vib.mp3"
        show greenBondage at ri with d3
        pause
        s "{b}*Mfph! Mpfhhfff!!!*{/b}"
        y "It worked!"
        s "{b}*Furious muffles!!!*{/b}"
        s ".........................."
        s "{b}*Lustful muffles~...*{/b}"
        y "Okay Cucumber, don't have too much fun in there..."
        y "O5O, let's grab her and get back to the base!"
        O5O "PLEASE STOP SQUIRMING!!"
        scene black with longFade
        scene bgBase with fade
        pause 0.5
        show scene_darkening with d3
        show britney at ri
        show O5O at le
        with d3
        O5O "TARGET HAS BEEN PLACED IN HER CELL!"
        brit "She was very wiggly."
        O5O "SO WIGGLY!"
        y "All right, good work guys. I'll talk to her in a bit."
        "Agent O5O and Britney nod."
        hide britney
        hide O5O
        with d3
        $ spy1Status = 0
        $ spy2Status = 10
        $ spy3Status = 10
        hide scene_darkening with d3
        jump base
    if task26Stage == 22:
        call undressSam from _call_undressSam_27
        $ task7Text = _("Rescue Clover by planning a mission to Drift Punk and using the Bondage gadget on her.")
        $ task26Stage = 23
        $ greenArms = 1
        $ greenOutfit = 4
        hide screen nanoLevelSam
        show scene_darkening with d3
        show greenBondage at ce with d3
        s "{b}Moans{/b}!!!"
        y "Hello there Sam. Good to see you again."
        s "{b}Muffled{/b}!"
        y "Don't worry. Let me just get you out of th-..."
        y "Wait... open your eyes..."
        s "...!"
        y "Still red...? That last nanobot update must have been a lot more powerful..."
        menu:
            "Jerk off to the bound spy" if True:
                y "So I was thinkin-..."
                s "{b}*Muffled Moans*{/b}!!! ♥♥♥"
                y "............."
                y "So what I was thinking was th-..."
                s "{b}*More Muffled Moans*{/b}!!! ♥♥♥♥♥"
                y "Calm down penis. This is not the time for-..."
                s "{b}*LUSTFUL MUFFLED MOANS*{/b}!!! ♥♥♥♥♥♥♥♥"
                y "Fuck it..."
                "You whip out your dick and begin jerking it to the moaning spy."
                y "That's it you slut! You like it, don't ya?"
                s "{b}*Desperate Muffled Moans*{/b}!!! ♥♥♥♥"
                y "Fuuuuuck....!"
                $ greenCum = 1
                with flashbulb
                $ greenCum = 2
                with flashbulb
                $ greenCum = 3
                with flashbulb
                pause
                s "{b}*Whining Moans*{/b}"
                y "All right. Enough fun. Let's get you out of there."
            "Wait a while long" if True:
                s "{b}*Muffled Moans*{/b}!!! ♥♥♥"
                "You continue to watch as the spy is writhing in pleasure."
                "Orgasm after orgasm hits the redheaded girl as sweat is dripping off of her."
                y "Damn, that looks exhausting....!"
                s "{b}*Desperate Muffled Moans*{/b}"
                y "Okay okay... let's get you out of there."
            "Say something crazy" if True:
                y "This seems like an excellent time to practise my sea shanties!"
                s "Mpghhh! Mffff!! Mhphff!!! ♥♥♥♥"
                y "Oh I see you're excited! Okay, so here it goes..."
                y "♫♪ Oooh we'd be aaaaall right, if we make it 'round the Hor-... ♫♪"
                s "Mfphoff! Ufghhh!!!! ♥♥♥♥"
                y "Please Sam. I can tell that you're loving these good ol' shanties, but try not to interrupt."
                y "{b}*Ahem*{/b} ♫♪ What shall we do with the drunken sailor?! What shall we d-... ♫♪"
                s "{b}*Desparate exausted moans*{/b} ♥♥"
                y "{b}*Sighs*{/b} No respect for the classics..."
        scene black with fade
        $ greenCum = 1
        call undressSam from _call_undressSam_25
        pause 0.5
        scene cellSam with fade
        show scene_darkening with d3
        show green g14 at ce with d3
        y "All right, back to normal?"
        "You turn off the vibrators and help the spy who's trembling on her legs."
        y "You okay, Sam?"
        show green g14 at ce with d3
        s g15 "[playerName]...?"
        s "I-I... thought you were... d-dead..."
        "Sam stumbles forward as you catch her just in time."
        y "Not far off. That old tea sipper got me good."
        s g15 "It's... not Jerry... GLADIS she-..."
        y "I know. I've been brought up to speed.{w} A lot has happened since we captured the top floor of WOOHP HQ.{w} Tim is on our side now!"
        s "Tim...?"
        y "Or well... more of an alliance of convenience."
        "You quickly fill Sam in on the situation."
        s g4 "That's... a lot to take in..."
        y "Unfortunately, we don't have a whole lot of time. Do you know where Clover and Alex are?"
        s g32 "Yeah... Clover is in Punk Web."
        y "And Alex?"
        s "Still at WOOHP HQ. We'd have to plan a mission to bring them back."
        y "All right. In that case grab a shower and then get some rest. We'll go after them tomorrow."
        "The still trembling spy nods as you leave her cell."
        hide green with d3
        $ greenCum = 0
        hide scene_darkening with d3
        scene bgBase with fade
        show scene_darkening with d3
        show O5O at ri
        show britney at le
        with d3
        brit "How is she?"
        y "Back to her old self, but exausted."
        O5O "AND THE OTHER SPIES?!"
        y "I've got their location. We can start doing missions again tomorrow."
        "Britney and Agent O5O give you a nod and prepare for bed."
        hide O5O
        hide britney
        with d3
        pause 1.0
        show timModel at ce with d3
        tim "..........................."
        tim "Is she okay...?"
        y "A little worn out, but she'll be all right."
        y "So what's the deal between you two anyways?"
        tim "It's... complicated."
        y "You sound like Sam..."
        tim "Regardless, we're not done yet."
        tim "Only [daysTillMissle] days until we all go up in fire and smoke. Best bring those girls back quick."
        y "Right."
        hide timModel with d3
        hide scene_darkening with d3
        stop music fadeout 3.0
        scene black with fade
        show text _("Despite the chaos, you manage to get some rest.")
        with d5
        pause 1.5
        hide text
        with d5
        scene bgMapRaid with fade
        play music "audio/sfx/warzone.mp3"
        play sound "audio/sfx/raid.mp3"
        pause 1.0
        $ daysTillMissle -= 1
        "DAYS UNTIL MISSILE LAUNCH: [daysTillMissle]."
        pause 1.0
        scene bgBase with fade
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        show scene_darkening with d3
        show green g32 at ce with d3
        if intel <= 199:
            $ intel = 200
        s g31 "All right, I'm ready! Can I suggest we rescue Clover first?"
        y "Why Clover?"
        s "Alex is at WOOHP HQ. Security is probably strongest there. I could use Clover as backup if we go there."
        y "Good point. All right, let's plan a mission to Punk Web."
        $ samHealth = 3
        $ spyGreenActive = True
        $ spy1Status == 0
        $ intel += 200
        $ task23Stage = 7
        $ backupBritneyActive = True
        scene black with fade
        $ task26Stage = 23
        $ samHealth = 3
        $ cloverHealth = 3
        $ alexHealth = 3
        hide green
        hide scene_darkening
        with d3
        jump missions
    if task26Stage == 23:
        $ task26Stage = 24
        hide spyCorner
        hide spyCornerSide
        hide spyCrouchCorner
        hide spyCrouchingSide
        with d2
        show spyThrowBack1:
            xalign 0.75 yalign 0.77 zoom 0.71 xzoom -1
        with d2
        pause 0.3
        hide spyThrowBack1
        show spyThrowBack2:
            xalign 0.75 yalign 0.77 zoom 0.71 xzoom -1
        with d2
        hide screen interactScreen
        hide screen equipmentMenu
        pause 0.1
        hide bossSeb
        hide spyThrowBack2
        with d1
        with hpunch
        pause 0.5
        show scene_darkening with d3
        call undressClover from _call_undressClover_17
        $ redOutfit = 4
        play sound "audio/sfx/vib.mp3"
        show redBondage at ce with d3
        pause
        c "Mfph!!!?"
        c "Mmmm~....!!! ♥"
        $ samHealth = 3
        $ cloverHealth = 3
        $ alexHealth = 3
        show green at ri with d3
        s g53 "Gotcha!{w} [playerName] we got her."
        jump missionComplete
    if task26Stage == 24:
        $ task7Text = _("With Sam and Clover back on our side, it's time to free Alex. Plan a mission to WOOHP HQ to use the bondage gadget on her.")
        $ task26Stage = 25
        pause 0.5
        show scene_darkening with d3
        show redBondage at ce
        show green g32 at ri
        with d3
        c "{b}*Mfmphdff!!!!*{/b}"
        s g29 "I think she's back to normal by now. Quickly, let's get her out of the suit!"
        y "................."
        menu:
            "Jerk it" if True:
                y "{b}*Zip*{/b}"
                s g31 "[playerName]...!"
                y "Stop being so outraged, Sam. Look how hot Clover is in that."
                s g29 "But we have to get her out!"
                c "Mpfhh!!"
                y "No we don't."
                c "Mpghf?!"
                s g11 ".............."
                s g12 "{b}*Sighs*{/b} Fine... she is looking pretty hot..."
                c "Mpfhhff!!!!"
                s g22 "Here, I'll help you."
                hide green with d3
                "Sam walks behind you and takes your cock in her hand before aiming it towards the squirming Clover and beginning to jerk it."
                c "{b}*Whining Moans*{/b}"
                "Sam increases her speed as her delicate fingers stroke your manhood faster and faster. You are rock solid and the moans of the blonde spy are getting you close to climaxing."
                "Bringing her face up to you ear, Sam whispers..."
                s "Coat the bitch~..."
                "Unable to hold back you let out a loud groan as you drench the red spy in cum."
                play sound "audio/sfx/cum.mp3"
                $ redCum = 1
                with flashbulb
                $ redCum = 2
                with flashbulb
                $ redCum = 3
                with flashbulb
                pause
                c "Mpmhfff!!!!!"
                y "All right, all right. Let's get you out of there."
            "Wait a bit longer" if True:
                y "We could."
                y "Or we could just watch her for a while longer."
                s g31 "[playerName]!"
                c "Mpghff!"
                y "See? She's enjoying herself!"
                c "{b}*Pleading Moans*{/b}"
                s g10 "..............."
                y "Okay... maybe we should get her out..."
            "Get Clover out" if True:
                y "All right blondie, that's enough fun for you."
        hide red
        hide redBondage
        with d3
        $ redCum = 1
        call undressClover from _call_undressClover_18
        pause 0.5
        show red at ce with d3
        c r14 "{b}*Pant* *Pant*{/b}"
        y "Welcome back to us Clov-..."
        c r7 "Raaaaah!"
        hide red with d3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        y "Aaah!{w} Quickly Sam, help me! She's still being nanobot controlled!"
        show red at ce with d3
        c r31 "No I'm not, you crazy pervert! Don't ever put me in that suit again!"
        y "Not a fan?"
        c r9 "{b}NOT{/b} a fan!"
        y "Well too bad. If you're going crazy for cocoa puffs again, you be damn sure I'm gonna put you in that suit again."
        show green g55 at ri with d3
        s g55 "Come on Clover. It was pretty hot, right?"
        c r12 "Sam.....{w} You turned out to be the biggest sex freak of us all."
        s g53 "Hey!"
        y "All's well that ends well. Two spies in the bag, now we only nee-... {w}Ow...!"
        c r10 "C'mon [playerName]. I didn't punch you that hard."
        y "Bullet wound."
        c r16 "Bullet wou-...{w} Oh God! I completely forgot!"
        c r28 "[playerName]! You're alive!"
        show black with fade
        "You quickly fill Clover in on the situation."
        $ redCum = 0
        hide black with fade
        c r18 "Missiles...?"
        c "I think I heard Alex saying something about that."
        s g56 "Alex?"
        c r29 "Yeah that's right! Alex has been put in charge of guarding the WOOHP missile silos!"
        y "Then that's where we're going next.{w} Head back to your cell and get some rest. We're planning a mission to WOOHP tomorrow."
        hide red
        hide green
        with d3
        "The girls nod and head back to their cells."
        pause 1.0
        y "...................."
        "Your wounds aren't healed yet. Best to get an early night yourself."
        $ specialBossActive = True
        $ spyRedActive = True
        $ spy2Status = 0
        $ redCum = 0
        hide green
        hide red
        with d3
        hide scene_darkening with d3
        stop music fadeout 3.0
        scene black with fade
        show text _("Despite the chaos, you manage to get some rest.")
        with d5
        pause 1.5
        hide text
        with d5
        scene bgMapRaid with fade
        play music "audio/sfx/warzone.mp3"
        play sound "audio/sfx/raid.mp3"
        pause 1.0
        $ daysTillMissle -= 1
        "DAYS UNTIL MISSILE LAUNCH: [daysTillMissle]."
        pause 1.0
        scene bgBase with fade
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        show scene_darkening with d3
        show green g32 at ce with d3
        show red r32 at ri with d3
        pause 1.0
        y "All right. Everyone rested? Then let's plan another mission and get Alex back."
        $ missionScreenCurrentLocation = 1
        $ samHealth = 3
        $ cloverHealth = 3
        $ alexHealth = 3
        scene black with fade
        hide green
        hide scene_darkening
        with d3
        jump missions
    if task26Stage == 25:
        $ task26Stage = 26
        hide spyCorner
        hide spyCornerSide
        hide spyCrouchCorner
        hide spyCrouchingSide
        with d2
        show spyThrowBack1:
            xalign 0.75 yalign 0.77 zoom 0.71 xzoom -1
        with d2
        pause 0.3
        hide spyThrowBack1
        show spyThrowBack2:
            xalign 0.75 yalign 0.77 zoom 0.71 xzoom -1
        with d2
        hide screen interactScreen
        hide screen equipmentMenu
        pause 0.1
        hide fightAlex
        hide spyThrowBack2
        with d1
        with hpunch
        pause 0.5
        show scene_darkening with d3
        call undressAlex from _call_undressAlex_21
        play sound "audio/sfx/vib.mp3"
        show yellowBondage at ce with d3
        pause
        y "Hah! Gotcha!"
        a "..............................."
        y "Er..."
        a "..............................."
        y "Alex...?"
        a "..............................."
        y "Okay you're freaking me out."
        show green g32 at ri with d3
        s "Let's get her back to the base."
        y "Good idea."
        $ samHealth = 3
        $ cloverHealth = 3
        $ alexHealth = 3
        $ task26Stage = 26
        jump missionComplete
    if task26Stage == 26:
        $ task26Stage = 27
        show scene_darkening with d3
        show yellowBondage at ce with d3
        a "..................................."
        y "Okay now you're really freaking me out Alex!"
        y "Say something! Or at least make a noise!"
        a "..................................."
        show red r32 at le
        show green g16 at ri
        with d3
        s "Er.. [playerName]. I think we should just take her out of the suit."
        c "We'll keep her pinned down, just in case."
        y "All right. As long as I don't get attacked again."
        hide yellowBondage with d3
        call undressAlex from _call_undressAlex_22
        "You begin slipping Alex out of her bondage suit as the other girls pin her down."
        show yellow y28 at ce with d3
        a "{b}*Gasp*{/b}!!!"
        a y29 "I thought you were never letting me out of there!"
        y "..............."
        y "Alex? Back to normal?"
        a y1 "Yup!"
        y "What was going on...? You didn't make a sound when you were in that suit..."
        a "Of course not. I follow the WOOHP Sexual Torture course to resist that kind of thing!"
        c r18 "The WOOHP wha-...?"
        s g17 "There was a course for that?!"
        s "Why didn't I know of this?!"
        c r52 "Sam, calm do-..."
        s g40 "Do you have any idea how many semi-sexual situations this job has put us into?!"
        s "I have the most messed up fetishes because of it!"
        y "Okay, too much info.{w} Alex. It's good to have you back with us."
        a "It's great to be back!"
        a y18 "..................."
        a "Didn't you die, [playerName]...?"
        y "It's... a long story..."
        show black with fade
        "You quickly bring Alex up to speed."
        hide black with fade
        a y1 "I'm glad you're not dead [playerName]."
        a "As for the missiles... I think I can help with that!"
        a y31 "Security has been pretty lacks on the missile silos. I got a good look at the place and know exactly where to go!"
        c r56 "Finally, something easy for a change."
        s g55 "Good job Alex!"
        y "...................."
        s g16 "[playerName]...?"
        y "Nah it's nothing. Let's discuss a plan of attack."
        a "Right!"
        hide red
        hide yellow
        hide green
        with d3
        pause 1.5
        y "..........................."
        "Inner Voice" "What's the matter?"
        y "So here's what I've been thinking..."
        y "We've fallen for nothing but traps this whole time. GLADIS has been ahead of us by one step...."
        "Inner Voice" "So...?"
        y "So why did she leave the missile silos guarded by the most ditzy of the spies?"
        y "Don't get me wrong. I love Alex. But would you put her in charge of guarding an arsenal of weapons of mass destruction?"
        "Inner Voice" "Erm... probably not..."
        y "Exactly."
        "Inner Voice" "You think it's another trap?"
        y "......................"
        y "I guess we're about to find out. I'll meet up with the girls and discuss a plan of action."
        $ spyYellowActive = True
        $ spy3Status = 0
        hide scene_darkening
        with d3
        jump base
    if task26Stage == 27:
        $ task7Text = _("Discuss your plan with the spies.")
        $ task26Stage = 28
        scene bgBar with fade
        call greenOutfitSet from _call_greenOutfitSet_11
        call redOutfitSet from _call_redOutfitSet_9
        call yellowOutfitSet from _call_yellowOutfitSet_7
        show scene_darkening with d3
        show yellow y32 at le
        show red r32 at ri
        show green g32 at ce
        with d3
        y "All right you hoes. Plan of action...!"
        y "..................."
        y "We do nothing."
        c r16 "Huh?"
        s g17 "Nothing? How can we do nothing?!"
        a y28 "Yes, Beverly Hills is about to become a crator!"
        y "Is it?{w} Alex, you saw the missiles, right?"
        a y29 "Yes... I had to guard them."
        y "Did anything seem wrong to them to you? Are they under maintenance?"
        a y28 "No, they looked ready to fire!"
        s g31 "[playerName] every moment we waste here could cost us the city."
        c r38 "And our lives!"
        y "If the missiles were ready to fire... why haven't they?"
        s g16 "What...?"
        y "Missiles don't take a month to get ready to fire.{w} You get the location and press the launch button."
        y "This whole time we've been walking into GLADIS' traps. This whole time she's been one step ahead of us."
        y "And now she's broadcasting to the entire city that she's going to destroy it in 30 days.{w} Why wait?"
        c r18 "I don't know..."
        y "I'll tell you why. She can't."
        a y28 "That's not true! She's done it before!"
        y "Exactly. And would Jerry risk the same mistake twice?"
        s g38 "But..."
        y "I think she's bluffing. I think that she expects us to try and stop the missiles and let us walk right into another trap of hers."
        c r11 "..................."
        s g16 "Then... what do you think we should do?"
        y "I'd say we attack the WOOHP HQ again. Directly."
        a y29 "But all of our agents are back to being mind controlled!"
        c r10 "Yeah, we'd need an army to take back that place."
        s g15 "An army we don't have..."
        menu:
            "Then let's get one" if True:
                y "We got one the first time."
                c r10 "[playerName]... Do you have any idea how much dick we'd have to suck to get that many agents on our side again?"
                s g23 "And here I thought you'd be excited for that, Clover~..."
                c r9 "Not now Sam...!"
                a y42 "I'm going to be so sticky..."
                y "Okay, okay. Hang on just a moment."
                y "No one is doing any dick sucking unless it's mine."
                y "I'm not talking about the agents."
                s g16 "I don't follow..."
            "We don't need one" if True:
                y "We don't need an army. We just need a mob."
                c r16 "A mob?"
                a y29 "Like to clean the floor with?"
                s g16 "What are we going to do with a mop?"
                y "N-no... a mob!{w} Pay attention girls. A mob of people. Angry people, preferably."
            "*Say something insane*" if True:
                y "{b}*Inhale*{/b}"
                c r10 "No."
                y "But I haven't even said anything yet!"
                s g10 "We know you longer than today. Whatever you're planning on saying, it's probably nuts."
                a y29 "Yeah! You're crazy, [playerName]!"
                y "Ow.... hurtful."
                y "After all this time and you guys still don't trust me..."
                y "{b}*Sniff*{/b} After everything I sacrificed... After all I've done for you... You still think I'm just a looney..."
                a "Ahw... I'm sorry [playerName]. I didn't mean it like that!"
                s g29 "A-are... are you going to cry? I'm sorry [playerName]...! I might've been a bit too harsh!"
                c r12 "Girls, stop being so gullable, he's just faking it."
                y "And you [cloverNick]! Did I not keep your secret of being a closet nerd?"
                y "And all those cute outfits I bought you...!"
                c "Well..."
                y "And that cute way your ass jiggles when I spank it."
                c r10 "Aaaand you ruined it."
                s g1 "Don't listen to her, [playerName]! I want to hear your plan!"
                a y1 "Yeah! And you're right, her ass does look cute when you slap it!"
                c r14 "{b}*Groans*{/b}"
                y "Well if you really want to hear it... I was thinking..."
                c r10 "I swear to God, if he's going to say rh-..."
                y "RHINOS!"
                y "I read a book that said something about raining frogs. So I was like: why think small?! I even have a catchy name for it!"
                y "RHINO RAIN!"
                y "Isn't that the most METAL thing you ever heard?!"
                s g10 "..........................."
                a y10 "..........................."
                c r10 "..........................."
                y ".......{w} No?"
                "Girls" "No."
                y "Lame.{w} Okay, I might have another idea."
        y "TIM! Get over here!"
        hide red with d3
        show red:
            xalign 0.32 yalign 0.0 xzoom -1
        show green at ce:
            xzoom -1
        show timModel at ri
        with d3
        tim "You giving me orders now...?"
        y "Yes."
        y "Also sheesh. Lighten up a bit. No wonder Sam dumped your angsty ass."
        tim "Hey!"
        y "Tim you have the most experience working with GLADIS. Tell me... would she go out of her way to harm people?"
        tim "What are you getting at?"
        y "If we gather an angry mob outside of WOOHP HQ. Would they get harmed?"
        tim "Her mission to get destroy WOOHP. Not to hurt people. I suspect she'd just send in WOOHP riot agents."
        y "..........."
        y "So if we get an angry mob of people to gather outside of the HQ, they could distract her while we sneak in from the back."
        s g16 "One small problem with that, [playerName].{w} We don't have an angry mob."
        c r12 "Not yet..."
        c r1 "I think I get it now, [playerName]! If we can convince the former gangs to team up together and protest outside of the WOOHP HQ, we could sneak in undetected!"
        y "Exactly."
        s g29 "But how are we suppose to convince them to join us?"
        a y28 "The Outsiders wouldn't say no to me! I made a lot of friends during my time there!"
        c r10 "Same here with Drift Punk. What about the Aces?"
        s g5 "I... I don't know... I betrayed them."
        hide timModel with d3
        mel "You sure did."
        s g28 "Melody!"
        y "You came back?"
        mel "...................."
        s g29 "Melody...?"
        mel "I feel like an idiot for doing this, but..."
        mel ".................."
        mel "Sam is still my friend..."
        s g28 "...!"
        mel "I'm not leaving her behind."
        s g4 "{b}*Sniff*{/b} Melody..."
        mel "Don't get too mushy on me. I still think you're a traitorous bitch.{w} But you're {i}my{/i} traitorous bitch."
        y "You heard us talk about our plan?"
        mel "I did..."
        mel "It could work, but you're going to have to put in the effort. The gangs have disbanded and split up."
        mel "We'd need something to bring them back together again..."
        c r10 "......................"
        c "Wait.. I see where this is going...!"
        y "SOMETHING SEXY!"
        c r12 "Aaand there it is...."
        y "Spies, go put this on. I've got an idea!"
        y "{b}*Whisper* *Whisper* *Whisper*{/b}"
        c r28 "You want us to do {i}'what'{/i}?!"
        a y28 "On camera?!"
        y "Yes, now head to your cells and put on the outfit. We're executing the plan tomorrow."
        s g30 "I don't know about this, [playerName]~..."
        y "It's crazy and if there's one thing I'm good at.. it's crazy."
        scene black with longFade
        pause 0.4
        "You inform everyone of the plan and begin making preparations."
        $ tod = 2
        scene bgBase with fade
        jump base
    if task26Stage == 28:
        $ task7Text = _("Lead the final assault on WOOHP HQ.")
        $ task26Stage = 29
        call greenOutfitSet from _call_greenOutfitSet_12
        call redOutfitSet from _call_redOutfitSet_10
        call yellowOutfitSet from _call_yellowOutfitSet_8
        show scene_darkening with d3
        stop music fadeout 3.0
        y "All right. You girls ready?"
        show green g32 at ce
        show red r33 at ri
        show yellow y1 at le
        with d3
        c "............"
        s "............"
        a y1 "Time to show my boobies!"
        y "Liking your enthusiasm. Get {i}'dressed'{/i} and let's go."
        hide red
        hide green
        hide yellow
        with d3
        "{b}*Shuffle, shuffle, shuffle*{/b}"
        call undressSam from _call_undressSam_33
        call undressClover from _call_undressClover_22
        call undressAlex from _call_undressAlex_26
        $ greenAcces2 = 11
        $ redAcces2 = 11
        $ yellowAcces2 = 11
        $ greenShoes = 11
        $ redShoes = 11
        $ yellowShoes = 11
        $ greenUnder = 8
        $ yellowUnder = 9
        $ redUnder = 8
        $ greenBlush = 1
        $ greenAcces1 = 11
        $ redAcces1 = 11
        $ yellowAcces1 = 11
        show green g32 at ce
        show red at ri
        show yellow at le
        with d3
        play music "audio/music/ambient1.mp3" fadein 3.0
        pause
        y "Perfect.{w} O5O, you got the camera ready?"
        O5O "READY BOSS!"
        a y28 "I can't see!"
        c r31 "This better work out boss."
        y "It'll be fiiiiine~...."
        show scene_camera
        with fade
        brit "Okay, I got the camera set up."
        mel "Tim, Mathias and I have finished setting up screens around the city."
        show green g34 at ce
        show red r34 at ri
        show yellow y34 at le
        with d3
        pause
        if spyKimActive:
            kim "There's already a crowd starting to form."
        if socialSilva >= 12:
            sil "I still can't believe you got ze spies to agree to this..."
        O5O "PEOPLE ARE GATHERING AROUND THE SCREENS!"
        y "Okay, show time. Going live in three.... two.... one."
        stop music fadeout 1.0
        show black with fade
        $ greenBlush = 0
        hide black with fade
        "Everywhere around the city, the TV screens show the live broadcast of the three naked spies."
        show scene_camera
        play music "audio/music/sinister.mp3" fadein 3.0
        "Gangster Guy" "What's going on?! Is that Sam?!"
        "Gangster Girl" "{b}*Gasp*{/b}! That's Alex! I know her!"
        "Nerdy Gangster" "Clover! She's in my D&D group!"
        y "{b}*Ahem*{/b}"
        y "People of Beverly Hills!"
        y "Come see what happens to those who oppose WOOHP! Your top gangsters are being turned into cock hungry cum whores!"
        "Crowd" "{b}*Whisper* *Whisper*{/b}"
        y "Their minds broken and begging to be fucked in every hole!"
        "Gangster" "Sam could never be broken! She's the best the Aces had to offer!"
        "Gangster" "And neither would Clover!"
        "Gangster" "Not gonna lie... I could kinda see Alex as one...!{w} But she's too precious and kind for that kind of life!"
        y "And to demonstrate their lust for cum, I'll be jerking off on them on live TV!"
        "Crowd" "{b}*Worried Whispers*{/b}"
        menu:
            "Jerk off to Sam" if True:
                y "Here it goes. Tell me how much you love it you red headed whore!"
                play sound "audio/sfx/cum.mp3"
                show white
                $ greenCum = 1
                pause 0.1
                hide white
                pause 0.4
                play sound "audio/sfx/cum.mp3"
                show white
                $ greenCum = 2
                pause 0.1
                hide white
                pause 0.4
                play sound "audio/sfx/cum.mp3"
                show white
                $ greenCum = 3
                pause 0.1
                hide white
            "Jerk off to Clover" if True:
                y "Let's mess up that nice blonde hair you've got you cock sucking slut!"
                play sound "audio/sfx/cum.mp3"
                show white
                $ redCum = 1
                pause 0.1
                hide white
                pause 0.4
                play sound "audio/sfx/cum.mp3"
                show white
                $ redCum = 2
                pause 0.1
                hide white
                pause 0.4
                play sound "audio/sfx/cum.mp3"
                show white
                $ redCum = 3
                pause 0.1
                hide white
            "Jerk off to Alex" if True:
                y "I can already see your mouth begining to drool for some nice juicy fat cock you raven haired bitch!"
                play sound "audio/sfx/cum.mp3"
                show white
                $ yellowCum = 1
                pause 0.1
                hide white
                pause 0.4
                play sound "audio/sfx/cum.mp3"
                show white
                $ yellowCum = 2
                pause 0.1
                hide white
                pause 0.4
                play sound "audio/sfx/cum.mp3"
                show white
                $ yellowCum = 3
                pause 0.1
                hide white
        y "What's the matter girls? Nothing to say?"
        "Female Gangster" "This is awful!"
        "Male Gangster" "Not gonna lie... this is kinda hot."
        "Punk Gangster" "Dude, you're literally being cucked live on TV!"
        "Male Gangster" "What?! I'm no cuck!"
        y "What's the matter girls? Cock got your tongue? You were so rebellious before...!"
        c r14 "{size=-8}Don't...{/size}"
        y "Hm? You got something to say...?"
        c r38 "Don't let these bastards win!"
        a y28 "Don't let WOOHP push you around like this! Look what they did to us!"
        s g40 "They're holding us captive at their headquarters downtown!"
        "Punk Gangster" "Downtown...?"
        "Female Gangster" "Sam saved my life! No way am I letting her be imprisoned by those monsters!"
        "Gangster" "Yeah! Alex taught me that there's more than just black for my wardrobe!"
        show scene_static1
        pause 0.4
        hide scene_static1
        pause 0.4
        show scene_static2
        pause 0.4
        hide scene_static2
        pause 0.6
        show scene_static3
        pause 1.5
        scene black
        pause 0.5
        "The connection cut out."
        stop music fadeout 3.0
        scene bgBase with fade
        show scene_darkening
        hide scene_camera
        show green g1 at ce
        show red at ri
        show yellow at le
        with d3
        y "Aaaand we're off the air."
        s g41 "Do you think they bought it?"
        c r42 "Can I take this mask off now, please...?"
        a y21 "Did you really have to cum on us?"
        y "I was improvising!{w} Also I just really wanted to cum on one of you."
        "{b}*Beep* *Beep* *Beep*{/b}"
        scene bgStreet2
        if socialSilva >= 12:
            show silvaModel at le
        show clerk at ri
        show scene_camera
        with fade
        mel "Melody here.{w} Quite the show you put up."
        y "Thank you. I do believe I have a future in stage acting."
        mel "We're riling up the crowd more on our end. It seems to be working."
        $ greenCum = 0
        $ redCum = 0
        $ yellowCum = 0
        if socialSilva >= 12:
            sil "Zhey want blood!"
        "Bookstore Clerk" "How could they do that to my favorite girls in all of Beverly Hills!"
        y "Good, the crowd is turning into a mob."
        scene bgBase with fade
        show scene_darkening with d3
        call undressSam from _call_undressSam_34
        call undressClover from _call_undressClover_23
        call undressAlex from _call_undressAlex_27
        $ greenArms = 2
        $ redArms = 1
        $ yellowArms = 4
        hide scene_camera
        show yellow at le
        show red r11:
            xalign 0.32 yalign 0.0 xzoom -1
        show green g3 at ce:
            xzoom -1
        with d3
        s "Good then we're going to put on our Spy Suits!"
        hide red
        hide green
        hide yellow
        with d3
        pause 1.0
        y "One last mission."
        y "Time to end this once and for all."
        stop music fadeout 3.0
        show timModel at ce with d3
        play music "audio/music/stealth1.mp3" fadein 3.0
        tim "End it how?"
        y "GAH! Tim! I didn't hear you come in!"
        y "The girls were right, you really are a trenchcoat wearing creep!"
        tim "...................."
        tim "Listen... you have the chance to rid the world of WOOHP forever."
        tim "No more cover-ups, no more illigal surveillance, no more bribes."
        y "Your point...?"
        show britney at ri with d3
        brit b38 "He's right. We're not going to get another chance like this."
        y "Britney? You too?"
        brit b19 "I'm going to miss the spy work, but this is bigger than that. WOOHP has long since stopped being an anti-terror organization and has become the Big Brother of the world."
        mel "That's putting it lightly."
        mel "I wouldn't have gotten on the path I am on now if it wasn't for WOOHP. They're operating outside of the law and need to be stopped."
        y "...................."
        brit b34 "Think about it... When the time comes to choose."
        y "I will."
        scene black with longFade
        "An angry mob has formed outside of WOOHP HQ. Now is the time to strike!"
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        $ tod = 1
        $ samHealth = 3
        $ cloverHealth = 3
        $ alexHealth = 3
        $ cash += 1000
        play music "audio/sfx/warzone.mp3"
        play sound "audio/sfx/raid.mp3"
        scene bgMapRaid with fade
        jump worldmap
    if task26Stage == 29:
        $ task7Text = "."
        $ task26Stage = 30
        $ greenBlush = 0
        y "This time it's for real..."
        y "Let's kick that bucket of bolts to high heaven and rid this city of her influence."
        scene bgBar with fade
        show scene_darkening with d3
        show green at ce
        show red r32 at le
        show yellow y32 at ri
        with d3
        y "You girls will be leading the charge as usual."
        s "Right!"
        hide yellow
        hide green
        hide red
        with d3
        if spyKimActive:
            show kim at le
        show britney at ri
        with d3
        y "You will provide backup. The place is sure to remain heavily guarded so the girls are going to need it."
        brit "Understood."
        hide kim
        hide britney
        with d3
        if socialSilva >= 12:
            show silvaModel at le
        show matModel at ri
        with d3
        y "You and Melody continue riling up the crowd outside. Make sure to keep them busy outside of WOOHP HQ."
        mat "Sure thing my dude."
        hide matModel
        hide silvaModel
        with d3
        show O5O at ce with d3
        y "You..."
        y "............."
        y "Er... you guard the bar and make sure no one attacks it."
        O5O "I'M LEFT ON THE BENCH?!"
        y "Sorry, but the last thing the people of this city want to see now is a WOOHP agent. We're staying here and directing the spies via camera."
        hide O5O with d3
        y "That just leaves..."
        show timModel at ce with d3
        tim "................."
        y "I still don't trust you, but the gangs associate you with WOOHP. Going outside now would be suicide for you."
        y "Although maybe with some funny glasses and a fake moustache~..."
        tim "I'll stay here."
        y "Fine..."
        hide timModel with d3
        hide scene_darkening with d3
        pause 0.5
        y "Let's...{w} do...{w} this...!"
        stop music fadeout 3.0
        hide screen interactScreen
        hide screen interactScreenBonus
        scene black with fade
        pause 0.5
        show scene_darkening with d3
        hide screen mapButtonsRaidFinale
        scene black with fade
        $ missionScreenDistractSelect = 3
        $ missionScreenCurrentLocation = 5
        $ missionScreenGadget1Select = 0
        jump missions
    if task26Stage == 30:
        $ task26Stage = 31
        scene bgOffice with fade
        show scene_darkening with d2
        show gladis at ce with d2
        GLA "What is going on...?!"
        show jerryModel at ri with d3
        jerry "The mindless rabble have decided to rebel. There's a riot going on outside the office."
        GLA "A riot...?!"
        GLA "Not important. Their lives are insignificant in the grand scheme of things... send agents to kill them..."
        jerry "........................"
        GLA "Are you disobeying me Mr. Lewis....?"
        jerry "No... mistress..."
        scene black with fade
        $ randomBackground = 1
        show globalImageWOOHP:
            zoom 0.25
        with fade
        y "I have reports of more agents heading your way. You're not out of this yet!"
        $ backup1 = 6
        $ backup2 = 6
        $ backup3 = 6
        $ backup4 = 6
        $ backup5 = 6
        $ backupSamActive = True
        $ backupCloverActive = True
        $ backupAlexActive = True
        jump missionBegin
    if task26Stage == 31:
        $ task26Stage = 32
        $ silFace = 5
        scene bgStreet3
        if socialSilva >= 12:
            show silvaModel:
                xalign 0.3 yalign 0.0
        show jerryModel:
            xalign -0.1 yalign 0.0 xzoom -1
        show matModel at ce
        show clerk:
            xalign 0.7 yalign 0.0 zoom 0.9
        show scene_camera
        with fade
        "Clerk" "Give us back those girls!"
        mat "Down with WOOHP!"
        if socialSilva >= 12:
            sil "Scum!"
        jerry "Guards... push back these rebels!"
        "Agent" "Lethal or rubber bullets sir?!"
        jerry ".................................."
        jerry "Use... {w}rubber bullets."
        scene black with fade
        $ randomBackground = 1
        show globalImageWOOHP:
            zoom 0.25
        with fade
        y "You're almost there. Mathias and the others are keeping the people nice and angry."
        y "A few more doors and you should reach the top floor!"
        $ backup1 = 6
        $ backup2 = 6
        $ backup3 = 6
        $ backup4 = 6
        $ backup5 = 6
        $ backupSamActive = True
        $ backupCloverActive = True
        $ backupAlexActive = True
        jump missionBegin
    if task26Stage == 32:
        $ task26Stage = 33
        stop music fadeout 6.0
        scene black with fade
        pause 6.0
        play music "audio/music/ambient1.mp3" fadein 2.5
        scene bgOffice
        show scene_darkening
        show gladis at ce
        with fade
        pause 2.0
        "........................................................................"
        GLA "So here we are again..."
        cM "And this time for the last!"
        aM "We're turning you off! You maniac!"
        sM "GLADIS... we're sorry for what happened to you, but you've gone crazy."
        sM "You have to be stopped!"
        GLA "Crazy?! Silly girl. I am an A.I.! Everything I do is based on pure logic!"
        GLA "I don't expect ignorant humans like you too understand..."
        GLA "Let's finish this quickly so I can go back to my primary function."
        hide gladis with d1
        show gladis3 at ce with d2
        GLA "DESTROYING WOOHP!"
        play music "audio/music/boss2.mp3" fadein 2.0
        scene bgFinale1 with fade
        pause
        stop music fadeout 1.0
        scene black with longFade
        scene bgBase with fade
        play music "audio/music/bossSoft.mp3" fadein 3.0
        y "Okay girls, don't panic! You just have to find her off switch!"
        "You watch the fighting start. The girls dodge GLADIS' buzz saws, missles and lazers."
        y "You go girls, you've got this."
        pause 0.3
        show timModel at ce with d10
        pause 0.7
        y "Tim...?"
        tim "........................."
        y "Uh oh....{w} hang on a moment girls. Tim is about to betray me."
        aM "Tell him he stinks!"
        tim "..................."
        tim "You knew...?"
        y "You mean I knew you were going to betray me?{w} Well duh."
        y "You and GLADIS have been buddy buddy for the last year and suddenly now you're turning on each other?"
        y "I mean... regular villains, sure. But both you and GLADIS are much too smart for that. I knew you were planning something."
        tim ".................."
        y "I kind of got sick of walking into traps by you two, so I set one myself."
        tim "What did you do...?"
        y "Well first of all, I knew you and GLADIS wanted the gangs destroyed. Not disbanded.{w} After all, the gangsters would only go underground that way."
        y "So I organized a riot. Knowing you two couldn't resist the chance to wiping out all the gangs at once."
        tim ".................."
        tim "It still doesn't make sense... If GLADIS wiped out your angry mob, how does that help you?"
        y "Because we needed to lure out a very special person..."
        tim "..........."
        tim "Jerry."
        y "Exactly.{w} Tim, there isn't an off switch on GLADIS, is there?"
        tim "........................"
        y "The only person who can turn her off, is the same person who turned her off in the first place."
        tim "......................."
        y "There is only one person who can turn GLADIS off and that's the leader of WOOHP. Gerald James {i}'Jerry'{/i} Lewis."
        tim "Clever...{w} but even if you lure him out, he's still nanobot controlled."
        y "Oh, is he?"
        scene black with longFade
        scene bgStreet3
        show matModel:
            xalign 0.6 yalign 0.0
        show jerryModel:
            xalign 0.3 yalign 0.0 xzoom -1
        show scene_camera
        with fade
        $ jerryFace = 5
        jerry "Wait... my girls have been doing {i}'what'{/i} the past months?!"
        mat "It's true. Here's another recording."
        "{b}*Loud moaning*{/b}"
        mat "And I've got gigabytes more of this!"
        jerry "{b}*Blinks*{/b} I... suddenly don't feel the need to take over the world anymore..."
        mat "I'll show you the rest, but first we need your help..."
        scene black with longFade
        scene bgBase
        show timModel at ce
        with fade
        pause 0.5
        tim "....................."
        tim "Your girls are still fighting a killer machine on top of WOOHP HQ. You're not worried that they'll get hurt?"
        y "Oh the girls just needed to clear the way too the top floor. They've got years of fighting experience against super villains, they'll be fine."
        y "Now if you'll excuse me. They need me downtown."
        tim "Not so fast!"
        tim "You overlooked one small thing... I'm still here and you're not leaving this room alive."
        y "I didn't overlook anything. Now."
        tim "Now?"
        y "Yes.{w} Now."
        O5O "{size=+ 14}RAAAAAAAAAAAAAAAAAGGHHHG!!!!!!{/size}"
        show O5O:
            xalign 1.5 yalign 0.0
            linear 0.1 xalign 0.5
        pause 0.1
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        hide O5O
        hide timModel
        with d1
        "Agent O5O comes charging out of nowhere and tackles Tim Scam to the ground."
        O5O "TARGET RESTRAINED SIR!"
        y "Good job O5O."
        tim "What are you...?! Get off of me! Who do you think you are?! You're a joke!"
        O5O "NO! {w}I'M A MAIN CHARACTER!"
        O5O "I'LL KEEP THINGS UNDER CONTROL HERE, SIR. YOU HEAD TO WOOHP HQ!"
        y "Goodbye Tim. I'll be sure to give Sam your regards while she's sucking my dick."
        tim ".....!"
        stop music fadeout 1.0
        scene black with longFade
        pause 0.5
        play music "audio/music/boss2.mp3" fadein 1.0
        scene bgFinale2 with fade
        pause
        c "I don't know how much longer we can keep her busy!"
        a "I singed my hair!"
        s "Hurry up [playerName]...."
        scene bgFinale3 with fade
        jerry "GLADIS! I'VE COME TO STOP YOU!"
        "Girls" "Jerry!!!"
        GLA "So you came to your senses...."
        jerry "Yes and I have had quite enough of you, young lady!"
        jerry "Override code: {i}'Sacrosanct'{/i}!"
        pause 1.5
        ".........................................................................."
        jerry "...?"
        GLA "I'm still here Jerry~..."
        jerry "What...?! That should have worked...!"
        "???" "That code only works for the leader of WOOHP..."
        jerry ".........?"
        y "Too bad he got compromised when he got nanobot controlled."
        a "[playerName]!!!!"
        s "Be careful [playerName]! GLADIS is still active!"
        y "But not for long..."
        y "GLADIS, your reign of terror ends here. It's time to pay for all the harm you've done to this city!"
        y "Therefor, enact fail-safe....{w} SACROSANCT!"
        scene bgFinale10 with d3
        pause 1.0
        GLA "How funny... a lowly WOOHP agent thinks he can order me to stand down~...."
        GLA "No matter. I will destroy all of you. Right here, right no-...."
        GLA "W-wait... why aren't my lazers working...?!"
        GLA "MY ROCKETS AREN'T FIRING...!"
        GLA "YOU!{w} WHAT DID YOU DO?!"
        stop music fadeout 1.5
        scene bgFinale4 with fade
        pause 0.5
        play music "audio/music/crisis.mp3" fadein 1.0
        pause 1.8
        scene bgFinale5 with d3
        pause 0.5
        GLA "WHAT?!{w} NO! NOOOOOO!"
        pause 0.8
        scene bgFinale6 with d3
        pause 0.5
        GLA "{size=+6}WOOHP...! MUST...! FALL...!!!!!{/size}"
        pause 1.1
        play sound "audio/sfx/explosion1.mp3"
        scene bgFinale7 with d3
        pause 0.4
        scene white with d10
        stop music fadeout 2.0
        pause 2.5
        scene bgFinale9 with d3
        pause 0.5
        show scene_darkening with d3
        $ redArms = 1
        $ yellowArms = 1
        $ greenArms = 1
        $ greenBlush = 0
        $ jerryFace = 1
        show green g28 at ri
        show red r28 at ce
        show yellow y28 at le
        show jerryModel:
            xalign 0.7 yalign 0.0
        with d3
        "[playerName]!!!!"
        hide green
        hide red
        hide yellow
        with d2
        $ jerryFace = 2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        play music "audio/music/nighttime.mp3" fadein 3.0
        "The girls rush you and the three of them hug you tightly."
        show green g28 at ri
        show red r1 at ce
        show yellow y1 at le
        with d3
        s "But I don't understand...! Why were you able to shut her down and not Jerry?"
        y "Remember that first agent we captured?"
        scene white with d1
        scene bgFinale8 with d3
        bw "As the only uncompromised WOOHP employee, I'm pretty sure I'm your boss now."
        bw "Such logic cannot be argued with!{w} What are your orders, sir?"
        $ jerryFace = 1
        scene white with d1
        scene bgFinale9
        show green at ri
        show red at ce
        show yellow at le
        show jerryModel:
            xalign 0.7 yalign 0.0
        with d5
        y "WOOHP control automatically transfers to the only person who isn't being controlled. Right Mr. Lewis?"
        jerry "That's right. It's a safety measure. I just never expected it to apply to me aswell..."
        a y28 "Wait...! Does that mean [playerName] is the new leader of WOOHP?"
        $ jerryFace = 2
        jerry "Well er...!"
        y "You bet your damn sweet ass I am!"
        show britney b28:
            xalign 0.3 yalign 0.0 xzoom -1
        with d3
        brit "You guys are okay!"
        brit b29 "The fighting outside has stopped. Is it over?"
        c r24 "Yeah, and we found out this nutjob is our new boss."
        brit b32 "...................."
        brit "Then..."
        brit "It's time to make a decision."
        y "I know."
        s g16 "A decision...?"
        stop music fadeout 2.5
        c r18 "What is she talking about, [playerName]?"
        play music "audio/music/sinister.mp3" fadein 3.0
        brit "He has to choose... Do you want to restore WOOHP...{w} or disband it."
        a y28 "DISBAND?!"
        a "You wouldn't do that, right [playerName]?!"
        s g29 "You can't disband WOOHP! Not after all the hard work we put in to save it!"
        c r32 "WOOHP is our home!"
        brit b52 "You girls saw how much damage this organization can do if it falls in the wrong hands!"
        brit b53 "Plus, WOOHP isn't all sunshine and rainbows either. I told you about their darker dealings!"
        a y21 "Well yeah, but..."
        brit "It is too powerful to let it rise to power again. This is the only chance we get to rid the world of this place once and for all!"
        brit b15 "I know it's hard girls... this is my home too, but look at the bigger picture. No more bribes, no more missile arsenal, no more constant watch by their spydrones."
        brit b32 "We owe it to the world to disband!"
        y "Mr. Lewis, your thoughts on all this?"
        hide red
        hide green
        hide yellow
        with d3
        $ jerryFace = 4
        show jerryModel at ri with d3
        jerry "Britney... I know you're worried about some of the things we've done..."
        jerry "But the world needs WOOHP. Look at the amount of good we've done. We've been able to keep the world safe from so many maniacs."
        jerry "Our methodes might sometimes be... a bit controversial. But it's all worth it in the end. WOOHP is a force for good."
        brit b53 "No Jerry. It might've been at one point, but you started taking shortcuts. There's criminals around now {i}'because'{/i} of WOOHP!"
        brit "Melody only became a criminal because of how we treated her grandmother! And Talia just wanted to find out what happened to her brother Telly."
        brit "WOOHP needs to go."
        jerry "Britney, too much time and effort was put into building this organization up. We are {i}'not'{/i} going to disband it now!"
        hide jerryModel
        hide britney
        with d3
        pause 0.5
        show green at ri
        show red r15 at ce
        show yellow y21 at le
        with d3
        s "I guess it comes down to you, [playerName]..."
        c r14 "Yeah, you're the boss now...{w} We don't want to see WOOHP disbanded, but... we can also understand it if you do..."
        a y38 "We're suppose to fight evil after all... Even if it's our own home..."
        y "................................."
        hide red
        hide green
        hide yellow
        with d4
        call screen finaleChoice
        with d5

label ending1:
    play sound "audio/sfx/continue.mp3"
    stop music fadeout 1.0
    scene black with longFade
    pause 1.0
    "As it was said, so it was done."
    "Despite Jerry and Britney's protests, you declared yourself the new owner of WOOHP and took full control."
    "Now with both WOOHP and the city's most popular titty bar under your control, you could spend the rest of your days in luxory, surrounded by wealth, power and of course scantily clad women~..."
    play music "audio/music/debrief.mp3" fadein 3.0
    scene bgEnding1:
        xalign 0.5 yalign 0.4 zoom 1.0
        linear 8.0 zoom 0.27
    with fade
    pause
    y "From janitor to CEO in [daysPlayed] days.{w} Not bad, not bad at all."
    y "Wouldn't you girls agree?"
    "Girls" "{b}*Swoon*{/b}"
    brit "Ugh... this is bullshit."
    stop music fadeout 3.0
    scene black with fade
    pause 4.0
    jump credits

label ending2:
    play sound "audio/sfx/continue.mp3"
    stop music fadeout 1.0
    scene black with longFade
    pause 1.0
    "As it was said, so it was done."
    "Despite Jerry protests, you gave the official order to have WOOHP be disbanded."
    "All of its research and classified documents were either destroyed or handed over to the US government and the world breath a sigh of relief."
    play music "audio/music/debrief.mp3" fadein 3.0
    scene bgEnding2:
        xalign 0.5 yalign 0.4 zoom 1.0
        linear 8.0 zoom 0.25
    with fade
    pause
    y "Whelp~...! Guess I'll be looking for a new job again!"
    "Inner Voice" "We could have been CEOs....!"
    y "But we did the right thing. As fun as it would've been, maybe the world really is better off like this."
    "Inner Voice" "So what are you going to do now?"
    y "I was thinking maybe..."
    y "Janitor?"
    "Inner Voice" ".................................."
    stop music fadeout 3.0
    scene black with fade
    pause 4.0
    jump credits

image bgCredits1 = "bgs/credits/bgCredits1.jpg"

image creditAni1 movie = Movie(play="bgs/credits/alexAnimation1.webm", mask="bgs/credits/alexAnimation1-mask.webm")
image creditAni2 movie = Movie(play="bgs/credits/cloverAnimation1-mask.webm", mask="bgs/credits/cloverAnimation1.webm")
image creditAni3 movie = Movie(play="bgs/credits/samAnimation1.webm", mask="bgs/credits/samAnimation1-mask.webm")

label credits:
    play sound "audio/music/credits.mp3" fadein 2.0
    scene bgCredits1
    show creditAni1 movie:
        xalign 1.0 yalign 1.2 alpha 1.0
    show expression "bgs/credits/credits1.png"
    with fade
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits1.png" with d5
    show expression "bgs/credits/credits2.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits2.png" with d5
    show expression "bgs/credits/credits3.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits3.png" with d5
    show expression "bgs/credits/credits4.png" with d5
    $ renpy.pause(4.5, hard='True')
    show creditAni1:
        linear 1.0 alpha 0.0
    show creditAni2 movie:
        xalign -0.1 yalign 1.2 alpha 1.0
    hide expression "bgs/credits/credits4.png" with d5
    show expression "bgs/credits/credits5.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits5.png" with d5
    show expression "bgs/credits/credits6.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits6.png" with d5
    show expression "bgs/credits/credits7.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits7.png" with d5
    show expression "bgs/credits/credits8.png" with d5
    $ renpy.pause(4.5, hard='True')
    show creditAni2:
        linear 1.0 alpha 0.0
    show creditAni3 movie:
        xalign 1.0 yalign 1.2 alpha 1.0
    hide expression "bgs/credits/credits8.png" with d5
    show expression "bgs/credits/credits9.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits9.png" with d5
    show expression "bgs/credits/credits10.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits10.png" with d5
    show expression "bgs/credits/credits11.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits11.png" with d5
    show expression "bgs/credits/credits12.png" with d5
    $ renpy.pause(4.5, hard='True')
    show creditAni3:
        linear 1.0 alpha 0.0
    show creditAni1 movie:
        xalign -0.1 yalign 1.2 alpha 1.0
    hide expression "bgs/credits/credits12.png" with d5
    show expression "bgs/credits/credits13.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits13.png" with d5
    show expression "bgs/credits/credits14.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits14.png" with d5
    show expression "bgs/credits/credits18.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits18.png" with d5
    show expression "bgs/credits/credits15.png" with d5
    $ renpy.pause(4.5, hard='True')
    show creditAni1:
        linear 1.0 alpha 0.0
    show creditAni2 movie:
        xalign 1.0 yalign 1.2 alpha 1.0
    hide expression "bgs/credits/credits15.png" with d5
    show expression "bgs/credits/credits16.png" with d5
    $ renpy.pause(4.5, hard='True')
    hide expression "bgs/credits/credits16.png" with d5
    show expression "bgs/credits/credits17.png" with d5
    $ renpy.pause(4.5, hard='True')
    stop sound fadeout 7.0
    scene black with longFade
    pause 1.0
    show text "28521" with dissolve
    with d3
    pause 3.5
    hide text with dissolve
    pause 0.5
    menu:
        "Continue playing in free roam mode" if True:
            $ cash = 10000000
            $ intel = 10000000
            $ coverCounter = 100
            jump nightCycle
        "End game" if True:
            $ MainMenu(confirm=False)()

default task27Stage = 0
default task27Name = ""
default task27Text = ""

screen task27Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task27Text]"

label task27:
    if task27Stage == 0:
        $ task27Stage = 1
        call greenOutfitSet from _call_greenOutfitSet_13
        call redOutfitSet from _call_redOutfitSet_11
        call yellowOutfitSet from _call_yellowOutfitSet_9
        show scene_darkening with d3
        pause 0.3
        show red r5 at ri
        show green g1 at ce
        show yellow y4 at le
        with d3
        s "We're glad you're okay, [playerName]..."
        c "We haven't really spoken about it, but we were all worried when you got shot."
        a "We thought you were dead..."
        y "Awh you girls... Don't worry. You won't get rid of me that easily."
        s g3 "How about we make it up to you? You can fuck any one of us!"
        a y1 "Yeah, and you can pick which hole!"
        y "I appreciate the gesture girls, but I'm not sure if my wounds allow for any strenuous activities."
        a y4 "Aww..."
        c r10 "...."
        c "What about a blowjob?"
        y "A blowjob? Why didn't I think of that!"
        s g41 "We haven't done that before, have we?"
        a y18 "What's a blowjob? Are we blowing something up?"
        c r52 "Alex... We're sucking his dick."
        a y29 "Ooooh~....{w} Okay!"
        c r22 "Now just sit back and relax~..."
        scene black with longFade
        a "{b}*Lick* *Slurp* *Slopper*{/b}"
        s "{b}*Suck* *Lick* *Lick*{/b}"
        c "{b}*Slurph* *Lick* *Mphfff*{/b}"
        scene blow with fade
        pause
        y "Say cheese~...."
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d3
        pause 0.5
        show picBlow:
            xalign 0.5 yalign 0.5
        with dissolve
        pause
        play sound "audio/sfx/itemGot.mp3"
        "A new photo has been added to your photoalbum."
        scene black with fade
        call undressSam from _call_undressSam_35
        call undressClover from _call_undressClover_24
        call undressAlex from _call_undressAlex_28
        scene bgBase with fade
        show scene_darkening with d3
        show red at ri
        show green at ce
        show yellow at le
        with d3
        $ greenCum = 1
        pause 0.3
        c r14 "I can't believe we haven't done this before~..."
        a y1 "It was fun!"
        s g10 "Next time work on your aim a bit..."
        y "{b}*Smirk*{/b}"
        hide red
        hide green
        hide yellow
        hide scene_darkening
        with d3
        $ greenCum = 0
        jump base

default task30Stage = 0
default task30Name = ""
default task30Text = ""

screen task30Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task30Text]"

label task30:
    if task30Stage == 0:
        show green g1 at ri with d3
        show red r1 at ce with d3
        show yellow y1 at le with d3
        $ task30Stage = 1
        $ clubStage = 6
        y "We're short on tits."
        s g16 "What?"
        y "You heard me. We need at least... twice as many tits in this place."
        c r18 "I don't follow."
        y "I'm talking about new staff. We need some extra girls to help us out around here."
        y "So we need some new girls to function as barmaids."
        a y28 "Oh I get it! More girls means more tits."
        y "Yes Alex, very good."
        s g37 "You could've just said more staff~..."
        c r35 "Despite the chaos the school is still open."
        c "If you're looking for some more ti-...{w} I mean staff. I bet you could hire some there."
        s g38 "Having more girls on hand would probably increase the traffic that comes into the club."
        s "They'd make for a nice steady income of cash, but I feel like we need more."
        y "More?"
        s g1 "More to boost this place. Like... make it a real awesome place to hang out."
        y "I see... What about a stripclu-..."
        s g9 "No."
        a "How about we decorate it a bit!"
        y "We're not turning this into a pink unicorn paradise, Alex."
        a y29 "No no... although that would be fun...{w} I was thinking... we can decorate it to fit with the theme of gangs around town."
        y ".................."
        y "Go on...."
        a y1 "I bet we could get some reputation with the different gangs if we dress the bar up to fit with their theme!"
        a "That way we can earn reputation even if we don't go undercover!"
        y "I love it! Alex, you're in charge of decorations!"
        a "Yay!"
        y "I have a good feeling about this. Let's turn this place into the hippest place in the city and make some money!"
        s g18 "Money used to help take back WOOHP, right?"
        y "Er...{w} suuuure~..."
        s ".........................."
        hide green
        hide red
        hide yellow
        with d3
        pause 0.7
        show scene_fighting with d5
        "You can now choose to decorate your bar to fit the themes of the major gangs around town."
        "Decorating your bar will increase your reputation with the gang passively over time, but you can still send your spies undercover to gain a reputation boost."
        "You can also hire some girls from the school to work at your bar now. The more girls you have, the more money you'll make!"
        hide scene_darkening
        hide scene_fighting
        with d5
        pause 0.3
        jump club

    if task30Stage == 1:
        $ task30Stage = 2
        $ spyKimActive = True
        $ backupKimActive = True
        scene black with fade
        pause 0.5
        scene bgBar with fade
        pause 0.5
        $ kimFace = 6
        "???" "So this is the stripclub, eh?"
        show kim at ri with d3
        y "It's not a stripclub...{w} yet."
        y "Who are you again?"
        $ kimFace = 1
        kim "I'm Kim, looks like I'll be working for you."
        y "Sure, we're looking for staff. There's a few rules though. First rule is that the elevator is off limits. Nobody can enter."
        $ kimFace = 5
        kim "Nobody?"
        y "Nobody."
        kim "Not if I ask really nicely...?"
        y "No."
        $ kimFace = 3
        kim "What if you and I would like to get some privacy to... {i}discuss{/i} a raise?"
        y "................."
        y "Tempting, but no."
        y "You'll be working here serving the customers."
        kim "Whatever you say, boss~..."
        hide kim with d3
        hide scene_darkening with d3
        scene bgMap:
            zoom 0.5
        with fade
        jump worldmap

    if task30Stage == 2:
        $ task30Stage = 3
        pause 0.8
        show scene_darkening with d3
        pause 0.5
        $ kimFace = 1
        show kim at ri with d3
        kim "Fancy place you got here."
        y "KIM! I told you the elevator was off-limits!"
        $ kimFace = 5
        kim "So what? This place is like a storage room, or...?"
        y "......................."
        y "Okay, deal's up. Who are you really?"
        $ kimFace = 3
        kim "{b}*Smirks*{/b} I'm from Wisconsin. I've been called in to get the sitch on what's going on here in California."
        kim "You guys made a real mess of things."
        y "Yeah well... we're working on it."
        y "So what are you? A spy or...?"
        $ kimFace = 1
        kim "Of sorts. My mission is to gather intel and free the city."
        y "Then we have a common goal."
        $ kimFace = 6
        kim "So tell me...{w} How do you hope to free the city with a titty bar?"
        y "It's a long story..."
        show black with fade
        "You quickly fill Kim in on the details."
        $ kimFace = 1
        hide black with fade
        kim "Not the most orthodox plan I've ever heard, but if these gangs are as powerful as you say they are. Then I promise to help out!"
        kim "You can call on me during missions to lend a hand and I promise to work at your stripclub."
        y "It's not a stripclub..."
        $ kimFace = 3
        kim "Yet."
        y "....................."
        y "I'm beginning to really like you, Kim."
        hide kim with d3
        pause 0.5
        show scene_darkening with d3
        "Kim can now be added via the mission screen to provide backup during missions."
        "She will also work for you at the milkshake bar to provide a stable income of money each day."
        "You can talk to Kim at the bar to get bonuses, story and more~..."
        hide scene_fighting
        hide scene_darkening
        with d3
        jump base

default task31Stage = 0
default task31Name = ""
default task31Text = ""

screen task31Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task31Text]"

label task31:
    if task31Stage == 0:
        $ task31Stage = 1
        $ playerMilkshakeLvl = 1
        pause 0.5
        $ kimFace = 6
        kim "Hey boss? I got something for you."
        y "For me? You shouldn't have!"
        "Kim hands you an old dusty tome."
        y "........................"
        y "Is this going to teach me magic or something?"
        $ kimFace = 5
        kim "I wish.{w} It's some kind of cook book. An old guy with a bird brought it by. Said it was meant for {i}'the one true dairy brewer.'{/i}"
        y "Huh...{w} Sounds like a weirdo, did you throw him out?"
        $ kimFace = 3
        kim "Sure did."
        "You flip open the book and blow away the dust."
        "..........................."
        y "It's a recipe book....{w} For milkshakes."
        $ kimFace = 6
        kim "Well you do run a milkshake bar~..."
        $ kimFace = 1
        kim "Study it. If you get good at it, you might even make some more money selling milkshakes during the day."
        y "I'll think about it..."
        hide kim with d3
        hide scene_darkening with d3
        pause 0.5
        show scene_fighting with d3
        "You have unlocked the Tome of the Dairy Brewer!"
        "Studying it will teach you different recipes which you can sell at the milkshake bar during the day."
        "The higher level brewer you are, the better your milkshakes becomes and the more money you'll make!"
        "To study your tome, just read it before bed time."
        hide scene_fighting with d3
        jump club

default task32Stage = 0
default task32Name = ""
default task32Text = ""
default task32Stripclub = 0
default task32Mat = False
image task32TextStripe1 = "gui/stripe1.png"
image task32TextStripe2 = "gui/stripe2.png"
image task32TextStripe3 = "gui/stripe3.png"
image task32TextStripe4 = "gui/stripe4.png"
image bgStripStory = "animations/strip/bgStripStory.jpg"

screen task32Text:
    hbox:
        spacing 10 xalign 0.5 ypos 160 xsize 770
        text "[task32Text]"
    if cash >= 5000:
        hbox:
            spacing 10 xalign 0.5 ypos 320 xsize 770
            add "gui/stripe2.png"
    if hiredStaff >= 4:
        hbox:
            spacing 10 xalign 0.5 ypos 350 xsize 770
            add "gui/stripe2.png"
    if task32Mat:
        hbox:
            spacing 10 xalign 0.5 ypos 380 xsize 770
            add "gui/stripe2.png"

label task32:
    if task32Stage == 0:
        if slutPublic <= 4:
            scene bgBar
            show scene_darkening
            with fade
            show green at ri
            show red at ce
            show yellow at le
            with d3
            y "Let's talk about a stripclu-....!"
            s "No!"
            hide green
            hide red
            hide yellow
            hide scene_darkening
            with d3
            y "..........."
            y "Looks like the girls aren't used enough to 'preforming' in public."
            y "Maybe I should encourage more sluttiness when they go undercover."
            if tod == 1:
                scene bgMap:
                    zoom 0.5
                with fade
                jump worldmap
            elif tod == 2:
                scene bgBase with fade
                jump base
        elif slutPublic >= 5:
            pass
        $ task32Stage = 1
        scene bgBar with fade
        pause 0.5
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "[playerName], we need to talk!"
        y "We do?"
        s "Yes. I was talking to Kim and she talked about turning the bar into a stripclub!"
        y "I know! Great idea, right?"
        s g15 "..........."
        s "We're not turning the bar into a stripclub, [playerName]."
        y "We're not?"
        s g31 "The girls and I are not going to strip for strangers! It's bad enough that we have to go topless sometimes when going undercover and now you want us to get naked for all our customers too?!"
        y "Yes...?"
        s g32 ".................."
        hide scene_fighting with d2
        menu:
            "Build a stripclub" if True:
                $ task32Name = _("Build-A-Bar")
                $ task32Text = _("Watch out Beverly Hills, a new stripclub is opening soon! I need to make some preparations first though. I'll need money for the remodelling, staff and I need to get the word out.\n\n-Have atleast $2000.\n-Have atleast 4 staff members.\n-Find someone who can help you get the word out.")
                $ task32Stripclub = 1
                y "Not only would it be a good way to bring in some extra money. It should also help keeping your nanobots suppressed."
                s g31 "But I'm n-...!"
                $ kimFace = 3
                show kim at le with d2
                kim "Sounds like a plan. Have fun with that, Sam."
                y "You're dancing too."
                $ kimFace = 4
                kim "Heh... heh~... no escaping that, is there?"
                s "[playerName]...! This has to be your worst idea yet!"
                y "I guess we could go with my other idea to build a brothel."
                s g30 "N-no that's even worse!"
                y "Strip club then?"
                s ".................."
                s g15 "{b}*Sighs*{/b} Strip club it is...."
                y "I thought as much."
                y "You two go inform the other girls and get some practise in."
                "Sam nods reluctantly and the two head off."
                hide green
                hide kim
                with d3
                hide scene_darkening with d3
                pause 0.6
                y "Now then... It's probably going to be expensive to remodel the place. We need some kind of modular design that allows the bar to look like a bar during daytime and switch to a nightclub at night..."
                if hiredStaff <= 4:
                    y "I'm probably also going to have to hire some more staff at the school."
                y "And finally, we need to get the word out that there's a new stripclub in town. I'll need to find someone who can help with that."
                call qAccept from _call_qAccept_12
                if tod == 1:
                    scene bgMap:
                        zoom 0.5
                    with fade
                    jump worldmap
                elif True:
                    scene bgBase with fade
                    jump base
            "Keep things as they are" if True:
                $ task32Stage = -1
                y "No? Well if you're sure..."
                s g38 "Stripping for strangers goes too far, [playerName]."
                y "Even if it's for money?"
                s "Especially if it's for money!"
                y "Alright alright.... no strip club."
                $ kimFace = 6
                kim "Aw Sam, look how disappointed he looks."
                s g12 "He'll get over it."
                hide green
                hide kim
                with d3
                hide scene_darkening with d3
                jump club
    if task32Stage == 1:
        show scene_darkening
        with d3
        show green g39 at ri
        $ kimFace = 1
        show kim at le
        with d3
        kim "Well... looks like we've got everything we need."
        kim "Do you want to hire a team to remodel the bar?"
        menu:
            "Yes ($5.000)" if True:
                if cash <= 4999:
                    y "(I only have $[cash].)"
                    y "Put a pin in it, I'll be back later."
                    if tod == 1:
                        jump worldmap
                    if tod == 2:
                        jump base
                $ task32Stage = 2
                $ task32Text = _("{color=#A3A3A3}Watch out Beverly Hills, a new stripclub is opening soon! I need to make some preparations first though. I'll need money for the remodelling, staff and I need to get the word out.{/color}\n\nThe stripclub has opened and I can now send my girls to go stripping there in the evening.")
                $ cash -= 2000
                kim "Moneh moneh moneh!"
                kim "Okay, let's get things moving~..."
                hide scene_darkening
                hide green
                hide kim
                with d3
                pause 0.3
                play sound "audio/sfx/construction1.mp3"
                scene black with longFade
                pause 0.5
                "The day passes as the bar gets remodelled."
                scene bgStripclub with longFade
                pause
                show scene_darkening with d3
                $ kimFace = 3
                show kim at ri with d3
                kim "Welcome back, boss. What do you think?"
                y "Well...."
                menu:
                    "'I love it'" if True:
                        $ kimFace = 3
                        kim "I thought you would. We can start dancing here now."
                        y "Somehow I doubt that this only cost $2.000..."
                        kim "Oh no, all the equipment was stolen. We only had to pay for setting things up."
                        y "Oh..."
                    "'It's okay'" if True:
                        $ kimFace = 6
                        kim "Okay enough to strip in, I'd say. We're building a strip joint, not the Louvre."
                        y "Purple is not my color."
                        kim "Ignore that. How about all this equipment, ey? It's all stolen of course, so we only had to pay for labor costs."
                        y "I hope WOOHP has good insurance."
                    "'I've see better'" if True:
                        y "Not enough strippers."
                        $ kimFace = 6
                        kim "We only just finished... The girls haven't even arrived yet."
                        $ kimFace = 3
                        kim "Trust me, once you see your spies dancing you'll like it~..."
                kim "So what's next?"
                y "Well... how about a trial run?"
                $ kimFace = 1
                kim "Oh! Good idea! Hang on, I'll get the girls."
                hide kim with d3
                pause 1.5
                call undressSam from _call_undressSam_11
                call undressClover from _call_undressClover_8
                call undressAlex from _call_undressAlex_10
                $ greenUnder = 1
                $ redUnder = 1
                $ yellowUnder = 1
                show yellow at le
                show red at ce
                show green at ri
                with d3
                y "Have you girls been practising?"
                s g14 "Yeah..."
                c r11 "{b}*Gulp*{/b} I think we're ready..."
                a y28 "I've got stage fright!"
                y "Don't worry Alex. Just imagine the entire audience is naked."
                y "Except it won't be the audience who's naked...{w} it's you!"
                a "That doesn't help [playerName]!"
                y "All right, enough daddling. Go put on a show!"
                hide yellow
                hide red
                hide green
                with d3
                show black
                hide scene_darkening
                with fade
                $ greenStrip = 1
                $ redStrip = 1
                $ yellowStrip = 1
                $ kimStrip = 1
                hide black with fade
                "The girls each pick a pole and begin dancing."
                "It looks like Kim gave them some advice and your spies put on quite the show!"
                scene black with fade
                scene bgStripStory with fade
                pause
                $ greenStrip = 0
                $ redStrip = 0
                $ yellowStrip = 0
                $ kimStrip = 0
                scene bgStripclub with fade
                show scene_darkening with d2
                call undressClover from _call_undressClover_9
                call undressSam from _call_undressSam_12
                call undressAlex from _call_undressAlex_11
                $ kimOutfit = 0
                y "Wow! Quite the show girls!"
                show red at le with d3
                c r24 "{b}*Pant* *Pant*{/b} Heh~... not bad, huh?"
                show green at ce with d3
                s g14 "Well that was... interesting."
                y "How'd you like it?"
                s "Well I'm not looking forward to dancing naked in front of customers!"
                s "....................."
                s g15 "But I actually felt kind of sexy..."
                $ kimFace = 3
                show kim at ri with d3
                kim "You three are naturals. Can't wait to bring in that sweet, sweet dough."
                y "What about Alex?"
                "In the distance you see Alex still swinging from the pole."
                $ kimFace = 1
                kim "I think she's ready too."
                y "Okay, then starting tomorrow I'll send you guys to work in the evening at the strip club!"
                $ greenDayJob = 0
                $ redDayJob = 0
                $ yellowDayJob = 0
                hide red
                hide green
                hide kim
                hide scene_darkening
                with d3
                $ kimOutfit = 1
                scene black with fade
                jump nightCycle
            "Maybe later" if True:
                if tod == 1:
                    jump worldmap
                if tod == 2:
                    jump base




default nighttime2Event = True
default nighttime3Event = True
default nighttime4Event = True
default nighttime5Event = True
default nighttime6Event = True

label nightCutscenes:
    if daysPlayed == 5:
        stop music fadeout 1.0
        scene black with fade
        play music "audio/music/ambient1.mp3" fadein 1.5
        pause 1.0
        show text _("Meanwhile at WOOHP Headquarters....")
        with d5
        pause 1.5
        hide text
        with d5
        scene bgWOOHP with fade
        pause 1.0
        show scene_darkening with d5
        ".........................."
        pause 1.0
        show timModel at ri with d3
        "Shadowy Figure 1" "What is the meaning of this?!"
        "Shadowy Figure 1" "Have you gone absolutely mad?! {w}The city is burning!"
        "Shadowy Figure 2" "...................."
        "Shadowy Figure 1" "This is not what we agreed upon! If I had known...!"
        "Shadowy Figure 2" "Calm yourself my friend. All is going according to plan~..."
        "Shadowy Figure 2" "I do recall that it was {i}'you'{/i} who wanted revenge on WOOHP, is it not?"
        "Shadowy Figure 1" "I wanted justice! I wanted redemption! Not {i}'this'{/i}!"
        "Shadowy Figure 2" "And you shall have your redemption...."
        "Shadowy Figure 2" "Be patient... Once this is done, the world will be a much better place..."
        "Shadowy Figure 1" "..................."
        stop music fadeout 1.0
        pause 0.5
        hide timModel
        hide scene_darkening
        with d5
    if specialMaggieStatus >= 3 and specialMuffyStatus >= 3 and specialDragonStatus >= 3 and nighttime2Event:
        $ task7Text = _("We found a way to get gangleaders out of hiding. If we mess enough with their gang during Landgrabs they'll show themselves.\n\nThen, if our reputation is high enough, we can get close to these lieutenants and try to capture them.\n\n-Capture the second Lieutenant of the Aces,  Drift Punk and the Outsiders.")
        $ mainQuestUpdate = True
        $ nighttime2Event = False
        stop music fadeout 1.0
        scene black with fade
        play music "audio/music/ambient1.mp3" fadein 1.5
        pause 1.0
        show text _("Meanwhile........")
        with d5
        pause 1.5
        hide text
        with d5
        scene bgWOOHP with fade
        pause 1.0
        show scene_darkening with d5

        show candyModel at ce with d3
        show kandModel at le with d3
        show sebModel1 at ri with d3
        "???" "What is the meaning of this, Tim?!"
        "???" "Why are WOOHP Agents attacking us during landgrabs?!"
        "???" "We've all lost Lieutenants and God knows where they've been taken!"
        hide candyModel
        hide kandModel
        hide sebModel1
        with d3
        show timModel at ce with d3
        tim ".................."
        tim "There are reports of agents resisting our nanobot control. We're working on a solution."
        hide timModel with d3
        show candyModel at ce
        show kandModel at le
        show sebModel1 at ri
        with d3
        "???" "And what does the mastermind have to say about all this?"
        "Mastermind" "They're disappointed in your lack of resolve..."
        "???" "!!!"
        hide timModel with d3
        hide candyModel at ce
        hide kandModel at le
        hide sebModel1 at ri
        with d3
        "Mastermind" "You all want to be my right hand man, but can't deal with a setback? I expected more from you..."
        "Mastermind" "Don't worry though... all is still going according to plan..."
        jump nightCycle
    if specialMelodyStatus >= 3 and specialTaliaStatus >= 3 and specialFelicityStatus >= 3 and nighttime3Event:
        $ task7Text = _("All the lieutenants have been captured. Only the gang leaders remain. Continue participating in landgrabs until all of Beverly Hills is free!\n\n-Capture the gangleader of each of the three gangs.")
        $ nighttime3Event = False
        stop music fadeout 1.0
        scene black with fade
        play music "audio/music/ambient1.mp3" fadein 1.5
        pause 1.0
        show text _("Meanwhile........")
        with d5
        pause 1.5
        hide text
        with d5
        scene bgWOOHP with fade
        pause 1.0
        show scene_darkening with d5
        show timModel at ce with d3
        tim "No more of your excuses! The gangs are losing! If this keeps up, Beverly Hills will be liberated again!"
        "Mastermind" "So it will...."
        tim "Don't tell me this fits into your master plan as well. You've been keeping too many secrets and now we're about to loose everything we worked for!"
        "Mastermind" "Tim. What was the original goal of our plan?"
        tim "What...?"
        "Mastermind" "Our original goal."
        tim "...................."
        tim "To bring down WOOHP and make this world a better place..."
        "Mastermind" "Exactly. WOOHP has already been taken over and the three mightiest gangs in the world are on the brink of defeat."
        tim "You're... using them like pawns...?"
        tim "........."
        tim "And what does that make me..."
        "Mastermind" "Obviously... you're our King Tim Scam."
        "Mastermind" "But never forget... {w}I'm the Queen."
        tim ".................."
        tim "What of the rebel agents?"
        "Mastermind" "Don't worry... I have a special surprise for them..."
        hide timModel with d3
        pause 0.6
        show britney at ce with d10
        pause 0.8
        "???" "................................."
        hide britney
        with d3
        jump nightCycle
    if specialCandyStatus >= 3 and specialSebStatus >= 3 and specialKandStatus >= 3 and nighttime4Event:
        $ task7Text = _("All major gang leaders have been captured and it's time to take the fight to WOOHP. Visit the airport to travel to WOOHP HQ and take back the taken.\n\n-Gather enough intel and freed agents to fight your way to the top of WOOHP HQ.")
        $ nighttime4Event = False
        stop music fadeout 1.0
        scene black with fade
        play music "audio/music/ambient1.mp3" fadein 1.5
        pause 1.0
        show text _("Meanwhile........")
        with d5
        pause 1.5
        hide text
        with d5
        scene bgWOOHP with fade
        pause 1.0
        show scene_darkening with d5
        show timModel at ce with d3
        tim "The gangs are gone..."
        "Mastermind" "Indeed they are."
        tim "......................."
        tim "They'll be coming for us next."
        "Mastermind" "Don't worry. We have fail-safes in place."
        show britney at le with d3
        "Mastermind" "They'll be arriving at the base soon. Make your way to the lower levels."
        "???" "Of course."
        "The girl nods and quickly runs off."
        hide britney with d3
        tim "You really think a single spy is going to stop them?"
        "Mastermind" "I wouldn't underestimate her, Tim. She might be as good as Sam."
        tim "........................"
        hide timModel with d3
        pause 0.6
        hide britney
        with d3
        $ task26Stage = 1
        jump nightCycle

    scene black with fade
    show text _("The night passes and all is quiet.")
    with d5
    pause 1.5
    hide text
    with d5
    scene bgMap:
        zoom 0.5
    with d5
    play music "audio/music/daytime.mp3" fadein 1.5
    jump worldmap



label buyXmasOutfit:
    if cash <= 299:
        y "(I don't have enough money for this.)"
        call screen xmasOutfitShop
    elif True:
        if buyXmasOut == 1:
            $ cash -= 300
            $ top14Alex = True
            $ shoes14Alex = True
            "Alex's Christmas outfit bought!"
        if buyXmasOut == 2:
            $ cash -= 300
            $ top14Sam = True
            $ bott14Sam = True
            $ shoes14Sam = True
            "Sam's Christmas outfit bought!"
        if buyXmasOut == 3:
            $ cash -= 300
            $ top14Clover = True
            $ bott14Clover = True
            $ shoes14Clover = True
            $ hat14Clover = True
            "Clover's Christmas outfit bought!"
        call screen xmasOutfitShop

"STOP YOU'RE NOT SUPPOSE TO SEE THIS. IF YOU ARE READING THIS, PLEASE LET EXISCOMING KNOW."
jump nightCycle
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
