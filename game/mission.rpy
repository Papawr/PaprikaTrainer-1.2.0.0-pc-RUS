



default missionSetting = "Castle"




image gadgetCloud1 = "mission/gadgets/gadgetCloud1.png"
image hackCloud = "mission/gadgets/hackCloud.png"
image dramaCumSam = "mission/fx/dramaCumSam.png"
image dramaCumClover = "mission/fx/dramaCumClover.png"
image dramaCumAlex = "mission/fx/dramaCumAlex.png"

transform hackCloud:
    linear 0.7 ypos 130 alpha 0.0

label vibCumming:
    if activeSpy == 1:
        show drama1:
            ypos 70
        show dramaCumSam:
            ypos 70
        with d1
        pause 0.8
        hide drama1
        hide dramaCumSam
        with d1
    if activeSpy == 2:
        show drama1:
            ypos 70
        show dramaCumClover:
            ypos 70
        with d1
        pause 0.8
        hide drama1
        hide dramaCumClover
        with d1
    if activeSpy == 3:
        show drama1:
            ypos 70
        show dramaCumAlex:
            ypos 70
        with d1
        pause 0.8
        hide drama1
        hide dramaCumAlex
        with d1
    return


image agentAlert = "mission/fx/agentAlert.png"
label agentAlert:
    if 1 <= randomBackground <= 3:
        show agentAlert:
            xalign 0.6 yalign 0.37 alpha 1.0
            linear 0.3 yalign 0.34
            linear 0.2 alpha 0.0
        pause 0.5
        hide agentAlert
    return





default hiddenStatus = 0
default activeSpy = 1
default missionProgression = 0
default switchMode = 1
default currentPosition = 0
default interact1 = 0
default interact2 = 0
default bonusAvailable = 0

default samOnMission = False
default cloverOnMission = False
default alexOnMission = False

default target1Underfire = False
default target2Underfire = False

default obst1FoV = 0
default obst2FoV = 0

default randomAgent1 = 0
default randomAgent2 = 0
default randomAgent3 = 0
default randomAgent4 = 0

default randomBoss = 0
default randomBossHP = 3

default normalAmmoCount = 6
default specialBossActive = False

default gunStatus = 0


default randomLoot1 = 0
default randomLoot = 0

default chanceOfControl = 0
default controlCountDown = 4


default currentGadgetSelect = 0


default flashbangSpecial = False




default loot1 = 0
default loot2 = 0
default loot3 = 0
default loot4 = 0
default loot5 = 0
default loot6 = 0


default lootPhone = 0
default lootExam = 0
default lootTrophy = 0
default lootCandle = 0
default lootVase = 0


transform item_drop(pos):
    pos pos
    yoffset 0
    linear 0.3 yoffset -30
    linear 0.2 pos (1280,0)

image dropCash = "gui/dropCash.png"
image dropConsum = "gui/dropConsum.png"
image dropMats = "gui/dropMats.png"
default lootDrop = 0
image bonusLootBG5 = "mission/extra/bonusSuitcase2.png"

image cameraTrigger = "mission/fx/obstCameraTrigger.png"
layeredimage lazerTrigger:
    if activeSpy == 1:
        "mission/fx/obstLazerTriggerGreen.png"
    if activeSpy == 2:
        "mission/fx/obstLazerTriggerRed.png"
    if activeSpy == 3:
        "mission/fx/obstLazerTriggerYellow.png"

label randomLoot:
    $ loot1Chance = renpy.random.randint(1,10)
    if loot1Chance == 10:
        $ randomMats = renpy.random.randint(1,2)
        if randomMats == 1:
            $ loot1 += 1
        if randomMats == 2:
            $ loot2 += 1
        play sound "audio/sfx/jobReward.mp3"
        if 1 <= randomBackground <= 3 and lootLoc == 1:
            show dropMats at item_drop((500,300))
            with d3
            hide dropMats
        if 1 <= randomBackground <= 3 and lootLoc == 2:
            show dropMats at item_drop((730,430))
            with d3
            hide dropMats
        if 4 <= randomBackground <= 7 and lootLoc == 1:
            show dropMats at item_drop((780,500))
            with d3
            hide dropMats
        if 4 <= randomBackground <= 7 and lootLoc == 2:
            show dropMats at item_drop((80,500))
            with d3
            hide dropMats
        if 4 <= randomBackground <= 7 and lootLoc == 3:
            show dropMats at item_drop((910,350))
            with d3
            hide dropMats
        if 4 <= randomBackground <= 7 and lootLoc == 4:
            show dropMats at item_drop((200,150))
            with d3
            hide dropMats
        return
    elif True:
        pass

    $ loot2Chance = renpy.random.randint(1,10)
    if loot2Chance == 10:
        $ loot3 += 1
        play sound "audio/sfx/jobReward.mp3"
        if 1 <= randomBackground <= 3 and lootLoc == 1:
            show dropConsum at item_drop((500,300))
            with d3
            hide dropConsum
        if 1 <= randomBackground <= 3 and lootLoc == 2:
            show dropConsum at item_drop((730,430))
            with d3
            hide dropConsum
        if 4 <= randomBackground <= 7 and lootLoc == 1:
            show dropConsum at item_drop((780,500))
            with d3
            hide dropConsum
        if 4 <= randomBackground <= 7 and lootLoc == 2:
            show dropConsum at item_drop((80,500))
            with d3
            hide dropConsum
        if 4 <= randomBackground <= 7 and lootLoc == 3:
            show dropConsum at item_drop((910,350))
            with d3
            hide dropConsum
        if 4 <= randomBackground <= 7 and lootLoc == 4:
            show dropConsum at item_drop((200,150))
            with d3
            hide dropConsum
        return
    elif True:
        pass
return




default gadgetActive = 0
default glassMissActive = False
default gunMissActive = False
default gunReadyFire = 0
default hookMissActive = False

image gadgetSelectBlue = "gui/gadgets/equipment/gadgetSelectBlue.png"
screen gadgetSelectUI:
    vbox xalign 0.385 yalign 0.96:
        imagebutton:
            idle "gui/gadgets/equipment/gadgetSelectUI.png"
            hover "gui/gadgets/equipment/gadgetSelectUI.png"
            action SetVariable("gadgetActive", 1), Jump("activateGadget")
    vbox xalign 0.44 yalign 0.96:
        imagebutton:
            idle "gui/gadgets/equipment/gadgetSelectUI.png"
            hover "gui/gadgets/equipment/gadgetSelectUI.png"
            action SetVariable("gadgetActive", 2), Jump("activateGadget")
    vbox xalign 0.495 yalign 0.96:
        imagebutton:
            idle "gui/gadgets/equipment/gadgetSelectUI.png"
            hover "gui/gadgets/equipment/gadgetSelectUI.png"
            action SetVariable("gadgetActive", 3), Jump("activateGadget")
    vbox xalign 0.55 yalign 0.96:
        imagebutton:
            idle "gui/gadgets/equipment/gadgetSelectUI.png"
            hover "gui/gadgets/equipment/gadgetSelectUI.png"
            action SetVariable("gadgetActive", 4), Jump("activateGadget")
    vbox xalign 0.605 yalign 0.96:
        imagebutton:
            idle "gui/gadgets/equipment/gadgetSelectUI.png"
            hover "gui/gadgets/equipment/gadgetSelectUI.png"
            action SetVariable("gadgetActive", 5), Jump("activateGadget")
    text "{size=-9}1{/size}" xalign 0.39 yalign 0.999
    text "{size=-9}2{/size}" xalign 0.445 yalign 0.999
    text "{size=-9}3{/size}" xalign 0.495 yalign 0.999
    text "{size=-9}4{/size}" xalign 0.55 yalign 0.999
    text "{size=-9}5{/size}" xalign 0.6 yalign 0.999


    if gadgetVIBActive:
        add "gui/gadgets/equipment/gadgetSelect1.png"
    if gadgetHackActive:
        add "gui/gadgets/equipment/gadgetSelect2.png"
    if gadgetGlassesActive:
        add "gui/gadgets/equipment/gadgetSelect3.png"
    if gadgetGunActive:
        add "gui/gadgets/equipment/gadgetSelect4.png"
    if gadgetHookActive:
        add "gui/gadgets/equipment/gadgetSelect5.png"

screen glassScreen:
    add "gui/gadgets/equipment/glassScreen1.png"

    if 1 <= randomBackground <= 3 and randomGlass == 1 and currentPosition == 0:
        vbox xalign 0.08 yalign 0.42:
            imagebutton:
                idle "mission/interact/secret.png"
                hover "mission/interact/secret-hover.png"
                action Jump("missRandSecret")

    if 4 <= randomBackground <= 7 and randomGlass == 1 and currentPosition == 1:
        vbox xalign 0.5 yalign 0.9:
            imagebutton:
                idle "mission/interact/secret.png"
                hover "mission/interact/secret-hover.png"
                action Jump("missRandSecret")

    if 8 <= randomBackground <= 10 and randomGlass == 1 and currentPosition == 1:
        vbox xalign 0.15 yalign 0.8:
            imagebutton:
                idle "mission/interact/secret.png"
                hover "mission/interact/secret-hover.png"
                action Jump("missRandSecret")

screen gadgetMenu:
    if gadgetVIBActive:
        key "K_1" action SetVariable("gadgetActive", 1), Jump("activateGadget")
    if gadgetHackActive and vibActive == False:
        key "K_2" action SetVariable("gadgetActive", 2), Jump("activateGadget")
    if gadgetGlassesActive and vibActive == False:
        key "K_3" action SetVariable("gadgetActive", 3), Jump("activateGadget")
    if gadgetGunActive and vibActive == False:
        key "K_4" action SetVariable("gadgetActive", 4), Jump("activateGadget")
    if gadgetHookActive and vibActive == False:
        key "K_5" action SetVariable("gadgetActive", 5), Jump("activateGadget")

screen reloadGun:
    text "Press R to load the gun." xalign 0.5 yalign 1.0
    key "K_r" action Jump("reloadGun")

label reloadGun:
    menu:
        "Load Afro Dart" if gadgetAfroDart >= 1:
            $ gadgetAfroDart -= 1
            $ gunReadyFire = 1
            hide screen reloadGun
            play sound "audio/sfx/miscSound1.mp3"
            "Afro Dart Loaded. Ready to fire."
            jump jumpStartScene
        "Load Poison Dart" if gadgetStunDart >= 1:
            $ gadgetStunDart -= 1
            $ gunReadyFire = 2
            hide screen reloadGun
            play sound "audio/sfx/miscSound1.mp3"
            "Poison Dart Loaded. Ready to fire."
            jump jumpStartScene
        "Never mind" if True:
            jump jumpStartScene

label activateGadget:
    $ interSelect = 0
    hide screen gadgetMenu
    hide screen reloadGun
    show screen gadgetSelectUI
    if gadgetActive == 1:
        show gadgetSelectBlue onlayer minigame:
            xalign 0.381 yalign 0.97
        pause 0.4
        $ gadgetActive = 0
        hide screen gadgetSelectUI 
        hide gadgetSelectBlue onlayer minigame
        with d3
        show screen gadgetMenu
        jump vibratorActive
    elif gadgetActive == 2:
        $ interSelect = 2
        show gadgetSelectBlue onlayer minigame:
            xalign 0.381 yalign 0.97
            linear 0.18 xalign 0.44 yalign 0.97
        pause 0.4
        $ gadgetActive = 0
        hide screen gadgetSelectUI 
        hide gadgetSelectBlue onlayer minigame
        with d3
        show screen gadgetMenu
        jump jumpStartScene
    elif gadgetActive == 3:
        if glassMissActive == False:
            $ glassMissActive = True
            show gadgetSelectBlue onlayer minigame:
                xalign 0.381 yalign 0.97
                linear 0.18 xalign 0.494 yalign 0.97
            play sound "audio/sfx/nightVision.mp3"
            pause 0.4
            show screen glassScreen
        elif True:
            $ glassMissActive = False
            $ gadgetActive = 0
            hide screen glassScreen
            with d2
        $ gadgetActive = 0
        hide screen gadgetSelectUI 
        hide gadgetSelectBlue onlayer minigame
        with d3
        show screen gadgetMenu
        jump jumpStartScene
    elif gadgetActive == 4:
        $ gunMissActive = True
        show gadgetSelectBlue onlayer minigame:
            xalign 0.381 yalign 0.97
            linear 0.21 xalign 0.55 yalign 0.97
        pause 0.6
        show screen reloadGun
        $ gadgetActive = 0
        hide screen gadgetSelectUI
        hide gadgetSelectBlue onlayer minigame
        with d3
        show screen gadgetMenu
        jump jumpStartScene
    elif gadgetActive == 5:
        show gadgetSelectBlue onlayer minigame:
            xalign 0.381 yalign 0.97
            linear 0.18 xalign 0.606 yalign 0.97
        pause 0.4
        hide screen gadgetSelectUI 
        hide gadgetSelectBlue onlayer minigame
        with d3
        show screen gadgetMenu
        jump jumpStartScene
    elif True:

        "Something went wrong"

label missRandSecret:
    $ randomGlass = 0
    $ randSecret = renpy.random.randint(1,3)

    if 4 <= task25Stage <= 8 and randSecret == 3:
        $ randSecret = 1

    label missRandSecret2:
        if randSecret == 1:
            $ resourceClothes += 10
            $ medkit += 1
            $ cash += 20
            "There is a small cache hidden here."
            play sound "audio/sfx/itemGot.mp3"
            "You find $20.\nYou find {color=#ffeda6}Clothing{/color} x10\nYou find {color=#ffeda6}Medkit{/color} x1"
            $ randomGlass = 0
            jump jumpStartScene
        if randSecret == 2:
            $ resourceWater += 5
            $ cash += 25
            "There is a small cache hidden here."
            play sound "audio/sfx/itemGot.mp3"
            "You find $25.\nYou find {color=#ffeda6}Water{/color} x5\n{color=#ffeda6}"
            $ randomGlass = 0
            jump jumpStartScene
        if randSecret == 3:
            "You find a secret shortcut! Take it?"
            menu:
                "Take shortcut" if True:
                    $ randomGlass = 0
                    $ glassMissActive = False
                    $ gadgetActive = 0
                    hide screen glassScreen
                    if missionProgression <= 7:
                        $ missionProgression = 7
                        jump missionBegin
                    elif True:
                        $ missionProgression = 9
                        jump missionBegin
                "Ignore it" if True:
                    $ randomGlass = 0
                    $ glassMissActive = False
                    $ gadgetActive = 0
                    hide screen glassScreen
                    with d2
                    jump jumpStartScene





layeredimage globalImageCastle:

    if missionSetting == "Castle" and randomBackground == 1:
        "mission/castleDistant1.jpg"
    if missionSetting == "Castle" and randomBackground == 2:
        "mission/castleDistant2.jpg"
    if missionSetting == "Castle" and randomBackground == 3:
        "mission/castleDistant3.jpg"
    if missionSetting == "Castle" and randomBackground == 4:
        "mission/castleSide1.jpg"
    if missionSetting == "Castle" and randomBackground == 5:
        "mission/castleSide2.jpg"
    if missionSetting == "Castle" and randomBackground == 6:
        "mission/castleSide3.jpg"
    if missionSetting == "Castle" and randomBackground == 7:
        "mission/castleSide4.jpg"
    if missionSetting == "Castle" and randomBackground == 8:
        "mission/castle3Var1.jpg"
    if missionSetting == "Castle" and randomBackground == 9:
        "mission/castle3Var2.jpg"
    if missionSetting == "Castle" and randomBackground == 10:
        "mission/castle3Var3.jpg"
    if missionSetting == "Castle" and randomBackground == 11:
        "mission/castleBalcony.jpg"
    if missionSetting == "Castle" and randomBackground == 12:
        "mission/castleLift.jpg"


    if 1 <= randomBackground <= 3 and randomExit == 1:
        "mission/castle/exit/exit1.png"
    if 1 <= randomBackground <= 3 and randomExit == 2:
        "mission/castle/exit/exit2.png"
    if 1 <= randomBackground <= 3 and randomExit == 3:
        "mission/castle/exit/exit3.png"

    if 4 <= randomBackground <= 7 and randomExit == 1:
        "mission/castle/exit/bg2/exit1.png"
    if 4 <= randomBackground <= 7 and randomExit == 2:
        "mission/castle/exit/bg2/exit2.png"
    if 4 <= randomBackground <= 7 and randomExit == 3:
        "mission/castle/exit/bg2/exit3.png"

    if 8 <= randomBackground <= 10 and randomExit == 1:
        "mission/castle/exit/bg3/exit1.png"
    if 8 <= randomBackground <= 10 and randomExit == 2:
        "mission/castle/exit/bg3/exit2.png"
    if 8 <= randomBackground <= 10 and randomExit == 3:
        "mission/castle/exit/bg3/exit3.png"





    if 11 <= randomBackground <= 11 and randomExit >= 1:
        "mission/castle/exit/bg4/exit3.png"

    if 7 <= randomBackground <= 7 and randomExit == 1:
        "mission/castle/exit/bg2/exit1.png"
    if 7 <= randomBackground <= 7 and randomExit == 2:
        "mission/castle/exit/bg2/exit2Lib.png"
    if 7 <= randomBackground <= 7 and randomExit == 3:
        "mission/castle/exit/bg2/exit3Lib.png"


    if 1 <= randomBackground <= 3 and frontExit == 8:
        "mission/castle/exit/frontExit.png"

    if 4 <= randomBackground <= 7 and frontExit == 8:
        "mission/castle/exit/bg2/frontExit.png"

    if 8 <= randomBackground <= 10 and frontExit == 8:
        "mission/castle/exit/bg3/frontExit.png" xpos 600 ypos 250


    if 1 <= randomBackground <= 3 and bonusExit == 10:
        "mission/castle/exit/bnsExit1.png"
    if 8 <= randomBackground <= 10 and bonusExit == 10:
        "mission/castle/exit/bg3/bnsExit1.png"


    if 1 <= randomBackground <= 3 and randomCover1 == 1:
        "mission/castle/cover/chest1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 2:
        "mission/castle/cover/pillar1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 3:
        "mission/castle/cover/statue1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 4:
        "mission/castle/cover/bust1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 5:
        "mission/castle/cover/statue2.png"


    if 1 <= randomBackground <= 3 and randomCover2 == 1:
        "mission/castle/cover/table2.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 2:
        "mission/castle/cover/armor2.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 3:
        "mission/castle/cover/armor2.png"
    if 1 <= randomBackground <= 3 and randomCover2 >= 4:
        "mission/castle/cover/armor2.png"


    if 1 <= randomBackground <= 3 and randomCover2 == 1 and randomLoot == 1:
        "mission/castle/cover/loot1.png"
    elif 1 <= randomBackground <= 3 and randomCover2 == 1 and randomLoot == 2:
        "mission/castle/cover/loot2.png"



    if 1 <= randomBackground <= 3 and interact1 == 8:
        "mission/castle/interactable/chandelier.png" xpos 2700 ypos 0
    if 1 <= randomBackground <= 3 and interact2 == 8:
        "mission/castle/interactable/camera1.png" xpos 3450 ypos 755
    if 1 <= randomBackground <= 3 and interact2 == 8.1:
        "mission/castle/interactable/camera2.png" xpos 3450 ypos 755



    if 4 <= randomBackground <= 7 and interact1 == 8:
        "mission/castle/interactable/chandelier2.png" xpos 4050 ypos 0



    if 8 <= randomBackground <= 10 and interact1 == 8:
        "mission/castle/interactable/chandelier3.png" xpos 1940 ypos 90 zoom 0.63



    if 4 <= randomBackground <= 7 and randomCover1 == 1:
        "mission/castle/cover/bg2/armor1.png" xpos 3650 ypos 1750
    if 4 <= randomBackground <= 7 and randomCover1 == 2:
        "mission/castle/cover/bg2/bust1.png" xpos 3700 ypos 2000
    if 4 <= randomBackground <= 7 and randomCover1 == 3:
        "mission/castle/cover/bg2/statue1.png" xpos 3630 ypos 1790
    if 4 <= randomBackground <= 7 and randomCover1 == 4:
        "mission/castle/cover/bg2/statue1.png" xpos 3630 ypos 1790
    if 4 <= randomBackground <= 7 and randomCover1 == 5:
        "mission/castle/cover/bg2/statue2.png" xpos 3650 ypos 1950

    if 4 <= randomBackground <= 7 and randomCover2 == 1:
        "mission/castle/cover/bg2/table1.png" xpos 1800 ypos 2160
    if 4 <= randomBackground <= 7 and randomCover2 == 2:
        "mission/castle/cover/bg2/chest2.png" xpos 1460 ypos 2330
    if 4 <= randomBackground <= 7 and randomCover2 == 3:
        "mission/castle/cover/bg2/armor1.png" xpos 1810 ypos 1800
    if 4 <= randomBackground <= 7 and randomCover2 == 4:
        "mission/castle/cover/bg2/bust1.png" xpos 1830 ypos 2040
    if 4 <= randomBackground <= 7 and randomCover2 == 5:
        "mission/castle/cover/bg2/statue1.png" xpos 1700 ypos 1800


    if 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 1:
        "mission/castle/cover/bg2/loot1.png" xpos 1800 ypos 2160
    elif 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 2:
        "mission/castle/cover/bg2/loot2.png" xpos 1800 ypos 2160


    if 8 <= randomBackground <= 10 and randomCover1 == 1:
        "mission/castle/cover/bg3/table1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 2:
        "mission/castle/cover/bg3/armor1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 3:
        "mission/castle/cover/bg3/pillar1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 4:
        "mission/castle/cover/bg3/plant1.png"
    if 8 <= randomBackground <= 10 and randomCover1 >= 5:
        "mission/castle/cover/bg3/statue1.png"


    if 8 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 1:
        "mission/castle/cover/bg3/loot1.png"
    elif 8 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 2:
        "mission/castle/cover/bg3/loot2.png"


    if 8 <= randomBackground <= 10 and randomCover2 == 1:
        "mission/castle/cover/bg3/chest2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 2:
        "mission/castle/cover/bg3/bust2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 3:
        "mission/castle/cover/bg3/armor2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 4:
        "mission/castle/cover/bg3/pillar2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 5:
        "mission/castle/cover/bg3/statue2.png"


    if 11 <= randomBackground <= 11 and randomCover1 >= 1:
        "mission/castle/cover/bg4/chest1.png"

    if 11 <= randomBackground <= 11 and randomCover2 == 1:
        "mission/castle/cover/bg4/armorFlag2.png"
    if 11 <= randomBackground <= 11 and randomCover2 == 2:
        "mission/castle/cover/bg4/bust2.png"
    if 11 <= randomBackground <= 11 and randomCover2 == 3:
        "mission/castle/cover/bg4/chest2.png"
    if 11 <= randomBackground <= 11 and randomCover2 == 4:
        "mission/castle/cover/bg4/statue2.png"
    if 11 <= randomBackground <= 11 and randomCover2 == 5:
        "mission/castle/cover/bg4/armor2.png"


    if 11 <= randomBackground <= 11 and 0 <= currentPosition <= 1:
        "mission/castle/decor/balcony.png"

layeredimage globalImage:

    if randomBackground == 1:
        "mission/schoolDistant1.jpg"
    if randomBackground == 2:
        "mission/schoolDistant2.jpg"
    if randomBackground == 3:
        "mission/schoolDistant3.jpg"
    if randomBackground == 4:
        "mission/schoolSide1.jpg"
    if randomBackground == 5:
        "mission/schoolSide2.jpg"
    if randomBackground == 6:
        "mission/schoolSide3.jpg"
    if randomBackground == 7:
        "mission/schoolSide4.jpg"
    if randomBackground == 8:
        "mission/school3Var1.jpg"
    if randomBackground == 9:
        "mission/school3Var2.jpg"
    if randomBackground == 10:
        "mission/school3Var3.jpg"
    if randomBackground == 11:
        "mission/schoolBalcony.jpg"
    if randomBackground == 12:
        "mission/schoolLift.jpg"


    if 1 <= randomBackground <= 3 and randomExit == 1:
        "mission/school/exit/exit1.png"
    if 1 <= randomBackground <= 3 and randomExit == 2:
        "mission/school/exit/exit2.png"
    if 1 <= randomBackground <= 3 and randomExit == 3:
        "mission/school/exit/exit3.png"


    if 4 <= randomBackground <= 6 and randomExit == 1:
        "mission/school/exit/bg2/exit1.png"
    if 4 <= randomBackground <= 6 and randomExit == 2:
        "mission/school/exit/bg2/exit2.png"
    if 4 <= randomBackground <= 6 and randomExit == 3:
        "mission/school/exit/bg2/exit3.png"

    if 7 <= randomBackground <= 7 and randomExit == 1:
        "mission/school/exit/bg2/exit1.png"
    if 7 <= randomBackground <= 7 and randomExit == 2:
        "mission/school/exit/bg2/exit2Lib.png"
    if 7 <= randomBackground <= 7 and randomExit == 3:
        "mission/school/exit/bg2/exit3Lib.png"

    if 8 <= randomBackground <= 10 and randomExit == 1:
        "mission/school/exit/bg3/exit1.png"
    if 8 <= randomBackground <= 10 and randomExit == 2:
        "mission/school/exit/bg3/exit2.png"
    if 8 <= randomBackground <= 10 and randomExit == 3:
        "mission/school/exit/bg3/exit3.png"


    if 1 <= randomBackground <= 3 and frontExit == 8:
        "mission/school/exit/frontExit1.png"

    if 4 <= randomBackground <= 7 and frontExit == 8:
        "mission/school/exit/bg2/frontExit.png"

    if 8 <= randomBackground <= 10 and frontExit == 8:
        "mission/school/exit/bg3/frontExit.png" xpos 620 ypos 420


    if 1 <= randomBackground <= 3 and bonusExit == 10:
        "mission/school/exit/bnsExit1.png"


    if 1 <= randomBackground <= 3 and randomCover1 == 1:
        "mission/school/cover/bg1/locker.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 2:
        "mission/school/cover/bg1/trophy.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 3:
        "mission/school/cover/bg1/fountain1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 4 and month != 12:
        "mission/school/cover/bg1/plant1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 4 and month == 12:
        "mission/school/cover/bg1/xmastree1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 5:
        "mission/school/cover/bg1/vendingSide2.png"


    if 1 <= randomBackground <= 3 and randomCover2 == 1:
        "mission/school/cover/bg1/vending.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 2:
        "mission/school/cover/bg1/fountain2.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 3:
        "mission/school/cover/bg1/chairs1.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 4:
        "mission/school/cover/bg1/trash1.png"



    if 4 <= randomBackground <= 7 and interact1 == 8:
        "mission/school/interactable/light1.png" xpos 4000 ypos 0


    if 4 <= randomBackground <= 6 and randomCover1 == 1:
        "mission/school/cover/bg2/lockerSide2.png"
    if 4 <= randomBackground <= 6 and randomCover1 == 2:
        "mission/school/cover/bg2/vendingSide1.png"
    if 4 <= randomBackground <= 6 and randomCover1 >= 3:
        "mission/school/cover/bg2/trophySide.png"

    if 7 <= randomBackground <= 7 and randomCover1 == 1:
        "mission/school/cover/bg2/bookcase1.png"
    if 7 <= randomBackground <= 7 and randomCover1 == 2:
        "mission/school/cover/bg2/bookcase2.png"
    if 7 <= randomBackground <= 7 and randomCover1 == 3:
        "mission/school/cover/bg2/bookcase3.png"
    if 7 <= randomBackground <= 7 and randomCover1 == 4:
        "mission/school/cover/bg2/bookcase4.png"
    if 7 <= randomBackground <= 7 and randomCover1 == 5:
        "mission/school/cover/bg2/bookcase5.png"



    if 4 <= randomBackground <= 6 and randomCover2 == 1:
        "mission/school/cover/bg2/table.png"
    if 4 <= randomBackground <= 6 and randomCover2 == 2:
        "mission/school/cover/bg2/trash.png"
    if 4 <= randomBackground <= 6 and randomCover2 == 3:
        "mission/school/cover/bg2/fountain.png"
    if 4 <= randomBackground <= 6 and randomCover2 == 4 and month != 12:
        "mission/school/cover/bg2/plant.png"
    if 4 <= randomBackground <= 6 and randomCover2 == 4 and month == 12:
        "mission/school/cover/bg2/xmastree.png"
    if 4 <= randomBackground <= 6 and randomCover2 == 5:
        "mission/school/cover/bg2/trophy.png"
    if 4 <= randomBackground <= 6 and 2 <=  task13Stage <= 2.1:
        "mission/extra/lockerSam.png"


    if 7 <= randomBackground <= 7 and randomCover2 == 1:
        "mission/school/cover/bg2/table.png"
    if 7 <= randomBackground <= 7 and randomCover2 == 2:
        "mission/school/cover/bg2/trash.png"
    if 7 <= randomBackground <= 7 and randomCover2 == 3:
        "mission/school/cover/bg2/chairs.png"
    if 7 <= randomBackground <= 7 and randomCover2 ==4:
        "mission/school/cover/bg2/books1.png"
    if 7 <= randomBackground <= 7 and randomCover2 == 5 and month != 12:
        "mission/school/cover/bg2/trolley.png"
    if 7 <= randomBackground <= 7 and randomCover2 == 5 and month == 12:
        "mission/school/cover/xmastree.png"


    if 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 1:
        "mission/school/cover/bg2/loot1.png"
    if 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 2:
        "mission/school/cover/bg2/loot2.png"


    if 1 <= randomBackground <= 3 and randomCover2 == 1:
        "mission/school/cover/bg1/vending.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 2:
        "mission/school/cover/bg1/fountain2.png"


    if 8 <= randomBackground <= 10 and randomCover1 == 1:
        "mission/school/cover/bg3/locker1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 2:
        "mission/school/cover/bg3/soda1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 3:
        "mission/school/cover/bg3/trophy1.png"
    if 8 <= randomBackground <= 10 and randomCover1 >= 4:
        "mission/school/cover/bg3/fountain1.png"


    if 8 <= randomBackground <= 10 and randomCover2 == 1:
        "mission/school/cover/bg3/trash2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 2:
        "mission/school/cover/bg3/chairs2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 3:
        "mission/school/cover/bg3/fountain2.png"
    if 8 <= randomBackground <= 10 and randomCover2 >= 4 and month != 12:
        "mission/school/cover/bg3/soda2.png"
    if 8 <= randomBackground <= 10 and randomCover2 >= 4 and month == 12:
        "mission/school/cover/bg3/xmastree2.png"


    if 11 <= randomBackground <= 11 and currentPosition <= 1:
        "mission/school/decor/balcony.png"


    if 11 <= randomBackground <= 11 and randomCover1 >= 1:
        "mission/school/cover/bg4/fountain1.png"


    if 11 <= randomBackground <= 11 and randomCover2 >= 1:
        "mission/school/cover/bg4/chairs2.png"


    if 1 <= randomBackground <= 3 and bonusAvailable == 1:
        "mission/extra/bonusSuitcase.png"


    if missionProgression >= 2 and acesBounty3 == 1 and 4 <= randomBackground <= 7:
        "mission/extra/vault.png"




    if 1 <= randomBackground <= 3 and interact2 == 8:
        "mission/school/interactable/camera1.png" xpos 3450 ypos 775


    if 4 <= randomBackground <= 7 and interact3 == 8:
        "mission/school/interactable/light1.png" xpos 4000 ypos 0

image musicPillar1:
    "mission/database/cover/bg3/music1.png"
    pause 0.3
    "mission/database/cover/bg3/music2.png"
    pause 0.3
    "mission/database/cover/bg3/music3.png"
    pause 0.3
    "mission/database/cover/bg3/music4.png"
    pause 0.3
    repeat

image musicBall1:
    "mission/database/interactable/ball1.png"
    pause 0.3
    "mission/database/interactable/ball2.png"
    pause 0.3
    "mission/database/interactable/ball3.png"
    pause 0.3
    repeat

layeredimage globalImageDatabase:

    if missionSetting == "Database" and randomBackground == 1:
        "mission/databaseDistant1.jpg"
    if missionSetting == "Database" and randomBackground == 2:
        "mission/databaseDistant2.jpg"
    if missionSetting == "Database" and randomBackground == 3:
        "mission/databaseDistant3.jpg"
    if missionSetting == "Database" and randomBackground == 4:
        "mission/databaseSide1.jpg"
    if missionSetting == "Database" and randomBackground == 5:
        "mission/databaseSide2.jpg"
    if missionSetting == "Database" and randomBackground == 6:
        "mission/databaseSide3.jpg"
    if missionSetting == "Database" and randomBackground == 7:
        "mission/databaseSide4.jpg"
    if missionSetting == "Database" and randomBackground == 8:
        "mission/database3Var1.jpg"
    if missionSetting == "Database" and randomBackground == 9:
        "mission/database3Var2.jpg"
    if missionSetting == "Database" and randomBackground == 10:
        "mission/database3Var3.jpg"
    if missionSetting == "Database" and randomBackground == 11:
        "mission/dataBalcony.jpg"
    if missionSetting == "Database" and randomBackground == 12:
        "mission/databaseLift.jpg"


    if task12Stage == 3 and missionProgression == 10:
        "mission/database/exit/niecePrison.png"


    if 4 <= randomBackground <= 7 and randomExit == 1:
        "mission/database/exit/bg2/exit1.png"
    if 4 <= randomBackground <= 7 and randomExit == 2:
        "mission/database/exit/bg2/exit2.png"
    if 4 <= randomBackground <= 7 and randomExit == 3:
        "mission/database/exit/bg2/exit3.png"

    if 7 <= randomBackground <= 7 and randomExit == 1:
        "mission/database/exit/bg2/exit1.png"
    if 7 <= randomBackground <= 7 and randomExit == 2:
        "mission/database/exit/bg2/exit2Lib.png"
    if 7 <= randomBackground <= 7 and randomExit == 3:
        "mission/database/exit/bg2/exit3Lib.png"

    if 1 <= randomBackground <= 3 and frontExit == 8:
        "mission/database/exit/frontExit.png"

    if 4 <= randomBackground <= 7 and frontExit == 8:
        "mission/database/exit/bg2/frontExit.png"

    if 8 <= randomBackground <= 10 and frontExit == 8:
        "mission/database/exit/bg3/frontExit.png"


    if 1 <= randomBackground <= 3 and bonusExit == 10:
        "mission/database/exit/bnsExit1.png"


    if 1 <= randomBackground <= 3 and randomCover1 == 1:
        "mission/database/cover/table.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 2:
        "mission/database/cover/arcade1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 3:
        "mission/database/cover/cube2.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 4:
        "mission/database/cover/dj1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 5:
        "mission/database/cover/speaker1.png"


    if 1 <= randomBackground <= 3 and randomCover1 == 1 and randomLoot == 1:
        "mission/database/cover/loot1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 1 and randomLoot == 2:
        "mission/database/cover/loot1.png"


    if 1 <= randomBackground <= 3 and randomCover2 == 1:
        "mission/database/cover/arcade2.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 2:
        "mission/database/cover/cube3.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 3:
        "mission/database/cover/cube4.png"
    if 1 <= randomBackground <= 3 and randomCover2 >= 4:
        "mission/database/cover/speaker2.png"



    if 4 <= randomBackground <= 7 and interact1 == 8:
        "musicBall1" xpos 4250 ypos 0


    if 4 <= randomBackground <= 7 and randomCover1 == 1:
        "mission/database/cover/bg2/speaker1.png" xpos 3660 ypos 1950
    if 4 <= randomBackground <= 7 and randomCover1 == 2:
        "mission/database/cover/bg2/hologram1.png" xpos 3630 ypos 1970
    if 4 <= randomBackground <= 7 and randomCover1 == 3:
        "mission/database/cover/bg2/cube1.png" xpos 3539 ypos 1820
    if 4 <= randomBackground <= 7 and randomCover1 >= 4:
        "mission/database/cover/bg2/arcade1.png" xpos 3690 ypos 1940


    if 4 <= randomBackground <= 7 and randomCover2 == 1:
        "mission/database/cover/bg2/table.png" xpos 1800 ypos 2200
    if 4 <= randomBackground <= 7 and randomCover2 == 2:
        "mission/database/cover/bg2/dj1.png" xpos 1330 ypos 1835
    if 4 <= randomBackground <= 7 and randomCover2 == 3:
        "mission/database/cover/bg2/hologram2.png" xpos 1650 ypos 2030
    if 4 <= randomBackground <= 7 and randomCover2 == 4:
        "mission/database/cover/bg2/cube2.png" xpos 1590 ypos 1900
    if 4 <= randomBackground <= 7 and randomCover2 >= 5:
        "mission/database/cover/bg2/pirate1.png" xpos 1620 ypos 1880


    if 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 1:
        "mission/database/cover/bg2/loot1.png" xpos 1800 ypos 2200
    if 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 2:
        "mission/database/cover/bg2/loot2.png" xpos 1800 ypos 2200


    if 8 <= randomBackground <= 10 and randomCover1 == 1:
        "mission/database/cover/bg3/table.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 2:
        "mission/database/cover/bg3/arcade1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 3:
        "mission/database/cover/bg3/cube1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 4:
        "mission/database/cover/bg3/cube2.png"
    if 8 <= randomBackground <= 10 and randomCover1 >= 5:
        "musicPillar1"


    if 8 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 1:
        "mission/database/cover/bg3/loot1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 2:
        "mission/database/cover/bg3/loot2.png"


    if 8 <= randomBackground <= 10 and randomCover2 == 1:
        "mission/database/cover/bg3/arcade2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 2:
        "mission/database/cover/bg3/cube3.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 3:
        "mission/database/cover/bg3/cube4.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 4:
        "mission/database/cover/bg3/dj1.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 5:
        "mission/database/cover/bg3/speaker1.png"


    if 8 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 1:
        "mission/database/cover/bg3/loot1.png"


    if 11 <= randomBackground <= 11 and currentPosition <= 1:
        "mission/database/decor/balcony.png"


    if 11 <= randomBackground <= 11 and randomCover1 >= 1:
        "mission/database/cover/bg4/girl.png"


    if 11 <= randomBackground <= 11 and randomCover2 >= 1:
        "mission/database/cover/bg4/music2.png"

    if task15Stage == 1 and task15Music == False and 4 <= randomBackground <= 7:
        "mission/extra/vault.png"


    if missionProgression >= 2 and acesBounty1 == 1 and 4 <= randomBackground <= 7:
        "mission/extra/vault.png"





image magicwall:
    "mission/fx/magicwall.png"
    pause 0.3
    "mission/fx/magicwall2.png"
    pause 0.3
    "mission/fx/magicwall3.png"
    pause 0.3
    repeat

image magicwall2:
    "mission/fx/magicwallRed.png"
    pause 0.3
    "mission/fx/magicwallRed2.png"
    pause 0.3
    "mission/fx/magicwallRed3.png"
    pause 0.3
    repeat

image magicwall3:
    "mission/fx/magicwallGreen.png"
    pause 0.3
    "mission/fx/magicwallGreen2.png"
    pause 0.3
    "mission/fx/magicwallGreen3.png"
    pause 0.3
    repeat

layeredimage globalImageFaire:

    if missionSetting == "Faire" and randomBackground == 1:
        "mission/faireDistant1.jpg"
    if missionSetting == "Faire" and randomBackground == 2:
        "mission/faireDistant2.jpg"
    if missionSetting == "Faire" and randomBackground == 3:
        "mission/faireDistant3.jpg"
    if missionSetting == "Faire" and randomBackground == 4:
        "mission/faireSide1.jpg"
    if missionSetting == "Faire" and randomBackground == 5:
        "mission/faireSide2.jpg"
    if missionSetting == "Faire" and randomBackground == 6:
        "mission/faireSide3.jpg"
    if missionSetting == "Faire" and randomBackground == 7:
        "mission/faireSide4.jpg"
    if missionSetting == "Faire" and randomBackground == 8:
        "mission/faire3Var1.jpg"
    if missionSetting == "Faire" and randomBackground == 9:
        "mission/faire3Var2.jpg"
    if missionSetting == "Faire" and randomBackground == 10:
        "mission/faire3Var3.jpg"
    if missionSetting == "Faire" and randomBackground == 11:
        "mission/parkBalcony.jpg"
    if missionSetting == "Faire" and randomBackground == 12:
        "mission/faireLift.jpg"


    if 1 <= randomBackground <= 3 and randomExit == 1:
        "mission/faire/exit/exit1.png"
    if 1 <= randomBackground <= 3 and randomExit == 2:
        "mission/faire/exit/exit2.png"
    if 1 <= randomBackground <= 3 and randomExit == 3:
        "mission/faire/exit/exit3.png"

    if 4 <= randomBackground <= 7 and randomExit == 1:
        "mission/faire/exit/bg2/exit1.png"
    if 4 <= randomBackground <= 7 and randomExit == 2:
        "mission/faire/exit/bg2/exit2.png"
    if 4 <= randomBackground <= 7 and randomExit == 3:
        "mission/faire/exit/bg2/exit3.png"

    if 7 <= randomBackground <= 7 and randomExit == 1:
        "mission/faire/exit/bg2/exit1.png"
    if 7 <= randomBackground <= 7 and randomExit == 2:
        "mission/faire/exit/bg2/exit2Lib.png"
    if 7 <= randomBackground <= 7 and randomExit == 3:
        "mission/faire/exit/bg2/exit3Lib.png"

    if 1 <= randomBackground <= 3 and frontExit == 8:
        "mission/faire/exit/frontExit.png"

    if 4 <= randomBackground <= 7 and frontExit == 8:
        "mission/faire/exit/bg2/frontExit.png"

    if 8 <= randomBackground <= 10 and frontExit == 8:
        "mission/faire/exit/bg3/frontExit.png" xpos 645 ypos 305


    if 1 <= randomBackground <= 3 and bonusExit == 10:
        "mission/faire/exit/bnsExit1.png"


    if 1 <= randomBackground <= 3 and randomCover1 == 1:
        "mission/faire/cover/pedestal.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 2:
        "mission/faire/cover/hotdog1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 3:
        "mission/faire/cover/popcorn1.png"
    if 1 <= randomBackground <= 3 and randomCover1 == 4:
        "mission/faire/cover/statue1.png"
    if 1 <= randomBackground <= 3 and randomCover1 >= 5:
        "mission/faire/cover/tickets1.png"


    if 1 <= randomBackground <= 3 and randomCover2 == 1:
        "mission/faire/cover/hotdog2.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 2:
        "mission/faire/cover/icecream.png"
    if 1 <= randomBackground <= 3 and randomCover2 == 3:
        "mission/faire/cover/popcorn2.png"
    if 1 <= randomBackground <= 3 and randomCover2 >= 4:
        "mission/faire/cover/tickets2.png"


    if 1 <= randomBackground <= 3 and randomCover1 == 1 and randomLoot == 1:
        "mission/faire/cover/loot1.png"











    if 4 <= randomBackground <= 7 and randomCover1 == 1:
        "mission/faire/cover/bg2/icecream.png" xpos 3490 ypos 1480
    if 4 <= randomBackground <= 7 and randomCover1 == 2:
        "mission/faire/cover/bg2/cotton.png" xpos 3400 ypos 1460
    if 4 <= randomBackground <= 7 and randomCover1 == 3:
        "mission/faire/cover/bg2/cookies.png" xpos 3300 ypos 1540
    if 4 <= randomBackground <= 7 and randomCover1 >= 4:
        "mission/faire/cover/bg2/popcorn.png" xpos 3480 ypos 1950


    if 4 <= randomBackground <= 7 and randomCover2 == 1:
        "mission/faire/cover/bg2/pedestal.png" xpos 1800 ypos 2000
    if 4 <= randomBackground <= 7 and randomCover2 == 2:
        "mission/faire/cover/bg2/icecream.png" xpos 1600 ypos 1510
    if 4 <= randomBackground <= 7 and randomCover2 == 3:
        "mission/faire/cover/bg2/cotton.png" xpos 1500 ypos 1450
    if 4 <= randomBackground <= 7 and randomCover2 >= 4:
        "mission/faire/cover/bg2/cookies.png" xpos 1500 ypos 1550


    if 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 1:
        "mission/faire/cover/bg2/loot1.png" xpos 1800 ypos 2000


    if 8 <= randomBackground <= 10 and randomCover1 == 1:
        "mission/faire/cover/bg3/pedestal.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 2:
        "mission/faire/cover/bg3/hotdog1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 3:
        "mission/faire/cover/bg3/popcorn1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 4:
        "mission/faire/cover/bg3/tickets1.png"
    if 8 <= randomBackground <= 10 and randomCover1 == 5:
        "mission/faire/cover/bg3/cotton1.png"


    if 8 <= randomBackground <= 10 and randomCover2 == 1:
        "mission/faire/cover/bg3/statue2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 2:
        "mission/faire/cover/bg3/hotdog2.png"
    if 8 <= randomBackground <= 10 and randomCover2 == 3:
        "mission/faire/cover/bg3/popcorn2.png"
    if 8 <= randomBackground <= 10 and randomCover2 >= 4:
        "mission/faire/cover/bg3/tickets2.png"


    if 7 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 1:
        "mission/faire/cover/bg3/loot1.png"


    if 11 <= randomBackground <= 11 and randomCover1 >= 1:
        "mission/faire/cover/bg4/cover1.png"


    if 11 <= randomBackground <= 11 and randomCover2 == 1:
        "mission/faire/cover/bg4/popcorn.png"
    if 11 <= randomBackground <= 11 and randomCover2 == 2:
        "mission/faire/cover/bg4/clown.png"
    if 11 <= randomBackground <= 11 and randomCover2 >= 3:
        "mission/faire/cover/bg4/hotdog.png"


    if missionProgression >= 2 and acesBounty2 == 1 and 4 <= randomBackground <= 7:
        "mission/extra/vault.png"

    if task15Stage == 1 and task15Fireworks == False and 4 <= randomBackground <= 7:
        "mission/extra/vault.png"



layeredimage globalImageWOOHP:

    if missionSetting == "WOOHP" and randomBackground == 1:
        "mission/WOOHPDistant1.jpg"
    if missionSetting == "WOOHP" and randomBackground == 2:
        "mission/WOOHPDistant2.jpg"
    if missionSetting == "WOOHP" and randomBackground == 3:
        "mission/WOOHPDistant3.jpg"
    if missionSetting == "WOOHP" and randomBackground == 4:
        "mission/WOOHPSide1.jpg"
    if missionSetting == "WOOHP" and randomBackground == 5:
        "mission/WOOHPSide2.jpg"
    if missionSetting == "WOOHP" and randomBackground == 6:
        "mission/WOOHPSide3.jpg"
    if missionSetting == "WOOHP" and randomBackground == 7:
        "mission/WOOHPSide4.jpg"
    if missionSetting == "WOOHP" and randomBackground == 8:
        "mission/WOOHP3Var1.jpg"
    if missionSetting == "WOOHP" and randomBackground == 9:
        "mission/WOOHP3Var2.jpg"
    if missionSetting == "WOOHP" and randomBackground == 10:
        "mission/WOOHP3Var3.jpg"
    if missionSetting == "WOOHP" and randomBackground == 11:
        "mission/WOOHPBalcony.jpg"     
    if missionSetting == "WOOHP" and randomBackground == 12:
        "mission/WOOHPLift.jpg"


    if 1 <= randomBackground <= 3 and randomExit == 1:
        "mission/WOOHP/exit/exit1.png"
    if 1 <= randomBackground <= 3 and randomExit == 2:
        "mission/WOOHP/exit/exit2.png"
    if 1 <= randomBackground <= 3 and randomExit == 3:
        "mission/WOOHP/exit/exit3.png"

    if 4 <= randomBackground <= 7 and randomExit == 1:
        "mission/WOOHP/exit/bg2/exit1.png"
    if 4 <= randomBackground <= 7 and randomExit == 2:
        "mission/WOOHP/exit/bg2/exit2.png"
    if 4 <= randomBackground <= 7 and randomExit == 3:
        "mission/WOOHP/exit/bg2/exit3.png"

    if 8 <= randomBackground <= 10 and randomExit == 1:
        "mission/WOOHP/exit/bg3/exit1.png"
    if 8 <= randomBackground <= 10 and randomExit == 2:
        "mission/WOOHP/exit/bg3/exit2.png"
    if 8 <= randomBackground <= 10 and randomExit == 3:
        "mission/WOOHP/exit/bg3/exit3.png"





    if 11 <= randomBackground <= 11 and randomExit >= 1:
        "mission/WOOHP/exit/bg4/exit3.png"

    if 7 <= randomBackground <= 7 and randomExit == 1:
        "mission/WOOHP/exit/bg2/exit1.png"
    if 7 <= randomBackground <= 7 and randomExit == 2:
        "mission/WOOHP/exit/bg2/exit2Lib.png"
    if 7 <= randomBackground <= 7 and randomExit == 3:
        "mission/WOOHP/exit/bg2/exit3Lib.png"

    if 1 <= randomBackground <= 3 and frontExit == 8:
        "mission/WOOHP/exit/frontExit.png"

    if 4 <= randomBackground <= 7 and frontExit == 8:
        "mission/WOOHP/exit/bg2/frontExit.png"

    if 8 <= randomBackground <= 10 and frontExit == 8:
        "mission/WOOHP/exit/bg3/frontExit.png"


    if 1 <= randomBackground <= 3 and bonusExit == 10:
        "mission/WOOHP/exit/bnsExit1.png"
    if 8 <= randomBackground <= 10 and bonusExit == 10:
        "mission/WOOHP/exit/bg3/bnsExit1.png"


    if 1 <= randomBackground <= 3 and randomCover1 >= 1:
        "mission/WOOHP/cover/desk1.png"


    if 1 <= randomBackground <= 3 and randomCover2 >= 1:
        "mission/WOOHP/cover/desk2.png"


    if 1 <= randomBackground <= 3 and randomCover2 == 1 and randomLoot == 1:
        "mission/WOOHP/cover/loot1.png"
    elif 1 <= randomBackground <= 3 and randomCover2 == 1 and randomLoot == 2:
        "mission/WOOHP/cover/loot2.png"



    if 1 <= randomBackground <= 3 and interact1 == 8:
        "mission/WOOHP/interactable/chandelier.png" xpos 2700 ypos 0
    if 1 <= randomBackground <= 3 and interact2 == 8:
        "mission/WOOHP/interactable/camera1.png" xpos 3450 ypos 755
    if 1 <= randomBackground <= 3 and interact2 == 8.1:
        "mission/WOOHP/interactable/camera2.png" xpos 3450 ypos 755



    if 4 <= randomBackground <= 7 and interact1 == 8:
        "mission/WOOHP/interactable/chandelier2.png" xpos 4050 ypos 0



    if 8 <= randomBackground <= 10 and interact1 == 8:
        "mission/WOOHP/interactable/chandelier3.png" xpos 1840 ypos 90 zoom 0.63



    if 4 <= randomBackground <= 7 and randomCover1 >= 1:
        "mission/WOOHP/cover/bg2/power1.png" xpos 3570 ypos 1950

    if 4 <= randomBackground <= 7 and randomCover2 >= 1:
        "mission/WOOHP/cover/bg2/power2.png" xpos 1730 ypos 2270


    if 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 1:
        "mission/WOOHP/cover/bg2/loot1.png" xpos 1800 ypos 2160
    elif 4 <= randomBackground <= 7 and randomCover2 == 1 and randomLoot == 2:
        "mission/WOOHP/cover/bg2/loot2.png" xpos 1800 ypos 2160


    if 8 <= randomBackground <= 10 and randomCover1 >= 1:
        "mission/WOOHP/cover/bg3/pillar1.png"


    if 8 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 1:
        "mission/WOOHP/cover/bg3/loot1.png"
    elif 8 <= randomBackground <= 10 and randomCover1 == 1 and randomLoot == 2:
        "mission/WOOHP/cover/bg3/loot2.png"


    if 8 <= randomBackground <= 10 and randomCover2 >= 1:
        "mission/WOOHP/cover/bg3/pillar2.png"


    if 11 <= randomBackground <= 11 and randomCover1 >= 1:
        "mission/WOOHP/cover/bg4/chest1.png"





    if 11 <= randomBackground <= 11 and randomCover2 >= 1:
        "mission/WOOHP/cover/bg4/cover2.png" xpos 950 ypos 3350







default randomBackground = 1



default CoS1 = 0
default CoS2 = 0
default CoS3 = 0
default CoS4 = 0

default obst1Shield = 1
default obst2Shield = 1
default obst3Shield = 1
default obst4Shield = 1



image obstHulk = "mission/enemy/agentHulk.png"
image obstHulkBlock = "mission/enemy/agentHulkBlock.png"
image obstHulkHit = "mission/enemy/agentHulkHit.png"
image obstHulkAttack = "mission/enemy/agentHulkAttack.png"


image obstHulk2 = "mission/enemy/agentHulk2.png"
image obstHulkBlock2 = "mission/enemy/agentHulkBlock2.png"
image obstHulkHit2 = "mission/enemy/agentHulkHit2.png"
image obstHulkAttack2 = "mission/enemy/agentHulkAttack2.png"


default specialMaggieStatus = 0
default specialMaggieBounty = False
image obstMaggie = "mission/enemy/specialMaggie.png"


default specialMelodyStatus = 0
default specialMelodyBounty = False
image obstMelody = "mission/enemy/specialMelody.png"


default specialCandyStatus = 0
default specialCandyBounty = False
image obstCandy = "mission/enemy/specialCandy.png"


default specialDragonStatus = 0
default specialDragonBounty = False
image obstDragon = "mission/enemy/specialDragon.png"


default specialTaliaStatus = 0
default specialTaliaBounty = False
image obstTalia = "mission/enemy/specialTalia.png"


default specialKandStatus = 0
default specialKandBounty = False


default specialSebStatus = 0
default specialSebBounty = False


default specialMuffyStatus = 0
default specialMuffyBounty = False
image obstMuffy = "mission/enemy/specialMuffy.png"


default specialFelicityStatus = 0
default specialFelicityBounty = False
image obstFelicity = "mission/enemy/specialFelicity.png"


default specialBritneyBounty = False
image obstBritney = "mission/models/brit/britCombat1.png"


image obstTim1 = "mission/enemy/obstTim1.png"
image obstTim2 = "mission/enemy/obstTim2.png"
image obstTim3 = "mission/enemy/obstTim3.png"
image obstTim4 = "mission/enemy/obstTim4.png"


layeredimage obst1:



    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV <= 2:
        "mission/enemy/agentNeutral.png"
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV <= 2:
        "mission/enemy/agentNeutralArmor1.png"


    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 1:
        "mission/enemy/agentAlert1.png"
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 1:
        "mission/enemy/agentAlert1Armor.png"


    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus >= 2 and 1 <= randomBackground <= 3:
        "mission/enemy/agentAlert3.png"
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus >= 2 and 1 <= randomBackground <= 3:
        "mission/enemy/agentAlert3Armor.png"

    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert1.png"
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert1Armor.png"

    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus >= 2 and 8 <= randomBackground <= 11:
        "mission/enemy/agentAlert2.png" xzoom -1
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus >= 2 and 8 <= randomBackground <= 11:
        "mission/enemy/agentAlert2Armor.png" xzoom -1


    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 1 <= randomBackground <= 3:
        "mission/enemy/agentNeutral2.png"
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 1 <= randomBackground <= 3:
        "mission/enemy/agentNeutral2Armor1.png"

    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 4 <= randomBackground <= 7:
        "mission/enemy/agentNeutral.png"
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 4 <= randomBackground <= 7:
        "mission/enemy/agentNeutralArmor1.png"

    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 8 <= randomBackground <= 10:
        "mission/enemy/agentNeutral2.png" xzoom -1
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 8 <= randomBackground <= 10:
        "mission/enemy/agentNeutral2Armor1.png" xzoom -1

    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 11 <= randomBackground <= 11:
        "mission/enemy/agentNeutral2.png"
    if randomObst1 == 1 and randomAgent1 == 1 and hiddenStatus == 0 and obst1FoV == 3 and 11 <= randomBackground <= 11:
        "mission/enemy/agentNeutral2Armor1.png"



    if randomObst1 == 1 and randomAgent1 == 2 and obst1FoV == 1:
        "mission/enemy/agentShieldNeutral.png"

    if randomObst1 == 1 and randomAgent1 == 2 and obst1FoV == 1 and obst1Shield == 1:
        "mission/enemy/agentShieldNeutralSh.png"


    if randomObst1 == 1 and randomAgent1 == 2 and obst1FoV == 2:
        "mission/enemy/agentShieldNeutral.png"

    if randomObst1 == 1 and randomAgent1 == 2 and obst1FoV == 2:
        "mission/enemy/agentShieldNeutralSh.png"


    if randomObst1 == 1 and randomAgent1 == 2 and obst1FoV == 3:
        "mission/enemy/agentShieldBackSh.png"

    if randomObst1 == 1 and randomAgent1 == 2 and obst1FoV == 3:
        "mission/enemy/agentShieldBack.png"



    if randomObst1 == 1 and randomAgent1 == 3 and obst1FoV <= 2:
        "mission/enemy/agentSpecNeutral.png"


    if randomObst1 == 1 and randomAgent1 == 3 and obst1FoV == 3:
        "mission/enemy/agentSpecDistract.png"


    if randomObst1 == 2 and 1 <= randomBackground <= 3 and gadgetHackActive:
        "mission/enemy/lazer1.png"


    if randomObst1 == 2 and 11 <= randomBackground <= 11:
        "mission/enemy/fence.png"


    if randomObst1 == 3 and 1 <= randomBackground <= 3:
        "mission/enemy/agentRope1.png"


    if randomObst1 == 4 and 11 <= randomBackground <= 11:
        "mission/enemy/fence.png"


    if flashbangActive == 2 and randomObst1 == 1:
        "flashEffect" xpos 20 ypos -15

image flashEffect:
    "mission/gadgets/flashEffect1.png"
    pause 0.8
    "mission/gadgets/flashEffect2.png"
    pause 0.8
    repeat

image loveEffect:
    "mission/gadgets/loveEffect1.png"
    pause 0.8
    "mission/gadgets/loveEffect2.png"
    pause 0.8
    repeat


layeredimage obst2:


    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus == 0 and obst2FoV <= 2:
        "mission/enemy/agentNeutral.png"
    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus == 0 and obst2FoV <= 2:
        "mission/enemy/agentNeutralArmor1.png"

    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus == 1 and obst2FoV <= 2:
        "mission/enemy/agentAlert1.png"
    if randomObst2 == 1 and randomAgent2 == 1  and hiddenStatus == 1 and obst2FoV <= 2:
        "mission/enemy/agentAlert1Armor.png"


    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus >= 2 and 1 <= randomBackground <= 3:
        "mission/enemy/agentAlert3.png"
    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus >= 2 and 1 <=  randomBackground <= 3:
        "mission/enemy/agentAlert3Armor.png"

    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert4.png"
    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert4Armor.png"

    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus >= 2 and 8 <= randomBackground <= 11:
        "mission/enemy/agentAlert3.png"
    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus >= 2 and 8 <=  randomBackground <= 11:
        "mission/enemy/agentAlert3Armor.png"


    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus == 0 and obst2FoV == 3:
        "mission/enemy/agentNeutral2.png"
    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus == 0 and obst2FoV == 3:
        "mission/enemy/agentNeutral2Armor1.png"

    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus == 1 and obst2FoV == 3:
        "mission/enemy/agentNeutral2.png"
    if randomObst2 == 1 and randomAgent2 == 1 and hiddenStatus == 1 and obst2FoV == 3:
        "mission/enemy/agentNeutral2Armor1.png"




    if randomObst2 == 1 and randomAgent2 == 2 and obst2FoV == 1:
        "mission/enemy/agentShieldNeutral.png"

    if randomObst2 == 1 and randomAgent2 == 2 and obst2FoV == 1 and obst2Shield == 1:
        "mission/enemy/agentShieldNeutralSh.png"


    if randomObst2 == 1 and randomAgent2 == 2 and obst2FoV == 2:
        "mission/enemy/agentShieldNeutral.png"

    if randomObst2 == 1 and randomAgent2 == 2 and obst2FoV == 2:
        "mission/enemy/agentShieldNeutralSh.png"


    if randomObst2 == 1 and randomAgent2 == 2 and obst2FoV == 3:
        "mission/enemy/agentShieldBackSh.png"

    if randomObst2 == 1 and randomAgent2 == 2 and obst2FoV == 3:
        "mission/enemy/agentShieldBack.png"


    if flashbangActive == 2 and randomObst2 == 1:
        "flashEffect" xpos 20 ypos -15

layeredimage obst3:


    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV <= 2:
        "mission/enemy/agentNeutral.png"
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV <= 2:
        "mission/enemy/agentNeutralArmor1.png"


    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 1:
        "mission/enemy/agentAlert1.png"
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 1:
        "mission/enemy/agentAlert1Armor.png"


    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert4.png"
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert4Armor.png"

    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus >= 2 and 8 <= randomBackground <= 10:
        "mission/enemy/agentAlert2.png" xzoom -1
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus >= 2 and 8 <= randomBackground <= 10:
        "mission/enemy/agentAlert2Armor.png" xzoom -1

    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus >= 2 and 11 <= randomBackground <= 11:
        "mission/enemy/agentAlert2.png" xzoom -1
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus >= 2 and 11 <= randomBackground <= 11:
        "mission/enemy/agentAlert2Armor.png" xzoom -1


    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV == 3 and 4 <= randomBackground <= 7:
        "mission/enemy/agentNeutral.png"
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV == 3 and 4 <= randomBackground <= 7:
        "mission/enemy/agentNeutralArmor1.png"

    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV == 3 and 8 <= randomBackground <= 10:
        "mission/enemy/agentNeutral2.png" xzoom -1
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV == 3 and 8 <= randomBackground <= 10:
        "mission/enemy/agentNeutral2Armor1.png" xzoom -1

    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV == 3 and 11 <= randomBackground <= 11:
        "mission/enemy/agentNeutral2.png" xzoom -1
    if randomObst3 == 1 and randomAgent3 == 1 and hiddenStatus == 0 and obst3FoV == 3 and 11 <= randomBackground <= 11:
        "mission/enemy/agentNeutral2Armor1.png" xzoom -1



    if randomObst3 == 1 and randomAgent3 == 2 and obst3FoV == 1:
        "mission/enemy/agentShieldNeutral.png"

    if randomObst3 == 1 and randomAgent3 == 2 and obst3FoV == 1 and obst3Shield == 1:
        "mission/enemy/agentShieldNeutralSh.png"


    if randomObst3 == 1 and randomAgent3 == 2 and obst3FoV == 2:
        "mission/enemy/agentShieldNeutral.png" xzoom -1

    if randomObst3 == 1 and randomAgent3 == 2 and obst3FoV == 2:
        "mission/enemy/agentShieldNeutralSh.png" xzoom -1


    if randomObst3 == 1 and randomAgent3 == 2 and obst3FoV == 3:
        "mission/enemy/agentShieldBackSh.png" xzoom -1

    if randomObst3 == 1 and randomAgent3 == 2 and obst3FoV == 3:
        "mission/enemy/agentShieldBack.png" xzoom -1


    if flashbangActive == 2 and randomObst3 == 1:
        "flashEffect" xpos 20 ypos -15

layeredimage obst4:


    if randomObst4 == 1 and randomAgent4 == 1 and hiddenStatus == 0:
        "mission/enemy/agentNeutral.png"
    if randomObst4 == 1 and randomAgent4 == 1 and hiddenStatus == 0:
        "mission/enemy/agentNeutralArmor1.png"

    if randomObst4 == 1 and randomAgent4 == 1 and hiddenStatus == 1:
        "mission/enemy/agentAlert1.png"
    if randomObst4 == 1 and randomAgent4 == 1 and hiddenStatus == 1:
        "mission/enemy/agentAlert1Armor.png"


    if randomObst4 == 1 and randomAgent4 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert4.png"
    if randomObst4 == 1 and randomAgent4 == 1 and hiddenStatus >= 2 and 4 <= randomBackground <= 7:
        "mission/enemy/agentAlert4Armor.png"



    if randomObst4 == 1 and randomAgent4 == 2 and obst4FoV == 1:
        "mission/enemy/agentShieldNeutral.png"

    if randomObst4 == 1 and randomAgent4 == 2 and obst4FoV == 1 and obst3Shield == 1:
        "mission/enemy/agentShieldNeutralSh.png"


    if randomObst4 == 1 and randomAgent4 == 2 and obst4FoV == 2:
        "mission/enemy/agentShieldNeutral.png"

    if randomObst4 == 1 and randomAgent4 == 2 and obst4FoV == 2:
        "mission/enemy/agentShieldNeutralSh.png"


    if randomObst4 == 1 and randomAgent4 == 2 and obst4FoV == 3:
        "mission/enemy/agentShieldBackSh.png"

    if randomObst4 == 1 and randomAgent4 == 2 and obst4FoV == 3:
        "mission/enemy/agentShieldBack.png"


    if flashbangActive == 2 and randomObst4 == 1:
        "flashEffect" xpos 20 ypos -15

layeredimage agentNeutral:
    always:
        "mission/enemy/agentNeutral.png"
    if tutorialActive == True:
        "mission/enemy/agentNeutralArmor1.png"

layeredimage agentGuard:

    if randomAgent1 == 1 and combatTarget == 1:
        "mission/enemy/agentGuard1.png"
    if randomAgent2 == 1 and combatTarget == 2:
        "mission/enemy/agentGuard1.png"
    if randomAgent3 == 1 and combatTarget == 3:
        "mission/enemy/agentGuard1.png"
    if randomAgent4 == 1 and combatTarget == 4:
        "mission/enemy/agentGuard1.png"

    if randomAgent1 == 2 and combatTarget == 1:
        "mission/enemy/agentGuard2.png"
    if randomAgent2 == 2 and combatTarget == 2:
        "mission/enemy/agentGuard2.png"
    if randomAgent3 == 2 and combatTarget == 3:
        "mission/enemy/agentGuard2.png"
    if randomAgent4 == 2 and combatTarget == 4:
        "mission/enemy/agentGuard2.png"

    if randomAgent1 == 3 and combatTarget == 1:
        "mission/enemy/agentGuard3.png"
    if randomAgent2 == 3 and combatTarget == 2:
        "mission/enemy/agentGuard3.png"
    if randomAgent3 == 3 and combatTarget == 3:
        "mission/enemy/agentGuard3.png"
    if randomAgent4 == 3 and combatTarget == 4:
        "mission/enemy/agentGuard3.png"


layeredimage agentAttack:

    if randomObst1 == 1 and randomAgent1 == 1 and combatTarget == 1:
        "mission/enemy/agentAttack.png"

    if randomObst1 == 1 and randomAgent1 == 2 and combatTarget == 1:
        "mission/enemy/agentShieldAttackSh.png"
    if randomObst1 == 1 and randomAgent1 == 2 and combatTarget == 1:
        "mission/enemy/agentShieldAttack.png"

    if randomObst2 == 1 and randomAgent2 == 1 and combatTarget == 2:
        "mission/enemy/agentAttack.png"

    if randomObst2 == 1 and randomAgent2 == 2 and combatTarget == 2:
        "mission/enemy/agentShieldAttackSh.png"
    if randomObst2 == 1 and randomAgent2 == 2 and combatTarget == 2:
        "mission/enemy/agentShieldAttack.png"

    if randomObst3 == 1 and randomAgent3 == 1 and combatTarget == 3:
        "mission/enemy/agentAttack.png"

    if randomObst3 == 1 and randomAgent3 == 2 and combatTarget == 3:
        "mission/enemy/agentShieldAttackSh.png"
    if randomObst3 == 1 and randomAgent3 == 2 and combatTarget == 3:
        "mission/enemy/agentShieldAttack.png"

    if randomObst4 == 1 and randomAgent4 == 1 and combatTarget == 4:
        "mission/enemy/agentAttack.png"

    if randomObst4 == 1 and randomAgent4 == 2 and combatTarget == 4:
        "mission/enemy/agentShieldAttackSh.png"
    if randomObst4 == 1 and randomAgent4 == 2 and combatTarget == 4:
        "mission/enemy/agentShieldAttack.png"

    if randomAgent1 == 3 and combatTarget == 1:
        "mission/enemy/agentSpecAttack.png"
    if randomAgent2 == 3 and combatTarget == 2:
        "mission/enemy/agentSpecAttack.png"
    if randomAgent3 == 3 and combatTarget == 3:
        "mission/enemy/agentSpecAttack.png"
    if randomAgent4 == 3 and combatTarget == 4:
        "mission/enemy/agentSpecAttack.png"


layeredimage agentShieldAttack:
    if obst1Shield == 1:
        "mission/enemy/agentShieldAttackSh.png"
    always:
        "mission/enemy/agentShieldAttack.png"

layeredimage shieldUnderFire:
    always:
        "mission/enemy/shieldv1.png"
        xalign 0.0 yalign 0.3 zoom 0.8      

layeredimage agentAlert:

    if 1 <= randomBackground <= 6:
        "mission/enemy/agentAlert1.png"
    if 1 <= randomBackground <= 6:
        "mission/enemy/agentAlert1Armor.png"

layeredimage agentFire:

    if 1 <= randomBackground <= 3:
        "mission/enemy/agentShoot1.png"
    if 1 <= randomBackground <= 3:
        "mission/enemy/agentShoot1Armor.png"

layeredimage agentHit:

    if randomAgent1 == 1 and combatTarget == 1:
        "mission/enemy/agentHit1.png"
    if randomAgent2 == 1 and combatTarget == 2:
        "mission/enemy/agentHit1.png"
    if randomAgent3 == 1 and combatTarget == 3:
        "mission/enemy/agentHit1.png"
    if randomAgent4 == 1 and combatTarget == 4:
        "mission/enemy/agentHit1.png"
    if randomAgent1 == 2 and combatTarget == 1:
        "mission/enemy/agentHit2.png"
    if randomAgent2 == 2 and combatTarget == 2:
        "mission/enemy/agentHit2.png"
    if randomAgent3 == 2 and combatTarget == 3:
        "mission/enemy/agentHit2.png"
    if randomAgent4 == 2 and combatTarget == 4:
        "mission/enemy/agentHit2.png"
    if randomAgent1 == 3 and combatTarget == 1:
        "mission/enemy/agentHit3.png"
    if randomAgent2 == 3 and combatTarget == 2:
        "mission/enemy/agentHit3.png"
    if randomAgent3 == 3 and combatTarget == 3:
        "mission/enemy/agentHit3.png"
    if randomAgent4 == 3 and combatTarget == 4:
        "mission/enemy/agentHit3.png"

layeredimage agentHitObject:

    if randomAgent2 == 1 and 1 <= randomBackground <= 3:
        "mission/enemy/agentHit1.png"
    if randomAgent2 == 2 and 1 <= randomBackground <= 3:
        "mission/enemy/agentHit2.png"

    if randomAgent3 == 1 and 8 <= randomBackground <= 10:
        "mission/enemy/agentHit1.png"
    if randomAgent3 == 2 and 8 <= randomBackground <= 10:
        "mission/enemy/agentHit2.png"


layeredimage spyCorner:
    always:
        "mission/models/spyHidingBase1.png"
    if activeSpy == 1:
        "mission/models/sam/spyHidingSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyHidingHair1.png"
    if activeSpy == 1:
        "mission/models/sam/spyHidingFace1.png"
    if activeSpy == 2:
        "mission/models/clover/spyHidingSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyHidingHair1.png"
    if activeSpy == 2:
        "mission/models/clover/spyHidingFace1.png"
    if activeSpy == 3:
        "mission/models/alex/spyHidingSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyHidingHair1.png"
    if activeSpy == 3:
        "mission/models/alex/spyHidingFace1.png"

layeredimage spyCornerSide:
    always:
        "mission/models/spyCornerSide.png"
    if activeSpy == 1:
        "mission/models/sam/spyCornerSideSuit.png"
    if activeSpy == 1:
        "mission/models/sam/spyCornerSideHair.png"
    if activeSpy == 1:
        "mission/models/sam/spyCornerSideFace.png"
    if activeSpy == 2:
        "mission/models/clover/spyCornerSideSuit.png"
    if activeSpy == 2:
        "mission/models/clover/spyCornerSideHair.png"
    if activeSpy == 2:
        "mission/models/clover/spyCornerSideFace.png"
    if activeSpy == 3:
        "mission/models/alex/spyCornerSideSuit.png"
    if activeSpy == 3:
        "mission/models/alex/spyCornerSideHair.png"
    if activeSpy == 3:
        "mission/models/alex/spyCornerSideFace.png"

layeredimage spyCrouchCorner:
    always:
        "mission/models/spyHidingCrouch1.png"
    if activeSpy == 1:
        "mission/models/sam/spyCrouchingSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyCrouchingHair1.png"
    if activeSpy == 1:
        "mission/models/sam/spyCrouchingFace1.png"
    if activeSpy == 2:
        "mission/models/clover/spyCrouchingSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyCrouchingHair1.png"
    if activeSpy == 2:
        "mission/models/clover/spyCrouchingFace1.png"
    if activeSpy == 3:
        "mission/models/alex/spyCrouchingSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyCrouchingHair1.png"
    if activeSpy == 3:
        "mission/models/alex/spyCrouchingFace1.png"

layeredimage spyCombat1:
    always:
        "mission/models/spyCombat1.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatHair1.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatFace1.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatHair1.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatFace1.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatHair1.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatFace1.png"
layeredimage spyCombat2:
    always:
        "mission/models/spyCombat2.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatSuit2.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatHair2.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatFace2.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatSuit2.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatHair2.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatFace2.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatSuit2.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatHair2.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatFace2.png"
layeredimage spyCombat3:
    always:
        "mission/models/spyCombat3.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatSuit3.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatHair3.png"
    if activeSpy == 1:
        "mission/models/sam/spyCombatFace3.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatSuit3.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatHair3.png"
    if activeSpy == 2:
        "mission/models/clover/spyCombatFace3.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatSuit3.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatHair3.png"
    if activeSpy == 3:
        "mission/models/alex/spyCombatFace3.png"


image bossSeb = "mission/models/clover/bossSeb.png"
image bossSeb2 = "mission/models/clover/bossSeb2.png"
image bossSeb3 = "mission/models/clover/spyGuard.png"
image bossSeb4 = "mission/models/clover/spyHit.png"


image fightAlex = "mission/models/alex/fightAlex.png"


layeredimage spyHit:
    if activeSpy == 1:
        "mission/models/sam/spyHit.png"
    if activeSpy == 2:
        "mission/models/clover/spyHit.png"
    if activeSpy == 3:
        "mission/models/alex/spyHit.png"


layeredimage spyGuard:
    if activeSpy == 1:
        "mission/models/sam/spyGuard.png"
    if activeSpy == 2:
        "mission/models/clover/spyGuard.png"
    if activeSpy == 3:
        "mission/models/alex/spyGuard.png"

layeredimage spyGuard2:
    if activeSpy == 1:
        "mission/models/sam/spyGuard2.png"
    if activeSpy == 2:
        "mission/models/clover/spyGuard2.png"
    if activeSpy == 3:
        "mission/models/alex/spyGuard2.png"


layeredimage spyGuardTut:
    if activeSpy == 1:
        "mission/models/clover/spyGuard.png"
    if activeSpy == 2:
        "mission/models/alex/spyGuard.png"
    if activeSpy == 3:
        "mission/models/sam/spyGuard.png"

image agentGuardTut = "mission/enemy/agentGuard1.png"


layeredimage spyBackup1:
    if backupUsed <= 4:
        "mission/models/spyCombat1.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatSuit1.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatHair1.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatFace1.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatSuit1.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatHair1.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatFace1.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatSuit1.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatHair1.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatFace1.png"
    if backupUsed == 4:
        "mission/models/kim/kimCombat.png"
    if backupUsed == 5:
        "mission/models/brit/britCombat3.png"
layeredimage spyBackup2:
    if backupUsed <= 4:
        "mission/models/spyCombat2.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatSuit2.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatHair2.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatFace2.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatSuit2.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatHair2.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatFace2.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatSuit2.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatHair2.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatFace2.png"
    if backupUsed == 4:
        "mission/models/kim/kimCombat2.png"
    if backupUsed == 5:
        "mission/models/brit/britCombat5.png"
layeredimage spyBackup3:
    if backupUsed <= 4:
        "mission/models/spyCombat3.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatSuit3.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatHair3.png"
    if backupUsed == 1:
        "mission/models/sam/spyCombatFace3.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatSuit3.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatHair3.png"
    if backupUsed == 2:
        "mission/models/clover/spyCombatFace3.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatSuit3.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatHair3.png"
    if backupUsed == 3:
        "mission/models/alex/spyCombatFace3.png"
    if backupUsed == 4:
        "mission/models/kim/kimCombat3.png"
    if backupUsed == 5:
        "mission/models/brit/britCombat6.png"
layeredimage spyBackup4:
    if backupUsed <= 4:
        "mission/models/spyFallBase1.png"
    if backupUsed == 1:
        "mission/models/sam/spyFallingSuit1.png"
    if backupUsed == 1:
        "mission/models/sam/spyFallingHair1.png"
    if backupUsed == 1:
        "mission/models/sam/spyFallingFace1.png"
    if backupUsed == 2:
        "mission/models/clover/spyFallingSuit1.png"
    if backupUsed == 2:
        "mission/models/clover/spyFallingHair1.png"
    if backupUsed == 2:
        "mission/models/clover/spyFallingFace1.png"
    if backupUsed == 3:
        "mission/models/alex/spyFallingSuit1.png"
    if backupUsed == 3:
        "mission/models/alex/spyFallingHair1.png"
    if backupUsed == 3:
        "mission/models/alex/spyFallingFace1.png"
    if backupUsed == 4:
        "mission/models/kim/kimFalling.png"
    if backupUsed == 5:
        "mission/models/brit/britFalling.png"

layeredimage spyFalling:
    always:
        "mission/models/spyFallBase1.png"
    if activeSpy == 1:
        "mission/models/sam/spyFallingSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyFallingHair1.png"
    if activeSpy == 1:
        "mission/models/sam/spyFallingFace1.png"
    if activeSpy == 2:
        "mission/models/clover/spyFallingSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyFallingHair1.png"
    if activeSpy == 2:
        "mission/models/clover/spyFallingFace1.png"
    if activeSpy == 3:
        "mission/models/alex/spyFallingSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyFallingHair1.png"
    if activeSpy == 3:
        "mission/models/alex/spyFallingFace1.png"

layeredimage spyCrouchingSide:
    always:
        "mission/models/spyHidingCrouch2.png"
    if activeSpy == 1:
        "mission/models/sam/spyCrouchingSuit2.png"
    if activeSpy == 1:
        "mission/models/sam/spyCrouchingHair2.png"
    if activeSpy == 1:
        "mission/models/sam/spyCrouchingFace2.png"
    if activeSpy == 2:
        "mission/models/clover/spyCrouchingSuit2.png"
    if activeSpy == 2:
        "mission/models/clover/spyCrouchingHair2.png"
    if activeSpy == 2:
        "mission/models/clover/spyCrouchingFace2.png"
    if activeSpy == 3:
        "mission/models/alex/spyCrouchingSuit2.png"
    if activeSpy == 3:
        "mission/models/alex/spyCrouchingHair2.png"
    if activeSpy == 3:
        "mission/models/alex/spyCrouchingFace2.png"

layeredimage spyFlirt1:
    always:
        "mission/models/spyFlirt1.png"
    if activeSpy == 1:
        "mission/models/sam/spyFlirt1.png"
    if activeSpy == 2:
        "mission/models/clover/spyFlirt1.png"
    if activeSpy == 3:
        "mission/models/alex/spyFlirt1.png"

layeredimage spyFlirt2:
    always:
        "mission/models/spyFlirt2.png"
    if activeSpy == 1:
        "mission/models/sam/spyFlirt2.png"
    if activeSpy == 2:
        "mission/models/clover/spyFlirt2.png"
    if activeSpy == 3:
        "mission/models/alex/spyFlirt2.png"

layeredimage spyFlirt3:
    always:
        "mission/models/spyFlirt3.png"
    if activeSpy == 1:
        "mission/models/sam/spyFlirt3.png"
    if activeSpy == 2:
        "mission/models/clover/spyFlirt3.png"
    if activeSpy == 3:
        "mission/models/alex/spyFlirt3.png"

layeredimage spyShootSideNormal:
    always:
        "mission/models/spyShootSide1.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootingSideSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootingSideFace1.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootingSideSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootingSideFace1.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootingSideSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootingSideFace1.png"

layeredimage spyShootSideUp:
    always:
        "mission/models/spyShootUp2.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootUpSuit2.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootUpHair2.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootUpFace2.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootUpSuit2.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootUpHair2.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootUpFace2.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootUpSuit2.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootUpHair2.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootUpFace2.png"

    if gunStatus == 1:
        "mission/models/shootUpGunSide.png" xpos 290 ypos -55
    if gunStatus == 2:
        "mission/models/shootUpHookSide.png" xpos 290 ypos -55

layeredimage spyShootBackNormal:
    always:
        "mission/models/spyShoot1.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootingSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootUpHair1.png"
        xalign -0.01
    if activeSpy == 2:
        "mission/models/clover/spyShootingSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootUpHair1.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootingSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootUpHair1.png"

    if gunStatus == 1:
        "mission/models/shootGun.png"
    if gunStatus == 2:
        "mission/models/shootHook.png"

layeredimage spyShootBackUp:
    always:
        "mission/models/spyShootUp1.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootUpSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootUpHair1.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootUpSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootUpHair1.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootUpSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootUpHair1.png"

    if gunStatus == 1:
        "mission/models/shootUpGun.png"
    if gunStatus == 2:
        "mission/models/shootUpHook.png"

layeredimage spyThrowBack1:
    if activeSpy == 1:
        "mission/models/sam/spyThrow1.png"
    if activeSpy == 2:
        "mission/models/clover/spyThrow1.png"
    if activeSpy == 3:
        "mission/models/alex/spyThrow1.png"

layeredimage spyThrowBack2:
    if activeSpy == 1:
        "mission/models/sam/spyThrow2.png"
    if activeSpy == 2:
        "mission/models/clover/spyThrow2.png"
    if activeSpy == 3:
        "mission/models/alex/spyThrow2.png"

layeredimage spyThrowSide1:
    always:
        "mission/models/spyThrowSide1.png"
    if activeSpy == 1:
        "mission/models/sam/spyThrowSideFace.png"
    if activeSpy == 1:
        "mission/models/sam/spyThrowSideSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyThrowSideSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyThrowSideFace.png"
    if activeSpy == 3:
        "mission/models/alex/spyThrowSideSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyThrowSideFace.png"
layeredimage spyThrowSide2:
    always:
        "mission/models/spyThrowSide2.png"
    if activeSpy == 1:
        "mission/models/sam/spyThrowSideFace.png"
    if activeSpy == 1:
        "mission/models/sam/spyThrowSideSuit2.png"
    if activeSpy == 2:
        "mission/models/clover/spyThrowSideSuit2.png"
    if activeSpy == 2:
        "mission/models/clover/spyThrowSideFace.png"
    if activeSpy == 3:
        "mission/models/alex/spyThrowSideSuit2.png"
    if activeSpy == 3:
        "mission/models/alex/spyThrowSideFace.png"


screen spyHacking:
    if missionSetting == "School":
        if activeSpy == 1:
            add "mission/models/sam/hacking1.jpg"
        if activeSpy == 2:
            add "mission/models/clover/hacking1.jpg"
        if activeSpy == 3:
            add "mission/models/alex/hacking1.jpg"
    if missionSetting == "Castle":
        if activeSpy == 1:
            add "mission/models/sam/hacking2.jpg"
        if activeSpy == 2:
            add "mission/models/clover/hacking2.jpg"
        if activeSpy == 3:
            add "mission/models/alex/hacking2.jpg"
    if missionSetting == "Database":
        if activeSpy == 1:
            add "mission/models/sam/hacking3.jpg"
        if activeSpy == 2:
            add "mission/models/clover/hacking3.jpg"
        if activeSpy == 3:
            add "mission/models/alex/hacking3.jpg"
    if missionSetting == "Faire":
        if activeSpy == 1:
            add "mission/models/sam/hacking4.jpg"
        if activeSpy == 2:
            add "mission/models/clover/hacking4.jpg"
        if activeSpy == 3:
            add "mission/models/alex/hacking4.jpg"
    if missionSetting == "WOOHP":
        if activeSpy == 1:
            add "mission/models/sam/hacking5.jpg"
        if activeSpy == 2:
            add "mission/models/clover/hacking5.jpg"
        if activeSpy == 3:
            add "mission/models/alex/hacking5.jpg"

    bar at rotHack:
        value hackResult
        range 100
        left_bar "mission/interact/bar.png"
        right_bar "mission/interact/barEmpty.png"
        thumb_offset 0
        xysize (260,100)
        xpos 180
        ypos 145


    vbox xalign 0.38 yalign 0.25:
        imagebutton:
            idle "mission/interact/hackSkillButton.png"
            hover "mission/interact/hackSkillButton-hover.png"
            if hackSkillUsed == False:
                if skillHack == 0:
                    action SetVariable("hackResult", hackResult + 10), SetVariable("hackSkillUsed", True)
                elif skillHack == 1:
                    action SetVariable("hackResult", hackResult + 15), SetVariable("hackSkillUsed", True)
                elif skillHack == 2:
                    action SetVariable("hackResult", hackResult + 20), SetVariable("hackSkillUsed", True)
                elif skillHack == 3:
                    action SetVariable("hackResult", hackResult + 25), SetVariable("hackSkillUsed", True)
                else:
                    action SetVariable("hackResult", hackResult + 25), SetVariable("hackSkillUsed", True)

transform rotHack:
    rotate -18

image spyReadyGreen = "mission/models/sam/readyFull.png"
image spyReadyRed = "mission/models/clover/readyFull.png"
image spyReadyYellow = "mission/models/alex/readyFull.png"

image spyFlirt1Green = "mission/models/sam/spyFlirt1.png"
image spyFlirt1Red = "mission/models/clover/spyFlirt1.png"
image spyFlirt1Yellow = "mission/models/alex/spyFlirt1.png"

layeredimage spyMasturbate:
    if activeSpy == 1 and vibUpgrade == False and breakControlChance <= 1:
        "mission/models/sam/masturbate1.png"
    if activeSpy == 2 and vibUpgrade == False and breakControlChance <= 1:
        "mission/models/clover/masturbate1.png"
    if activeSpy == 3 and vibUpgrade == False and breakControlChance <= 1:
        "mission/models/alex/masturbate1.png"

    if activeSpy == 1 and vibUpgrade == False and breakControlChance >= 2:
        "mission/models/sam/masturbate2.png"
    if activeSpy == 2 and vibUpgrade == False and breakControlChance >= 2:
        "mission/models/clover/masturbate2.png"
    if activeSpy == 3 and vibUpgrade == False and breakControlChance >= 2:
        "mission/models/alex/masturbate2.png"

    if activeSpy == 1 and vibUpgrade == True:
        "mission/models/sam/masturbate3.png"
    if activeSpy == 2 and vibUpgrade == True:
        "mission/models/clover/masturbate3.png"
    if activeSpy == 3 and vibUpgrade == True:
        "mission/models/alex/masturbate3.png"





image light1Anim = "mission/school/interactable/light1Anim.png"







layeredimage jumpGraphic:

    if 1 <= randomBackground <= 3 and currentPosition == 0 and activeSpy == 1:
        "mission/jumps/green/bg1Jump1.png"
    if 1 <= randomBackground <= 3 and currentPosition == 1 and activeSpy == 1:
        "mission/jumps/green/bg1Jump2.png"
    if 4 <= randomBackground <= 7 and currentPosition == 0 and activeSpy == 1:
        "mission/jumps/green/bg2Jump1.png"
    if 4 <= randomBackground <= 7 and currentPosition == 1 and activeSpy == 1:
        "mission/jumps/green/bg2Jump2.png"
    if 4 <= randomBackground <= 7 and currentPosition == 2 and activeSpy == 1:
        "mission/jumps/green/bg2Jump3.png"
    if 4 <= randomBackground <= 7 and currentPosition == 3 and activeSpy == 1:
        "mission/jumps/green/bg2Jump4.png"
    if 8 <= randomBackground <= 10 and currentPosition == 0 and activeSpy == 1:
        "mission/jumps/green/bg3Jump1.png"
    if 8 <= randomBackground <= 10 and currentPosition == 1 and activeSpy == 1:
        "mission/jumps/green/bg3Jump2.png"
    if 11 <= randomBackground <= 11 and currentPosition == 0 and activeSpy == 1:
        "mission/jumps/green/bg4Jump1.png"
    if 11 <= randomBackground <= 11 and currentPosition == 1 and activeSpy == 1:
        "mission/jumps/green/bg4Jump2.png"
    if 11 <= randomBackground <= 11 and currentPosition == 2 and activeSpy == 1:
        "mission/jumps/green/bg4Jump3.png"
    if 11 <= randomBackground <= 11 and currentPosition == 3 and activeSpy == 1:
        "mission/jumps/green/bg4Jump4.png"
    if 11 <= randomBackground <= 11 and currentPosition == 4 and activeSpy == 1:
        "mission/jumps/green/bg4Jump5.png"


    if 1 <= randomBackground <= 3 and currentPosition == 0 and activeSpy == 2:
        "mission/jumps/red/bg1Jump1.png"
    if 1 <= randomBackground <= 3 and currentPosition == 1 and activeSpy == 2:
        "mission/jumps/red/bg1Jump2.png"
    if 4 <= randomBackground <= 7 and currentPosition == 0 and activeSpy == 2:
        "mission/jumps/red/bg2Jump1.png"
    if 4 <= randomBackground <= 7 and currentPosition == 1 and activeSpy == 2:
        "mission/jumps/red/bg2Jump2.png"
    if 4 <= randomBackground <= 7 and currentPosition == 2 and activeSpy == 2:
        "mission/jumps/red/bg2Jump3.png"
    if 4 <= randomBackground <= 7 and currentPosition == 3 and activeSpy == 2:
        "mission/jumps/red/bg2Jump4.png"
    if 8 <= randomBackground <= 10 and currentPosition == 0 and activeSpy == 2:
        "mission/jumps/red/bg3Jump1.png"
    if 8 <= randomBackground <= 10 and currentPosition == 1 and activeSpy == 2:
        "mission/jumps/red/bg3Jump2.png"
    if 11 <= randomBackground <= 11 and currentPosition == 0 and activeSpy == 2:
        "mission/jumps/red/bg4Jump1.png"
    if 11 <= randomBackground <= 11 and currentPosition == 1 and activeSpy == 2:
        "mission/jumps/red/bg4Jump2.png"
    if 11 <= randomBackground <= 11 and currentPosition == 2 and activeSpy == 2:
        "mission/jumps/red/bg4Jump3.png"
    if 11 <= randomBackground <= 11 and currentPosition == 3 and activeSpy == 2:
        "mission/jumps/red/bg4Jump4.png"
    if 11 <= randomBackground <= 11 and currentPosition == 4 and activeSpy == 2:
        "mission/jumps/red/bg4Jump5.png"


    if 1 <= randomBackground <= 3 and currentPosition == 0 and activeSpy == 3:
        "mission/jumps/yellow/bg1Jump1.png"
    if 1 <= randomBackground <= 3 and currentPosition == 1 and activeSpy == 3:
        "mission/jumps/yellow/bg1Jump2.png"
    if 4 <= randomBackground <= 7 and currentPosition == 0 and activeSpy == 3:
        "mission/jumps/yellow/bg2Jump1.png"
    if 4 <= randomBackground <= 7 and currentPosition == 1 and activeSpy == 3:
        "mission/jumps/yellow/bg2Jump2.png"
    if 4 <= randomBackground <= 7 and currentPosition == 2 and activeSpy == 3:
        "mission/jumps/yellow/bg2Jump3.png"
    if 4 <= randomBackground <= 7 and currentPosition == 3 and activeSpy == 3:
        "mission/jumps/yellow/bg2Jump4.png"
    if 8 <= randomBackground <= 10 and currentPosition == 0 and activeSpy == 3:
        "mission/jumps/yellow/bg3Jump1.png"
    if 8 <= randomBackground <= 10 and currentPosition == 1 and activeSpy == 3:
        "mission/jumps/yellow/bg3Jump2.png"
    if 11 <= randomBackground <= 11 and currentPosition == 0 and activeSpy == 3:
        "mission/jumps/yellow/bg4Jump1.png"
    if 11 <= randomBackground <= 11 and currentPosition == 1 and activeSpy == 3:
        "mission/jumps/yellow/bg4Jump2.png"
    if 11 <= randomBackground <= 11 and currentPosition == 2 and activeSpy == 3:
        "mission/jumps/yellow/bg4Jump3.png"
    if 11 <= randomBackground <= 11 and currentPosition == 3 and activeSpy == 3:
        "mission/jumps/yellow/bg4Jump4.png"
    if 11 <= randomBackground <= 11 and currentPosition == 4 and activeSpy == 3:
        "mission/jumps/yellow/bg4Jump5.png"

layeredimage jumpBackup:

    if activeSpy == 1 and currentPosition == 0 and 1 <= randomBackground <= 3:
        "mission/jumps/green/bkup/bg1Backup.png"
    if activeSpy == 2 and currentPosition == 0 and 1 <= randomBackground <= 3:
        "mission/jumps/red/bkup/bg1Backup.png"
    if activeSpy == 3 and currentPosition == 0 and 1 <= randomBackground <= 3:
        "mission/jumps/yellow/bkup/bg1Backup.png"

    if activeSpy == 1 and currentPosition == 1 and 1 <= randomBackground <= 3:
        "mission/jumps/green/bkup/bg1Backup2.png"
    if activeSpy == 2 and currentPosition == 1 and 1 <= randomBackground <= 3:
        "mission/jumps/red/bkup/bg1Backup2.png"
    if activeSpy == 3 and currentPosition == 1 and 1 <= randomBackground <= 3:
        "mission/jumps/yellow/bkup/bg1Backup2.png"


    if activeSpy == 1 and currentPosition == 0 and 4 <= randomBackground <= 7:
        "mission/jumps/green/bkup/bg2Backup0.png"
    if activeSpy == 2 and currentPosition == 0 and 4 <= randomBackground <= 7:
        "mission/jumps/red/bkup/bg2Backup0.png"
    if activeSpy == 3 and currentPosition == 0 and 4 <= randomBackground <= 7:
        "mission/jumps/yellow/bkup/bg2Backup0.png"

    if activeSpy == 1 and currentPosition == 1 and 4 <= randomBackground <= 7:
        "mission/jumps/green/bkup/bg2Backup1.png"
    if activeSpy == 2 and currentPosition == 1 and 4 <= randomBackground <= 7:
        "mission/jumps/red/bkup/bg2Backup1.png"
    if activeSpy == 3 and currentPosition == 1 and 4 <= randomBackground <= 7:
        "mission/jumps/yellow/bkup/bg2Backup1.png"

    if activeSpy == 1 and currentPosition == 3 and 4 <= randomBackground <= 7:
        "mission/jumps/green/bkup/bg2Backup3.png"
    if activeSpy == 2 and currentPosition == 3 and 4 <= randomBackground <= 7:
        "mission/jumps/red/bkup/bg2Backup3.png"
    if activeSpy == 3 and currentPosition == 3 and 4 <= randomBackground <= 7:
        "mission/jumps/yellow/bkup/bg2Backup3.png"

    if activeSpy == 1 and currentPosition == 4 and 4 <= randomBackground <= 7:
        "mission/jumps/green/bkup/bg2Backup4.png"
    if activeSpy == 2 and currentPosition == 4 and 4 <= randomBackground <= 7:
        "mission/jumps/red/bkup/bg2Backup4.png"
    if activeSpy == 3 and currentPosition == 4 and 4 <= randomBackground <= 7:
        "mission/jumps/yellow/bkup/bg2Backup4.png"


    if activeSpy == 1 and currentPosition == 0 and 8 <= randomBackground <= 10:
        "mission/jumps/green/bkup/bg1Backup.png"
    if activeSpy == 2 and currentPosition == 0 and 8 <= randomBackground <= 10:
        "mission/jumps/red/bkup/bg1Backup.png"
    if activeSpy == 3 and currentPosition == 0 and 8 <= randomBackground <= 10:
        "mission/jumps/yellow/bkup/bg1Backup.png"
    if activeSpy == 1 and currentPosition == 2 and 8 <= randomBackground <= 10:
        "mission/jumps/green/bkup/bg3Backup2.png"
    if activeSpy == 2 and currentPosition == 2 and 8 <= randomBackground <= 10:
        "mission/jumps/red/bkup/bg3Backup2.png"
    if activeSpy == 3 and currentPosition == 2 and 8 <= randomBackground <= 10:
        "mission/jumps/yellow/bkup/bg3Backup2.png"


    if activeSpy == 1 and currentPosition == 0 and 11 <= randomBackground <= 11:
        "mission/jumps/green/bkup/bg1Backup.png"
    if activeSpy == 2 and currentPosition == 0 and 11 <= randomBackground <= 11:
        "mission/jumps/red/bkup/bg1Backup.png"
    if activeSpy == 3 and currentPosition == 0 and 11 <= randomBackground <= 11:
        "mission/jumps/yellow/bkup/bg1Backup.png"
    if activeSpy == 1 and currentPosition == 2 and 11 <= randomBackground <= 11:
        "mission/jumps/green/bkup/bg1Backup.png"
    if activeSpy == 2 and currentPosition == 2 and 11 <= randomBackground <= 11:
        "mission/jumps/red/bkup/bg1Backup.png"
    if activeSpy == 3 and currentPosition == 2 and 11 <= randomBackground <= 11:
        "mission/jumps/yellow/bkup/bg1Backup.png"

layeredimage flirtJump:
    if activeSpy == 1 and currentPosition == 0 and 1 <= randomBackground <= 3:
        "mission/jumps/green/flirtJump1.png"

image zoomGraphic = "mission/cover/zoom.png"





label missionScreenFinish:

    if task23Stage == 4:
        $ specialBossActive = True
    $ specialBossActive = True
    if task26Stage == 23 and missionScreenCurrentLocation == 3:
        $ specialBossActive = True
        pass
    elif task26Stage == 23 and missionScreenCurrentLocation != 3:
        y "I should plan a mission to Punk Web first to rescue Clover."
        jump missions
    elif task26Stage == 25 and missionScreenCurrentLocation != 5:
        y "I should plan a mission to WOOHP first to rescue Alex."
        jump missions

    $ chanceOfControl = 0
    if missionScreenFrontlineSelect == 0:
        "No frontline spy selected."
        jump missions
    if intel < intelCost:
        "Not enough intel to plan mission"
        jump missions
    if missionScreenCurrentLocation == 0:
        "Please choose a location."
    if missionScreenCurrentLocation == 2 and missionAreaCastleActive == False:
        "Please choose a location."
        jump missions
    if missionScreenCurrentLocation == 3 and missionAreaDatabaseActive == False:
        "Please choose a location."
        jump missions
    if missionScreenCurrentLocation == 4 and missionAreaDatabaseActive == False:
        "Please choose a location."
        jump missions
    if missionScreenCurrentLocation == 5 and missionAreaWOOHPActive == False:
        "Please choose a location."
        jump missions

    if missionScreenFrontlineSelect == 1 or missionScreenSupportSelect == 1 or missionScreenDistractSelect == 1:
        $ samOnMission = True
    if missionScreenFrontlineSelect == 2 or missionScreenSupportSelect == 2 or missionScreenDistractSelect == 2:
        $ cloverOnMission = True
    if missionScreenFrontlineSelect == 3 or missionScreenSupportSelect == 3 or missionScreenDistractSelect == 3:
        $ alexOnMission = True

    if missionScreenSupportSelect == 1:
        $ backupSamActive = True
        $ backup1 = 6
    if missionScreenSupportSelect == 2:
        $ backupCloverActive = True
        $ backup2 = 6
    if missionScreenSupportSelect == 3:
        $ backupAlexActive = True
        $ backup3 = 6

    if missionScreenDistractSelect == 1:
        $ backupSamActive = True
        $ backup1 = 6
    if missionScreenDistractSelect == 2:
        $ backupCloverActive = True
        $ backup2 = 6
    if missionScreenDistractSelect == 3:
        $ backupAlexActive = True
        $ backup3 = 6

    if missionScreenFrontlineSelect == 1:
        $ backupSamActive = False
    if missionScreenFrontlineSelect == 2:
        $ backupCloverActive = False
    if missionScreenFrontlineSelect == 3:
        $ backupAlexActive = False

    if specialMaggieStatus == 1 or specialDragonStatus == 1 or specialMuffyStatus == 1:
        $ randomBossHP = 3
        $ specialBossActive = True
    if specialMelodyStatus == 1 and task6Stage == 12:
        $ randomBossHP = 3
        $ specialBossActive = True
    if specialCandyStatus == 1 and task16Stage == 3:
        $ randomBossHP = 3
        $ specialBossActive = True
    if specialTaliaStatus == 1 and task18Stage == 2:
        $ randomBossHP = 3
        $ specialBossActive = True
    if specialFelicityStatus and task21Stage == 6:
        $ randomBossHP = 3
        $ specialBossActive = True
    if task26Stage == 9:
        $ randomBossHP = 3
        $ specialBossActive = True
    hide screen missionScreenButtons
    $ controlCountDown = 4
    scene black
    with d3
    $ missionProgression = 0
    if missionScreenCurrentLocation == 1:
        $ intel -= 100
        $ missionSetting = "School"
        show text "Launching mission.\nLocation: Malibu University."
        with d5
        pause 1.5
        hide text
        with d5
        $ randMusic = renpy.random.randint(1, 2)
        if randMusic == 1:
            play music "audio/music/stealth1.mp3"
        if randMusic == 2:
            play music "audio/music/stealth2.mp3"
    if missionScreenCurrentLocation == 2:
        $ intel -= 200
        $ missionSetting = "Castle"
        show text "Launching mission.\nLocation: Valencia, Spain."
        with d5
        pause 1.5
        hide text
        with d5
        pause 1.5
        hide text
        with d5
        $ randMusic = renpy.random.randint(1, 2)
        if randMusic == 1:
            play music "audio/music/stealth1.mp3"
        if randMusic == 2:
            play music "audio/music/stealth2.mp3"



    if missionScreenCurrentLocation == 3:
        $ intel -= 300
        $ missionSetting = "Database"
        show text "Launching mission.\nLocation: Punk Web."
        with d5
        pause 1.5
        hide text
        with d5
        pause 1.5
        hide text
        with d5
        play music "audio/music/techdungeon.mp3"
    if missionScreenCurrentLocation == 4:
        $ intel -= 300
        $ missionSetting = "Faire"
        show text "Launching mission.\nLocation: The Carnival."
        with d5
        pause 1.5
        hide text
        with d5
        pause 1.5
        hide text
        with d5
        $ randMusic = renpy.random.randint(1, 2)
        if randMusic == 1:
            play music "audio/music/stealth1.mp3"
        if randMusic == 2:
            play music "audio/music/stealth2.mp3"
    if missionScreenCurrentLocation == 5 and missionAreaWOOHPActive:
        $ intel -= 0
        $ missionSetting = "WOOHP"
        show text "Launching mission.\nLocation: WOOHP HQ."
        with d5
        pause 1.5
        hide text
        with d5
        pause 1.5
        hide text
        with d5
        $ randMusic = renpy.random.randint(1, 2)
        if task26Stage == 30:
            play music "audio/music/boss.mp3" fadein 3.0
            $ randMusic = 0
            $ hiddenStatus = 2
        if randMusic == 1:
            play music "audio/music/stealth1.mp3"
        if randMusic == 2:
            play music "audio/music/stealth2.mp3"
    $ activeSpy = missionScreenFrontlineSelect



    $ greenHat = 0
    $ greenAcces1 = 0
    $ greenNeck = 0
    $ greenChest = 0
    $ greenBottom = 0
    $ greenShoes = 0
    $ greenOutfit = 1
    $ greenOutfitArms = 1

    $ redHat = 0
    $ redAcces1 = 0
    $ redNeck = 0
    $ redChest = 0
    $ redBottom = 0
    $ redShoes = 0
    $ redOutfit = 1
    $ redOutfitArms = 1

    $ yellowHat = 0
    $ yellowAcces1 = 0
    $ yellowNeck = 0
    $ yellowChest = 0
    $ yellowBottom = 0
    $ yellowShoes = 0
    $ yellowOutfit = 1
    $ yellowOutfitArms = 1


    $ missionProgression = 0
    $ disableScreen = False
    $ randomBoss = 0

    jump missionBegin





label loadingLevel:

    if missionProgression >= 1:
        $ randomExit = 0
        $ randomObst1 = 0
        $ randomObst2 = 0
        $ randomObst3 = 0
        $ randomObst4 = 0
        $ randomCover1 = 0
        $ randomCover2 = 0
        $ frontExit = 0

    $ currentPosition = 0
    $ randomExit = renpy.random.randint(1, 3)
    $ frontExit = renpy.random.randint(1, 8)
    $ bonusExit = renpy.random.randint(1, 10)
    $ interSelect = renpy.random.randint(0, 2)
    $ randomBackground = renpy.random.randint(1, 12)

    if randomBackground == 12 and gadgetHookActive == False:
        $ randomBackground = 1

    if missionProgression >= 10:
        $ randomBackground = 1


    if backupSamActive:
        $ backup1 += 1
    if backupCloverActive:
        $ backup2 += 1
    if backupAlexActive:
        $ backup3 += 1
    if backupKimActive:
        $ backup4 += 1


    if controlCountDown > 0:
        $ controlCountDown -= 1


    $ interact1 = renpy.random.randint(1, 8)
    $ interact2 = renpy.random.randint(1, 8)
    $ interact3 = renpy.random.randint(1, 8)
    $ interact4 = renpy.random.randint(1, 8)


    if task2Stage <= 8 and interact2 == 8:
        $ interact2 = 0


    $ randomExit = renpy.random.randint(1, 3)


    $ randomCover1 = renpy.random.randint(1, 5)
    $ randomCover2 = renpy.random.randint(1, 5)
    $ randomCover2 = renpy.random.randint(1, 4)



    $ randomLoot = renpy.random.randint(1, 5)



    $ randomObst1 = renpy.random.randint(0, 3)
    if randomObst1 == 1:
        $ obst1FoV = renpy.random.randint(1, 3)
        if hiddenStatus == 2:
            $ obst1FoV = 2
        if slutLevel <= 2:
            $ randomAgent1 = renpy.random.randint(1, 1)
        elif slutLevel == 3:
            $ randomAgent1 = renpy.random.randint(1, 2)
        elif slutLevel == 4:
            $ randomAgent1 = renpy.random.randint(1, 3)
        $ CoS1 = renpy.random.randint(75, 80)
        $ obst1FoV = renpy.random.randint(1, 3)

        if hiddenStatus >= 1:
            $ obst1FoV = 1

        if task2Stage <= 9 and missionSetting == "School":
            $ CoS1 += 25


        if skillRank >= 1:
            $ CoS1 += 15
            $ CoS2 += 15
            $ CoS3 += 15
            $ CoS4 += 15


        if obst1FoV == 3:
            $ CoS1 += 20
        if skillTakedown == 1:
            $ CoS1 += 5
        if skillTakedown == 2:
            $ CoS1 += 10
        if skillTakedown == 3:
            $ CoS1 += 15
        if CoS1 > 100:
            $ CoS1 = 100


        if daysPlayed >= 60:
            $ CoS1 -= 5
        if daysPlayed >= 80:
            $ CoS1 -= 5


        if randomAgent1 == 2:
            $ CoS1 -= 10
            $ obst1Shield = 1
        if randomAgent1 == 3:
            $ CoS1 -= 20


    $ randomObst2 = renpy.random.randint(0, 1)
    if randomObst2 == 1:
        $ obst2FoV = renpy.random.randint(1, 3)
        if hiddenStatus == 2:
            $ obst2FoV = 2
        if slutLevel <= 2:
            $ randomAgent2 = renpy.random.randint(1, 1)
        elif slutLevel == 3:
            $ randomAgent2 = renpy.random.randint(1, 2)
        $ CoS2 = renpy.random.randint(75, 80)
        $ obst2FoV = renpy.random.randint(1, 3)

        if hiddenStatus >= 1:
            $ obst2FoV = 1

        if task2Stage <= 9 and missionSetting == "School":
            $ CoS2 += 25

        if obst2FoV == 3:
            $ CoS2 += 20
        if skillTakedown == 1:
            $ CoS2 += 5
        if skillTakedown == 2:
            $ CoS2 += 10
        if skillTakedown == 3:
            $ CoS2 += 15
        if CoS2 > 100:
            $ CoS2 = 100


        if daysPlayed >= 60:
            $ CoS2 -= 5
        if daysPlayed >= 80:
            $ CoS2 -= 5


        if randomAgent2 == 2 and day >= 60:
            $ CoS2 -= 10
            $ obst2Shield = 1
        if randomAgent1 == 3:
            $ CoS2 -= 20

    $ randomObst3 = renpy.random.randint(0, 1)
    if randomObst3 == 1:
        $ obst3FoV = renpy.random.randint(1, 3)
        if hiddenStatus == 2:
            $ obst3FoV = 2
        if slutLevel <= 2:
            $ randomAgent3 = renpy.random.randint(1, 1)
        elif slutLevel == 3:
            $ randomAgent3 = renpy.random.randint(1, 2)
        $ CoS3 = renpy.random.randint(75, 80)
        $ obst3FoV = renpy.random.randint(1, 3)

        if hiddenStatus >= 1:
            $ obst3FoV = 1

        if task2Stage <= 9 and missionSetting == "School":
            $ CoS3 += 25
        if obst3FoV == 3:
            $ CoS3 += 20
        if skillTakedown == 1:
            $ CoS3 += 5
        if skillTakedown == 2:
            $ CoS3 += 10
        if skillTakedown == 3:
            $ CoS3 += 15
        if CoS3 > 100:
            $ CoS3 = 100



        if randomAgent3 == 2 and day >= 50:
            $ CoS3 -= 10
            $ obst3Shield = 1
        if randomAgent3 == 3:
            $ CoS3 -= 20


    $ randomObst4 = renpy.random.randint(0, 1)
    if randomObst4 == 1:
        $ obst4FoV = renpy.random.randint(1, 3)
        if hiddenStatus == 2:
            $ obst4FoV = 2
        if slutLevel <= 2:
            $ randomAgent4 = renpy.random.randint(1, 1)
        elif slutLevel == 3:
            $ randomAgent4 = renpy.random.randint(1, 2)
        $ CoS4 = renpy.random.randint(75, 80)
        $ obst4FoV = renpy.random.randint(1, 3)

        if hiddenStatus >= 1:
            $ obst4FoV = 1

        if task2Stage <= 9 and missionSetting == "School":
            $ CoS4 += 25
        if obst4FoV == 3:
            $ CoS4 += 20
        if skillTakedown == 1:
            $ CoS4 += 5
        if skillTakedown == 2:
            $ CoS4 += 10
        if skillTakedown == 3:
            $ CoS4 += 15
        if CoS4 > 100:
            $ CoS4 = 100



        if randomAgent4 == 2 and day >= 60:
            $ CoS4 -= 10
            $ obst4Shield = 1
        if randomAgent4 == 3:
            $ CoS4 -= 20
    if missionProgression >= 10:
        $ randomBoss = renpy.random.randint(1,1)
    if missionProgression != 10 and randomBoss >= 1:
        $ randomBoss = 0


    if tutStage <= 4:
        $ randomObst1 = 0
        $ randomObst2 = 0
        $ randomObst3 = 0
        $ randomObst4 = 0



    show screen gadgetMenu
    if 1 <= randomBackground <= 3:
        if missionSetting == "School":
            show globalImage:
                zoom 0.25
        if missionSetting == "Castle":
            show globalImageCastle:
                zoom 0.25
        if missionSetting == "Database":
            show globalImageDatabase:
                zoom 0.25
        if missionSetting == "Faire":
            show globalImageFaire:
                zoom 0.25
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                zoom 0.25

    if 4 <= randomBackground <= 7:
        if missionSetting == "School":
            show globalImage:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "Castle":
            show globalImageCastle:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "Database":
            show globalImageDatabase:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "Faire":
            show globalImageFaire:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                xalign 1.0 yalign 0.75 zoom 0.36

    if 8 <= randomBackground <= 10:
        if missionSetting == "School":
            show globalImage:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "Castle":
            show globalImageCastle:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "Database":
            show globalImageDatabase:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "Faire":
            show globalImageFaire:
                xalign 1.0 yalign 0.75 zoom 0.36
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                xalign 1.0 yalign 0.75 zoom 0.36

    if 11 <= randomBackground <= 11:
        if missionSetting == "School":
            show globalImage:
                xalign 0.0 yalign 0.0 zoom 0.5
        if missionSetting == "Castle":
            show globalImageCastle:
                xalign 0.0 yalign 0.0 zoom 0.5
        if missionSetting == "Database":
            show globalImageDatabase:
                xalign 0.0 yalign 0.0 zoom 0.5
        if missionSetting == "Faire":
            show globalImageFaire:
                xalign 0.0 yalign 0.0 zoom 0.5
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                xalign 0.0 yalign 0.0 zoom 0.5

    if 12 <= randomBackground <= 12:
        if missionSetting == "School":
            show globalImage:
                xalign 0.0 yalign 1.0
        if missionSetting == "Castle":
            show globalImageCastle:
                xalign 0.0 yalign 1.0
        if missionSetting == "Database":
            show globalImageDatabase:
                xalign 0.0 yalign 1.0
        if missionSetting == "Faire":
            show globalImageFaire:
                xalign 0.0 yalign 1.0
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                xalign 0.0 yalign 1.0

    if 1 <= randomBackground <= 3 and droneUsed == False:
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78
    if 4 <= randomBackground <= 7 and droneUsed == False:
        show spyCornerSide:
            xalign 0.97 yalign 0.90 zoom 0.39
    if 8 <= randomBackground <= 10 and droneUsed == False:
        show spyCorner:
            xalign 0.99 yalign 0.83 zoom 0.78
    if 11 <= randomBackground <= 11 and droneUsed == False:
        show spyCorner:
            xalign 1.15 ypos 200
    if 12 <= randomBackground <= 12 and droneUsed == False:
        show spyCrouchingSide:
            xalign 0.28 yalign 0.88 zoom 0.22 rotate -2




    if 1 <= randomBackground <= 3:
        if randomObst1 == 1:

            if obst1FoV == 1:
                show obst1:
                    xalign 0.365 yalign 0.43 rotate 2 zoom 0.48
            if obst1FoV == 2:
                show obst1:
                    xalign 0.325 yalign 0.43 rotate 2 zoom 0.48 xzoom -1
            if obst1FoV == 3:
                show obst1:
                    xalign 0.35 yalign 0.43 rotate 2 zoom 0.48
        if randomObst1 == 2 and gadgetHackActive:
            show obst1:
                xalign 0.365 yalign 0.61

        if randomObst1 == 3 and missionProgression <= 9:
            $ CoS1 = renpy.random.randint(75, 80)
            $ obst1FoV = renpy.random.randint(1, 2)


        if missionProgression >= 10:
            $ interact2 = 0
            $ frontExit = 0
            hide obst1
            hide obst2
            $ randomObst1 = 0
            $ randomObst2 = 0

            if specialBossActive == True:
                if missionSetting == "Castle" and specialMaggieStatus == 1:
                    show obstMaggie:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        y "Wait a second, she's in the WOOHP Database..."
                        "Database" "Facial recognition complete. Maggie T. - Bounty: $500."
                        y "Get her, she's one of the Aces Lieutenants!"
                elif missionSetting == "Castle" and specialMelodyStatus == 1 and task6Stage == 12:
                    show obstMelody:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        $ randomBoss = 1
                        "Database" "Facial recognition complete. Melody G. - Bounty: $1200."
                        y "Time to take her down."
                elif missionSetting == "Castle" and specialCandyStatus == 1 and task16Stage == 3:
                    show obstCandy:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        "Database" "Facial recognition complete. Margaret N. - Bounty: $1800."
                        y "Time to take her down."
                elif missionSetting == "Database" and task26Stage == 23:
                    $ glassMissActive = False
                    hide screen glassScreen
                    hide screen interactScreen
                    show bossSeb:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    y "There she is!"
                    s "What do I do...?"
                    y "Just throw the bondage gadget and watch the fireworks."
                    $ missionScreenGadget1Select = 0
                    $ missionScreenGadget2Select = 0
                    $ missionScreenGadget3Select = 0
                    $ missionScreenGadget4Select = 0
                    $ renpy.pause(hard='True')
                elif missionSetting == "Database" and specialDragonStatus == 1 and task10Stage == 3:
                    show obstDragon:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        y "Wait a second, she's in the WOOHP Database..."
                        "Database" "Facial recognition complete. Carla Wong - Bounty: $500."
                        y "She's on the wanted list! Take her in!"
                elif missionSetting == "Database" and specialTaliaStatus == 1 and task18Stage == 2:
                    show obstTalia:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        y "Wait a second, she's in the WOOHP Database..."
                        "Database" "Facial recognition complete. Talia H. - Bounty: $1200."
                        y "Time to take her in. Let's make it look realistic!"
                elif missionSetting == "Database" and specialSebStatus == 1 and task23Stage == 4:
                    jump task23
                elif missionSetting == "Faire" and specialMuffyStatus == 1 and task11Stage == 4:
                    show obstMuffy:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        y "I think she's in the WOOHP database..."
                        "Database" "Facial recognition complete. Muffy Peprich - Bounty: $500."
                        y "Take her in!"
                elif missionSetting == "Faire" and specialFelicityStatus == 1 and task21Stage == 6:
                    show obstFelicity:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        y "Woah, that's way too much pink for a punker to have. Let's see what the database says..."
                        "Database" "Facial recognition complete. Felicity Fences - Bounty: $1200."
                        y "We got our target. Take her in!"
                elif missionSetting == "WOOHP" and task26Stage == 9:
                    show obstBritney:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        y "There she is! Punch her! Punch her really hard!"
                elif missionSetting == "WOOHP" and task26Stage == 14:
                    show obstTim1:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    if randomBossHP == 3:
                        y "There he is!"
                        y "PUNCH HIM IN HIS STUPID HANDSOME FACE!"
                elif missionSetting == "WOOHP" and task26Stage == 25:
                    $ glassMissActive = False
                    hide screen glassScreen
                    hide screen interactScreen
                    show fightAlex:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                    y "There's our banana. Quickly, throw the bondage gadget at her and let's get her out of here!"
                    $ missionScreenGadget1Select = 0
                    $ missionScreenGadget2Select = 0
                    $ missionScreenGadget3Select = 0
                    $ missionScreenGadget4Select = 0
                    $ renpy.pause(hard='True')
                elif True:
                    if randomBoss == 1:
                        $ randomBossHP = 3
                        show obstHulk:
                            xalign 0.5 yalign 0.48 zoom 0.5 rotate 3
                        if task26Stage == 30:
                            $ randomBossHP = 5
            elif True:

                if randomBoss == 1:
                    $ randomBossHP = 3
                    show obstHulk:
                        xalign 0.5 yalign 0.48 zoom 0.5 rotate 3

        if randomObst2 == 1:

            if obst2FoV == 1:
                show obst2:
                    xalign 0.623 yalign 0.49 rotate 6 zoom 0.30
            if obst2FoV == 2:
                show obst2:
                    xalign 0.623 yalign 0.49 rotate 2 zoom 0.30 xzoom -1
            if obst2FoV == 3:
                show obst2:
                    xalign 0.623 yalign 0.49 rotate 6 zoom 0.30


        if randomObst1 == 3 and missionProgression <= 9:
            play sound "audio/sfx/glassBreaking.mp3"
            show obst1:
                xalign 0.425 ypos -1.8 zoom 0.41
                linear 1.0 yalign -0.45
            pause 1.35
            hide obst1
            with d2
            $ randomObst1 = 1
            $ randomAgent1 = 1
            if task2Stage <= 9:
                $ CoS1 = 100
            show obst1:
                xalign 0.365 yalign 0.43 rotate 2 zoom 0.48
            with d2


    if 4 <= randomBackground <= 7:
        if randomObst1 == 1:
            if obst1FoV == 1:
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48 xzoom -1
            if obst1FoV == 2:
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48
            if obst1FoV == 3:
                show obst1:
                    xalign 0.64 yalign 0.99 zoom 0.48

    if 8 <= randomBackground <= 10:

        if randomObst3 == 1:
            show obst3:
                xalign 0.52 yalign 0.40 zoom 0.25

        if randomObst1 == 1:
            show obst1:
                xalign 0.535 yalign 0.50 zoom 0.49

    if 11 <= randomBackground <= 11:

        if randomObst1 >= 3:
            $ randomObst1 = 1


        if randomObst1 == 1:
            show obst1:
                xalign 0.4 yalign 1.1 zoom 0.7
        if randomObst1 == 2:
            show obst1:
                xpos 137 yalign 0.61



    show screen equipmentMenu

    if task23Stage == 2 and missionSetting == "Database":
        jump task23

    if randomBackground == 12 and gadgetHookActive == False:
        "The path is blocked. Looks like you'll need a specific piece of equipment to get higher up."
        $ missionProgression -= 1
        jump missionBegin
    return

label missionBegin:

    $ _skipping = False






    hide spyCrouchingSide
    hide spyCrouchCorner
    hide spyCornerSide

    hide dramaCumSam
    hide dramaCumClover
    hide dramaCumAlex

    hide scene_camera

    $ missionProgression += 1
    if missionProgression >= 11:
        $ missionProgression = 9
        "WARNING: mission.rpy. missionProgression: [missionProgression] \nThe game has encountered an error. Attempting to fix it. If you get this message again, please contact exiscoming."


    $ randomHack = 0
    $ hackResult = 0
    $ hackSkillUsed = False
    $ hackAvail = True
    $ hackFailed = False


    if flashbangActive == 1:
        $ flashbangActive = 2
    elif flashbangActive == 2:
        $ flashbangActive = 0


    $ gadgetUsed = 0


    $ backupUsed = 0


    $ target1LoveActive = False
    $ target1PoisonActive = False


    $ randomGlass = 0
    $ randomGlass = renpy.random.randint(1,3)

    if missionProgression == 4:
        if tutStage == 4:
            show globalImage:
                zoom 0.25
            hide screen interactScreen
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            $ randomExit = 1
            $ currentPosition = 0
            $ randomCover2 = 0
            $ randomCover1 = 0
            $ randomBackground = 1
            with fade
            jump tutStage5

        if task2Stage == 1 and missionSetting == "School":
            hide spyCrouchCorner
            hide spyCorner
            $ task2Stage = 2
            pause 0.001
            jump task2

        if task2Stage == 2 and missionSetting == "School":
            hide spyCrouchCorner
            hide spyCorner
            $ task2Stage = 3
            pause 0.001
            jump task2

        if task2Stage == 4 and missionSetting == "School":
            hide spyCrouchCorner
            hide spyCorner
            $ task2Stage = 5
            pause 0.001
            jump task2

        if task4Stage == 2:
            $ randomCover2 = 2
            $ randomCover1 = 2
            $ randomBackground = 1
            jump task4

        if task25Stage == 3 and missionSetting == "Faire":
            hide screen equipmentMenu
            $ kandHidden = False
            $ randomExit = 1
            $ currentPosition = 0
            $ randomCover2 = 1
            $ randomCover1 = 0
            $ randomBackground = 1
            show globalImageFaire:
                zoom 0.25
            show kandModel:
                xalign 0.6 yalign 0.45 rotate 0.7 zoom 0.3
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            with fade
            jump task25

        if 6 <= task25Stage <= 8 and missionSetting == "Faire":
            hide screen equipmentMenu
            $ kandHidden = False
            $ randomExit = 1
            $ currentPosition = 0
            $ randomCover2 = 1
            $ randomCover1 = 0
            $ randomBackground = 1
            show globalImageFaire:
                zoom 0.25
            show kandModel:
                xalign 0.6 yalign 0.45 rotate 0.7 zoom 0.3
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            with fade
            jump task25

    if missionProgression == 8:

        if task23Stage == 3 and missionSetting == "Database":
            jump task23
        if tutStage == 5:
            jump tutStage6
        if task4Stage == 3:
            $ randomExit = 0
            $ randomCover2 = 1
            $ randomCover1 = 3
            $ randomBackground = 2
            jump task4
        if task24Stage == 1 and missionSetting == "Faire":
            jump task24

        if task25Stage == 5 and missionSetting == "Faire":
            hide screen equipmentMenu
            $ randomExit = 1
            $ currentPosition = 0
            $ randomCover2 = 1
            $ randomCover1 = 0
            $ randomBackground = 2
            show globalImageFaire:
                zoom 0.25
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            with fade
            jump task25

    if missionProgression >= 10:
        if tutStage == 6.5:
            hide spyCrouchCorner
            hide spyCornerSide
            hide spyCorner
            jump tutStage65
        if task2Stage == 8:
            $ randomBoss = 1
            scene black with d1
            jump task2
        if task10Stage == 2:
            $ randomBoss = 0
            scene black with d1
            jump task10
        if 2 <= task12Stage <= 3 and missionSetting == "Database":
            $ task12Stage = 2
            jump task12

        if task25Stage == 7 and missionSetting == "Faire":
            hide screen equipmentMenu
            $ randomExit = 1
            $ currentPosition = 0
            $ randomCover2 = 1
            $ randomCover1 = 0
            $ randomBackground = 2
            show globalImageFaire:
                zoom 0.25
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            with fade
            jump task25
    elif True:
        pass
    scene black
    pause 0.01
    call loadingLevel from _call_loadingLevel

    if flashbangSpecial == True:
        $ flashbangSpecial = False
        $ randomObst1 = 0
        $ randomObst2 = 0
        $ randomObst3 = 0
        $ randomObst4 = 0

    if droneUsed:
        hide spyCrouchingSide
        hide spyCrouchCorner
        hide spyCornerSide
        show scene_camera
        hide screen equipmentMenu
        pause
        menu:
            "{color=#ff8533}Blow-up!{/color}" if droneUpgrade:
                $ droneUsed = False
                $ hiddenStatus += 1
                play sound "audio/sfx/droneExpl.mp3"
                pause 0.3
                show white with d1
                hide scene_camera
                if randomObst1 >= 1:
                    $ randomObst1 = 0
                if randomObst1 == 0 and randomObst2 >= 1:
                    $ randomObst2 = 0
                if randomObst1 == 0 and randomObst3 >= 1:
                    $ randomObst3 = 0
                if missionProgression == 10 and randomBossHP >= 2:
                    $ randomBossHP -= 1
                pause 1.0
                hide white with d10
                if 1 <= randomBackground <= 3:
                    show jumpBackup:
                        xalign 1.0 yalign 0.9
                    pause 0.07
                    hide jumpBackup
                    show spyCorner:
                        xalign 0.90 yalign 0.83 zoom 0.78
                    with d2
                if 4 <= randomBackground <= 7:
                    show jumpBackup:
                        xalign 1.0 yalign 0.9
                    pause 0.07
                    hide jumpBackup
                    show spyCornerSide:
                        xalign 0.97 yalign 0.90 zoom 0.39
                    with d2
                if 8 <= randomBackground <= 10:
                    show jumpBackup:
                        xalign 1.1 yalign 0.9
                    pause 0.07
                    hide jumpBackup with d1
                    show spyCorner:
                        xalign 0.99 yalign 0.83 zoom 0.78
                    with d2
                show screen equipmentMenu
                call screen interactScreen
            "Head in" if True:
                $ droneUsed = False
                hide scene_camera
                with d3
                if 1 <= randomBackground <= 3:
                    show jumpBackup:
                        xalign 1.0 yalign 0.9
                    pause 0.07
                    hide jumpBackup
                    show spyCorner:
                        xalign 0.90 yalign 0.83 zoom 0.78
                    with d2
                if 4 <= randomBackground <= 7:
                    show jumpBackup:
                        xalign 1.0 yalign 0.9
                    pause 0.07
                    hide jumpBackup
                    show spyCornerSide:
                        xalign 0.97 yalign 0.90 zoom 0.39
                    with d2
                if 8 <= randomBackground <= 10:
                    show jumpBackup:
                        xalign 1.1 yalign 0.9
                    pause 0.07
                    hide jumpBackup with d1
                    show spyCorner:
                        xalign 0.99 yalign 0.83 zoom 0.78
                    with d2
                show screen equipmentMenu
            "Take detour" if True:
                $ droneUsed = False
                hide scene_camera
                $ missionProgression -= 1
                hide obst1
                hide obst2
                call loadingLevel from _call_loadingLevel_1
                call screen interactScreen


    if controlCountDown == 0 and task4Stage >= 4 and droneUsed == False:
        $ chanceOfControl = renpy.random.randint(1,100)
        if activeSpy == 1 and nanoLevelSam >= 80 or activeSpy == 2 and nanoLevelClover >= 80 or activeSpy == 3 and nanoLevelAlex >= 80:
            $ chanceOfControl += 15
        elif activeSpy == 1 and nanoLevelSam >= 70 or activeSpy == 2 and nanoLevelClover >= 70 or activeSpy == 3 and nanoLevelAlex >= 70:
            $ chanceOfControl += 10
        elif activeSpy == 1 and nanoLevelSam >= 60 or activeSpy == 2 and nanoLevelClover >= 60 or activeSpy == 3 and nanoLevelAlex >= 60:
            $ chanceOfControl += 5
        if chanceOfControl >= 90 and controlCountDown == 0 and missionProgression != 10:
            $ controlCountDown = 4
            play sound "audio/sfx/shockcrash.mp3"
            "V.I.B." "Danger! Nanobot control detected. Use your V.I.B. by pressing 1 on your keyboard."

            $ renpy.pause(2.0, hard='True')

            hide spyCrouchCorner
            hide spyCrouchingSide
            hide spyCorner
            hide spyCornerSide
            with d3
            "Your spy was controlled and ran away!"
            $ chanceOfControl = 0
            call spyHitBackup from _call_spyHitBackup_9
            call screen interactScreen
    label jumpStartScene:
        pass
    show screen gadgetMenu
    call screen interactScreen
    $ renpy.pause(hard='True')






layeredimage bgDebrief:
    always:
        "gui/debrief/bgDebrief.jpg"

    if spyGreenActive:
        "gui/debrief/head1.png"
        xalign 0.23 yalign 0.55 zoom 0.45
    if spyGreenActive == False:
        "gui/debrief/headLocked1.png"
        xalign 0.23 yalign 0.55 zoom 0.45

    if spyRedActive:
        "gui/debrief/head2.png"
        xalign 0.23 yalign 0.65 zoom 0.45
    if spyRedActive == False:
        "gui/debrief/headLocked2.png"
        xalign 0.23 yalign 0.65 zoom 0.45

    if spyYellowActive:
        "gui/debrief/head3.png"
        xalign 0.23 yalign 0.75 zoom 0.45
    if spyYellowActive == False:
        "gui/debrief/headLocked3.png"
        xalign 0.23 yalign 0.75 zoom 0.45

screen debriefHealth:
    if spyGreenActive:
        if samHealth == 3:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Healthy{/color}{/font}":
                xalign 0.30 yalign 0.55
        if samHealth == 2:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Hurt{/color}{/font}":
                xalign 0.30 yalign 0.55
        if samHealth == 1:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Badly hurt{/color}{/font}":
                xalign 0.30 yalign 0.55
        if samHealth == 0:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}K.O.{/color}{/font}":
                xalign 0.30 yalign 0.55
    else:
        text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}- - -{/color}{/font}":
            xalign 0.30 yalign 0.55

    if spyRedActive:
        if cloverHealth == 3:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Healthy{/color}{/font}":
                xalign 0.30 yalign 0.65
        if cloverHealth == 2:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Hurt{/color}{/font}":
                xalign 0.30 yalign 0.65
        if cloverHealth == 1:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Badly hurt{/color}{/font}":
                xalign 0.30 yalign 0.65
        if cloverHealth == 0:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}K.O.{/color}{/font}":
                xalign 0.30 yalign 0.65
    else:
        text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}- - -{/color}{/font}":
            xalign 0.30 yalign 0.65

    if spyYellowActive:
        if alexHealth == 3:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Healthy{/color}{/font}":
                xalign 0.30 yalign 0.75
        if alexHealth == 2:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Hurt{/color}{/font}":
                xalign 0.30 yalign 0.75
        if alexHealth == 1:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}Badly hurt{/color}{/font}":
                xalign 0.30 yalign 0.75
        if alexHealth == 0:
            text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}K.O.{/color}{/font}":
                xalign 0.30 yalign 0.75
    else:
        text "{font=fonts/freshmarker.ttf}{color=#CA1A1E}- - -{/color}{/font}":
            xalign 0.30 yalign 0.75

screen lootText:
    text "{font=fonts/freshMarker.ttf}{color=#ffffff}X [loot1]{/color}{/font}":
        xalign 0.61 yalign 0.50
    text "{font=fonts/freshMarker.ttf}{color=#ffffff}X [loot2]{/color}{/font}":
        xalign 0.61 yalign 0.65
    text "{font=fonts/freshMarker.ttf}{color=#ffffff}X [loot3]{/color}{/font}":
        xalign 0.61 yalign 0.80
    text "{font=fonts/freshMarker.ttf}{color=#ffffff}X [loot4]{/color}{/font}":
        xalign 0.78 yalign 0.50
    text "{font=fonts/freshMarker.ttf}{color=#ffffff}X [loot5]{/color}{/font}":
        xalign 0.78 yalign 0.65
    text "{font=fonts/freshMarker.ttf}{color=#ffffff}X [loot6]{/color}{/font}":
        xalign 0.78 yalign 0.80

image debriefAni = "gui/debrief/debriefAni.png"

label missionComplete:
    hide screen reloadGun
    hide screen gadgetMenu
    hide screen glassScreen
    $ glassMissActive = False
    $ gadgetActive = 0
    hide screen spyMasturbate
    $ _skipping = True
    if activeSpy == 1:
        sM "Mission complete!"
    if activeSpy == 2:
        cM "Mission complete!"
    if activeSpy == 3:
        aM "Mission complete!"
    y "All right, I'm getting you out of there."
    stop music fadeout 2.5
    hide globalImage
    hide screen interactScreen
    hide screen equipmentMenu
    scene black
    with fade
    pause 0.5

    play music "audio/music/debrief.mp3" fadein 1.0
    scene bgDebrief
    show screen debriefHealth
    with fade
    play sound "audio/sfx/lootbox.mp3"
    show debriefAni:
        xalign 0.75 yalign 0.27 zoom 3.0
        linear 0.13 xalign 0.75 yalign 0.27 zoom 1.0
    $ renpy.pause(0.14, hard='True')
    show screen lootText

    if missionSetting == "School":
        show itemMatsDust:
            xalign 0.55 yalign 0.50 zoom 0.35
        show itemMatsGlue:
            xalign 0.55 yalign 0.65 zoom 0.35
        show itemIntel1:
            xalign 0.55 yalign 0.80 zoom 0.35
        show itemPhone:
            xalign 0.70 yalign 0.50 zoom 0.35
        show itemTest:
            xalign 0.70 yalign 0.65 zoom 0.35
        show itemTrophy:
            xalign 0.70 yalign 0.80 zoom 0.36
        $ matsDust += loot1
        $ matsGlue += loot2
        $ intelBoost += loot3

    if missionSetting == "Castle":
        show itemMatsAcid:
            xalign 0.55 yalign 0.50 zoom 0.35
        show itemMatsChip:
            xalign 0.55 yalign 0.65 zoom 0.35
        show itemIntel1:
            xalign 0.55 yalign 0.80 zoom 0.35
        show itemCandle:
            xalign 0.70 yalign 0.50 zoom 0.35
        show itemTest:
            xalign 0.70 yalign 0.65 zoom 0.35
        show itemVase:
            xalign 0.70 yalign 0.80 zoom 0.36
        $ matsAcid += loot1
        $ matsChip += loot2
        $ intelBoost += loot3

    if missionSetting == "Database":
        show itemMatsDust:
            xalign 0.55 yalign 0.50 zoom 0.35
        show itemMatsChip:
            xalign 0.55 yalign 0.65 zoom 0.35
        show itemIntel1:
            xalign 0.55 yalign 0.80 zoom 0.35
        show itemData1:
            xalign 0.70 yalign 0.50 zoom 0.35
        show itemTest:
            xalign 0.70 yalign 0.65 zoom 0.35
        show itemData2:
            xalign 0.70 yalign 0.80 zoom 0.36
        $ matsDust += loot1
        $ matsChip += loot2
        $ intelBoost += loot3

    if missionSetting == "Faire":
        show itemMatsDust:
            xalign 0.55 yalign 0.50 zoom 0.35
        show itemMatsWires:
            xalign 0.55 yalign 0.65 zoom 0.35
        show itemIntel1:
            xalign 0.55 yalign 0.80 zoom 0.35
        show itemCashRegister:
            xalign 0.70 yalign 0.50 zoom 0.36
        show itemTest:
            xalign 0.70 yalign 0.65 zoom 0.35
        show itemCashRegister:
            xalign 0.70 yalign 0.80 zoom 0.36
        $ matsDust += loot1
        $ matsWires += loot2
        $ intelBoost += loot3

    if missionSetting == "WOOHP":
        show itemMatsValu:
            xalign 0.55 yalign 0.50 zoom 0.35
        show itemMatsGlue:
            xalign 0.55 yalign 0.65 zoom 0.35
        show itemMatsChip:
            xalign 0.55 yalign 0.80 zoom 0.35
        show intel1:
            xalign 0.70 yalign 0.50 zoom 0.36
        show itemTest:
            xalign 0.70 yalign 0.65 zoom 0.35
        show intel2:
            xalign 0.70 yalign 0.80 zoom 0.36
        $ matsValu += loot1
        $ matsGlue += loot2
        $ matsChip += loot3


    $ backupSamActive = False
    $ backupCloverActive = False
    $ backupAlexActive = False

    $ samOnMission = False
    $ cloverOnMission = False
    $ alexOnMission = False

    $ randomBoss = 0


    call screen debriefCont
    $ cashEarned4 = loot4 * 50
    $ cashEarned5 = loot5 * 75
    $ cashEarned6 = loot6 * 80
    $ cashEarned = cashEarned4 + cashEarned5 + cashEarned6
    if missionSetting == "WOOHP":
        $ cashEarned = cashEarned * 5
        $ intel += cashEarned
        if cashEarned >= 1:
            "You store your materials and study what you've gathered and get [cashEarned] intel."
            $ randIntel = cashEarned
            call missionRewardInt from _call_missionRewardInt_34
    elif True:
        $ cash += cashEarned
        if cashEarned >= 1:
            "You store your materials and sell your loot and gain $ [cashEarned]."
            $ randMoney = cashEarned
            call missionRewardMoney from _call_missionRewardMoney_72
    $ cashEarned4 = 0
    $ cashEarned5 = 0
    $ cashEarned6 = 0
    hide screen debriefHealth
    hide screen lootText
    scene black
    with fade
    stop music fadeout 1.0

    $ loot1 = 0
    $ loot2 = 0
    $ loot3 = 0
    $ loot4 = 0
    $ loot5 = 0
    $ loot6 = 0

    if task2Stage == 9:
        jump task2
    jump jobReport

label spyHitBackup:
    show screen gadgetMenu
    if 1 <= randomBackground <= 3:
        if backupSamActive:
            $ backupSamActive = False
            if activeSpy == 2:
                play sound "audio/voice/worriedClover.mp3"
            if activeSpy == 3:
                play sound "audio/voice/worriedAlex.mp3"
            $ activeSpy = 1
            if currentPosition == 0:
                show jumpBackup:
                    xalign 1.0 yalign 0.9
                pause 0.07
                hide jumpBackup
                show spyCorner:
                    xalign 0.90 yalign 0.83 zoom 0.78
                with d2

            if currentPosition == 1:
                show jumpBackup:
                    xalign 1.0 yalign 0.9
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign -0.03 yalign 0.84 zoom 0.405
                with d2

        elif backupCloverActive:
            $ backupCloverActive = False
            if activeSpy == 1:
                play sound "audio/voice/clover/worriedSam.mp3"
            if activeSpy == 3:
                play sound "audio/voice/clover/worriedAlex.mp3"
            $ activeSpy = 2
            if currentPosition == 0:
                show jumpBackup:
                    xalign 1.0 yalign 0.9
                pause 0.07
                hide jumpBackup
                show spyCorner:
                    xalign 0.90 yalign 0.83 zoom 0.78
                with d2

            if currentPosition == 1:
                show jumpBackup:
                    xalign 1.0 yalign 0.9
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign -0.03 yalign 0.84 zoom 0.405
                with d2

        elif backupAlexActive:
            $ backupAlexActive = False
            if activeSpy == 1:
                play sound "audio/voice/alex/worriedSam.mp3"
            if activeSpy == 2:
                play sound "audio/voice/alex/worriedClover.mp3"
            $ activeSpy = 3
            if currentPosition == 0:
                show jumpBackup:
                    xalign 1.0 yalign 0.9
                pause 0.07
                hide jumpBackup
                show spyCorner:
                    xalign 0.90 yalign 0.83 zoom 0.78
                with d2

            if currentPosition == 1:
                show jumpBackup:
                    xalign 1.0 yalign 0.9
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign -0.03 yalign 0.84 zoom 0.405
                with d2
        elif True:
            if task25Stage == 8:
                kand "Alakazam!"
                show black with fade
                y "Don't give up girls, you can do it!"
                "Your spies crawl back up to their feet."
                $ backupCloverActive = True
                $ backupAlexActive = True
                $ activeSpy = 1
                show spyCorner:
                    xalign 0.90 yalign 0.83 zoom 0.78
                show screen equipmentMenu
                hide black
                with fade
                y "That shield is blocking all of your attacks! Try finding a way to dispell it!"
                $ renpy.pause(hard='True')
            hide screen equipmentMenu
            scene black with longFade

            $ _skipping = True
            call allKnockedOut from _call_allKnockedOut
        if task25Stage == 8:
            call screen interactScreenBonus
        if task26Stage == 9 and missionProgression == 10 and missionSetting == "WOOHP":
            return
        if task26Stage == 14 and missionProgression == 10 and missionSetting == "WOOHP":
            return
        if task23Stage == 7 and missionSetting == "Database":
            return
        call screen interactScreen
    if 4 <= randomBackground <= 7:
        if backupSamActive:
            $ backupSamActive = False
            if activeSpy == 2:
                play sound "audio/voice/worriedClover.mp3"
            if activeSpy == 3:
                play sound "audio/voice/worriedAlex.mp3"
            $ activeSpy = 1
            show jumpBackup
            pause 0.07
            hide jumpBackup with d1
            if currentPosition == 0:
                show spyCornerSide:
                    xalign 0.97 yalign 0.90 zoom 0.39
            if currentPosition == 1:
                show spyCornerSide:
                    xalign 0.88 yalign 0.90 zoom 0.39
            if currentPosition == 3:
                show spyCornerSide:
                    xalign 0.497 yalign 0.59 zoom 0.37 xzoom -1
            if currentPosition == 4:
                show spyCornerSide:
                    xalign 0.46 yalign 0.16 zoom 0.27
            with d2
            call screen interactScreen
        elif backupCloverActive:
            $ backupCloverActive = False
            if activeSpy == 1:
                play sound "audio/voice/clover/worriedSam.mp3"
            if activeSpy == 3:
                play sound "audio/voice/clover/worriedAlex.mp3"
            $ activeSpy = 2
            show jumpBackup
            pause 0.07
            hide jumpBackup with d1
            if currentPosition == 0:
                show spyCornerSide:
                    xalign 0.97 yalign 0.90 zoom 0.39
            if currentPosition == 1:
                show spyCornerSide:
                    xalign 0.88 yalign 0.90 zoom 0.39
            if currentPosition == 3:
                show spyCornerSide:
                    xalign 0.497 yalign 0.59 zoom 0.37 xzoom -1
            if currentPosition == 4:
                show spyCornerSide:
                    xalign 0.46 yalign 0.16 zoom 0.27
            with d2
            call screen interactScreen
        elif backupAlexActive:
            $ backupAlexActive = False
            if activeSpy == 1:
                play sound "audio/voice/alex/worriedSam.mp3"
            if activeSpy == 2:
                play sound "audio/voice/alex/worriedClover.mp3"
            $ activeSpy = 3
            show jumpBackup
            pause 0.07
            hide jumpBackup with d1
            if currentPosition == 0:
                show spyCornerSide:
                    xalign 0.97 yalign 0.90 zoom 0.39
            if currentPosition == 1:
                show spyCornerSide:
                    xalign 0.88 yalign 0.90 zoom 0.39
            if currentPosition == 3:
                show spyCornerSide:
                    xalign 0.497 yalign 0.59 zoom 0.37 xzoom -1
            if currentPosition == 4:
                show spyCornerSide:
                    xalign 0.46 yalign 0.16 zoom 0.27
            with d2
            call screen interactScreen
        elif True:
            hide screen equipmentMenu
            scene black with longFade

            $ _skipping = True
            call allKnockedOut from _call_allKnockedOut_1

        jump jumpStartScene
    if 8 <= randomBackground <= 10:
        if backupSamActive:
            $ backupSamActive = False
            if activeSpy == 2:
                play sound "audio/voice/worriedClover.mp3"
            if activeSpy == 3:
                play sound "audio/voice/worriedAlex.mp3"
            $ activeSpy = 1
            show jumpBackup:
                xalign 1.1 yalign 0.9
            pause 0.07
            hide jumpBackup
            with d1
            if currentPosition == 0:
                show spyCorner:
                    xalign 0.99 yalign 0.83 zoom 0.78
                with d2
            if currentPosition == 2:
                show spyCrouchCorner:
                    xalign -0.1 yalign 1.5 rotate -3 zoom 0.52
                with d2
            call screen interactScreen
        elif backupCloverActive:
            $ backupCloverActive = False
            if activeSpy == 1:
                play sound "audio/voice/clover/worriedSam.mp3"
            if activeSpy == 3:
                play sound "audio/voice/clover/worriedAlex.mp3"
            $ activeSpy = 2
            show jumpBackup:
                xalign 1.1 yalign 0.9
            pause 0.07
            hide jumpBackup
            with d1
            if currentPosition == 0:
                show spyCorner:
                    xalign 0.99 yalign 0.83 zoom 0.78
                with d2
            if currentPosition == 2:
                show spyCrouchCorner:
                    xalign -0.1 yalign 1.5 rotate -3 zoom 0.52
                with d2
            call screen interactScreen
        elif backupAlexActive:
            $ backupAlexActive = False
            if activeSpy == 1:
                play sound "audio/voice/alex/worriedSam.mp3"
            if activeSpy == 2:
                play sound "audio/voice/alex/worriedClover.mp3"
            $ activeSpy = 3
            show jumpBackup:
                xalign 1.1 yalign 0.9
            pause 0.07
            hide jumpBackup
            with d1
            if currentPosition == 0:
                show spyCorner:
                    xalign 0.99 yalign 0.83 zoom 0.78
                with d2
            if currentPosition == 2:
                show spyCrouchCorner:
                    xalign -0.1 yalign 1.5 rotate -3 zoom 0.52
                with d2
            call screen interactScreen
        elif True:
            hide screen equipmentMenu
            scene black with longFade

            $ _skipping = True
            call allKnockedOut from _call_allKnockedOut_2
        jump jumpStartScene
    if 11 <= randomBackground <= 11:
        if backupSamActive:
            $ backupSamActive = False
            if activeSpy == 2:
                play sound "audio/voice/worriedClover.mp3"
            if activeSpy == 3:
                play sound "audio/voice/worriedAlex.mp3"
            $ activeSpy = 1
            if currentPosition == 0:
                show jumpBackup:
                    xalign 1.2 yalign 1.1
                pause 0.07
                hide jumpBackup
                show spyCorner:
                    xalign 1.15 ypos 200
                with d2
                call screen interactScreen
            if currentPosition == 2:
                show jumpBackup:
                    xalign 1.0 yalign 0.9 zoom 0.8
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign 0.96 yalign 1.1 rotate 5 zoom 0.39 xzoom -1
                with d2
            if currentPosition == 3:
                show jumpBackup:
                    xalign 1.0 yalign 0.9 zoom 0.8
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign 0.22 yalign 0.81 rotate -5 zoom 0.38
                with d2

        elif backupCloverActive:
            $ backupCloverActive = False
            if activeSpy == 1:
                play sound "audio/voice/clover/worriedSam.mp3"
            if activeSpy == 3:
                play sound "audio/voice/clover/worriedAlex.mp3"
            $ activeSpy = 2
            if currentPosition == 0:
                show jumpBackup:
                    xalign 1.2 yalign 1.1
                pause 0.07
                hide jumpBackup
                show spyCorner:
                    xalign 1.15 ypos 200
                with d2
                call screen interactScreen
            if currentPosition == 2:
                show jumpBackup:
                    xalign 1.0 yalign 0.9 zoom 0.8
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign 0.96 yalign 1.1 rotate 5 zoom 0.39 xzoom -1
                with d2
            if currentPosition == 3:
                show jumpBackup:
                    xalign 1.0 yalign 0.9 zoom 0.8
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign 0.22 yalign 0.81 rotate -5 zoom 0.38
                with d2

        elif backupAlexActive:
            $ backupAlexActive = False
            if activeSpy == 1:
                play sound "audio/voice/alex/worriedSam.mp3"
            if activeSpy == 2:
                play sound "audio/voice/alex/worriedClover.mp3"
            $ activeSpy = 3
            if currentPosition == 0:
                show jumpBackup:
                    xalign 1.2 yalign 1.1
                pause 0.07
                hide jumpBackup
                show spyCorner:
                    xalign 1.15 ypos 200
                with d2
                call screen interactScreen
            if currentPosition == 2:
                show jumpBackup:
                    xalign 1.0 yalign 0.9 zoom 0.8
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign 0.96 yalign 1.1 rotate 5 zoom 0.39 xzoom -1
                with d2
            if currentPosition == 3:
                show jumpBackup:
                    xalign 1.0 yalign 0.9 zoom 0.8
                pause 0.07
                hide jumpBackup
                show spyCrouchCorner:
                    xalign 0.22 yalign 0.81 rotate -5 zoom 0.38
                with d2
        elif True:
            hide screen equipmentMenu
            scene black with longFade

            $ _skipping = True
            call allKnockedOut from _call_allKnockedOut_3
        call screen interactScreen

        jump jumpStartScene


label reduceHealth:
    if activeSpy == 1:
        $ samHealth -= 1
        $ backupSamActive = False
    elif activeSpy == 2:
        $ cloverHealth -= 1
        $ backupCloverActive = False
    elif activeSpy == 3:
        $ alexHealth -= 1
        $ backupAlexActive = False
    elif True:
        pass
    return
    "DEV: ERROR LABEL reduceHealth. Please report this to Exiscoming."

label captureCalculator:
    if spyGreenActive and samOnMission:
        $ spy1Status = 999
    if spyRedActive and cloverOnMission:
        $ spy2Status = 999
    if spyYellowActive and alexOnMission:
        $ spy3Status = 999


    $ backupSamActive = False
    $ backupCloverActive = False
    $ backupAlexActive = False

    $ samOnMission = False
    $ cloverOnMission = False
    $ alexOnMission = False

    $ randomBoss = 0
    return
    "DEV: ERROR LABEL captureCalculator. Please report this to Exiscoming"

label allKnockedOut:
    if 1 <= task4Stage <= 3:
        "Your spies take some time to collect themselves and quickly regroup."
        $ backupCloverActive = True
        $ activeSpy = 1
        $ missionProgression -= 1
        if missionProgression == 10:
            $ missionProgression = 9
        jump missionBegin
    if task10Stage == 2:
        "Your spies take some time to collect themselves and quickly regroup."
        $ backupAlexActive = True
        $ activeSpy = 1
        if missionProgression == 10:
            $ missionProgression = 9
        jump missionBegin
    if task16Stage == 3:
        "Your spies take some time to collect themselves and quickly regroup."
        $ backupAlexActive = True
        $ activeSpy = 2
        if missionProgression == 10:
            $ missionProgression = 9
        jump missionBegin
    if 3 <= task23Stage <= 5:
        "Your spy wakes up a few minutes later..."
        $ missionProgression = 6
        jump missionBegin
    if 3 <= task25Stage <= 7:
        "Your spies take some time to collect themselves and quickly regroup."
        $ backupCloverActive = True
        $ backupAlexActive = True
        $ activeSpy = 1
        if missionProgression == 10:
            $ missionProgression = 9
        show screen equipmentMenu
        jump missionBegin
    if task26Stage == 9:
        "Your spies take some time to collect themselves and quickly regroup."
        $ backupCloverActive = True
        $ backupAlexActive = True
        $ activeSpy = 1
        if missionProgression == 10:
            $ missionProgression = 9
        show screen equipmentMenu
        jump missionBegin
    if task26Stage == 14:
        "Your spies take some time to collect themselves and quickly regroup."
        $ backupCloverActive = True
        $ backupAlexActive = True
        $ activeSpy = 1
        if missionProgression == 10:
            $ missionProgression = 9
        show screen equipmentMenu
        jump missionBegin
    if task26Stage == 23:
        "Your spies take some time to collect themselves and quickly regroup."
        $ activeSpy = 1
        if missionProgression == 10:
            $ missionProgression = 9
        show screen equipmentMenu
        jump missionBegin
    if task26Stage == 25 or task26Stage >= 30:
        "Your spies take some time to collect themselves and quickly regroup."
        $ backupCloverActive = True
        $ activeSpy = 1
        if missionProgression == 10:
            $ missionProgression = 9
        show screen equipmentMenu
        jump missionBegin
    elif True:
        pass
    hide screen gadgetMenu
    $ gadgetActive = 0
    hide screen glassScreen
    "All spies were knocked out during the mission."
    $ randRansom = renpy.random.randint(150, 250)
    if day >= 25:
        $ randRansom += 100
    if day >= 50:
        $ randRansom += 150
    if day >= 75:
        $ randRansom += 200
    if day >= 75:
        $ randRansom += 250
    "The ransom is $ [randRansom]. You can pay now or wait for your spies to escape on their own."
    menu:
        "Pay $ [randRansom]" if cash >= randRansom:
            $ cash -= randRandsom
            "Your spies were returned to you later that evening..."
        "Wait for them to escape" if True:
            call captureCalculator from _call_captureCalculator
            "Believing in your spys abilities, you decide not to ransom them."
    jump jobReport

label useVIB1:
    play sound "audio/sfx/vib.mp3"
    hide spyCrouchCorner
    hide spyCrouchingSide
    hide spyCorner
    hide spyCornerSide
    with d2
    if 1 <= randomBackground <= 3:
        if currentPosition == 0:
            show spyMasturbate:
                xalign 0.87 yalign 0.79 zoom 0.75
            with d2
        elif currentPosition == 1:
            show spyMasturbate:
                xalign -0.1 yalign 0.67 zoom 0.53 rotate 4
            with d2
        elif currentPosition == 2:
            show spyMasturbate:
                xalign 0.81 yalign 1.1 zoom 0.53
            with d2
    if 4 <= randomBackground <= 7:
        if currentPosition == 0:
            show spyMasturbate:
                xalign 0.98 yalign 0.91 zoom 0.4
            with d2
        elif currentPosition == 1:
            show spyMasturbate:
                xalign 0.87 yalign 0.9 zoom 0.4
            with d2
        elif currentPosition == 2:
            show spyMasturbate:
                xalign 0.71 yalign 0.9 zoom 0.42
            with d2
        elif currentPosition == 3:
            show spyMasturbate:
                xalign 0.5 yalign 0.59 zoom 0.38
            with d2
        elif currentPosition == 4:
            show spyMasturbate:
                xalign 0.46 yalign 0.16 zoom 0.27
            with d2
    if 8 <= randomBackground <= 10:
        if currentPosition == 0:
            show spyMasturbate:
                xalign 0.95 yalign 0.79 zoom 0.75
            with d2
        elif currentPosition == 1:
            show spyMasturbate:
                xalign 0.9 yalign 1.1 zoom 0.67
            with d2
        elif currentPosition == 2:
            show spyMasturbate:
                xalign 0.1 yalign 1.1 zoom 0.65
            with d2
    if 11 <= randomBackground <= 11:
        if currentPosition == 0:
            show spyMasturbate:
                xalign 1.05 ypos 210 zoom 0.94
            with d2
        if currentPosition == 1:
            show spyMasturbate:
                xalign 0.31 yalign 0.9 zoom 0.49
            with d2
        if currentPosition == 2:
            show spyMasturbate:
                xalign 0.85 yalign 0.92 zoom 0.56
            with d2
        if currentPosition == 3:
            show spyMasturbate:
                xalign 0.26 yalign 0.67 zoom 0.5
            with d2
        if currentPosition == 4:
            show spyMasturbate:
                xalign 0.71 yalign 0.91 zoom 0.57
            with d2
    if 12 <= randomBackground <= 12:
        show spyMasturbate:
            xalign 0.34 yalign 0.87 zoom 0.33
        with d2
    return

label useVIB2:
    $ vibActive = False
    play sound "audio/sfx/continue.mp3"

    hide spyMasturbate
    if 1 <= randomBackground <= 3:
        if currentPosition == 0:
            hide spyMasturbate
            with d2
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            with d2
        elif currentPosition == 1:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign -0.03 yalign 0.81 zoom 0.405
            with d2
        elif currentPosition == 2:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign 0.93 yalign 1.3 rotate 12 zoom 0.42 xzoom -1
            with d2
    if 4 <= randomBackground <= 7:
        if currentPosition == 0:
            hide spyMasturbate
            with d2
            show spyCornerSide:
                xalign 0.97 yalign 0.90 zoom 0.39
            with d2
        elif currentPosition == 1:
            hide spyMasturbate
            with d2
            show spyCornerSide:
                xalign 0.87 yalign 0.90 zoom 0.39
            with d2
        elif currentPosition == 2:
            hide spyMasturbate
            with d2
            show spyCrouchingSide:
                xalign 0.72 yalign 0.986 zoom 0.27 rotate 5 xzoom -1
            with d2
        elif currentPosition == 3:
            hide spyMasturbate
            with d2
            show spyCornerSide:
                xalign 0.497 yalign 0.59 zoom 0.37 xzoom -1
            with d2
        elif currentPosition == 4:
            hide spyMasturbate
            with d2
            show spyCornerSide:
                xalign 0.46 yalign 0.16 zoom 0.27
            with d2
    if 8 <= randomBackground <= 10:
        if currentPosition == 0:
            hide spyMasturbate
            with d2
            show spyCorner:
                xalign 0.99 yalign 0.83 zoom 0.78
            with d2
        elif currentPosition == 1:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign 1.0 yalign 1.4 rotate 0.6 zoom 0.48 xzoom -1
            with d2
        elif currentPosition == 2:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign -0.1 yalign 1.5 rotate -3 zoom 0.52
            with d2
    if 11 <= randomBackground <= 11:
        if currentPosition == 0:
            hide spyMasturbate
            with d2
            show spyCorner:
                xalign 1.15 ypos 200
            with d2
        if currentPosition == 1:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign 0.2 yalign 1.1 rotate -5 zoom 0.39
            with d2
        if currentPosition == 2:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign 0.96 yalign 1.1 rotate 5 zoom 0.39 xzoom -1
            with d2
        if currentPosition == 3:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign 0.23 yalign 0.84 rotate -5 zoom 0.38
            with d2
        if currentPosition == 4:
            hide spyMasturbate
            with d2
            show spyCrouchCorner:
                xalign 0.76 yalign 1.03 rotate 5 zoom 0.4 xzoom -1
            with d2
    if 12 <= randomBackground <= 12:
        if currentPosition == 0:
            hide spyMasturbate
            with d2
            show spyCrouchingSide:
                xalign 0.28 yalign 0.88 zoom 0.22 rotate -2
            with d2

    show screen gadgetMenu
    if chanceOfControl >= 90:
        "Nanobot control still active! Keep using your VIB or the spy will run."

        $ renpy.pause(2.0, hard='True')

        hide spyCrouchCorner
        hide spyCrouchingSide
        hide spyCorner
        hide spyCornerSide
        with d3
        "Your spy was controlled and ran away!"
        $ chanceOfControl = 0
        call spyHitBackup from _call_spyHitBackup_10
        call screen interactScreen
    jump jumpStartScene


default target1LoveActive = False
default target2LoveActive = False
default target3LoveActive = False
default target4LoveActive = False

default target1PoisonActive = False
default target2PoisonActive = False
default target3PoisonActive = False
default target4PoisonActive = False

label agentInteractGun:
    hide spyCorner
    hide spyCornerSide
    hide spyCrouchCorner
    hide spyCrouchingSide
    with d2

    if 1 <= randomBackground <= 3 and currentPosition == 0:
        show spyShootBackNormal:
            xalign 0.75 yalign 0.9 zoom 0.77 xzoom -1
        with d2
        pause 0.3

        if combatTarget == 1:
            hide obst1
            show agentGuard:
                xalign 0.383 yalign 0.47 zoom 0.45 xzoom -1
            with d2
            pause 1.0
            hide agentGuard
            $ obst1FoV = 1
            $ CoS1 += 5
            show obst1:
                xalign 0.325 yalign 0.43 rotate 2 zoom 0.48 xzoom -1
            with d3

            if gunReadyFire == 1:
                $ target1LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.386 yalign 0.21 zoom 0.6
            if gunReadyFire == 2:
                $ target1PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.386 yalign 0.21 zoom 0.6



        hide spyShootBackNormal with d3
        show spyCorner:
            xalign 0.90 yalign 0.83 zoom 0.78


    if 1 <= randomBackground <= 3 and currentPosition == 1:
        show spyShootBackNormal:
            xalign 0.05 yalign 0.8 zoom 0.57 rotate 6
        with d2
        pause 0.3
        if combatTarget == 2:
            hide obst2
            show agentGuard:
                xalign 0.61 yalign 0.8 zoom 0.43
            with d2
            pause 1.0
            hide agentGuard
            $ obst2FoV = 1
            $ CoS2 += 5
            show obst2:
                xalign 0.63 yalign 0.78 zoom 0.45
            with d3

            if gunReadyFire == 1:
                $ target2LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.61 yalign 0.4 zoom 0.4
            if gunReadyFire == 2:
                $ target2PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.61 yalign 0.4 zoom 0.4

        hide spyShootBackNormal with d3
        show spyCrouchCorner:
            xalign -0.07 yalign 0.83 zoom 0.39 rotate 5


    if 4 <= randomBackground <= 7 and currentPosition == 0:
        show spyShootSideNormal:
            xalign 0.95 yalign 0.93 zoom 0.41 xzoom -1
        with d2
        pause 0.3

        if combatTarget == 1:
            hide obst1
            show agentGuard:
                xalign 0.64 yalign 0.99 zoom 0.48 xzoom -1
            with d2
            pause 1.0
            hide agentGuard
            $ obst1FoV = 0
            $ CoS1 += 5
            show obst1:
                xalign 0.64 yalign 0.99 zoom 0.48 xzoom -1
            with d3

            if gunReadyFire == 1:
                $ target1LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.64 yalign 0.48 zoom 0.48
            if gunReadyFire == 2:
                $ target1PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.64 yalign 0.48 zoom 0.48
        hide spyShootSideNormal with d3
        show spyCornerSide:
            xalign 0.98 yalign 0.90 zoom 0.39
    if 4 <= randomBackground <= 7 and currentPosition == 1:
        show spyShootSideNormal:
            xalign 0.95 yalign 0.93 zoom 0.39 xzoom -1
        with d2
        pause 0.3

        if combatTarget == 2:
            hide obst2
            show agentGuard:
                xalign 0.01 yalign 0.99 zoom 0.46 xzoom -1
            with d2
            pause 1.0
            hide agentGuard
            $ obst2FoV = 1
            $ CoS2 += 5
            show obst2:
                xalign 0.04 yalign 0.99 zoom 0.48 xzoom -1
            with d3

            if gunReadyFire == 1:
                $ target2LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.09 yalign 0.5 zoom 0.48
            if gunReadyFire == 2:
                $ target2PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.09 yalign 0.5 zoom 0.48
        hide spyShootSideNormal with d3
        show spyCornerSide:
            xalign 0.88 yalign 0.90 zoom 0.39
    if 4 <= randomBackground <= 7 and currentPosition == 3:
        show spyShootSideNormal:
            xalign 0.495 yalign 0.63 zoom 0.37 rotate 3
        with d2
        pause 0.3

        if combatTarget == 3:
            hide obst3
            show agentGuard:
                xalign 0.82 yalign 0.61 zoom 0.42 rotate -5
            with d2
            pause 1.0
            hide agentGuard
            $ obst3FoV = 1
            $ CoS3 += 5
            show obst3:
                xalign 0.79 yalign 0.58 zoom 0.43
            with d3

            if gunReadyFire == 1:
                $ target3LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.76 yalign 0.3 zoom 0.45
            if gunReadyFire == 2:
                $ target2PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.76 yalign 0.3 zoom 0.45
        hide spyShootSideNormal with d3
        show spyCornerSide:
            xalign 0.495 yalign 0.59 zoom 0.37 xzoom -1
    if 4 <= randomBackground <= 7 and currentPosition == 4:
        show spyShootSideNormal:
            xalign 0.45 yalign 0.15 zoom 0.27 xzoom -1 rotate -3
        with d2
        pause 0.3

        if combatTarget == 4:
            hide obst4
            show agentGuard:
                xalign 0.08 yalign 0.15 zoom 0.29 xzoom -1 rotate 5
            with d2
            pause 1.0
            hide agentGuard
            $ obst4FoV = 1
            $ CoS4 += 5
            show obst4:
                xalign 0.1 yalign 0.12 zoom 0.31 xzoom -1
            with d3

            if gunReadyFire == 1:
                $ target4LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.1 yalign 0.05 zoom 0.46
            if gunReadyFire == 2:
                $ target2PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.1 yalign 0.05 zoom 0.46
        hide spyShootSideNormal with d3
        show spyCornerSide:
            xalign 0.46 yalign 0.16 zoom 0.27


    if 8 <= randomBackground <= 10 and currentPosition == 0:
        show spyShootBackNormal:
            xalign 0.85 yalign 0.9 zoom 0.77 xzoom -1
        with d2
        pause 0.3

        if combatTarget == 1:
            hide obst1
            show agentGuard:
                xalign 0.53 yalign 0.53 rotate 2 zoom 0.43 xzoom -1
            with d2
            pause 1.0
            hide agentGuard
            $ obst1FoV = 0
            $ CoS1 += 5
            show obst1:
                xalign 0.53 yalign 0.5 zoom 0.47 xzoom -1
            with d3

            if gunReadyFire == 1:
                $ target1LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.54 yalign 0.23 zoom 0.6
            if gunReadyFire == 2:
                $ target1PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.54 yalign 0.23 zoom 0.6

        hide spyShootBackNormal with d3
        show spyCorner:
            xalign 0.99 yalign 0.83 zoom 0.78


    if 8 <= randomBackground <= 10 and currentPosition == 2:
        show spyShootBackNormal:
            xalign 0.06 yalign 1.2 zoom 0.7
        with d2
        pause 0.3
        if combatTarget == 3:
            hide obst3
            show agentGuard:
                xalign 0.51 yalign 0.66 zoom 0.58
            with d2
            pause 1.0
            hide agentGuard
            $ obst3FoV = 1
            $ CoS2 += 5
            show obst3:
                xalign 0.5 yalign 0.62 zoom 0.65
            with d3

            if gunReadyFire == 1:
                $ target3LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.5 yalign 0.2 zoom 0.6
            if gunReadyFire == 2:
                $ target3PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.5 yalign 0.2 zoom 0.6

        hide spyShootBackNormal with d3
        show spyCrouchCorner:
            xalign -0.03 yalign 1.22 zoom 0.53


    if 11 <= randomBackground <= 11 and currentPosition == 0:
        show spyShootBackNormal:
            xalign 0.9 yalign 2.2 zoom 0.87 xzoom -1
        with d2
        pause 0.3
        if combatTarget == 1:
            hide obst1
            show agentGuard:
                xalign 0.383 yalign 1.1 zoom 0.72 xzoom -1
            with d2
            pause 1.0
            hide agentGuard
            $ obst1FoV = 2
            $ CoS1 += 5
            show obst1:
                xalign 0.4 yalign 1.1 zoom 0.7 xzoom -1
            with d3

            if gunReadyFire == 1:
                $ target1LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.45 yalign 0.27 zoom 0.8
            if gunReadyFire == 2:
                $ target1PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.45 yalign 0.27 zoom 0.8

        hide spyShootBackNormal with d3
        call return2Pos from _call_return2Pos_17


    if 11 <= randomBackground <= 11 and currentPosition == 2:
        show spyShootBackUp:
            xalign 0.82 yalign 0.9 zoom 0.55 xzoom -1
        with d2
        pause 0.3
        if combatTarget == 2:
            hide obst2
            show agentGuard:
                xalign 0.54 yalign 0.7 rotate 2 zoom 0.47 xzoom -1
            with d2
            pause 1.0
            hide agentGuard
            $ obst2FoV = 2
            $ CoS2 += 5
            show obst2:
                xalign 0.53 yalign 0.66 zoom 0.48 xzoom -1
            with d3

            if gunReadyFire == 1:
                $ target3LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.54 yalign 0.3 zoom 0.6
            if gunReadyFire == 2:
                $ target3PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.54 yalign 0.3 zoom 0.6

        hide spyShootBackUp with d3
        call return2Pos from _call_return2Pos_16

    if 11 <= randomBackground <= 11 and currentPosition == 3:
        show spyShootBackUp:
            xalign 0.27 yalign 0.78 zoom 0.57
        with d2
        pause 0.3
        if combatTarget == 3:
            hide obst3
            show agentGuard:
                xalign 0.64 yalign 0.35 rotate -2 zoom 0.38
            with d2
            pause 1.0
            hide agentGuard
            $ obst3FoV = 2
            $ CoS3 += 5
            show obst3:
                xalign 0.66 yalign 0.3 rotate 2 zoom 0.41
            with d3

            if gunReadyFire == 1:
                $ target3LoveActive = True
                $ gunReadyFire = 0
                show loveEffect:
                    xalign 0.62 yalign 0.15 zoom 0.6
            if gunReadyFire == 2:
                $ target3PoisonActive = True
                $ gunReadyFire = 0
                show flashEffect:
                    xalign 0.62 yalign 0.15 zoom 0.6

        hide spyShootBackUp with d3
        call return2Pos from _call_return2Pos_18

    jump jumpStartScene

label return2Pos:
    if 1 <= randomBackground <= 3:
        if currentPosition == 0:
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
        if currentPosition == 1:
            show spyCrouchCorner:
                xalign -0.03 yalign 0.81 zoom 0.405
        if currentPosition == 2:
            show spyCrouchCorner:
                xalign 0.93 yalign 1.3 rotate 12 zoom 0.42 xzoom -1
        with d3
    if 4 <= randomBackground <= 7:
        if currentPosition == 0:
            show spyCornerSide:
                xalign 0.97 yalign 0.90 zoom 0.39
        if currentPosition == 1:
            show spyCornerSide:
                xalign 0.88 yalign 0.90 zoom 0.39
        if currentPosition == 2:
            show spyCrouchCorner:
                xalign 0.93 yalign 1.3 rotate 12 zoom 0.42 xzoom -1
        if currentPosition == 3:
            show spyCornerSide:
                xalign 0.49 yalign 0.59 zoom 0.37 xzoom -1
        if currentPosition == 4:
            show spyCornerSide:
                xalign 0.47 yalign 0.16 zoom 0.27
        with d3
    if 8 <= randomBackground <= 10:
        if currentPosition == 0:
            show spyCorner:
                xalign 0.99 yalign 0.83 zoom 0.78
        if currentPosition == 1:
            show spyCrouchCorner:
                xalign -0.03 yalign 0.81 zoom 0.405
        if currentPosition == 2:
            show spyCrouchCorner:
                xalign -0.05 yalign 1.4 rotate -5 zoom 0.48
        with d3
    if 11 <= randomBackground <= 11:
        if currentPosition == 0:
            show spyCorner:
                xalign 1.15 ypos 200
        if currentPosition == 1:
            show spyCrouchCorner:
                xalign -0.03 yalign 0.81 zoom 0.405
        if currentPosition == 2:
            show spyCrouchCorner:
                xalign 0.93 yalign 1.05 rotate 5 zoom 0.37 xzoom -1
        if currentPosition == 3:
            show spyCrouchCorner:
                xalign 0.23 yalign 0.84 rotate -5 zoom 0.38
        if currentPosition == 4:
            show spyCrouchCorner:
                xalign 0.77 yalign 1.08 rotate 5 zoom 0.4 xzoom -1
        with d3
    return

image hookBg4Fx = "mission/fx/hookBg4.png"
image hookBg5Fx = "mission/fx/hookBg5.png"
image hookBg5bFx = "mission/fx/hookBg5b.png"
image hookBg2Fx = "mission/fx/hookBg2.png"
image fxHookgunBg4 = "mission/fx/fxHookgunBg4.png"
image fxHookgunBg5 = "mission/fx/fxHookgunBg5.png"
image fxHookgunBg5b = "mission/fx/fxHookgunBg5b.png"

label hookInteract:
    if 4 <= randomBackground <= 6:
        $ randomObst1 = 0
        hide spyCornerSide with d2
        $ gunStatus = 2
        show spyShootSideUp:
            xalign 0.95 yalign 0.96 zoom 0.44 xzoom -1
        with d2
        pause 0.4
        show hookBg2Fx
        with d1
        play sound "audio/sfx/shoot1.mp3"
        pause 0.1
        hide hookBg2Fx
        hide spyShootSideUp
        $ gunStatus = 0
        with d1
        if missionSetting == "School":
            show globalImage:
                linear 0.35 xalign 0.0 yalign 0.0
        if missionSetting == "Castle":
            show globalImageCastle:
                linear 0.35 xalign 0.0 yalign 0.0
        if missionSetting == "Database":
            show globalImageDatabase:
                linear 0.35 xalign 0.0 yalign 0.0
        if missionSetting == "Faire":
            show globalImageFaire:
                linear 0.35 xalign 0.0 yalign 0.0
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                linear 0.35 xalign 0.0 yalign 0.0
        $ currentPosition = 4
        pause 0.35
        show spyFalling:
            xalign 0.49 yalign -0.4 zoom 0.28 xzoom -1
            linear 0.3 yalign 0.22
        pause 0.3
        hide spyFalling
        show spyCornerSide:
            xalign 0.473 yalign 0.17 zoom 0.28
        with d2
    if randomBackground == 11:
        hide spyCrouchCorner with d2
        show spyShootBackUp:
            xalign 0.25 yalign 0.94 zoom 0.54
        show fxHookgunBg4
        with d2
        play sound "audio/sfx/shoot1.mp3"
        show hookBg4Fx with d1
        pause 0.5
        hide hookBg4Fx
        hide spyShootBackUp
        hide fxHookgunBg4
        with d2
        $ randomCover1 = 0
        if missionSetting == "School":
            show globalImage:
                xalign 0.5 yalign 0.0 zoom 0.5
                linear 0.45 xalign 0.5 yalign 0.123 zoom 1.3
        if missionSetting == "Castle":
            show globalImageCastle:
                xalign 0.5 yalign 0.0 zoom 0.5
                linear 0.45 xalign 0.5 yalign 0.13 zoom 1.5
        if missionSetting == "Database":
            show globalImageDatabase:
                xalign 0.5 yalign 0.0 zoom 0.5
                linear 0.45 xalign 0.5 yalign 0.13 zoom 1.5
        if missionSetting == "Faire":
            show globalImageFaire:
                xalign 0.5 yalign 0.0 zoom 0.5
                linear 0.45 xalign 0.5 yalign 0.13 zoom 1.5
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                xalign 0.5 yalign 0.0 zoom 0.5
                linear 0.45 xalign 0.5 yalign 0.13 zoom 1.5
        $ currentPosition = 5
        pause 0.45
        show spyFalling:
            xalign 0.75 yalign -0.4 zoom 0.51 xzoom -1
            linear 0.3 yalign 1.0
        pause 0.3
        hide spyFalling
        show spyCrouchCorner:
            xalign 0.8 yalign 1.15 rotate 3 zoom 0.45 xzoom -1
        with d2
        jump jumpStartScene

    if randomBackground == 12 and currentPosition == 0:
        hide spyCrouchingSide with d2
        show spyShootSideUp:
            xalign 0.24 yalign 0.88 zoom 0.37 rotate -2
        show fxHookgunBg5
        with d2
        play sound "audio/sfx/shoot1.mp3"
        show hookBg5Fx with d1
        pause 0.5
        hide hookBg5Fx
        hide spyShootSideUp
        hide fxHookgunBg5
        with d2
        $ randomCover1 = 0
        if missionSetting == "School":
            show globalImage:
                linear 0.45 yalign 0.5
        if missionSetting == "Castle":
            show globalImageCastle:
                linear 0.45 yalign 0.5
        if missionSetting == "Database":
            show globalImageDatabase:
                linear 0.45 yalign 0.5
        if missionSetting == "Faire":
            show globalImageFaire:
                linear 0.45 yalign 0.5
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                linear 0.45 yalign 0.5
        $ currentPosition = 1
        pause 0.45
        show spyFalling:
            xalign 0.6 yalign 0.2 zoom 0.3
            linear 0.3 yalign 0.97
        pause 0.3
        hide spyFalling
        show spyCrouchCorner:
            xalign 0.63 yalign 1.08 rotate -3 zoom 0.275
        with d2
        jump jumpStartScene
    if randomBackground == 12 and currentPosition == 1:
        hide spyCrouchCorner with d2
        show spyShootSideUp:
            xalign 0.67 yalign 1.05 zoom 0.35 rotate 2 xzoom -1
        show fxHookgunBg5b
        with d2
        play sound "audio/sfx/shoot1.mp3"
        show hookBg5bFx with d1
        pause 0.5
        hide hookBg5bFx
        hide spyShootSideUp
        hide fxHookgunBg5b
        with d2
        $ randomCover1 = 0
        if missionSetting == "School":
            show globalImage:
                linear 0.45 yalign 0.0
        if missionSetting == "Castle":
            show globalImageCastle:
                linear 0.45 yalign 0.0
        if missionSetting == "Database":
            show globalImageDatabase:
                linear 0.45 yalign 0.0
        if missionSetting == "Faire":
            show globalImageFaire:
                linear 0.45 yalign 0.0
        if missionSetting == "WOOHP":
            show globalImageWOOHP:
                linear 0.45 yalign 0.0
        $ currentPosition = 2
        pause 0.45
        show bonusLootBG5:
            xalign 0.41 yalign 0.98 zoom 0.31
        show spyFalling:
            xalign 0.4 yalign 0.2 zoom 0.3
            linear 0.3 yalign 0.97
        pause 0.3
        hide spyFalling
        show spyCrouchCorner:
            xalign 0.43 yalign 1.08 rotate 3 zoom 0.275 xzoom -1
        with d2
        hide bonusLootBG5
        play sound "audio/sfx/jobReward.mp3"
        $ bonusAvailable = 0
        $ loot1 += 1
        $ loot5 += 1
        show dropMats at item_drop((450,620))
        pause 0.25
        play sound "audio/sfx/jobReward.mp3"
        show dropConsum at item_drop((450,620))
        jump jumpStartScene

label lootItem:
    play sound "audio/sfx/loot1.mp3"
    if randomLoot == 1:
        $ loot6 += 1
    elif randomLoot == 2:
        $ loot4 += 1
    $ randomLoot = 0
    call missionLootText from _call_missionLootText
    jump jumpStartScene


label missionLootText:
    if 1 <= randomBackground <= 3 and currentPosition == 1:
        show text "{size=+5}{font=fonts/freshmarker.ttf}Gotcha!{/font}{/size}" at jobReward:
            xalign 0.14 yalign 0.42
            linear 0.35 yalign 0.36
    if 1 <= randomBackground <= 3 and currentPosition == 2:
        show text "{size=+5}{font=fonts/freshmarker.ttf}Mine!{/font}{/size}" at jobReward:
            xalign 0.82 yalign 0.67
            linear 0.35 yalign 0.59
    if 4 <= randomBackground <= 7 and currentPosition == 2:
        show text "{size=+5}{font=fonts/freshmarker.ttf}Ka-ching!{/font}{/size}" at jobReward:
            xalign 0.56 yalign 0.8
            linear 0.35 yalign 0.75
    if 8 <= randomBackground <= 10 and currentPosition == 1:
        show text "{size=+5}{font=fonts/freshmarker.ttf}Loot!{/font}{/size}" at jobReward:
            xalign 0.83 yalign 0.55
            linear 0.35 yalign 0.47
    with d3
    hide text with d3
return

label lootSpecial:
    if task13Stage == 2.1:
        play sound "audio/sfx/itemGot.mp3"
        "Inside the locker you find {color=#ffeda6}Sam's notes{/color}."
        sM "We got the notes!"
        menu:
            "Pull out now" if True:
                jump missionComplete
            "Continue the mission" if True:
                sM "Roger!"
                jump jumpStartScene



layeredimage inter1Bg1:
    if missionSetting == "Castle":
        "mission/castle/interactable/chandelier.png"
    if missionSetting == "WOOHP":
        "mission/WOOHP/interactable/chandelier.png"
layeredimage inter1Bg2:
    if missionSetting == "School":
        "mission/school/interactable/light1.png"
    if missionSetting == "Castle":
        "mission/castle/interactable/chandelier2.png"
    if missionSetting == "Database":
        "musicBall1"
    if missionSetting == "WOOHP":
        "mission/WOOHP/interactable/chandelier2.png"
layeredimage inter1Bg3:
    if missionSetting == "Castle":
        "mission/castle/interactable/chandelier3.png"
    if missionSetting == "WOOHP":
        "mission/WOOHP/interactable/chandelier3.png"

label spyShootHigh:
    $ gunStatus = 1
    if 1 <= randomBackground <= 3:
        hide spyCorner
        show spyShootBackUp:
            xalign 1.0 yalign 0.9 zoom 0.766 rotate 7 xzoom -1
        with d2
        pause 0.3
        play sound "audio/sfx/shoot1.mp3"
        pause 0.3
        if interSelect == 1:
            $ interact1 = 0
            show inter1Bg1:
                xalign 0.61 yalign 0.0 zoom 0.25
                linear 0.1 xalign 0.615
                linear 0.1 xalign 0.61
                linear 0.1 xalign 0.615
                linear 0.1 xalign 0.61
                pause 0.53
                linear 0.2 yalign 0.5
            pause 1.0
            if randomObst2 == 1:
                show agentHitObject:
                    xalign 0.6 yalign 0.5 zoom 0.28
                play sound "audio/sfx/defeatEnemy.mp3"
            $ randomObst2 = 0
            hide obst2
            hide inter1Bg1
            with d1
            hide agentHitObject with d2
            pause 0.2
            hide spyShootBackUp
            show spyCorner:
                xalign 0.90 yalign 0.83 zoom 0.78
            $ gunStatus = 0
            with d3

    if 4 <= randomBackground <= 7:
        if gadgetGunActive == True:
            $ gunStatus = 1
            hide spyCornerSide
            with d2
            show spyShootSideUp:
                xalign 0.53 yalign 0.6 zoom 0.4
        with d2
        pause 0.3
        play sound "audio/sfx/shoot1.mp3"
        pause 0.3
        if interSelect == 1 or interSelect == 3:
            $ interact1 = 0
            $ interact2 = 0
            $ interact3 = 0
            show inter1Bg2:
                xalign 0.75 yalign 0.0 zoom 0.35
                linear 0.1 xalign 0.77
                linear 0.1 xalign 0.75
                linear 0.1 xalign 0.77
                linear 0.1 xalign 0.75
                pause 0.53
                linear 0.2 yalign 0.5
            pause 1.11
            if randomObst3 >= 1:
                show agentHit:
                    xalign 0.755 yalign 0.58 zoom 0.4
                play sound "audio/sfx/defeatEnemy.mp3"
            hide inter1Bg2
            hide obst3
            $ randomObst3 = 0
            pause 0.3
            hide agentHit
            with d1
            hide spyShootSideUp
            $ lootLoc = 3
            call randomLoot from _call_randomLoot_6
            show spyCornerSide:
                xalign 0.497 yalign 0.59 zoom 0.37 xzoom -1
            $ gunStatus = 0
            with d2
            jump jumpStartScene
        elif True:
            "It looks like this can be shot down with the appropriate gadget."
            jump jumpStartScene

    if 8 <= randomBackground <= 10:
        hide spyCorner
        show spyShootBackUp:
            xalign 1.14 yalign 0.98 zoom 0.76 rotate 3 xzoom -1
        with d2
        pause 0.3
        play sound "audio/sfx/shoot1.mp3"
        pause 0.3
        if interSelect == 1:
            $ interact1 = 0
            show inter1Bg3:
                xalign 0.51 yalign -0.02 zoom 0.23
                linear 0.1 xalign 0.515
                linear 0.1 xalign 0.51
                linear 0.1 xalign 0.515
                linear 0.1 xalign 0.51
                pause 0.53
                linear 0.2 yalign 0.5
            pause 0.5
            if randomObst1 == 1:
                $ obst1FoV = 3
                hide obst1
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
            pause 0.5
            if randomObst3 == 1:
                show agentHitObject:
                    xalign 0.5 yalign 0.4 zoom 0.28
                hide obst1
            if randomObst1 == 1:
                $ CoS1 += 2
                show obst1:
                    xalign 0.535 yalign 0.50 zoom 0.49
            play sound "audio/sfx/defeatEnemy.mp3"
            $ randomObst3 = 0
            hide obst3
            hide inter1Bg3
            with d1
            hide agentHitObject with d2
            pause 0.2
            hide spyShootBackUp
            show spyCorner:
                xalign 1.0 yalign 0.83 zoom 0.79
            $ gunStatus = 0
            with d3
    return

"Mission.rpy - An error has occurred. Please report this to Exiscoming."
jump jumpStartScene
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
