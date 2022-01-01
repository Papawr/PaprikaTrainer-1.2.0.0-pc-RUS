default disableScreen = False

screen interactScreenBonus:

    if task12Stage == 3 and missionProgression == 10:
        vbox xalign 0.3 yalign 0.40:
            imagebutton:
                idle "mission/enemy/bg1Tar1.png"
                hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                action Jump("task12")


    if task24Stage == 2 and missionProgression == 8:
        vbox xalign 0.3 yalign 0.40:
            imagebutton:
                idle "mission/enemy/bg1Tar1.png"
                hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                action Jump("task24")


    if task25Stage == 8 and missionProgression == 10:
        vbox xalign 0.63 yalign 0.40:
            imagebutton:
                idle "mission/enemy/bg1Tar1.png"
                hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                action Jump("kandInteract")

screen interactScreen:




    if 1 <= randomBackground <= 3 and currentPosition == 0:


        if randomObst1 != 1 and randomBoss == 0:
            vbox xalign 0.31 yalign 0.48:
                imagebutton:
                    idle "mission/cover/bg1Cover1.png"
                    hover "mission/cover/bg1Cover1-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        if randomObst1 == 1:
            vbox xalign 0.41 yalign 0.32:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 1), Jump("agentInteract")
            $ tooltip = GetTooltip()
            if tooltip:
                text "[CoS1]%" xalign 0.46 yalign 0.32
        if randomBoss >= 1 and missionProgression >= 10:
            vbox xalign 0.52 yalign 0.40:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action Jump("bossInteract")
            $ tooltip = GetTooltip()
            if tooltip:
                text "[randomBossHP] HP" xalign 0.555 yalign 0.39


        if interact1 == 8:
            vbox xalign 0.60 yalign -0.04:
                imagebutton:
                    idle "mission/interact/shoot1.png"
                    hover "mission/interact/shoot1-hover.png"
                    action SetVariable("interSelect", 1), Jump("interInteract")
        if interact2 == 8:
            vbox xalign 0.73 yalign 0.2:
                imagebutton:
                    if interSelect == 2:
                        idle "mission/interact/intercomSemiActive.png"
                    else:
                        idle "mission/interact/intercom.png"
                    hover "mission/interact/intercom-hover.png"
                    action SetVariable("interSelect", 2), Jump("interInteract")
        if randomObst1 == 2:
            vbox xalign 0.15 yalign 0.5:
                imagebutton:
                    if interSelect == 2:
                        idle "mission/interact/intercomSemiActive.png"
                    else:
                        idle "mission/interact/intercom.png"
                    hover "mission/interact/intercom-hover.png"
                    action SetVariable("interSelect", 3), Jump("interInteract")



        if frontExit == 8 and randomObst1 != 1 and missionSetting != "Faire":
            vbox xalign 0.165 yalign 0.43:
                imagebutton:
                    idle "mission/interact/frontExit.png"
                    hover "mission/interact/frontExit-hover.png"
                    action Jump("missionBegin")
        elif frontExit == 8 and randomObst1 != 1 and missionSetting == "Faire":
            vbox xalign 0.18 yalign 0.54:
                imagebutton:
                    idle "mission/interact/frontExit3.png"
                    hover "mission/interact/frontExit3-hover.png"
                    action Jump("missionBegin")


    if 1 <= randomBackground <= 3 and currentPosition == 1:


        if randomObst2 != 1 and currentPosition == 1:
            vbox xalign 0.87 yalign 0.95:
                imagebutton:
                    idle "mission/cover/bg1Cover2.png"
                    hover "mission/cover/bg1Cover2-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        if randomObst2 == 1:
            vbox xalign 0.65 yalign 0.56:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 2), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS2]%" xalign 0.67 yalign 0.53


        if interact2 == 8:
            vbox xalign 0.84 yalign 0.385:
                imagebutton:
                    idle "mission/interact/intercom.png"
                    hover "mission/interact/intercom-hover.png"
                    action SetVariable("interSelect", 2), Jump("interInteract")

        if 1 <= randomLoot <= 2 and randomCover1 == 1 and missionSetting != "School":
            vbox xalign 0.14 yalign 0.42:
                imagebutton:
                    idle "mission/interact/loot.png"
                    hover "mission/interact/loot-hover.png"
                    action Jump("lootItem")


    if 1 <= randomBackground <= 3 and currentPosition == 2:


        if randomExit >= 1:
            vbox xalign 0.65 yalign 0.6:
                imagebutton:
                    idle "mission/interact/bg1Exit1.png"
                    hover "mission/interact/bg1Exit1-hover.png"
                    action Jump("missionBegin")

        if 1 <= randomLoot <= 2 and randomCover2 == 1:
            vbox xalign 0.82 yalign 0.64:
                imagebutton:
                    idle "mission/interact/loot.png"
                    hover "mission/interact/loot-hover.png"
                    action Jump("lootItem")

        if bonusExit == 10 and missionSetting != "Faire":
            vbox xalign 0.18 yalign 0.45:
                imagebutton:
                    idle "mission/interact/bonusExit.png"
                    hover "mission/interact/bonusExit-hover.png"
                    action SetVariable("bonusAvailable", 1), Jump("missionBegin")
        if bonusExit == 10 and missionSetting == "Faire":
            vbox xalign 0.1 yalign 0.6:
                imagebutton:
                    idle "mission/interact/bonusExit.png"
                    hover "mission/interact/bonusExit-hover.png"
                    action SetVariable("bonusAvailable", 1), Jump("missionBegin")























    if 4 <= randomBackground <= 7 and currentPosition == 0 and chanceOfControl <= 89:


        if randomObst1 != 1:
            vbox xalign 0.58 yalign 0.95:
                imagebutton:
                    idle "mission/cover/bg1Cover1.png"
                    hover "mission/cover/bg1Cover1-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        if gadgetHookActive and gadgetActive == 5 and randomExit == 3:
            vbox xalign 0.0 yalign 0.1:
                imagebutton:
                    idle "mission/interact/hook.png"
                    hover "mission/interact/hook-hover.png"
                    action Jump("hookInteract")


        if randomObst1 == 1:
            vbox xalign 0.665 yalign 0.68:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 1), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS1]%" xalign 0.685 yalign 0.63


        if frontExit == 8 and randomObst1 != 1:
            vbox xalign 0.67 yalign 0.73:
                imagebutton:
                    idle "mission/interact/frontExit2.png"
                    hover "mission/interact/frontExit2-hover.png"
                    action Jump("missionBegin")


    if 4 <= randomBackground <= 7 and currentPosition == 1:


        if randomObst2 != 1 and currentPosition == 1:
            vbox xalign 0.33 yalign 0.98:
                imagebutton:
                    idle "mission/cover/bg1Cover1.png"
                    hover "mission/cover/bg1Cover1-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        default tt = Tooltip("No button selected.")
        if randomObst2 == 1:
            vbox xalign 0.07 yalign 0.68:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 2), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS2]%" xalign 0.16 yalign 0.63

        if task13Stage == 2 and missionSetting == "School":
            vbox xalign 0.62 yalign 0.7:
                imagebutton:
                    idle "mission/interact/locker.png"
                    hover "mission/interact/locker-hover.png"
                    action SetVariable("task13Stage", 2.1), Jump("lootSpecial")


    if 4 <= randomBackground <= 7 and currentPosition == 2:


        if randomExit >= 2:
            vbox xalign 0.70 yalign 0.35:
                imagebutton:
                    idle "mission/cover/bg2Cover2.png"
                    hover "mission/cover/bg2Cover2-hover.png"
                    action Jump("coverInteract")


        if 1 <= randomLoot <= 2 and randomCover2 == 1:
            vbox xalign 0.56 yalign 0.8:
                imagebutton:
                    idle "mission/interact/loot.png"
                    hover "mission/interact/loot-hover.png"
                    action Jump("lootItem")


        if currentPosition == 2 and randomExit == 1:
            vbox xalign 0.05 yalign 0.9:
                imagebutton:
                    idle "mission/interact/frontExit2.png"
                    hover "mission/interact/frontExit2-hover.png"
                    action Jump("missionBegin")

        if missionSetting == "School":
            if acesBounty3 == 1 and missionProgression >= 2 and hackFailed == False:
                vbox xpos 0.27 yalign 0.81:
                    imagebutton:
                        if interSelect == 2:
                            idle "mission/interact/intercomSemiActive.png"
                        else:
                            idle "mission/interact/intercom.png"
                        hover "mission/interact/intercom-hover.png"
                        action SetVariable("interSelect", 10), Jump("interInteract")
        if missionSetting == "Castle":
            if acesBounty2 == 1 and missionProgression >= 2 and hackFailed == False:
                vbox xpos 0.27 yalign 0.81:
                    imagebutton:
                        if interSelect == 2:
                            idle "mission/interact/intercomSemiActive.png"
                        else:
                            idle "mission/interact/intercom.png"
                        hover "mission/interact/intercom-hover.png"
                        action SetVariable("interSelect", 10), Jump("interInteract")

        if missionSetting == "Database" and hackFailed == False:
            if acesBounty1 == 1 and missionProgression >= 2:
                vbox xpos 0.27 yalign 0.81:
                    imagebutton:
                        if interSelect == 2:
                            idle "mission/interact/intercomSemiActive.png"
                        else:
                            idle "mission/interact/intercom.png"
                        hover "mission/interact/intercom-hover.png"
                        action SetVariable("interSelect", 10), Jump("interInteract")
        if missionSetting == "Faire":
            pass

        if task15Stage == 1 and missionSetting == "Database" or task15Stage == 1 and missionSetting == "Faire":
            vbox xpos 0.27 yalign 0.81:
                imagebutton:
                    if interSelect == 2:
                        idle "mission/interact/intercomSemiActive.png"
                    else:
                        idle "mission/interact/intercom.png"
                    hover "mission/interact/intercom-hover.png"
                    action SetVariable("interSelect", 10), Jump("interInteract")


    if 4 <= randomBackground <= 7 and currentPosition == 3:


        if randomExit == 3:
            vbox xalign 0.35 yalign 0.40:
                imagebutton:
                    idle "mission/cover/bg2Cover3.png"
                    hover "mission/cover/bg2Cover3-hover.png"
                    action Jump("coverInteract")


        if interact1 == 8:
            vbox xalign 0.75 yalign -0.04:
                imagebutton:
                    idle "mission/interact/shoot1.png"
                    hover "mission/interact/shoot1-hover.png"
                    action SetVariable("interSelect", 1), Jump("interInteract")


        if randomExit == 2:
            vbox xalign 0.95 yalign 0.53:
                imagebutton:
                    idle "mission/interact/frontExit2.png"
                    hover "mission/interact/frontExit2-hover.png"
                    if randomObst3 != 1:
                        action Jump("missionBegin")


        if randomObst3 == 1:
            vbox xalign 0.84 yalign 0.46:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 3), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS3]%" xalign 0.84 yalign 0.44


        if interact3 == 8:
            vbox xalign 0.7 yalign 0.0:
                imagebutton:
                    idle "mission/interact/shoot1.png"
                    hover "mission/interact/shoot1-hover.png"
                    action SetVariable("interSelect", 3), Jump("interInteract")


    if 4 <= randomBackground <= 7 and currentPosition == 4:


        if randomExit == 3:
            vbox xalign 0.11 yalign 0.17:
                imagebutton:
                    idle "mission/interact/Exit3.png"
                    hover "mission/interact/Exit3-hover.png"
                    if randomObst4 != 1:
                        action Jump("missionBegin")


        if randomObst4 == 1:
            vbox xalign 0.12 yalign 0.1:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 4), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS4]%" xalign 0.205 yalign 0.13



    if 8 <= randomBackground <= 10 and currentPosition == 0 and chanceOfControl <= 89:


        if randomObst1 != 1:
            vbox xalign 0.68 yalign 0.70:
                imagebutton:
                    idle "mission/cover/bg3Cover1.png"
                    hover "mission/cover/bg3Cover1-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        if interact1 == 8:
            vbox xalign 0.51 yalign -0.04:
                imagebutton:
                    idle "mission/interact/shoot1.png"
                    hover "mission/interact/shoot1-hover.png"
                    action SetVariable("interSelect", 1), Jump("interInteract")



        if randomObst1 == 1:
            vbox xalign 0.55 yalign 0.38:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 1), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS1]%" xalign 0.58 yalign 0.38


        if frontExit == 8:
            vbox xalign 0.10 yalign 0.50:
                imagebutton:
                    idle "mission/interact/frontExit1.png"
                    hover "mission/interact/frontExit1-hover.png"
                    action Jump("missionBegin")


    if 8 <= randomBackground <= 10 and currentPosition == 1:


        vbox xalign 0.31 yalign 0.80:
            imagebutton:
                idle "mission/cover/bg1Cover1.png"
                hover "mission/cover/bg1Cover1-hover.png"
                if disableScreen != True:
                    action Jump("coverInteract")


        if 1 <= randomLoot <= 2 and randomCover1 == 1:
            vbox xalign 0.83 yalign 0.55:
                imagebutton:
                    idle "mission/interact/loot.png"
                    hover "mission/interact/loot-hover.png"
                    action Jump("lootItem")





    if 8 <= randomBackground <= 10 and currentPosition == 2:


        vbox xalign 0.49 yalign 0.45:
            imagebutton:
                idle "mission/interact/bg3Exit1.png"
                hover "mission/interact/bg3Exit1-hover.png"
                if randomObst3 != 1:
                    action Jump("missionBegin")


        if randomObst3 == 1:
            vbox xalign 0.52 yalign 0.35:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 3), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS3]%" xalign 0.555 yalign 0.345


        if bonusExit == 10:
            vbox xalign 0.75 yalign 0.55:
                imagebutton:
                    idle "mission/interact/bonusExit2.png"
                    hover "mission/interact/bonusExit2-hover.png"
                    action SetVariable("bonusAvailable", 1), Jump("missionBegin")



    if 11 <= randomBackground <= 11 and currentPosition == 0 and chanceOfControl <= 89:


        if randomObst1 == 0:
            vbox xalign 0.27 yalign 0.97:
                imagebutton:
                    idle "mission/cover/bg1Cover1.png"
                    hover "mission/cover/bg1Cover1-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        if randomObst1 == 1:
            vbox xalign 0.42 yalign 0.5:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 1), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS1]%" xalign 0.47 yalign 0.48

        if randomObst1 == 2:
            vbox xalign 0.42 yalign 0.5:
                imagebutton:
                    idle "mission/interact/hackBig.png"
                    hover "mission/interact/hackBig-hover.png"
                    action SetVariable("interSelect", 2), Jump("interInteract")



    if 11 <= randomBackground <= 11 and currentPosition == 1:

        vbox xalign 0.85 yalign 0.75:
            imagebutton:
                idle "mission/cover/bg4Cover2.png"
                hover "mission/cover/bg4Cover2-hover.png"
                if disableScreen != True:
                    action Jump("coverInteract")


        if gadgetHookActive and gadgetActive == 5:
            vbox xalign 0.57 yalign 0.3:
                imagebutton:
                    idle "mission/interact/hook.png"
                    hover "mission/interact/hook-hover.png" tooltip " "
                    action Jump("hookInteract")


    if 11 <= randomBackground <= 11 and currentPosition == 2:

        if randomObst2 != 1:
            vbox xalign 0.38 yalign 0.67:
                imagebutton:
                    idle "mission/cover/bg3Cover2.png"
                    hover "mission/cover/bg3Cover2-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        if randomObst2 == 1:
            vbox xalign 0.56 yalign 0.5:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 2), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS2]%" xalign 0.59 yalign 0.48


    if 11 <= randomBackground <= 11 and currentPosition == 3:

        if randomObst3 != 1:
            vbox xalign 0.77 yalign 0.52:
                imagebutton:
                    idle "mission/cover/bg3Cover1.png"
                    hover "mission/cover/bg3Cover1-hover.png"
                    if disableScreen != True:
                        action Jump("coverInteract")


        if randomObst3 == 1:
            vbox xalign 0.67 yalign 0.25:
                imagebutton:
                    idle "mission/enemy/bg1Tar1.png"
                    hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                    action SetVariable("combatTarget", 3), Jump("agentInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[CoS3]%" xalign 0.69 yalign 0.26


    if 11 <= randomBackground <= 11 and currentPosition == 4:

        if currentPosition == 4:
            vbox xalign 0.49 yalign 0.5:
                imagebutton:
                    idle "mission/interact/Exit2.png"
                    hover "mission/interact/Exit2-hover.png"
                    action Jump("missionBegin")


    if 11 <= randomBackground <= 11 and currentPosition == 5:

        if currentPosition == 5:
            vbox xalign 0.52 yalign 0.5:
                imagebutton:
                    idle "mission/interact/frontExit2.png"
                    hover "mission/interact/frontExit2-hover.png"
                    action Jump("missionBegin")



    if 12 <= randomBackground <= 12 and currentPosition == 0 and chanceOfControl <= 89:

        if gadgetHookActive and gadgetActive == 5:
            vbox xalign 0.89 yalign 0.0:
                imagebutton:
                    idle "mission/interact/hook.png"
                    hover "mission/interact/hook-hover.png" tooltip " "
                    action Jump("hookInteract")


    if 12 <= randomBackground <= 12 and currentPosition == 1:

        if gadgetHookActive and gadgetActive == 5:
            vbox xalign 0.14 yalign 0.0:
                imagebutton:
                    idle "mission/interact/hook.png"
                    hover "mission/interact/hook-hover.png" tooltip " "
                    action Jump("hookInteract")


        if currentPosition == 1:
            vbox xalign 0.75 yalign 0.84:
                imagebutton:
                    idle "mission/interact/frontExit2.png"
                    hover "mission/interact/frontExit2-hover.png"
                    action Jump("missionBegin")


    if 12 <= randomBackground <= 12 and currentPosition == 2:

        if currentPosition == 2:
            vbox xalign 0.29 yalign 0.83:
                imagebutton:
                    idle "mission/interact/frontExit2.png"
                    hover "mission/interact/frontExit2-hover.png"
                    action Jump("missionBegin")





label agentInteract:
    hide spyGuard1
    hide spyGuard2
    hide spyGuard2
    hide agentAttack
    hide screen gadgetMenu
    hide screen interactScreen
    if gunReadyFire >= 1:
        jump agentInteractGun
    if 1 <= randomBackground <= 3 and currentPosition == 0:

        if combatTarget == 1:

            $ enemyCombSuc = renpy.random.randint(1, 99)
            if enemyCombSuc <= CoS1:
                if randomAgent1 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCorner
                    hide obst1

                    if target1LoveActive:
                        show obst1:
                            xalign 0.362 yalign 0.42 zoom 0.48
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.31 yalign 0.46 zoom 0.42
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.3 yalign 0.45 zoom 0.41
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.3 yalign 0.46 zoom 0.39
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target1LoveActive = False
                        $ flashbangActive = False
                        hide obst1
                        with d3
                        pause 0.3
                        $ randomObst1 = 0
                        hide obst1
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        $ randomObst1 = 0
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.362 yalign 0.42 zoom 0.42
                            linear 0.4 xalign 0.365 yalign 0.40
                        show spyCombat1:
                            xalign 0.34 yalign 0.41 zoom 0.42
                            linear 0.5 xalign 0.34 yalign 0.36
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 1
                    call randomLoot from _call_randomLoot
                    show spyCorner:
                        xalign 0.90 yalign 0.83 zoom 0.78
                    with d2
                    show screen interactScreen
                    jump jumpStartScene
            elif True:
                $ CoS1 += 2
                call reduceHealth from _call_reduceHealth
                hide spyCorner
                hide obst1

                if target1LoveActive:
                    show obst1:
                        xalign 0.362 yalign 0.42 zoom 0.48
                    $ randFlirt = renpy.random.randint(1,3)
                    show flirtJump:
                        xalign 0.65 yalign 0.87
                    with d1
                    hide flirtJump with d1
                    if randFlirt == 1:
                        show spyFlirt1:
                            xalign 0.31 yalign 0.46 zoom 0.42
                    if randFlirt == 2:
                        show spyFlirt2:
                            xalign 0.3 yalign 0.45 zoom 0.41
                    if randFlirt == 3:
                        show spyFlirt3:
                            xalign 0.3 yalign 0.46 zoom 0.4
                    play sound "audio/sfx/giggle1.mp3"
                    $ renpy.pause(0.5, hard='True')
                    "Agent" "Begone you floozy!"
                    $ flashbangActive = False
                    hide obst1
                    hide spyFlirt1
                    hide spyFlirt2
                    hide spyFlirt3
                    with d3
                elif True:
                    play sound "audio/sfx/block1.mp3"
                    show agentGuard:
                        xalign 0.385 yalign 0.47 zoom 0.42
                    show spyCombat1:
                        xalign 0.34 yalign 0.41 zoom 0.42
                        linear 0.5 xalign 0.34 yalign 0.36
                    $ renpy.pause(0.5, hard='True')
                    hide agentGuard with d1
                    play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.385 yalign 0.41 zoom 0.43
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.33 yalign 0.46 zoom 0.43
                            linear 0.06 xalign 0.332
                            linear 0.06 xalign 0.33
                            linear 0.06 xalign 0.332
                            linear 0.06 xalign 0.33
                        with d1
                        pause 0.24
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.34 yalign 0.36 zoom 0.35 xzoom -1
                    linear 0.4 xalign 0.33 yalign 0.345
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                $ obst1FoV = 1
                show obst1:
                    xalign 0.365 yalign 0.43 rotate 2 zoom 0.48
                with d3
                call spyHitBackup from _call_spyHitBackup
                call screen interactScreen
        if combatTarget == 2:
            "Target is out of range. Get closer or use a gadget instead."
            jump jumpStartScene


    if 1 <= randomBackground <= 3 and currentPosition == 1:
        if combatTarget == 2:

            $ enemyCombSuc = renpy.random.randint(1, 99)
            if enemyCombSuc <= CoS2:
                $ flashbangActive = 0
                if randomAgent2 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCrouchCorner
                    hide spyCorner
                    hide obst2

                    if target2LoveActive:
                        show obst2:
                            xalign 0.657 yalign 0.8 rotate 3 zoom 0.46
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.58 yalign 0.79 zoom 0.4
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.58 yalign 0.78 zoom 0.39
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.58 yalign 0.79 zoom 0.37
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target2LoveActive = False
                        $ flashbangActive = False
                        hide obst2
                        with d3
                        pause 0.3
                        $ randomObst2 = 0
                        hide obst2
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        $ randomObst2 = 0
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.635 yalign 0.77 zoom 0.40
                            linear 0.4 xalign 0.635 yalign 0.76
                        show spyCombat1:
                            xalign 0.56 yalign 0.70 zoom 0.42
                            linear 0.5 xalign 0.56 yalign 0.69
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 1
                    call randomLoot from _call_randomLoot_1
                    show spyCrouchCorner:
                        xalign -0.03 yalign 0.84 zoom 0.405
                    with d2
                    show screen interactScreen
                    jump jumpStartScene
            elif True:
                $ CoS2 += 2
                call reduceHealth from _call_reduceHealth_1
                hide spyCrouchCorner
                hide spyCorner
                hide obst2

                if target1LoveActive:
                    show obst1:
                        xalign 0.362 yalign 0.42 zoom 0.48
                    $ randFlirt = renpy.random.randint(1,3)
                    show flirtJump:
                        xalign 0.65 yalign 0.87
                    with d1
                    hide flirtJump with d1
                    if randFlirt == 1:
                        show spyFlirt1:
                            xalign 0.31 yalign 0.46 zoom 0.42
                    if randFlirt == 2:
                        show spyFlirt2:
                            xalign 0.3 yalign 0.45 zoom 0.41
                    if randFlirt == 3:
                        show spyFlirt3:
                            xalign 0.3 yalign 0.46 zoom 0.4
                    play sound "audio/sfx/giggle1.mp3"
                    $ renpy.pause(0.5, hard='True')
                    "Agent" "Begone you floozy!"
                    $ flashbangActive = False
                    hide obst1
                    hide spyFlirt1
                    hide spyFlirt2
                    hide spyFlirt3
                    with d3
                elif True:
                    play sound "audio/sfx/block1.mp3"
                    show agentGuard:
                        xalign 0.635 yalign 0.77 zoom 0.40
                    show spyCombat1:
                        xalign 0.56 yalign 0.70 zoom 0.42
                        linear 0.5 xalign 0.56 yalign 0.69
                    $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.67 yalign 0.77 rotate 3 zoom 0.40
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.61 yalign 0.77 zoom 0.4
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.56 yalign 0.70 zoom 0.35 xzoom -1
                    linear 0.4 xalign 0.55 yalign 0.68
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                $ obst2FoV = 1
                show obst2:
                    xalign 0.635 yalign 0.755 zoom 0.43
                with d3
                call spyHitBackup from _call_spyHitBackup_1
        jump missionBegin



    if 4 <= randomBackground <= 7 and currentPosition == 0:

        if combatTarget == 1:

            $ enemyCombSuc = renpy.random.randint(1, 99)
            if enemyCombSuc <= CoS1:
                if randomAgent1 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCornerSide
                    hide obst1

                    if target1LoveActive:
                        show obst1:
                            xalign 0.65 yalign 0.98 zoom 0.48
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.6 yalign 0.98 zoom 0.42
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.6 yalign 0.98 zoom 0.41
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.6 yalign 0.98 zoom 0.39
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ flashbangActive = False
                        $ target1LoveActive = False
                        $ randomObst1 = 0
                        hide obst1
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.67 yalign 0.97 zoom 0.44 xzoom -1
                            linear 0.35 xalign 0.66 yalign 0.95
                        show spyCombat1:
                            xalign 0.69 yalign 0.95 zoom 0.455 xzoom -1
                            linear 0.35 xalign 0.69 yalign 0.92
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ randomObst1 = 0
                    $ lootLoc = 1
                    call randomLoot from _call_randomLoot_2
                    show spyCornerSide:
                        xalign 0.97 yalign 0.90 zoom 0.39
                    with d2
                    show screen interactScreen
                    jump jumpStartScene
            elif True:
                $ CoS1 += 2
                call reduceHealth from _call_reduceHealth_2
                hide spyCornerSide
                hide obst1
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.65 yalign 0.97 zoom 0.46
                    linear 0.1 xalign 0.653
                    linear 0.1 xalign 0.65
                    linear 0.1 xalign 0.653
                    linear 0.1 xalign 0.65
                show spyCombat1:
                    xalign 0.57 yalign 0.94 zoom 0.46
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.65 yalign 0.97 zoom 0.43
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.63 yalign 0.98 zoom 0.42
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.57 yalign 0.94 zoom 0.38 xzoom -1
                    linear 0.4 xalign 0.566 yalign 0.92
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                show obst1:
                    xalign 0.65 yalign 0.97 zoom 0.48
                with d3
                call spyHitBackup from _call_spyHitBackup_2
        jump missionBegin
        if combatTarget == 2:
            "Target is out of range. Get closer or use a gadget instead."
            jump jumpStartScene

    if 4 <= randomBackground <= 7 and currentPosition == 1:

        if combatTarget == 2:

            $ enemyCombSuc = renpy.random.randint(1, 99)
            if enemyCombSuc <= CoS2:
                if randomAgent2 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCornerSide
                    hide obst2

                    if target2LoveActive:
                        show obst2:
                            xalign 0.02 yalign 0.98 zoom 0.48
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.0 yalign 0.98
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.0 yalign 0.98 zoom 0.42
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.0 yalign 0.98 zoom 0.41
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.0 yalign 0.98 zoom 0.39
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target2LoveActive = False
                        $ flashbangActive = False
                        hide obst2
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                        $ randomObst2 = 0
                    elif True:
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.04 yalign 0.97 zoom 0.44 xzoom -1
                            linear 0.35 xalign 0.04 yalign 0.95
                        show spyCombat1:
                            xalign 0.08 yalign 0.95 zoom 0.455 xzoom -1
                            linear 0.35 xalign 0.08 yalign 0.92
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ randomObst2 = 0
                    $ lootLoc = 1
                    call randomLoot from _call_randomLoot_3
                    show spyCornerSide:
                        xalign 0.88 yalign 0.90 zoom 0.39
                    with d2
                    show screen interactScreen
                    jump jumpStartScene
            elif True:
                $ CoS2 += 2
                call reduceHealth from _call_reduceHealth_3
                hide spyCornerSide
                hide obst2
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.03 yalign 0.97 xzoom -1 zoom 0.46
                    linear 0.1 xalign 0.035
                    linear 0.1 xalign 0.03
                    linear 0.1 xalign 0.035
                    linear 0.1 xalign 0.03
                show spyCombat1:
                    xalign 0.14 yalign 0.94 xzoom -1 zoom 0.46
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.03 yalign 0.97 zoom 0.44 xzoom -1
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.04 yalign 0.96 zoom 0.41 xzoom -1
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.11 yalign 0.94 zoom 0.38
                    linear 0.4 xalign 0.12 yalign 0.92
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                show obst2:
                    xalign 0.03 yalign 0.97 zoom 0.48
                with d3
                call spyHitBackup from _call_spyHitBackup_3
        jump missionBegin
        if combatTarget == 2:
            "Target is out of range. Get closer or use a gadget instead."
            jump jumpStartScene
    if 4 <= randomBackground <= 7 and currentPosition == 3:

        if combatTarget == 3:

            $ enemyCombSuc = renpy.random.randint(1, 99)
            if enemyCombSuc <= CoS3:
                $ flashbangActive = 0
                if randomAgent3 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCornerSide
                    hide obst3

                    if target3LoveActive:
                        show obst3:
                            xalign 0.79 yalign 0.58 zoom 0.43
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.7 yalign 0.58 zoom 0.47
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.7 yalign 0.58 zoom 0.35
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.7 yalign 0.58 zoom 0.35
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target3LoveActive = False
                        hide obst3
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d2
                        $ randomObst3 = 0
                    elif True:
                        $ randomObst3 = 0
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.75 yalign 0.55 zoom 0.40
                            linear 0.30 xalign 0.755 yalign 0.53
                        show spyCombat1:
                            xalign 0.71 yalign 0.55 zoom 0.40
                            linear 0.30 xalign 0.71 yalign 0.50
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 1
                    call randomLoot from _call_randomLoot_4
                    show spyCornerSide:
                        xalign 0.497 yalign 0.59 zoom 0.37 xzoom -1
                    with d2
                    show screen interactScreen
                    jump jumpStartScene
            elif True:
                $ CoS3 += 2
                call reduceHealth from _call_reduceHealth_4
                hide spyCornerSide
                hide obst3
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.77 yalign 0.61 zoom 0.40
                    linear 0.1 xalign 0.78
                    linear 0.1 xalign 0.77
                    linear 0.1 xalign 0.78
                    linear 0.1 xalign 0.77
                show spyCombat1:
                    xalign 0.71 yalign 0.55 zoom 0.40
                    linear 0.30 xalign 0.71 yalign 0.50
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                if randomAgent3 == 1:
                    show agentAttack:
                        xalign 0.77 yalign 0.575 zoom 0.385
                if randomAgent3 == 2:
                    show agentAttack:
                        xalign 0.77 yalign 0.54 zoom 0.385
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.74 yalign 0.58 zoom 0.36
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.74 yalign 0.57 zoom 0.34 xzoom -1
                    linear 0.4 xalign 0.73 yalign 0.55
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                show obst3:
                    xalign 0.77 yalign 0.59 zoom 0.43
                with d3
                call spyHitBackup from _call_spyHitBackup_4
        jump missionBegin
        if combatTarget == 2:
            "Target is out of range. Get closer or use a gadget instead."
            jump jumpStartScene

    if 4 <= randomBackground <= 7 and currentPosition == 4:

        if combatTarget == 4:

            $ enemyCombSuc = renpy.random.randint(1, 99)
            if enemyCombSuc <= CoS4:
                $ flashbangActive = 0
                if randomAgent4 <= 4:
                    hide flashEffect
                    hide loveEffect
                    $ randomObst4 = 0
                    hide spyCornerSide
                    hide obst4

                    if target1LoveActive:
                        show obst1:
                            xalign 0.362 yalign 0.42 zoom 0.48
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.31 yalign 0.46 zoom 0.42
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.3 yalign 0.45 zoom 0.41
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.3 yalign 0.46 zoom 0.39
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target4LoveActive = False
                        $ flashbangActive = False
                        hide obst1
                        with d3
                        pause 0.3
                        $ randomObst1 = 0
                        hide obst1
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        $ randomObst4 = 0
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.12 yalign 0.16 zoom 0.305
                            linear 0.30 xalign 0.125 yalign 0.15
                        show spyCombat1:
                            xalign 0.10 yalign 0.12 zoom 0.32
                            linear 0.30 xalign 0.10 yalign 0.11
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 1
                    call randomLoot from _call_randomLoot_5
                    show spyCrouchCorner:
                        xalign 0.19 yalign 0.22 rotate 4 zoom 0.23 xzoom -1
                    with d2
                    show screen interactScreen
                    jump jumpStartScene
            elif True:
                $ CoS4 += 2
                call reduceHealth from _call_reduceHealth_5
                hide spyCornerSide
                hide obst4
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.12 yalign 0.17 zoom 0.30
                    linear 0.1 xalign 0.125
                    linear 0.1 xalign 0.12
                    linear 0.1 xalign 0.125
                    linear 0.1 xalign 0.12
                show spyCombat1:
                    xalign 0.10 yalign 0.12 zoom 0.32
                    linear 0.30 xalign 0.10 yalign 0.11
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.13 yalign 0.11 zoom 0.305
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.07 yalign 0.14 zoom 0.29
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.10 yalign 0.13 zoom 0.25 xzoom -1
                    linear 0.4 xalign 0.09 yalign 0.12
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                show obst4:
                    xalign 0.12 yalign 0.12 zoom 0.32
                with d3
                call spyHitBackup from _call_spyHitBackup_5
        jump missionBegin
        if combatTarget == 2:
            "Target is out of range. Get closer or use a gadget instead."
            jump jumpStartScene


    if 8 <= randomBackground <= 10 and currentPosition == 0:
        hide screen interactScreen

        if combatTarget == 1:

            $ enemyCombSuc = renpy.random.randint(1, 100)
            if enemyCombSuc <= CoS1:
                hide spyCrouchCorner
                if randomAgent1 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCorner

                    if target1LoveActive:
                        hide obst1
                        show obst1:
                            xalign 0.53 yalign 0.5 zoom 0.47
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.43 yalign 0.54 zoom 0.38
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.43 yalign 0.54 zoom 0.38
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.43 yalign 0.54 zoom 0.38
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target1LoveActive = False
                        $ flashbangActive = False
                        hide obst1
                        with d3
                        pause 0.3
                        $ randomObst1 = 0
                        hide obst1
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        $ randomObst1 = 0
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.50 yalign 0.50 zoom 0.46
                            linear 0.4 xalign 0.50 yalign 0.45
                        show spyCombat1:
                            xalign 0.465 yalign 0.50 zoom 0.46
                            linear 0.5 xalign 0.465 yalign 0.45
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 2
                    call randomLoot from _call_randomLoot_7
                    show spyCorner:
                        xalign 0.99 yalign 0.83 zoom 0.78
                    with d2
                    jump jumpStartScene
            elif True:
                $ CoS1 += 2
                call reduceHealth from _call_reduceHealth_6
                hide spyCrouchCorner
                hide spyCorner
                hide obst1
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.53 yalign 0.55 zoom 0.44
                show spyCombat1:
                    xalign 0.46 yalign 0.50 zoom 0.46
                    linear 0.5 xalign 0.46 yalign 0.45
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.53 yalign 0.54 zoom 0.44
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.5 yalign 0.59 zoom 0.43
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.465 yalign 0.50 zoom 0.38 xzoom -1
                    linear 0.5 xalign 0.455 yalign 0.49
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                $ obst1FoV = 1
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
                with d3
                call spyHitBackup from _call_spyHitBackup_6
                call screen interactScreen
    if 8 <= randomBackground <= 10 and currentPosition == 2:
        hide screen interactScreen

        if combatTarget == 3:

            $ enemyCombSuc = renpy.random.randint(1, 100)
            if enemyCombSuc <= CoS3:
                $ flashbangActive = 0
                hide spyCrouchCorner
                if randomAgent1 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCorner

                    if target3LoveActive:
                        show obst3:
                            xalign 0.5 yalign 0.62 zoom 0.65
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.42 yalign 0.65 zoom 0.52
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.42 yalign 0.65 zoom 0.51
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.42 yalign 0.68 zoom 0.5
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target3LoveActive = False
                        $ flashbangActive = False
                        hide obst3
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        play sound "audio/sfx/defeatEnemy.mp3"
                        hide obst3
                        show agentHit:
                            xalign 0.50 yalign 0.50 zoom 0.59
                            linear 0.4 xalign 0.50 yalign 0.45
                        show spyCombat1:
                            xalign 0.465 yalign 0.50 zoom 0.59
                            linear 0.5 xalign 0.465 yalign 0.45
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ randomObst3 = 0
                    $ lootLoc = 2
                    call randomLoot from _call_randomLoot_8
                    show spyCrouchCorner:
                        xalign -0.1 yalign 1.5 rotate -3 zoom 0.52
                    with d2
                    jump jumpStartScene
            elif True:
                $ CoS3 += 2
                call reduceHealth from _call_reduceHealth_7
                hide spyCrouchCorner
                hide spyCorner
                hide obst3
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.50 yalign 0.70 zoom 0.59
                show spyCombat1:
                    xalign 0.425 yalign 0.50 zoom 0.59
                    linear 0.5 xalign 0.425 yalign 0.45
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.50 yalign 0.65 zoom 0.57
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.46 yalign 0.76 zoom 0.56
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.465 yalign 0.50 zoom 0.48 xzoom -1
                    linear 0.5 xalign 0.455 yalign 0.49
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                $ obst3FoV = 1
                show obst3:
                    xalign 0.50 yalign 0.63 zoom 0.65
                with d3
                call spyHitBackup from _call_spyHitBackup_7
                call screen interactScreen



    if 11 <= randomBackground <= 11 and currentPosition == 0:
        hide screen interactScreen

        if combatTarget == 1:

            $ enemyCombSuc = renpy.random.randint(1, 100)
            if enemyCombSuc <= CoS1:
                hide spyCrouchCorner
                if randomAgent1 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCorner

                    if target1LoveActive:
                        hide obst1
                        show obst1:
                            xalign 0.4 yalign 1.1 zoom 0.7
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.31 yalign 0.98 zoom 0.62
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.3 yalign 0.98 zoom 0.61
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.3 yalign 0.98 zoom 0.59
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target1LoveActive = False
                        $ flashbangActive = False
                        hide obst1
                        with d3
                        pause 0.3
                        $ randomObst1 = 0
                        hide obst1
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        play sound "audio/sfx/defeatEnemy.mp3"
                        $ randomObst1 = 0
                        show agentHit:
                            xalign 0.4 yalign 0.90 zoom 0.62
                            linear 0.4 xalign 0.4 yalign 0.8
                        show spyCombat1:
                            xalign 0.33 yalign 0.7 zoom 0.65
                            linear 0.5 xalign 0.33 yalign 0.6
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 2
                    call randomLoot from _call_randomLoot_9
                    show spyCorner:
                        xalign 1.15 ypos 200
                    with d2
                    jump jumpStartScene
            elif True:
                $ CoS1 += 2
                call reduceHealth from _call_reduceHealth_9
                hide spyCrouchCorner
                hide spyCorner
                hide obst1
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.43 yalign 1.0 zoom 0.62
                show spyCombat1:
                    xalign 0.33 yalign 0.7 zoom 0.65
                    linear 0.5 xalign 0.33 yalign 0.6
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.43 yalign 1.09 zoom 0.62
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.3 yalign 1.07 zoom 0.58
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.33 yalign 0.7 zoom 0.55 xzoom -1
                    linear 0.5 xalign 0.32 yalign 0.68 zoom 0.55
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                $ obst1FoV = 1
                show obst1:
                    xalign 0.4 yalign 1.1 zoom 0.7
                with d3
                call spyHitBackup from _call_spyHitBackup_11
                call screen interactScreen
    if 11 <= randomBackground <= 11 and currentPosition == 2:
        hide screen interactScreen

        if combatTarget == 2:

            $ enemyCombSuc = renpy.random.randint(1, 100)
            if enemyCombSuc <= CoS2:
                hide spyCrouchCorner
                if randomAgent2 <= 4:
                    hide flashEffect
                    hide loveEffect
                    $ randomObst2 = 0
                    hide spyCorner

                    if target1LoveActive:
                        show Obst2:
                            xalign 0.362 yalign 0.42 zoom 0.48
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.65 yalign 0.87
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.31 yalign 0.46 zoom 0.42
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.3 yalign 0.45 zoom 0.41
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.3 yalign 0.46 zoom 0.39
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target1LoveActive = False
                        $ flashbangActive = False
                        hide Obst2
                        with d3
                        pause 0.3
                        $ randomObst2 = 0
                        hide Obst2
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        play sound "audio/sfx/defeatEnemy.mp3"
                        show agentHit:
                            xalign 0.56 yalign 0.60 zoom 0.42
                            linear 0.4 xalign 0.562 yalign 0.55
                        show spyCombat1:
                            xalign 0.47 yalign 0.6 zoom 0.45
                            linear 0.5 xalign 0.47 yalign 0.54
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 2
                    call randomLoot from _call_randomLoot_10
                    show spyCrouchCorner:
                        xalign 0.96 yalign 1.1 rotate 5 zoom 0.39 xzoom -1
                    with d2
                    jump jumpStartScene
            elif True:
                $ CoS2 += 2
                call reduceHealth from _call_reduceHealth_10
                hide spyCrouchCorner
                hide spyCorner
                hide obst2
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.57 yalign 0.62 zoom 0.42
                show spyCombat1:
                    xalign 0.51 yalign 0.58 zoom 0.42
                    linear 0.5 xalign 0.51 yalign 0.56
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.57 yalign 0.62 zoom 0.4
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.5 yalign 0.59 zoom 0.43
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.465 yalign 0.50 zoom 0.33 xzoom -1
                    linear 0.5 xalign 0.455 yalign 0.49
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                $ Obst2FoV = 1
                show obst2:
                    xalign 0.53 yalign 0.66 zoom 0.45
                with d3
                call spyHitBackup from _call_spyHitBackup_12
                call screen interactScreen

    if 11 <= randomBackground <= 11 and currentPosition == 3:
        hide screen interactScreen

        if combatTarget == 3:

            $ enemyCombSuc = renpy.random.randint(1, 100)
            if enemyCombSuc <= CoS3:
                hide spyCrouchCorner
                if randomAgent3 <= 4:
                    hide flashEffect
                    hide loveEffect
                    hide spyCorner

                    if target3LoveActive:
                        show obst2:
                            xalign 0.61 yalign 0.35 zoom 0.48
                        $ randFlirt = renpy.random.randint(1,3)
                        show flirtJump:
                            xalign 0.61 yalign 0.35 zoom 0.5
                        with d1
                        hide flirtJump with d1
                        if randFlirt == 1:
                            show spyFlirt1:
                                xalign 0.55 yalign 0.36 zoom 0.37
                        if randFlirt == 2:
                            show spyFlirt2:
                                xalign 0.55 yalign 0.36 zoom 0.35
                        if randFlirt == 3:
                            show spyFlirt3:
                                xalign 0.55 yalign 0.36 zoom 0.34
                        play sound "audio/sfx/giggle1.mp3"
                        $ renpy.pause(0.5, hard='True')
                        "Agent" "Wow, a pretty girl is talking to me! I'm gonna call my mom!"
                        $ target1LoveActive = False
                        $ flashbangActive = False
                        hide Obst2
                        with d3
                        pause 0.3
                        $ randomObst3 = 0
                        hide Obst2
                        hide spyFlirt1
                        hide spyFlirt2
                        hide spyFlirt3
                        with d3
                    elif True:
                        play sound "audio/sfx/defeatEnemy.mp3"
                        $ randomObst3 = 0
                        show agentHit:
                            xalign 0.6 yalign 0.32 zoom 0.4
                            linear 0.4 xalign 0.6 yalign 0.3
                        show spyCombat1:
                            xalign 0.54 yalign 0.3 zoom 0.41
                            linear 0.5 xalign 0.54 yalign 0.28
                        $ renpy.pause(0.5, hard='True')
                        hide agentHit
                        hide spyCombat1
                        with d1
                    $ lootLoc = 2
                    call randomLoot from _call_randomLoot_11
                    show spyCrouchCorner:
                        xalign 0.2 yalign 0.9 rotate -5 zoom 0.39
                    $ disableScreen = False
                    jump jumpStartScene
            elif True:
                $ CoS2 += 2
                call reduceHealth from _call_reduceHealth_11
                hide spyCrouchCorner
                hide spyCorner
                hide obst3
                play sound "audio/sfx/block1.mp3"
                show agentGuard:
                    xalign 0.64 yalign 0.32 zoom 0.4
                show spyCombat1:
                    xalign 0.55 yalign 0.28 zoom 0.4
                    linear 0.5 xalign 0.55 yalign 0.26
                $ renpy.pause(0.5, hard='True')
                hide agentGuard with d1
                play sound "audio/sfx/punch1.mp3"
                show agentAttack:
                    xalign 0.64 yalign 0.32 zoom 0.4
                hide spyCombat1

                if skillSecondChance == 1:
                    $ chanceToDefend = renpy.random.randint(1, 100)
                    if flashbangActive == 2:
                        $ chanceToDefend += 30
                    if target1PoisonActive == True:
                        $ chanceToDefend += 10
                    if chanceToDefend >= 75:
                        show spyGuard2:
                            xalign 0.5 yalign 0.59 zoom 0.43
                        with d2
                        call screen interactScreen
                elif True:
                    pass

                show spyHit:
                    xalign 0.55 yalign 0.28 zoom 0.35 xzoom -1
                    linear 0.5 xalign 0.54 yalign 0.27
                with d1
                pause 0.4
                hide spyHit
                hide agentAttack
                $ Obst2FoV = 1
                show obst3:
                    xalign 0.64 yalign 0.32 zoom 0.4
                with d3
                call spyHitBackup from _call_spyHitBackup_13
                call screen interactScreen




label bossInteract:
    hide spyGuard
    if 1 <= randomBackground <= 3:
        hide screen interactScreen
        hide spyGuard2
        hide spyCorner
        if specialBossActive:

            if missionSetting == "Castle" and specialMaggieStatus == 1:
                $ randomBossHP -= 1
                hide obstMaggie
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstMaggie:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    mag "Foolish girls! You are no match for our combined strength!"
                    hide obstMaggie with d3
                    $ randomBoss = 0
                    if activeSpy == 1:
                        sM "She's getting away!"
                        sM "Should we pursue her or pull back?"
                    if activeSpy == 2:
                        cM "She's getting away!"
                        cM "Should we pursue her or pull back?"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        aM "Should we pursue her or pull back?"
                    hide spyCombat2 with d1
                    menu:
                        "Pursue the target" if True:
                            $ missionProgression = 7
                            jump missionBegin
                        "Pull back for now" if True:
                            y "We'll get 'em next time."
                            hide screen equipmentMenu
                            $ randomBoss = 0
                            hide spyCombat1
                            with d3
                            $ loot1 += 1
                            $ loot5 += 1
                            play sound "audio/sfx/jobReward.mp3"
                            show dropMats at item_drop((550,300))
                            pause 0.3
                            play sound "audio/sfx/jobReward.mp3"
                            show dropConsum at item_drop((550,300))
                            with d3
                            pause 0.5
                            call threatNeutralized from _call_threatNeutralized
                            jump missionComplete
                elif randomBossHP <= 0:
                    $ specialMaggieStatus = 2
                    $ specialBossActive = False
                    show obstMaggie:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    mag "Oof~...!"
                    jump task3

            if missionSetting == "Castle" and specialMelodyStatus == 1 and task6Stage >= 12:
                $ randomBossHP -= 1
                hide obstMelody
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstMelody:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    mel "You won't take me in that easily!"
                    hide obstMelody with d3
                    $ randomBoss = 0
                    if activeSpy == 1:
                        sM "She's getting away!"
                        sM "Should we pursue her or pull back?"
                    if activeSpy == 2:
                        cM "She's getting away!"
                        cM "Should we pursue her or pull back?"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        aM "Should we pursue her or pull back?"
                    hide spyCombat2 with d1
                    menu:
                        "Pursue the target" if True:
                            $ missionProgression = 7
                            jump missionBegin
                        "Pull back for now" if True:
                            y "We'll get 'em next time."
                            hide screen equipmentMenu
                            $ randomBoss = 0
                            hide spyCombat1
                            with d3
                            $ loot1 += 1
                            $ loot5 += 1
                            play sound "audio/sfx/jobReward.mp3"
                            show dropMats at item_drop((550,300))
                            pause 0.3
                            play sound "audio/sfx/jobReward.mp3"
                            show dropConsum at item_drop((550,300))
                            with d3
                            pause 0.5
                            call threatNeutralized from _call_threatNeutralized_1
                            jump missionComplete
                elif randomBossHP <= 0:
                    $ specialMelodyStatus = 2
                    $ specialBossActive = False
                    show obstMelody:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    mel "Ugh~...!"
                    $ task6Stage = 12
                    jump task6

            if missionSetting == "Castle" and specialCandyStatus == 1 and task16Stage == 3:
                $ randomBossHP -= 1
                hide obstCandy
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstCandy:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    candy "It won't be that easy..."
                    hide obstCandy with d3
                    $ randomBoss = 0
                    if activeSpy == 2:
                        cM "She's getting away!"
                        y "After her!"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        y "After her!"
                    hide spyCombat2 with d1
                    $ missionProgression = 7
                    jump missionBegin
                elif randomBossHP <= 0:
                    $ specialCandyStatus = 2
                    $ specialBossActive = False
                    show obstCandy:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    candy "Back off, brats!"
                    $ task16Stage = 4
                    jump task16



            if missionSetting == "Database" and specialDragonStatus == 1:
                $ randomBossHP -= 1
                hide obstDragon
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstDragon:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    drag "Getting cocky are we? You won't take this dragon in so easily!"
                    hide obstDragon with d3
                    $ randomBoss = 0
                    if activeSpy == 1:
                        sM "She's getting away!"
                        sM "Should we pursue her or pull back?"
                    if activeSpy == 2:
                        cM "She's getting away!"
                        cM "Should we pursue her or pull back?"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        aM "Should we pursue her or pull back?"
                    hide spyCombat2 with d1
                    menu:
                        "Pursue the target" if True:
                            $ missionProgression = 7
                            jump missionBegin
                        "Pull back for now" if True:
                            y "We'll get 'em next time."
                            hide screen equipmentMenu
                            $ randomBoss = 0
                            hide spyCombat1
                            with d3
                            $ loot1 += 1
                            $ loot5 += 1
                            play sound "audio/sfx/jobReward.mp3"
                            show dropMats at item_drop((550,300))
                            pause 0.3
                            play sound "audio/sfx/jobReward.mp3"
                            show dropConsum at item_drop((550,300))
                            with d3
                            pause 0.5
                            call threatNeutralized from _call_threatNeutralized_2
                            jump missionComplete
                elif randomBossHP <= 0:
                    $ specialDragonStatus = 2
                    $ specialBossActive = False
                    show obstDragon:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    $ prisonersNew = True
                    $ task10Text = _("We discovered that a former video game programmer called Carla Wong, aka The Dragon Lady, is the lead developer on Punk Web. She's already attacked Clover once, so it's time we brought her in.\n\n{color=#b5b5b5}-Set up a mission and capture Carla Wong.{/color}\n\n-Interrogate Carla Wong at the base.")
                    drag "My fire has gone out..."
                    drag "Take me back to prison, I won't resist..."
                    hide obstDragon
                    hide spyCombat2
                    hide screen equipmentMenu
                    $ randomBoss = 0
                    hide spyCombat1
                    with d3
                    $ loot1 += 1
                    $ loot2 += 1
                    $ loot3 += 1
                    $ loot5 += 1
                    play sound "audio/sfx/jobReward.mp3"
                    show dropMats at item_drop((550,300))
                    pause 0.3
                    play sound "audio/sfx/jobReward.mp3"
                    show dropConsum at item_drop((550,300))
                    with d3
                    pause 0.5
                    call threatNeutralized from _call_threatNeutralized_4
                    jump missionComplete
            if missionSetting == "Database" and specialTaliaStatus == 1 and task18Stage == 2:
                $ randomBossHP -= 1
                hide obstTalia
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstTalia:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    tali "Oooh no! Please don't capture me and take me away from my gang!"
                    hide obstTalia with d3
                    $ randomBoss = 0
                    if activeSpy == 1:
                        sM "She's getting away!"
                        sM "Should we pursue her or pull back?"
                    if activeSpy == 2:
                        cM "She's getting away!"
                        cM "Should we pursue her or pull back?"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        aM "Should we pursue her or pull back?"
                    hide spyCombat2 with d1
                    menu:
                        "Pursue the target" if True:
                            $ missionProgression = 7
                            jump missionBegin
                        "Pull back for now" if True:
                            y "We'll get 'em next time."
                            hide screen equipmentMenu
                            $ randomBoss = 0
                            hide spyCombat1
                            with d3
                            $ loot1 += 1
                            $ loot6 += 1
                            play sound "audio/sfx/jobReward.mp3"
                            show dropMats at item_drop((550,300))
                            pause 0.3
                            play sound "audio/sfx/jobReward.mp3"
                            show dropConsum at item_drop((550,300))
                            with d3
                            pause 0.5
                            call threatNeutralized from _call_threatNeutralized_8
                            jump missionComplete
                elif randomBossHP <= 0:
                    $ specialTaliaStatus = 2
                    $ specialBossActive = False
                    show obstTalia:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    $ prisonersNew = True
                    $ task10Text = _("We discovered that a former video game programmer called Carla Wong, aka The Dragon Lady, is the lead developer on Punk Web. She's already attacked Clover once, so it's time we brought her in.\n\n{color=#b5b5b5}-Set up a mission and capture Carla Wong.{/color}\n\n-Interrogate Carla Wong at the base.")
                    tali "Oh no! You tore my favorite coat~..."
                    tali "I couldn't possibly go on. Take me to prison. I won't resist..."
                    hide obstTalia
                    hide spyCombat2
                    hide screen equipmentMenu
                    $ randomBoss = 0
                    hide spyCombat1
                    with d3
                    $ loot1 += 1
                    $ loot2 += 1
                    $ loot3 += 1
                    $ loot4 += 1
                    $ loot5 += 1
                    play sound "audio/sfx/jobReward.mp3"
                    show dropMats at item_drop((550,300))
                    pause 0.3
                    play sound "audio/sfx/jobReward.mp3"
                    show dropConsum at item_drop((550,300))
                    with d3
                    pause 0.5
                    call threatNeutralized from _call_threatNeutralized_9
                    jump missionComplete
            if missionSetting == "Database" and specialSebStatus == 1 and task23Stage == 5:
                $ randomBossHP -= 1
                hide bossSeb
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show bossSeb3:
                        xalign 0.50 yalign 0.54 rotate 3 zoom 0.41
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.55 zoom 0.43
                    pause 0.35

                    $ spyBlockChance = renpy.random.randint(6, 10)

                    if spyBlockChance >= 6:
                        hide spyCombat2
                        hide bossSeb3
                        with d1
                        show bossSeb2:
                            xalign 0.5 yalign 0.46 zoom 0.52
                        show spyGuard2:
                            xalign 0.41 yalign 0.55 zoom 0.47 rotate 3
                            linear 0.1 xalign 0.415
                            linear 0.1 xalign 0.41
                            linear 0.1 xalign 0.415
                            linear 0.1 xalign 0.41
                        with d2
                        pause 0.4
                        hide bossSeb2
                        show bossSeb:
                            xalign 0.48 yalign 0.48 zoom 0.45 rotate 3
                        hide spyGuard2
                        show spyGuard2:
                            xalign 0.41 yalign 0.55 zoom 0.47 rotate 3
                        with d2
                        call screen interactScreen
                    elif True:
                        hide spyCombat2
                        hide bossSeb3
                        with d1
                        show bossSeb2:
                            xalign 0.5 yalign 0.46 zoom 0.52
                        show spyHit:
                            xalign 0.42 yalign 0.4 zoom 0.41 xzoom -1
                            linear 0.3 xalign 0.417 yalign 0.38
                        with d2
                        pause 0.4
                        hide bossSeb2
                        hide spyHit
                        show bossSeb:
                            xalign 0.48 yalign 0.48 zoom 0.45 rotate 3
                        with d2
                        call spyHitBackup from _call_spyHitBackup_14

                elif randomBossHP <= 0:
                    $ specialSebStatus = 2
                    $ specialBossActive = False
                    show bossSeb4:
                        xalign 0.48 yalign 0.48 zoom 0.4 rotate 3
                        linear 0.5 xalign 0.49 yalign 0.47
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    $ prisonersNew = True
                    $ task23Text = _("Sebastian Sage has been captured and the Drift Punk have lost their leader. With him gone the gang will soon disband.")
                    c "Oof~....!"
                    hide bossSeb4
                    hide spyCombat2
                    hide screen equipmentMenu
                    $ randomBoss = 0
                    hide spyCombat1
                    with d3
                    $ loot1 += 1
                    $ loot2 += 1
                    $ loot3 += 1
                    $ loot4 += 1
                    $ loot5 += 1
                    play sound "audio/sfx/jobReward.mp3"
                    show dropMats at item_drop((550,300))
                    pause 0.3
                    play sound "audio/sfx/jobReward.mp3"
                    show dropConsum at item_drop((550,300))
                    with d3
                    jump task23


            if missionSetting == "Faire" and specialMuffyStatus == 1:
                $ randomBossHP -= 1
                hide obstMuffy
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstMuffy:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    muff "You've got spunk! Chase after me if you dare."
                    hide obstMuffy with d3
                    $ randomBoss = 0
                    if activeSpy == 1:
                        sM "She's getting away!"
                        sM "Should we pursue her or pull back?"
                    if activeSpy == 2:
                        cM "She's getting away!"
                        cM "Should we pursue her or pull back?"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        aM "Should we pursue her or pull back?"
                    hide spyCombat2 with d1
                    menu:
                        "Pursue the target" if True:
                            $ missionProgression = 7
                            jump missionBegin
                        "Pull back for now" if True:
                            y "We'll get 'em next time."
                            hide screen equipmentMenu
                            $ randomBoss = 0
                            hide spyCombat1
                            with d3
                            $ loot1 += 1
                            $ loot5 += 1
                            play sound "audio/sfx/jobReward.mp3"
                            show dropMats at item_drop((550,300))
                            pause 0.3
                            play sound "audio/sfx/jobReward.mp3"
                            show dropConsum at item_drop((550,300))
                            with d3
                            pause 0.5
                            call threatNeutralized from _call_threatNeutralized_5
                            jump missionComplete
                elif randomBossHP <= 0:
                    $ specialMuffyStatus = 2
                    $ specialBossActive = False
                    show obstMuffy:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    $ prisonersNew = True
                    muff "Ow... not so rough!"
                    muff "Fine, take me in. I won't resist."
                    hide obstMuffy
                    hide spyCombat2
                    hide screen equipmentMenu
                    $ randomBoss = 0
                    hide spyCombat1
                    with d3
                    $ loot1 += 1
                    $ loot2 += 1
                    $ loot3 += 1
                    $ loot5 += 1
                    play sound "audio/sfx/jobReward.mp3"
                    show dropMats at item_drop((550,300))
                    pause 0.3
                    play sound "audio/sfx/jobReward.mp3"
                    show dropConsum at item_drop((550,300))
                    with d3
                    pause 0.5
                    call threatNeutralized from _call_threatNeutralized_6
                    jump missionComplete

            if missionSetting == "Faire" and specialFelicityStatus == 1 and task21Stage == 6:
                $ randomBossHP -= 1
                hide obstFelicity
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstFelicity:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    feli "Eeewwww, get away from me uggo!"
                    hide obstFelicity with d3
                    $ randomBoss = 0
                    if activeSpy == 1:
                        sM "She's getting away!"
                        sM "Should we pursue her or pull back?"
                    if activeSpy == 2:
                        cM "She's getting away!"
                        cM "Should we pursue her or pull back?"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        aM "Should we pursue her or pull back?"
                    hide spyCombat2 with d1
                    menu:
                        "Pursue the target" if True:
                            $ missionProgression = 7
                            jump missionBegin
                        "Pull back for now" if True:
                            y "We'll get 'em next time."
                            hide screen equipmentMenu
                            $ randomBoss = 0
                            hide spyCombat1
                            with d3
                            $ loot1 += 1
                            $ loot5 += 1
                            play sound "audio/sfx/jobReward.mp3"
                            show dropMats at item_drop((550,300))
                            pause 0.3
                            play sound "audio/sfx/jobReward.mp3"
                            show dropConsum at item_drop((550,300))
                            with d3
                            pause 0.5
                            call threatNeutralized from _call_threatNeutralized_10
                            jump missionComplete
                elif randomBossHP <= 0:
                    $ specialFelicityStatus = 2
                    $ specialBossActive = False
                    show obstFelicity:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.5
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    pause 0.4
                    $ prisonersNew = True
                    feli "Okay okay! No need to get rough!"
                    feli "Do I still get to keep my man servant in jail...?"
                    hide obstFelicity
                    hide spyCombat2
                    hide screen equipmentMenu
                    $ randomBoss = 0
                    hide spyCombat1
                    with d3
                    $ loot1 += 1
                    $ loot2 += 1
                    $ loot3 += 1
                    $ loot5 += 1
                    play sound "audio/sfx/jobReward.mp3"
                    show dropMats at item_drop((550,300))
                    pause 0.3
                    play sound "audio/sfx/jobReward.mp3"
                    show dropConsum at item_drop((550,300))
                    with d3
                    pause 0.5
                    call threatNeutralized from _call_threatNeutralized_11
                    jump missionComplete

            if missionSetting == "WOOHP" and task26Stage == 9:
                $ randomBossHP -= 1
                hide obstBritney
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show expression "mission/models/brit/britCombat2.png":
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.48
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    brit "Gotcha now~..."
                    play sound "audio/sfx/punch1.mp3"
                    hide spyCombat2
                    hide expression "mission/models/brit/britCombat2.png"
                    show expression "mission/models/brit/britCombat3.png":
                        xalign 0.50 yalign 0.4 zoom 0.54 xzoom -1
                    show spyHit:
                        xalign 0.39 yalign 0.4 zoom 0.42 xzoom -1
                        linear 0.3 xalign 0.377 yalign 0.38
                    with d1
                    pause 0.4
                    hide spyHit
                    hide expression "mission/models/brit/britCombat3.png"
                    with d2
                    call spyHitBackup from _call_spyHitBackup_18
                    if activeSpy == 1:
                        sM "She's getting away!"
                        sM "Should we pursue her or pull back?"
                    if activeSpy == 2:
                        cM "She's getting away!"
                        cM "Should we pursue her or pull back?"
                    if activeSpy == 3:
                        aM "She's getting away!"
                        aM "Should we pursue her or pull back?"
                    menu:
                        "Pursue the target" if True:
                            $ missionProgression = 7
                            jump missionBegin
                        "Pull back for now" if True:
                            y "We'll get 'em next time."
                            hide screen equipmentMenu
                            $ randomBoss = 0
                            hide spyCombat1
                            with d3
                            $ loot1 += 1
                            $ loot5 += 1
                            play sound "audio/sfx/jobReward.mp3"
                            show dropMats at item_drop((550,300))
                            pause 0.3
                            play sound "audio/sfx/jobReward.mp3"
                            show dropConsum at item_drop((550,300))
                            with d3
                            pause 0.5
                            call threatNeutralized from _call_threatNeutralized_12
                            jump missionComplete
                elif randomBossHP <= 0:
                    $ specialBossActive = False
                    show expression "mission/models/brit/britCombat4.png":
                        xalign 0.505 yalign 0.455 zoom 0.47
                        linear 0.28 xalign 0.519 yalign 0.456
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.7
                    hide expression "mission/models/brit/britCombat4.png"
                    hide spyCombat2
                    with d5
                    brit "I... give... up..."
                    $ britCaptured = True
                    pause 1.0
                    call threatNeutralized from _call_threatNeutralized_13
                    jump missionComplete

            if missionSetting == "WOOHP" and task26Stage == 14:
                $ randomBossHP -= 1
                hide obstTim1
                play sound "audio/sfx/punch1.mp3"
                if randomBossHP >= 1:
                    show obstTim2:
                        xalign 0.50 yalign 0.48 rotate 3 zoom 0.48
                        linear 0.12 xalign 0.505
                        linear 0.12 xalign 0.495
                        linear 0.12 xalign 0.50
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.35
                    tim "Heads up...!"
                    play sound "audio/sfx/punch1.mp3"
                    hide spyCombat2
                    hide obstTim2
                    show obstTim3:
                        xalign 0.50 yalign 0.42 zoom 0.5
                    show spyHit:
                        xalign 0.39 yalign 0.39 zoom 0.42 xzoom -1
                        linear 0.3 xalign 0.367 yalign 0.38
                    show expression "mission/fx/net.png":
                        xalign 0.39 yalign 0.39 zoom 0.6 xzoom -1
                        linear 0.3 xalign 0.367 yalign 0.38
                    with d1
                    pause 0.4
                    hide spyHit
                    hide obstTim3
                    hide expression "mission/fx/net.png"
                    with d2
                    call spyHitBackup from _call_spyHitBackup_19
                    if activeSpy == 1:
                        sM "He's getting away!"
                        y "After him!"
                    if activeSpy == 2:
                        cM "He's getting away!"
                        y "After him!"
                    if activeSpy == 3:
                        aM "He's getting away!"
                        y "After him!"
                    $ missionProgression = 7
                    jump missionBegin
                elif randomBossHP <= 0:
                    hide screen equipmentMenu
                    $ specialBossActive = False
                    show obstTim4:
                        xalign 0.51 yalign 0.465 zoom 0.46
                        linear 0.25 xalign 0.519 yalign 0.456
                    show spyCombat2:
                        xalign 0.41 yalign 0.52 zoom 0.43
                    pause 0.7
                    hide obstTim4
                    hide spyCombat2
                    with d5
                    tim "A little help here..."
                    $ task26Stage = 15
                    pause 0.8
                    scene black with fade
                    jump task26

        if randomBoss == 1:
            $ randomBossHP -= 1
            hide obstHulk
            play sound "audio/sfx/punch1.mp3"
            if randomBossHP >= 1:
                show obstHulkBlock:
                    xalign 0.50 yalign 0.40 zoom 0.52
                    linear 0.12 xalign 0.505
                    linear 0.12 xalign 0.495
                    linear 0.12 xalign 0.50
            if randomBossHP <= 0:
                play sound "audio/sfx/defeatEnemy.mp3"
                show obstHulkHit:
                    xalign 0.50 yalign 0.415 zoom 0.52
                    linear 0.3 xalign 0.50 yalign 0.39
            show spyCombat1:
                xalign 0.37 yalign 0.41 zoom 0.46
                linear 0.5 yalign 0.36
            $ renpy.pause(0.5, hard='True')
            hide obstHulkBlock
            if randomBossHP <= 0:
                hide screen equipmentMenu
                $ randomBoss = 0
                hide spyCombat1
                hide obstHulkHit
                with d3
                $ loot1 += 1
                $ loot5 += 1
                play sound "audio/sfx/jobReward.mp3"
                show dropMats at item_drop((550,300))
                pause 0.3
                play sound "audio/sfx/jobReward.mp3"
                show dropConsum at item_drop((550,300))
                with d3
                pause 0.5
                if 30 <= task26Stage <= 32:
                    $ missionProgression = 7
                    $ randomBoss = 1
                    jump task26
                call threatNeutralized from _call_threatNeutralized_7
                jump missionComplete
            elif True:
                show obstHulk:
                    xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                with d3
                hide obstHulk
                play sound "audio/sfx/punch1.mp3"
                show obstHulkAttack:
                    xalign 0.5 yalign 0.45 zoom 0.53 rotate 3
                $ spyBlockChance = renpy.random.randint(1, 10)

                if task2Stage == 9:
                    $ spyBlockChance = 10

                if spyBlockChance >= 6:
                    hide spyCombat1
                    with d1
                    show spyGuard2:
                        xalign 0.35 yalign 0.57 zoom 0.44 rotate 3
                        linear 0.1 xalign 0.355
                        linear 0.1 xalign 0.35
                        linear 0.1 xalign 0.355
                        linear 0.1 xalign 0.35
                    with d2
                    pause 0.4
                    hide obstHulkAttack
                    show obstHulk:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    hide spyGuard2
                    show spyGuard2:
                        xalign 0.35 yalign 0.57 zoom 0.44 rotate 3
                    with d2
                    call screen interactScreen
                elif True:
                    hide spyCombat1
                    hide spyCombat2
                    hide spyCombat3
                    call reduceHealth from _call_reduceHealth_8
                    show spyHit:
                        xalign 0.38 yalign 0.4 zoom 0.35 xzoom -1
                        linear 0.3 xalign 0.377 yalign 0.38
                    pause 0.3
                    hide spyHit
                    with d2
                    hide obstHulkAttack
                    show obstHulk:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    with d3
                    call spyHitBackup from _call_spyHitBackup_8




label hideInteract:
    hide obst1
    hide obst2
    hide obst3
    hide obst4
    hide interact1
    hide interact2
    return

label showInteract:
    if 1 <= randomBackground <= 3:
        if randomObst2 == 1:
            show obst2:
                xalign 0.65 yalign 0.80 rotate 2 zoom 0.45
    return





label coverInteract:
    if 1 <= randomBackground <= 3:
        if currentPosition == 0:
            $ disableScreen = True
            hide spyCorner
            show jumpGraphic:
                xalign 0.75 yalign 0.87
            pause 0.07
            hide jumpGraphic
            with d1
            call hideInteract from _call_hideInteract
            if missionSetting == "School":

                if interact2 == 8:
                    play sound "audio/sfx/alarm1.mp3"
                    show cameraTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    if hiddenStatus > 2:
                        $ hiddenStatus = 2
                    pause 1.2
                    $ obst2FoV = 1
                    $ CoS2 -= 25
                    hide cameraTrigger
                    with d1

                if randomObst1 == 2 and hackPart >= 3:
                    play sound "audio/sfx/alarm1.mp3"
                    show lazerTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    if hiddenStatus > 2:
                        $ hiddenStatus = 2
                    pause 1.2
                    $ obst2FoV = 1
                    $ CoS2 -= 25
                    hide lazerTrigger
                    with d1
                show globalImage:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45
            if missionSetting == "Castle":

                if interact2 == 8:
                    play sound "audio/sfx/alarm1.mp3"
                    show cameraTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    if hiddenStatus > 2:
                        $ hiddenStatus = 2
                    pause 1.2
                    $ obst2FoV = 1
                    $ CoS2 -= 25
                    hide cameraTrigger
                    with d1

                if randomObst1 == 2 and hackPart >= 3:
                    play sound "audio/sfx/alarm1.mp3"
                    show lazerTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    if hiddenStatus > 2:
                        $ hiddenStatus = 2
                    pause 1.2
                    $ obst2FoV = 1
                    $ CoS2 -= 25
                    hide lazerTrigger
                    with d1
                show globalImageCastle:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45

                if randomObst1 == 2 and hackPart >= 3:
                    play sound "audio/sfx/alarm1.mp3"
                    show lazerTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    if hiddenStatus > 2:
                        $ hiddenStatus = 2
                    pause 1.2
                    $ obst2FoV = 1
                    $ CoS2 -= 25
                    hide lazerTrigger
                    with d1
                show globalImageDatabase:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45

            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45

                if randomObst1 == 2 and hackPart >= 3:
                    play sound "audio/sfx/alarm1.mp3"
                    show lazerTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    if hiddenStatus > 2:
                        $ hiddenStatus = 2
                    pause 1.2
                    $ obst2FoV = 1
                    $ CoS2 -= 25
                    hide lazerTrigger
                    with d1
                show globalImageFaire:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45

            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45


                if randomObst1 == 2 and hackPart >= 3:
                    play sound "audio/sfx/alarm1.mp3"
                    show lazerTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    if hiddenStatus > 2:
                        $ hiddenStatus = 2
                    pause 1.2
                    $ obst2FoV = 1
                    $ CoS2 -= 25
                    hide lazerTrigger
                    with d1
                show globalImageWOOHP:
                    linear 0.15 xalign 0.55 yalign 0.24 zoom 0.45

            pause 0.15
            call showInteract from _call_showInteract
            $ currentPosition = 1
            show spyCrouchCorner:
                xalign -0.08 yalign 0.85 rotate 7 zoom 0.40
            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 1:
            $ disableScreen = True
            hide spyCrouchCorner
            show jumpGraphic:
                xalign 0.25 yalign 0.85
            pause 0.1
            hide jumpGraphic
            with d1
            if missionSetting == "School":
                show globalImage:
                    linear 0.15 xalign 0.68 yalign 0.45 zoom 0.90
                pause 0.15
                $ currentPosition = 2
                show spyCrouchCorner:
                    xalign 0.93 yalign 1.3 rotate 12 zoom 0.48 xzoom -1
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.15 xalign 0.68 yalign 0.45 zoom 0.90
                pause 0.15
                $ currentPosition = 2
                show spyCrouchCorner:
                    xalign 0.93 yalign 1.3 rotate 12 zoom 0.42 xzoom -1
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.15 xalign 0.68 yalign 0.45 zoom 0.90
                pause 0.15
                $ currentPosition = 2
                show spyCrouchCorner:
                    xalign 0.93 yalign 1.3 rotate 12 zoom 0.42 xzoom -1
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.15 xalign 0.68 yalign 0.45 zoom 0.90
                pause 0.15
                $ currentPosition = 2
                show spyCrouchCorner:
                    xalign 0.93 yalign 1.3 rotate 12 zoom 0.42 xzoom -1
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.15 xalign 0.68 yalign 0.45 zoom 0.90
                pause 0.15
                $ currentPosition = 2
                show spyCrouchCorner:
                    xalign 0.93 yalign 1.3 rotate 12 zoom 0.42 xzoom -1
            if bonusAvailable >= 1:
                play sound "audio/sfx/jobReward.mp3"
                $ bonusAvailable = 0
                $ loot1 += 1
                $ loot5 += 1
                show dropMats at item_drop((950,600))
                pause 0.25
                play sound "audio/sfx/jobReward.mp3"
                show dropConsum at item_drop((950,600))
            $ disableScreen = False
            jump jumpStartScene

    elif 4 <= randomBackground <= 7:
        if currentPosition == 0:
            $ disableScreen = True
            hide spyCornerSide
            show jumpGraphic:
                xalign 0.93 yalign 0.91
            pause 0.07
            hide jumpGraphic
            with d1
            call hideInteract from _call_hideInteract_1
            if missionSetting == "School":
                show globalImage:
                    linear 0.35 xalign 0.5 yalign 0.75 zoom 0.36
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.35 xalign 0.5 yalign 0.75 zoom 0.36
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.35 xalign 0.5 yalign 0.75 zoom 0.36
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.35 xalign 0.5 yalign 0.75 zoom 0.36
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.35 xalign 0.5 yalign 0.75 zoom 0.36
            pause 0.35
            call showInteract from _call_showInteract_1
            $ currentPosition = 1





            show spyCornerSide:
                xalign 0.875 yalign 0.90 zoom 0.39

            $ randomDirection = renpy.random.randint(1, 2)
            if hiddenStatus == 2:
                $ randomDirection = 1
            if randomDirection == 1:
                show obst2:
                    xalign 0.05 yalign 0.99 zoom 0.49
            if randomDirection == 2:
                show obst2:
                    xalign 0.05 yalign 0.99 zoom 0.49 xzoom -1

            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 1:
            $ disableScreen = True
            hide spyCornerSide
            show jumpGraphic:
                xalign 0.79 yalign 0.91
            pause 0.07
            hide jumpGraphic
            with d1
            call hideInteract from _call_hideInteract_2
            if missionSetting == "School":
                show globalImage:
                    linear 0.15 xalign 0.0
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.15 xalign 0.0
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.15 xalign 0.0
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.15 xalign 0.0
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.15 xalign 0.0
            pause 0.15
            call showInteract from _call_showInteract_2
            $ currentPosition = 2
            show spyCrouchingSide:
                xalign 0.72 yalign 0.986 zoom 0.27 rotate 5 xzoom -1
            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 2:
            $ disableScreen = True
            hide spyCrouchingSide
            show jumpGraphic:
                xalign 0.99 yalign 0.80
            pause 0.07
            hide jumpGraphic
            with d1
            call hideInteract from _call_hideInteract_3
            if missionSetting == "School":
                show globalImage:
                    linear 0.15 xalign 0.80 yalign 0.0 zoom 0.35
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.15 xalign 0.80 yalign 0.0 zoom 0.35
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.15 xalign 0.80 yalign 0.0 zoom 0.35
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.15 xalign 0.80 yalign 0.0 zoom 0.35
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.15 xalign 0.80 yalign 0.0 zoom 0.35
            pause 0.15
            call showInteract from _call_showInteract_3
            $ currentPosition = 3





            $ randomDirection = renpy.random.randint(1, 2)
            if hiddenStatus == 2:
                $ randomDirection = 2
            if randomDirection == 1:
                show obst3:
                    xalign 0.77 yalign 0.58 zoom 0.42
            elif True:
                show obst3:
                    xalign 0.77 yalign 0.58 zoom 0.42 xzoom -1
            show spyCornerSide:
                xalign 0.497 yalign 0.59 zoom 0.37 xzoom -1
            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 3:
            $ disableScreen = True
            hide spyCornerSide
            show jumpGraphic:
                xalign 0.01 yalign 0.505
            pause 0.07
            hide jumpGraphic
            with d1
            call hideInteract from _call_hideInteract_4
            if missionSetting == "School":
                show globalImage:
                    linear 0.15 xalign 0.0 yalign 0.0 zoom 0.35
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.15 xalign 0.0 yalign 0.0 zoom 0.35
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.15 xalign 0.0 yalign 0.0 zoom 0.35
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.15 xalign 0.0 yalign 0.0 zoom 0.35
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.15 xalign 0.0 yalign 0.0 zoom 0.35
            pause 0.15
            call showInteract from _call_showInteract_4
            $ currentPosition = 4
            show obst4:
                xalign 0.12 yalign 0.115 zoom 0.32
            show spyCornerSide:
                xalign 0.46 yalign 0.16 zoom 0.27
            $ disableScreen = False
            jump jumpStartScene

    elif 8 <= randomBackground <= 10:
        if currentPosition == 0:
            $ disableScreen = True
            hide spyCorner
            show jumpGraphic:
                xalign 0.88 yalign 0.93
            pause 0.07
            hide jumpGraphic
            with d1
            call hideInteract from _call_hideInteract_5
            if missionSetting == "School":
                show globalImage:
                    linear 0.20 xalign 0.55 yalign 0.40 zoom 0.65
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.20 xalign 0.55 yalign 0.40 zoom 0.65
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.20 xalign 0.55 yalign 0.40 zoom 0.65
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.20 xalign 0.55 yalign 0.40 zoom 0.65
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.20 xalign 0.55 yalign 0.40 zoom 0.65
            pause 0.15
            call showInteract from _call_showInteract_5
            $ currentPosition = 1
            show obst3:
                xalign 0.60 yalign 0.50 zoom 0.45
            show spyCrouchCorner:
                xalign 1.0 yalign 1.4 rotate 0.6 zoom 0.48 xzoom -1
            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 1:
            $ disableScreen = True
            hide spyCrouchCorner
            if randomObst3 >= 1:
                hide obst3
            show jumpGraphic:
                xalign 0.78 yalign 1.0
            pause 0.1
            hide jumpGraphic
            with d1
            if missionSetting == "School":
                show globalImage:
                    linear 0.20 xalign 0.60 yalign 0.40 zoom 1.05
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.20 xalign 0.60 yalign 0.40 zoom 1.05
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.20 xalign 0.60 yalign 0.40 zoom 1.05
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.20 xalign 0.60 yalign 0.40 zoom 1.05
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.20 xalign 0.60 yalign 0.40 zoom 1.05
            pause 0.15
            $ currentPosition = 2
            if randomObst3 >= 1:
                show obst3:
                    xalign 0.5 yalign 0.62 zoom 0.65
            show spyCrouchCorner:
                xalign -0.1 yalign 1.5 rotate -3 zoom 0.52
            if bonusAvailable >= 1:
                play sound "audio/sfx/jobReward.mp3"
                $ bonusAvailable = 0
                $ loot1 += 1
                $ loot5 += 1
                show dropMats at item_drop((950,600))
                pause 0.25
                play sound "audio/sfx/jobReward.mp3"
                show dropConsum at item_drop((950,600))
            $ disableScreen = False
            jump jumpStartScene

    elif 11 <= randomBackground <= 11:
        if currentPosition == 0:
            $ disableScreen = True
            hide spyCorner
            show jumpGraphic:
                xalign 1.0 yalign 1.0
            pause 0.07
            hide jumpGraphic
            with d1
            call showInteract from _call_showInteract_6
            $ currentPosition = 1
            show spyCrouchCorner:
                xalign 0.2 yalign 1.1 rotate -5 zoom 0.39
            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 1:
            $ disableScreen = True
            hide spyCrouchCorner
            show jumpGraphic:
                xalign 0.7 yalign 0.9
            pause 0.07
            hide jumpGraphic
            with d1
            pause 0.15
            if missionSetting == "School":
                show globalImage:
                    linear 0.4 yalign 1.0
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.4 yalign 1.0
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.4 yalign 1.0
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.4 yalign 1.0
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.4 yalign 1.0
            pause 0.8
            $ currentPosition = 2
            show jumpGraphic:
                xalign 1.0 yalign 0.85

            if randomObst3 == 1 and currentPosition == 2:
                show obst3:
                    xalign 0.57 yalign 0.44 zoom 0.2

            if randomObst2 == 1 and currentPosition == 2:
                show obst2:
                    xalign 0.53 yalign 0.66 zoom 0.48
            pause 0.15
            hide jumpGraphic
            call showInteract from _call_showInteract_7
            show spyCrouchCorner:
                xalign 0.96 yalign 1.1 rotate 5 zoom 0.39 xzoom -1
            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 2:
            hide obst3
            $ disableScreen = True
            hide spyCrouchCorner
            $ currentPosition = 3
            show jumpGraphic:
                xalign 0.77 yalign 0.93
            pause 0.15
            hide jumpGraphic
            if missionSetting == "School":
                show globalImage:
                    linear 0.3 xalign 0.5 yalign 0.9 zoom 1.0
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.3 xalign 0.5 yalign 0.9 zoom 1.0
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.3 xalign 0.5 yalign 0.9 zoom 1.0
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.3 xalign 0.5 yalign 0.9 zoom 1.0
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.3 xalign 0.5 yalign 0.9 zoom 1.0
            pause 0.3
            show obst3:
                xalign 0.64 yalign 0.3 zoom 0.4 xzoom -1
            hide jumpGraphic
            call showInteract from _call_showInteract_8
            show spyCrouchCorner:
                xalign 0.23 yalign 0.84 rotate -5 zoom 0.38
            $ disableScreen = False
            jump jumpStartScene
        if currentPosition == 3:
            $ disableScreen = True
            hide spyCrouchCorner
            $ currentPosition = 4
            show jumpGraphic:
                xalign 0.5 yalign 0.75
            pause 0.15
            hide jumpGraphic
            if missionSetting == "School":
                show globalImage:
                    linear 0.2 xalign 0.6 yalign 0.83 zoom 1.8
            if missionSetting == "Castle":
                show globalImageCastle:
                    linear 0.2 xalign 0.6 yalign 0.83 zoom 1.8
            if missionSetting == "Database":
                show globalImageDatabase:
                    linear 0.2 xalign 0.6 yalign 0.83 zoom 1.8
            if missionSetting == "Faire":
                show globalImageFaire:
                    linear 0.2 xalign 0.6 yalign 0.83 zoom 1.8
            if missionSetting == "WOOHP":
                show globalImageWOOHP:
                    linear 0.2 xalign 0.6 yalign 0.83 zoom 1.8
            pause 0.3
            hide jumpGraphic
            call showInteract from _call_showInteract_9
            show spyCrouchCorner:
                xalign 0.77 yalign 1.08 rotate 5 zoom 0.42 xzoom -1
            $ disableScreen = False
            jump jumpStartScene




default interSelect = 0
default hackResult = 0
default hackAvail = True
default hackFailed = False

label interInteract:
    if 1 <= randomBackground <= 3:
        if interSelect == 1:
            if gadgetGunActive:
                call spyShootHigh from _call_spyShootHigh
                jump jumpStartScene
            elif True:
                "It looks like this can be shot down with the proper equipment."
                jump jumpStartScene
        if interSelect == 2:
            if hackPart >= 3:
                if activeSpy == 1:
                    play sound "audio/voice/illCrippleTheirFacilities.mp3"
                if activeSpy == 2:
                    play sound "audio/voice/clover/hackingEngaged.mp3"
                if activeSpy == 3:
                    play sound "audio/voice/alex/hackingIntoTheirSystems.mp3"
                show screen spyHacking
                with fade
                $ randomHack = renpy.random.randint(1,4)

                if randomHack == 1:
                    while hackResult < 100:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 2:
                    while hackResult < 91:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 3:
                    while hackResult < 76:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 4:
                    while hackResult < 55:
                        $ hackResult += 1
                        pause 0.003
                if wormUpgrade and hackResult:
                    $ hackAvail = False
                    "Hacking Worm activated."
                    $ hackResult += 15
                pause
                if hackResult >= 100:
                    if activeSpy == 1:
                        play sound "audio/voice/imIn.mp3"
                    if activeSpy == 2:
                        play sound "audio/voice/clover/imIn.mp3"
                    if activeSpy == 3:
                        play sound "audio/voice/alex/imIn.mp3"
                    "Hack succesful. Camera disabled."
                    hide screen spyHacking with fade
                    play sound "audio/sfx/shoot1.mp3"
                    show hackCloud at hackCloud:
                        xalign 0.7 ypos 180 zoom 0.7
                    pause 0.7
                    $ obst1FoV = 3
                    $ CoS1 += 10
                    $ obst2FoV = 3
                    $ CoS2 += 10
                    $ hackResult = 0
                    $ interact2 = 8.1
                    jump jumpStartScene
                elif True:
                    "Hack failed."
                    hide screen spyHacking with fade
                    play sound "audio/sfx/alarm1.mp3"
                    show cameraTrigger:
                        xalign 0.5 yalign 0.0
                    with d1
                    $ hiddenStatus += 1
                    $ CoS1 -= 10
                    $ CoS2 -= 10
                    pause 0.5
                    hide cameraTrigger
                    with d1
                    jump jumpStartScene
                jump jumpStartScene
            elif True:
                "It looks like this device can be hacked with the proper gadget."
                jump jumpStartScene
        if interSelect == 3:
            if hackPart >= 3:
                if activeSpy == 1:
                    play sound "audio/voice/illCrippleTheirFacilities.mp3"
                if activeSpy == 2:
                    play sound "audio/voice/clover/hackingEngaged.mp3"
                if activeSpy == 3:
                    play sound "audio/voice/alex/hackingIntoTheirSystems.mp3"
                show screen spyHacking
                with fade
                $ randomHack = renpy.random.randint(1,4)

                if randomHack == 1:
                    while hackResult < 100:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 2:
                    while hackResult < 91:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 3:
                    while hackResult < 76:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 4:
                    while hackResult < 55:
                        $ hackResult += 1
                        pause 0.003
                if wormUpgrade and hackResult <= 100 and hackAvail:
                    $ hackAvail = False
                    "Hacking Worm activated."
                    $ hackResult += 15
                pause
                if hackResult >= 100:
                    $ randomObst1 = 0
                    if activeSpy == 1:
                        play sound "audio/voice/imIn.mp3"
                    if activeSpy == 2:
                        play sound "audio/voice/clover/imIn.mp3"
                    if activeSpy == 3:
                        play sound "audio/voice/alex/imIn.mp3"
                    "Hack succesful. Laser disabled."
                    hide screen spyHacking with fade
                    play sound "audio/sfx/shoot1.mp3"
                    show hackCloud at hackCloud:
                        xalign 0.15 yalign 0.5 zoom 0.7
                    pause 0.7
                    $ hackResult = 0
                    jump jumpStartScene
                elif True:
                    "Hack failed."
                    hide screen spyHacking with fade
                    with d1
                    jump jumpStartScene
                jump jumpStartScene
            elif True:
                "It looks like this device can be hacked with the proper gadget."
                jump jumpStartScene
    if 4 <= randomBackground <= 7:
        if interSelect == 1:
            if gadgetGunActive:
                call spyShootHigh from _call_spyShootHigh_1
                jump jumpStartScene
            elif True:
                "It looks like this can be shot down with the proper equipment."
                jump jumpStartScene
        if interSelect == 2:
            call spyShootHigh from _call_spyShootHigh_3
        if interSelect == 3:
            call spyShootHigh from _call_spyShootHigh_4

        if interSelect == 10:
            if hackPart >= 3:
                if activeSpy == 1:
                    play sound "audio/voice/illCrippleTheirFacilities.mp3"
                if activeSpy == 2:
                    play sound "audio/voice/clover/hackingEngaged.mp3"
                if activeSpy == 3:
                    play sound "audio/voice/alex/hackingIntoTheirSystems.mp3"
                show screen spyHacking
                with fade
                $ randomHack = renpy.random.randint(1,4)

                if randomHack == 1:
                    while hackResult < 100:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 2:
                    while hackResult < 91:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 3:
                    while hackResult < 76:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 4:
                    while hackResult < 55:
                        $ hackResult += 1
                        pause 0.003
                pause
                if hackResult >= 100:
                    if activeSpy == 1:
                        play sound "audio/voice/imIn.mp3"
                    if activeSpy == 2:
                        play sound "audio/voice/clover/imIn.mp3"
                    if activeSpy == 3:
                        play sound "audio/voice/alex/imIn.mp3"
                    "Hack succesful."
                    hide screen spyHacking with fade
                    if interSelect == 1:
                        play sound "audio/sfx/shoot1.mp3"
                        show hackCloud at hackCloud:
                            xalign 0.7 ypos 180 zoom 0.7
                        pause 0.7
                        $ obst1FoV = 3
                        $ CoS1 += 10
                        $ obst2FoV = 3
                        $ CoS2 += 10
                        jump jumpStartScene
                    elif interSelect == 10:
                        $ hackResult = 0


                        if task15Music == False and missionSetting == _("Database"):
                            $ task15Music = True
                            if task15Fireworks == False:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n-Plan a mission to the Abandoned Amusement Park and steal fireworks.\n{color=#A3A3A3}-Plan a mission to Punk Web and steal the hottest mixtape.{/color}\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            if task15Fireworks == True:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n{color=#A3A3A3}-Plan a mission to the Abandoned Amusement Park and steal fireworks.{/color}\n{color=#A3A3A3}-Plan a mission to Punk Web and steal the hottest mixtape.{/color}\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the music you need for the party!"
                            menu:
                                "Continue mission" if True:
                                    hide screen spyHacking with fade
                                    jump jumpStartScene
                                "Pull out" if True:
                                    jump missionComplete
                        if task15Fireworks == False and missionSetting == _("Faire"):
                            $ task15Fireworks = True
                            if task15Music == False:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n{color=#A3A3A3}-Plan a mission to the Abandoned Amusement Park and steal fireworks.{/color}\n-Plan a mission to Punk Web and steal the hottest mixtape.\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            if task15Music == True:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n{color=#A3A3A3}-Plan a mission to the Abandoned Amusement Park and steal fireworks.{/color}\n{color=#A3A3A3}-Plan a mission to Punk Web and steal the hottest mixtape.{/color}\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the fireworks you need for the party!"
                            menu:
                                "Continue mission" if True:
                                    hide screen spyHacking with fade
                                    jump jumpStartScene
                                "Pull out" if True:
                                    jump missionComplete

                        if acesBounty3 == 1 and missionSetting == _("School"):
                            $ acesBounty3 = 2
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the upcoming test answers."
                            jump jumpStartScene
                        if acesBounty2 == 1 and missionSetting == "Faire":
                            $ acesBounty2 = 2
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the Outsiders stash of grafitti."
                            jump jumpStartScene
                        if acesBounty1 == 1 and missionSetting == "Database":
                            $ acesBounty1 = 2
                            play sound "audio/sfx/itemGot.mp3"
                            "You find Drift Punk's hacking codes."
                            jump jumpStartScene
                elif True:
                    "Hack failed. Magnetic lock activated."
                    $ hackFailed = True
                    hide screen spyHacking with fade
                    jump jumpStartScene
            elif True:
                "It looks like this device can be hacked with the proper gadget."
                jump jumpStartScene
    if 8 <= randomBackground <= 10:
        if interSelect == 1:
            if gadgetGunActive:
                call spyShootHigh from _call_spyShootHigh_2
                jump jumpStartScene
            elif True:
                "It looks like this can be shot down with the proper equipment."
                jump jumpStartScene
        if interSelect == 2:
            ""
        if interSelect == 3:
            if gadgetGunActive == True:
                hide spyCornerSide
                with d2
                show spyShootSideUp:
                    xalign 0.465 yalign 0.6 zoom 0.38
                with d2
                "gunsound effect"
                $ interact3 = 0
                show light1Anim:
                    xalign 1.0 yalign 0.0 zoom 0.952
                    linear 0.05 xalign 1.01
                    pause 0.05
                    linear 0.05 xalign 0.99
                    pause 0.05
                    linear 0.05 xalign 1.01
                    pause 0.05
                    linear 0.05 xalign 0.99
                    pause 0.05
                    linear 0.05 xalign 1.0
                    pause 0.1
                    linear 0.23 yalign 0.80
                pause 0.68
                if randomObst3 >= 1:
                    show agentHit:
                        xalign 0.755 yalign 0.58 zoom 0.4
                    play sound "audio/sfx/defeatEnemy.mp3"
                hide light1Anim
                hide obst3
                $ randomObst3 = 0
                pause 0.3
                hide agentHit
                with d1
                hide spyShootSideUp
                $ lootLoc = 3
                call randomLoot from _call_randomLoot_12
                show spyCornerSide:
                    xalign 0.497 yalign 0.59 zoom 0.40 xzoom -1
                jump jumpStartScene
            elif True:
                "It looks like this can be shot down with the appropriate gadget."
                jump jumpStartScene

        if interSelect == 10:
            if hackPart >= 3:
                if activeSpy == 1:
                    play sound "audio/voice/illCrippleTheirFacilities.mp3"
                if activeSpy == 2:
                    play sound "audio/voice/clover/hackingEngaged.mp3"
                if activeSpy == 3:
                    play sound "audio/voice/alex/hackingIntoTheirSystems.mp3"
                show screen spyHacking
                with fade
                $ randomHack = renpy.random.randint(1,4)

                if randomHack == 1:
                    while hackResult < 100:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 2:
                    while hackResult < 91:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 3:
                    while hackResult < 76:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 4:
                    while hackResult < 55:
                        $ hackResult += 1
                        pause 0.003
                pause
                if hackResult >= 100:
                    if activeSpy == 1:
                        play sound "audio/voice/imIn.mp3"
                    if activeSpy == 2:
                        play sound "audio/voice/clover/imIn.mp3"
                    if activeSpy == 3:
                        play sound "audio/voice/alex/imIn.mp3"
                    "Hack succesful."
                    hide screen spyHacking with fade
                    if interSelect == 1:
                        play sound "audio/sfx/shoot1.mp3"
                        show hackCloud at hackCloud:
                            xalign 0.7 ypos 180 zoom 0.7
                        pause 0.7
                        $ obst1FoV = 3
                        $ CoS1 += 10
                        $ obst2FoV = 3
                        $ CoS2 += 10
                        jump jumpStartScene
                    elif interSelect == 10:
                        $ hackResult = 0


                        if task15Music == False and missionSetting == "Database":
                            $ task15Music = True
                            if task15Fireworks == False:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n-Plan a mission to the Abandoned Amusement Park and steal fireworks.\n{color=#A3A3A3}-Plan a mission to Punk Web and steal the hottest mixtape.{/color}\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            if task15Fireworks == True:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n{color=#A3A3A3}-Plan a mission to the Abandoned Amusement Park and steal fireworks.{/color}\n{color=#A3A3A3}-Plan a mission to Punk Web and steal the hottest mixtape.{/color}\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the music you need for the party!"
                            menu:
                                "Continue mission" if True:
                                    hide screen spyHacking with fade
                                    jump jumpStartScene
                                "Pull out" if True:
                                    jump missionComplete
                        if task15Fireworks == False and missionSetting == "Faire":
                            $ task15Fireworks = True
                            if task15Music == False:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n{color=#A3A3A3}-Plan a mission to the Abandoned Amusement Park and steal fireworks.{/color}\n-Plan a mission to Punk Web and steal the hottest mixtape.\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            if task15Music == True:
                                $ task15Text = _("We're going to give a party the Aces will remember for years. We have a few things to do however.\n{color=#A3A3A3}-Plan a mission to the Abandoned Amusement Park and steal fireworks.{/color}\n{color=#A3A3A3}-Plan a mission to Punk Web and steal the hottest mixtape.{/color}\n-Visit the school and pick up some thots.\n-Have at least $2.000.")
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the fireworks you need for the party!"
                            menu:
                                "Continue mission" if True:
                                    hide screen spyHacking with fade
                                    jump jumpStartScene
                                "Pull out" if True:
                                    jump missionComplete

                        if acesBounty3 == 1 and missionSetting == "School":
                            $ acesBounty3 = 2
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the upcoming test answers."
                            jump jumpStartScene
                        if acesBounty2 == 1 and missionSetting == "Faire":
                            $ acesBounty2 = 2
                            play sound "audio/sfx/itemGot.mp3"
                            "You find the Outsiders stash of grafitti."
                            jump jumpStartScene
                        if acesBounty1 == 1 and missionSetting == "Database":
                            $ acesBounty1 = 2
                            play sound "audio/sfx/itemGot.mp3"
                            "You find Drift Punk's hacking codes."
                            jump jumpStartScene
                elif True:
                    "Hack failed."
                    hide screen spyHacking with fade
                    jump jumpStartScene
            elif True:
                "It looks like this device can be hacked with the proper gadget."
                jump jumpStartScene
    if 11 <= randomBackground <= 11:
        if hackPart >= 3:
            if interSelect == 2:
                if activeSpy == 1:
                    play sound "audio/voice/illCrippleTheirFacilities.mp3"
                if activeSpy == 2:
                    play sound "audio/voice/clover/hackingEngaged.mp3"
                if activeSpy == 3:
                    play sound "audio/voice/alex/hackingIntoTheirSystems.mp3"
                show screen spyHacking
                with fade
                $ randomHack = renpy.random.randint(1,4)

                if randomHack == 1:
                    while hackResult < 100:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 2:
                    while hackResult < 91:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 3:
                    while hackResult < 76:
                        $ hackResult += 1
                        pause 0.003
                elif randomHack == 4:
                    while hackResult < 55:
                        $ hackResult += 1
                        pause 0.003
                if wormUpgrade and hackResult:
                    $ hackAvail = False
                    "Hacking Worm activated."
                    $ hackResult += 15
                pause
                if hackResult >= 100:
                    if activeSpy == 1:
                        play sound "audio/voice/imIn.mp3"
                    if activeSpy == 2:
                        play sound "audio/voice/clover/imIn.mp3"
                    if activeSpy == 3:
                        play sound "audio/voice/alex/imIn.mp3"
                    "Hack succesful. Opening gate."
                    hide screen spyHacking with fade
                    play sound "audio/sfx/defeatGang1.mp3"
                    hide obst1
                    show obst1:
                        xpos 137 ypos 0
                        linear 1.8 ypos -700
                    pause 1.8
                    $ randomObst1 = 0
                    jump jumpStartScene
                elif True:
                    "Hack failed. You'll have to find another way around."
                    hide screen spyHacking with fade
                    $ missionProgression -=1
                    pause 0.5
                    hide spyCorner with d3
                    pause 0.4
                    scene black with fade
                    jump missionBegin
                jump jumpStartScene
        elif True:
            "A hacking device is needed to get through this. You'll have to find another way around."
            $ missionProgression -=1
            pause 0.5
            hide spyCorner with d3
            pause 0.4
            scene black with fade
            jump missionBegin





screen interactScreenSpecial1:
    if task2Stage == 6:
        vbox xalign 0.61 yalign 0.40:
            imagebutton:
                idle "mission/enemy/bg1Tar1.png"
                hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                action SetVariable("task2Stage", 7), Jump("task2")
    if task2Stage == 9:
        vbox xalign 0.52 yalign 0.40:
            imagebutton:
                idle "mission/enemy/bg1Tar1.png"
                hover "mission/enemy/bg1Tar1-hover.png" tooltip " "
                action Jump("bossInteract")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[randomBossHP] HP" xalign 0.555 yalign 0.39





default vibActive = False
default breakControlChance = 0
default hackSkillUsed = False
default droneUsed = False

label vibratorActive:
    if hiddenStatus >= 2:
        if task26Stage <= 29:
            play music "audio/music/crisis.mp3" fadein 1.5
    if vibActive == False:
        $ vibActive = True
        $ breakControlChance = renpy.random.randint(1,4)
        if vibUpgrade:
            $ breakControlChance = 1
        call useVIB1 from _call_useVIB1
        pause 1.5
        if breakControlChance == 1:
            $ chanceOfControl = 0
            "V.I.B." "Control restored."
            jump vibratorActive
        if randomObst1 == 1:
            $ CoS1 -= 10
            $ obst1FoV = 1
            hide obst1
            if 1 <= randomBackground <= 3:
                show obst1:
                    xalign 0.325 yalign 0.43 rotate 2 zoom 0.48 xzoom -1
                with d3
            if 4 <= randomBackground <= 7:
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48 xzoom -1
                with d3
            if 8 <= randomBackground <= 10:
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
                with d3
            if 11 <= randomBackground <= 11:
                show obst1:
                    xalign 0.4 yalign 1.1 zoom 0.7 xzoom -1
                with d3
        play sound "audio/sfx/vib.mp3"
        if randomObst1 == 1 or randomObst2 == 1:
            pause 1.0
            $ hiddenStatus += 1
        if breakControlChance == 2:
            $ chanceOfControl = 0
            "V.I.B." "Control restored."
            jump vibratorActive
        if randomObst1 == 1:
            $ CoS1 -= 10
            hide obst1 with d3
            if 1 <= randomBackground <= 3:
                show obst1:
                    xalign 0.325 yalign 0.43 rotate 2 zoom 0.48 xzoom -1
                with d3
            if 4 <= randomBackground <= 7:
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48 xzoom -1
                with d3
            if 8 <= randomBackground <= 10:
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
                with d3
            if 11 <= randomBackground <= 11:
                show obst1:
                    xalign 0.4 yalign 1.1 zoom 0.7 xzoom -1
                with d3
        play sound "audio/sfx/vib.mp3"
        pause 1.5
        if breakControlChance == 3:
            $ chanceOfControl = 0
            play sound "audio/voice/samCumShort.mp3"
            "V.I.B." "Control restored."
            jump vibratorActive
        if randomObst1 == 1:
            $ CoS1 -= 10
            hide obst1 with d3
            if 1 <= randomBackground <= 3:
                show obst1:
                    xalign 0.325 yalign 0.43 rotate 2 zoom 0.48 xzoom -1
                with d3
            if 4 <= randomBackground <= 7:
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48 xzoom -1
                with d3
            if 8 <= randomBackground <= 10:
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
                with d3
            if 11 <= randomBackground <= 11:
                show obst1:
                    xalign 0.4 yalign 1.1 zoom 0.7 xzoom -1
                with d3
        if randomObst1 == 1 or randomObst2 == 1:
            pause 1.0
            $ hiddenStatus += 1
        if breakControlChance == 4:
            $ chanceOfControl = 0
            if task26Stage <= 29:
                play music "audio/music/crisis.mp3" fadein 1.0
            play sound "audio/voice/samCumShort.mp3"
            call vibCumming from _call_vibCumming
            "V.I.B." "Control restored."
            jump vibratorActive
        if randomObst1 == 0:
            $ randomObst1 = 1
            if 1 <= randomBackground <= 3:
                show obst1:
                    xalign 0.325 yalign 0.43 rotate 2 zoom 0.48 xzoom -1
                with d3
            if 4 <= randomBackground <= 7:
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48 xzoom -1
                with d3
            if 8 <= randomBackground <= 10:
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49 xzoom -1
                with d3
            if 11 <= randomBackground <= 11:
                show obst1:
                    xalign 0.4 yalign 1.1 zoom 0.7 xzoom -1
                with d3
        if randomObst2 == 0:
            $ randomObst2 = 1
            if 1 <= randomBackground <= 3:
                show obst2:
                    xalign 0.623 yalign 0.49 rotate 6 zoom 0.30 xzoom -1
                with d3
        jump vibratorActive
    elif True:
        call useVIB2 from _call_useVIB2






screen bagInteractGadgets:
    modal True
    default x = renpy.get_mouse_pos()[0]
    default y = renpy.get_mouse_pos()[1]
    frame:
        pos (x - 253, y + 15)
        has vbox
        if task26Stage == 23 and missionProgression == 10:
            textbutton _("Bondage Gadget"):
                action Hide("bagInteract"), Hide("bagInteractGadgets"), Jump("task26")
        if task26Stage == 25 and missionProgression == 10:
            textbutton _("Bondage Gadget"):
                action Hide("bagInteract"), Hide("bagInteractGadgets"), Jump("task26")
        if gadgetEarrings >= 1:
            if missionScreenGadget1Select == 1 or missionScreenGadget2Select == 1 or missionScreenGadget3Select == 1 or missionScreenGadget4Select == 1:
                textbutton _("Hypno Earrings"):
                    action Hide("bagInteract"), Hide("bagInteractGadgets"), SetVariable("gadgetUsed", 1), Jump("gadgetUsed")
        if gadgetPowder >= 1:
            if missionScreenGadget1Select == 2 or missionScreenGadget2Select == 2 or missionScreenGadget3Select == 2 or missionScreenGadget4Select == 2:
                textbutton _("Distraction Powder"):
                    action Hide("bagInteract"), Hide("bagInteractGadgets"), SetVariable("gadgetUsed", 2), Jump("gadgetUsed")
        if gadgetFlashbangBelt >= 1:
            if missionScreenGadget1Select == 3 or missionScreenGadget2Select == 3 or missionScreenGadget3Select == 3 or missionScreenGadget4Select == 3:
                textbutton _("Flashbang Belt"):
                    action Hide("bagInteract"), Hide("bagInteractGadgets"), SetVariable("gadgetUsed", 3), Jump("gadgetUsed")
        if gadgetDrone >= 1:
            if missionScreenGadget1Select == 4 or missionScreenGadget2Select == 4 or missionScreenGadget3Select == 4 or missionScreenGadget4Select == 4:
                textbutton _("AC Drone"):
                    action Hide("bagInteract"), Hide("bagInteractGadgets"), SetVariable("gadgetUsed", 4), Jump("gadgetUsed")
        if gadgetStealth >= 1:
            if missionScreenGadget1Select == 5 or missionScreenGadget2Select == 5 or missionScreenGadget3Select == 5 or missionScreenGadget4Select == 5:
                textbutton _("Stealth Bracelet"):
                    action Hide("bagInteract"), Hide("bagInteractGadgets"), SetVariable("gadgetUsed", 5), Jump("gadgetUsed")
        if gadgetJetpack >= 1:
            textbutton _("Jetpack"):
                action Hide("bagInteract"), Hide("bagInteractGadgets"), SetVariable("gadgetUsed", 6), Jump("gadgetUsed")
        textbutton _("Cancel"):
            action Hide("bagInteractGadgets")

label gadgetUsed:
    if tutStage == 5:
        jump tutHypno
    if 12 <= randomBackground <= 12:
        "Gadgets not unavailable on this floor."
        $ gadgetUsed = 0
        if gadgetHookActive == False:
            "ERROR: Grappling hook not detected. Attempting fix..."
            jump missionBegin
        call screen interactScreen
    if gadgetUsed == 1:
        $ gadgetUsed = 0
        if 1 <= randomBackground <= 3:

            $ gadgetEarrings -= 1

            if currentPosition == 0 and randomObst1 == 1:
                $ combatTarget = 1
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
                pause 0.1
                $ randomObst1 = 0
                show agentGuard:
                    xalign 0.365 yalign 0.49 rotate 2 zoom 0.45 xzoom -1
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.35 yalign 0.3
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Attack other agent" if randomObst2 == 1:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'Attack... other... agent...~{/i}'"
                        play sound "audio/sfx/punch1.mp3"
                        with hpunch
                        hide agentGuard
                        $ randomObst1 = 0
                        $ randomObst2 = 0
                        with quickflash
                        "The two agents knock each other out."
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                        if randomObst2 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ obst2FoV = 2
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                            call agentAlert from _call_agentAlert
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "Here! Take this suitcase, I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                        if randomObst2 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                hide spyThrowBack2
                call return2Pos from _call_return2Pos
                jump jumpStartScene


            if currentPosition == 0 and randomObst2 == 1:
                $ combatTarget = 2
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
                pause 0.1
                $ randomObst2 = 0
                show agentGuard:
                    xalign 0.61 yalign 0.50 rotate 2 zoom 0.30 xzoom -1
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.60 yalign 0.4 zoom 0.5
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "Here! Take this suitcase, I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                hide spyThrowBack2
                call return2Pos from _call_return2Pos_1
                jump jumpStartScene


            if currentPosition == 1 and randomObst2 == 1:
                $ combatTarget = 2
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowBack1:
                    xalign 0.13 yalign 0.76 zoom 0.55
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.13 yalign 0.76 zoom 0.55
                with d2
                pause 0.1
                $ randomObst2 = 0
                show agentGuard:
                    xalign 0.628 yalign 0.81 rotate 2 zoom 0.44
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.60 yalign 0.50 zoom 0.70
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "Here! Take this suitcase, I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                hide spyThrowBack2
                call return2Pos from _call_return2Pos_2
                jump jumpStartScene
            elif True:

                "No target."
                jump jumpStartScene
        if 4 <= randomBackground <= 7:

            $ gadgetEarrings -= 1

            if currentPosition == 0 and randomObst1 == 1:
                $ combatTarget = 1
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowSide1:
                    xalign 0.97 yalign 0.97 zoom 0.41 xzoom -1
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 0.97 yalign 0.97 zoom 0.41 xzoom -1
                with d2
                pause 0.1
                $ randomObst1 = 0
                show agentGuard:
                    xalign 0.68 yalign 1.05 rotate 3 zoom 0.435 xzoom -1
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.70 yalign 0.80 zoom 0.70
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "I know there's an important suitcase somewhere, if you see it, pick it up!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                hide spyThrowSide2
                call return2Pos from _call_return2Pos_3
                jump jumpStartScene


            if currentPosition == 1 and randomObst2 == 1:
                $ combatTarget = 2
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowSide1:
                    xalign 0.90 yalign 0.97 zoom 0.41 xzoom -1
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 0.90 yalign 0.97 zoom 0.41 xzoom -1
                with d2
                pause 0.1
                $ randomObst2 = 0
                show agentGuard:
                    xalign 0.01 yalign 1.05 rotate 3 zoom 0.435 xzoom -1
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.01 yalign 0.80 zoom 0.70
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "I know there's an important suitcase somewhere, if you see it, pick it up!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                hide spyThrowSide2
                call return2Pos from _call_return2Pos_4
                jump jumpStartScene


            if currentPosition == 3 and randomObst3 == 1:
                $ combatTarget = 3
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowSide1:
                    xalign 0.50 yalign 0.61 rotate 3 zoom 0.38
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 0.50 yalign 0.61 rotate 3 zoom 0.38
                with d2
                pause 0.1
                $ randomObst3 = 0
                show agentGuard:
                    xalign 0.83 yalign 0.63 rotate -4 zoom 0.42
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.83 yalign 0.51 zoom 0.70
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "I know there's an important suitcase somewhere, if you see it, pick it up!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                hide spyThrowSide2
                call return2Pos from _call_return2Pos_5
                jump jumpStartScene


            if currentPosition == 4 and randomObst4 == 1:
                $ combatTarget = 4
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowSide1:
                    xalign 0.46 yalign 0.15 xzoom -1 rotate -1 zoom 0.28
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 0.46 yalign 0.15 xzoom -1 rotate -1 zoom 0.28
                with d2
                pause 0.1
                $ randomObst4 = 0
                show agentGuard:
                    xalign 0.09 yalign 0.14 rotate 3 xzoom -1 zoom 0.30
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.13 yalign 0.10 zoom 0.50
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "I know there's an important suitcase somewhere, if you see it, pick it up!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                hide spyThrowSide2
                call return2Pos from _call_return2Pos_6
                jump jumpStartScene

        if 8 <= randomBackground <= 10:


            if currentPosition == 0 and randomObst1 == 1:
                $ combatTarget = 1
                $ gadgetEarrings -= 1
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowBack1:
                    xalign 0.85 yalign 0.80 zoom 0.69 xzoom -1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.85 yalign 0.80 zoom 0.69 xzoom -1
                with d2
                pause 0.1
                $ randomObst1 = 0
                show agentGuard:
                    xalign 0.50 yalign 0.55 rotate 2 zoom 0.47 xzoom -1
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.55 yalign 0.4 zoom 0.70
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Attack other agent" if randomObst3 == 1:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'Attack... other... agent...~{/i}'"
                        play sound "audio/sfx/punch1.mp3"
                        with hpunch
                        hide agentGuard
                        $ randomObst1 = 0
                        $ randomObst3 = 0
                        with quickflash
                        "The two agents knock each other out."
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage == 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "There is this one suitcase. I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                        if randomObst2 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                hide spyThrowBack2
                call return2Pos from _call_return2Pos_7
                jump jumpStartScene
            if currentPosition == 2 and randomObst3 == 1:
                $ combatTarget = 3
                $ gadgetEarrings -= 1
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowBack1:
                    xalign 0.1 yalign 1.1 zoom 0.67
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.1 yalign 1.1 zoom 0.67
                with d2
                pause 0.1
                $ randomObst3 = 0
                show agentGuard:
                    xalign 0.50 yalign 0.68 rotate 2 zoom 0.55
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.55 yalign 0.4 zoom 0.70
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Attack other agent" if randomObst3 == 1:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'Attack... other... agent...~{/i}'"
                        play sound "audio/sfx/punch1.mp3"
                        with hpunch
                        hide agentGuard
                        $ randomObst1 = 0
                        $ randomObst3 = 0
                        with quickflash
                        "The two agents knock each other out."
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "There is this one suitcase. I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                        if randomObst2 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                hide spyThrowBack2
                call return2Pos from _call_return2Pos_8
                jump jumpStartScene
            elif True:
                "I need to get closer first."
                jump jumpStartScene

        if 11 <= randomBackground <= 11:

            $ gadgetEarrings -= 1

            if currentPosition == 0 and randomObst1 == 1:
                $ combatTarget = 1
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowBack1:
                    xalign 1.0 yalign 2.3 zoom 0.86 xzoom -1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 1.0 yalign 2.3 zoom 0.86 xzoom -1
                with d2
                pause 0.1
                $ randomObst1 = 0
                show agentGuard:
                    xalign 0.4 yalign 1.05 zoom 0.64 xzoom -1
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.41 yalign 0.5 zoom 0.8

                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "There is this one suitcase. I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d3
                hide spyThrowBack2
                call return2Pos from _call_return2Pos_9
                jump jumpStartScene
            if currentPosition == 2 and randomObst2 == 1:
                $ combatTarget = 2
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowBack1:
                    xalign 0.8 yalign 0.9 zoom 0.53 xzoom -1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.8 yalign 0.9 zoom 0.53 xzoom -1
                with d2
                pause 0.1
                $ randomObst2 = 0
                show agentGuard:
                    xalign 0.53 yalign 0.72 rotate 2 zoom 0.44 xzoom -1
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.55 yalign 0.4 zoom 0.70
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Attack other agent" if randomObst3 == 1:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'Attack... other... agent...~{/i}'"
                        play sound "audio/sfx/punch1.mp3"
                        with hpunch
                        hide agentGuard
                        $ randomObst1 = 0
                        $ randomObst3 = 0
                        with quickflash
                        "The two agents knock each other out."
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "There is this one suitcase. I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                        if randomObst2 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                hide spyThrowBack2
                call return2Pos from _call_return2Pos_10
                jump jumpStartScene
            if currentPosition == 3 and randomObst3 == 1:
                $ combatTarget = 3
                hide spyCorner
                hide spyCornerSide
                hide spyCrouchCorner
                hide spyCrouchingSide
                with d2
                show spyThrowBack1:
                    xalign 0.23 yalign 0.75 zoom 0.54
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.23 yalign 0.75 zoom 0.54
                with d2
                pause 0.1
                $ randomObst3 = 0
                show agentGuard:
                    xalign 0.66 yalign 0.34 rotate -2 zoom 0.4
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.65 yalign 0.3 zoom 0.50
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "{b}*Cough* *Cough*{/b}"
                menu:
                    "Return to safehouse" if True:
                        play sound "audio/voice/agent/doingAsImTold.mp3"
                        "Agent" "{i}'I will return to the safehouse....~'{/i}"
                        $ capturedAgents += 1
                        hide agentGuard
                        with d3
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                    "Interrogate" if True:
                        $ randomInterr = renpy.random.randint(1,10)
                        if randomInterr >= 4:
                            "Agent" "If only I had taken the WOOHP Working-Under-Pressure course!"
                            "Agent" "There is this one suitcase. I think there might be something important in it!"
                            $ bonusAvailable = 1
                            "The hypnotized agent falls asleep..."
                        elif True:
                            "Agent" "They never let me in on any of the good stuff, I swear!"
                            "The hypnotized agent falls asleep..."
                        hide agentGuard
                        with d2
                        if randomObst3 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                        if randomObst2 == 1:
                            stop music fadeout 0.5
                            play sound "audio/sfx/alert.mp3"
                            if task26Stage <= 29:
                                play music "audio/music/crisis.mp3"
                            $ CoS2 -= 20
                            $ hiddenStatus = 2
                        with d3
                hide spyThrowBack2
                call return2Pos from _call_return2Pos_11
                jump jumpStartScene
        elif True:

            "DEV: GADGETS NOT IMPLEMENTED IN THIS BACKGROUND."
            jump jumpStartScene

    if gadgetUsed == 2:
        $ gadgetUsed = 0
        if 1 <= randomBackground <= 3:
            $ gadgetPowder -= 1

            if currentPosition == 0:
                hide spyCorner
                with d2
                show spyThrowBack1:
                    xalign 0.86 yalign 0.77 zoom 0.71 xzoom -1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.86 yalign 0.77 zoom 0.71 xzoom -1
                with d2
                pause 0.1
                with d3
                $ CoS1 += 20
                if CoS1 >= 100:
                    $ CoS1 = 100
                $ CoS2 += 20
                if CoS2 >= 100:
                    $ CoS2 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.65 yalign 0.55 zoom 0.3
                hide obst1 with d1
                $ obst1FoV = 3
                show obst1:
                    xalign 0.365 yalign 0.43 rotate 2 zoom 0.48
                with d2
                $ obst2FoV = 3
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                if randomObst1 == 1:
                    "Agent" "...?"
                hide spyThrowBack2
                show spyCorner:
                    xalign 0.90 yalign 0.83 zoom 0.78
                with d3
                jump jumpStartScene
            if currentPosition == 1:
                hide spyCrouchCorner
                with d2
                show spyThrowBack1:
                    xalign -0.09 yalign 0.72 zoom 0.53 rotate 1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign -0.09 yalign 0.72 zoom 0.53 rotate 1
                with d2
                pause 0.1
                with d3
                $ CoS1 += 20
                if CoS1 >= 100:
                    $ CoS1 = 100
                $ CoS2 += 20
                if CoS2 >= 100:
                    $ CoS2 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.78 yalign 0.8 zoom 0.3
                $ obst1FoV = 3
                $ obst2FoV = 3
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                if randomObst2 == 1:
                    "Agent" "...?"
                hide spyThrowBack2
                show spyCrouchCorner:
                    xalign -0.08 yalign 0.85 rotate 7 zoom 0.40
                with d3
                jump jumpStartScene
            if currentPosition == 2:
                "Nowhere to throw."
                jump jumpStartScene

        if 4 <= randomBackground <= 7:
            $ gadgetPowder -= 1

            if currentPosition == 0:
                hide spyCornerSide
                with d2
                show spyThrowSide1:
                    xalign 1.0 yalign 0.93 zoom 0.41 xzoom -1
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 1.0 yalign 0.93 zoom 0.41 xzoom -1
                with d2
                pause 0.1
                $ CoS1 += 20
                if CoS1 >= 100:
                    $ CoS1 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.0 yalign 0.98 zoom 0.3
                hide obst1
                $ obst1FoV = 3
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowSide2
                show spyCornerSide:
                    xalign 0.97 yalign 0.90 zoom 0.39
                with d3
                jump jumpStartScene
            if currentPosition == 1:
                hide spyCornerSide
                with d2
                show spyThrowSide1:
                    xalign 0.88 yalign 0.92 zoom 0.41 xzoom -1
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 0.88 yalign 0.92 zoom 0.41 xzoom -1
                with d2
                pause 0.1
                $ CoS2 += 20
                if CoS2 >= 100:
                    $ CoS2 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.0 yalign 0.98 zoom 0.3
                hide obst2
                $ obst2FoV = 3
                show obst2:
                    xalign 0.05 yalign 0.99 zoom 0.49
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowSide2
                show spyCornerSide:
                    xalign 0.87 yalign 0.90 zoom 0.385
                with d3
                jump jumpStartScene
            if currentPosition == 3:
                hide spyCornerSide
                with d2
                show spyThrowSide1:
                    xalign 0.48 yalign 0.60 zoom 0.39
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 0.48 yalign 0.60 zoom 0.39
                with d2
                pause 0.1
                $ CoS3 += 20
                if CoS3 >= 100:
                    $ CoS3 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.95 yalign 0.73 zoom 0.3
                hide obst2
                $ obst3FoV = 3
                show obst3:
                    xalign 0.775 yalign 0.60 zoom 0.44 xzoom -1
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowSide2
                show spyCornerSide:
                    xalign 0.485 yalign 0.60 zoom 0.377 xzoom -1
                with d3
                jump jumpStartScene
            if currentPosition == 4:
                hide spyCornerSide
                with d2
                show spyThrowSide1:
                    xalign 0.45 yalign 0.15 zoom 0.285 xzoom -1
                with d2
                pause 0.3
                hide spyThrowSide1
                show spyThrowSide2:
                    xalign 0.45 yalign 0.15 zoom 0.285 xzoom -1
                with d2
                pause 0.1
                $ CoS4 += 20
                if CoS4 >= 100:
                    $ CoS4 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.01 yalign 0.30 zoom 0.3
                hide obst4
                $ obst4FoV = 3
                show obst4:
                    xalign 0.12 yalign 0.115 zoom 0.321
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowSide2
                show spyCornerSide:
                    xalign 0.46 yalign 0.15 zoom 0.285
                with d3
                jump jumpStartScene

        if 8 <= randomBackground <= 10:
            $ gadgetPowder -= 1

            if currentPosition == 0:
                hide spyCorner
                with d2
                show spyThrowBack1:
                    xalign 0.95 yalign 0.85 zoom 0.71 xzoom -1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.95 yalign 0.85 zoom 0.71 xzoom -1
                with d2
                pause 0.1
                $ CoS1 += 20
                $ CoS3 += 20
                if CoS1 >= 100:
                    $ CoS1 = 100
                if CoS3 >= 100:
                    $ CoS3 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.55 yalign 0.50 zoom 0.3
                hide obst1
                hide obst3
                $ obst1FoV = 3
                $ obst3FoV = 3
                show obst3:
                    xalign 0.52 yalign 0.40 zoom 0.25
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowBack2
                with d1
                show spyCorner:
                    xalign 0.99 yalign 0.83 zoom 0.78
                with d3
                jump jumpStartScene
            if currentPosition == 2:
                hide spyCrouchCorner
                with d2
                show spyThrowBack1:
                    xalign 0.05 yalign 1.15 zoom 0.71
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.05 yalign 1.15 zoom 0.71
                with d2
                pause 0.1
                $ CoS1 += 20
                $ CoS3 += 20
                if CoS1 >= 100:
                    $ CoS1 = 100
                if CoS3 >= 100:
                    $ CoS3 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.5 yalign 0.85 zoom 0.3
                hide obst1
                hide obst3
                $ obst1FoV = 3
                $ obst3FoV = 3
                show obst3:
                    xalign 0.5 yalign 0.8 zoom 0.73
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowBack2
                with d1
                show spyCrouchCorner:
                    xalign 0.03 yalign 1.23 zoom 0.53
                with d3
                jump jumpStartScene

        if 11 <= randomBackground <= 11:
            $ gadgetPowder -= 1

            if currentPosition == 0:
                hide spyCorner
                with d2
                show spyThrowBack1:
                    xalign 1.0 yalign 2.3 zoom 0.86 xzoom -1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 1.0 yalign 2.3 zoom 0.86 xzoom -1
                with d2
                pause 0.1
                $ CoS1 += 20
                $ CoS3 += 20
                if CoS1 >= 100:
                    $ CoS1 = 100
                if CoS3 >= 100:
                    $ CoS3 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.3 yalign 0.98 zoom 0.3
                hide obst1
                hide obst3
                $ obst1FoV = 3
                show obst1:
                    xalign 0.4 yalign 1.15 zoom 0.72 xzoom -1
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowBack2
                with d1
                call return2Pos from _call_return2Pos_12
                jump jumpStartScene
            if currentPosition == 2:
                hide spyCrouchCorner
                with d2
                show spyThrowBack1:
                    xalign 0.8 yalign 0.9 zoom 0.53 xzoom -1
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.8 yalign 0.9 zoom 0.53 xzoom -1
                with d2
                pause 0.1
                $ CoS2 += 20
                $ CoS3 += 20
                if CoS2 >= 100:
                    $ CoS2 = 100
                if CoS3 >= 100:
                    $ CoS3 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.55 yalign 0.5 zoom 0.3
                hide obst2
                hide obst3
                $ obst2FoV = 3
                $ obst3FoV = 3

                if randomObst3 == 1 and currentPosition == 2:
                    show obst3:
                        xalign 0.57 yalign 0.44 zoom 0.2

                if randomObst2 == 1 and currentPosition == 2:
                    $ obst2FoV = 3
                    show obst2:
                        xalign 0.53 yalign 0.66 zoom 0.48
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.1
                "Agent" "...?"
                hide spyThrowBack2
                with d1
                call return2Pos from _call_return2Pos_13
                jump jumpStartScene
            if currentPosition == 3:
                hide spyCrouchCorner
                with d2
                show spyThrowBack1:
                    xalign 0.23 yalign 0.8 zoom 0.5
                with d2
                pause 0.3
                hide spyThrowBack1
                show spyThrowBack2:
                    xalign 0.23 yalign 0.8 zoom 0.5
                with d2
                pause 0.1
                $ CoS3 += 20
                if CoS3 >= 100:
                    $ CoS3 = 100
                play sound "audio/sfx/poof1.mp3"
                show gadgetCloud1:
                    xalign 0.65 yalign 0.48 zoom 0.3
                hide obst3
                $ obst3FoV = 3

                if randomObst3 == 1 and currentPosition == 3:
                    show obst3:
                        xalign 0.64 yalign 0.3 zoom 0.4
                pause 0.2
                hide gadgetCloud1
                with d5
                pause 0.5
                "Agent" "...?"
                hide spyThrowBack2
                with d1
                call return2Pos from _call_return2Pos_14
                jump jumpStartScene
        elif True:

            "DEV: GADGETS NOT IMPLEMENTED IN THIS BACKGROUND."
            jump jumpStartScene

    if gadgetUsed == 3:
        $ gadgetUsed = 0
        if 1 <= randomBackground <= 3 and currentPosition == 2:
            hide spyCrouchCorner
            with d2
            $ disableScreen = True
            $ flashbangActive = 1
            $ gadgetFlashbangBelt -= 1
            show spyThrowBack1:
                xalign 0.65 yalign 0.82 zoom 0.59 rotate 8
            with d2
            pause 0.3
            hide spyThrowBack1
            show spyThrowBack2:
                xalign 0.65 yalign 0.82 zoom 0.59 rotate 8
            with d2
        elif 4 <= randomBackground <= 7 and currentPosition == 2 and randomExit == 1:
            hide spyCrouchingSide
            with d2
            $ disableScreen = True
            $ flashbangActive = 1
            $ gadgetFlashbangBelt -= 1
            show spyThrowBack1:
                xalign 0.07 yalign 0.93 zoom 0.41
            with d2
            pause 0.3
            hide spyThrowBack1
            show spyThrowBack2:
                xalign 0.07 yalign 0.93 zoom 0.41
            with d2
        elif 4 <= randomBackground <= 7 and currentPosition == 3 and randomExit == 2:
            hide spyCorner
            hide spyCornerSide
            hide spyCrouchingSide
            hide spyCrouchCorner
            with d2
            $ disableScreen = True
            $ flashbangActive = 1
            $ gadgetFlashbangBelt -= 1
            show spyThrowBack1:
                xalign 0.85 yalign 0.62 zoom 0.4
            with d2
            pause 0.3
            hide spyThrowBack1
            show spyThrowBack2:
                xalign 0.85 yalign 0.62 zoom 0.4
            with d2
        elif 4 <= randomBackground <= 7 and currentPosition == 4 and randomExit == 3:
            hide spyCorner
            hide spyCornerSide
            hide spyCrouchingSide
            hide spyCrouchCorner
            with d2
            $ disableScreen = True
            $ flashbangActive = 1
            $ gadgetFlashbangBelt -= 1
            show spyThrowBack1:
                xalign 0.07 yalign 0.17 zoom 0.28
            with d2
            pause 0.3
            hide spyThrowBack1
            show spyThrowBack2:
                xalign 0.07 yalign 0.17 zoom 0.28
            with d2
        elif 8 <= randomBackground <= 10 and currentPosition == 2:
            hide spyCorner
            hide spyCornerSide
            hide spyCrouchingSide
            hide spyCrouchCorner
            with d2
            $ disableScreen = True
            $ flashbangActive = 1
            $ gadgetFlashbangBelt -= 1
            show spyThrowBack1:
                xalign 0.3 yalign 1.0 zoom 0.65
            with d2
            pause 0.3
            hide spyThrowBack1
            show spyThrowBack2:
                xalign 0.3 yalign 1.0 zoom 0.65
            with d2
        elif 11 <= randomBackground <= 11 and currentPosition == 4:
            hide spyCorner
            hide spyCornerSide
            hide spyCrouchingSide
            hide spyCrouchCorner
            with d2
            $ disableScreen = True
            $ flashbangActive = 1
            $ gadgetFlashbangBelt -= 1
            show spyThrowBack1:
                xalign 0.7 yalign 0.9 zoom 0.62 xzoom -1
            with d2
            pause 0.3
            hide spyThrowBack1
            show spyThrowBack2:
                xalign 0.7 yalign 0.9 zoom 0.62 xzoom -1
            with d2
        elif True:
            "Not close enough to an exit."
            jump jumpStartScene
        pause 0.1
        play sound "audio/sfx/flashbang.mp3"
        pause 0.55
        show white
        pause 0.08
        hide white
        pause 0.5
        hide spyThrowBack2
        with d2
        call return2Pos from _call_return2Pos_15
        if flashUpgrade == True:
            $ flashbangRandom = renpy.random.randint(1,100)
            if flashbangRandom >= 75:
                $ flashbangSpecial = True
                "Flashbang Belt Upgrade triggered!"
                "All enemies in the room are knocked out."
        $ disableScreen = False
        jump jumpStartScene

    if gadgetUsed == 4:
        $ gadgetUsed = 0
        if 1 <= randomBackground <= 3 and currentPosition == 2:
            $ droneUsed = True
            jump missionBegin
        elif 4 <= randomBackground <= 7 and currentPosition == 3:
            $ droneUsed = True
            jump missionBegin
        elif 4 <= randomBackground <= 7 and currentPosition == 4:
            $ droneUsed = True
            jump missionBegin
        elif 8 <= randomBackground <= 10 and currentPosition == 2:
            $ droneUsed = True
            jump missionBegin
        elif 11 <= randomBackground <= 11 and currentPosition == 4:
            $ droneUsed = True
            jump missionBegin
        elif True:
            "Not near an exit."
            jump jumpStartScene

    if gadgetUsed == 5:
        $ gadgetUsed = 0
        $ hiddenStatus = 0
        if 1 <= randomBackground <= 3 and currentPosition == 0:
            show spyCorner:
                linear 0.5 alpha 0.5
        if 1 <= randomBackground <= 3 and currentPosition >= 1 or randomBackground == 11 and 1 <= currentPosition <= 4:
            show spyCrouchCorner:
                linear 0.5 alpha 0.5
        if 4 <= randomBackground <= 7 and 0 <= currentPosition <= 1 or 4 <= randomBackground <= 7 and 3 <= currentPosition <= 4:
            show spyCornerSide:
                linear 0.5 alpha 0.5
        if 4 <= randomBackground <= 7 and currentPosition == 2:
            show spyCrouchingSide:
                linear 0.5 alpha 0.5
        if randomBackground == 11 and currentPosition == 0:
            show spyCorner:
                linear 0.5 alpha 0.5
        pause 0.5
        "Stealth bracelet activated. Threat level reduced."
        jump jumpStartScene

    if gadgetUsed == 6:
        $ gadgetUsed = 0
        if missionSetting == "School":
            if 1 <= task4Stage <= 4 or 1 <= task2Stage <= 9:
                "Gadget not available during this mission."
                jump jumpStartScene
        if missionSetting == "Database":
            if 1 <= task23Stage <= 6:
                "Gadget not available during this mission."
                jump jumpStartScene
        if missionSetting == "Faire":
            if 1 <= task25Stage <= 9:
                "Gadget not available during this mission."
                jump jumpStartScene
        if missionSetting == "WOOHP":
            if 1 <= task25Stage <= 9:
                "Gadget not available during this mission."
                jump jumpStartScene
            if 30 <= task26Stage <= 33:
                "Gadget not available during this mission."
                jump jumpStartScene
        hide screen gadgetMenu
        hide screen equipmentMenu
        scene black with fade
        "Your spy straps on a jetpack and flies up a couple of floors!"
        play sound "audio/sfx/ship.mp3"
        $ missionProgression = 8
        jump missionBegin





default backupUsed = 0
default backup1 = 6
default backup2 = 6
default backup3 = 6
default backup4 = 6
default backup5 = 6

screen bagInteractBackup:
    modal True
    default x = renpy.get_mouse_pos()[0]
    default y = renpy.get_mouse_pos()[1]
    frame:
        xpos 1000 ypos 100
        has vbox
        if backupSamActive and backup1 >= 6:
            textbutton _("Sam{#tbinmS}"):
                action Hide("bagInteract"), Hide("bagInteractBackup"), SetVariable("backupUsed", 1), SetVariable("backup1", 0), Jump("backupUsed")
        if backupCloverActive and backup2 >= 6:
            textbutton _("Clover{#tbinmS}"):
                action Hide("bagInteract"), Hide("bagInteractBackup"), SetVariable("backupUsed", 2), SetVariable("backup2", 0), Jump("backupUsed")
        if backupAlexActive and backup3 >= 6:
            textbutton _("Alex{#tbinmS}"):
                action Hide("bagInteract"), Hide("bagInteractBackup"), SetVariable("backupUsed", 3), SetVariable("backup3", 0), Jump("backupUsed")
        if backupKimActive and backup4 >= 6:
            textbutton _("Kim{#tbinmS}"):
                action Hide("bagInteract"), Hide("bagInteractBackup"), SetVariable("backupUsed", 4), SetVariable("backup4", 0), Jump("backupUsed")
        if backupBritneyActive and backup5 >= 6:
            textbutton _("Britney{#tbinmS}"):
                action Hide("bagInteract"), Hide("bagInteractBackup"), SetVariable("backupUsed", 5), SetVariable("backup5", 0), Jump("backupUsed")
        textbutton _("Cancel"):
            action Hide("bagInteractBackup")

label backupUsed:
    hide screen gadgetMenu
    hide screen interactScreen
    show white
    hide spyGuard2
    pause 0.01
    hide white
    if 1 <= backupUsed <= 5:
        if 1 <= randomBackground <= 3:
            if randomObst1 == 1 and currentPosition == 0:
                $ combatTarget = 1
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/youGotIt3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onMyWay1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.30 yalign -0.7 zoom 0.39
                    linear 0.2 yalign 0.50
                pause 0.3
                hide spyBackup4
                $ randomObst1 = 0
                hide obst1
                show agentGuard:
                    xalign 0.40 yalign 0.50 zoom 0.43
                    linear 0.12 xalign 0.41
                    linear 0.12 xalign 0.39
                    linear 0.12 xalign 0.41
                    linear 0.12 xalign 0.39
                    linear 0.12 xalign 0.41
                    linear 0.12 xalign 0.39
                    linear 0.12 xalign 0.41
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.36 yalign 0.50 zoom 0.415
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.35 yalign 0.52 zoom 0.38
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.40 yalign 0.50 zoom 0.43
                    linear 0.35 xalign 0.41 yalign 0.48
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.36 yalign 0.46 zoom 0.445
                    linear 0.3 yalign 0.44
                pause 0.3
                hide spyBackup1
                hide agentHit
                show spyCorner:
                    xalign 0.90 yalign 0.83 zoom 0.78
                with d2
                show screen gadgetMenu
                call screen interactScreen
            if randomObst2 == 1 and currentPosition == 1:
                $ combatTarget = 2
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.50 yalign -0.5 zoom 0.37
                    linear 0.2 yalign 0.78
                pause 0.3
                hide spyBackup4
                $ randomObst2 = 0
                hide obst2
                show agentGuard:
                    xalign 0.60 yalign 0.78 zoom 0.43
                    linear 0.12 xalign 0.61
                    linear 0.12 xalign 0.59
                    linear 0.12 xalign 0.61
                    linear 0.12 xalign 0.59
                    linear 0.12 xalign 0.61
                    linear 0.12 xalign 0.59
                    linear 0.12 xalign 0.61
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.56 yalign 0.77 zoom 0.42
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.54 yalign 0.79 zoom 0.38
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.60 yalign 0.75 zoom 0.43
                    linear 0.35 xalign 0.61 yalign 0.72
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.52 yalign 0.74 zoom 0.44
                    linear 0.3 yalign 0.70
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen

            if specialMaggieStatus == 1 and missionSetting == "Castle" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if specialMelodyStatus == 1 and missionSetting == "Castle" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if specialCandyStatus == 1 and missionSetting == "Castle" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if specialDragonStatus == 1 and missionSetting == "Database" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if missionSetting == "Database" and missionProgression == 10 and task26Stage == 23:
                "Backup is currently not available."
                $ renpy.pause(hard='True')
            if specialMuffyStatus == 1 and missionSetting == "Faire" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if task26Stage == 9 and missionSetting == "WOOHP" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if task26Stage == 14 and missionSetting == "WOOHP" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if task26Stage == 23 and missionSetting == "WOOHP" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if task26Stage == 25 and missionSetting == "WOOHP" and missionProgression == 10:
                "Backup is currently not available."
                show screen gadgetMenu
                call screen interactScreen
            if randomBoss == 1 and currentPosition == 0:
                show spyCorner:
                    xalign 0.90 yalign 0.83 zoom 0.78
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.37 yalign -0.5 zoom 0.39
                    linear 0.3 yalign 0.50
                pause 0.3
                hide spyBackup4
                hide obstHulk
                $ randomBossHP -= 1
                show obstHulkBlock:
                    xalign 0.50 yalign 0.40 zoom 0.52
                    linear 0.12 xalign 0.505
                    linear 0.12 xalign 0.495
                    linear 0.12 xalign 0.505
                    linear 0.12 xalign 0.495
                    linear 0.12 xalign 0.505
                    linear 0.12 xalign 0.495
                    linear 0.12 xalign 0.50
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.37 yalign 0.50 zoom 0.41
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.37 yalign 0.50 zoom 0.40
                pause 0.3
                hide spyBackup2
                show spyBackup1:
                    xalign 0.37 yalign 0.41 zoom 0.46
                    linear 0.5 yalign 0.36
                if randomBossHP <= 0:
                    $ randomBoss = 0
                    hide obstHulkBlock
                    play sound "audio/sfx/defeatEnemy.mp3"
                    show obstHulkHit:
                        xalign 0.50 yalign 0.415 zoom 0.52
                        linear 0.3 xalign 0.50 yalign 0.39
                    $ renpy.pause(0.5, hard='True')
                    hide spyBackup1
                    hide obstHulkHit
                    with d3
                    $ loot1 += 1
                    $ loot5 += 1
                    play sound "audio/sfx/jobReward.mp3"
                    show dropMats at item_drop((550,300))
                    pause 0.3
                    play sound "audio/sfx/jobReward.mp3"
                    show dropConsum at item_drop((550,300))
                    with d3
                    if 30 <= task26Stage <= 32:
                        hide screen equipmentMenu
                        $ missionProgression = 7
                        $ randomBoss = 1
                        jump task26
                    pause 0.5
                    call threatNeutralized from _call_threatNeutralized_3
                    jump missionComplete

                play sound "audio/sfx/punch1.mp3"
                show spyBackup1:
                    xalign 0.37 yalign 0.44 zoom 0.49
                    linear 0.3 yalign 0.40
                pause 0.3
                hide spyBackup1
                with d2
                hide obstHulkBlock
                show obstHulk:
                    xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                with d3
                show screen gadgetMenu
                call screen interactScreen
            elif True:
                if backupUsed == 1:
                    $ backup1 = 6
                if backupUsed == 2:
                    $ backup2 = 6
                if backupUsed == 3:
                    $ backup3 = 6
                "Nothing in range."
                show screen gadgetMenu
                call screen interactScreen
        if 4 <= randomBackground <= 7:
            if randomObst1 == 1 and currentPosition == 0:
                $ combatTarget = 1
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.55 yalign -0.5 zoom 0.39
                    linear 0.3 yalign 0.99
                pause 0.3
                hide spyBackup4
                $ randomObst1 = 0
                hide obst1
                show agentGuard:
                    xalign 0.64 yalign 0.99 zoom 0.44
                    linear 0.12 xalign 0.643
                    linear 0.12 xalign 0.637
                    linear 0.12 xalign 0.643
                    linear 0.12 xalign 0.637
                    linear 0.12 xalign 0.643
                    linear 0.12 xalign 0.637
                    linear 0.12 xalign 0.64
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.55 yalign 0.98 zoom 0.41
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.55 yalign 0.99 zoom 0.40
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.65 yalign 0.97 zoom 0.44
                    linear 0.35 xalign 0.655 yalign 0.95
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.55 yalign 0.95 zoom 0.47
                    linear 0.3 yalign 0.93
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen
            if randomObst2 == 1 and currentPosition == 1:
                $ combatTarget = 2
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign -0.05 yalign -0.5 zoom 0.39
                    linear 0.3 yalign 0.99
                pause 0.3
                hide spyBackup4
                $ randomObst2 = 0
                hide obst2
                show agentGuard:
                    xalign 0.10 yalign 0.99 zoom 0.43
                    linear 0.12 xalign 0.101
                    linear 0.12 xalign 0.09
                    linear 0.12 xalign 0.101
                    linear 0.12 xalign 0.09
                    linear 0.12 xalign 0.101
                    linear 0.12 xalign 0.09
                    linear 0.12 xalign 0.10
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.00 yalign 0.98 zoom 0.41
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.00 yalign 0.99 zoom 0.40
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.10 yalign 0.97 zoom 0.440
                    linear 0.35 xalign 0.11 yalign 0.95
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.05 yalign 0.95 zoom 0.47
                    linear 0.3 yalign 0.93
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen
            if randomObst3 == 1 and currentPosition == 3:
                $ combatTarget = 3
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.70 yalign -0.5 zoom 0.35
                    linear 0.3 yalign 0.60
                pause 0.3
                hide spyBackup4
                $ randomObst3 = 0
                hide obst3
                show agentGuard:
                    xalign 0.76 yalign 0.60 zoom 0.43
                    linear 0.1 xalign 0.77
                    linear 0.1 xalign 0.75
                    linear 0.1 xalign 0.77
                    linear 0.1 xalign 0.75
                    linear 0.1 xalign 0.77
                    linear 0.1 xalign 0.75
                    linear 0.1 xalign 0.76
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.75 yalign 0.60 zoom 0.41
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.72 yalign 0.62 zoom 0.38
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.76 yalign 0.56 zoom 0.440
                    linear 0.35 xalign 0.77 yalign 0.54
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.70 yalign 0.54 zoom 0.47
                    linear 0.3 yalign 0.51
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen
            if randomObst4 == 1 and currentPosition == 4:
                $ combatTarget = 4
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.02 yalign -0.5 zoom 0.27
                    linear 0.3 yalign 0.17
                pause 0.3
                hide spyBackup4
                $ randomObst4 = 0
                hide obst4
                show agentGuard:
                    xalign 0.10 yalign 0.11 zoom 0.34
                    linear 0.1 xalign 0.105
                    linear 0.1 xalign 0.095
                    linear 0.1 xalign 0.105
                    linear 0.1 xalign 0.095
                    linear 0.1 xalign 0.105
                    linear 0.1 xalign 0.095
                    linear 0.1 xalign 0.105
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.04 yalign 0.14 zoom 0.31
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.04 yalign 0.16 zoom 0.30
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.10 yalign 0.10 zoom 0.34
                    linear 0.35 xalign 0.105 yalign 0.09
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.044 yalign 0.06 zoom 0.36
                    linear 0.3 yalign 0.05
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen
            elif True:
                if backupUsed == 1:
                    $ backup1 = 6
                if backupUsed == 2:
                    $ backup2 = 6
                if backupUsed == 3:
                    $ backup3 = 6
                "Nothing in range."
                show screen gadgetMenu
                call screen interactScreen
        if 8 <= randomBackground <= 10:
            if randomObst1 == 1 and currentPosition == 0:
                $ combatTarget = 1
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.45 yalign -0.5 zoom 0.39
                    linear 0.3 yalign 0.51
                pause 0.3
                hide spyBackup4
                $ randomObst1 = 0
                hide obst1
                show agentGuard:
                    xalign 0.53 yalign 0.50 zoom 0.45
                    linear 0.12 xalign 0.55
                    linear 0.12 xalign 0.53
                    linear 0.12 xalign 0.55
                    linear 0.12 xalign 0.53
                    linear 0.12 xalign 0.55
                    linear 0.12 xalign 0.53
                    linear 0.12 xalign 0.55
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.45 yalign 0.53 zoom 0.41
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.45 yalign 0.53 zoom 0.39
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.52 yalign 0.52 zoom 0.46
                    linear 0.35 xalign 0.52 yalign 0.50
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.45 yalign 0.46 zoom 0.47
                    linear 0.3 yalign 0.42
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen
            if randomObst3 == 1 and currentPosition == 2:
                $ combatTarget = 3
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.38 yalign -0.5 zoom 0.47
                    linear 0.3 yalign 0.63
                pause 0.3
                hide spyBackup4
                $ randomObst3 = 0
                hide obst3
                show agentGuard:
                    xalign 0.52 yalign 0.68 zoom 0.60
                    linear 0.12 xalign 0.53
                    linear 0.12 xalign 0.52
                    linear 0.12 xalign 0.53
                    linear 0.12 xalign 0.52
                    linear 0.12 xalign 0.53
                    linear 0.12 xalign 0.52
                    linear 0.12 xalign 0.53
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.41 yalign 0.65 zoom 0.54
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.41 yalign 0.71 zoom 0.50
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.51 yalign 0.50 zoom 0.56
                    linear 0.35 xalign 0.52 yalign 0.48
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.44 yalign 0.50 zoom 0.56
                    linear 0.3 yalign 0.48
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen
            elif True:
                if backupUsed == 1:
                    $ backup1 = 6
                if backupUsed == 2:
                    $ backup2 = 6
                if backupUsed == 3:
                    $ backup3 = 6
                if backupUsed == 4:
                    $ backup4 = 6
                if backupUsed == 5:
                    $ backup5 = 6
                "Nothing in range."
                show screen gadgetMenu
                call screen interactScreen

        if 11 <= randomBackground <= 11:
            if randomObst1 == 1 and currentPosition == 0:
                $ combatTarget = 1
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.27 yalign -0.5 zoom 0.56
                    linear 0.3 yalign 1.0
                pause 0.3
                hide spyBackup4
                $ randomObst1 = 0
                hide obst1
                show agentGuard:
                    xalign 0.4 yalign 1.1 zoom 0.7
                    linear 0.12 xalign 0.4
                    linear 0.12 xalign 0.43
                    linear 0.12 xalign 0.4
                    linear 0.12 xalign 0.43
                    linear 0.12 xalign 0.4
                    linear 0.12 xalign 0.43
                    linear 0.12 xalign 0.4
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.27 yalign 1.0 zoom 0.61
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.27 yalign 1.0 zoom 0.6
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.4 yalign 1.1 zoom 0.6
                    linear 0.35 xalign 0.41 yalign 0.95
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.27 yalign 0.98 zoom 0.68
                    linear 0.3 yalign 0.9
                pause 0.33
                hide spyBackup1
                hide agentHit
                with d2
                show screen gadgetMenu
                call screen interactScreen
            if randomObst2 == 1 and currentPosition == 2:
                $ combatTarget = 2
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.4 yalign -0.5 zoom 0.4
                    linear 0.3 yalign 0.71
                pause 0.3
                hide spyBackup4
                $ randomObst2 = 0
                hide obst2
                show agentGuard:
                    xalign 0.55 yalign 0.67 zoom 0.49
                    linear 0.12 xalign 0.56
                    linear 0.12 xalign 0.55
                    linear 0.12 xalign 0.56
                    linear 0.12 xalign 0.55
                    linear 0.12 xalign 0.56
                    linear 0.12 xalign 0.55
                    linear 0.12 xalign 0.56
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.46 yalign 0.65 zoom 0.44
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.46 yalign 0.68 zoom 0.43
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.51 yalign 0.65 zoom 0.5
                    linear 0.35 xalign 0.52 yalign 0.6
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.46 yalign 0.65 zoom 0.52
                    linear 0.3 yalign 0.6
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                $ combatTarget = 0
                show screen gadgetMenu
                call screen interactScreen
            if randomObst3 == 1 and currentPosition == 3:
                $ combatTarget = 3
                if backupUsed == 1:
                    play sound "audio/voice/youGotIt1.mp3"
                if backupUsed == 2:
                    play sound "audio/voice/clover/yougotit3.mp3"
                if backupUsed == 3:
                    play sound "audio/voice/alex/onmyway1.mp3"
                    pause 0.6
                pause 0.8
                show spyBackup4:
                    xalign 0.55 yalign -0.5 zoom 0.35
                    linear 0.3 yalign 0.39
                pause 0.3
                hide spyBackup4
                $ randomObst3 = 0
                hide obst3
                show agentGuard:
                    xalign 0.65 yalign 0.39 zoom 0.4
                    linear 0.12 xalign 0.66
                    linear 0.12 xalign 0.65
                    linear 0.12 xalign 0.66
                    linear 0.12 xalign 0.65
                    linear 0.12 xalign 0.66
                    linear 0.12 xalign 0.65
                    linear 0.12 xalign 0.66
                play sound "audio/sfx/punch1.mp3"
                show spyBackup3:
                    xalign 0.57 yalign 0.39 zoom 0.35
                pause 0.3
                hide spyBackup3
                play sound "audio/sfx/punch1.mp3"
                show spyBackup2:
                    xalign 0.57 yalign 0.39 zoom 0.34
                pause 0.3
                hide spyBackup2
                hide agentGuard
                show agentHit:
                    xalign 0.65 yalign 0.39 zoom 0.4
                    linear 0.35 xalign 0.66 yalign 0.35
                play sound "audio/sfx/defeatEnemy.mp3"
                show spyBackup1:
                    xalign 0.55 yalign 0.39 zoom 0.42
                    linear 0.3 yalign 0.36
                pause 0.3
                hide spyBackup1
                hide agentHit
                with d2
                $ combatTarget = 0
                show screen gadgetMenu
                call screen interactScreen
            elif True:
                if backupUsed == 1:
                    $ backup1 = 6
                if backupUsed == 2:
                    $ backup2 = 6
                if backupUsed == 3:
                    $ backup3 = 6
                "Nothing in range."
                show screen gadgetMenu
                call screen interactScreen
        if 12 <= randomBackground <= 12:
            "Backup unavailable on this floor."
            if gadgetHookActive == False:
                "ERROR: Grappling hook not detected. Attempting fix..."
                jump missionBegin
            show screen gadgetMenu
            call screen interactScreen





default itemtUsed = 0
default blueMagicBlock = False
default greenMagicBlock = False
default redMagicBlock = False

screen bagInteractItems:
    if bagItemsName == "Potions":
        modal True
        default x = renpy.get_mouse_pos()[0]
        default y = renpy.get_mouse_pos()[1]
        frame:
            pos (x - 213, y + 15)
            has vbox
            if task25Stage >= 4:
                textbutton _("Blue Potion"):
                    action Hide("bagInteract"), Hide("bagInteractItems"), SetVariable("itemtUsed", 10), Jump("itemUsed")
                textbutton _("Green Potion"):
                    action Hide("bagInteract"), Hide("bagInteractItems"), SetVariable("itemtUsed", 11), Jump("itemUsed")
                textbutton _("Red Potion"):
                    action Hide("bagInteract"), Hide("bagInteractItems"), SetVariable("itemtUsed", 12), Jump("itemUsed")
            textbutton _("Cancel"):
                action Hide("bagInteractItems")
    elif bagItemsName == "Items":
        modal True
        default x = renpy.get_mouse_pos()[0]
        default y = renpy.get_mouse_pos()[1]
        frame:
            pos (x - 213, y + 15)
            has vbox
            if medkit >= 1:
                textbutton _("Medkit"):
                    action Hide("bagInteract"), Hide("bagInteractItems"), SetVariable("itemtUsed", 1), Jump("itemUsed")
            textbutton _("Cancel"):
                action Hide("bagInteractItems")

label itemUsed:
    if itemtUsed == 1:
        $ itemtUsed = 0
        if activeSpy == 1:
            play sound "audio/voice/50CcStat.mp3"
            $ backupSamActive = False
        if activeSpy == 2:
            play sound "audio/voice/clover/medkitNow.mp3"
            $ backupCloverActive = False
        if activeSpy == 3:
            play sound "audio/voice/alex/needAMedic.mp3"
            $ backupAlexActive = False
            pause 2.0
        "Who do you wish to use the medkit on?"
        menu:
            "Sam [samHealth]/3" if samHealth <= 2 and spy1Status != 999:
                play sound "audio/voice/backToTheFight.mp3"
                $ samHealth += 1
                $ backupSamActive = True
                $ backup1 = 6
            "Clover [cloverHealth]/3" if cloverHealth <= 2 and spy2Status != 999:
                play sound "audio/voice/clover/goodToGo.mp3"
                $ cloverHealth += 1
                $ backupCloverActive = True
                $ backup2 = 6
            "Alex [alexHealth]/3" if alexHealth <= 2 and spy3Status != 999:
                play sound "audio/voice/alex/readyToRock.mp3"
                $ alexHealth += 1
                $ backupAlexActive = True
                $ backup3 = 6
            "Never mind" if True:
                call screen interactScreen
        "Wounded spy has become available for backup again."
        call screen interactScreen


    if itemtUsed == 10:
        $ itemtUsed = 0
        if blueMagicBlock == True:
            $ blueMagicBlock = False
            "{b}*Glug* *Glug* *Glug*{/b}"
            hide magicwall
            hide shield1
            with d3
            if task25Stage == 4:
                jump task25
            elif task25Stage == 8:
                call screen interactScreenBonus
            elif True:
                call screen interactScreen
        elif True:
            "No effect."
            if blueMagicBlock == False and redMagicBlock == False and greenMagicBlock == False:
                call screen interactScreenBonus
            $ renpy.pause(hard='True')
    if itemtUsed == 11:
        $ itemtUsed = 0
        if greenMagicBlock == True:
            $ greenMagicBlock = False
            "{b}*Glug* *Glug* *Glug*{/b}"
            hide magicwall2
            hide shield3
            with d3
            if task25Stage == 7:
                jump task25
            elif task25Stage == 8:
                call screen interactScreenBonus
            elif True:
                call screen interactScreen
            call screen interactScreen
        elif True:
            "No effect."
            if blueMagicBlock == False and redMagicBlock == False and greenMagicBlock == False:
                call screen interactScreenBonus
            $ renpy.pause(hard='True')
    if itemtUsed == 12:
        $ itemtUsed = 0
        if redMagicBlock == True:
            $ redMagicBlock = False
            "{b}*Glug* *Glug* *Glug*{/b}"
            hide magicwall3
            hide shield2
            with d3
            if task25Stage == 6:
                jump task25
            elif task25Stage == 8:
                call screen interactScreenBonus
            elif True:
                call screen interactScreen
        elif True:
            "No effect."
            if blueMagicBlock == False and redMagicBlock == False and greenMagicBlock == False:
                call screen interactScreenBonus
            $ renpy.pause(hard='True')


image shield1 = "mission/fx/shield1.png"
image shield2 = "mission/fx/shield2.png"
image shield3 = "mission/fx/shield3.png"

label kandInteract:
    if blueMagicBlock:
        hide spyCorner
        show spyCombat1:
            xalign 0.53 yalign 0.45 zoom 0.36
        show shield1:
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
        with d1
        pause 0.6
        hide spyCombat1
        show spyHit:
            xalign 0.54 yalign 0.46 zoom 0.28 xzoom -1
            linear 0.5 xalign 0.535 yalign 0.45
        show expression "mission/fx/bolt.png":
            xalign 0.59 yalign 0.0
        with d1
        pause 0.1
        hide expression "mission/fx/bolt.png"
        pause 0.45
        hide spyHit
        call spyHitBackup from _call_spyHitBackup_15
    elif redMagicBlock:
        hide spyCorner
        show spyCombat1:
            xalign 0.53 yalign 0.45 zoom 0.36
        show shield2:
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
        with d1
        pause 0.6
        hide spyCombat1
        show spyHit:
            xalign 0.54 yalign 0.46 zoom 0.28 xzoom -1
            linear 0.5 xalign 0.535 yalign 0.45
        show expression "mission/fx/bolt2.png":
            xalign 0.59 yalign 0.0
        with d1
        pause 0.1
        hide expression "mission/fx/bolt2.png"
        pause 0.45
        hide spyHit
        call spyHitBackup from _call_spyHitBackup_16
    elif greenMagicBlock:
        hide spyCorner
        show spyCombat1:
            xalign 0.53 yalign 0.45 zoom 0.36
        show shield3:
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
            linear 0.05 xalign 0.588
            linear 0.05 xalign 0.58
        with d1
        pause 0.6
        hide spyCombat1
        show spyHit:
            xalign 0.54 yalign 0.46 zoom 0.28 xzoom -1
            linear 0.5 xalign 0.535 yalign 0.45
        show expression "mission/fx/bolt3.png":
            xalign 0.59 yalign 0.0
        with d1
        pause 0.1
        hide expression "mission/fx/bolt3.png"
        pause 0.45
        hide spyHit
        call spyHitBackup from _call_spyHitBackup_17
    elif True:
        $ randomBossHP -= 1
        hide spyCorner
        show spyCombat1:
            xalign 0.53 yalign 0.45 zoom 0.36
        show kandModel:
            xalign 0.6 yalign 0.45 rotate 0.7 zoom 0.3
            linear 0.06 xalign 0.61
            linear 0.06 xalign 0.60
            linear 0.06 xalign 0.61
            linear 0.06 xalign 0.60
            linear 0.06 xalign 0.61
            linear 0.06 xalign 0.60
        if randomBossHP == 2:
            kand "Abra Kadabra!"
            show shield2:
                xalign 0.58 yalign 0.44 rotate 0.7
            hide spyCombat1
            with d2
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            $ redMagicBlock = True
            call screen interactScreenBonus
        if randomBossHP == 1:
            kand "Alakazam!"
            show shield3:
                xalign 0.58 yalign 0.44 rotate 0.7
            hide spyCombat1
            with d2
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            $ greenMagicBlock = True
            call screen interactScreenBonus
        if randomBossHP == 0:
            $ task25Stage = 9
            $ specialKandStatus = 2
            kand "Excel...sior..!"
            kand "Ugh~..."
            hide kandModel with d3
            "Kandinsky collapses!"
            hide spyCombat1 with d3
            pause 0.4
            jump missionComplete

"Something has gone wrong when using backup and you're not suppose to see this."
"Game will not attempt to correct itself. If you see this message, please contact Exiscoming."
hide spyBackup1
hide spyBackup2
$ randomBackground = 1
$ backupUsed = 2
$ missionScreenFrontlineSelect = 1
$ missionScreenSupportSelect = 2
jump missionBegin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
