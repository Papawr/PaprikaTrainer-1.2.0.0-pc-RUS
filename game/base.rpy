label base:

    $ greenArms = 1
    $ redArms = 1
    $ yellowArms = 1


    if task26Stage >= 13 and sexAct6 == "???":
        $ sexAct6 = "Foursome"

    hide screen nanoLevelSam
    hide screen nanoLevelClover
    hide screen nanoLevelAlex

    if month == 10 and 14 <= day <= 31:
        scene bgBaseHalloween
    elif month == 12 and 14 <= day <= 31:
        scene bgBaseChristmas
    elif True:
        scene bgBase
    if tutorialActive == True:
        call screen tutBase
    elif True:

        if task3Stage == 2:
            jump task3


        if task5Stage == 6:
            jump task5
        if task5Stage == 7 and samMood >= 26 and cloverMood >= 26 and alexMood >= 26:
            jump task5

        if task26Stage == 24:
            jump task26
        if baseMessage:
            $ baseMessage = False
            "A new villain has been added to your WOOHP detention center."
            menu:
                "Visit now" if True:
                    $ HQLevelStatus = 1
                    scene black with fade
                    show bgHQ:
                        xalign 0.0 yalign 1.0
                    with fade
                    jump prisonHQ
                "Ignore" if True:
                    pass
        call screen base

default HQMove = 0
default HQLevelStatus = 1
default baseMessage = False

label moveHQ:
    if HQMove == 1:
        if HQLevelStatus == 1:
            $ HQLevelStatus = 2
            show bgHQ:
                xalign 0.0 yalign 1.0
                linear 0.4 xalign 0.0 yalign 0.80
        elif HQLevelStatus == 2:
            $ HQLevelStatus = 3
            show bgHQ:
                xalign 0.0 yalign 0.83
                linear 0.4 xalign 0.0 yalign 0.45
        elif HQLevelStatus == 3:
            $ HQLevelStatus = 4
            show bgHQ:
                xalign 0.0 yalign 0.45
                linear 0.4 xalign 0.0 yalign 0.28
        elif HQLevelStatus == 4:
            $ HQLevelStatus = 5
            show bgHQ:
                xalign 0.0 yalign 0.28
                linear 0.4 xalign 0.0 yalign 0.0
        elif HQLevelStatus == 5:
            pass
        call screen HQButtons
    if HQMove == 2:
        if HQLevelStatus == 5:
            $ HQLevelStatus = 4
            show bgHQ:
                xalign 0.0 yalign 0.0
                linear 0.4 xalign 0.0 yalign 0.28
        elif HQLevelStatus == 4:
            $ HQLevelStatus = 3
            show bgHQ:
                xalign 0.0 yalign 0.28
                linear 0.4 xalign 0.0 yalign 0.45
        elif HQLevelStatus == 3:
            $ HQLevelStatus = 2
            show bgHQ:
                xalign 0.0 yalign 0.45
                linear 0.4 xalign 0.0 yalign 0.80
        elif HQLevelStatus == 2:
            $ HQLevelStatus = 1
            show bgHQ:
                xalign 0.0 yalign 0.83
                linear 0.4 xalign 0.0 yalign 1.0
        call screen HQButtons

default HQLiberated = 0

label assaultHQ:
    if HQLiberated == 0:
        "To lead the assault you will need:\n5 agents\n1000 intel"
        if freedAgents >= 5 and intel >= 1000:
            menu:
                "Lead the assault" if True:
                    stop music fadeout 2.0
                    call undressSam from _call_undressSam_16
                    call undressClover from _call_undressClover_11
                    call undressAlex from _call_undressAlex_15
                    $ greenOutfit = 1
                    $ greenOutfitArms = 1
                    $ redOutfit = 1
                    $ redOutfitArms = 1
                    $ yellowOutfit = 1
                    $ yellowOutfitArms = 1
                    show yellow y32:
                        xalign -0.3 yalign 0.0 xzoom -1
                    show red r32:
                        xalign 0.0 yalign 0.0 xzoom -1
                    show green g32:
                        xalign 0.3 yalign 0.0 xzoom -1
                    show agentModel4:
                        xalign 0.8 yalign 0.0
                    show agentModel2:
                        xalign 1.0 yalign 0.0
                    show agentModel3:
                        xalign 1.3 yalign 0.0
                    with d3
                    "You seem to be prepared and ready to liberate the next floor."
                    play music "audio/music/ambient1.mp3" fadein 1.0
                    $ randAudio = renpy.random.randint(1,3)
                    if randAudio == 1:
                        play sound "audio/voice/agent/hasAnybodySeenMyFlakJacket.mp3"
                    if randAudio == 2:
                        play sound "audio/voice/agent/goingInGunsBlazing.mp3"
                    if randAudio == 3:
                        play sound "audio/voice/agent/locknload.mp3"
                    "Agents" "Go! Go! Go!"
                    play sound "audio/sfx/explosion1.mp3"
                    scene black with fade
                    pause 0.5
                    stop music fadeout 3.0
                    pause 1.5
                    $ HQLiberated = 1
                    show bgHQ:
                        xalign 0.0 yalign 1.0
                    with fade
                    play music "audio/music/nighttime.mp3" fadein 2.0
                    pause 0.8
                    jump task26
                "Wait a moment" if True:
                    call screen HQButtons
        elif True:
            hide HQButtons

    if HQLiberated == 1 and task26Stage >= 6:
        "Required:\n10 Freed Agents\n1000 Intel"
        menu:
            "Lead the assault" if freedAgents >= 10 and intel >= 1000:
                pass
            "Wait" if True:
                stop music fadeout 2.0
                hide yellow
                hide red
                hide green
                hide agentModel4
                hide agentModel2
                hide agentModel3
                with d3
                call screen HQButtons
        stop music fadeout 2.0
        $ intel -= 1000
        call undressSam from _call_undressSam_18
        call undressClover from _call_undressClover_12
        call undressAlex from _call_undressAlex_16
        $ greenOutfit = 1
        $ greenOutfitArms = 1
        $ redOutfit = 1
        $ redOutfitArms = 1
        $ yellowOutfit = 1
        $ yellowOutfitArms = 1
        show yellow y32:
            xalign -0.3 yalign 0.0 xzoom -1
        show red r32:
            xalign 0.0 yalign 0.0 xzoom -1
        show green g32:
            xalign 0.3 yalign 0.0 xzoom -1
        show agentModel4:
            xalign 0.8 yalign 0.0
        show agentModel2:
            xalign 1.0 yalign 0.0
        show agentModel3:
            xalign 1.3 yalign 0.0
        with d3
        y "Okay, we got enough people to take the next floor. Get ready everyone."
        play music "audio/music/ambient1.mp3" fadein 1.0
        hide HQButtons
        $ randAudio = renpy.random.randint(1,3)
        if randAudio == 1:
            play sound "audio/voice/agent/hasAnybodySeenMyFlakJacket.mp3"
        if randAudio == 2:
            play sound "audio/voice/agent/goingInGunsBlazing.mp3"
        if randAudio == 3:
            play sound "audio/voice/agent/locknload.mp3"
        "Agents" "Go! Go! Go!"
        play sound "audio/sfx/explosion1.mp3"
        scene black with fade
        play sound "audio/sfx/gunfight.mp3"
        pause 2.5
        stop music fadeout 3.0
        pause 2.5
        $ HQLiberated = 2
        $ HQLevelStatus = 2
        show bgHQ:
            xalign 0.0 yalign 0.8
        with fade
        pause 0.8
        jump task26

    if HQLiberated == 2:
        "Required:\n12 Freed Agents\n1000 Intel"
        menu:
            "Lead the assault" if freedAgents >= 12 and intel >= 1000:
                pass
            "Wait" if True:
                stop music fadeout 2.0
                hide yellow
                hide red
                hide green
                hide agentModel4
                hide agentModel2
                hide agentModel3
                with d3
                call screen HQButtons
        $ intel -= 1000
        hide HQButtons
        $ randAudio = renpy.random.randint(1,3)
        if randAudio == 1:
            play sound "audio/voice/agent/hasAnybodySeenMyFlakJacket.mp3"
        if randAudio == 2:
            play sound "audio/voice/agent/goingInGunsBlazing.mp3"
        if randAudio == 3:
            play sound "audio/voice/agent/locknload.mp3"
        "Agents" "Go! Go! Go!"
        scene black with fade
        pause 0.3
        $ HQLevelStatus = 2
        show bgHQ:
            xalign 0.0 yalign 0.48
        with fade
        $ HQLiberated = 3
        if task26Stage >= 9:
            $ task26Stage = 8
        jump task26

    if HQLiberated == 3 and task26Stage >= 8:
        if task26Stage >= 10:
            y "With Britney's intel, we should be able to launch the next attack."
        elif True:
            y "We need to plan a mission for WOOHP HQ first and capture Britney."
            scene black with fade
            jump worldmap
        "Required:\n12 Freed Agents\n1000 Intel."
        menu:
            "Lead the assault" if freedAgents >= 12 and intel >= 1000:
                pass
            "Wait" if True:
                stop music fadeout 2.0
                hide yellow
                hide red
                hide green
                hide agentModel4
                hide agentModel2
                hide agentModel3
                with d3
                call screen HQButtons
        $ intel -= 1000
        hide HQButtons
        $ randAudio = renpy.random.randint(1,3)
        if randAudio == 1:
            play sound "audio/voice/agent/hasAnybodySeenMyFlakJacket.mp3"
        if randAudio == 2:
            play sound "audio/voice/agent/goingInGunsBlazing.mp3"
        if randAudio == 3:
            play sound "audio/voice/agent/locknload.mp3"
        "Agents" "Go! Go! Go!"
        scene black with fade
        pause 0.3
        $ HQLevelStatus = 3
        show bgHQ:
            xalign 0.0 yalign 0.48
        with fade
        $ HQLiberated = 4
        jump task26
    if HQLiberated == 4 and freedAgents >= 12 and intel >= 1000:
        "Required:\n12 Freed Agents\n1000 Intel"
        menu:
            "Lead the assault" if freedAgents >= 12 and intel >= 1000:
                pass
            "Wait" if True:
                stop music fadeout 2.0
                hide yellow
                hide red
                hide green
                hide agentModel4
                hide agentModel2
                hide agentModel3
                with d3
                call screen HQButtons
        hide HQButtons
        $ intel -= 1000
        $ randAudio = renpy.random.randint(1,3)
        if randAudio == 1:
            play sound "audio/voice/agent/hasAnybodySeenMyFlakJacket.mp3"
        if randAudio == 2:
            play sound "audio/voice/agent/goingInGunsBlazing.mp3"
        if randAudio == 3:
            play sound "audio/voice/agent/locknload.mp3"
        "Agents" "Go! Go! Go!"
        scene black with fade
        pause 0.3
        $ HQLevelStatus = 3
        show bgHQ:
            xalign 0.0 yalign 0.3
        with fade
        $ HQLiberated = 5
        jump task26
    if HQLiberated == 5:
        "Required:\n12 Freed Agents\n1000 Intel."

        menu:
            "Lead the assault" if freedAgents >= 12 and intel >= 1000:
                pass
            "Wait" if True:
                stop music fadeout 2.0
                hide yellow
                hide red
                hide green
                hide agentModel4
                hide agentModel2
                hide agentModel3
                with d3
                call screen HQButtons
        hide HQButtons
        $ intel -= 1000
        $ randAudio = renpy.random.randint(1,3)
        if randAudio == 1:
            play sound "audio/voice/agent/hasAnybodySeenMyFlakJacket.mp3"
        if randAudio == 2:
            play sound "audio/voice/agent/goingInGunsBlazing.mp3"
        if randAudio == 3:
            play sound "audio/voice/agent/locknload.mp3"
        "Agents" "Go! Go! Go!"
        scene black with fade
        pause 0.3
        $ HQLevelStatus = 6
        show bgHQ:
            xalign 0.0 yalign 0.3
        with fade
        $ HQLiberated = 6
        jump task26
    elif True:
        "Unable to launch the next assault."
        call screen HQButtons

label lift:
    if 18 <= task26Stage <= 30:
        y "No shows are giving during the lockdown."
        jump base
    if tod == 2 and task32Stage >= 2:
        if 26 <= task26Stage <= 27:
            y "No shows are being given during the lockdown."
            jump base
        scene bgStripclub with fade
        pause 0.5
        jump club
    elif True:
        scene bgBar with fade
        pause 0.5
        jump club
label quarters:
    if 18 <= task26Stage <= 21:
        jump finaleNightCycle
    menu:
        "{color=#EFD66D}'Let's have sex already'{/color}" if task13Stage == 4:
            jump task13
        "{color=#EFD66D}'Let's have sex already'{/color}" if task13Stage == 2.1 and otActive:
            $ task13Stage = 3
            jump task13
        "{color=#EFD66D}'Let's have sex already'{/color}" if task13Stage == 0 and specialMaggieStatus >= 3 and specialMuffyStatus >= 3 and specialDragonStatus >= 3 and slutLevel >= 3 and task5Stage >= 8:
            jump task13
        "{color=#EFD66D}'A taste of what's to come'{/color}" if task8Stage == 1:
            jump task8
        "{color=#EFD66D}'Dingalingaling'{/color}" if task5Stage == 4 and spy1Status == 0 and spy1Status == 0 and spy3Status == 0:
            jump task5
        "{color=#EFD66D}'Double Trouble'{/color}" if task2Stage == 14:
            jump task2
        "{color=#EFD66D}'Double Trouble'{/color}" if task2Stage == 12 or task2Stage == 12.5:
            $ task2Stage = 12.5
            jump task2
        "{color=#EFD66D}'Retaken the Taken'{/color}" if task26Stage == 4:
            jump task26
        "{color=#EFD66D}'Retaken the Taken'{/color}" if task26Stage == 7:
            jump task26
        "{color=#EFD66D}'Retaken the Taken'{/color}" if 26 <= task26Stage <= 28:
            jump task26
        "{color=#EFD66D}'What about blowjobs?'{/color}" if task27Stage == 0 and task26Stage >= 28:
            jump task27
        "Visit Sam" if spyGreenActive and spy1Status <= 9:
            if cellSamWall != 1:
                jump fixCellDecor
            $ spyRoomRand = renpy.random.randint(1,10)
            show cellSam
            with d3
            jump samCall
        "Visit Clover" if spyRedActive and spy2Status <= 9:
            if cellCloverWall != 1:
                jump fixCellDecor2
            $ spyRoomRand = renpy.random.randint(1,10)
            show cellClover
            with d3
            jump cloverCall
        "Visit Alex" if spyYellowActive and spy3Status <= 9:
            if cellAlexWall != 1:
                jump fixCellDecor3
            show cellAlex
            $ spyRoomRand = renpy.random.randint(1,10)
            with d3
            jump alexCall
        "{color=#EFD66D}Visit prisoners{/color}" if prisonersNew:
            $ prisonersNew = False
            scene bgPrison with fade
            jump prisonersCall
        "Visit prisoners" if prisonersNew == False and task3Stage >= 6 and task26Stage <= 25:
            scene bgPrison with fade
            jump prisonersCall
        "Go to bed" if True:

            if 25 <= task26Stage <= 32:
                jump jobReportFinale2
            if 1 <= playerMilkshakeLvl <= 5:
                jump inspRecipeBook
            elif True:
                jump nightCycle
        "Never mind" if True:
            jump base

label missions:
    scene missionScreenBG
    $ missionScreenCurrentLocation = 5
    call screen missionScreenButtons




default missionScreenFrontlineSelect = 0
default missionScreenSupportSelect = 0
default missionScreenDistractSelect = 0

default missionScreenBackup1Select = 0

default backupSamActive = False
default backupCloverActive = False
default backupAlexActive = False
default backupKimActive = False
default backupBritneyActive = False
default backupAmandaActive = False
default backupErinActive = False

default missionScreenCurrentLocation = 0
default missionAreaCastleActive = False
default missionAreaDatabaseActive = False
default missionAreaWOOHPActive = False
default missionAreaFaireActive = False

default intelCost = 0


screen missionScreenButtons:
    hbox:
        xpos 160 ypos 47
        text _("{size=-1}{color=#f7c64f}Spy 1{/color}{/size}") font "fonts/BigSquareDots.ttf"
    hbox:
        xpos 325 ypos 47
        text _("{size=-1}{color=#f7c64f}Spy 2{/color}{/size}") font "fonts/BigSquareDots.ttf"
    hbox:
        xpos 490 ypos 47
        text _("{size=-1}{color=#f7c64f}Spy 3{/color}{/size}") font "fonts/BigSquareDots.ttf"
    hbox:
        xpos 714 ypos 47
        text _("{size=-1}{color=#f7c64f}Location{/color}{/size}") font "fonts/BigSquareDots.ttf"
    hbox:
        xpos 876 ypos 49
        text _("{size=-3}{color=#f7c64f}Intel cost: [intel]/[intelCost]{/color}{/size}") font "fonts/BigSquareDots.ttf"
    hbox:
        xpos 149 ypos 469
        text _("{size=-1}{color=#f7c64f}Backup{/color}{/size}") font "fonts/BigSquareDots.ttf"
    hbox:
        xpos 722 ypos 475
        text _("{size=-1}{color=#f7c64f}Gadgets{/color}{/size}") font "fonts/BigSquareDots.ttf"
    hbox:
        xalign 0.955 yalign 0.966
        text _("{size=-1}{color=#f7c64f}FINISH >>{/color}{/size}") font "fonts/BigSquareDots.ttf"
    if gadgetJetpack >= 1:
        hbox:
            xalign 0.625 yalign 0.9
            text _("{size=-8}{color=#f7c64f}*Jetpack available{/color}{/size}") font "fonts/BigSquareDots.ttf"


    if missionScreenFrontlineSelect == 1:
        add "gui/missionScreen/missionScreenSamSelect.png" xalign 0.10 yalign 0.22
    if missionScreenSupportSelect == 1:
        add "gui/missionScreen/missionScreenSamSelect.png" xalign 0.25 yalign 0.22
    if missionScreenDistractSelect == 1:
        add "gui/missionScreen/missionScreenSamSelect.png" xalign 0.40 yalign 0.22

    if missionScreenFrontlineSelect == 2:
        add "gui/missionScreen/missionScreenCloverSelect.png" xalign 0.10 yalign 0.22
    if missionScreenSupportSelect == 2:
        add "gui/missionScreen/missionScreenCloverSelect.png" xalign 0.25 yalign 0.22
    if missionScreenDistractSelect == 2:
        add "gui/missionScreen/missionScreenCloverSelect.png" xalign 0.40 yalign 0.22

    if missionScreenFrontlineSelect == 3:
        add "gui/missionScreen/missionScreenAlexSelect.png" xalign 0.10 yalign 0.22
    if missionScreenSupportSelect == 3:
        add "gui/missionScreen/missionScreenAlexSelect.png" xalign 0.25 yalign 0.22
    if missionScreenDistractSelect == 3:
        add "gui/missionScreen/missionScreenAlexSelect.png" xalign 0.40 yalign 0.22


    if missionScreenBackup1Select == 1:
        add "gui/missionScreen/missionScreenKimSelect.png" xalign 0.105 yalign 0.846
    if missionScreenBackup1Select == 2:
        add "gui/missionScreen/missionScreenBritneySelect.png" xalign 0.105 yalign 0.846


    if missionScreenGadget1Select == 1:
        add "gui/missionScreen/gadget1.png" xalign 0.595 yalign 0.841
    if missionScreenGadget1Select == 2:
        add "gui/missionScreen/gadget2.png" xalign 0.595 yalign 0.841
    if missionScreenGadget1Select == 3:
        add "gui/missionScreen/gadget3.png" xalign 0.595 yalign 0.841
    if missionScreenGadget1Select == 4:
        add "gui/missionScreen/gadget4.png" xalign 0.595 yalign 0.841
    if missionScreenGadget1Select == 5:
        add "gui/missionScreen/gadget5.png" xalign 0.595 yalign 0.841


    if missionScreenGadget2Select == 1:
        add "gui/missionScreen/gadget1.png" xalign 0.71 yalign 0.841
    if missionScreenGadget2Select == 2:
        add "gui/missionScreen/gadget2.png" xalign 0.71 yalign 0.841
    if missionScreenGadget2Select == 3:
        add "gui/missionScreen/gadget3.png" xalign 0.71 yalign 0.841
    if missionScreenGadget2Select == 4:
        add "gui/missionScreen/gadget4.png" xalign 0.71 yalign 0.841
    if missionScreenGadget2Select == 5:
        add "gui/missionScreen/gadget5.png" xalign 0.71 yalign 0.841


    if missionScreenGadget3Select == 1:
        add "gui/missionScreen/gadget1.png" xalign 0.82 yalign 0.841
    if missionScreenGadget3Select == 2:
        add "gui/missionScreen/gadget2.png" xalign 0.82 yalign 0.841
    if missionScreenGadget3Select == 3:
        add "gui/missionScreen/gadget3.png" xalign 0.82 yalign 0.841
    if missionScreenGadget3Select == 4:
        add "gui/missionScreen/gadget4.png" xalign 0.82 yalign 0.841
    if missionScreenGadget3Select == 5:
        add "gui/missionScreen/gadget5.png" xalign 0.82 yalign 0.841


    if missionScreenGadget4Select == 1:
        add "gui/missionScreen/gadget1.png" xalign 0.93 yalign 0.841
    if missionScreenGadget4Select == 2:
        add "gui/missionScreen/gadget2.png" xalign 0.93 yalign 0.841
    if missionScreenGadget4Select == 3:
        add "gui/missionScreen/gadget3.png" xalign 0.93 yalign 0.841
    if missionScreenGadget4Select == 4:
        add "gui/missionScreen/gadget4.png" xalign 0.93 yalign 0.841
    if missionScreenGadget4Select == 5:
        add "gui/missionScreen/gadget5.png" xalign 0.93 yalign 0.841


    if missionScreenCurrentLocation == 1:
        add "gui/missionScreen/missionScreenLocationSchool.png" xalign 0.893 yalign 0.22
    elif missionScreenCurrentLocation == 2 and missionAreaCastleActive == True:
        add "gui/missionScreen/missionScreenLocationCastle.png" xalign 0.895 yalign 0.22
    elif missionScreenCurrentLocation == 3 and missionAreaDatabaseActive == True:
        add "gui/missionScreen/missionScreenLocationDatabase.png" xalign 0.895 yalign 0.22
    elif missionScreenCurrentLocation == 4 and missionAreaFaireActive == True:
        add "gui/missionScreen/missionScreenLocationFaire.png" xalign 0.895 yalign 0.22
    elif missionScreenCurrentLocation == 5 and missionAreaWOOHPActive == True:
        add "gui/missionScreen/missionScreenLocationWOOHP.png" xalign 0.895 yalign 0.22
    else:
        add "gui/missionScreen/missionScreenLocationLocked.png" xalign 0.894 yalign 0.22

    vbox xalign 0.9 yalign 0.114:
        imagebutton:
            idle "gui/missionScreen/missionScreenLocationPicker.png"


    if task26Stage != 30:
        vbox xalign 0.94 yalign 0.212:
            imagebutton:
                idle "gui/missionScreen/missionScreenLocationNxt.png"
                hover "gui/missionScreen/missionScreenLocationNxt-hover.png"
                action Jump("missionLocNxt")



        vbox xalign 0.558 yalign 0.212:
            imagebutton:
                idle "gui/missionScreen/missionScreenLocationPrv.png"
                hover "gui/missionScreen/missionScreenLocationPrv-hover.png"
                action Jump("missionLocPrv")





    vbox xpos 850 yalign 0.062:
        imagebutton:
            idle "gui/missionScreen/intelCost.png"


    vbox xalign 0.102 yalign 0.84:
        imagebutton:
            idle "gui/missionScreen/missionScreenBackup.png"
            hover "gui/missionScreen/missionScreenBackup-hover.png"
            action Show("selectBackupMenu")


    vbox xalign 0.10 yalign 0.10:
        imagebutton:
            idle "gui/missionScreen/missionScreenAgent.png"
            hover "gui/missionScreen/missionScreenAgent-hover.png"
            action Show("selectSpyFrontlineMenu")


    vbox xalign 0.25 yalign 0.10:
        imagebutton:
            idle "gui/missionScreen/missionScreenAgent.png"
            hover "gui/missionScreen/missionScreenAgent-hover.png"
            action Show("selectSpySupportMenu")


    vbox xalign 0.40 yalign 0.10:
        imagebutton:
            idle "gui/missionScreen/missionScreenAgent.png"
            hover "gui/missionScreen/missionScreenAgent-hover.png"
            action Show("selectSpyDistractMenu")


    vbox xalign 0.62 yalign 0.68:
        imagebutton:
            idle "gui/missionScreen/gadgetTitleBox.png"
    vbox xalign 0.595 yalign 0.84:
        imagebutton:
            idle "gui/missionScreen/missionScreenGadget.png"
            hover "gui/missionScreen/missionScreenGadget-hover.png"
            action Show("selectGadget1Menu")
    vbox xalign 0.709 yalign 0.84:
        imagebutton:
            idle "gui/missionScreen/missionScreenGadget.png"
            hover "gui/missionScreen/missionScreenGadget-hover.png"
            action Show("selectGadget2Menu")
    vbox xalign 0.819 yalign 0.84:
        imagebutton:
            idle "gui/missionScreen/missionScreenGadget.png"
            hover "gui/missionScreen/missionScreenGadget-hover.png"
            action Show("selectGadget3Menu")
    vbox xalign 0.929 yalign 0.84:
        imagebutton:
            idle "gui/missionScreen/missionScreenGadget.png"
            hover "gui/missionScreen/missionScreenGadget-hover.png"
            action Show("selectGadget4Menu")


    vbox xalign 0.985 yalign 0.99:
        imagebutton:
            idle "gui/missionScreen/missionScreenBegin.png"
            hover "gui/missionScreen/missionScreenBegin-hover.png"
            action Jump("missionScreenFinish")


    if task26Stage != 30:
        vbox xalign 0.99 yalign 0.02:
            imagebutton:
                idle "gui/missionScreen/exitButton2.png"
                hover "gui/missionScreen/exitButton2-hover.png"
                if task26Stage == 23 or task26Stage == 25:
                    action Jump("missions")
                if tod == 1:
                    action Jump("worldmap")
                if tod == 2:
                    action Jump("missions")

label missionLocNxt:
    $ missionScreenCurrentLocation += 1

    if missionScreenCurrentLocation == 1:
        $ intelCost = 100
    elif missionScreenCurrentLocation == 2:
        $ intelCost = 200
    elif missionScreenCurrentLocation == 3:
        $ intelCost = 200
    elif missionScreenCurrentLocation == 4:
        $ intelCost = 200
    if missionScreenCurrentLocation >= 6:
        $ intelCost = 100
        $ missionScreenCurrentLocation = 1
    if missionScreenCurrentLocation == 5:
        $ intelCost = 0
    call screen missionScreenButtons

label missionLocPrv:
    $ missionScreenCurrentLocation -= 1

    if missionScreenCurrentLocation == 1:
        $ intelCost = 100
    elif missionScreenCurrentLocation == 2:
        $ intelCost = 200
    elif missionScreenCurrentLocation == 3:
        $ intelCost = 200
    elif missionScreenCurrentLocation == 4:
        $ intelCost = 200
    if missionScreenCurrentLocation <= 0:
        $ intelCost = 0
        $ missionScreenCurrentLocation = 5
    if missionScreenCurrentLocation == 5:
        $ intelCost = 0
    call screen missionScreenButtons




screen selectSpyFrontlineMenu():
    modal True


    vbox xalign 0.53 yalign 0.1:
        imagebutton:
            idle "gui/missionScreen/gadgetExit.png"
            hover "gui/missionScreen/gadgetExit.png"
            action Hide("selectSpyFrontlineMenu")

    if spyGreenActive == True and samHealth != 1 and spy1Status == 0:
        vbox xalign 0.18 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenSamSelect.png"
                hover "gui/missionScreen/missionScreenSamSelect-hover.png"
                if missionScreenSupportSelect == 1:
                    action SetVariable("missionScreenFrontlineSelect", 1), SetVariable("missionScreenSupportSelect", 0), Hide("selectSpyFrontlineMenu")
                elif missionScreenDistractSelect == 1:
                    action SetVariable("missionScreenFrontlineSelect", 1), SetVariable("missionScreenDistractSelect", 0), Hide("selectSpyFrontlineMenu")
                else:
                    action SetVariable("missionScreenFrontlineSelect", 1), Hide("selectSpyFrontlineMenu")
    else:
        vbox xalign 0.18 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"

    if spyRedActive == True and cloverHealth != 1 and spy2Status == 0:
        vbox xalign 0.324 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenCloverSelect.png"
                hover "gui/missionScreen/missionScreenCloverSelect-hover.png"
                if missionScreenSupportSelect == 2:
                    action SetVariable("missionScreenFrontlineSelect", 2), SetVariable("missionScreenSupportSelect", 0), Hide("selectSpyFrontlineMenu")
                elif missionScreenDistractSelect == 2:
                    action SetVariable("missionScreenFrontlineSelect", 2), SetVariable("missionScreenDistractSelect", 0), Hide("selectSpyFrontlineMenu")
                else:
                    action SetVariable("missionScreenFrontlineSelect", 2), Hide("selectSpyFrontlineMenu")
    else:
        vbox xalign 0.324 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"

    if spyYellowActive == True and alexHealth != 1 and spy3Status == 0:
        vbox xalign 0.464 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenAlexSelect.png"
                hover "gui/missionScreen/missionScreenAlexSelect-hover.png"
                if missionScreenSupportSelect == 3:
                    action SetVariable("missionScreenFrontlineSelect", 3), SetVariable("missionScreenSupportSelect", 0), Hide("selectSpyFrontlineMenu")
                elif missionScreenDistractSelect == 3:
                    action SetVariable("missionScreenFrontlineSelect", 3), SetVariable("missionScreenDistractSelect", 0), Hide("selectSpyFrontlineMenu")
                else:
                    action SetVariable("missionScreenFrontlineSelect", 3), Hide("selectSpyFrontlineMenu")
    else:
        vbox xalign 0.464 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"


screen selectSpySupportMenu():
    modal True


    vbox xalign 0.53 yalign 0.1:
        imagebutton:
            idle "gui/missionScreen/gadgetExit.png"
            hover "gui/missionScreen/gadgetExit.png"
            action Hide("selectSpySupportMenu")

    if spyGreenActive == True and samHealth != 1 and spy1Status == 0:
        vbox xalign 0.28 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenSamSelect.png"
                hover "gui/missionScreen/missionScreenSamSelect-hover.png"
                if missionScreenFrontlineSelect == 1:
                    action SetVariable("missionScreenSupportSelect", 1), SetVariable("missionScreenFrontlineSelect", 0), Hide("selectSpySupportMenu")
                elif missionScreenDistractSelect == 1:
                    action SetVariable("missionScreenSupportSelect", 1), SetVariable("missionScreenDistractSelect", 0), Hide("selectSpySupportMenu")
                else:
                    action SetVariable("missionScreenSupportSelect", 1), Hide("selectSpySupportMenu")
    else:
        vbox xalign 0.28 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"
    if spyRedActive == True and cloverHealth != 1 and spy2Status == 0:
        vbox xalign 0.422 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenCloverSelect.png"
                hover "gui/missionScreen/missionScreenCloverSelect-hover.png"
                if missionScreenFrontlineSelect == 2:
                    action SetVariable("missionScreenSupportSelect", 2), SetVariable("missionScreenFrontlineSelect", 0), Hide("selectSpySupportMenu")
                elif missionScreenDistractSelect == 2:
                    action SetVariable("missionScreenSupportSelect", 2), SetVariable("missionScreenDistractSelect", 0), Hide("selectSpySupportMenu")
                else:
                    action SetVariable("missionScreenSupportSelect", 2), Hide("selectSpySupportMenu")
    else:
        vbox xalign 0.422 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"

    if spyYellowActive == True and alexHealth != 1 and spy3Status == 0:
        vbox xalign 0.56 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenAlexSelect.png"
                hover "gui/missionScreen/missionScreenAlexSelect-hover.png"
                if missionScreenFrontlineSelect == 3:
                    action SetVariable("missionScreenSupportSelect", 3), SetVariable("missionScreenFrontlineSelect", 0), Hide("selectSpySupportMenu")
                elif missionScreenDistractSelect == 3:
                    action SetVariable("missionScreenSupportSelect", 3), SetVariable("missionScreenDistractSelect", 0), Hide("selectSpySupportMenu")
                else:
                    action SetVariable("missionScreenSupportSelect", 3), Hide("selectSpySupportMenu")
    else:
        vbox xalign 0.56 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"



screen selectSpyDistractMenu():
    modal True


    vbox xalign 0.53 yalign 0.1:
        imagebutton:
            idle "gui/missionScreen/gadgetExit.png"
            hover "gui/missionScreen/gadgetExit.png"
            action Hide("selectSpyDistractMenu")

    if spyGreenActive == True and samHealth != 1 and spy1Status == 0:
        vbox xalign 0.48 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenSamSelect.png"
                hover "gui/missionScreen/missionScreenSamSelect-hover.png"
                if missionScreenFrontlineSelect == 1:
                    action SetVariable("missionScreenDistractSelect", 1), SetVariable("missionScreenFrontlineSelect", 0), Hide("selectSpyDistractMenu")
                elif missionScreenSupportSelect == 1:
                    action SetVariable("missionScreenDistractSelect", 1), SetVariable("missionScreenSupportSelect", 0), Hide("selectSpyDistractMenu")
                else:
                    action SetVariable("missionScreenDistractSelect", 1), Hide("selectSpyDistractMenu")
    else:
        vbox xalign 0.48 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"
    if spyRedActive == True and cloverHealth != 1 and spy2Status == 0:
        vbox xalign 0.62 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenCloverSelect.png"
                hover "gui/missionScreen/missionScreenCloverSelect-hover.png"
                if missionScreenFrontlineSelect == 2:
                    action SetVariable("missionScreenDistractSelect", 2), SetVariable("missionScreenFrontlineSelect", 0), Hide("selectSpyDistractMenu")
                elif missionScreenSupportSelect == 2:
                    action SetVariable("missionScreenDistractSelect", 2), SetVariable("missionScreenSupportSelect", 0), Hide("selectSpyDistractMenu")
                else:
                    action SetVariable("missionScreenDistractSelect", 2), Hide("selectSpyDistractMenu")
    else:
        vbox xalign 0.62 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"
    if spyYellowActive == True and alexHealth != 1 and spy3Status == 0:
        vbox xalign 0.757 yalign 0.25:
            imagebutton:
                idle "gui/missionScreen/missionScreenAlexSelect.png"
                hover "gui/missionScreen/missionScreenAlexSelect-hover.png"
                if missionScreenFrontlineSelect == 3:
                    action SetVariable("missionScreenDistractSelect", 3), SetVariable("missionScreenFrontlineSelect", 0), Hide("selectSpyDistractMenu")
                elif missionScreenSupportSelect == 3:
                    action SetVariable("missionScreenDistractSelect", 3), SetVariable("missionScreenSupportSelect", 0), Hide("selectSpyDistractMenu")
                else:
                    action SetVariable("missionScreenDistractSelect", 3), Hide("selectSpyDistractMenu")
    else:
        vbox xalign 0.757 yalign 0.34:
            imagebutton:
                idle "gui/missionScreen/missionScreenSpyLocked.png"






screen selectLocationMenu:
    modal True
    if backupKimActive == True:
        vbox xalign 0.90 yalign 0.10:
            imagebutton:
                idle "gui/missionScreen/missionScreenKimSelect.png"
                hover "gui/missionScreen/missionScreenKimSelect-hover.png"
                action SetVariable("missionScreenBackup1Select", 1), Hide("selectBackupMenu")
    if backupBritneyActive == True:
        vbox xalign 0.90 yalign 0.10:
            imagebutton:
                idle "gui/missionScreen/missionScreenBritneySelect.png"
                hover "gui/missionScreen/missionScreenBritneySelect-hover.png"
                action SetVariable("missionScreenBackup1Select", 2), Hide("selectBackupMenu")



screen selectBackupMenu():
    modal True
    if backupKimActive == True:
        vbox xalign 0.18 yalign 0.90:
            imagebutton:
                idle "gui/missionScreen/missionScreenKimSelect.png"
                hover "gui/missionScreen/missionScreenKimSelect-hover.png"
                action SetVariable("missionScreenBackup1Select", 1), Hide("selectBackupMenu")
    else:
        vbox xalign 0.18 yalign 0.90:
            imagebutton:
                idle "gui/missionScreen/missionScreenBackupLocked.png"
                action Hide("selectBackupMenu")

    if backupBritneyActive == True:
        vbox xalign 0.323 yalign 0.90:
            imagebutton:
                idle "gui/missionScreen/missionScreenBritneySelect.png"
                hover "gui/missionScreen/missionScreenBritneySelect-hover.png"
                action SetVariable("missionScreenBackup1Select", 2), Hide("selectBackupMenu")
    else:
        vbox xalign 0.323 yalign 0.90:
            imagebutton:
                idle "gui/missionScreen/missionScreenBackupLocked.png"
                action Hide("selectBackupMenu")

    if backupErinActive == True:
        vbox xalign 0.464 yalign 0.90:
            imagebutton:
                idle "gui/missionScreen/missionScreenErinSelect.png"
                hover "gui/missionScreen/missionScreenErinSelect-hover.png"
                action SetVariable("missionScreenBackup1Select", 3), Hide("selectBackupMenu")
    else:
        vbox xalign 0.464 yalign 0.90:
            imagebutton:
                idle "gui/missionScreen/missionScreenBackupLocked.png"
                action Hide("selectBackupMenu")


default missionScreenGadget1Select = 0
default missionScreenGadget2Select = 0
default missionScreenGadget3Select = 0
default missionScreenGadget4Select = 0
default missionScreenGadget5Select = 0
default missionScreenGadget6Select = 0
default missionScreenGadget7Select = 0
default missionScreenGadget8Select = 0

screen selectGadget1Menu:
    add "gui/missionScreen/gadgetBG.png" xalign 0.89 yalign 0.80
    modal True
    if gadgetEarrings >= 1 and missionScreenGadget2Select != 1 and missionScreenGadget3Select != 1 and missionScreenGadget4Select != 1:
        vbox xalign 0.63 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget1.png"
                hover "gui/missionScreen/gadget1-hover.png"
                action SetVariable("missionScreenGadget1Select", 1), Hide("selectGadget1Menu")
    if gadgetPowder >= 1 and missionScreenGadget2Select != 2 and missionScreenGadget3Select != 2 and missionScreenGadget4Select != 2:
        vbox xalign 0.73 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget2.png"
                hover "gui/missionScreen/gadget2-hover.png"
                action SetVariable("missionScreenGadget1Select", 2), Hide("selectGadget1Menu")
    if gadgetFlashbangBelt >= 1 and missionScreenGadget2Select != 3 and missionScreenGadget3Select != 3 and missionScreenGadget4Select != 3:
        vbox xalign 0.83 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget3.png"
                hover "gui/missionScreen/gadget3-hover.png"
                action SetVariable("missionScreenGadget1Select", 3), Hide("selectGadget1Menu")
    if gadgetDrone >= 1 and missionScreenGadget2Select != 4 and missionScreenGadget3Select != 4 and missionScreenGadget4Select != 4:
        vbox xalign 0.927 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget4.png"
                hover "gui/missionScreen/gadget4-hover.png"
                action SetVariable("missionScreenGadget1Select", 4), Hide("selectGadget1Menu")
    if gadgetStealth >= 1 and missionScreenGadget2Select != 5 and missionScreenGadget3Select != 5 and missionScreenGadget4Select != 5:
        vbox xalign 0.63 yalign 0.995:
            imagebutton:
                idle "gui/missionScreen/gadget5.png"
                hover "gui/missionScreen/gadget5-hover.png"
                action SetVariable("missionScreenGadget1Select", 5), Hide("selectGadget1Menu")
    vbox xalign 0.53 yalign 0.70:
        imagebutton:
            idle "gui/missionScreen/gadgetExit.png"
            hover "gui/missionScreen/gadgetExit.png"
            action Hide("selectGadget1Menu")

screen selectGadget2Menu:
    add "gui/missionScreen/gadgetBG.png" xalign 0.89 yalign 0.80
    modal True
    if gadgetEarrings >= 1 and missionScreenGadget1Select != 1 and missionScreenGadget3Select != 1 and missionScreenGadget4Select != 1:
        vbox xalign 0.63 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget1.png"
                hover "gui/missionScreen/gadget1-hover.png"
                action SetVariable("missionScreenGadget2Select", 1), Hide("selectGadget2Menu")
    if gadgetPowder >= 1 and missionScreenGadget1Select != 2 and missionScreenGadget3Select != 2 and missionScreenGadget4Select != 2:
        vbox xalign 0.73 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget2.png"
                hover "gui/missionScreen/gadget2-hover.png"
                action SetVariable("missionScreenGadget2Select", 2), Hide("selectGadget2Menu")
    if gadgetFlashbangBelt >= 1 and missionScreenGadget1Select != 3 and missionScreenGadget3Select != 3 and missionScreenGadget4Select != 3:
        vbox xalign 0.83 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget3.png"
                hover "gui/missionScreen/gadget3-hover.png"
                action SetVariable("missionScreenGadget2Select", 3), Hide("selectGadget2Menu")
    if gadgetDrone >= 1 and missionScreenGadget2Select != 4 and missionScreenGadget3Select != 4 and missionScreenGadget4Select != 4:
        vbox xalign 0.927 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget4.png"
                hover "gui/missionScreen/gadget4-hover.png"
                action SetVariable("missionScreenGadget2Select", 4), Hide("selectGadget2Menu")
    if gadgetStealth >= 1 and missionScreenGadget1Select != 5 and missionScreenGadget3Select != 5 and missionScreenGadget4Select != 5:
        vbox xalign 0.63 yalign 0.995:
            imagebutton:
                idle "gui/missionScreen/gadget5.png"
                hover "gui/missionScreen/gadget5-hover.png"
                action SetVariable("missionScreenGadget2Select", 5), Hide("selectGadget2Menu")
    vbox xalign 0.53 yalign 0.70:
        imagebutton:
            idle "gui/missionScreen/gadgetExit.png"
            hover "gui/missionScreen/gadgetExit.png"
            action Hide("selectGadget2Menu")

screen selectGadget3Menu:
    add "gui/missionScreen/gadgetBG.png" xalign 0.89 yalign 0.80
    modal True
    if gadgetEarrings >= 1 and missionScreenGadget1Select != 1 and missionScreenGadget2Select != 1 and missionScreenGadget4Select != 1:
        vbox xalign 0.63 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget1.png"
                hover "gui/missionScreen/gadget1-hover.png"
                action SetVariable("missionScreenGadget3Select", 1), Hide("selectGadget3Menu")
    if gadgetPowder >= 1 and missionScreenGadget1Select != 2 and missionScreenGadget2Select != 2 and missionScreenGadget4Select != 2:
        vbox xalign 0.73 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget2.png"
                hover "gui/missionScreen/gadget2-hover.png"
                action SetVariable("missionScreenGadget3Select", 2), Hide("selectGadget3Menu")
    if gadgetFlashbangBelt >= 1 and missionScreenGadget2Select != 3 and missionScreenGadget1Select != 3 and missionScreenGadget4Select != 3:
        vbox xalign 0.83 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget3.png"
                hover "gui/missionScreen/gadget3-hover.png"
                action SetVariable("missionScreenGadget3Select", 3), Hide("selectGadget3Menu")
    if gadgetDrone >= 1 and missionScreenGadget2Select != 4 and missionScreenGadget3Select != 4 and missionScreenGadget4Select != 4:
        vbox xalign 0.927 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget4.png"
                hover "gui/missionScreen/gadget4-hover.png"
                action SetVariable("missionScreenGadget3Select", 4), Hide("selectGadget3Menu")
    if gadgetStealth >= 1 and missionScreenGadget2Select != 5 and missionScreenGadget1Select != 5 and missionScreenGadget4Select != 5:
        vbox xalign 0.63 yalign 0.995:
            imagebutton:
                idle "gui/missionScreen/gadget5.png"
                hover "gui/missionScreen/gadget5-hover.png"
                action SetVariable("missionScreenGadget3Select", 5), Hide("selectGadget3Menu")
    vbox xalign 0.53 yalign 0.70:
        imagebutton:
            idle "gui/missionScreen/gadgetExit.png"
            hover "gui/missionScreen/gadgetExit.png"
            action Hide("selectGadget3Menu")

screen selectGadget4Menu:
    add "gui/missionScreen/gadgetBG.png" xalign 0.89 yalign 0.80
    modal True
    if gadgetEarrings >= 1 and missionScreenGadget1Select != 1 and missionScreenGadget2Select != 1 and missionScreenGadget3Select != 1:
        vbox xalign 0.63 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget1.png"
                hover "gui/missionScreen/gadget1-hover.png"
                action SetVariable("missionScreenGadget4Select", 1), Hide("selectGadget4Menu")
    if gadgetPowder >= 1 and missionScreenGadget1Select != 2 and missionScreenGadget2Select != 2 and missionScreenGadget3Select != 2:
        vbox xalign 0.73 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget2.png"
                hover "gui/missionScreen/gadget2-hover.png"
                action SetVariable("missionScreenGadget4Select", 2), Hide("selectGadget4Menu")
    if gadgetFlashbangBelt >= 1 and missionScreenGadget2Select != 3 and missionScreenGadget3Select != 3 and missionScreenGadget1Select != 3:
        vbox xalign 0.83 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget3.png"
                hover "gui/missionScreen/gadget3-hover.png"
                action SetVariable("missionScreenGadget4Select", 3), Hide("selectGadget4Menu")
    if gadgetDrone >= 1 and missionScreenGadget2Select != 4 and missionScreenGadget3Select != 4 and missionScreenGadget4Select != 4:
        vbox xalign 0.927 yalign 0.80:
            imagebutton:
                idle "gui/missionScreen/gadget4.png"
                hover "gui/missionScreen/gadget4-hover.png"
                action SetVariable("missionScreenGadget4Select", 4), Hide("selectGadget4Menu")
    if gadgetStealth >= 1 and missionScreenGadget2Select != 5 and missionScreenGadget3Select != 5 and missionScreenGadget1Select != 5:
        vbox xalign 0.63 yalign 0.995:
            imagebutton:
                idle "gui/missionScreen/gadget5.png"
                hover "gui/missionScreen/gadget5-hover.png"
                action SetVariable("missionScreenGadget4Select", 5), Hide("selectGadget4Menu")
    vbox xalign 0.53 yalign 0.70:
        imagebutton:
            idle "gui/missionScreen/gadgetExit.png"
            hover "gui/missionScreen/gadgetExit.png"
            action Hide("selectGadget4Menu")

label resetVarMis:
    if samHealth == 1 and cloverHealth == 1 and alexHealth == 1:
        "All your spies are badly injured. Heal them up with some medkits."
        jump worldmap
    if tutStage <= 7:
        y "Best not mess around with this right now."
        jump worldmap
    if task2Stage == 0:
        y "I don't really have a reason to set up a new mission right now."
        jump worldmap
    $ missionScreenGadget1Select = 0
    $ missionScreenGadget2Select = 0
    $ missionScreenGadget3Select = 0
    $ missionScreenGadget4Select = 0
    $ missionScreenBackup1Select = 0
    $ missionScreenBackup2Select = 0
    $ missionScreenBackup3Select = 0
    $ missionScreenFrontlineSelect = 0
    $ missionScreenSupportSelect = 0
    $ missionScreenDistractSelect = 0
    jump missions


default dailyMagAgent = False

label prison:
    if task3Stage >= 8:
        "You have captured [capturedAgents] agents and have [freedAgents] freed agents."
        menu:
            "Throw down dirty mags" if magazine >= 1:
                if capturedAgents <= 0:
                    "There are no agents that need to be broken free from nanobot control."
                    jump base
                elif True:
                    if capturedAgents >= 1:
                        $ capturedAgents -= 1
                        $ freedAgents += 1
                    $ magazine -= 1
                    $ randAgentDia = renpy.random.randint(1, 4)
                    if randAgentDia == 1:
                        play sound "audio/voice/agent/daylightStingsMyEyes.mp3"
                        "Agent" "Daylight stings my eyes!"
                    if randAgentDia == 2:
                        play sound "audio/voice/agent/iReadItForTheArticles.mp3"
                        "Agent" "I read it for the articles!"
                    if randAgentDia == 3:
                        play sound "audio/voice/agent/aToiletWouldBeNice.mp3"
                        "Agent" "A toilet down here would be nice!"
                    if randAgentDia == 4:
                        play sound "audio/voice/agent/iHopeMyWifeDoesntFindOut.mp3"
                        "Agent" "I hope my wife doesn't find out!"
                    jump prison
            "Back" if True:
                jump base
    elif True:
        "Just an underground room."
    jump base
label spyCamera:
    if 18 <= task26Stage <= 22:
        y "No one to spy on."
        jump base
    "Who do you wish to spy on?"
    menu:
        "Sam" if spyGreenActive and spy1Status == 0:
            jump spyCameraGreen
        "Clover" if spyRedActive and spy2Status == 0:
            jump spyCameraRed
        "Alex" if spyYellowActive and spy3Status == 0:
            jump spyCameraYellow



default deskToolsActive = 0
image basedesk = "bgs/base/basedesk.jpg"












default vibPart1 = 0
default vibPart2 = 0
default vibPart3 = 0

screen equip1VIB:
    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/exitButton.png"
            hover "gui/exitButton-hover.png"
            if tod == 1:
                action Hide("gadgetButtons"), Jump("worldmap")
            if tod == 2 or tutStage == 4:
                action Hide("gadgetButtons"), Jump("base")

    if vibPart1:
        add "gui/gadgets/equipment/vibStatus0Done.png" xalign 0.694 ypos 0.206
    if vibPart2:
        add "gui/gadgets/equipment/vibStatus1Done.png" xalign 0.621 ypos 0.318
    if vibPart3:
        add "gui/gadgets/equipment/vibStatus2Done.png" xalign 0.25 ypos 0.025

    if vibPart1 == 0:
        vbox xalign 0.694 ypos 0.20:
            imagebutton:
                idle "gui/gadgets/equipment/vibStatus0.png"
                hover "gui/gadgets/equipment/vibStatus0-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("vibPart1", 1), Jump("buildVIB")

    if vibPart2 == 0 and vibPart1 == 1:
        vbox xalign 0.621 ypos 0.30:
            imagebutton:
                idle "gui/gadgets/equipment/vibStatus1.png"
                hover "gui/gadgets/equipment/vibStatus1-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("vibPart2",  1), Jump("buildVIB")

    if vibPart3 == 0:
        vbox xalign 0.25 ypos 0.025:
            imagebutton:
                idle "gui/gadgets/equipment/vibStatus2.png"
                hover "gui/gadgets/equipment/vibStatus2-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("vibPart3",  1), Jump("buildVIB")
    if vibPart1 == 1 and vibPart2 == 1 and vibPart3 == 1:
        $ task2Stage = 13

default hackPart = 0
image hackGraph = "gui/gadgets/equipment/hackComplete.png"

screen equip2Hack:
    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/exitButton.png"
            hover "gui/exitButton-hover.png"
            if tod == 1:
                action Hide("gadgetButtons"), Jump("worldmap")
            if tod == 2 or tutStage == 4:
                action Hide("gadgetButtons"), Jump("base")

    if hackPart >= 1:
        add "gui/gadgets/equipment/hackStatus0Done.png" xalign 0.5
    if hackPart >= 2:
        add "gui/gadgets/equipment/hackStatus1Done.png" xalign 0.5
    if hackPart >= 3:
        add "gui/gadgets/equipment/hackStatus2Done.png" xalign 0.5

    if hackPart == 0:
        vbox xalign 0.5 yalign 0.0:
            imagebutton:
                idle "gui/gadgets/equipment/hackStatus0.png"
                hover "gui/gadgets/equipment/hackStatus0Done.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("hackPart", 1), Jump("buildHack")
    if hackPart == 1:
        vbox xalign 0.5 yalign 0.0:
            imagebutton:
                idle "gui/gadgets/equipment/hackStatus1.png"
                hover "gui/gadgets/equipment/hackStatus1Done.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("hackPart", 2), Jump("buildHack")
    if hackPart == 2:
        vbox xalign 0.5 yalign 0.0:
            imagebutton:
                idle "gui/gadgets/equipment/hackStatus2.png"
                hover "gui/gadgets/equipment/hackStatus2Done.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("hackPart", 3), Jump("buildHack")



default glassesPart = 0
image glassesGraph = "gui/gadgets/equipment/glass3-hover.png"

screen equip3Glasses:
    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/exitButton.png"
            hover "gui/exitButton-hover.png"
            if tod == 1:
                action Hide("gadgetButtons"), Jump("worldmap")
            if tod == 2 or tutStage == 4:
                action Hide("gadgetButtons"), Jump("base")

    if glassesPart >= 1:
        add "gui/gadgets/equipment/glass1-hover.png" xalign 0.5
    if glassesPart >= 2:
        add "gui/gadgets/equipment/glass2-hover.png" xalign 0.5
    if glassesPart >= 3:
        add "gui/gadgets/equipment/glass3-hover.png" xalign 0.5

    if glassesPart == 0:
        vbox xalign 0.5 yalign 0.0:
            imagebutton:
                idle "gui/gadgets/equipment/glass1.png"
                hover "gui/gadgets/equipment/glass1-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("glassesPart", 1), Jump("buildGlasses")
    if glassesPart == 1:
        vbox xalign 0.5 yalign 0.0:
            imagebutton:
                idle "gui/gadgets/equipment/glass2.png"
                hover "gui/gadgets/equipment/glass2-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("glassesPart", 2), Jump("buildGlasses")
    if glassesPart == 2:
        vbox xalign 0.5 yalign 0.0:
            imagebutton:
                idle "gui/gadgets/equipment/glass3.png"
                hover "gui/gadgets/equipment/glass3-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("glassesPart", 3), Jump("buildGlasses")



default gunPart = 0
image gunGraph = "gui/gadgets/equipment/gun3-hover.png"

screen equip4Gun:
    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/exitButton.png"
            hover "gui/exitButton-hover.png"
            if tod == 1:
                action Hide("gadgetButtons"), Jump("worldmap")
            if tod == 2 or tutStage == 4:
                action Hide("gadgetButtons"), Jump("base")

    if gunPart >= 1:
        add "gui/gadgets/equipment/gun1-hover.png" xalign 0.5 yalign 0.5
    if gunPart >= 2:
        add "gui/gadgets/equipment/gun2-hover.png" xalign 0.5 yalign 0.5
    if gunPart >= 3:
        add "gui/gadgets/equipment/gun3-hover.png" xalign 0.5 yalign 0.5

    if gunPart == 0:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/gadgets/equipment/gun1.png"
                hover "gui/gadgets/equipment/gun1-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("gunPart", 1), Jump("buildGun")
    if gunPart == 1:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/gadgets/equipment/gun2.png"
                hover "gui/gadgets/equipment/gun2-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("gunPart", 2), Jump("buildGun")
    if gunPart == 2:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/gadgets/equipment/gun3.png"
                hover "gui/gadgets/equipment/gun3-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("gunPart", 3), Jump("buildGun")




default hookPart = 0
image hookGraph = "gui/gadgets/equipment/hook3-hover.png"

screen equip4Hook:
    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/exitButton.png"
            hover "gui/exitButton-hover.png"
            if tod == 1:
                action Hide("gadgetButtons"), Jump("worldmap")
            if tod == 2 or tutStage == 4:
                action Hide("gadgetButtons"), Jump("base")

    if hookPart >= 1:
        add "gui/gadgets/equipment/hook1-hover.png" xalign 0.5 yalign 0.5
    if hookPart >= 2:
        add "gui/gadgets/equipment/hook2-hover.png" xalign 0.5 yalign 0.5
    if hookPart >= 3:
        add "gui/gadgets/equipment/hook3-hover.png" xalign 0.5 yalign 0.5

    if hookPart == 0:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/gadgets/equipment/hook1.png"
                hover "gui/gadgets/equipment/hook1-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("hookPart", 1), Jump("buildHook")
    if hookPart == 1:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/gadgets/equipment/hook2.png"
                hover "gui/gadgets/equipment/hook2-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("hookPart", 2), Jump("buildHook")
    if hookPart == 2:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/gadgets/equipment/hook3.png"
                hover "gui/gadgets/equipment/hook3-hover.png"
                action Play("sound", "audio/sfx/miscSound1.mp3"), SetVariable("hookPart", 3), Jump("buildHook")



default craftEquip1 = "{color=#0a0a0a}---Protected---{/color}"
default craftEquip2 = "{color=#0a0a0a}---Protected---{/color}"
default craftEquip3 = "{color=#0a0a0a}---Protected---{/color}"
default craftEquip4 = "{color=#0a0a0a}---Protected---{/color}"
default craftEquip5 = "{color=#0a0a0a}---Protected---{/color}"

label desk:
    if tutStage <= 3:
        y "Not right now."
        jump worldmap
    scene basedesk
    menu:
        "Craft Gadgets" if True:
            show screen gadgetButtons
            call screen deskToolsInterface
        "Craft Equipment" if True:
            "Loading WOOHP database...."
            label deskEquipment:
                pass
            menu:
                "{color=#EFD66D}'Double Trouble'{/color}" if task2Stage == 10:
                    jump task2
                "[craftEquip1]" if gadgetVIBActive == False:
                    if craftEquip1 != "V.I.B.":
                        jump deskEquipment
                    elif True:
                        label buildVIB:
                            if vibPart1 == 1 and vibPart2 == 1 and vibPart3 == 1:
                                $ task2Stage = 13
                                jump task2
                            elif True:
                                call screen equip1VIB
                "[craftEquip2]" if gadgetHackActive == False:
                    if craftEquip2 != "Hacking Tool":
                        jump deskEquipment
                    elif True:
                        label buildHack:
                            if hackPart == 3:
                                show hackGraph:
                                    xalign 0.5 yalign 0.0
                                pause 0.3
                                play sound "audio/sfx/itemGot.mp3"
                                "Hacking Device build!"
                                $ gadgetHackActive = True
                                "The hacking device can be used to hack into electronic devices during missions. Unlike gadgets, Equipment (like the V.I.B. and the Hacking Tool) are always available for use."
                                hide hackGraph with d3
                            elif True:
                                call screen equip2Hack
                            if tod == 1:
                                jump worldmap
                            elif True:
                                jump base
                "[craftEquip3]" if gadgetGlassesActive == False:
                    if craftEquip3 != "Cyber Infiltration Glasses":
                        jump deskEquipment
                    elif True:
                        label buildGlasses:
                            if glassesPart == 3:
                                show glassesGraph:
                                    xalign 0.5 yalign 0.0
                                pause 0.3
                                play sound "audio/sfx/itemGot.mp3"
                                "Cyber Infiltration Glasses crafted!"
                                $ gadgetGlassesActive = True
                                "The Cyber Infiltration Glasses. Press {b}3{/b} to turn on during missions and spot hidden messages."
                                hide glassesGraph with d3
                            elif True:
                                call screen equip3Glasses
                            if tod == 1:
                                jump worldmap
                            elif True:
                                jump base
                "[craftEquip4]" if gadgetGunActive == False:
                    if craftEquip4 != "Multitool Revolver":
                        jump deskEquipment
                    elif True:
                        label buildGun:
                            if gunPart == 3:
                                show gunGraph:
                                    xalign 0.5 yalign 0.5
                                pause 0.3
                                play sound "audio/sfx/itemGot.mp3"
                                "Multitool Revolver crafted!"
                                $ gadgetGunActive = True
                                "Press {b}4{/b} to equip during missions and then R to load with darts."
                                hide gunGraph with d3
                            elif True:
                                call screen equip4Gun
                            if tod == 1:
                                jump worldmap
                            elif True:
                                jump base
                "[craftEquip5]" if gadgetHookActive == False:
                    if craftEquip5 != "Grappling Hook":
                        jump deskEquipment
                    elif True:
                        label buildHook:
                            if hookPart == 3:
                                show hookGraph:
                                    xalign 0.5 yalign 0.5
                                pause 0.3
                                play sound "audio/sfx/itemGot.mp3"
                                "Grappling Hook crafted!"
                                $ gadgetHookActive = True
                                "Press {b}5{/b} to equip your grappling hook and bypass obstacles."
                                hide hookGraph with d3
                            elif True:
                                call screen equip4Hook
                            if tod == 1:
                                jump worldmap
                            elif True:
                                jump base
                "Back" if True:
                    jump desk
        "Craft Medicine" if True:

            label engineerHQMed:
                pass
            menu:
                "Sildenafil Pills ([herbAphro]/3 Vigor Leaf)" if True:
                    if herbAphro >= 3:
                        $ herbAphro -= 3
                        $ medPills += 1
                        "You created some {color=#ffeda6}vigor pills{/color} that allow you to keep going and going all thoughout the night!"
                        jump engineerHQMed
                    elif True:
                        y "I don't have enough of these."
                        jump engineerHQMed
                "Whisper Ear Drops ([herbWhisper]/3 Whisper Weed)" if True:
                    if herbWhisper >= 3:
                        $ herbWhisper -= 3
                        play sound "audio/sfx/itemGot.mp3"
                        "You crafted some {color=#ffeda6}Whisper Ear Drops{/color}."
                        play sound "audio/sfx/whispers.mp3"
                        "{b}*Whisper* *Whisper* *Whisper*{/b}"
                        y "....................."
                        $ randEarDrops = renpy.random.randint(1, 3)
                        if randEarDrops == 1:
                            y "How scandalous!"
                        if randEarDrops == 2:
                            y "Oh he did {b}'NOT'{/b} just say that."
                        if randEarDrops == 3:
                            y "That lying floozy!"
                        $ randintel = 50
                        $ intel += 50
                        call missionRewardInt from _call_missionRewardInt_16
                        jump engineerHQMed
                    elif True:
                        y "I don't have enough of these."
                        jump engineerHQMed
                "Medkit ([herbHeal]/3 Apple Seed)" if True:
                    if herbHeal >= 3:
                        $ herbHeal -= 3
                        $ medkit += 1
                        play sound "audio/sfx/itemGot.mp3"
                        "You created a {color=#ffeda6}medkit{/color}. Check your items to use it."
                        jump engineerHQMed
                    elif True:
                        y "I don't have enough of these."
                        jump engineerHQMed
                "Tonic of Youth ([herbGold]/3 Goldthorn)" if True:
                    if herbGold >= 3:
                        $ herbGold -= 3
                        play sound "audio/sfx/itemGot.mp3"
                        "You created a {color=#ffeda6}tonic of eternal youth{/color}! You sell it for a 100 bucks."
                        $ cash += 100
                        $ randMoney = 100
                        call missionRewardMoney from _call_missionRewardMoney_42
                        jump engineerHQMed
                    elif True:
                        y "I don't have enough of these."
                        jump engineerHQMed
                "Nanobot Injector ([herbRebel]/3 Rebel Weed)" if True:
                    if herbRebel >= 3:
                        $ herbRebel -= 3
                        play sound "audio/sfx/itemGot.mp3"
                        "You created a {color=#ffeda6}Nanobot Injector{/color}!"
                        $ injectorSmall += 1
                        call missionRewardItem from _call_missionRewardItem_11
                        jump engineerHQMed
                    elif True:
                        y "I don't have enough of these."
                        jump engineerHQMed
                "Strange Potions ([herbMutant]/1 Strange Vine)" if True:
                    if herbMutant >= 1:
                        $ herbMutant -= 1
                        $ medPotion += 1
                        play sound "audio/sfx/itemGot.mp3"
                        "You got a {color=#ffeda6}Strange Potion{/color}. Visit the advanced section to turn it into medicine."
                        jump engineerHQMed
                    elif True:
                        y "I don't have enough of these."
                        jump engineerHQMed
                "Advanced" if True:
                    menu:
                        "Breast Enhancement Salve ([medPotion]/2 Strange Potions)" if True:
                            if medPotion >= 2:
                                $ medPotion -= 2
                                play sound "audio/sfx/itemGot.mp3"
                                "You got 1 {color=#ffeda6}Breast Enhancing Salve{/color}!"
                                "Who do you wish to use it on?"
                                menu:
                                    "Sam" if True:
                                        $ greenArms = 1
                                        y "Hey [samNick]! Come over here a second...{w} Topless!"
                                        $ greenChest = 0
                                        $ greenUnder = 0
                                        show green g16 at ri with d3
                                        s "Er... I'm here..."
                                        y "Good, let's see if this works~..."
                                        s "H-hey...!"
                                        "You rub the Breast Enhancement salve on Sam's tits."
                                        if samTitSize == 1:
                                            $ samTitSize = 2
                                            show green at ri with d2
                                            s "!!!"
                                            y "(It worked! Her breasts got bigger.)"
                                            hide green with d3
                                            jump engineerHQMed
                                        elif samTitSize == 2:
                                            $ samTitSize = 3
                                            show green at ri with d2
                                            s "!!!"
                                            y "(It worked! Her breasts got bigger.)"
                                            hide green with d3
                                            jump engineerHQMed
                                        elif samTitSize == 3:
                                            "Nothing happened."
                                            y "(Her beasts don't get any bigger than this it seems.)"
                                            hide green with d3
                                            jump engineerHQMed
                                    "Clover" if True:
                                        $ redArms = 1
                                        y "Hey [cloverNick]! Come over here a second...{w} Topless!"
                                        $ redChest = 0
                                        $ redUnder = 0
                                        show red r16 at ri with d3
                                        c "Er... I'm here..."
                                        y "Good, let's see if this works~..."
                                        c "H-hey...!"
                                        "You rub the Breast Enhancement salve on Clover's tits."
                                        if cloverTitSize == 1:
                                            $ cloverTitSize = 2
                                            show red at ri with d2
                                            c "!!!"
                                            y "(It worked! Her breasts got bigger.)"
                                            hide red with d3
                                            jump engineerHQMed
                                        elif cloverTitSize == 2:
                                            $ cloverTitSize = 3
                                            show red at ri with d2
                                            c "!!!"
                                            y "(It worked! Her breasts got bigger.)"
                                            hide red with d3
                                            jump engineerHQMed
                                        elif cloverTitSize == 3:
                                            "Nothing happened."
                                            y "(Her beasts don't get any bigger than this it seems.)"
                                            hide red with d3
                                            jump engineerHQMed
                                    "Alex" if True:
                                        $ yellowArms = 1
                                        y "Hey [alexNick]! Come over here a second...{w} Topless!"
                                        $ yellowChest = 0
                                        $ yellowUnder = 0
                                        show yellow y16 at ri with d3
                                        a "Er... I'm here..."
                                        y "Good, let's see if this works~..."
                                        a "H-hey...!"
                                        "You rub the Breast Enhancement salve on Alex's tits."
                                        if alexTitSize == 1:
                                            $ alexTitSize = 2
                                            show yellow at ri with d2
                                            a "!!!"
                                            y "(It worked! Her breasts got bigger.)"
                                            hide yellow with d3
                                            jump engineerHQMed
                                        elif alexTitSize == 2:
                                            $ alexTitSize = 3
                                            show yellow at ri with d2
                                            a "!!!"
                                            y "(It worked! Her breasts got bigger.)"
                                            hide yellow with d3
                                            jump engineerHQMed
                                        elif alexTitSize == 3:
                                            "Nothing happened."
                                            y "(Her beasts don't get any bigger than this it seems.)"
                                            hide yellow with d3
                                            jump engineerHQMed
                            elif True:
                                "I don't have enough to make this."
                                jump engineerHQMed
                        "Breast Reduction Salve ([medPotion]/2 Strange Potions)" if True:

                            if medPotion >= 2:
                                $ medPotion -= 2
                                play sound "audio/sfx/itemGot.mp3"
                                "You got 1 {color=#ffeda6}Breast Reduction Salve{/color}!"
                                "Who do you wish to use it on?"
                                menu:
                                    "Sam" if True:
                                        $ greenArms = 1
                                        y "Hey [samNick]! Come over here a second...{w} Topless!"
                                        $ greenChest = 0
                                        $ greenUnder = 0
                                        show green g16 at ri with d3
                                        s "Er... I'm here..."
                                        y "Good, let's see if this works~..."
                                        s "H-hey...!"
                                        "You rub the Breast Reduction salve on Sam's tits."
                                        if samTitSize == 1:
                                            "Nothing happened."
                                            y "(Her beasts don't get any smaller than this it seems.)"
                                            hide green with d3
                                            jump engineerHQMed
                                        elif samTitSize == 2:
                                            hide green with d2
                                            $ samTitSize = 1
                                            show green at ri with d2
                                            s "!!!"
                                            y "(It worked! Her breasts got smaller.)"
                                            hide green with d3
                                            jump engineerHQMed
                                        elif samTitSize == 3:
                                            hide green with d2
                                            $ samTitSize = 2
                                            show green at ri with d2
                                            s "!!!"
                                            y "(It worked! Her breasts got smaller.)"
                                            hide green with d3
                                            jump engineerHQMed
                                    "Clover" if True:
                                        $ redArms = 1
                                        y "Hey [cloverNick]! Come over here a second...{w} Topless!"
                                        $ redChest = 0
                                        $ redUnder = 0
                                        show red r16 at ri with d3
                                        c "Er... I'm here..."
                                        y "Good, let's see if this works~..."
                                        c "H-hey...!"
                                        "You rub the Breast Reduction salve on Clover's tits."
                                        if cloverTitSize == 1:
                                            "Nothing happened."
                                            y "(Her beasts don't get any smaller than this it seems.)"
                                            hide red with d3
                                            jump engineerHQMed
                                        elif cloverTitSize == 2:
                                            hide red with d2
                                            $ cloverTitSize = 1
                                            show red at ri with d2
                                            c "!!!"
                                            y "(It worked! Her breasts got smaller.)"
                                            hide red with d3
                                            jump engineerHQMed
                                        elif cloverTitSize == 3:
                                            hide red with d2
                                            $ cloverTitSize = 2
                                            show red at ri with d2
                                            c "!!!"
                                            y "(It worked! Her breasts got smaller.)"
                                            hide red with d3
                                            jump engineerHQMed
                                    "Alex" if True:
                                        $ yellowArms = 1
                                        y "Hey [alexNick]! Come over here a second...{w} Topless!"
                                        $ yellowChest = 0
                                        $ yellowUnder = 0
                                        show yellow y16 at ri with d3
                                        a "Er... I'm here..."
                                        y "Good, let's see if this works~..."
                                        a "H-hey...!"
                                        "You rub the Breast Reduction salve on Alex's tits."
                                        if alexTitSize == 1:
                                            "Nothing happened."
                                            y "(Her beasts don't get any smaller than this it seems.)"
                                            hide yellow with d3
                                            jump engineerHQMed
                                        elif alexTitSize == 2:
                                            hide yellow with d2
                                            $ alexTitSize = 1
                                            show yellow at ri with d2
                                            a "!!!"
                                            y "(It worked! Her breasts got smaller.)"
                                            hide yellow with d3
                                            jump engineerHQMed
                                        elif alexTitSize == 3:
                                            hide yellow with d2
                                            $ alexTitSize = 2
                                            show yellow at ri with d2
                                            a "!!!"
                                            y "(It worked! Her breasts got smaller.)"
                                            hide yellow with d3
                                            jump engineerHQMed
                            elif True:
                                "I don't have enough to make this."
                                jump engineerHQMed
                        "Back" if True:
                            jump engineerHQMed
                "Back" if True:

                    call greenOutfitSet from _call_greenOutfitSet_5
                    call redOutfitSet from _call_redOutfitSet_4
                    call yellowOutfitSet from _call_yellowOutfitSet_2
                    jump desk

            if tod == 1:
                jump worldmap
            if tod == 2:
                jump base
        "Never mind" if True:

            if tod == 1:
                jump worldmap
            if tod == 2:
                jump base

label finishVIB:
    $ task2Stage = 13
    jump task2




default craftCurrentGadget = 0


default scrapmetal = 2
default blastingPowder = 1
default gel = 0
default wiringKit = 0
default valuables = 1

default matsAcid = 0
default matsChip = 0
default matsDust = 1
default matsGlue = 2
default matsValu = 1
default matsWires = 0


default bugToy = 0


default gadgetVIBActive = False
default gadgetHackActive = False
default gadgetGunActive = False
default gadgetGlassesActive = False
default gadgetHookActive = False


default gadgetEarringsActive = True
default gadgetPowderActive = False
default gadgetAfroDartActive = False
default gadgetStunDartActive = False
default gadgetFlashbangBeltActive = False
default gadgetDroneActive = False
default gadgetShieldActive = False
default gadgetStealthActive = False
default gadgetJetpackActive = False


default gadgetEarrings = 0
default gadgetPowder = 0
default gadgetAfroDart = 0
default gadgetStunDart = 0
default gadgetFlashbangBelt = 0
default gadgetDrone = 0
default gadgetShield = 0
default gadgetStealth = 0
default gadgetJetpack = 0


default flashbangActive = 0

screen gadgetButtons:
    add "gui/gadgets/bgGadgets.png" xalign 0.4 yalign 0.5
    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/exitButton.png"
            hover "gui/exitButton-hover.png"
            if tod == 1:
                action Hide("gadgetButtons"), Jump("worldmap")
            if tod == 2 or tutStage == 4:
                action Hide("gadgetButtons"), Jump("base")

    if gadgetEarringsActive == True:
        vbox xalign 0.10 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetsEarrings.png"
                hover "gui/gadgets/gadgetsEarrings-hover.png" tooltip "ttEarrings"
                action SetVariable("craftCurrentGadget", 1), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttEarrings":
            text _("{color=#000000}{font=fonts/freshmarker.ttf}HYPNO EARRINGS - THROW TO HYPNOTIZE TARGETS. \n1 SALTPETER, 1 VALUABLES, 1 COOLING AGENT{/font}{/color}") xpos 110 ypos 550
            add "gui/gadgets/matsEarrings.jpg" xalign 0.08 yalign 0.06
            text "{size=-4}{color=#000000}[matsDust]/1{/color}{/size}" xpos 130 ypos 80
            text "{size=-4}{color=#000000}[matsValu]/1{/color}{/size}" xpos 220 ypos 80
            text "{size=-4}{color=#000000}[matsGlue]/1{/color}{/size}" xpos 300 ypos 80
    else:
        vbox xalign 0.10 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")

    if gadgetPowderActive == True:
        vbox xalign 0.30 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetsPowder.png"
                hover "gui/gadgets/gadgetsPowder-hover.png" tooltip "ttPowder"
                action SetVariable("craftCurrentGadget", 2), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttPowder":
            text "{color=#000000}{font=fonts/freshmarker.ttf}DISTRACTION BOMB - A SMOKE BOMB THAT CAUSES A DISTRACTION. \n1 WIRE KITS, 1 SALTPETER{/font}{/color}" xpos 110 ypos 550
            add "gui/gadgets/matsPowder.jpg" xalign 0.28 yalign 0.06
            text "{size=-4}{color=#000000}[matsDust]/1{/color}{/size}" xpos 370 ypos 80
            text "{size=-4}{color=#000000}[matsWires]/1{/color}{/size}" xpos 505 ypos 80
    else:
        vbox xalign 0.30 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")

    if gadgetFlashbangBeltActive == True:
        vbox xalign 0.50 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetsBelt.png"
                hover "gui/gadgets/gadgetsBelt-hover.png" tooltip "ttBelt"
                action SetVariable("craftCurrentGadget", 3), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttBelt":
            text _("{color=#000000}{font=fonts/freshmarker.ttf}FLASHBANG BELT - THROW INTO NEXT ROOM TO INCREASE YOUR CHANCES TO BLOCK.\nHYDROFLUORIC ACID, 1 COMPUTER CHIP, 1 WIRING KIT{/font}{/color}") xpos 110 ypos 550
            add "gui/gadgets/matsBelt.jpg" xalign 0.5 yalign 0.06
            text "{size=-4}{color=#000000}[matsAcid]/1{/color}{/size}" xpos 550 ypos 80
            text "{size=-4}{color=#000000}[matsChip]/1{/color}{/size}" xpos 650 ypos 80
            text "{size=-4}{color=#000000}[matsWires]/1{/color}{/size}" xpos 735 ypos 80
    else:
        vbox xalign 0.50 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")

    if gadgetJetpackActive == True:
        vbox xalign 0.70 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetsJetpack.png"
                hover "gui/gadgets/gadgetsJetpack-hover.png" tooltip "ttJetpack"
                action SetVariable("craftCurrentGadget", 9), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttJetpack":
            text _("{color=#000000}{font=fonts/freshmarker.ttf}JETPACK BACKPACK - USE DURING MISSIONS TO SKIP A FEW FLOORS.\n2 SALTPETER, 2 VALUABLES, 2 COOLING AGENTS{/font}{/color}") xpos 110 ypos 550
            add "gui/gadgets/matsEarrings.jpg" xalign 0.72 yalign 0.06
            text "{size=-4}{color=#000000}[matsDust]/2{/color}{/size}" xpos 793 ypos 80
            text "{size=-4}{color=#000000}[matsValu]/2{/color}{/size}" xpos 865 ypos 80
            text "{size=-4}{color=#000000}[matsGlue]/2{/color}{/size}" xpos 950 ypos 80
    else:
        vbox xalign 0.70 yalign 0.20:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")

    if gadgetAfroDartActive == True:
        vbox xalign 0.30 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetsDart1.png"
                hover "gui/gadgets/gadgetsDart1-hover.png" tooltip "ttLove"
                action SetVariable("craftCurrentGadget", 5), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttLove":
            text _("{color=#000000}{font=fonts/freshmarker.ttf}LOVE DART - LOAD REVOLVER WITH A LOVE DART INSTEAD OF KNOCKING AGENTS\nOUT YOU CAN TRY CHARMING THEM. 1 WIRING KIT, 1 ACID{/font}{/color}") xpos 110 ypos 550
            add "gui/gadgets/matsLove.jpg" xalign 0.28 yalign 0.4
            text "{size=-4}{color=#000000}[matsWires]/1{/color}{/size}" xpos 385 ypos 300
            text "{size=-4}{color=#000000}[matsAcid]/1{/color}{/size}" xpos 485 ypos 300
    else:
        vbox xalign 0.30 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")

    if gadgetStunDartActive == True:
        vbox xalign 0.50 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetsDart2.png"
                hover "gui/gadgets/gadgetsDart2-hover.png" tooltip "ttPoison"
                action SetVariable("craftCurrentGadget", 4), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttPoison":
            text _("{color=#000000}{font=fonts/freshmarker.ttf}POISON DART - LOAD REVOLVER WITH A POISON DART, INCREASING YOUR BLOCK CHANCE.\n1 ACID{/font}{/color}") xpos 110 ypos 550
            add "gui/gadgets/matsPoison.jpg" xalign 0.5 yalign 0.4
            text "{size=-4}{color=#000000}[matsAcid]/1{/color}{/size}" xpos 650 ypos 300
    else:
        vbox xalign 0.50 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")

    if gadgetDroneActive == True:
        vbox xalign 0.10 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetsRC.png"
                hover "gui/gadgets/gadgetsRC-hover.png" tooltip "ttDrone"
                action SetVariable("craftCurrentGadget", 6), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttDrone":
            text _("{color=#000000}{font=fonts/freshmarker.ttf}DRONE - BEFORE GOING INTO THE NEXT ROOM, ACTIVATE YOUR DRONE TO SEE\nWHAT'S ON AT THE OTHER SIDE. 1 COOLING AGENT, 1 WIRING KIT, 1 COMPUTER CHIP{/font}{/color}") xpos 110 ypos 550
            add "gui/gadgets/matsDrone.jpg" xalign 0.08 yalign 0.4
            text "{size=-4}{color=#000000}[matsGlue]/1{/color}{/size}" xpos 120 ypos 300
            text "{size=-4}{color=#000000}[matsWires]/1{/color}{/size}" xpos 220 ypos 300
            text "{size=-4}{color=#000000}[matsChip]/1{/color}{/size}" xpos 310 ypos 300
    else:
        vbox xalign 0.10 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")






















    if gadgetStealthActive == True:
        vbox xalign 0.70 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetsBracelet.png"
                hover "gui/gadgets/gadgetsBracelet-hover.png" tooltip "ttStealth"
                action SetVariable("craftCurrentGadget", 8), Jump("craftGadgetLabel")
        $ tooltip = GetTooltip()
        if tooltip == "ttStealth":
            text _("{color=#000000}{font=fonts/freshmarker.ttf}STEALTH BRACELET - USE TO REDUCE DETECTION RATING.\n1 VALUABLES, 1 WIRING KIT, 1 COMPUTER CHIP{/font}{/color}") xpos 110 ypos 550
            add "gui/gadgets/matsStealth.jpg" xalign 0.72 yalign 0.4
            text "{size=-4}{color=#ffeda6}[matsValu]/1{/color}{/size}" xpos 793 ypos 300
            text "{size=-4}{color=#ffeda6}[matsWires]/1{/color}{/size}" xpos 865 ypos 300
            text "{size=-4}{color=#ffeda6}[matsChip]/1{/color}{/size}" xpos 950 ypos 300
    else:
        vbox xalign 0.70 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetLocked.png"
                hover "gui/gadgets/gadgetLocked-hover.png"
                action Jump("gadgetUnavailableMsg")















    if hackerUnlocked:
        vbox xalign 0.90 yalign 0.60:
            imagebutton:
                idle "gui/gadgets/gadgetBuy.png"
                hover "gui/gadgets/gadgetBuy-hover.png"
                action Hide("gadgetButtons"), Jump("hackSkipShop")



label gadgetUnavailableMsg:
    y "This gadget has not yet been unlocked."
    show screen gadgetButtons
    call screen deskToolsInterface

screen deskToolsInterface:
    hbox:
        spacing 10 xalign 0.90 yalign 0.35

    hbox:
        xalign 0.20 yalign 0.36
        text _("[gadgetEarrings]")
    hbox:
        xalign 0.375 yalign 0.36
        text _("[gadgetPowder]")
    hbox:
        xalign 0.55 yalign 0.36
        text _("[gadgetFlashbangBelt]")
    hbox:
        xalign 0.375 yalign 0.68
        text _("[gadgetAfroDart]")
    hbox:
        xalign 0.55 yalign 0.68
        text _("[gadgetStunDart]")
    hbox:
        xalign 0.20 yalign 0.68
        text _("[gadgetDrone]")



    hbox:
        xalign 0.73 yalign 0.68
        text _("[gadgetStealth]")
    hbox:
        xalign 0.73 yalign 0.36
        text _("[gadgetJetpack]")

label craftGadgetLabel:
    hide screen gadgetButtons
    hide screen deskToolsInterface
    if craftCurrentGadget == 1:
        if matsGlue >= 1 and matsDust >= 1 and matsValu >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsGlue -= 1
            $ matsDust -= 1
            $ matsValu -= 1
            $ gadgetEarrings += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        if tutStage == 4:
            jump tutMissionSetup
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 2:
        if matsWires >= 1 and matsDust >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsWires -= 1
            $ matsDust -= 1
            $ gadgetPowder += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 3:
        if matsWires >= 1 and matsChip >= 1 and matsAcid >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsWires -= 1
            $ matsChip -= 1
            $ matsAcid -= 1
            $ gadgetFlashbangBelt += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 4:
        if matsAcid >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsAcid -= 1
            $ gadgetStunDart += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 5:
        if matsAcid >= 1 and matsWires >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsAcid -= 1
            $ matsWires -= 1
            $ gadgetAfroDart += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 6:
        if matsGlue >= 1 and matsWires >= 1 and matsChip >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsGlue -= 1
            $ matsWires -= 1
            $ matsChip -= 1
            $ gadgetDrone += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 7:
        if matsGlue >= 1 and matsWires >= 1 and matsChip >= 1 and matsValu >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsGlue -= 1
            $ matsWires -= 1
            $ matsChip -= 1
            $ matsValu -= 1
            $ gadgetShield += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 8:
        if matsWires >= 1 and matsChip >= 1 and matsValu >= 1:
            play sound "audio/sfx/construction1.mp3"
            $ matsWires -= 1
            $ matsChip -= 1
            $ matsValu -= 1
            $ gadgetStealth += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

    if craftCurrentGadget == 9:
        if matsGlue >= 2 and matsDust >= 2 and matsValu >= 2:
            play sound "audio/sfx/construction1.mp3"
            $ matsGlue -= 2
            $ matsDust -= 2
            $ matsValu -= 2
            $ gadgetJetpack += 1
            play sound "audio/sfx/itemGot.mp3"
        elif True:
            "Not enough materials."
        show screen gadgetButtons
        call screen deskToolsInterface

label deskStatus:
    if tutStage == 2:
        y "(Let's focus on crafting that gadget first.)"
        jump desk
    elif True:
        ""

label Creditcards:
    if tutStage == 2:
        "I should probably craft that gadget and plan a new mission first."
        jump base
    elif True:
        jump creditcards


label prisonHQ:
    menu:
        "View bounties" if True:
            label viewBounties:
                pass
            menu:
                "{color=#EFD66D}Maggie T. (!){/color}" if specialMaggieBounty == True:
                    $ specialMaggieBounty = False
                    "System" "Confirmation: Maggie T. has been captured. Resources alocated to your position."
                    $ randMoney = 1000
                    $ cash += randMoney
                    call missionRewardMoney from _call_missionRewardMoney_56
                    jump viewBounties
                "Maggie T." if specialMaggieStatus == 1:
                    "Maggie T. is currently located at the Aces castle in Valencia.\nReward: $1000."
                    jump viewBounties
                "{color=#EFD66D}Carla Wong (!){/color}" if specialDragonBounty == True:
                    $ specialDragonBounty = False
                    "System" "Confirmation: Carla Wong has been captured. Resources alocated to your position."
                    $ randMoney = 1000
                    $ cash += randMoney
                    call missionRewardMoney from _call_missionRewardMoney_57
                    jump viewBounties
                "Carla Wong" if specialDragonStatus == 1:
                    "Carla Wong is currently located inside the digital world of Drift Punk.\nReward: $1000."
                    jump viewBounties
                "Back" if True:


                    call screen HQButtons

    jump base
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
