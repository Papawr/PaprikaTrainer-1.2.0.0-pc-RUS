

$ _skipping = False






define woohp = "WOOHP"


define tutorialActive = True

define tutlift = False
define tutquarters = False
define tutCreditCard = False
define tutmissions = False
define tutprison = False
define tutspyCamera = False
define tutdesk = False
default menuTutActive = True
default landgrabTut2 = True





image bgWOOHP = "bgs/bgWOOHP.jpg"
image bgWOOHP2 = "bgs/bgWOOHP2.jpg"
image bgBase = "bgs/base/base.jpg"
image bgBaseHalloween = "bgs/base/baseHalloween.jpg"
image bgBaseChristmas = "bgs/base/baseChristmas.jpg"
image bgPrison = "bgs/bgPrison.jpg"
image bgOffice = "bgs/bgOffice.jpg"
image bgMall = "bgs/bgMall.jpg"
image bgSchool1 = "bgs/bgSchool1.jpg"
image bgStreet1 = "bgs/streetview1.jpg"
image bgStreet2 = "bgs/streetview2.jpg"
image bgStreet3 = "bgs/streetview3.jpg"
image bgStreet4 = "bgs/streetview4.jpg"
image bgStreet5 = "bgs/streetview5.jpg"
image bgCastle = "bgs/bgCastle.jpg"
image black = "bgs/black.jpg"
image bgMap = "bgs/bgMap.jpg"
image bgMapNight = "bgs/bgMapNight.jpg"
image bgMapRaid = "bgs/bgMapRaid.jpg"
image bgShowersSchool = "bgs/bgShowersSchool.jpg"
image bgLibrarySchool = "bgs/bgLibrarySchool.jpg"
image bgCafeteriaSchool = "bgs/bgCafeteriaSchool.jpg"



image bgGang = "gui/gangScreen.jpg"
image bgClub = "bgs/bgClub.jpg"
image bgClub0 = "bgs/bgClub0.jpg"
image bgClub1 = "bgs/bgClub1.jpg"
image bgStatic = "bgs/bgStatic1.jpg"
image bgWardrobe = "bgs/wardrobeBlue.jpg"
image bgItems = "gui/itemUI/items/bgItems.jpg"
image bgShops = "bgs/shopRed.jpg"
image bgPhotos = "gui/photos/bgPhoto.jpg"
image bgStatus = "gui/status.jpg"
image bgXmas = "bgs/xmas.jpg"
image bgLore = "bgs/bgLore.jpg"

image bgDatabase = "bgs/bgDatabase.jpg"
image bgSmoothie = "bgs/bgSmoothie.jpg"
image bgTrip1 = "bgs/bgTrip1.jpg"
image bgTrip2 = "bgs/bgTrip2.jpg"
image bgTrip3 = "bgs/bgTrip3.jpg"
image bgInjector = "bgs/bgInjector.jpg"
image bgFashion = "bgs/bgFashion.jpg"
image bgIntel = "bgs/bgIntel.jpg"
image bgBarAces = "bgs/bar/stageAces.jpg"
image bgNight = "bgs/bgNight.png"
image bgStrip = "animations/strip/bgStrip.jpg"
image bgNanoTut = "bgs/bgNanoTut.jpg"
image bgNanoTut2 = "bgs/bgNanoTut2.jpg"
image bgMenuTut = "bgs/bgMenuTut.jpg"
image bgBookstore = "bgs/bgBookstore.jpg"
image bgSamCell = "bgs/bgSamCell.jpg"
image bgAudioroom = "bgs/bgAudioroom.jpg"
image skipLandgrabTut = "bgs/skipLandgrabTut.jpg"
image orderOfCaptureTut = "bgs/orderOfCaptureTut.jpg"
image bgFaire = "bgs/bgFaire.jpg"
image bgEngineer = "bgs/bgEngineer.jpg"
image bgPropaganda = "bgs/bgPropaganda.jpg"
image bgGunshot = "bgs/gunshot.jpg"
image bgSky = "bgs/bgSky.jpg"
image bgBasement = "bgs/bgBasement.jpg"

image bgFinale1 = "bgs/finale1.jpg"
image bgFinale2 = "bgs/finale2.jpg"
image bgFinale3 = "bgs/finale3.jpg"
image bgFinale4 = "bgs/finale4.jpg"
image bgFinale5 = "bgs/finale5.jpg"
image bgFinale6 = "bgs/finale6.jpg"
image bgFinale7 = "bgs/finale7.jpg"
image bgFinale8 = "bgs/finale8.jpg"
image bgFinale9 = "bgs/finale9.jpg"
image bgFinale10 = "bgs/finale10.jpg"

layeredimage bgEnding1:
    always:
        "bgs/bgEnding1.jpg"
    if socialSilva >= 12:
        "bgs/bgEndingSilva.png"
    if task30Stage >= 3:
        "bgs/bgEndingKim.png"
image bgEnding2 = "bgs/bgEnding2.jpg"

screen debriefCont:
    vbox xpos 0.43 ypos 590:
        imagebutton:
            idle "gui/debrief/continue.png"
            hover "gui/debrief/continue-hover.png"
            action Play("sound", "audio/sfx/continue.mp3"), Return()

screen tutHole:
    if holeinwall == 1:
        add "bgs/base/tutHole1.png"
    if holeinwall == 1:
        add "bgs/base/tutHole2.png"


image bgSideroom = "bgs/base/sideroom.jpg"

image missionScreenBG = "bgs/missionScreenBG.jpg"

image white = "gui/white.jpg"
image redScr = "gui/red.png"




define quickflash = Fade(0.1, 0.0, 0.2, color='#fff')
define flashbulb = Fade(0.2, 0.0, 0.4, color='#fff')
define flash = Fade(0.2, 0.5, 0.8, color='#fff')
define bloodbulb = Fade(0.1, 0.0, 0.4, color='#DF0101')
define qFade = Fade(0.02, 0.1, 0.25, color='#000000')
define wFade = Fade(0.02, 0.1, 0.05, color='#000000')
define medFade = Fade(0.1, 0.1, 2.0, color='#000000')
define longFade = Fade(0.8, 1.0, 1.5, color='#000000')
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d10 = Dissolve(1.0)
define quick_menu = False
image likelikelike = "gui/likelike.png"
image landgrabFX = "gui/landgrabFX.png"

image disco:
    "bgs/disco1.png"
    pause 0.8
    "bgs/disco2.png"
    pause 0.8
    "bgs/disco3.png"
    pause 0.8
    repeat

image audioroom:
    "bgs/audioroom1.png"
    pause 0.5
    "bgs/audioroom2.png"
    pause 0.5
    "bgs/audioroom3.png"
    pause 0.5
    "bgs/audioroom4.png"
    pause 0.5
    repeat

label threatNeutralized:
    play sound "audio/sfx/tension1.mp3"
    show threatNeutralized:
        xalign 0.5 yalign 0.4
    with d5
    $ renpy.pause(1.5, hard='True')
    hide threatNeutralized
    with d5
    pause 0.3
    return

transform disbanded:
    linear 0.15 zoom 0.9


image bgControl = "bgs/bgControl.png"

image warzoneFilter = "gui/warzoneFilter.png"

image qAccept = "gui/taskAccept.png"
image qUpdated = "gui/taskUpdated.png"
image qCompleted = "gui/taskCompleted.png"
image qCompleted2 = "gui/taskCompleted2.png"

image threatNeutralized = "gui/threatNeutralized.png"

image bossTarget1 = "gui/bossTarget1.png"

label qAccept:
    play sound "audio/sfx/qAccept.mp3"
    show qAccept:
        xalign 0.5 yalign 0.5
    with d1
    $ renpy.pause(1.5, hard='True')
    hide qAccept
    with d10
    return

label qUpdated:
    play sound "audio/sfx/qAccept.mp3"
    show qUpdated:
        xalign 0.5 yalign 0.5
    with d1
    $ renpy.pause(1.5, hard='True')
    hide qUpdated
    with d10
    return

label qCompleted:
    play sound "audio/sfx/qComplete.mp3"
    show qCompleted:
        xalign 0.5 yalign 0.5
    with d1
    $ renpy.pause(1.2, hard='True')
    hide qCompleted
    show qCompleted2:
        xalign 0.5 yalign 0.5
    $ renpy.pause(1.3, hard='True')
    hide qCompleted2
    with d10
    return

image scene_darkening = "gui/sceneDarkening.png"
image scene_camera = "gui/sceneCamera.png"
image scene_fighting = "gui/sceneFighting.png"

image scene_static1 = "gui/static1.png"
image scene_static2 = "gui/static2.png"
image scene_static3:
    "gui/static3.png"
    pause 0.1
    "gui/static4.png"
    pause 0.1
    "gui/static5.png"
    pause 0.1
    repeat

image drama1 = "gui/drama1.png"
image drama2 = "gui/drama2.png"
image drama3 = "gui/drama3.png"

image dramaJerry = "models/jerry/dramaJerry.png"


image intel = "gui/intel.png"
image moodHapSam = "gui/moodHapSam.png"
image moodSadSam = "gui/moodSadSam.png"
default moodDirection = 0

transform moodEff:
    yalign 0.2
    linear 0.3 yalign 0.1

label moodHap:
    if moodDirection == 1:
        show moodHapSam at moodEff:
            xalign 0.8
        with d3
        hide moodHapSam at moodEff
        with d3
    if moodDirection == 2:
        show moodHapSam at moodEff:
            xalign 0.2
        with d3
        hide moodHapSam at moodEff
        with d3
    if moodDirection == 3:
        show moodHapSam at moodEff:
            xalign 0.5
        with d3
        hide moodHapSam at moodEff
        with d3
    return

label moodSad:
    if moodDirection == 1:
        show moodSadSam at moodEff:
            xalign 0.8
        with d3
        hide moodSadSam
        with d3
    if moodDirection == 2:
        show moodSadSam at moodEff:
            xalign 0.2
        with d3
        hide moodSadSam
        with d3
    if moodDirection == 3:
        show moodSadSam at moodEff:
            xalign 0.5
        with d3
        hide moodSadSam
        with d3
    return

label intelGain:
    if moodDirection == 1:
        show intel at moodEff:
            xalign 0.8
        with d3
        hide intel at moodEff
        with d3
    if moodDirection == 2:
        show intel at moodEff:
            xalign 0.2
        with d3
        hide intel at moodEff
        with d3
    if moodDirection == 3:
        show intel at moodEff:
            xalign 0.5
        with d3
        hide intel at moodEff
        with d3
    return

transform jobReward:
    yalign 0.2
    linear 0.3 yalign 0.1

label missionRewardInt:
    play sound "audio/sfx/jobReward.mp3"
    show text "Gained [randIntel] INT" at jobReward:
        xalign 0.99
    with d2
    hide text
    with d5
return

label missionRewardMoney:
    play sound "audio/sfx/jobReward.mp3"
    show text "Gained $[randMoney]" at jobReward:
        xalign 0.99
    with d2
    hide text
    with d5
return

label missionRewardLore:
    play sound "audio/sfx/jobReward.mp3"
    show text "Lore gathered" at jobReward:
        xalign 0.99
    with d2
    hide text
    with d5
return

label missionRewardRep:
    play sound "audio/sfx/jobReward.mp3"
    show text "Rep gained" at jobReward:
        xalign 0.99
    with d2
    hide text
    with d5
return

label missionRewardItem:
    play sound "audio/sfx/jobReward.mp3"
    show text "Item(s) gained" at jobReward:
        xalign 0.99
    with d2
    hide text
    with d5
return

label missionRewardCrew:
    play sound "audio/sfx/jobReward.mp3"
    show text "Crew gained" at jobReward:
        xalign 0.99
    with d2
    hide text
    with d5
return

label newPhoto:
    play sound "audio/sfx/camera.mp3"
    pause 0.5
    play sound "audio/sfx/jobReward.mp3"
    show text "Quest photo added" at jobReward:
        xalign 0.99
    with d2
    pause 1.0
    hide text
    with d5
return





default photoMaggie = False
default photoClaus = False
default photoClerk = False





default agentCombatUpgrade = 0
default combatTarget = 0
default spy1Status = 0
default spy2Status = 0
default spy3Status = 0
default spy4Status = 0
default spy5Status = -1
default spy6Status = -1
default spy0Status = 0

default greenDayJob = 0
default redDayJob = 0
default yellowDayJob = 0






default dlc1Active = True
default dlc2Active = False
default dlc3Active = False
default dlc4Active = False




default daysPlayed = 0
default cash = 0
default intel = 100
default traitorRandom = 0
default clubStage = 0
default tod = 1
default crew = 0
default landgrabTimer = 0
default hackerUnlocked = False
default mathVisit = False
default randRandsom = 0
default coverCounter = 100
default coverStatus = "INCOGNITO"
default emergencyCrimeSpree = 0
default playerMilkshakeLvl = 0
default playerMilkshakeExp = 0
default playerMilkshake = False
default otActive = False
default exoticMilk = 0

default missionAreaAchiev = False
default sexAchiev = False
default month1Achiev = False
default orangeAchiev = False
default xmasAchiev = False
default tentacleAchiev = False
default moneyAchiev = False
default brewAchiev = False
default woohpHQAchiev = False





default acesBounty1 = 0
default acesBounty2 = 0
default acesBounty3 = 0



default samSpySex = 0
default cloverSpySex = 0
default alexSpySex = 0




default freedAgents = 1
default capturedAgents = 0

default landgrabRandomAssist1 = 0
default landgrabRandomAssist2 = 0
default landgrabRandomAssist3 = 0

default resourceFood = 0
default resourceWater = 0
default resourceToys = 0
default resourceClothes = 0
default resourceTools = 0

default donateReward = 0

default supplycrateOpen = False

layeredimage supplycrate:
    if supplycrateOpen:
        "gui/supplycrateOpen.png"
    else:
        "gui/supplycrateClose.png"

screen supplyCrate:
    vbox xalign 0.4 yalign 0.75:
        imagebutton:
            idle "gui/open.png"
            hover "gui/open-hover.png"
            action SetVariable("supplycrateOpen", True), Jump("exploreLoot")




default magazine = 0
default medkit = 0
default itemsScreen = 0
default smoothieCoupon = 0
default injectorSmall = 0
default injectorMedium = 0
default injectorLarge = 0

default herbHeal = 0
default herbAphro = 0
default herbWeed = 0
default herbMutant = 0
default herbGold = 0
default herbWhisper = 0
default herbRebel = 0

default medPills = 0
default medPotion = 0


default acesRep = 0
default acesRank = 1

default punkRep = 0
default punkRank = 1

default outsideRep = 0
default outsideRank = 1

default epinesRep = 0
default huntRep = 0
default glimRep = 0
default exchRep = 0

default mallActive = False
default beachActive = False
default firstPick = 0





default treatBag = 0


default xmasAnnouchment = True
default buyXmasOut = 0

screen xmasOutfitShop:

    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("mall")
    if top14Alex == False:
        vbox xalign 0.2 yalign 0.2:
            imagebutton:
                idle "gui/itemUI/xmas/yellowDummy.png"
                hover "gui/itemUI/xmas/yellowDummy-hover.png" tooltip " "
                action SetVariable("buyXmasOut", 1), Jump("buyXmasOutfit")
    if top14Sam == False:
        vbox xalign 0.5 yalign 0.2:
            imagebutton:
                idle "gui/itemUI/xmas/greenDummy.png"
                hover "gui/itemUI/xmas/greenDummy-hover.png" tooltip " "
                action SetVariable("buyXmasOut", 2), Jump("buyXmasOutfit")
    if top14Clover == False:
        vbox xalign 0.8 yalign 0.2:
            imagebutton:
                idle "gui/itemUI/xmas/redDummy.png"
                hover "gui/itemUI/xmas/redDummy-hover.png" tooltip " "
                action SetVariable("buyXmasOut", 3), Jump("buyXmasOutfit")







define spyGreenActive = False
define spyRedActive = False
define spyYellowActive = False
define spyKimActive = False

screen spyScreens:
    if spyGreenActive == True:
        vbox xpos 590 ypos 85:
            imagebutton:
                idle "gui/spyScreens/spyScreen1.png"
                hover "gui/spyScreens/spyScreen1-hover.png"
                action Jump("spyCameraGreen")
        hbox:
            spacing 10 xpos 600 ypos 95
            text "Spy: [greenName] \nLocation: [greenLocation] \nExpertise: Support"

    if spyRedActive == True:
        vbox xpos 110 ypos 140:
            imagebutton:
                idle "gui/spyScreens/spyScreen2.png"
                hover "gui/spyScreens/spyScreen2-hover.png"
                action Jump("spyCameraRed")
        hbox:
            spacing 10 xpos 120 ypos 150
            text "Spy: [redName] \nLocation: [redLocation] \nExpertise: Distraction"

    if spyYellowActive == True:
        vbox xpos 652 ypos 369:
            imagebutton:
                idle "gui/spyScreens/spyScreen3.png"
                hover "gui/spyScreens/spyScreen3-hover.png"
                action Jump("spyCameraYellow")
        hbox:
            spacing 10 xpos 725 ypos 435
            text "Spy: [yellowName] \nLocation: [yellowLocation] \nExpertise: Infiltration"



screen tutBase:
    zorder 0
    imagemap:
        ground "bgs/base/base.jpg"
        hover "bgs/base/base-hover.png"

        hotspot (1008, 168, 770, 464) clicked Jump("tutLift")
        hotspot (866, 349, 98, 205) clicked Jump("tutQuarters")

        hotspot (649, 581, 310, 120) clicked Jump("tutPrison")
        hotspot (122, 165, 183, 645) clicked Jump("tutSpyCamera")
        hotspot (297, 546, 241, 110) clicked Jump("tutDesk")



image blockOffice = "bgs/HQBlocks/blockOffice.png"
image blockIntel = "bgs/HQBlocks/blockIntel.png"
image blockFashion = "bgs/HQBlocks/blockFashion.png"
image blockEngineering = "bgs/HQBlocks/blockEngineering.png"
image blockEngineering = "bgs/HQBlocks/blockEngineering.png"
image blockPrison = "bgs/HQBlocks/blockPrison.png"

layeredimage bgHQ:
    always:
        "bgs/bgHQ.jpg"
    if HQLiberated <= 5:
        "bgs/HQBlocks/blockOffice.png"
    if HQLiberated <= 4:
        "bgs/HQBlocks/blockIntel.png"
    if HQLiberated <= 3:
        "bgs/HQBlocks/blockFashion.png"
    if HQLiberated <= 2:
        "bgs/HQBlocks/blockPropaganda.png"
    if HQLiberated <= 1:
        "bgs/HQBlocks/blockEngineering.png"
    if HQLiberated == 0:
        "bgs/HQBlocks/blockPrison.png"



screen HQButtons:

    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/missionScreen/exitButton2.png"
            hover "gui/missionScreen/exitButton2-hover.png"
            action Jump("worldmap")

    vbox xpos 0.88 ypos 10:
        imagebutton:
            idle "gui/HQButtonUp.png"
            hover "gui/HQButtonUp-hover.png"
            action SetVariable("HQMove", 1), Jump("moveHQ")

    vbox xpos 0.88 ypos 90:
        imagebutton:
            idle "gui/HQButtonDown.png"
            hover "gui/HQButtonDown-hover.png"
            action SetVariable("HQMove", 2), Jump("moveHQ")

    vbox xpos 0.84 ypos 150:
        imagebutton:
            idle "gui/assaultBt.png"
            hover "gui/assaultBt-hover.png"
            action Jump("assaultHQ")








image mapGangs = "gui/mapGangs/mapGangs.png"
default gangScreenActive = False

default zone1 = "aces"
default zone2 = "aces"
default zone3 = "glimmers"
default zone4 = "glimmers"
default zone5 = "punk"
default zone6 = "punk"
default zone7 = "punk"
default zone8 = "punk"
default zone9 = "glimmers"
default zone10 = "hunters"
default zone11 = "aces"
default zone12 = "aces"
default zone13 = "epines"
default zone14 = "epines"
default zone15 = "epines"
default zone16 = "hunters"
default zone17 = "harbingers"
default zone18 = "harbingers"
default zone19 = "harbingers"
default zone20 = "exchange"
default zone21 = "exchange"
default zone22 = "harbingers"
default zone23 = "harbingers"



screen white:
    add "gui/white.jpg"



default gang1Active = False
default gang2Active = False
default gang3Active = False
default gang4Active = False
default gang5Active = False
default gang6Active = False
default gang7Active = False
default gang8Active = False
default gang9Active = False
default mapSpy1Active = False
default mapSpy2Active = False
default mapSpy3Active = False
default mapSpy1Selected = False
default mapSpy2Selected = False
default mapSpy3Selected = False
default mapSpy4Selected = False
default mapSpy5Selected = False
default mapSpy6Selected = False
default mapSpy0Selected = False
default mainQuestUpdate = False
default searchTarget = 0

default mainQuestUpdatePic = "gui/mainQuestUpdate.png"

default mapSelectButton = 0

default randNotMission = 0

transform mainQuestUpdateAni:
    linear 0.25 rotate 10
    pause 0.7
    linear 0.25 rotate -20
    pause 0.7
    repeat

default phoneAniPic = "gui/phone.png"
transform phoneAni:
    linear 0.25 rotate 10
    pause 0.7
    linear 0.25 rotate -20
    pause 0.7
    repeat

screen mapButtons:

    if spyGreenActive and mapSpy1Active and mapSpy1Selected == False and spy1Status == 0:
        vbox xalign 0.44 yalign 0.88:
            imagebutton:
                idle "gui/spyMap1.png"
                hover "gui/spyMap1-hover.png"
                action Jump("spy1MapSelect")
    if spyGreenActive and mapSpy1Active and mapSpy1Selected == True and spy1Status == 0:
        vbox xalign 0.44 yalign 0.88:
            imagebutton:
                idle "gui/spyMap1-hover.png"
                hover "gui/spyMap1-hover.png"
                action Jump("spy1MapSelect")
    if spyGreenActive and mapSpy1Active and mapSpy1Selected == False and spy1Status >= 1:
        vbox xalign 0.44 yalign 0.88:
            imagebutton:
                idle "gui/spyMap1Disable.png"


    if spyRedActive and mapSpy2Active and mapSpy2Selected == False and spy2Status == 0:
        vbox xalign 0.49 yalign 0.88:
            imagebutton:
                idle "gui/spyMap2.png"
                hover "gui/spyMap2-hover.png"
                action Jump("spy2MapSelect")
    if spyRedActive and mapSpy2Active and mapSpy2Selected == True and spy2Status == 0:
        vbox xalign 0.49 yalign 0.88:
            imagebutton:
                idle "gui/spyMap2-hover.png"
                hover "gui/spyMap2-hover.png"
                action Jump("spy2MapSelect")
    if spyRedActive and mapSpy2Active and mapSpy2Selected == False and spy2Status >= 1:
        vbox xalign 0.49 yalign 0.88:
            imagebutton:
                idle "gui/spyMap2Disable.png"


    if spyYellowActive and mapSpy3Active and mapSpy3Selected == False and spy3Status == 0:
        vbox xalign 0.54 yalign 0.88:
            imagebutton:
                idle "gui/spyMap3.png"
                hover "gui/spyMap3-hover.png"
                action Jump("spy3MapSelect")
    if spyYellowActive and mapSpy3Active and mapSpy3Selected == True and spy3Status == 0:
        vbox xalign 0.54 yalign 0.88:
            imagebutton:
                idle "gui/spyMap3-hover.png"
                hover "gui/spyMap3-hover.png"
                action Jump("spy3MapSelect")
    if spyYellowActive and mapSpy3Active and mapSpy3Selected == False and spy3Status >= 1:
        vbox xalign 0.54 yalign 0.88:
            imagebutton:
                idle "gui/spyMap3Disable.png"


    if spyGreenActive and spyRedActive and spyYellowActive:
        if mapSpy1Selected or mapSpy1Selected or mapSpy1Selected:
            vbox xalign 0.57 yalign 0.88:
                imagebutton:
                    idle "gui/selectSpies.png"
        elif spy1Status >= 1 or spy2Status >= 1 or spy3Status >= 1:
            vbox xalign 0.57 yalign 0.88:
                imagebutton:
                    idle "gui/selectSpies.png"
        else:
            vbox xalign 0.57 yalign 0.88:
                imagebutton:
                    idle "gui/selectSpies.png"
                    hover "gui/selectSpies-hover.png"
                    action SetVariable("mapSpy1Selected", True), SetVariable("mapSpy2Selected", True), SetVariable("mapSpy3Selected", True)


    if task4Stage >= 4:
        vbox xalign 0.25 yalign 0.0:
            imagebutton:
                idle "gui/coverCounter.png"
                hover "gui/coverCounter.png" tooltip "ttCover"
                action Jump("status")
        $ tooltip = GetTooltip()
        if tooltip == "ttCover":
            text "{font=fonts/freshMarker.ttf}{size=-4}Noteriety{/size}{/font}" xpos 310 yalign 0.055
        text "{font=fonts/freshMarker.ttf}[coverCounter]{/font}" xpos 350 yalign 0.012


    vbox xalign 0.40 yalign 0.0:
        imagebutton:
            idle "gui/moneyCounter.png"
            hover "gui/moneyCounter.png" tooltip "ttMoney"
            action Jump("status")
    $ tooltip = GetTooltip()
    if tooltip == "ttMoney":
        text "{font=fonts/freshMarker.ttf}{size=-4}Cash{/size}{/font}" xpos 470 yalign 0.055
    text "{font=fonts/freshMarker.ttf}[cash]{/font}" xpos 510 yalign 0.012


    vbox xalign 0.55 yalign 0.0:
        imagebutton:
            idle "gui/intelCounter.png"
            hover "gui/intelCounter.png" tooltip "ttIntel"
            action Jump("status")
    $ tooltip = GetTooltip()
    if tooltip == "ttIntel":
        text "{font=fonts/freshMarker.ttf}{size=-4}Intel{/size}{/font}" xpos 630 yalign 0.055
    text "{font=fonts/freshMarker.ttf}[intel]{/font}" xpos 670 yalign 0.012


    if capturedAgents >= 1 or freedAgents >= 1:
        vbox xalign 0.70 yalign 0.0:
            imagebutton:
                idle "gui/agentCounter.png"
                hover "gui/agentCounter.png" tooltip "ttAgents"
                action Jump("checkStatusAgents")
        $ tooltip = GetTooltip()
        if tooltip == "ttAgents":
            text "{font=fonts/freshMarker.ttf}{size=-4}Agents{/size}{/font}" xpos 800 yalign 0.055
        text "{font=fonts/freshMarker.ttf}[freedAgents]/[capturedAgents]{/font}" xpos 840 yalign 0.012


    add "gui/dayCounter.png" xpos 940 yalign 0.0
    text "{font=fonts/freshMarker.ttf}{size=-4}Day: [daysPlayed]{/size}{/font}" xpos 990 yalign 0.012


    if mainQuestUpdate:
        vbox xalign 0.24 yalign 1.0:
            imagebutton:
                idle mainQuestUpdatePic at mainQuestUpdateAni
                hover "gui/mainQuestUpdate.png"
                action SetVariable("mainQuestUpdate", False), Jump("quests")


    if tutStage >= 2:
        vbox xalign 0.5 yalign 1.0:
            imagebutton:
                idle "gui/mapUI.png"

        vbox xalign 0.308 yalign 1.0:
            imagebutton:
                idle "gui/mapUIMission.png"
                hover "gui/mapUIMission-hover.png"
                action Jump("resetVarMis")
        if mapSelectButton == 1:
            frame:
                xpadding 12
                pos (360, 555)
                has vbox
                if spyGreenActive:
                    textbutton "Sam":
                        clicked Hide("menu1"), Jump("samCall")
                else:
                    textbutton "???":
                        clicked Hide("menu1"), Jump("worldmap")
                if spyRedActive:
                    textbutton "Clover":
                        clicked Hide("menu1"), Jump("cloverCall")
                else:
                    textbutton "???":
                        clicked Hide("menu1"), Jump("worldmap")
                if spyYellowActive:
                    textbutton "Alex":
                        clicked Hide("menu1"), Jump("alexCall")
                else:
                    textbutton "???":
                        clicked Hide("menu1"), Jump("worldmap")


        vbox xalign 0.404 yalign 1.0:
            imagebutton:
                idle "gui/mapUIStatus.png"
                hover "gui/mapUIStatus-hover.png"
                if mapSelectButton == 2:
                    action SetVariable("mapSelectButton", 0)
                else:
                    action SetVariable("mapSelectButton", 2)
        if mapSelectButton == 2:
            frame:
                xpadding 22
                pos (467, 565)
                has vbox
                textbutton "{font=fonts/freshmarker.ttf}Quests{/font}":

                    action SetVariable("mapSelectButton", 0), Jump("quests")
                textbutton "{font=fonts/freshmarker.ttf}Lore{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("lore")
                textbutton "{font=fonts/freshmarker.ttf}Status{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("status")


        vbox xalign 0.503 yalign 1.0:
            imagebutton:
                idle "gui/mapUIItems.png"
                hover "gui/mapUIItems-hover.png"
                if mapSelectButton != 3:
                    action SetVariable("mapSelectButton", 3)
                else:
                    action SetVariable("mapSelectButton", 0)
        if mapSelectButton == 3:
            frame:
                xpadding 15
                pos (582, 565)
                has vbox
                textbutton "{font=fonts/freshmarker.ttf}Gadgets{/font}":

                    clicked SetVariable("mapSelectButton", 0), Jump("desk")
                textbutton "{font=fonts/freshmarker.ttf}Outfits{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("outfits")
                textbutton "{font=fonts/freshmarker.ttf}Items{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("items")


        vbox xalign 0.6 yalign 1.0:
            imagebutton:
                idle "gui/mapUIExplore.png"
                hover "gui/mapUIExplore-hover.png"
                action Jump("exploreMap")


        vbox xalign 0.69 yalign 1.0:
            imagebutton:
                idle "gui/mapUINight.png"
                hover "gui/mapUINight-hover.png"
                if tod == 1:
                    action Jump("jobReport")
                else:
                    action Jump("nightCycle")


        if jobEventSam == 4 and slutLevel >= 3:
            vbox xalign 0.02 yalign 0.99:
                imagebutton:
                    idle phoneAniPic
                    hover "gui/phone-hover.png"
                    action Jump("workBonusMenu")

        if jobEventClover == 4 and slutLevel >= 3:
            vbox xalign 0.02 yalign 0.99:
                imagebutton:
                    idle phoneAniPic
                    hover "gui/phone-hover.png"
                    action Jump("workBonusMenu")

        if jobEventAlex == 4 and slutLevel >= 3:
            vbox xalign 0.02 yalign 0.99:
                imagebutton:
                    idle phoneAniPic
                    hover "gui/phone-hover.png"
                    action Jump("workBonusMenu")


    if task30Stage >= 1:
        vbox xpos 1020 ypos 250:
            imagebutton:
                idle "gui/arrowSchool.png"
                hover "gui/arrowSchool-hover.png"
                action Jump("hireStaff")


    if task15Stage == 1 and task15Girls == False:
        vbox xpos 1060 ypos 270:
            imagebutton:
                idle "gui/arrowSchool.png"
                hover "gui/arrowSchool-hover.png"
                action Jump("task15HireSluts")


    if task4Stage == 1:
        vbox xpos 1010 ypos 280:
            imagebutton:
                idle "gui/arrowSchool.png"
                hover "gui/arrowSchool-hover.png"
                action Jump("task4")
        if task4Stage == 1:
            add "gui/qMarker1.png" xpos 1040 ypos 280

        if task5Stage == 0 and spyYellowActive and gang3Active and day >= 35:
            add "gui/qMarker1.png" xpos 1040 ypos 280




    if month == 10 and 14 <= day <= 31 and spiritEncounter <= 4 and tutorialActive == False:
        vbox xalign 0.495 yalign 0.295:
            imagebutton:
                idle "gui/arrowHalloween.png"
                hover "gui/arrowHalloween-hover.png"
                action Jump("halloweenEvent")

    if month == 10 and 14 <= day <= 31 and gang1Active == False and gang2Active == False and gang3Active == False:
        if mapSpy1Selected or mapSpy2Selected or mapSpy3Selected:
            vbox xalign 0.5 yalign 0.57:
                imagebutton:
                    idle "gui/arrowHalloween.png"
                    hover "gui/arrowHalloween-hover.png"
                    action Jump("jobTrickOrTreat")


    if month == 12 and 14 <= day <= 31 and spiritEncounter <= 4 and tutorialActive == False and xmasUpdateStage <= 5:
        vbox xalign 0.395 yalign 0.55:
            imagebutton:
                idle "gui/arrowXmas.png"
                hover "gui/arrowXmas-hover.png"
                action Jump("christmasUpdate")


    if gang1Active and mapSpy1Selected or gang1Active and mapSpy2Selected or gang1Active and mapSpy3Selected:
        vbox xpos 80 ypos 150:
            imagebutton:
                idle "gui/daggerAces.png"
                hover "gui/daggerAces-hover.png" tooltip "ttAces"
                action Jump("acesMapSelect")
        $ tooltip = GetTooltip()
        if tooltip == "ttAces":
            add "gui/mapGangs/gangRepGraphic.png" xpos 120 ypos 130
            text "{font=fonts/freshmarker.ttf}{size=+18}Aces{/size}{/font}" xpos 265 ypos 202
            if specialMaggieStatus == 1:
                add "gui/mapGangs/acesLt1.png" xpos 225 ypos 300
            elif specialMaggieStatus >= 2:
                add "gui/mapGangs/acesLt1Cap.png" xpos 225 ypos 300
            if specialMelodyStatus == 1:
                add "gui/mapGangs/acesLt2.png" xpos 275 ypos 300
            if specialMelodyStatus >= 2:
                add "gui/mapGangs/acesLt2Cap.png" xpos 275 ypos 300
            if specialCandyStatus == 1:
                add "gui/mapGangs/acesLt3.png" xpos 330 ypos 300
            if specialCandyStatus == 3:
                add "gui/mapGangs/acesLt3Cap.png" xpos 330 ypos 300

            bar:
                value acesRep
                range 18
                left_bar "gui/mapGangs/bar.png"
                right_bar "gui/mapGangs/barEmpty.png"
                thumb_offset 0
                xysize (90,10)
                xpos 215
                ypos 265
            text "{font=fonts/truckin.ttf}[acesRank]{/size}" xpos 371 ypos 257

        if task3Stage == 1 and spyYellowActive == True:
            add "gui/qMarker1.png" xpos 105 ypos 150
        if task6Stage == 0 and acesRep >= 9 and acesRank >= 2:
            add "gui/qMarker1.png" xpos 105 ypos 150
        if task6Stage == 4 and acesRep >= 18 and acesRank >= 2:
            add "gui/qMarker1.png" xpos 105 ypos 150
        if task6Stage == 6 and acesRep >= 9 and acesRank >= 3:
            add "gui/qMarker1.png" xpos 105 ypos 150
        if task6Stage == 9 and acesRep >= 18 and acesRank >= 3 and specialMelodyStatus == 1 and specialDragonStatus >= 2 and specialMuffyStatus >= 2:
            add "gui/qMarker1.png" xpos 105 ypos 150
        if task15Stage == 0 and acesRep >= 9 and acesRank >= 4:
            add "gui/qMarker1.png" xpos 105 ypos 150
        if task16Stage == 0 and task15Stage >= 3 and acesRep >= 18 and acesRank >= 4 and specialCandyStatus >= 1:
            add "gui/qMarker1.png" xpos 105 ypos 150

        if task19Stage == 0 and acesRep >= 4 and acesRank == 1 and mapSpy1Selected:
            add "gui/qMarker1.png" xpos 105 ypos 150

    if gang2Active == True and mapSpy1Selected or gang2Active == True and mapSpy2Selected or gang2Active == True and mapSpy3Selected:
        vbox xpos 900 ypos 430:
            imagebutton:
                idle "gui/daggerPunk.png"
                hover "gui/daggerPunk-hover.png" tooltip "ttPunks"
                action Jump("punkMapSelect")
        $ tooltip = GetTooltip()
        if tooltip == "ttPunks":
            add "gui/mapGangs/gangRepGraphic.png" xpos 940 ypos 420
            text "{font=fonts/freshmarker.ttf}{size=+12}Drift Punk{/size}{/font}" xpos 1030 ypos 500
            if specialDragonStatus == 1:
                add "gui/mapGangs/punkLt1.png" xpos 1045 ypos 590
            if specialDragonStatus >= 2:
                add "gui/mapGangs/punkLt1Cap.png" xpos 1045 ypos 590
            if specialTaliaStatus == 1:
                add "gui/mapGangs/punkLt2.png" xpos 1098 ypos 590
            if specialTaliaStatus >= 2:
                add "gui/mapGangs/punkLt2Cap.png" xpos 1098 ypos 590
            if specialSebStatus == 1:
                add "gui/mapGangs/punkLt3.png" xpos 1151 ypos 590
            if specialSebStatus >= 2:
                add "gui/mapGangs/punkLt3Cap.png" xpos 1151 ypos 590

            bar:
                value punkRep
                range 18
                left_bar "gui/mapGangs/bar.png"
                right_bar "gui/mapGangs/barEmpty.png"
                thumb_offset 0
                xysize (100,10)
                xpos 1030
                ypos 555
            text "{font=fonts/truckin.ttf}[punkRank]{/size}" xpos 1190 ypos 546

        if punkRank >= 1 and punkRep >= 5 and task9Stage == 0 and mapSpy2Selected:
            add "gui/qMarker1.png" xpos 935 ypos 430
        if punkRank >= 1 and punkRep >= 18 and task10Stage == 0 and task3Stage >= 7 and task4Stage >= 4 and mapSpy2Selected:
            add "gui/qMarker1.png" xpos 935 ypos 430
        if punkRank >= 2 and punkRep >= 11 and task17Stage == 0 and mapSpy2Selected:
            add "gui/qMarker1.png" xpos 935 ypos 430
        if punkRank >= 2 and punkRep >= 18 and task17Stage == 7 and task18Stage == 0 and specialTaliaStatus == 1 and mapSpy2Selected:
            add "gui/qMarker1.png" xpos 935 ypos 430
        if task17Stage >= 7 and punkRank >= 2 and punkRep >= 4 and task24Stage == 0 and mapSpy2Selected:
            add "gui/qMarker1.png" xpos 935 ypos 430
        if punkRank >= 3 and punkRep >= 18 and task23Stage == 0 and specialSebStatus == 1 and mapSpy2Selected:
            add "gui/qMarker1.png" xpos 935 ypos 430


    if gang3Active == True and mapSpy1Selected or gang3Active == True and mapSpy2Selected or gang3Active == True and mapSpy3Selected:
        vbox xalign 0.93 yalign 0.15:
            imagebutton:
                idle "gui/daggerHar.png"
                hover "gui/daggerHar-hover.png" tooltip "ttOutsiders"
                action Jump("harbingerMapSelect")
        $ tooltip = GetTooltip()
        if tooltip == "ttOutsiders":
            add "gui/mapGangs/gangRepGraphic.png" xpos 840 ypos 60
            text "{font=fonts/freshmarker.ttf}{size=+14}Outsiders{/size}{/font}" xpos 935 ypos 136
            if specialMuffyStatus == 1:
                add "gui/mapGangs/outsidersLt1.png" xpos 945 ypos 230
            if specialMuffyStatus >= 2:
                add "gui/mapGangs/outsidersLt1Cap.png" xpos 945 ypos 230
            if specialFelicityStatus == 1:
                add "gui/mapGangs/outsidersLt2.png" xpos 995 ypos 230
            if specialFelicityStatus >= 2:
                add "gui/mapGangs/outsidersLt2Cap.png" xpos 1000 ypos 230
            if specialKandStatus == 1:
                add "gui/mapGangs/outsidersLt3.png" xpos 1050 ypos 230
            if specialKandStatus == 3:
                add "gui/mapGangs/outsidersLt3Cap.png" xpos 1050 ypos 230

            bar:
                value outsideRep
                range 18
                left_bar "gui/mapGangs/bar.png"
                right_bar "gui/mapGangs/barEmpty.png"
                thumb_offset 0
                xysize (100,10)
                xpos 930
                ypos 195
            text "{font=fonts/truckin.ttf}[outsideRank]{/size}" xpos 1090 ypos 186

        if outsideRank >= 1 and outsideRep >= 6 and task11Stage == 0 and mapSpy3Selected:
            add "gui/qMarker1.png" xpos 1170 ypos 85
        if outsideRank >= 1 and outsideRep >= 18 and task11Stage == 2 and mapSpy3Selected:
            add "gui/qMarker1.png" xpos 1170 ypos 85
        if outsideRank >= 2 and outsideRep >= 9 and task20Stage == 0 and mapSpy3Selected:
            add "gui/qMarker1.png" xpos 1170 ypos 85
        if outsideRank >= 2 and outsideRep >= 18 and task21Stage == 0 and specialFelicityStatus == 1 and mapSpy3Selected:
            add "gui/qMarker1.png" xpos 1170 ypos 85
        if outsideRank >= 3 and outsideRep >= 18 and mapSpy3Selected and specialKandStatus == 1:
            add "gui/qMarker1.png" xpos 1170 ypos 85
        if task4Stage == 6 and spy1Status <= 1 and mapSpy3Selected:
            add "gui/qMarker1.png" xpos 1170 ypos 85

    if task12Stage == 0 and daysPlayed >= 61:
        add "gui/qMarker1.png" xpos 680 ypos 50

    if task26Stage >= 2:
        vbox xalign 0.2 yalign 0.1:
            imagebutton:
                idle "gui/woohpIcon.png"
                hover "gui/woohpIcon-hover.png"
                action Jump("woohpHQ")


    if task3Stage == 7 and spy1Status == 0 and spy2Status == 0 and spy3Status == 0 and spyYellowActive:
        vbox xalign 0.545 yalign 0.335:
            imagebutton:
                idle "gui/mapUISideQuest.png"
                hover "gui/mapUISideQuest-hover.png"
                action Jump("task3")


    if gang4Active == True and mapSpy1Selected == False and mapSpy2Selected == False and mapSpy3Selected == False and socialSilva <= 7:
        vbox xalign 0.65 yalign 0.26:
            imagebutton:
                idle "gui/arrowSilva.png"
                hover "gui/arrowSilva-hover.png"
                action Jump("socialSilva")
    if gang4Active == True and mapSpy1Selected or gang4Active == True and mapSpy2Selected or gang4Active == True and mapSpy3Selected:
        vbox xalign 0.661 yalign 0.28:
            imagebutton:
                idle "gui/daggerSilva.png"
                hover "gui/daggerSilva-hover.png"
                action Jump("epinesMapSelect")
    if tutStage >= 8 and mapSpy1Selected or tutStage >= 8 and mapSpy2Selected or tutStage >= 8 and mapSpy3Selected:
        vbox xalign 0.565 yalign 0.275:
            imagebutton:
                idle "gui/daggerClub.png"
                hover "gui/daggerClub-hover.png"
                if mapSpy1Selected:
                    action Jump("clubMapSelect")
                elif mapSpy2Selected:
                    action Jump("clubMapSelect")
                elif mapSpy3Selected:
                    action Jump("clubMapSelect")
    elif tutStage >= 8 and mapSpy1Selected == False or tutStage >= 8 and mapSpy2Selected == False or tutStage >= 8 and mapSpy3Selected == False:
        vbox xalign 0.565 yalign 0.275:
            imagebutton:
                idle "gui/arrowClub.png"
                hover "gui/arrowClub-hover.png"
                action Jump("club")
        if menuTutActive and spyGreenActive and spyRedActive and spyYellowActive:
            add "gui/qMarker1.png" xalign 0.575 yalign 0.283
    if task8Stage >= 2 and mapSpy1Selected or task8Stage >= 2 and mapSpy2Selected or task8Stage >= 2 and mapSpy3Selected:
        vbox xalign 0.565 yalign 0.34:
            imagebutton:
                idle "gui/arrowBreak.png"
                hover "gui/arrowBreak-hover.png"
                if mapSpy1Selected:
                    action Jump("breakMapSelect")
                elif mapSpy2Selected:
                    action Jump("breakMapSelect")
                elif mapSpy3Selected:
                    action Jump("breakMapSelect")
    if tutorialActive == False:
        if mapSpy1Selected == False or mapSpy2Selected == False or mapSpy3Selected == False:
            vbox xalign 0.63 yalign 0.42:
                imagebutton:
                    idle "gui/arrowATM.png"
                    hover "gui/arrowATM-hover.png"
                    action Jump("creditcards")
    if tutStage >= 4 and mallActive and tod == 1:
        vbox xalign 0.52 yalign 0.07:
            imagebutton:
                idle "gui/arrowMall.png"
                hover "gui/arrowMall-hover.png"
                if mapSpy1Selected == True:
                    action Jump("mallMapSelect")
                elif mapSpy2Selected:
                    action Jump("mallMapSelect")
                elif mapSpy3Selected:
                    action Jump("mallMapSelect")
                else:
                    action Jump("mall")
    if hackerUnlocked:
        vbox xalign 0.56 yalign 0.58:
            imagebutton:
                idle "gui/arrowMat.png"
                hover "gui/arrowMat-hover.png"
                action Jump("hacker")
    if mapSpy1Selected == True or mapSpy2Selected == True or mapSpy3Selected == True:
        if tutStage >= 4 and beachActive and tod == 1:
            vbox xalign 0.18 yalign 0.85:
                imagebutton:
                    idle "gui/arrowBeach.png"
                    hover "gui/arrowBeach-hover.png"
                    if mapSpy1Selected:
                        action Jump("beachMapSelect")
                    elif mapSpy2Selected:
                        action Jump("beachMapSelect")
                    elif mapSpy3Selected:
                        action Jump("beachMapSelect")

    if randNotMission == 10:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/arrowGun.png"
                hover "gui/arrowGun-hover.png"
                if mapSpy1Selected == True:
                    action Jump("crimeMapSelect")
                elif mapSpy2Selected:
                    action Jump("crimeMapSelect")
                elif mapSpy3Selected:
                    action Jump("crimeMapSelect")
    if randNotMission == 9:
        vbox xalign 0.2 yalign 0.75:
            imagebutton:
                idle "gui/arrowAuto.png"
                hover "gui/arrowAuto-hover.png"
                if mapSpy1Selected == True:
                    action Jump("crimeMapSelect")
                elif mapSpy2Selected:
                    action Jump("crimeMapSelect")
                elif mapSpy3Selected:
                    action Jump("crimeMapSelect")
    if randNotMission == 8:
        vbox xalign 0.38 yalign 0.42:
            imagebutton:
                idle "gui/arrowFire.png"
                hover "gui/arrowFire-hover.png"
                if mapSpy1Selected == True:
                    action Jump("crimeMapSelect")
                elif mapSpy2Selected:
                    action Jump("crimeMapSelect")
                elif mapSpy3Selected:
                    action Jump("crimeMapSelect")
    if 6 <= randNotMission <= 7:
        vbox xalign 0.6 yalign 0.65:
            imagebutton:
                idle "gui/arrowPP.png"
                hover "gui/arrowPP-hover.png"
                if mapSpy1Selected == True:
                    action Jump("crimeMapSelect")
                elif mapSpy2Selected:
                    action Jump("crimeMapSelect")
                elif mapSpy3Selected:
                    action Jump("crimeMapSelect")
    if 4 <= randNotMission <= 5:
        vbox xalign 0.54 yalign 0.15:
            imagebutton:
                idle "gui/arrowGraf.png"
                hover "gui/arrowGraf-hover.png"
                if mapSpy1Selected:
                    action Jump("crimeMapSelect")
                elif mapSpy2Selected:
                    action Jump("crimeMapSelect")
                elif mapSpy3Selected:
                    action Jump("crimeMapSelect")

    if task21Stage == 4:
        vbox xalign 0.3 yalign 0.9:
            imagebutton:
                idle "gui/arrowModel.png"
                hover "gui/arrowModel-hover.png"
                if mapSpy3Selected:
                    action Jump("task21")



    if greenDayJob == 1:
        vbox xpos 105 ypos 150:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 2:
        vbox xpos 870 ypos 450:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 3:
        vbox xpos 1186 ypos 103:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 4:
        vbox xpos 685 ypos 180:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 5:
        vbox xpos 770 ypos 165:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 6:
        vbox xpos 590 ypos 315:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 7:
        vbox xpos 440 ypos 260:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 8:
        vbox xpos 720 ypos 420:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 9:
        vbox xpos 650 ypos 80:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 10:
        vbox xpos 230 ypos 490:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 100:
        vbox xalign 0.485 yalign 0.06:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 101:
        vbox xalign 0.15 yalign 0.83:
            imagebutton:
                idle "gui/atLocationSam.png"
    if greenDayJob == 102:
        vbox xalign 0.5 yalign 0.5:
            imagebutton:
                idle "gui/atLocationSam.png"

    if redDayJob == 1:
        vbox xpos 125 ypos 150:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 2:
        vbox xpos 895 ypos 450:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 3:
        vbox xpos 1186 ypos 103:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 4:
        vbox xpos 710 ypos 180:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 5:
        vbox xpos 770 ypos 165:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 6:
        vbox xpos 610 ypos 315:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 7:
        vbox xpos 460 ypos 260:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 8:
        vbox xpos 740 ypos 420:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 9:
        vbox xpos 680 ypos 80:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 10:
        vbox xpos 250 ypos 490:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 100:
        vbox xalign 0.485 yalign 0.06:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 101:
        vbox xalign 0.17 yalign 0.83:
            imagebutton:
                idle "gui/atLocationClover.png"
    if redDayJob == 102:
        vbox xalign 0.515 yalign 0.5:
            imagebutton:
                idle "gui/atLocationClover.png"

    if yellowDayJob == 1:
        vbox xpos 145 ypos 150:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 2:
        vbox xpos 920 ypos 450:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 3:
        vbox xpos 1186 ypos 103:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 4:
        vbox xpos 665 ypos 180:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 5:
        vbox xpos 770 ypos 165:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 6:
        vbox xpos 630 ypos 315:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 7:
        vbox xpos 480 ypos 260:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 8:
        vbox xpos 760 ypos 420:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 9:
        vbox xpos 710 ypos 80:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 10:
        vbox xpos 270 ypos 490:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 100:
        vbox xalign 0.485 yalign 0.06:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 101:
        vbox xalign 0.19 yalign 0.83:
            imagebutton:
                idle "gui/atLocationAlex.png"
    if yellowDayJob == 102:
        vbox xalign 0.53 yalign 0.5:
            imagebutton:
                idle "gui/atLocationAlex.png"


label checkStatusAgents:
    "You have [capturedAgents] captured nano controlled agents and [freedAgents] freed agents ready for duty."
    $ timeToGrab = 30 - landgrabTimer
    "It is [timeToGrab] more days until the next Landgrab."
    if task3Stage >= 7:
        menu:
            "Skip to the next landgrab" if True:
                scene black with fade
                $ daysPlayed += timeToGrab
                $ landgrabTimer = 30
                jump worldmap
            "Never mind" if True:
                pass
    jump worldmap


screen mapButtonsRaid:

    if spyGreenActive and mapSpy1Active and mapSpy1Selected == False and spy1Status == 0:
        vbox xalign 0.44 yalign 0.88:
            imagebutton:
                idle "gui/spyMap1.png"
                hover "gui/spyMap1-hover.png"
                action Jump("spy1MapSelect")
    if spyGreenActive and mapSpy1Active and mapSpy1Selected == True and spy1Status == 0:
        vbox xalign 0.44 yalign 0.88:
            imagebutton:
                idle "gui/spyMap1-hover.png"
                hover "gui/spyMap1-hover.png"
                action Jump("spy1MapSelect")
    if spyGreenActive and mapSpy1Active and mapSpy1Selected == False and spy1Status >= 1:
        vbox xalign 0.44 yalign 0.88:
            imagebutton:
                idle "gui/spyMap1Disable.png"


    if spyRedActive and mapSpy2Active and mapSpy2Selected == False and spy2Status == 0:
        vbox xalign 0.49 yalign 0.88:
            imagebutton:
                idle "gui/spyMap2.png"
                hover "gui/spyMap2-hover.png"
                action Jump("spy2MapSelect")
    if spyRedActive and mapSpy2Active and mapSpy2Selected == True and spy2Status == 0:
        vbox xalign 0.49 yalign 0.88:
            imagebutton:
                idle "gui/spyMap2-hover.png"
                hover "gui/spyMap2-hover.png"
                action Jump("spy2MapSelect")
    if spyRedActive and mapSpy2Active and mapSpy2Selected == False and spy2Status >= 1:
        vbox xalign 0.49 yalign 0.88:
            imagebutton:
                idle "gui/spyMap2Disable.png"


    if spyYellowActive and mapSpy3Active and mapSpy3Selected == False and spy3Status == 0:
        vbox xalign 0.54 yalign 0.88:
            imagebutton:
                idle "gui/spyMap3.png"
                hover "gui/spyMap3-hover.png"
                action Jump("spy3MapSelect")
    if spyYellowActive and mapSpy3Active and mapSpy3Selected == True and spy3Status == 0:
        vbox xalign 0.54 yalign 0.88:
            imagebutton:
                idle "gui/spyMap3-hover.png"
                hover "gui/spyMap3-hover.png"
                action Jump("spy3MapSelect")
    if spyYellowActive and mapSpy3Active and mapSpy3Selected == False and spy3Status >= 1:
        vbox xalign 0.54 yalign 0.88:
            imagebutton:
                idle "gui/spyMap3Disable.png"


    if spyGreenActive and spyRedActive and spyYellowActive:
        if mapSpy1Selected or mapSpy1Selected or mapSpy1Selected:
            vbox xalign 0.57 yalign 0.88:
                imagebutton:
                    idle "gui/selectSpies.png"
        elif spy1Status >= 1 or spy2Status >= 1 or spy3Status >= 1:
            vbox xalign 0.57 yalign 0.88:
                imagebutton:
                    idle "gui/selectSpies.png"
        else:
            vbox xalign 0.57 yalign 0.88:
                imagebutton:
                    idle "gui/selectSpies.png"
                    hover "gui/selectSpies-hover.png"
                    action SetVariable("mapSpy1Selected", True), SetVariable("mapSpy2Selected", True), SetVariable("mapSpy3Selected", True)


    if 30 <= landgrabTimer <= 31 and task3Stage >= 7:
        if gang1Active and task3Stage >= 7:
            vbox xalign 0.12 yalign 0.25:
                imagebutton:
                    idle "gui/mapUILandgrabTarget.png"
                    hover "gui/mapUILandgrabTarget-hover.png"
                    action SetVariable("landgrabTarget", 1), Jump("landgrabPlanning")
        if gang2Active and task3Stage >= 8:
            vbox xalign 0.9 yalign 0.85:
                imagebutton:
                    idle "gui/mapUILandgrabTarget.png"
                    hover "gui/mapUILandgrabTarget-hover.png"
                    action SetVariable("landgrabTarget", 2), Jump("landgrabPlanning")
        if gang3Active and task3Stage >= 8:
            vbox xalign 0.86 yalign 0.15:
                imagebutton:
                    idle "gui/mapUILandgrabTarget.png"
                    hover "gui/mapUILandgrabTarget-hover.png"
                    action SetVariable("landgrabTarget", 3), Jump("landgrabPlanning")



        if landgrabRandomAssist1 == 1:
            vbox xalign 0.4 yalign 0.3:
                imagebutton:
                    idle "gui/mapUILandgrabAssist.png"
                    hover "gui/mapUILandgrabAssist-hover.png"
                    action SetVariable("landgrabTarget", 5), Jump("landgrabPlanning")
        if landgrabRandomAssist2 == 1:
            vbox xalign 0.7 yalign 0.5:
                imagebutton:
                    idle "gui/mapUILandgrabAssist.png"
                    hover "gui/mapUILandgrabAssist-hover.png"
                    action SetVariable("landgrabTarget", 6), Jump("landgrabPlanning")
        if landgrabRandomAssist3 == 1:
            vbox xalign 0.35 yalign 0.8:
                imagebutton:
                    idle "gui/mapUILandgrabAssist.png"
                    hover "gui/mapUILandgrabAssist-hover.png"
                    action SetVariable("landgrabTarget", 7), Jump("landgrabPlanning")



    if gang1Active and mapSpy1Selected or gang1Active and mapSpy2Selected or gang1Active and mapSpy3Selected:
        vbox xpos 80 ypos 150:
            imagebutton:
                idle "gui/daggerAces.png"
                hover "gui/daggerAces-hover.png" tooltip "ttAcesGrab"
                action Jump("acesMapSelect")
        $ tooltip = GetTooltip()
        if tooltip == "ttAcesGrab":
            add "gui/mapGangs/gangRepGraphic.png" xpos 120 ypos 130
            text "{font=fonts/freshmarker.ttf}{size=+18}Aces{/size}{/font}" xpos 265 ypos 202
            if specialMaggieStatus >= 1:
                add "gui/mapGangs/acesLt1.png" xpos 225 ypos 300

            bar:
                value acesRep
                range 18
                left_bar "gui/mapGangs/bar.png"
                right_bar "gui/mapGangs/barEmpty.png"
                thumb_offset 0
                xysize (90,10)
                xpos 215
                ypos 265
            text "{font=fonts/truckin.ttf}[acesRank]{/size}" xpos 371 ypos 257


    if gang2Active == True and mapSpy1Selected or gang2Active == True and mapSpy2Selected or gang2Active == True and mapSpy3Selected:
        vbox xpos 900 ypos 430:
            imagebutton:
                idle "gui/daggerPunk.png"
                hover "gui/daggerPunk-hover.png" tooltip "ttPunks"
                action Jump("punkMapSelect")
        $ tooltip = GetTooltip()
        if tooltip == "ttPunks":
            add "gui/mapGangs/gangRepGraphic.png" xpos 940 ypos 420
            text "{font=fonts/freshmarker.ttf}{size=+12}Drift Punk{/size}{/font}" xpos 1030 ypos 500
            bar:
                value punkRep
                range 18
                left_bar "gui/mapGangs/bar.png"
                right_bar "gui/mapGangs/barEmpty.png"
                thumb_offset 0
                xysize (100,10)
                xpos 1030
                ypos 555
            text "{font=fonts/truckin.ttf}[punkRank]{/size}" xpos 1190 ypos 546

    if gang3Active == True and mapSpy1Selected or gang3Active == True and mapSpy2Selected or gang3Active == True and mapSpy3Selected:
        vbox xalign 0.93 yalign 0.15:
            imagebutton:
                idle "gui/daggerHar.png"
                hover "gui/daggerHar-hover.png" tooltip "ttOutsiders"
                action Jump("harbingerMapSelect")
        $ tooltip = GetTooltip()
        if tooltip == "ttOutsiders":
            add "gui/mapGangs/gangRepGraphic.png" xpos 840 ypos 60
            text "{font=fonts/freshmarker.ttf}{size=+14}Outsiders{/size}{/font}" xpos 935 ypos 136
            bar:
                value outsideRep
                range 18
                left_bar "gui/mapGangs/bar.png"
                right_bar "gui/mapGangs/barEmpty.png"
                thumb_offset 0
                xysize (100,10)
                xpos 930
                ypos 195
            text "{font=fonts/truckin.ttf}[outsideRank]{/size}" xpos 1092 ypos 186


    vbox xalign 0.5 yalign 1.0:
        imagebutton:
            idle "gui/mapUI.png"

    vbox xalign 0.308 yalign 1.0:
        imagebutton:
            idle "gui/mapUIMission.png"
            hover "gui/mapUIMission-hover.png"
            action Jump("landgrabDeny")


    vbox xalign 0.404 yalign 1.0:
        imagebutton:
            idle "gui/mapUIStatus.png"
            hover "gui/mapUIStatus-hover.png"
            if mapSelectButton == 2:
                action SetVariable("mapSelectButton", 0)
            else:
                action SetVariable("mapSelectButton", 2)
    if mapSelectButton == 2:
        frame:
            xpadding 22
            pos (467, 565)
            has vbox
            textbutton "{font=fonts/freshmarker.ttf}Quests{/font}":

                action SetVariable("mapSelectButton", 0), Jump("quests")
            textbutton "{font=fonts/freshmarker.ttf}Lore{/font}":
                action SetVariable("mapSelectButton", 0), Jump("lore")
            textbutton "{font=fonts/freshmarker.ttf}Status{/font}":
                action SetVariable("mapSelectButton", 0), Jump("status")


    vbox xalign 0.503 yalign 1.0:
        imagebutton:
            idle "gui/mapUIItems.png"
            hover "gui/mapUIItems-hover.png"
            if mapSelectButton != 3:
                action SetVariable("mapSelectButton", 3)
            else:
                action SetVariable("mapSelectButton", 0)
    if mapSelectButton == 3:
        frame:
            xpadding 15
            pos (582, 565)
            has vbox
            textbutton "{font=fonts/freshmarker.ttf}Gadgets{/font}":

                clicked SetVariable("mapSelectButton", 0), Jump("desk")
            textbutton "{font=fonts/freshmarker.ttf}Outfits{/font}":
                action SetVariable("mapSelectButton", 0), Jump("outfits")
            textbutton "{font=fonts/freshmarker.ttf}Items{/font}":
                action SetVariable("mapSelectButton", 0), Jump("items")


    vbox xalign 0.6 yalign 1.0:
        imagebutton:
            idle "gui/mapUIExplore.png"
            hover "gui/mapUIExplore-hover.png"
            action Jump("landgrabDeny")


    vbox xalign 0.69 yalign 1.0:
        imagebutton:
            idle "gui/mapUINight.png"
            hover "gui/mapUINight-hover.png"
            if tod == 1:
                action Jump("jobReport")
            else:
                action Jump("nightCycle")

label landgrabDeny:
    y "Maybe not during a landgrab."
    jump worldmap


screen mapButtonsRaidFinale:
    if 20 <= task26Stage <= 21:
        vbox xalign 0.2 yalign 0.2:
            imagebutton:
                idle "gui/mapUISideQuest.png"
                hover "gui/mapUISideQuest-hover.png"
                if task26Stage == 20:
                    action Jump("task26")
                if task26Stage == 21:
                    if mapSpy4Selected == True:
                        action SetVariable("searchTarget", 1), Jump("finaleAirportAssault")
                    elif mapSpy5Selected:
                        action SetVariable("searchTarget", 1), Jump("finaleAirportAssault")
                    elif mapSpy6Selected:
                        action SetVariable("searchTarget", 1), Jump("finaleAirportAssault")
                    elif mapSpy0Selected:
                        action SetVariable("searchTarget", 1), Jump("finaleAirportAssault")
    if task26Stage == 29:
        vbox xalign 0.2 yalign 0.2:
            imagebutton:
                idle "gui/mapUISideQuest.png"
                hover "gui/mapUISideQuest-hover.png"
                action Jump("task26")



    vbox xalign 0.5 yalign 1.0:
        imagebutton:
            idle "gui/mapUI.png"

    vbox xalign 0.308 yalign 1.0:
        imagebutton:
            idle "gui/mapUIMission.png"
            hover "gui/mapUIMission-hover.png"
            action Jump("landgrabDeny")


    vbox xalign 0.404 yalign 1.0:
        imagebutton:
            idle "gui/mapUIStatus.png"
            hover "gui/mapUIStatus-hover.png"
            if mapSelectButton == 2:
                action SetVariable("mapSelectButton", 0)
            else:
                action SetVariable("mapSelectButton", 2)
    if mapSelectButton == 2:
        frame:
            xpadding 22
            pos (467, 565)
            has vbox
            textbutton "{font=fonts/freshmarker.ttf}Quests{/font}":

                action SetVariable("mapSelectButton", 0), Jump("quests")
            textbutton "{font=fonts/freshmarker.ttf}Lore{/font}":
                action SetVariable("mapSelectButton", 0), Jump("lore")
            textbutton "{font=fonts/freshmarker.ttf}Status{/font}":
                action SetVariable("mapSelectButton", 0), Jump("status")


    vbox xalign 0.503 yalign 1.0:
        imagebutton:
            idle "gui/mapUIItems.png"
            hover "gui/mapUIItems-hover.png"
            if mapSelectButton != 3:
                action SetVariable("mapSelectButton", 3)
            else:
                action SetVariable("mapSelectButton", 0)
    if mapSelectButton == 3:
        frame:
            xpadding 15
            pos (582, 585)
            has vbox
            textbutton "{font=fonts/freshmarker.ttf}Gadgets{/font}":

                clicked SetVariable("mapSelectButton", 0), Jump("desk")
            if task26Stage >= 26:
                textbutton "{font=fonts/freshmarker.ttf}Outfits{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("outfits")
            textbutton "{font=fonts/freshmarker.ttf}Items{/font}":
                action SetVariable("mapSelectButton", 0), Jump("items")


    vbox xalign 0.6 yalign 1.0:
        imagebutton:
            idle "gui/mapUIExplore.png"
            hover "gui/mapUIExplore-hover.png"
            action Jump("landgrabDeny")


    vbox xalign 0.69 yalign 1.0:
        imagebutton:
            idle "gui/mapUINight.png"
            hover "gui/mapUINight-hover.png"
            if tod == 1:
                action Jump("jobReportFinale")

    if task26Stage <= 18 or task26Stage == 21:

        if spy0Status == 0:
            vbox xalign 0.39 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap7.png"
                    hover "gui/spyMap7-hover.png"
                    action Jump("spy0MapSelect")
        else:
            vbox xalign 0.39 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap7Disable.png"

        if spy4Status == 0:
            vbox xalign 0.44 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap4.png"
                    hover "gui/spyMap4-hover.png"
                    action Jump("spy4MapSelect")
        else:
            vbox xalign 0.44 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap4Disable.png"


        if spy5Status == -1:
            pass
        elif spy5Status == 0 and task30Stage >= 3:
            vbox xalign 0.49 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap5.png"
                    hover "gui/spyMap5-hover.png"
                    action Jump("spy5MapSelect")
        else:
            vbox xalign 0.49 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap5Disable.png"


        if spy6Status == -1:
            pass
        elif spy6Status == 0 and socialSilva >= 12:
            vbox xalign 0.54 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap6.png"
                    hover "gui/spyMap6-hover.png"
                    action Jump("spy6MapSelect")
        else:
            vbox xalign 0.54 yalign 0.88:
                imagebutton:
                    idle "gui/spyMap6Disable.png"


        if mapSpy0Selected or mapSpy4Selected or mapSpy5Selected or mapSpy6Selected:
            if task26Stage == 18:
                vbox xalign 0.7 yalign 0.735:
                    imagebutton:
                        idle "gui/mapUISideQuest.png"
                        hover "gui/mapUISideQuest-hover.png"
                        if mapSpy4Selected == True:
                            action SetVariable("searchTarget", 1), Jump("finaleMapSelect")
                        elif mapSpy5Selected:
                            action SetVariable("searchTarget", 1), Jump("finaleMapSelect")
                        elif mapSpy6Selected:
                            action SetVariable("searchTarget", 1), Jump("finaleMapSelect")
                        elif mapSpy0Selected:
                            action SetVariable("searchTarget", 1), Jump("finaleMapSelect")
        if mapSpy0Selected or mapSpy4Selected or mapSpy5Selected or mapSpy6Selected:
            if task26Stage == 18:
                vbox xalign 0.3 yalign 0.4:
                    imagebutton:
                        idle "gui/mapUISideQuest.png"
                        hover "gui/mapUISideQuest-hover.png"
                        if mapSpy4Selected == True:
                            action SetVariable("searchTarget", 2), Jump("finaleMapSelect")
                        elif mapSpy5Selected:
                            action SetVariable("searchTarget", 2), Jump("finaleMapSelect")
                        elif mapSpy6Selected:
                            action SetVariable("searchTarget", 2), Jump("finaleMapSelect")
                        elif mapSpy0Selected:
                            action SetVariable("searchTarget", 2), Jump("finaleMapSelect")
        if mapSpy0Selected or mapSpy4Selected or mapSpy5Selected or mapSpy6Selected:
            if task26Stage == 18:
                vbox xalign 0.2 yalign 0.8:
                    imagebutton:
                        idle "gui/mapUISideQuest.png"
                        hover "gui/mapUISideQuest-hover.png"
                        if mapSpy4Selected == True:
                            action SetVariable("searchTarget", 3), Jump("finaleMapSelect")
                        elif mapSpy5Selected:
                            action SetVariable("searchTarget", 3), Jump("finaleMapSelect")
                        elif mapSpy6Selected:
                            action SetVariable("searchTarget", 3), Jump("finaleMapSelect")
                        elif mapSpy0Selected:
                            action SetVariable("searchTarget", 3), Jump("finaleMapSelect")
        if mapSpy0Selected or mapSpy4Selected or mapSpy5Selected or mapSpy6Selected:
            if task26Stage == 18:
                vbox xalign 0.8 yalign 0.2:
                    imagebutton:
                        idle "gui/mapUISideQuest.png"
                        hover "gui/mapUISideQuest-hover.png"
                        if mapSpy4Selected == True:
                            action SetVariable("searchTarget", 4), Jump("finaleMapSelect")
                        elif mapSpy5Selected:
                            action SetVariable("searchTarget", 4), Jump("finaleMapSelect")
                        elif mapSpy6Selected:
                            action SetVariable("searchTarget", 4), Jump("finaleMapSelect")
                        elif mapSpy0Selected:
                            action SetVariable("searchTarget", 4), Jump("finaleMapSelect")


        vbox xalign 0.5 yalign 1.0:
            imagebutton:
                idle "gui/mapUI.png"

        vbox xalign 0.308 yalign 1.0:
            imagebutton:
                idle "gui/mapUIMission.png"
                hover "gui/mapUIMission-hover.png"
                action Jump("landgrabDeny")


        vbox xalign 0.404 yalign 1.0:
            imagebutton:
                idle "gui/mapUIStatus.png"
                hover "gui/mapUIStatus-hover.png"
                if mapSelectButton == 2:
                    action SetVariable("mapSelectButton", 0)
                else:
                    action SetVariable("mapSelectButton", 2)
        if mapSelectButton == 2:
            frame:
                xpadding 22
                pos (467, 565)
                has vbox
                textbutton "{font=fonts/freshmarker.ttf}Quests{/font}":

                    action SetVariable("mapSelectButton", 0), Jump("quests")
                textbutton "{font=fonts/freshmarker.ttf}Lore{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("lore")
                textbutton "{font=fonts/freshmarker.ttf}Status{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("status")


        vbox xalign 0.503 yalign 1.0:
            imagebutton:
                idle "gui/mapUIItems.png"
                hover "gui/mapUIItems-hover.png"
                if mapSelectButton != 3:
                    action SetVariable("mapSelectButton", 3)
                else:
                    action SetVariable("mapSelectButton", 0)
        if mapSelectButton == 3:
            frame:
                xpadding 15
                pos (582, 595)
                has vbox
                textbutton "{font=fonts/freshmarker.ttf}Gadgets{/font}":

                    clicked SetVariable("mapSelectButton", 0), Jump("desk")
                textbutton "{font=fonts/freshmarker.ttf}Items{/font}":
                    action SetVariable("mapSelectButton", 0), Jump("items")


        vbox xalign 0.6 yalign 1.0:
            imagebutton:
                idle "gui/mapUIExplore.png"
                hover "gui/mapUIExplore-hover.png"
                action Jump("landgrabDeny")


        vbox xalign 0.69 yalign 1.0:
            imagebutton:
                idle "gui/mapUINight.png"
                hover "gui/mapUINight-hover.png"
                if tod == 1:
                    action Jump("jobReportFinale")


    if task26Stage == 19:
        vbox xalign 0.565 yalign 0.275:
            imagebutton:
                idle "gui/arrowClub.png"
                hover "gui/arrowClub-hover.png"
                action Jump("task26")


screen finaleChoice:
    vbox xalign 0.25 yalign 0.5:
        imagebutton:
            idle "gui/finaleControl.png"
            hover "gui/finaleControl-hover.png"
            action Jump("ending1")
    vbox xalign 0.75 yalign 0.5:
        imagebutton:
            idle "gui/finaleDisband.png"
            hover "gui/finaleDisband-hover.png"
            action Jump("ending2")

default landgrabTarget = 0
default acesStrength = 58
default punkStrength = 100
default outsidersStrength = 100
default agentsAvailable = 0

screen gangStrengthBarAces:
    add "gui/mapGangs/gangRepGraphic.png" xpos 120 ypos 130
    text "{font=fonts/freshmarker.ttf}{size=+18}Aces{/size}{/font}" xpos 265 ypos 202
    if specialMaggieStatus >= 1:
        add "gui/mapGangs/acesLt1.png" xpos 225 ypos 300
    if specialMelodyStatus >= 1:
        add "gui/mapGangs/acesLt2.png" xpos 275 ypos 300
    if specialCandyStatus >= 1:
        add "gui/mapGangs/acesLt3.png" xpos 325 ypos 300
    bar:
        value acesStrength
        range 100
        left_bar "gui/mapGangs/strFull.png"
        right_bar "gui/mapGangs/strEmpty.png"
        thumb_offset 0
        xysize (198,7)
        xpos 200
        ypos 170

screen gangStrengthBarPunk:
    add "gui/mapGangs/gangRepGraphic.png" xpos 820 ypos 330
    text "{font=fonts/freshmarker.ttf}{size=+18}Drift Punk{/size}{/font}" xpos 885 ypos 402
    if specialDragonStatus >= 1:
        add "gui/mapGangs/punkLt1.png" xpos 923 ypos 500
    if specialTaliaStatus >= 1:
        add "gui/mapGangs/punkLt2.png" xpos 976 ypos 500
    if specialSebStatus == 1:
        add "gui/mapGangs/punkLt3.png" xpos 1031 ypos 500
    bar:
        value punkStrength
        range 100
        left_bar "gui/mapGangs/strFull.png"
        right_bar "gui/mapGangs/strEmpty.png"
        thumb_offset 0
        xysize (198,7)
        xpos 900
        ypos 450

screen gangStrengthBarOutsiders:
    add "gui/mapGangs/gangRepGraphic.png" xpos 820 ypos 130
    text "{font=fonts/freshmarker.ttf}{size=+18}Outsiders{/size}{/font}" xpos 905 ypos 202
    if specialMuffyStatus >= 1:
        add "gui/mapGangs/outsidersLt1.png" xpos 925 ypos 300
    if specialFelicityStatus >= 1:
        add "gui/mapGangs/outsidersLt2.png" xpos 975 ypos 300
    if specialKandStatus >= 1:
        add "gui/mapGangs/outsidersLt3.png" xpos 1030 ypos 300
    bar:
        value outsidersStrength
        range 100
        left_bar "gui/mapGangs/strFull.png"
        right_bar "gui/mapGangs/strEmpty.png"
        thumb_offset 0
        xysize (198,7)
        xpos 900
        ypos 170

label randomAttackAudio:
    $ randAudio = renpy.random.randint(1,3)
    if randAudio == 1:
        play sound "audio/voice/agent/hasAnybodySeenMyFlakJacket.mp3"
    if randAudio == 2:
        play sound "audio/voice/agent/goingInGunsBlazing.mp3"
    if randAudio == 3:
        play sound "audio/voice/agent/locknload.mp3"
    return

label landgrabPlanning:
    if landgrabTarget == 1:
        "The Aces are currently at [acesStrength]%% strength. How many agents do you wish to send?"
        menu:
            "Send 5 agents" if agentsAvailable >= 5:
                call randomAttackAudio from _call_randomAttackAudio
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 5
                $ agentStrength = 15
                show screen gangStrengthBarAces
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ acesStrength -= 1
                    pause 0.003
            "Send 10 agents" if agentsAvailable >= 10:
                call randomAttackAudio from _call_randomAttackAudio_1
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 10
                $ agentStrength = 30
                show screen gangStrengthBarAces
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ acesStrength -= 1
                    pause 0.003
            "Send 20 agents" if agentsAvailable >= 20:
                call randomAttackAudio from _call_randomAttackAudio_2
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 20
                $ agentStrength = 60
                show screen gangStrengthBarAces
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ acesStrength -= 1
                    pause 0.003
            "Back" if True:
                jump worldmap
        if acesStrength <= 45 and specialMelodyStatus == 0:
            pause 0.5
            $ specialMelodyStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarAces
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Aces Lieutenant identified: Melody von Guggen."
        if acesStrength <= 15 and specialCandyStatus == 0:
            pause 0.5
            $ specialCandyStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarAces
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Aces Leader identified: Margaret N."
        elif True:
            pause 1.5
            hide screen gangStrengthBarAces
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
        if acesStrength <= 0:
            $ acesStrength = 0


        $ randLosses = renpy.random.randint(0,3)
        if randLosses == 1:
            $ freedAgents -= 1
        elif randLosses == 2:
            $ freedAgents -= 2
        elif randLosses == 3:
            $ freedAgents -= 3
        if randLosses >= 1:
            "You lost [randLosses] agent(s) to nanobot control during the last attack."
        jump worldmap

    if landgrabTarget == 2:
        "The Drift Punk are currently at [punkStrength]%% strength. How many agents do you wish to send?"
        menu:
            "Send 5 agents" if agentsAvailable >= 5:
                call randomAttackAudio from _call_randomAttackAudio_6
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 5
                $ agentStrength = 15
                show screen gangStrengthBarPunk
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ punkStrength -= 1
                    pause 0.003
            "Send 10 agents" if agentsAvailable >= 10:
                call randomAttackAudio from _call_randomAttackAudio_7
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 10
                $ agentStrength = 30
                show screen gangStrengthBarPunk
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ punkStrength -= 1
                    pause 0.003
            "Send 20 agents" if agentsAvailable >= 20:
                call randomAttackAudio from _call_randomAttackAudio_8
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 20
                $ agentStrength = 60
                show screen gangStrengthBarPunk
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ punkStrength -= 1
                    pause 0.003
            "Back" if True:
                jump worldmap
        if punkStrength <= 70 and specialDragonStatus == 0:
            pause 0.5
            $ specialDragonStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarPunk
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Drift Punk Lieutenant identified: Carla Wong."
        if punkStrength <= 45 and specialTaliaStatus == 0:
            pause 0.5
            $ specialTaliaStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarPunk
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Drift Punk Lieutenant identified: Talia H."
        if punkStrength <= 15 and specialSebStatus == 0:
            pause 0.5
            $ specialSebStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarPunk
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Drift Punk Lieutenant identified: ???"
        elif True:
            pause 1.5
            hide screen gangStrengthBarPunk
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
        if punkStrength <= 0:
            $ punkStrength = 0


        $ randLosses = renpy.random.randint(1,4)
        if randLosses == 1:
            $ freedAgents -= 1
        elif randLosses == 2:
            $ freedAgents -= 2
        elif randLosses == 3:
            $ freedAgents -= 3
        elif randLosses == 4:
            $ freedAgents -= 4
        elif randLosses == 5:
            $ freedAgents -= 5
        if randLosses >= 1:
            "You lost [randLosses] agent(s) to nanobot control during the last attack."
        jump worldmap

    if landgrabTarget == 3:
        "The Outsiders are currently at [outsidersStrength]%% strength. How many agents do you wish to send?"
        menu:
            "Send 5 agents" if agentsAvailable >= 5:
                call randomAttackAudio from _call_randomAttackAudio_3
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 5
                $ agentStrength = 15
                show screen gangStrengthBarOutsiders
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ outsidersStrength -= 1
                    pause 0.003
            "Send 10 agents" if agentsAvailable >= 10:
                call randomAttackAudio from _call_randomAttackAudio_4
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 10
                $ agentStrength = 30
                show screen gangStrengthBarOutsiders
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ outsidersStrength -= 1
                    pause 0.003
            "Send 20 agents" if agentsAvailable >= 20:
                call randomAttackAudio from _call_randomAttackAudio_5
                "Agents" "Go! Go! Go!"
                $ firstLandgrab = True
                $ agentsAvailable -= 20
                $ agentStrength = 60
                show screen gangStrengthBarOutsiders
                while agentStrength > 0:
                    $ agentStrength -= 1
                    $ outsidersStrength -= 1
                    pause 0.003
            "Back" if True:
                jump worldmap
        if outsidersStrength <= 70 and specialMuffyStatus == 0:
            pause 0.5
            $ specialMuffyStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarOutsiders
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Outsiders Lieutenant identified: Muffy Peprich."
            "Muffy Peprich is now available for capture. Send your spies on a mission to The Carnival to capture her."
        if outsidersStrength <= 45 and specialFelicityStatus == 0:
            pause 0.5
            $ specialFelicityStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarOutsiders
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Outsiders Lieutenant identified: Felicity Fences."
        if outsidersStrength <= 15 and specialKandStatus == 0:
            pause 0.5
            $ specialKandStatus = 1
            with d3
            pause 1.5
            hide screen gangStrengthBarOutsiders
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
            "Outsiders Leader identified: The Great Kandinsky."
        elif True:
            pause 1.5
            hide screen gangStrengthBarOutsiders
            hide expression "gui/mapGangs/gangRepGraphic.png"
            hide text
            with d3
        if outsidersStrength <= 0:
            $ outsidersStrength = 0


        $ randLosses = renpy.random.randint(1,3)
        if randLosses == 1:
            $ freedAgents -= 1
        elif randLosses == 2:
            $ freedAgents -= 2
        elif randLosses == 3:
            $ freedAgents -= 3
        if randLosses >= 1:
            "You lost [randLosses] agent(s) to nanobot control during the last attack."
        jump worldmap

    if landgrabTarget == 5:
        "A small group of civillians is scavenging for supplies while the gangs are preoccupied."
        label donateMenu1:
            pass
        menu:
            "Donate food ([resourceFood])" if True:
                if resourceFood >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceFood
                    $ donateReward += 20
                    $ resourceFood = 0
                elif True:
                    pass
                jump donateMenu1
            "Donate water ([resourceWater])" if True:
                if resourceWater >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceWater
                    $ resourceWater = 0
                elif True:
                    pass
                jump donateMenu1
            "Donate toys ([resourceToys])" if True:
                if resourceToys >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceToys
                    $ resourceToys = 0
                elif True:
                    pass
                jump donateMenu1
            "Donate clothes ([resourceClothes])" if True:
                if resourceClothes >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceClothes
                    $ resourceClothes = 0
                elif True:
                    pass
                jump donateMenu1
            "Donate tools ([resourceTools])" if True:
                if resourceTools >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceTools
                    $ resourceTools = 0
                elif True:
                    pass
                jump donateMenu1
            "Finish donating" if True:
                $ landgrabRandomAssist1 = 0
                $ donateReward = donateReward * 2
                $ cash += donateReward
                "The thankful civilians give you $ [donateReward] as a reward."
                if donateReward >= 150:
                    $ medkit += 3
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you {color=#ffeda6}Medkit{/color} x3."
                if donateReward >= 200:
                    $ matsChip += 3
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you {color=#ffeda6}Computer Chip{/color} x3."
                if donateReward >= 250:
                    $ injectorSmall += 1
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you a {color=#ffeda6}Nanobot Injector{/color}."
        $ donateReward = 0
        jump worldmap

    if landgrabTarget == 6:
        "A small group of civillians is scavenging for supplies while the gangs are preoccupied."
        label donateMenu2:
            pass
        menu:
            "Donate food ([resourceFood])" if True:
                if resourceFood >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceFood
                    $ resourceFood = 0
                elif True:
                    pass
                jump donateMenu2
            "Donate water ([resourceWater])" if True:
                if resourceWater >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceWater
                    $ donateReward += 20
                    $ resourceWater = 0
                elif True:
                    pass
                jump donateMenu2
            "Donate toys ([resourceToys])" if True:
                if resourceToys >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceToys
                    $ resourceToys = 0
                elif True:
                    pass
                jump donateMenu2
            "Donate clothes ([resourceClothes])" if True:
                if resourceClothes >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceClothes
                    $ resourceClothes = 0
                elif True:
                    pass
                jump donateMenu2
            "Donate tools ([resourceTools])" if True:
                if resourceTools >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceTools
                    $ resourceTools = 0
                elif True:
                    pass
                jump donateMenu2
            "Finish donating" if True:
                $ landgrabRandomAssist2 = 0
                $ donateReward = donateReward * 2
                $ cash += donateReward
                "The thankful civilians give you $ [donateReward] as a reward."
                if donateReward >= 150:
                    $ magazine += 3
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you {color=#ffeda6}Magazine{/color} x3."
                if donateReward >= 200:
                    $ matsDust += 3
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you {color=#ffeda6}Saltpeter{/color} x3."
                if donateReward >= 250:
                    $ injectorSmall += 1
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you a {color=#ffeda6}Nanobot Injector{/color}."
        $ donateReward = 0
        jump worldmap

    if landgrabTarget == 7:
        "A small group of civillians is scavenging for supplies while the gangs are preoccupied."
        label donateMenu3:
            pass
        menu:
            "Donate food ([resourceFood])" if True:
                if resourceFood >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceFood
                    $ resourceFood = 0
                elif True:
                    pass
                jump donateMenu3
            "Donate water ([resourceWater])" if True:
                if resourceWater >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceWater
                    $ resourceWater = 0
                elif True:
                    pass
                jump donateMenu3
            "Donate toys ([resourceToys])" if True:
                if resourceToys >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceToys
                    $ resourceToys = 0
                elif True:
                    pass
                jump donateMenu3
            "Donate clothes ([resourceClothes])" if True:
                if resourceClothes >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceClothes
                    $ donateReward += 20
                    $ resourceClothes = 0
                elif True:
                    pass
                jump donateMenu3
            "Donate tools ([resourceTools])" if True:
                if resourceTools >= 1:
                    play sound "audio/sfx/donate.mp3"
                    $ donateReward += resourceTools
                    $ resourceTools = 0
                elif True:
                    pass
                jump donateMenu3
            "Finish donating" if True:
                $ landgrabRandomAssist3 = 0
                $ donateReward = donateReward * 2
                $ cash += donateReward
                "The thankful civilians give you $ [donateReward] as a reward."
                if donateReward >= 150:
                    $ intelBoost += 1
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you {color=#ffeda6}Intel{/color} x1."
                if donateReward >= 200:
                    $ matsValu += 1
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you {color=#ffeda6}Valuables{/color} x1."
                if donateReward >= 250:
                    $ injectorSmall += 1
                    play sound "audio/sfx/itemGot.mp3"
                    "They also give you a {color=#ffeda6}Nanobot Injector{/color}."
        $ donateReward = 0
        jump worldmap




label audioConfirmationSam:
    $ randAud = renpy.random.randint(1, 9)
    if randAud == 1:
        play sound "audio/voice/understood1.mp3"
    if randAud == 2:
        play sound "audio/voice/understood2.mp3"
    if randAud == 3:
        play sound "audio/voice/understood3.mp3"
    if randAud == 4:
        play sound "audio/voice/onIt1.mp3"
    if randAud == 5:
        play sound "audio/voice/onIt2.mp3"
    if randAud == 6:
        play sound "audio/voice/onIt3.mp3"
    if randAud == 7:
        play sound "audio/voice/youGotIt1.mp3"
    if randAud == 8:
        play sound "audio/voice/youGotIt2.mp3"
    if randAud == 9:
        play sound "audio/voice/youGotIt3.mp3"
    return

label audioConfirmationClover:
    $ randAud = renpy.random.randint(1, 9)
    if randAud == 1:
        play sound "audio/voice/clover/understood1.mp3"
    if randAud == 2:
        play sound "audio/voice/clover/understood2.mp3"
    if randAud == 3:
        play sound "audio/voice/clover/understood3.mp3"
    if randAud == 4:
        play sound "audio/voice/clover/onIt1.mp3"
    if randAud == 5:
        play sound "audio/voice/clover/onIt2.mp3"
    if randAud == 6:
        play sound "audio/voice/clover/onIt3.mp3"
    if randAud == 7:
        play sound "audio/voice/clover/youGotIt1.mp3"
    if randAud == 8:
        play sound "audio/voice/clover/youGotIt2.mp3"
    if randAud == 9:
        play sound "audio/voice/clover/youGotIt3.mp3"
    return

label audioConfirmationAlex:
    $ randAud = renpy.random.randint(1, 4)
    if randAud == 1:
        play sound "audio/voice/alex/onMyWay1.mp3"
    if randAud == 2:
        play sound "audio/voice/alex/rogerDodger.mp3"
    if randAud == 3:
        play sound "audio/voice/alex/okGotIt.mp3"
    if randAud == 4:
        play sound "audio/voice/alex/onIt.mp3"
    return


default jobEventSam = 0
default jobEventClover = 0
default jobEventAlex = 0

default randomJobCallSpy = 0


label randomJobCall:
    if randomJobCallSpy == 1:
        $ jobEventSam = renpy.random.randint(1,4)
    if randomJobCallSpy == 2:
        $ jobEventClover = renpy.random.randint(1,4)
    if randomJobCallSpy == 3:
        $ jobEventAlex = renpy.random.randint(1,4)
    return

label workBonusMenu:
    if jobEventSam == 4:
        $ jobEventSam = 0
        $ randBonusEvent = renpy.random.randint(1,7)
        if slutLevel >= 3:
            if randBonusEvent == 1:
                sM "[playerName]? I got something here..."
                sM "I found someone who can give me more intel, but wants something in return."
                sM "................."
                sM "He wants me to show my naked breasts..."
                menu:
                    "Show them" if True:
                        $ slutPublic += 1
                        y "Well what are you waiting for?! Show them!"
                        sM "..........."
                        sM "{b}*Sigh*{/b} Yes sir."
                        if slutLevel == 3:
                            $ greenChest = 0
                            $ greenUnder = 0
                            scene black with fade
                            scene bgStreet1
                            show green g21 at ce
                            show scene_camera
                            with qFade
                            s "Well... here you go...."
                            "Gangster" "Oh wow you actually did it...!"
                            "Gangster" "A deal's a deal. Here's the intel."
                            $ samMood -= 5
                            $ randIntel = 45
                            $ intel += 45
                        if slutLevel == 4:
                            $ greenChest = 0
                            $ greenUnder = 0
                            scene black with qFade
                            scene bgStreet1
                            show green g1 at ce
                            show scene_camera
                            with qFade
                            s "You wanted to see boobs? Then you'll get boobs..."
                            "Gangster" "Oh my God! You have the nicest rack in the Aces!"
                            s "About the intel...."
                            "Gangster" "Oh of course! Here it is."
                            $ samMood -= 3
                            $ randIntel = 55
                            $ intel += 55
                        if slutLevel == 5:
                            $ greenChest = 0
                            $ greenUnder = 0
                            scene black with fade
                            scene bgStreet
                            show green g22 at ce
                            show scene_camera
                            with fade
                            s "Feast your eyes on these puppies!"
                            "Gangster" "The tits of a Goddess~....!"
                            "Gangster" "Here's the intel. I'll come find you if I find anymore!"
                            s "Sure, I'll be waiting~...."
                            $ samMood -= 1
                            $ randIntel = 80
                            $ intel += 80
                        scene black
                        with qFade
                        call missionRewardInt from _call_missionRewardInt_20
                        hide green
                        hide scene_camera
                        scene bgMap:
                            zoom 0.5
                        with fade
                        jump worldmap
                    "Don't show them" if True:
                        y "Don't be a floozy, Sam."
                        sM "But I thought...!"
                        sM "Erm... well all right then. I'll tell him no."
                        jump worldmap
            if randBonusEvent == 2:
                sM "Hey [playerName]..?"
                y "What's up, Sam?"
                sM "Well I think I can bring back a little more money, but~..."
                sM "I'll have to do some sexy dancing for it..."
                menu:
                    "Strip for money" if True:
                        $ slutPublic += 1
                        y "More is money! Time to lose your clothes!"
                        if slutLevel == 3:
                            sM "I guess you're right... I'm not happy about it though."
                            $ greenChest = 0
                            $ greenUnder = 0
                            scene black with fade
                            scene bgStreet
                            show green g21 at ce
                            show scene_camera
                            with fade
                            s "Well... here you go...."
                            "Gangster" "Oh wow you actually did it...!"
                            "Gangster" "Okay a deal's a deal. Here's the intel."
                            $ samMood -= 5
                            $ randMoney = 50
                            $ cash += 50
                            call missionRewardMoney from _call_missionRewardMoney_86
                            jump worldmap
                        if slutLevel == 4:
                            $ greenChest = 0
                            $ greenUnder = 0
                            scene black with fade
                            scene bgStreet1
                            show green g22 at ce
                            show scene_camera
                            with fade
                            s "You wanted to see boobs? Then you'll get boobs..."
                            "Gangster" "Oh my God! You have the nicest rack in the Aces!"
                            s "About the intel...."
                            "Gangster" "Oh of course! Here it is."
                            $ samMood -= 3
                            $ randIntel = 60
                            $ intel += 60
                            call missionRewardInt from _call_missionRewardInt_35
                            jump worldmap
                        if slutLevel == 5:
                            $ greenChest = 0
                            $ greenUnder = 0
                            scene black with fade
                            scene bgStreet
                            show green g22 at ce
                            show scene_camera
                            with fade
                            s "Feast your eyes on these puppies!"
                            "Gangster" "The tits of a Goddess~....!"
                            "Gangster" "Here's the intel. I'll come find you if I find anymore!"
                            s "Sure, I'll be waiting~...."
                            $ samMood -= 1
                            $ randIntel = 70
                            $ intel += 70
                            call missionRewardInt from _call_missionRewardMoney_23
                            jump worldmap
                    "Refuse" if True:
                        y "You can't go showing off your naked body!"
                        sM "Really? But... {i}'you'{/i} saw me naked."
                        sM "I mean.. If you don't want me to, then I approve. I'd rather not, but I expected you to be all for it."
                        sM "I'll refuse the offer then."
                        jump worldmap
            if randBonusEvent == 3:
                sM "This is Sam, reporting in."
                y "Sam? Did something happen?"
                sM "No, just..."
                sM "..........................."
                sM "They dared me to make out with another girl."
                y "What?"
                sM "They want me to kiss one of the girls. I won't get anything for it, but it'll boost my reputation a bit."
                menu:
                    "Kiss the girl" if True:
                        $ slutPublic += 1
                        y "H-hot... lesbian action?"
                        sM "[playerName]..."
                        y "YES!"
                        y "I mean... erm... yes, I think you totally should."
                        sM "I'm not sure I like how quickly you agreed to this, but whatever."
                        sM "It's a fine day to start doubting my sexuality..."
                        $ samMood -= 5
                        $ acesRep += 1
                        call missionRewardRep from _call_missionRewardRep_11
                        jump worldmap
                    "Reject" if True:
                        y "You can't just start kissing everyone you see, Sam."
                        sM "No, I know, but..."
                        y "I know kissing girls is hot, but please suppress your urges."
                        sM "[playerName]..."
                        jump worldmap
            if randBonusEvent == 4 and slutLevel >= 4:
                sM "Hey [playerName], it's me, Sam."
                y "Hello [samNick]. Anything to report?"
                sM "....................."
                sM "Someone wants a blowjob...."
                y "........"
                y "What?"
                sM "One of the gangsters promised me $100 bucks for a blowjob."
                menu:
                    "What are you waiting for?" if True:
                        $ slutPublic += 1
                        y "I don't see the downside to this."
                        sM "But it's a blowjob! That's pretty serious!"
                        y "No it's not. Better get sucking!"
                        y "Start polishing that girthy dickmeat until it glistens and explodes with the furiosity of a vulcano! Raining down on your soft and gentle pale face like the mana from heaven, in your greatest time of need!"
                        sM "Okay jeeze! Fine! I'll suck his dick!"
                        sM "God!"
                        $ greenCum = 1
                        scene black with fade
                        scene bgStreet1
                        show green g20 at ce
                        show scene_camera
                        with qFade
                        "Gangster" "Worth every dollar..."
                        s "...................."
                        hide scene_camera
                        hide green
                        scene black
                        with fade
                        $ samMood -= 5
                        $ cash += 100
                        $ randMoney = 100
                        $ greenCum = 0
                        call missionRewardMoney from _call_missionRewardMoney_58
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Turn him down" if True:
                        y "And have you walk around the base with penisbreath? I don't think so."
                        sM "Okay good, cause I wasn't really feeling lik-..."
                        y "Just imagining you suckle down on somebody else's meat makes me sick!"
                        sM "Er..."
                        y "I couldn't even look at you! {size=+4}You whore!{/size} {size=+8}You floozy!{/size} {size=+12}You common street tart!{/size}"
                        sM "Okay okay! Jeeze... calm down. No blowjobs, got it."
                        jump worldmap
            if randBonusEvent == 5 and slutLevel >= 4:
                sM "[playerName] report in."
                y "Reporting in! What's up [samNick]"
                sM "{b}*Ahem*{/b} Well..."
                sM "..................."
                y "What~...?"
                sM "Wet... wet t-shirt contest..."
                y "Oh... Oooh!"
                sM "Should I?"
                menu:
                    "Hell yeah!" if True:
                        $ greenChest = 99
                        $ greenBottom = 0
                        if greenUnder == 0:
                            $ greenUnder = 1.1
                        $ slutPublic += 1
                        y "YES!"
                        y "Wait do we get anything out of it?"
                        sM "It's a friendly competition between gangs. It just increases my reputation with them a bit."
                        y "Good enough, wet t-shirt contest!"
                        sM "As you wish..."
                        scene bgStreet1
                        show green g2 at ce
                        show scene_camera
                        with fade
                        "Aces" "Go Sam, go Sam, go Sam!"
                        pause
                        hide scene_camera
                        hide green
                        scene black
                        with fade
                        $ acesRep += 1
                        $ punkRep += 1
                        $ outsideRep += 1
                        call missionRewardRep from _call_missionRewardRep_12
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Reject" if True:
                        y "And have them see your perfectly shaped breasts clinging through your wet t-shirt as your gentle nipples poke through the fabric?"
                        sM "Er... yeah pretty much."
                        y "Never! Only I get to behold such majesty!"
                        sM "No? Well okay then."
                        jump worldmap
            if randBonusEvent == 6 and slutLevel >= 4:
                y "Sam?"
                sM "I think I got something here..."
                sM "I just overheard a couple of girls talking, but they headed into a sauna."
                sM "It sounded important, but it's... a mixed gender sauna."
                menu:
                    "Who cares, go in" if True:
                        $ slutPublic += 1
                        sM "Maybe it's just girls in there..."
                        sM "Okay, I'm going in!"
                        "...................................."
                        y "There's also guys in there, aren't there?"
                        s "{b}*Whines*{/b}"
                        $ intel += 20
                        $ randIntel = 20
                        call missionRewardInt from _call_missionRewardInt_23
                        jump worldmap
                    "Don't follow" if True:
                        y "Too bad. Don't follow them."
                        sM "Really? But it sounds like a good way to get some intel."
                        y "At the cost of you exposing yourself to strangers!"
                        sM "........................"
                        jump worldmap
            if randBonusEvent == 7 and slutLevel >= 5:
                "EVENT NOT VISIBLE TO PLAYER"
            elif True:
                sM "Sam reporting in. I... may have an opportunity."
                sM "Just got a request to show my tits. Should I?"
                menu:
                    "Go for it" if True:
                        $ slutPublic += 1
                        y "Will you get anything out of it?"
                        sM "A little bit of money. They also promised me some intel if I did it."
                        y "Then go right ahead."
                        sM "All right... naked tits seem to have a way of making guys talk..."
                        $ greenChest = 0
                        $ greenUnder = 0
                        scene black with qFade
                        scene bgStreet1
                        show green g22 at ce
                        show scene_camera
                        with fade
                        s "Here you go you guys~...."
                        "Gangsters" "Wooo! Go Sammy!"
                        hide green
                        hide scene_camera
                        scene black
                        with fade

                        $ cash += 40
                        $ randMoney = 40
                        call missionRewardMoney from _call_missionRewardMoney_59

                        $ intel += 35
                        $ randIntel = 35
                        call missionRewardInt from _call_missionRewardInt_24
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        $ greenChest = greenChestSet
                        $ greenUnder = greenUnderSet
                        jump worldmap
                    "Reject" if True:
                        y "Nah, but give 'em a slight hint that you {i}'might'{/i} do in the future and leave them a false sense of hope."
                        sM "That's evil..."
                        jump worldmap

    if jobEventClover == 4:
        $ jobEventClover = 0
        $ randBonusEvent = renpy.random.randint(1,7)
        if slutLevel >= 3:
            if randBonusEvent == 1:
                cM "Clover here."
                y "Coming in loud and clear."
                cM "This one guy promised me some intel in return for..."
                cM "............."
                cM "{b}*Sighs*{/b} Motorboating my tits."
                menu:
                    "Do it" if True:
                        $ slutPublic += 1
                        $ redUnder = 0
                        $ redChest = 0
                        y "We need all the intel we can get! Let him!"
                        cM "Ugh... {i}'so'{/i} not cool. Fine whatever, I'll let him..."
                        scene bgStreet1
                        show red r10 at ce
                        show scene_camera
                        with fade
                        c "{b}*Scoffs*{/b} Happy now?"
                        "Gangster" "I've never been so happy in my life!"
                        hide red
                        hide scene_camera
                        scene black
                        with fade
                        $ cloverMood -= 5
                        $ randIntel = 80
                        $ intel += 80
                        $ redUnder = redUnderSet
                        $ redChest = redChestSet
                        call missionRewardInt from _call_missionRewardInt_25
                        jump worldmap
                    "Don't do it" if True:
                        y "What a weirdo."
                        cM "That's what I thought."
                        y "Tell him no. Your tits are not for motorboating."
                        cM "Unless it's you...?"
                        y "Exactly!"
                        jump worldmap
            if randBonusEvent == 2:
                cM "I got an opportunity here."
                cM "An amateur photographer wannabe wants to photograph me in lingerie for money."
                menu:
                    "Agree to photoshoot" if True:
                        $ slutPublic += 1
                        $ redChest = 0
                        $ redBottom = 0
                        $ redUnder = 7
                        $ redArms = 5
                        $ redBlush = 1
                        y "Hot."
                        cM ".................."
                        y "Bring home the money!"
                        cM "Fine..."
                        scene bgStreet1
                        show red r10 at ce
                        show scene_camera
                        with fade
                        "Gangster" "Yes, you are rocking it!"
                        c "Did we have to do it outside...?"
                        pause
                        hide red
                        hide scene_camera
                        scene black
                        with fade
                        $ cloverMood -= 5
                        $ randMoney = 80
                        $ cash += 80
                        $ redChest = redChestSet
                        $ redBottom = redBottomSet
                        $ redUnder = redUnderSet
                        $ redArms = 1
                        $ redBlush = 0
                        call missionRewardMoney from _call_missionRewardMoney_60
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Refuse" if True:
                        y "Hey, nobody is allowed to photograph you in your underwear but me!"
                        cM "I figured you'd say that. All right, I'll tell him no."
                        jump worldmap
            if randBonusEvent == 3:
                y "Clover?"
                cM "So er..."
                cM "I accidentally spilled some milk over my top and it's becoming see through..."
                y "Nice."
                cM "Should I quickly go change and walk around like this for a while?"
                cM "It might raise my reputation around town."
                menu:
                    "Don't change" if True:
                        $ slutPublic += 1
                        $ redChest = 99
                        $ redUnder = 0
                        y "Don't be silly. Don't change and be sure to show off a bit!"
                        cM "All right, I'm already drawing some attention."
                        scene bgStreet1
                        show red r1 at ce
                        show scene_camera
                        with fade
                        "Gangster" "WOAH CLOVER!"
                        "Gangster" "Niiiice...!"
                        pause
                        hide scene_camera
                        hide red
                        scene black
                        with fade
                        $ redChest = redChestSet
                        $ redUnder = redUnderSet
                        $ cloverMood -= 5
                        $ acesRep += 1
                        $ punkRep += 1
                        $ outsideRep += 1
                        call missionRewardRep from _call_missionRewardRep_13
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Change" if True:
                        y "Have you no shame! Of course you're gonna go change!"
                        cM "But..."
                        y "Change! Can't have you walk around half decent!"
                        cM "Fine..."
                        jump worldmap
            if randBonusEvent == 4 and slutLevel >= 4:
                cM "Clover here. Someone is offering me $120 for a boobjob."
                cM "..............."
                cM "Should I...?"
                menu:
                    "Yes" if True:
                        $ slutPublic += 1
                        $ redChest = 0
                        $ redUnder = 0
                        $ redCum = 1
                        y "Money for lying down and doing nothing. Go for it!"
                        cM "I can't believe I'm doing this..."
                        scene bgStreet1
                        show red r4 at ce
                        show scene_camera
                        with fade
                        c "Ew...."
                        "Gangster" "Wow Clover. I never knew you were such a whore!"
                        c "................"
                        y "What a jerk..."
                        pause 1.0
                        y "You should visit him more often!"
                        c r38 "..........."
                        scene black with fade
                        $ cloverMood -= 5
                        $ cash += 140
                        $ randMoney = 140
                        $ redChest = redChestSet
                        $ redUnder = redUnderSet
                        $ redCum = 0
                        call missionRewardMoney from _call_missionRewardMoney_61
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Turn him down" if True:
                        y "Well you 'are' the boobjob queen."
                        y "But we can't have you wasting your talents on just anyone! Refuse the offer."
                        cM "All right, I will."
                        jump worldmap
            if randBonusEvent == 5 and slutLevel >= 4:
                cM "Hey [playerName]. I got something here, but...."
                cM "Erm... there's a video chat between the 3 biggest gangs in the city... "
                y "And?"
                cM "Well I was just thinking..."
                cM "What if I flashed my tits on livestream?"
                menu:
                    "Do it!" if True:
                        $ slutPublic += 1
                        y "That's a great idea!"
                        y "That has got to increase your reputation with the gangs a bit!"
                        cM "Okay... Okay, I'll do it!"
                        $ acesRep += 1
                        $ punkRep += 1
                        $ outsideRep += 1
                        call missionRewardRep from _call_missionRewardRep_14
                        jump worldmap
                    "Don't do it" if True:
                        y "No! No tit flashing, bad Clover!"
                        cM "But it will be some quick easy reputat-..."
                        y "You don't want to have a reputation of being quick and easy! Bad Clover!"
                        cM "All right, if you say so."
                        jump worldmap
            if randBonusEvent == 6 and slutLevel >= 4:
                cM "I think I can score a little extra intel."
                y "That's good. What do you have?"
                cM "I'm at a spa and just overheard some gangsters drop some info."
                cM "I think I can get some extra intel out of them if I offer a massage~..."
                menu:
                    "Do it" if True:
                        $ slutPublic += 1
                        y "Sounds like an easy way to get intel. Do it."
                        cM "Understood."
                        $ intel += 10
                        $ randIntel = 10
                        call missionRewardInt from _call_missionRewardInt_26
                        jump worldmap
                    "Don't" if True:
                        y "Leave them for now. I'm sure another chance will come around."
                        cM "If you say so."
                        jump worldmap
            if randBonusEvent == 7 and slutLevel >= 5:
                cM "Er..."
                y "Yeah?"
                cM "I've been offered $1.000 to star in a bondage show~...."
                cM "They're gonna undress me and tie me up."
                y "Aaaand fuck you?"
                cM "I have no idea..."
                menu:
                    "Do it" if True:
                        $ slutPublic += 1
                        y "Sounds like easy money. Go be a play toy for a while."
                        cM "All right then."
                        $ cash += 1000
                        $ randMoney = 1000
                        call missionRewardMoney from _call_missionRewardMoney_97
                    "Don't" if True:
                        y "Sounds like you're about to get gangbanged. Refuse."
                        cM "Might be for the best."
                        jump worldmap
            elif True:
                cM "Clover here. Would it be okay if I showed my tits off a bit today?"
                y "Okay...?"
                cM "There's a good atmosphere here today. I bet I could get some loose lips talking~..."
                menu:
                    "Go for it" if True:
                        $ slutPublic += 1
                        $ redChest = 0
                        $ redUnder = 0
                        y "If you think it will help, go for it."
                        cM "All right, got it."
                        scene black with fade
                        scene bgStreet1
                        show red r22 at ce
                        show scene_camera
                        with qFade
                        c "Check this out boys~...."
                        "Gangsters" "Clover! Clover! Clover!"
                        scene black with fade

                        $ cash += 35
                        $ randMoney = 35
                        call missionRewardMoney from _call_missionRewardMoney_62

                        $ intel += 15
                        $ randIntel = 15
                        call missionRewardInt from _call_missionRewardInt_27
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Reject" if True:
                        y "Nnnnnnnnnnnnnnnnnope."
                        cM "No?"
                        y "Nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn-....{nw}"
                        cM "Ugh... weirdo."
                        jump worldmap


    if jobEventAlex == 4:
        $ jobEventAlex = 0
        $ randBonusEvent = renpy.random.randint(1,7)
        if slutLevel >= 3:
            if randBonusEvent == 1:
                aM "Alex here!"
                y "Alex? What's up?"
                aM "So erm..."
                aM "There's this one really sexy swimsuit for sale at the mall and I've just been dared to try it on."
                aM "In return the guy promised to share some intel."
                menu:
                    "Do it" if True:
                        $ slutPublic += 1
                        $ yellowChest = 0
                        $ yellowBottom = 0
                        $ yellowUnder = 7
                        y "Go for it. What kind of swimsuit?"
                        aM "Erm... A one piece thong swimsuit..."
                        y "..........."
                        y "Not gonna lie, I'm kinda jealous that I'm not there to see it."
                        aM "Check the camera, I'll go put it on!"
                        scene black with fade
                        scene bgStreet1
                        show yellow at ce
                        show scene_camera
                        with qFade
                        a "So how do I look?"
                        "Gangster" "Nghhhh~...!"
                        scene black with fade
                        $ yellowChest = yellowChestSet
                        $ yellowBottom = yellowBottomSet
                        $ yellowUnder = yellowUnderSet
                        $ alexMood -= 5
                        $ randIntel = 45
                        $ intel += 45
                        call missionRewardInt from _call_missionRewardInt_28
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Don't do it" if True:
                        y "Swimsuits are for swimming and I don't think you'll be doing any swimming."
                        y "So no. Don't put on the swimsuit."
                        aM "Okay, if you say so, [playerName]."
                        jump worldmap
            if randBonusEvent == 2:
                aM "Hey [playerName]. There's this one super sketchie guy who says he'll pay me $50 if he can smell my feet!"
                y "................."
                y "What?"
                aM "It's weird, but...{w} It's still 50 bucks."
                menu:
                    "Agree" if True:
                        $ slutPublic += 1
                        y "Why couldn't it be something normal..."
                        y "Fine, go for it. We'll need the money and just never speak of it again."
                        aM "Okay~..."
                        $ alexMood -= 5
                        $ randMoney = 50
                        $ cash += 50
                        call missionRewardMoney from _call_missionRewardMoney_63
                        jump worldmap
                    "Refuse" if True:
                        y "Alex that's super weird. Get out of there now."
                        aM "No feet smelling?"
                        y "No feet smelling."
                        jump worldmap
            if randBonusEvent == 3:
                aM "What is... 'twerking'?"
                y "What?"
                aM "I've been asked to do some twerking for a diplomatic missions between the gangs."
                menu:
                    "Do it" if True:
                        $ slutPublic += 1
                        y "I have no idea what it is, but I'm sure you can look it up online."
                        y "So do it."
                        aM "Aw... okay...~"
                        $ alexMood -= 5
                        $ acesRep += 1
                        $ punkRep += 1
                        $ outsideRep += 1
                        call missionRewardRep from _call_missionRewardRep_15
                        jump worldmap
                    "Don't do it" if True:
                        y "Twerking...? That sounds painful. Best refuse."
                        a "All right."
                        jump worldmap
            if randBonusEvent == 4 and slutLevel >= 4:
                aM "You know those buttjobs we've been practising?"
                y "Yeees...?"
                aM "Someone here is willing to pay for one."
                y "Really? How much is he offering?"
                aM "A hundred bucks."
                menu:
                    "Agree" if True:
                        $ slutPublic += 1
                        y "Money for lying down and doing nothing. Go for it!"
                        aM "But... for a stranger...? I'll do it [playerName], but I don't like it!"
                        aM "......................"
                        aM "Okay maybe I like it a little!{w} But just a little bit!"
                        scene black with fade
                        show expression "gui/bonusButtjob.jpg" with fade
                        pause
                        scene black
                        $ alexMood -= 5
                        $ cash += 100
                        $ randMoney = 100
                        call missionRewardMoney from _call_missionRewardMoney_64
                        jump worldmap
                    "Turn him down" if True:
                        y "Buttjobs are a rare treasure, not meant to be given out all willy nilly!"
                        a "{b}*Giggle*{/b} You said willy!"
                        y "Turn him down, Alex. We'll make money some other way."
                        jump worldmap
            if randBonusEvent == 5 and slutLevel >= 4:
                aM "I get to be a waitress!"
                y "You already are a waitress."
                aM "But now I get to do it at a party!"
                aM "Hand out cocktails, cigarettes and snacks!"
                y "Okay.... what's the catch?"
                aM "Oh... right, I have to do it naked."
                menu:
                    "Do it" if True:
                        $ slutPublic += 1
                        call undressAlex from _call_undressAlex_12
                        $ yellowBottom = 99
                        y "Hot. I'd say, do it."
                        aM "I don't get anything out of it really, except a reputation boost."
                        y "That's worth it. Go for it."
                        scene bgCastle
                        show yellow at ce
                        show scene_camera
                        with fade
                        pause
                        a "Sigars! Cigarettes!"
                        "Gangster" "Hey hottie... are you on the menu?"
                        a "Tony is that you? How's your girlfriend?"
                        "Gangster" "A-Alex?! Er.. you never saw me here, okay?"
                        scene black with fade
                        $ acesRep += 1
                        $ punkRep += 1
                        $ outsideRep += 1
                        call missionRewardRep from _call_missionRewardRep_16
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Don't do it" if True:
                        y "Naked waitresses?!"
                        y "How sleezy!"
                        aM "But [playerName]...? Aren't we-..."
                        y "The answer is no."
                        jump worldmap
            if randBonusEvent == 6 and slutLevel >= 4:
                aM "Stuffed mouths don't talk."
                y "....................."
                y "What are you, a philosopher?"
                aM "I heard some bigshots say that. They're looking for some girls to give them blowjobs as they talk about their upcoming heist."
                y "Oooh..."
                menu:
                    "Give them a blowjob" if True:
                        $ slutPublic += 1
                        call undressAlex from _call_undressAlex_13
                        $ yellowCum = 1
                        y "Get into that meeting. If you have to suck some dick for it, do it."
                        aM "Are you sure...?"
                        y "Gaining valuable intel in return a 5 minutes blowjob? I'd say that's worth it."
                        aM "If you say so..."
                        scene bgStreet1
                        show yellow y20 at ce
                        show scene_camera
                        with fade
                        "Gangster" "That's a good girl, Alex."
                        "Gangster" "Best keep this up. We've got loads more of jummy cum for you~..."
                        a "........................."
                        scene black with fade
                        $ alexMood -= 10
                        $ intel += 150
                        $ randIntel = 150
                        call missionRewardInt from _call_missionRewardInt_29
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        $ yellowCum = 0
                        jump worldmap
                    "Don't give them a blowjob" if True:
                        y "It can't be that big of a heist if they let sluts into their secret meetings. Don't do it."
                        aM "Phew~... Okay!"
                        jump worldmap
            if randBonusEvent == 7 and slutLevel >= 5:
                "EVENT NOT VISIBLE TO PLAYER"
            elif True:
                aM "Boobies on display!"
                y "Huh?"
                aM "It's hot and some of the other girls are also doing it."
                aM "I've been dared to take off my top and flash my tits for a bit of money and intel."
                menu:
                    "Go for it" if True:
                        $ slutPublic += 1
                        y "If you think it will help, go for it."
                        aM "Bouncing boobies on display!"
                        $ yellowChest = 0
                        $ yellowUnder = 0
                        scene bgStreet1
                        show yellow at ce
                        show scene_camera
                        with fade
                        a "Bounce bounce bounce!"
                        "You hear a crowd of cheering gangsters in the backgrounds."
                        scene black with fade
                        $ yellowChest = yellowChestSet
                        $ yellowUnder = yellowUnderSet

                        $ cash += 40
                        $ randMoney = 40
                        call missionRewardMoney from _call_missionRewardMoney_65

                        $ intel += 15
                        $ randIntel = 15
                        call missionRewardInt from _call_missionRewardInt_30
                        scene bgMap:
                            zoom 0.5
                        with qFade
                        jump worldmap
                    "Reject" if True:
                        y "Seeing a good pair of tits is like having a fine wine."
                        y "You can't just whip them out whenever!"
                        a "So... No boobies on display then?"
                        y "Not today!"
                        jump worldmap
    jump worldmap



default spyPhoto = 0
default spyPhotoView = 0
default photoInterfaceStage = 0
default photoPage = 1
default samPic = 0
default shrineRestored = 0
default tentaclePic = False

screen gPhotosO1:
    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/missionScreen/exitButton2.png"
            hover "gui/missionScreen/exitButton2-hover.png"
            action Jump("items")

image picMaggie = "gui/photos/other/picMaggie.jpg"
image picTalia = "gui/photos/other/picTalia.jpg"
image picCarla = "gui/photos/other/picCarla.jpg"
image picMuffy = "gui/photos/other/picMuffy.jpg"
image picFelicity = "gui/photos/other/picFelicity.jpg"
image picMelody = "gui/photos/other/picMelody.jpg"
image picSam0 = "gui/photos/other/picSam0.jpg"
image picSam1 = "gui/photos/other/picSam1.jpg"
image picBlow = "gui/photos/other/picBlow.jpg"
image picTentacle = "gui/photos/other/picTentacle.jpg"

screen photoInterfaceStage:
    if photoInterfaceStage == 1:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picMaggie.jpg"
            hover "gui/photos/other/picMaggie.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 2:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picCarla.jpg"
            hover "gui/photos/other/picCarla.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 3:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picMuffy.jpg"
            hover "gui/photos/other/picMuffy.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 4:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picTalia.jpg"
            hover "gui/photos/other/picTalia.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 5:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picFelicity.jpg"
            hover "gui/photos/other/picFelicity.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 6:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picMelody.jpg"
            hover "gui/photos/other/picMelody.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 7:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picClerk.jpg"
            hover "gui/photos/other/picClerk.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 8:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picClaus.jpg"
            hover "gui/photos/other/picClaus.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 9:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picSilva.jpg"
            hover "gui/photos/other/picSilva.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 10:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picKim.jpg"
            hover "gui/photos/other/picKim.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 11:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picBritney.jpg"
            hover "gui/photos/other/picBritney.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 12:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picBlow.jpg"
            hover "gui/photos/other/picBlow.jpg"
            action SetVariable("photoInterfaceStage", 0)
    if photoInterfaceStage == 13:
        imagebutton:
            xalign 0.5 yalign 0.5
            idle "gui/photos/other/picTentacle.jpg"
            hover "gui/photos/other/picTentacle.jpg"
            action SetVariable("photoInterfaceStage", 0)

screen photoAlbum:
    add "gui/photos/bgPhoto.jpg"


    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/missionScreen/exitButton2.png"
            hover "gui/missionScreen/exitButton2-hover.png"
            action Hide("photoInterfaceStage"), Jump("items")

    vbox xalign 0.95 yalign 0.95:
        imagebutton:
            idle "gui/photos/photoNxt.png"
            hover "gui/photos/photoNxt-hover.png"
            if photoPage == 1:
                action SetVariable("photoPage", 2), Show("photoInterfaceStage")
            if photoPage == 2:
                action SetVariable("photoPage", 1), Show("photoInterfaceStage")

    if photoPage == 1:
        if specialMaggieStatus >= 3:
            imagebutton:
                xalign 0.15 yalign 0.217
                idle "gui/photos/other/picMaggiemini.jpg"
                hover "gui/photos/other/picMaggiemini-hover.jpg"
                action SetVariable("photoInterfaceStage", 1), Show("photoInterfaceStage")

        if specialDragonStatus >= 3 or carlaSocial >= 1:
            imagebutton:
                xalign 0.375 yalign 0.217
                idle "gui/photos/other/picCarlamini.jpg"
                hover "gui/photos/other/picCarlamini-hover.jpg"
                action SetVariable("photoInterfaceStage", 2), Show("photoInterfaceStage")

        if specialMuffyStatus >= 3 or muffySocial >= 1:
            imagebutton:
                xalign 0.638 yalign 0.217
                idle "gui/photos/other/picMuffymini.jpg"
                hover "gui/photos/other/picMuffymini-hover.jpg"
                action SetVariable("photoInterfaceStage", 3), Show("photoInterfaceStage")

        if specialTaliaStatus >= 3:
            imagebutton:
                xalign 0.863 yalign 0.217
                idle "gui/photos/other/picTaliamini.jpg"
                hover "gui/photos/other/picTaliamini-hover.jpg"
                action SetVariable("photoInterfaceStage", 4), Show("photoInterfaceStage")

        if specialFelicityStatus >= 3:
            imagebutton:
                xalign 0.15 yalign 0.801
                idle "gui/photos/other/picFelicitymini.jpg"
                hover "gui/photos/other/picFelicitymini-hover.jpg"
                action SetVariable("photoInterfaceStage", 5), Show("photoInterfaceStage")

        if task26Stage >= 22:
            imagebutton:
                xalign 0.375 yalign 0.801
                idle "gui/photos/other/picMelodymini.jpg"
                hover "gui/photos/other/picMelodymini-hover.jpg"
                action SetVariable("photoInterfaceStage", 6), Show("photoInterfaceStage")

        if picQuest10 == 3:
            imagebutton:
                xalign 0.638 yalign 0.802
                idle "gui/photos/other/picClerkmini.jpg"
                hover "gui/photos/other/picClerkmini-hover.jpg"
                action SetVariable("photoInterfaceStage", 7), Show("photoInterfaceStage")

        if photoClaus == True:
            imagebutton:
                xalign 0.863 yalign 0.802
                idle "gui/photos/other/picClausmini.jpg"
                hover "gui/photos/other/picClausmini-hover.jpg"
                action SetVariable("photoInterfaceStage", 8), Show("photoInterfaceStage")

    if photoPage == 2:
        if socialSilva >= 12:
            imagebutton:
                xalign 0.15 yalign 0.217
                idle "gui/photos/other/picSilvamini.jpg"
                hover "gui/photos/other/picSilvamini-hover.jpg"
                action SetVariable("photoInterfaceStage", 9), Show("photoInterfaceStage")
        if socialKim >= 10:
            imagebutton:
                xalign 0.375 yalign 0.217
                idle "gui/photos/other/picKimmini.jpg"
                hover "gui/photos/other/picKimmini-hover.jpg"
                action SetVariable("photoInterfaceStage", 10), Show("photoInterfaceStage")
        if task26Stage >= 11:
            imagebutton:
                xalign 0.638 yalign 0.217
                idle "gui/photos/other/picBritneymini.jpg"
                hover "gui/photos/other/picBritneymini-hover.jpg"
                action SetVariable("photoInterfaceStage", 11), Show("photoInterfaceStage")
        if task27Stage >= 1:
            imagebutton:
                xalign 0.863 yalign 0.217
                idle "gui/photos/other/picBlowmini.jpg"
                hover "gui/photos/other/picBlowmini-hover.jpg"
                action SetVariable("photoInterfaceStage", 12), Show("photoInterfaceStage")
        if tentaclePic:
            imagebutton:
                xalign 0.15 yalign 0.802
                idle "gui/photos/other/picTentaclemini.jpg"
                hover "gui/photos/other/picTentaclemini-hover.jpg"
                action SetVariable("photoInterfaceStage", 13), Show("photoInterfaceStage")


screen base:
    zorder 0
    imagemap:
        if month == 10 and 14 <= day <= 31:
            ground "bgs/base/baseHalloween.jpg"
        elif month == 12 and 14 <= day <= 31:
            ground "bgs/base/baseChristmas.jpg"
        else:
            ground "bgs/base/base.jpg"
        hover "bgs/base/base-hover.png"

        hotspot (1008, 168, 175, 464) clicked Jump("lift")
        hotspot (866, 349, 98, 205) clicked Jump("quarters")

        hotspot (649, 581, 310, 120) clicked Jump("prison")
        hotspot (122, 165, 183, 645) clicked Jump("spyCamera")
        hotspot (297, 546, 241, 110) clicked Jump("desk")
        hotspot (770, 380, 75, 140) clicked Jump("creditcards")





image cellNeutral = "bgs/cells/cellNeutral.jpg"
image cellDungeon = "bgs/cells/dungeon.jpg"

screen cellDoor:
    add "bgs/cells/cellDoor.png"


default cellSamLights = 1
default cellSamBed = 1
default cellSamWall = 1
default cellSamShower = 1
default cellSamCurtain = 1
default cellSamBookcase = 0
default cellSamBooks = 0
default cellSamPlug = 0
default cellSamChair = 0
default cellSamCouch = 0
default cellSamDesk = 0
default cellSamDildo = 0
default cellSamGag = 0
default cellSamHandCuffs = 0
default cellSamHangingChair = 0
default cellSamLaptop = 0
default cellSamMirror = 0
default cellSamPainting = 0
default cellSamSexmachine = 0
default cellSamShacklesBed = 0
default cellSamShoes = 0
default cellSamStatue = 0
default cellSamWatch = 0

default cellSamHall1 = 0

default cellSamChrist1 = 0

label fixCellDecor:
    if cellSamWall != 1:
        $ cellSamLights = 1
        $ cellSamBed = 1
        $ cellSamWall = 1
        $ cellSamShower = 1
        $ cellSamCurtain = 1
    show cellSam
    with d3
    jump samCall

label fixCellDecor2:
    if cellCloverWall != 1:
        $ cellCloverLights = 1
        $ cellCloverBed = 1
        $ cellCloverWall = 1
        $ cellCloverShower = 1
        $ cellCloverCurtain = 1
    show cellClover
    with d3
    jump cloverCall

label fixCellDecor3:
    if cellAlexWall != 1:
        $ cellAlexLights = 1
        $ cellAlexBed = 1
        $ cellAlexWall = 1
        $ cellAlexShower = 1
        $ cellAlexCurtain = 1
    show cellAlex
    with d3
    jump cloverCall


default cellSamHappiness = 0
default cellCloverHappiness = 0
default cellAlexHappiness = 0

layeredimage cellSam:
    always:
        "bgs/cells/bgCell.jpg"
    if cellSamHall1 == 1:
        "bgs/cells/bgCellHalloween.jpg"
    if cellSamChrist1 == 1:
        "bgs/cells/bgCellChristmas.jpg"
    if cellSamLights == 1:
        "bgs/cells/cellLights1.png"

    if cellSamWall == 1:
        "bgs/cells/cellWall1.png"

    if cellSamBed == 1:
        "bgs/cells/green/bed1.png"

    if cellSamShacklesBed == 1:
        "bgs/cells/green/shacklesBed.png"

    if cellSamShower == 1:
        "bgs/cells/cellShower1.png"


    if spyRoomRand == 1:
        "bgs/cells/showerWater.png"
    if spyRoomRand == 1:
        "bgs/cells/green/spyShower.png" xalign 0.282 ypos 185
    if spyRoomRand == 1:
        "bgs/cells/showerSteam.png"
    if spyRoomRand == 2 and slutLevel >= 4 and task26Stage <= 18 or task26Stage >= 33:
        "bgs/cells/spyLesb1.png"
    if spyRoomRand == 11:
        "bgs/cells/green/spybondage1.png"


    if cellSamCurtain == 1:
        "bgs/cells/green/cellCurtain1.png"

    if cellSamBookcase == 1:
        "bgs/cells/green/bookcase.png"

    if cellSamBooks == 1:
        "bgs/cells/green/books.png"

    if cellSamPlug == 1:
        "bgs/cells/green/buttPlug.png"

    if cellSamCouch == 1:
        "bgs/cells/green/couch.png"

    if cellSamDesk == 1:
        "bgs/cells/green/desk.png"

    if cellSamChair == 1:
        "bgs/cells/green/chair.png"

    if cellSamDildo == 1:
        "bgs/cells/green/dildo.png"

    if cellSamGag == 1:
        "bgs/cells/green/gag.png"

    if cellSamHandCuffs == 1:
        "bgs/cells/green/handcuffs.png"

    if cellSamHangingChair == 1:
        "bgs/cells/green/hangingChair.png"

    if cellSamLaptop == 1:
        "bgs/cells/green/laptop.png"

    if cellSamMirror == 1:
        "bgs/cells/green/mirror.png"

    if cellSamPainting == 1:
        "bgs/cells/green/painting.png"

    if cellSamSexmachine == 1:
        "bgs/cells/green/sexmachine.png"

    if cellSamShoes == 1:
        "bgs/cells/green/shoes.png"

    if cellSamStatue == 1:
        "bgs/cells/green/statue.png"

    if cellSamWatch == 1:
        "bgs/cells/green/watch.png"

    if cellSamHall1 == 1:
        "bgs/cells/halloween1.png"

    if cellSamChrist1 == 1:
        "bgs/cells/christmas1.png"

screen cellSamDeco:

    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("samCall")

    vbox xalign 0.01 yalign 0.98:
        imagebutton:
            idle "bgs/cells/cellLights1bt.png"
            hover "bgs/cells/cellLights1bt-hover.png"
            if cellSamLights == 0:
                action SetVariable("cellSamLights", 1)
            else:
                action SetVariable("cellSamLights", 0)










    vbox xalign 0.11 yalign 0.98:
        imagebutton:
            idle "bgs/cells/green/curtain1bt.png"
            hover "bgs/cells/green/curtain1bt-hover.png"
            if cellSamCurtain == 1 and task5Nudes:
                action SetVariable("cellSamCurtain", 2)
            elif cellSamCurtain == 2 and task5Nudes:
                action SetVariable("cellSamCurtain", 1)

    if cellSamBookcase >= 1:
        vbox xalign 0.16 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/bookcase1bt.png"
                hover "bgs/cells/green/bookcase1bt-hover.png"
                if cellSamBookcase == 1:
                    action SetVariable("cellSamBookcase", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamBookcase == 2:
                    action SetVariable("cellSamBookcase", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamBooks >= 1:
        vbox xalign 0.21 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/books1bt.png"
                hover "bgs/cells/green/books1bt-hover.png"
                if cellSamBooks == 1:
                    action SetVariable("cellSamBooks", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamBooks == 2:
                    action SetVariable("cellSamBooks", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamPlug >= 1:
        vbox xalign 0.26 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/plug1bt.png"
                hover "bgs/cells/green/plug1bt-hover.png"
                if cellSamPlug == 1:
                    action SetVariable("cellSamPlug", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamPlug == 2:
                    action SetVariable("cellSamPlug", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamChair >= 1:
        vbox xalign 0.31 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/chair1bt.png"
                hover "bgs/cells/green/chair1bt-hover.png"
                if cellSamChair == 1:
                    action SetVariable("cellSamChair", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamChair == 2:
                    action SetVariable("cellSamChair", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamCouch >= 1:
        vbox xalign 0.36 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/couch1bt.png"
                hover "bgs/cells/green/couch1bt-hover.png"
                if cellSamCouch == 1:
                    action SetVariable("cellSamCouch", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                if cellSamCouch == 2:
                    action SetVariable("cellSamCouch", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamDesk >= 1:
        vbox xalign 0.41 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/desk1bt.png"
                hover "bgs/cells/green/desk1bt-hover.png"
                if cellSamDesk == 1:
                    if cellSamLaptop != 1 and cellSamWatch != 1:
                        action SetVariable("cellSamDesk", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamDesk == 2:
                    action SetVariable("cellSamDesk", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamHangingChair >= 1:
        vbox xalign 0.46 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/hangingChair1bt.png"
                hover "bgs/cells/green/hangingChair1bt-hover.png"
                if cellSamHangingChair == 1:
                    action SetVariable("cellSamHangingChair", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamHangingChair == 2:
                    action SetVariable("cellSamHangingChair", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamLaptop >= 1:
        vbox xalign 0.51 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/laptop1bt.png"
                hover "bgs/cells/green/laptop1bt-hover.png"
                if cellSamLaptop == 1:
                    action SetVariable("cellSamLaptop", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamLaptop == 2:
                    action SetVariable("cellSamLaptop", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamMirror >= 1:
        vbox xalign 0.56 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/mirror1bt.png"
                hover "bgs/cells/green/mirror1bt-hover.png"
                if cellSamMirror == 1:
                    action SetVariable("cellSamMirror", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamMirror == 2:
                    action SetVariable("cellSamMirror", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamPainting >= 1:
        vbox xalign 0.61 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/painting1bt.png"
                hover "bgs/cells/green/painting1bt-hover.png"
                if cellSamPainting == 1:
                    action SetVariable("cellSamPainting", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamPainting == 2:
                    action SetVariable("cellSamPainting", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamSexmachine >= 1:
        vbox xalign 0.66 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/sexmachine1bt.png"
                hover "bgs/cells/green/sexmachine1bt-hover.png"
                if cellSamSexmachine == 1:
                    action SetVariable("cellSamSexmachine", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamSexmachine == 2:
                    action SetVariable("cellSamSexmachine", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamShacklesBed >= 1:
        vbox xalign 0.71 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/shackles1bt.png"
                hover "bgs/cells/green/shackles1bt-hover.png"
                if cellSamShacklesBed == 1:
                    action SetVariable("cellSamShacklesBed", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamShacklesBed == 2:
                    action SetVariable("cellSamShacklesBed", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamShoes >= 1:
        vbox xalign 0.76 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/shoes1bt.png"
                hover "bgs/cells/green/shoes1bt-hover.png"
                if cellSamShoes == 1:
                    action SetVariable("cellSamShoes", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                if cellSamShoes == 2:
                    action SetVariable("cellSamShoes", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamStatue >= 1:
        vbox xalign 0.81 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/statue1bt.png"
                hover "bgs/cells/green/statue1bt-hover.png"
                if cellSamStatue == 1:
                    action SetVariable("cellSamStatue", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamStatue == 2:
                    action SetVariable("cellSamStatue", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if cellSamWatch >= 1:
        vbox xalign 0.86 yalign 0.98:
            imagebutton:
                idle "bgs/cells/green/watch1bt.png"
                hover "bgs/cells/green/watch1bt-hover.png"
                if cellSamWatch == 1:
                    action SetVariable("cellSamWatch", 2), SetVariable("cellSamHappiness", cellSamHappiness - 1)
                elif cellSamWatch == 2:
                    action SetVariable("cellSamWatch", 1), SetVariable("cellSamHappiness", cellSamHappiness + 1)

    if month == 10 and 14 <= day <= 31:
        vbox xalign 0.01 yalign 0.90:
            imagebutton:
                idle "bgs/cells/hall1bt.png"
                hover "bgs/cells/hall1bt-hover.png"
                if cellSamHall1 == 0:
                    action SetVariable("cellSamHall1", 1)
                elif cellSamHall1 == 1:
                    action SetVariable("cellSamHall1", 0)

    if month == 12 and 14 <= day <= 31:
        vbox xalign 0.01 yalign 0.90:
            imagebutton:
                idle "bgs/cells/christBt1.png"
                hover "bgs/cells/christBt1-hover.png"
                if cellSamChrist1 == 0:
                    action SetVariable("cellSamChrist1", 1)
                elif cellSamChrist1 == 1:
                    action SetVariable("cellSamChrist1", 0)



default cellCloverLights = 1
default cellCloverBed = 1
default cellCloverWall = 1
default cellCloverShower = 1
default cellCloverCurtain = 1
default cellCloverGlow = 0
default cellCloverBookcase = 0
default cellCloverPlug = 0
default cellCloverChair = 0
default cellCloverClothes = 0
default cellCloverComics = 0
default cellCloverDesk = 0
default cellCloverDildo = 0
default cellCloverGames = 0
default cellCloverHandcuffs = 0
default cellCloverLaptop = 0
default cellCloverLights1 = 0
default cellCloverPainting = 0
default cellCloverPoster = 0
default cellCloverSexmachine = 0
default cellCloverShacklesBed = 0
default cellCloverVR = 0

default cellCloverHall1 = 0

default cellCloverChrist1 = 0

screen cellCloverDeco:

    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("cloverCall")


    vbox xalign 0.01 yalign 0.98:
        imagebutton:
            idle "bgs/cells/cellLights1bt.png"
            hover "bgs/cells/cellLights1bt-hover.png"
            if cellCloverLights == 1:
                action SetVariable("cellCloverLights", 2)
            elif cellCloverLights == 2:
                action SetVariable("cellCloverLights", 1)










    vbox xalign 0.11 yalign 0.98:
        imagebutton:
            idle "bgs/cells/red/curtain1bt.png"
            hover "bgs/cells/red/curtain1bt-hover.png"
            if cellCloverCurtain == 1 and task5Nudes:
                action SetVariable("cellCloverCurtain", 2)
            if cellCloverCurtain == 2 and task5Nudes:
                action SetVariable("cellCloverCurtain", 1)

    if cellCloverGlow >= 1:
        vbox xalign 0.16 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/bed1bt.png"
                hover "bgs/cells/red/bed1bt-hover.png"
                if cellCloverGlow == 1:
                    action SetVariable("cellCloverGlow", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverGlow == 2:
                    action SetVariable("cellCloverGlow", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverBookcase >= 1:
        vbox xalign 0.21 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/bookcase1bt.png"
                hover "bgs/cells/red/bookcase1bt-hover.png"
                if cellCloverBookcase == 1:
                    action SetVariable("cellCloverBookcase ", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverBookcase == 2:
                    action SetVariable("cellCloverBookcase ", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverPlug >= 1:
        vbox xalign 0.26 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/plug1bt.png"
                hover "bgs/cells/red/plug1bt-hover.png"
                if cellCloverPlug == 1:
                    action SetVariable("cellCloverPlug", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                if cellCloverPlug == 2:
                    action SetVariable("cellCloverPlug", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverChair >= 1:
        vbox xalign 0.31 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/chair1bt.png"
                hover "bgs/cells/red/chair1bt-hover.png"
                if cellCloverChair == 1:
                    action SetVariable("cellCloverChair", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverChair == 2:
                    action SetVariable("cellCloverChair", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverClothes >= 1:
        vbox xalign 0.36 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/clothes1bt.png"
                hover "bgs/cells/red/clothes1bt-hover.png"
                if cellCloverClothes == 1:
                    action SetVariable("cellCloverClothes", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                if cellCloverClothes == 2:
                    action SetVariable("cellCloverClothes", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverComics  >= 1:
        vbox xalign 0.41 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/comics1bt.png"
                hover "bgs/cells/red/comics1bt-hover.png"
                if cellCloverComics == 1:
                    action SetVariable("cellCloverComics", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverComics == 2:
                    action SetVariable("cellCloverComics", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverDesk >= 1:
        vbox xalign 0.46 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/desk1bt.png"
                hover "bgs/cells/red/desk1bt-hover.png"
                if cellCloverDesk == 1:
                    action SetVariable("cellCloverDesk", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverDesk == 2:
                    action SetVariable("cellCloverDesk", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverLaptop >= 1:
        vbox xalign 0.51 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/laptop1bt.png"
                hover "bgs/cells/red/laptop1bt-hover.png"
                if cellCloverLaptop == 1:
                    action SetVariable("cellCloverLaptop", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                if cellCloverLaptop == 2:
                    action SetVariable("cellCloverLaptop", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverPainting >= 1:
        vbox xalign 0.56 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/painting1bt.png"
                hover "bgs/cells/red/painting1bt-hover.png"
                if cellCloverPainting == 1:
                    action SetVariable("cellCloverPainting", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                if cellCloverPainting == 2:
                    action SetVariable("cellCloverPainting", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverSexmachine >= 1:
        vbox xalign 0.61 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/sexmachine1bt.png"
                hover "bgs/cells/red/sexmachine1bt-hover.png"
                if cellCloverSexmachine == 1:
                    action SetVariable("cellCloverSexmachine", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                if cellCloverSexmachine == 2:
                    action SetVariable("cellCloverSexmachine", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverShacklesBed >= 1:
        vbox xalign 0.66 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/shackles1bt.png"
                hover "bgs/cells/red/shackles1bt-hover.png"
                if cellCloverShacklesBed == 1:
                    action SetVariable("cellCloverShacklesBed", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                if cellCloverShacklesBed == 2:
                    action SetVariable("cellCloverShacklesBed", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverDildo >= 1:
        vbox xalign 0.71 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/dildo1bt.png"
                hover "bgs/cells/red/dildo1bt-hover.png"
                if cellCloverDildo == 1:
                    action SetVariable("cellCloverDildo", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverDildo == 2:
                    action SetVariable("cellCloverDildo", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverGames >= 1:
        vbox xalign 0.76 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/games1bt.png"
                hover "bgs/cells/red/games1bt-hover.png"
                if cellCloverGames == 1:
                    action SetVariable("cellCloverGames", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverGames == 2:
                    action SetVariable("cellCloverGames", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverLights1 >= 1:
        vbox xalign 0.81 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/lights1bt.png"
                hover "bgs/cells/red/lights1bt-hover.png"
                if cellCloverLights1 == 1:
                    action SetVariable("cellCloverLights1", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverLights1 == 2:
                    action SetVariable("cellCloverLights1", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverPoster >= 1:
        vbox xalign 0.86 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/poster1bt.png"
                hover "bgs/cells/red/poster1bt-hover.png"
                if cellCloverPoster == 1:
                    action SetVariable("cellCloverPoster", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverPoster == 2:
                    action SetVariable("cellCloverPoster", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if cellCloverVR >= 1:
        vbox xalign 0.91 yalign 0.98:
            imagebutton:
                idle "bgs/cells/red/vr1bt.png"
                hover "bgs/cells/red/vr1bt-hover.png"
                if cellCloverVR == 1:
                    action SetVariable("cellCloverVR", 2), SetVariable("cellCloverHappiness", cellCloverHappiness - 1)
                elif cellCloverVR == 2:
                    action SetVariable("cellCloverVR", 1), SetVariable("cellCloverHappiness", cellCloverHappiness + 1)

    if month == 10 and 14 <= day <= 31:
        vbox xalign 0.01 yalign 0.90:
            imagebutton:
                idle "bgs/cells/hall1bt.png"
                hover "bgs/cells/hall1bt-hover.png"
                if cellCloverHall1 == 0:
                    action SetVariable("cellCloverHall1", 1)
                elif cellCloverHall1 == 1:
                    action SetVariable("cellCloverHall1", 0)

    if month == 12 and 14 <= day <= 31:
        vbox xalign 0.01 yalign 0.90:
            imagebutton:
                idle "bgs/cells/christBt1.png"
                hover "bgs/cells/christBt1-hover.png"
                if cellCloverChrist1 == 0:
                    action SetVariable("cellCloverChrist1", 1)
                elif cellCloverChrist1 == 1:
                    action SetVariable("cellCloverChrist1", 0)


layeredimage cellClover:
    always:
        "bgs/cells/bgCell.jpg"
    if cellCloverHall1 == 1:
        "bgs/cells/bgCellHalloween.jpg"
    if cellCloverChrist1 == 1:
        "bgs/cells/bgCellChristmas.jpg"
    if cellCloverLights == 1:
        "bgs/cells/cellLights1.png"

    if cellCloverWall == 1:
        "bgs/cells/cellWall1.png"

    if cellCloverBed == 1:
        "bgs/cells/bed1.png"

    if cellCloverShower == 1:
        "bgs/cells/cellShower1.png"


    if spyRoomRand == 1:
        "bgs/cells/showerWater.png"
    if spyRoomRand == 1:
        "bgs/cells/red/spyShower.png" xalign 0.282 ypos 185
    if spyRoomRand == 1:
        "bgs/cells/showerSteam.png"
    if spyRoomRand == 11:
        "bgs/cells/red/spybondage1.png"


    if cellCloverCurtain == 1:
        "bgs/cells/red/cellCurtain2.png"

    if cellCloverGlow == 1:
        "bgs/cells/red/bedGlow.png"

    if cellCloverBookcase == 1:
        "bgs/cells/red/bookcase.png"

    if cellCloverPlug == 1:
        "bgs/cells/red/buttPlug.png"

    if cellCloverChair == 1:
        "bgs/cells/red/chair.png"

    if cellCloverComics == 1:
        "bgs/cells/red/comics.png"

    if cellCloverDesk == 1:
        "bgs/cells/red/desk.png"

    if cellCloverDildo == 1:
        "bgs/cells/red/cellCloverDildo.png"

    if cellCloverGames == 1:
        "bgs/cells/red/games.png"

    if cellCloverLaptop == 1:
        "bgs/cells/red/laptop.png"

    if cellCloverPainting == 1:
        "bgs/cells/red/painting.png"

    if cellCloverLights1 == 1:
        "bgs/cells/red/lights1.png"

    if cellCloverPoster == 1:
        "bgs/cells/red/poster.png"

    if cellCloverClothes == 1:
        "bgs/cells/red/clothes.png"

    if cellCloverSexmachine == 1:
        "bgs/cells/red/poster.png"

    if cellCloverShacklesBed == 1:
        "bgs/cells/red/shacklesBed.png"

    if cellCloverVR == 1:
        "bgs/cells/red/vr.png"

    if cellCloverHall1 == 1:
        "bgs/cells/halloween2.png"

    if cellCloverChrist1 == 1:
        "bgs/cells/christmas2.png"
    if spyRoomRand == 2 and slutLevel >= 4 and task26Stage <= 18 or task26Stage >= 33:
        "bgs/cells/spyLesb2.png"



default cellAlexLights = 1
default cellAlexBed = 1
default cellAlexWall = 1
default cellAlexShower = 1
default cellAlexCurtain = 1
default cellAlexBear = 0
default cellAlexBoombox = 0
default cellAlexBottles = 0
default cellAlexCans = 0
default cellAlexChair = 0
default cellAlexClothes = 0
default cellAlexDesk = 0
default cellAlexGraffiti = 0
default cellAlexGuitar = 0
default cellAlexNightstand = 0
default cellAlexPosters = 0
default cellAlexPosters2 = 0
default cellAlexSkull = 0

default cellAlexBookcase = 0
default cellAlexPlug = 0
default cellAlexDildo = 0
default cellAlexHandcuffs = 0
default cellAlexLights1 = 0
default cellAlexPainting = 0
default cellAlexPoetry = 0
default cellAlexSexmachine = 0
default cellAlexShacklesBed = 0

default cellAlexHall1 = 0

default cellAlexChrist1 = 0

layeredimage cellAlex:
    always:
        "bgs/cells/bgCell.jpg"
    if cellAlexHall1 == 1:
        "bgs/cells/bgCellHalloween.jpg"
    if cellAlexChrist1 == 1:
        "bgs/cells/bgCellChristmas.jpg"
    if cellAlexLights == 1:
        "bgs/cells/cellLights1.png"

    if cellAlexWall == 1:
        "bgs/cells/cellWall1.png"

    if cellAlexGraffiti == 1:
        "bgs/cells/yellow/graffiti.png"

    if cellAlexBed == 1:
        "bgs/cells/bed1.png"

    if cellAlexDesk == 1:
        "bgs/cells/yellow/desk.png"

    if cellAlexShower == 1:
        "bgs/cells/cellShower1.png"

    if cellAlexPoetry == 1:
        "bgs/cells/yellow/book1.png"

    if cellAlexBear == 1:
        "bgs/cells/yellow/bear.png"

    if cellAlexClothes == 1:
        "bgs/cells/yellow/clothes.png"

    if cellAlexBoombox == 1:
        "bgs/cells/yellow/boombox.png"

    if cellAlexChair == 1:
        "bgs/cells/yellow/chair.png"

    if cellAlexCans == 1:
        "bgs/cells/yellow/cans.png"

    if cellAlexBottles == 1:
        "bgs/cells/yellow/bottles.png"

    if cellAlexPosters == 1:
        "bgs/cells/yellow/posters.png"

    if cellAlexGuitar == 1:
        "bgs/cells/yellow/guitar.png"

    if cellAlexNightstand == 1:
        "bgs/cells/yellow/nightstand.png"

    if cellAlexPosters2 == 1:
        "bgs/cells/yellow/posters2.png"

    if cellAlexSkull == 1:
        "bgs/cells/yellow/skull.png"



    if spyRoomRand == 1:
        "bgs/cells/showerWater.png"
    if spyRoomRand == 1:
        "bgs/cells/yellow/spyShower.png" xalign 0.282 ypos 185
    if spyRoomRand == 1:
        "bgs/cells/showerSteam.png"
    if spyRoomRand == 2 and slutLevel >= 4 and cellAlexDesk == 1 and task26Stage <= 18 or task26Stage >= 33:
        "bgs/cells/spyLesb3.png"
    if spyRoomRand == 11:
        "bgs/cells/yellow/spybondage1.png"


    if cellAlexCurtain == 1:
        "bgs/cells/yellow/cellCurtain.png"


    if cellAlexHall1 == 1:
        "bgs/cells/halloween3.png"
    if cellAlexChrist1 == 1:
        "bgs/cells/christmas3.png"

screen cellAlexDeco:

    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action Jump("alexCall")


    vbox xalign 0.01 yalign 0.98:
        imagebutton:
            idle "bgs/cells/cellLights1bt.png"
            hover "bgs/cells/cellLights1bt-hover.png"
            if cellAlexLights == 1:
                action SetVariable("cellAlexLights", 0)
            elif cellAlexLights == 0:
                action SetVariable("cellAlexLights", 1)










    vbox xalign 0.11 yalign 0.98:
        imagebutton:
            idle "bgs/cells/yellow/curtain1bt.png"
            hover "bgs/cells/yellow/curtain1bt-hover.png"
            if cellAlexCurtain == 1 and task5Nudes:
                action SetVariable("cellAlexCurtain", 0)
            if cellAlexCurtain == 0 and task5Nudes:
                action SetVariable("cellAlexCurtain", 1)

    if cellAlexBear >= 1:
        vbox xalign 0.16 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/bear1bt.png"
                hover "bgs/cells/yellow/bear1bt-hover.png"
                if cellAlexBear == 1:
                    action SetVariable("cellAlexBear", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                elif cellAlexBear == 2:
                    action SetVariable("cellAlexBear", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexBoombox >= 1:
        vbox xalign 0.21 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/boombox1bt.png"
                hover "bgs/cells/yellow/boombox1bt-hover.png"
                if cellAlexBoombox == 1:
                    action SetVariable("cellAlexBoombox", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                elif cellAlexBoombox == 2:
                    action SetVariable("cellAlexBoombox", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexGraffiti >= 1:
        vbox xalign 0.26 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/graffiti1bt.png"
                hover "bgs/cells/yellow/graffiti1bt-hover.png"
                if cellAlexGraffiti == 1:
                    action SetVariable("cellAlexGraffiti", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexGraffiti == 2:
                    action SetVariable("cellAlexGraffiti", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexBookcase >= 1:
        vbox xalign 0.21 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/bookcase1bt.png"
                hover "bgs/cells/yellow/bookcase1bt-hover.png"
                if cellAlexBookcase == 1:
                    action SetVariable("cellAlexBookcase ", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                elif cellAlexBookcase == 2:
                    action SetVariable("cellAlexBookcase ", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexPlug >= 1:
        vbox xalign 0.26 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/plug1bt.png"
                hover "bgs/cells/yellow/plug1bt-hover.png"
                if cellAlexPlug == 1:
                    action SetVariable("cellAlexPlug", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexPlug == 2:
                    action SetVariable("cellAlexPlug", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexChair >= 1:
        vbox xalign 0.31 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/chair1bt.png"
                hover "bgs/cells/yellow/chair1bt-hover.png"
                if cellAlexChair == 1:
                    action SetVariable("cellAlexChair", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                elif cellAlexChair == 2:
                    action SetVariable("cellAlexChair", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexClothes >= 1:
        vbox xalign 0.36 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/clothes1bt.png"
                hover "bgs/cells/yellow/clothes1bt-hover.png"
                if cellAlexClothes == 1:
                    action SetVariable("cellAlexClothes", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexClothes == 2:
                    action SetVariable("cellAlexClothes", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexDesk >= 1:
        vbox xalign 0.41 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/desk1bt.png"
                hover "bgs/cells/yellow/desk1bt-hover.png"
                if cellAlexDesk == 1:
                    action SetVariable("cellAlexDesk", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                elif cellAlexDesk == 2:
                    action SetVariable("cellAlexDesk", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexCans >= 1:
        vbox xalign 0.46 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/cans1bt.png"
                hover "bgs/cells/yellow/cans1bt-hover.png"
                if cellAlexCans == 1:
                    action SetVariable("cellAlexCans", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                elif cellAlexCans == 2:
                    action SetVariable("cellAlexCans", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexPoetry >= 1:
        vbox xalign 0.51 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/book1bt.png"
                hover "bgs/cells/yellow/book1bt-hover.png"
                if cellAlexPoetry == 1:
                    action SetVariable("cellAlexPoetry", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexPoetry == 2:
                    action SetVariable("cellAlexPoetry", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexBottles >= 1:
        vbox xalign 0.56 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/bottles1bt.png"
                hover "bgs/cells/yellow/bottles1bt-hover.png"
                if cellAlexBottles == 1:
                    action SetVariable("cellAlexBottles", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexBottles == 2:
                    action SetVariable("cellAlexBottles", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexGuitar >= 1:
        vbox xalign 0.61 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/guitar1bt.png"
                hover "bgs/cells/yellow/guitar1bt-hover.png"
                if cellAlexGuitar == 1:
                    action SetVariable("cellAlexGuitar", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexGuitar == 2:
                    action SetVariable("cellAlexGuitar", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexNightstand >= 1:
        vbox xalign 0.66 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/nightstand1bt.png"
                hover "bgs/cells/yellow/nightstand1bt-hover.png"
                if cellAlexNightstand == 1:
                    action SetVariable("cellAlexNightstand", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexNightstand == 2:
                    action SetVariable("cellAlexNightstand", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexPosters >= 1:
        vbox xalign 0.71 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/posters1bt.png"
                hover "bgs/cells/yellow/posters1bt-hover.png"
                if cellAlexPosters == 1:
                    action SetVariable("cellAlexPosters", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexPosters == 2:
                    action SetVariable("cellAlexPosters", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexPosters2 >= 1:
        vbox xalign 0.76 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/posters2bt.png"
                hover "bgs/cells/yellow/posters2bt-hover.png"
                if cellAlexPosters2 == 1:
                    action SetVariable("cellAlexPosters2", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexPosters2 == 2:
                    action SetVariable("cellAlexPosters2", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexSkull >= 1:
        vbox xalign 0.81 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/skull1bt.png"
                hover "bgs/cells/yellow/skull1bt-hover.png"
                if cellAlexSkull == 1:
                    action SetVariable("cellAlexSkull", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexSkull == 2:
                    action SetVariable("cellAlexSkull", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexSexmachine >= 1:
        vbox xalign 0.66 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/sexmachine1bt.png"
                hover "bgs/cells/yellow/sexmachine1bt-hover.png"
                if cellAlexSexmachine == 1:
                    action SetVariable("cellAlexSexmachine", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexSexmachine == 2:
                    action SetVariable("cellAlexSexmachine", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexShacklesBed >= 1:
        vbox xalign 0.71 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/shackles1bt.png"
                hover "bgs/cells/yellow/shackles1bt-hover.png"
                if cellAlexShacklesBed == 1:
                    action SetVariable("cellAlexShacklesBed", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                if cellAlexShacklesBed == 2:
                    action SetVariable("cellAlexShacklesBed", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if cellAlexDildo >= 1:
        vbox xalign 0.71 yalign 0.98:
            imagebutton:
                idle "bgs/cells/yellow/dildo1bt.png"
                hover "bgs/cells/yellow/dildo1bt-hover.png"
                if cellAlexDildo == 2:
                    action SetVariable("cellAlexDildo", 2), SetVariable("cellAlexHappiness", cellAlexHappiness - 1)
                elif cellAlexDildo == 1:
                    action SetVariable("cellAlexDildo", 1), SetVariable("cellAlexHappiness", cellAlexHappiness + 1)

    if month == 10 and 14 <= day <= 31:
        vbox xalign 0.01 yalign 0.90:
            imagebutton:
                idle "bgs/cells/hall1bt.png"
                hover "bgs/cells/hall1bt-hover.png"
                if cellAlexHall1 == 0:
                    action SetVariable("cellAlexHall1", 1)
                elif cellAlexHall1 == 1:
                    action SetVariable("cellAlexHall1", 0)

    if month == 12 and 14 <= day <= 31:
        vbox xalign 0.01 yalign 0.90:
            imagebutton:
                idle "bgs/cells/christBt1.png"
                hover "bgs/cells/christBt1-hover.png"
                if cellAlexChrist1 == 0:
                    action SetVariable("cellAlexChrist1", 1)
                elif cellAlexChrist1 == 1:
                    action SetVariable("cellAlexChrist1", 0)





default zone = "Beverly Hills"
default statusSpy = 1
image statusHealthIcon1 = "gui/statusHPRed.png"
image statusHealthIcon2 = "gui/statusHPOrange.png"
image statusHealthIcon3 = "gui/statusHPGreen.png"

screen status:
    add "gui/status.jpg"


    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/missionScreen/exitButton2.png"
            hover "gui/missionScreen/exitButton2-hover.png"
            action Jump("worldmap")

    text "{font=fonts/freshmarker.ttf}{size=+5}[coverCounter]{/size}{/font}" xalign 0.27 yalign 0.358
    text "{font=fonts/freshmarker.ttf}{size=+5}$[cash]{/size}{/font}" xalign 0.27 yalign 0.42
    text "{font=fonts/freshmarker.ttf}{size=+5}[intel]{/size}{/font}" xalign 0.27 yalign 0.487


    if 90 <= playerKarma <= 100:
        text "{font=fonts/freshmarker.ttf}{size=+5}Angelic{/size}{/font}" xalign 0.27 yalign 0.555
    if 70 <= playerKarma <= 89:
        text "{font=fonts/freshmarker.ttf}{size=+5}Heroic{/size}{/font}" xalign 0.27 yalign 0.555
    if 50 <= playerKarma <= 69:
        text "{font=fonts/freshmarker.ttf}{size=+5}Good{/size}{/font}" xalign 0.27 yalign 0.555
    if 30 <= playerKarma <= 49:
        text "{font=fonts/freshmarker.ttf}{size=+5}Dubious{/size}{/font}" xalign 0.27 yalign 0.555
    if 10 <= playerKarma <= 29:
        text "{font=fonts/freshmarker.ttf}{size=+5}Moralless{/size}{/font}" xalign 0.27 yalign 0.555
    if 0 <= playerKarma <= 9:
        text "{font=fonts/freshmarker.ttf}{size=+5}Evil{/size}{/font}" xalign 0.27 yalign 0.555

    text "{font=fonts/freshmarker.ttf}{size=+5}[zone]{/size}{/font}" xalign 0.165 yalign 0.085


    if missionAreaWOOHPActive:
        add "gui/achiev/achiev1.png" xpos 85 ypos 505 zoom 0.12
    if sexAct1 != "???" and sexAct2 != "???" and sexAct3 != "???" and sexAct4 != "???" and sexAct5 != "???" and sexAct6 != "???":
        add "gui/achiev/achiev2.png" xpos 145 ypos 505 zoom 0.12
    if month1CardClaimed:
        add "gui/achiev/achiev3.png" xpos 200 ypos 505 zoom 0.12
    if swCardClaimed:
        add "gui/achiev/achiev4.png" xpos 260 ypos 505 zoom 0.12
    if photoClaus:
        add "gui/achiev/achiev5.png" xpos 320 ypos 505 zoom 0.12
    if tentaclePic:
        add "gui/achiev/achiev6.png" xpos 85 ypos 565 zoom 0.12
    if moneyAchiev:
        add "gui/achiev/achiev7.png" xpos 145 ypos 565 zoom 0.12
    if playerMilkshakeLvl >= 6:
        add "gui/achiev/achiev8.png" xpos 200 ypos 565 zoom 0.12
    if HQLiberated == 6:
        add "gui/achiev/achiev9.png" xpos 260 ypos 565 zoom 0.12


    if spyGreenActive:
        vbox xalign 0.7225 yalign 0.259:
            if statusSpy == 1:
                add "gui/samStatusIcon-hover.png"
            else:
                imagebutton:
                    idle "gui/statusIcon.png"
                    hover "gui/samStatusIcon-hover.png"
                    action SetVariable("statusSpy", 1)
    if spyRedActive:
        vbox xalign 0.809 yalign 0.259:
            if statusSpy == 2:
                add "gui/cloverStatusIcon-hover.png"
            else:
                imagebutton:
                    idle "gui/statusIcon.png"
                    hover "gui/cloverStatusIcon-hover.png"
                    action SetVariable("statusSpy", 2)
    if spyYellowActive:
        vbox xalign 0.894 yalign 0.259:
            if statusSpy == 3:
                add "gui/alexStatusIcon-hover.png"
            else:
                imagebutton:
                    idle "gui/statusIcon.png"
                    hover "gui/alexStatusIcon-hover.png"
                    action SetVariable("statusSpy", 3)


    if statusSpy == 1:
        add "gui/statusSpyGreen1.png" xalign 0.5 ypos 150
        text "{font=fonts/freshmarker.ttf}{size=+40}SAM{/size}{/font}" xalign 0.80 yalign 0.435
        if samHealth == 3:
            text "{font=fonts/freshmarker.ttf}Healthy{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPGreen.png" xalign 0.75 yalign 0.58
        if samHealth == 2:
            text "{font=fonts/freshmarker.ttf}Hurt{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPOrange.png" xalign 0.75 yalign 0.58
        if samHealth == 1:
            text "{font=fonts/freshmarker.ttf}}Badly hurt{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPRed.png" xalign 0.75 yalign 0.58

        if 0 <= slutLevel <= 2:
            text "{font=fonts/freshmarker.ttf}Prudish{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 3:
            text "{font=fonts/freshmarker.ttf}Flirty{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 4:
            text "{font=fonts/freshmarker.ttf}}Promiscuous{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 5:
            text "{font=fonts/freshmarker.ttf}}Slutty{/font}" xalign 0.91 yalign 0.676
        if slutLevel >= 6:
            text "{font=fonts/freshmarker.ttf}}Whorish{/font}" xalign 0.91 yalign 0.676

        if samMood <= 10:
            text "{font=fonts/freshmarker.ttf}Depressed{/font}" xalign 0.91 yalign 0.743
        if 11 <= samMood <= 25:
            text "{font=fonts/freshmarker.ttf}Very low{/font}" xalign 0.91 yalign 0.743
        if 26 <= samMood <= 45:
            text "{font=fonts/freshmarker.ttf}Low{/font}" xalign 0.91 yalign 0.743
        if 46 <= samMood <= 70:
            text "{font=fonts/freshmarker.ttf}Normal{/font}" xalign 0.91 yalign 0.743
        if 71 <= samMood <= 80:
            text "{font=fonts/freshmarker.ttf}High{/font}" xalign 0.91 yalign 0.743
        if samMood >= 81:
            text "{font=fonts/freshmarker.ttf}Very high{/font}" xalign 0.91 yalign 0.743

        text "{font=fonts/freshmarker.ttf}{size=-4}[samFriend]{/size}{/font}" xalign 0.91 yalign 0.81


        text "{font=fonts/freshmarker.ttf}[nanoLevelSam]/100{/font}" xalign 0.91 yalign 0.878


        if samSupLvl == 1:
            text "{font=fonts/freshmarker.ttf}Low{/font}" xalign 0.91 yalign 0.94
        if samSupLvl == 2:
            text "{font=fonts/freshmarker.ttf}Medium{/font}" xalign 0.91 yalign 0.94
        if samSupLvl == 3:
            text "{font=fonts/freshmarker.ttf}High{/font}" xalign 0.91 yalign 0.94

        if task2Stage >= 10:
            vbox xalign 0.97 yalign 0.95:
                imagebutton:
                    idle "gui/statusSet.png"
                    hover "gui/statusSet-hover.png"
                    action Jump("statusSetSup")


    if statusSpy == 2:
        add "gui/statusSpyRed1.png" xalign 0.5 ypos 150
        text "{font=fonts/freshmarker.ttf}{size=+40}CLOVER{/size}{/font}" xalign 0.85 yalign 0.435
        if cloverHealth == 3:
            text "{font=fonts/freshmarker.ttf}Healthy{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPGreen.png" xalign 0.75 yalign 0.58
        if cloverHealth == 2:
            text "{font=fonts/freshmarker.ttf}Hurt{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPOrange.png" xalign 0.75 yalign 0.58
        if cloverHealth == 1:
            text "{font=fonts/freshmarker.ttf}}Badly hurt{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPRed.png" xalign 0.75 yalign 0.58

        if 0 <= slutLevel <= 2:
            text "{font=fonts/freshmarker.ttf}Prudish{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 3:
            text "{font=fonts/freshmarker.ttf}Flirty{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 4:
            text "{font=fonts/freshmarker.ttf}}Promiscuous{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 5:
            text "{font=fonts/freshmarker.ttf}}Slutty{/font}" xalign 0.91 yalign 0.676
        if slutLevel >= 6:
            text "{font=fonts/freshmarker.ttf}}Whorish{/font}" xalign 0.91 yalign 0.676

        if cloverMood <= 10:
            text "{font=fonts/freshmarker.ttf}Depressed{/font}" xalign 0.91 yalign 0.743
        if 11 <= cloverMood <= 25:
            text "{font=fonts/freshmarker.ttf}Very low{/font}" xalign 0.91 yalign 0.743
        if 26 <= cloverMood <= 45:
            text "{font=fonts/freshmarker.ttf}Low{/font}" xalign 0.91 yalign 0.743
        if 46 <= cloverMood <= 70:
            text "{font=fonts/freshmarker.ttf}Normal{/font}" xalign 0.91 yalign 0.743
        if 71 <= cloverMood <= 80:
            text "{font=fonts/freshmarker.ttf}High{/font}" xalign 0.91 yalign 0.743
        if cloverMood >= 81:
            text "{font=fonts/freshmarker.ttf}Very high{/font}" xalign 0.91 yalign 0.743

        text "{font=fonts/freshmarker.ttf}{size=-4}[cloverFriend]{/size}{/font}" xalign 0.91 yalign 0.81


        text "{font=fonts/freshmarker.ttf}[nanoLevelClover]/100{/font}" xalign 0.91 yalign 0.878


        if cloverSupLvl == 1:
            text "{font=fonts/freshmarker.ttf}Low{/font}" xalign 0.91 yalign 0.94
        if cloverSupLvl == 2:
            text "{font=fonts/freshmarker.ttf}Medium{/font}" xalign 0.91 yalign 0.94
        if cloverSupLvl == 3:
            text "{font=fonts/freshmarker.ttf}High{/font}" xalign 0.91 yalign 0.94


        if task2Stage >= 10:
            vbox xalign 0.97 yalign 0.95:
                imagebutton:
                    idle "gui/statusSet.png"
                    hover "gui/statusSet-hover.png"
                    action Jump("statusSetSup")


    if statusSpy == 3:
        add "gui/statusSpyYellow1.png" xalign 0.5 ypos 150
        text "{font=fonts/freshmarker.ttf}{size=+40}ALEX{/size}{/font}" xalign 0.81 yalign 0.435
        if alexHealth == 3:
            text "{font=fonts/freshmarker.ttf}Healthy{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPGreen.png" xalign 0.75 yalign 0.58
        if alexHealth == 2:
            text "{font=fonts/freshmarker.ttf}Hurt{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPOrange.png" xalign 0.75 yalign 0.58
        if alexHealth == 1:
            text "{font=fonts/freshmarker.ttf}}Badly hurt{/font}" xalign 0.85 yalign 0.573
            add "gui/statusHPRed.png" xalign 0.75 yalign 0.58

        if 0 <= slutLevel <= 2:
            text "{font=fonts/freshmarker.ttf}Prudish{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 3:
            text "{font=fonts/freshmarker.ttf}Flirty{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 4:
            text "{font=fonts/freshmarker.ttf}}Promiscuous{/font}" xalign 0.91 yalign 0.676
        if slutLevel == 5:
            text "{font=fonts/freshmarker.ttf}}Slutty{/font}" xalign 0.91 yalign 0.676
        if slutLevel >= 6:
            text "{font=fonts/freshmarker.ttf}}Whorish{/font}" xalign 0.91 yalign 0.676

        if alexMood <= 10:
            text "{font=fonts/freshmarker.ttf}Depressed{/font}" xalign 0.91 yalign 0.743
        if 11 <= alexMood <= 25:
            text "{font=fonts/freshmarker.ttf}Very low{/font}" xalign 0.91 yalign 0.743
        if 26 <= alexMood <= 45:
            text "{font=fonts/freshmarker.ttf}Low{/font}" xalign 0.91 yalign 0.743
        if 46 <= alexMood <= 70:
            text "{font=fonts/freshmarker.ttf}Normal{/font}" xalign 0.91 yalign 0.743
        if 71 <= alexMood <= 80:
            text "{font=fonts/freshmarker.ttf}High{/font}" xalign 0.91 yalign 0.743
        if alexMood >= 81:
            text "{font=fonts/freshmarker.ttf}Very high{/font}" xalign 0.91 yalign 0.743

        text "{font=fonts/freshmarker.ttf}{size=-4}[alexFriend]{/size}{/font}" xalign 0.91 yalign 0.81


        text "{font=fonts/freshmarker.ttf}[nanoLevelAlex]/100{/font}" xalign 0.91 yalign 0.878


        text "{font=fonts/freshmarker.ttf}[nanoLevelAlex]/100{/font}" xalign 0.91 yalign 0.878


        if alexSupLvl == 1:
            text "{font=fonts/freshmarker.ttf}Low{/font}" xalign 0.91 yalign 0.94
        if alexSupLvl == 2:
            text "{font=fonts/freshmarker.ttf}Medium{/font}" xalign 0.91 yalign 0.94
        if alexSupLvl == 3:
            text "{font=fonts/freshmarker.ttf}High{/font}" xalign 0.91 yalign 0.94


        if task2Stage >= 10:
            vbox xalign 0.97 yalign 0.95:
                imagebutton:
                    idle "gui/statusSet.png"
                    hover "gui/statusSet-hover.png"
                    action Jump("statusSetSup")

label statusSetSup:
    if statusSpy == 1:
        "Set Sam's nanobot suppression levels."
        menu:
            "High Suppression" if True:
                $ samSupLvl = 3
                y "Make sure to keep your nanobots suppressed as much as possible."
                sM "Understood."
                jump status
            "Medium Suppression" if True:
                $ samSupLvl = 2
                y "Keep the nanobots suppressed, but don't overdo it."
                sM "Okay, got it."
                jump status
            "Low Suppression" if True:
                $ samSupLvl = 1
                y "I want to up your nanobot levels a bit. Go easy on the nanobot suppression."
                sM "Okay if you're sure."
                jump status
            "Info" if True:
                "Your spies nano levels will slowly rise over time."
                "High nano levels mean your spies will more easily agree to doing sexual actions and will have less of a mood penalty for all actions. However, spies may become more rebellious, steal or even disappear for a few days."
                "Low nano levels means that your spy will make a more steady amount of money, but will take greater mood penalties when asked to preform sex or illigal acts."
                "Medium nano levels is a steady balance between the two."
                "Nano levels can be reduced by having your spies preform sexual acts. Or they can be boosted by injecting them with more nanobots. A spy with low suppression will increase her nanobot levels much faster than one with high suppression as well."
                jump status
    if statusSpy == 2:
        "Set Clover's nanobot suppression levels."
        menu:
            "High Suppression" if True:
                $ cloverSupLvl = 3
                y "Make sure to keep your nanobots suppressed as much as possible."
                cM "Get my naughty on and suppress the nanobots. Got it."
                jump status
            "Medium Suppression" if True:
                $ cloverSupLvl = 2
                y "Keep the nanobots suppressed, but don't overdo it."
                cM "Okay, I can do that."
                jump status
            "Low Suppression" if True:
                $ cloverSupLvl = 1
                y "I want to up your nanobot levels a bit. Go easy on the nanobot suppression."
                cM "Risky, but all right."
                jump status
            "Info" if True:
                "Your spies nano levels will slowly rise over time."
                "High nano levels mean your spies will more easily agree to doing sexual actions and will have less of a mood penalty for all actions. However, spies may become more rebellious, steal or even disappear for a few days."
                "Low nano levels means that your spy will make a more steady amount of money, but will take greater mood penalties when asked to preform sex or illigal acts."
                "Medium nano levels is a steady balance between the two."
                "Nano levels can be reduced by having your spies preform sexual acts. Or they can be boosted by injecting them with more nanobots. A spy with low suppression will increase her nanobot levels much faster than one with high suppression."
                jump statusSetSup
    if statusSpy == 3:
        "Set Alex's nanobot suppression levels."
        menu:
            "High Suppression" if True:
                $ alexSupLvl = 3
                y "Make sure to keep your nanobots suppressed as much as possible."
                aM "Oh, I gets to have some fuuuun~...!."
                jump status
            "Medium Suppression" if True:
                $ alexSupLvl = 2
                y "Keep the nanobots suppressed, but don't overdo it."
                aM "Okidokie."
                jump status
            "Low Suppression" if True:
                $ alexSupLvl = 1
                y "I want to up your nanobot levels a bit. Go easy on the nanobot suppression."
                aM "Hm okay, but only if you're really really sure."
                jump status
            "Info" if True:
                "Your spies nano levels will slowly rise over time."
                "High nano levels mean your spies will more easily agree to doing sexual actions and will have less of a mood penalty for all actions. However, spies may become more rebellious, steal or even disappear for a few days."
                "Low nano levels means that your spy will make a more steady amount of money, but will take greater mood penalties when asked to preform sex or illigal acts."
                "Medium nano levels is a steady balance between the two."
                "Nano levels can be reduced by having your spies preform sexual acts. Or they can be boosted by injecting them with more nanobots. A spy with low suppression will increase her nanobot levels much faster than one with high suppression."
                jump statusSetSup







label shopPrev:
    if shopCategory == 1:
        if shopCurrentSpy == 1:
            show green g1:
                linear 0.2 xalign 1.0 yalign -0.9
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign -0.9
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign -0.9
    if shopCategory == 2:
        if shopCurrentSpy == 1:
            show green g1:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign -0.7
    if shopCategory == 3:
        if shopCurrentSpy == 1:
            show green:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign -0.7
    if shopCategory == 4:
        if shopCurrentSpy == 1:
            show green:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign -0.7
    if shopCategory == 5:
        if shopCurrentSpy == 1:
            show green:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign -0.7
    if shopCategory == 6:
        if shopCurrentSpy == 1:
            show green:
                linear 0.2 xalign 1.0 yalign 0.3
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign 0.3
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign 0.3
    if shopCategory == 7:
        if shopCurrentSpy == 1:
            show green:
                linear 0.2 xalign 1.0 yalign 0.9
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign 0.9
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign 0.9
    if shopCategory == 8:
        if shopCurrentSpy == 1:
            show green:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign -0.7
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign -0.7
    if shopCategory == 9:
        if shopCurrentSpy == 1:
            show green:
                linear 0.2 xalign 1.0 yalign 1.1
        if shopCurrentSpy == 2:
            show red:
                linear 0.2 xalign 1.0 yalign 1.1
        if shopCurrentSpy == 3:
            show yellow:
                linear 0.2 xalign 1.0 yalign 1.1
    if menuSelect == 1:
        call screen bgShop1
    elif menuSelect == 3:
        call screen bgShop3
    elif menuSelect == 6:
        call screen bgShop6


image bgShop1 = "gui/itemUI/shop1/bgShop1.png"


default shopItemSelect = 0
default shopSelectBox = "gui/itemUI/shopSelectBox.png"


default shopHeadSelect = False
default shopAcc1Select = False
default shopNeckSelect = False
default shopChestSelect = False
default shopAcc2Select = False
default shopBottSelect = False
default shopShoeSelect = False
default shopUnderSelect = False

default shopHeadPrice = 0
default shopAcc1Price = 0
default shopNeckPrice = 0
default shopChestPrice = 0
default shopAcc2Price = 0
default shopBottPrice = 0
default shopShoePrice = 0

default shopCategory = 0
default shopTotal = 0
default menuSelect = 0

default shopSpyName = "Name"
default shopCurrentSpy = 1

label mallNotAvailable:
    "Shopping not yet available. Work in progress."
    call screen bgShop3

screen bgShop1:
    add "gui/itemUI/shop1/bgShop1.png"


    text "{font=fonts/freshMarker.ttf}{size=+4}{color=#ffeda6}{color=#ffffff}[cash]{/color}{/size}{/font}" xpos 180 yalign 0.09


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action SetVariable("shopTotal", 0), Jump("exitShop")


    vbox xalign 0.085 yalign 0.95:
        imagebutton:
            idle "gui/itemUI/shop1/prv.png"
            hover "gui/itemUI/shop1/prv-hover.png"

    vbox xalign 0.55 yalign 0.95:
        imagebutton:
            idle "gui/itemUI/shop1/nxt.png"
            hover "gui/itemUI/shop1/nxt-hover.png"


    if shopCurrentSpy == 1:
        if spyGreenActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Sam"
    elif shopCurrentSpy == 2:
        if spyRedActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Clover"
    elif shopCurrentSpy == 3:
        if spyYellowActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Alex"
    hbox:
        spacing 10 xalign 0.64 yalign 0.29
        text "{color=#ffffff}{size=+12}{font=fonts/freshmarker.ttf}[shopSpyName]{/font}{/color}{/color}"




    vbox xalign 0.67 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpySam.png"
            hover "gui/itemUI/shopSpySam-hover.png"
            action Jump("shop1SpySam")

    vbox xalign 0.77 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyClover.png"
            hover "gui/itemUI/shopSpyClover-hover.png"
            action Jump("shop1SpyClover")

    vbox xalign 0.87 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyAlex.png"
            hover "gui/itemUI/shopSpyAlex-hover.png"
            action Jump("shop1SpyAlex")


    if shopCurrentSpy == 1:
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/reset.png"
                hover "gui/itemUI/reset-hover.png"
                action Jump("resetSamShop")
    if shopCurrentSpy == 2:
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/undress.png"
                hover "gui/itemUI/undress-hover.png"
                action Jump("resetSamShop")
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/reset.png"
                hover "gui/itemUI/reset-hover.png"
                action Jump("resetCloverShop")
    if shopCurrentSpy == 3:
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/undress.png"
                hover "gui/itemUI/undress-hover.png"
                action Jump("resetSamShop")
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/reset.png"
                hover "gui/itemUI/reset-hover.png"
                action Jump("resetAlexShop")





    if shopCategory == 1:
        vbox xalign 0.972 yalign 0.012:
            imagebutton:
                idle "gui/itemUI/shopButtHead.png"
                hover "gui/itemUI/shopButtHead-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.012:
            imagebutton:
                idle "gui/itemUI/shopButtHead.png"
                hover "gui/itemUI/shopButtHead-hover.png"
                action SetVariable("shopCategory", 1), Jump("shopPrev")

    if shopCategory == 2:
        vbox xalign 0.972 yalign 0.13:
            imagebutton:
                idle "gui/itemUI/shopButtFace-hover.png"
                hover "gui/itemUI/shopButtFace-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.13:
            imagebutton:
                idle "gui/itemUI/shopButtFace.png"
                hover "gui/itemUI/shopButtFace-hover.png"
                action SetVariable("shopCategory", 2), Jump("shopPrev")

    if shopCategory == 3:
        vbox xalign 0.972 yalign 0.25:
            imagebutton:
                idle "gui/itemUI/shopButtNeck-hover.png"
                hover "gui/itemUI/shopButtNeck-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.25:
            imagebutton:
                idle "gui/itemUI/shopButtNeck.png"
                hover "gui/itemUI/shopButtNeck-hover.png"
                action SetVariable("shopCategory", 3), Jump("shopPrev")

    if shopCategory == 4:
        vbox xalign 0.972 yalign 0.37:
            imagebutton:
                idle "gui/itemUI/shopButtTop-hover.png"
                hover "gui/itemUI/shopButtTop-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.37:
            imagebutton:
                idle "gui/itemUI/shopButtTop.png"
                hover "gui/itemUI/shopButtTop-hover.png"
                action SetVariable("shopCategory", 4), Jump("shopPrev")

    if shopCategory == 5:
        vbox xalign 0.972 yalign 0.49:
            imagebutton:
                idle "gui/itemUI/shopButtWrist-hover.png"
                hover "gui/itemUI/shopButtWrist-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.49:
            imagebutton:
                idle "gui/itemUI/shopButtWrist.png"
                hover "gui/itemUI/shopButtWrist-hover.png"
                action SetVariable("shopCategory", 5), Jump("shopPrev")

    if shopCategory == 6:
        vbox xalign 0.972 yalign 0.61:
            imagebutton:
                idle "gui/itemUI/shopButtBott-hover.png"
                hover "gui/itemUI/shopButtBott-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.61:
            imagebutton:
                idle "gui/itemUI/shopButtBott.png"
                hover "gui/itemUI/shopButtBott-hover.png"
                action SetVariable("shopCategory", 6), Jump("shopPrev")

    if shopCategory == 7:
        vbox xalign 0.972 yalign 0.73:
            imagebutton:
                idle "gui/itemUI/shopButtShoes-hover.png"
                hover "gui/itemUI/shopButtShoes-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.73:
            imagebutton:
                idle "gui/itemUI/shopButtShoes.png"
                hover "gui/itemUI/shopButtShoes-hover.png"
                action SetVariable("shopCategory", 7), Jump("shopPrev")

    if shopCategory == 8:
        vbox xalign 0.972 yalign 0.85:
            imagebutton:
                idle "gui/itemUI/shopButtUndies-hover.png"
                hover "gui/itemUI/shopButtUndies-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.85:
            imagebutton:
                idle "gui/itemUI/shopButtUndies.png"
                hover "gui/itemUI/shopButtUndies-hover.png"
                action SetVariable("shopCategory", 8), Jump("shopPrev")

    if shopCategory == 9:
        vbox xalign 0.972 yalign 0.97:
            imagebutton:
                idle "gui/itemUI/shopButtSuits-hover.png"
                hover "gui/itemUI/shopButtSuits-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.97:
            imagebutton:
                idle "gui/itemUI/shopButtSuits.png"
                hover "gui/itemUI/shopButtSuits-hover.png"
                action SetVariable("shopCategory", 9), Jump("shopPrev")


    if shopCurrentSpy == 1:
        if shopCategory == 1:
            if hat6Sam == False:
                vbox xalign 0.24 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/hat/hat6mini.png"
                        hover "models/green/outfit/hat/hat6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("greenHat", 6)
                vbox xalign 0.22 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("hat6Sam", True)
                        else:
                            action Jump("shopNoCash")

            if hat10Sam == False and task3Stage >= 4:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/green/outfit/hat/hat10mini.png"
                        hover "models/green/outfit/hat/hat10mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("greenHat", 10)
                vbox xalign 0.1 yalign 0.69:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("hat10Sam", True)
                        else:
                            action Jump("shopNoCash")

            if hat12Sam == False:
                vbox xalign 0.5 yalign 0.8:
                    imagebutton:
                        idle "models/green/outfit/hat/hat12mini.png"
                        hover "models/green/outfit/hat/hat12mini-hover.png"
                        action SetVariable("shopItemSelect", 12), SetVariable("greenHat", 12)
                vbox xalign 0.48 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("hat12Sam", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 3:
            if neck2Sam == False:
                vbox xalign 0.11 yalign 0.27:
                    imagebutton:
                        idle "models/green/outfit/neck/neck2mini.png"
                        hover "models/green/outfit/neck/neck2mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("greenNeck", 2)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.150 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("neck2Sam", True)
                        else:
                            action Jump("shopNoCash")

            if neck10Sam == False and task6Stage >= 4:
                vbox xalign 0.11 yalign 0.81:
                    imagebutton:
                        idle "models/green/outfit/neck/neck10mini.png"
                        hover "models/green/outfit/neck/neck10mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("greenNeck", 10)
                vbox xalign 0.10 yalign 0.680:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.83:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("neck10Sam", True)
                        else:
                            action Jump("shopNoCash")

            if neck7Sam == False:
                vbox xalign 0.25 yalign 0.27:
                    imagebutton:
                        idle "models/green/outfit/neck/neck7mini.png"
                        hover "models/green/outfit/neck/neck7mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("greenNeck", 7)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("neck7Sam", True)
                        else:
                            action Jump("shopNoCash")

        if shopCategory == 4:
            if top3Sam == False:
                vbox xalign 0.11 yalign 0.27:
                    imagebutton:
                        idle "models/green/outfit/chest/top3mini.png"
                        hover "models/green/outfit/chest/top3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("greenChest", 3)
                vbox xalign 0.097 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.150 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("top3Sam", True)
                        else:
                            action Jump("shopNoCash")

            if top4Sam == False:
                vbox xalign 0.24 yalign 0.27:
                    imagebutton:
                        idle "models/green/outfit/chest/top4mini.png"
                        hover "models/green/outfit/chest/top4mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("greenChest", 4)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top4Sam", True)
                        else:
                            action Jump("shopNoCash")

            if top5Sam == False:
                vbox xalign 0.375 yalign 0.27:
                    imagebutton:
                        idle "models/green/outfit/chest/top5mini.png"
                        hover "models/green/outfit/chest/top5mini-hover.png"
                        action SetVariable("shopItemSelect", 3), SetVariable("greenChest", 5)
                vbox xalign 0.350 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$1200{/size}{/font}"

                vbox xalign 0.404 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 1200:
                            action SetVariable("cash", cash - 1200), SetVariable("top5Sam", True)
                        else:
                            action Jump("shopNoCash")

            if top6Sam == False:
                vbox xalign 0.24 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/chest/top6mini.png"
                        hover "models/green/outfit/chest/top6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("greenChest", 6)
                vbox xalign 0.225 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top6Sam", True)
                        else:
                            action Jump("shopNoCash")

            if top7Sam == False:
                vbox xalign 0.37 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/chest/top7mini.png"
                        hover "models/green/outfit/chest/top7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("greenChest", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top7Sam", True)
                        else:
                            action Jump("shopNoCash")

            if top9Sam == False:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/green/outfit/chest/top9mini.png"
                        hover "models/green/outfit/chest/top9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("greenChest", 9)
                vbox xalign 0.1 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top9Sam", True)
                        else:
                            action Jump("shopNoCash")

            if top10Sam == False and specialCandyStatus >= 3:
                vbox xalign 0.24 yalign 0.82:
                    imagebutton:
                        idle "models/green/outfit/chest/top10mini.png"
                        hover "models/green/outfit/chest/top10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("greenChest", 10)
                vbox xalign 0.22 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top10Sam", True)
                        else:
                            action Jump("shopNoCash")

            if top12Sam == False:
                vbox xalign 0.5 yalign 0.82:
                    imagebutton:
                        idle "models/green/outfit/chest/top12mini.png"
                        hover "models/green/outfit/chest/top12mini-hover.png"
                        action SetVariable("shopItemSelect", 12), SetVariable("greenChest", 12)
                vbox xalign 0.48 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top12Sam", True)
                        else:
                            action Jump("shopNoCash")

        if shopCategory == 6:
            if bott3Sam == False:
                vbox xalign 0.11 yalign 0.25:
                    imagebutton:
                        idle "models/green/outfit/bott/bott3mini.png"
                        hover "models/green/outfit/bott/bott3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("greenBottom", 3)
                vbox xalign 0.10 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.15 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("bott3Sam", True)
                        else:
                            action Jump("shopNoCash")

            if bott5Sam == False:
                vbox xalign 0.245 yalign 0.27:
                    imagebutton:
                        idle "models/green/outfit/bott/bott5mini.png"
                        hover "models/green/outfit/bott/bott5mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("greenBottom", 5)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("bott5Sam", True)
                        else:
                            action Jump("shopNoCash")

            if bott6Sam == False:
                vbox xalign 0.24 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/bott/bott6mini.png"
                        hover "models/green/outfit/bott/bott6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("greenBottom", 6)
                vbox xalign 0.225 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott6Sam", True)
                        else:
                            action Jump("shopNoCash")

            if bott7Sam == False:
                vbox xalign 0.37 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/bott/bott7mini.png"
                        hover "models/green/outfit/bott/bott7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("greenBottom", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott7Sam", True)
                        else:
                            action Jump("shopNoCash")

            if bott9Sam == False:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/green/outfit/bott/bott9mini.png"
                        hover "models/green/outfit/bott/bott9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("greenBottom", 9)
                vbox xalign 0.1 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott9Sam", True)
                        else:
                            action Jump("shopNoCash")

            if bott10Sam == False:
                vbox xalign 0.24 yalign 0.81:
                    imagebutton:
                        idle "models/green/outfit/bott/bott10mini.png"
                        hover "models/green/outfit/bott/bott10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("greenBottom", 10)
                vbox xalign 0.225 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.83:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott10Sam", True)
                        else:
                            action Jump("shopNoCash")

            if bott12Sam == False:
                vbox xalign 0.5 yalign 0.82:
                    imagebutton:
                        idle "models/green/outfit/bott/bott12mini.png"
                        hover "models/green/outfit/bott/bott12mini-hover.png"
                        action SetVariable("shopItemSelect", 12), SetVariable("greenBottom", 12)
                vbox xalign 0.48 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott12Sam", True)
                        else:
                            action Jump("shopNoCash")

        if shopCategory == 7:
            if shoes5Sam == False:
                vbox xalign 0.11 yalign 0.26:
                    imagebutton:
                        idle "models/green/outfit/shoes/shoes5mini.png"
                        hover "models/green/outfit/shoes/shoes5mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("greenShoes", 5)
                vbox xalign 0.10 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.15 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("shoes5Sam", True)
                        else:
                            action Jump("shopNoCash")

            if shoes7Sam == False:
                vbox xalign 0.37 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/shoes/shoes7mini.png"
                        hover "models/green/outfit/shoes/shoes7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("greenShoes", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes7Sam", True)
                        else:
                            action Jump("shopNoCash")

            if shoes8Sam == False and slutLevel >= 3:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/shoes/shoes8mini.png"
                        hover "models/green/outfit/shoes/shoes8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("greenShoes", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("shoes8Sam", True)
                        else:
                            action Jump("shopNoCash")

            if shoes9Sam == False:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/green/outfit/shoes/shoes9mini.png"
                        hover "models/green/outfit/shoes/shoes9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("greenShoes", 9)
                vbox xalign 0.1 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes9Sam", True)
                        else:
                            action Jump("shopNoCash")

            if shoes10Sam == False and task6Stage >= 4:
                vbox xalign 0.24 yalign 0.81:
                    imagebutton:
                        idle "models/green/outfit/shoes/shoes10mini.png"
                        hover "models/green/outfit/shoes/shoes10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("greenShoes", 10)
                vbox xalign 0.225 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.83:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes10Sam", True)
                        else:
                            action Jump("shopNoCash")

            if shoes12Sam == False:
                vbox xalign 0.5 yalign 0.8:
                    imagebutton:
                        idle "models/green/outfit/shoes/shoes12mini.png"
                        hover "models/green/outfit/shoes/shoes12mini-hover.png"
                        action SetVariable("shopItemSelect", 12), SetVariable("greenShoes", 12)
                vbox xalign 0.48 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes12Sam", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 8:
            if under2Sam == False:
                vbox xalign 0.245 yalign 0.25:
                    imagebutton:
                        idle "models/green/outfit/under/under2mini.png"
                        hover "models/green/outfit/under/under2mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 2),
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under2Sam", True)
                        else:
                            action Jump("shopNoCash")

            if under3Sam == False and slutLevel >= 3:
                vbox xalign 0.375 yalign 0.25:
                    imagebutton:
                        idle "models/green/outfit/under/under3mini.png"
                        hover "models/green/outfit/under/under3mini-hover.png"
                        action SetVariable("shopItemSelect", 3), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 3)
                vbox xalign 0.35 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under3Sam", True)
                        else:
                            action Jump("shopNoCash")

            if under4Sam == False:
                vbox xalign 0.50 yalign 0.25:
                    imagebutton:
                        idle "models/green/outfit/under/under4mini.png"
                        hover "models/green/outfit/under/under4mini-hover.png"
                        action SetVariable("shopItemSelect", 4), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 4),
                vbox xalign 0.475 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$250{/size}{/font}"

                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 250:
                            action SetVariable("cash", cash - 250), SetVariable("under4Sam", True)
                        else:
                            action Jump("shopNoCash")

            if under7Sam == False:
                vbox xalign 0.12 yalign 0.53:
                    imagebutton:
                        idle "models/green/outfit/under/under7mini.png"
                        hover "models/green/outfit/under/under7mini-hover.png"
                        action SetVariable("shopItemSelect", 5), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 7),
                vbox xalign 0.1 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under7Sam", True)
                        else:
                            action Jump("shopNoCash")

            if under8Sam == False and slutLevel >= 3:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/green/outfit/under/under8mini.png"
                        hover "models/green/outfit/under/under8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 8),
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under8Sam", True)
                        else:
                            action Jump("shopNoCash")

            if under9Sam == False and slutLevel >= 2:
                vbox xalign 0.12 yalign 0.8:
                    imagebutton:
                        idle "models/green/outfit/under/under9mini.png"
                        hover "models/green/outfit/under/under9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 9),
                vbox xalign 0.1 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$300{/size}{/font}"

                vbox xalign 0.153 yalign 0.836:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 300:
                            action SetVariable("cash", cash - 300), SetVariable("under9Sam", True)
                        else:
                            action Jump("shopNoCash")

            if under10Sam == False and slutLevel >= 3:
                vbox xalign 0.245 yalign 0.8:
                    imagebutton:
                        idle "models/green/outfit/under/under10mini.png"
                        hover "models/green/outfit/under/under10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 10)
                vbox xalign 0.22 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$200{/size}{/font}"

                vbox xalign 0.28 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 200:
                            action SetVariable("cash", cash - 200), SetVariable("under10Sam", True)
                        else:
                            action Jump("shopNoCash")

            if under11Sam == False and slutLevel >= 3:
                vbox xalign 0.375 yalign 0.8:
                    imagebutton:
                        idle "models/green/outfit/under/under11mini.png"
                        hover "models/green/outfit/under/under11mini-hover.png"
                        action SetVariable("shopItemSelect", 11), SetVariable("greenChest", 0), SetVariable("greenBottom", 0), SetVariable("greenUnder", 11)
                vbox xalign 0.35 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$300{/size}{/font}"

                vbox xalign 0.405 yalign 0.836:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 300:
                            action SetVariable("cash", cash - 300), SetVariable("under11Sam", True)
                        else:
                            action Jump("shopNoCash")




















    if shopCurrentSpy == 2:
        if shopCategory == 1:
            if hat5Clover == False and specialDragonStatus >= 3:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/red/outfit/hat/hat5mini.png"
                        hover "models/red/outfit/hat/hat5mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("redHat", 5)
                vbox xalign 0.1 yalign 0.69:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("hat5Clover", True)
                        else:
                            action Jump("shopNoCash")

            if hat7Clover == False:
                vbox xalign 0.37 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/hat/hat7mini.png"
                        hover "models/red/outfit/hat/hat7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("redHat", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("hat7Clover", True)
                        else:
                            action Jump("shopNoCash")

            if hat8Clover == False:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/hat/hat8mini.png"
                        hover "models/red/outfit/hat/hat8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("redHat", 8)
                vbox xalign 0.47 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("hat8Clover", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 3:
            if neck2Clover == False:
                vbox xalign 0.11 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/neck/neck2mini.png"
                        hover "models/red/outfit/neck/neck2mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("redNeck", 2)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.151 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("neck2Clover", True)
                        else:
                            action Jump("shopNoCash")

            if neck7Clover == False:
                vbox xalign 0.24 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/neck/neck7mini.png"
                        hover "models/red/outfit/neck/neck7mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("redNeck", 7)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("neck7Clover", True)
                        else:
                            action Jump("shopNoCash")

            if neck8Clover == False:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/neck/neck8mini.png"
                        hover "models/red/outfit/neck/neck8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("redNeck", 8)
                vbox xalign 0.47 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$300{/size}{/font}"

                vbox xalign 0.53 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 300:
                            action SetVariable("cash", cash - 300), SetVariable("neck8Clover", True)
                        else:
                            action Jump("shopNoCash")

            if neck9Clover == False:
                vbox xalign 0.11 yalign 0.8:
                    imagebutton:
                        idle "models/red/outfit/neck/neck9mini.png"
                        hover "models/red/outfit/neck/neck9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("redNeck", 9)
                vbox xalign 0.1 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("neck9Clover", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 4:
            if top3Clover == False:
                vbox xalign 0.11 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/chest/top3mini.png"
                        hover "models/red/outfit/chest/top3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("redChest", 3)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.153 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("top3Clover", True)
                        else:
                            action Jump("shopNoCash")

            if top4Clover == False:
                vbox xalign 0.240 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/chest/top4mini.png"
                        hover "models/red/outfit/chest/top4mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("redChest", 4)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$950{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 950:
                            action SetVariable("cash", cash - 950), SetVariable("top4Clover", True)
                        else:
                            action Jump("shopNoCash")

            if punkRank >= 3 and top5Clover == False:
                vbox xalign 0.375 yalign 0.27:
                    imagebutton:
                        idle "models/red/outfit/chest/top5mini.png"
                        hover "models/red/outfit/chest/top5mini-hover.png"
                        action SetVariable("shopItemSelect", 3), SetVariable("redChest", 5), SetVariable("redBottom", 0)
                vbox xalign 0.350 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.404 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top5Clover", True)
                        else:
                            action Jump("shopNoCash")

            if top6Clover == False:
                vbox xalign 0.240 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/chest/top6mini.png"
                        hover "models/red/outfit/chest/top6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("redChest", 6)
                vbox xalign 0.225 yalign 0.445:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$850{/size}{/font}"

                vbox xalign 0.279 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 850:
                            action SetVariable("cash", cash - 850), SetVariable("top6Clover", True)
                        else:
                            action Jump("shopNoCash")

            if top7Clover == False:
                vbox xalign 0.37 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/chest/top7mini.png"
                        hover "models/red/outfit/chest/top7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("redChest", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top7Clover", True)
                        else:
                            action Jump("shopNoCash")

            if top8Clover == False:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/chest/top8mini.png"
                        hover "models/red/outfit/chest/top8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("redChest", 8)
                vbox xalign 0.47 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$700{/size}{/font}"

                vbox xalign 0.53 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 700:
                            action SetVariable("cash", cash - 700), SetVariable("top8Clover", True)
                        else:
                            action Jump("shopNoCash")

            if top9Clover == False:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/red/outfit/chest/top9mini.png"
                        hover "models/red/outfit/chest/top9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("redChest", 9)
                vbox xalign 0.1 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top9Clover", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 5:
            if wristAcc7Clover == False:
                vbox xalign 0.37 yalign 0.55:
                    imagebutton:
                        idle "models/red/outfit/acc2/acc7mini.png"
                        hover "models/red/outfit/acc2/acc7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("redAcces2", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$200{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 200:
                            action SetVariable("cash", cash - 200), SetVariable("wristAcc7Clover", True)
                        else:
                            action Jump("shopNoCash")

            if wristAcc8Clover == False:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/acc2/acc8mini.png"
                        hover "models/red/outfit/acc2/acc8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("redAcces2", 8)
                vbox xalign 0.47 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.53 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("wristAcc8Clover", True)
                        else:
                            action Jump("shopNoCash")



        if shopCategory == 6:
            if bott3Clover == False:
                vbox xalign 0.11 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/bott/bott3mini.png"
                        hover "models/red/outfit/bott/bott3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("redBottom", 3)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott3Clover", True)
                        else:
                            action Jump("shopNoCash")

            if bott4Clover == False:
                vbox xalign 0.240 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/bott/bott4mini.png"
                        hover "models/red/outfit/bott/bott4mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("redBottom", 4)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott4Clover", True)
                        else:
                            action Jump("shopNoCash")

            if bott6Clover == False:
                vbox xalign 0.240 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/bott/bott6mini.png"
                        hover "models/red/outfit/bott/bott6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("redBottom", 6)
                vbox xalign 0.225 yalign 0.445:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.279 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott6Clover", True)
                        else:
                            action Jump("shopNoCash")

            if bott7Clover == False:
                vbox xalign 0.37 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/bott/bott7mini.png"
                        hover "models/red/outfit/bott/bott7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("redBottom", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott7Clover", True)
                        else:
                            action Jump("shopNoCash")

            if bott8Clover == False:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/bott/bott8mini.png"
                        hover "models/red/outfit/bott/bott8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("redBottom", 8)
                vbox xalign 0.47 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott8Clover", True)
                        else:
                            action Jump("shopNoCash")

            if bott9Clover == False:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/red/outfit/bott/bott9mini.png"
                        hover "models/red/outfit/bott/bott9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("redBottom", 9)
                vbox xalign 0.1 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott9Clover", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 7:
            if shoes3Clover == False:
                vbox xalign 0.11 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/shoes/shoes3mini.png"
                        hover "models/red/outfit/shoes/shoes3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("redShoes", 3)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes3Clover", True)
                        else:
                            action Jump("shopNoCash")

            if shoes4Clover == False:
                vbox xalign 0.240 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/shoes/shoes4mini.png"
                        hover "models/red/outfit/shoes/shoes4mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("redShoes", 4)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes4Clover", True)
                        else:
                            action Jump("shopNoCash")

            if shoes5Clover == False and specialSebStatus >= 3:
                vbox xalign 0.11 yalign 0.53:
                    imagebutton:
                        idle "models/red/outfit/shoes/shoes5mini.png"
                        hover "models/red/outfit/shoes/shoes5mini-hover.png"
                        action SetVariable("shopItemSelect", 5), SetVariable("redShoes", 5)
                vbox xalign 0.1 yalign 0.44:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes5Clover", True)
                        else:
                            action Jump("shopNoCash")

            if shoes6Clover == False:
                vbox xalign 0.240 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/shoes/shoes6mini.png"
                        hover "models/red/outfit/shoes/shoes6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("redShoes", 6)
                vbox xalign 0.225 yalign 0.445:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.279 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("shoes6Clover", True)
                        else:
                            action Jump("shopNoCash")

            if shoes7Clover == False:
                vbox xalign 0.37 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/shoes/shoes7mini.png"
                        hover "models/red/outfit/shoes/shoes7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("redShoes", 7)
                vbox xalign 0.355 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.60:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes7Clover", True)
                        else:
                            action Jump("shopNoCash")

            if shoes8Clover == False and slutLevel >= 3:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/shoes/shoes8mini.png"
                        hover "models/red/outfit/shoes/shoes8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("redShoes", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("shoes8Clover", True)
                        else:
                            action Jump("shopNoCash")

            if shoes9Clover == False:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/red/outfit/shoes/shoes9mini.png"
                        hover "models/red/outfit/shoes/shoes9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("redShoes", 9)
                vbox xalign 0.1 yalign 0.685:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("shoes9Clover", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 8:
            if under2Clover == False:
                vbox xalign 0.24 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/under/under2mini.png"
                        hover "models/red/outfit/under/under2mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 2)
                vbox xalign 0.22 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under2Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under3Clover == False:
                vbox xalign 0.375 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/under/under3mini.png"
                        hover "models/red/outfit/under/under3mini-hover.png"
                        action SetVariable("shopItemSelect", 3), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 3)
                vbox xalign 0.35 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under3Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under4Clover == False:
                vbox xalign 0.50 yalign 0.25:
                    imagebutton:
                        idle "models/red/outfit/under/under4mini.png"
                        hover "models/red/outfit/under/under4mini-hover.png"
                        action SetVariable("shopItemSelect", 4), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 4)
                vbox xalign 0.47 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$250{/size}{/font}"

                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 250:
                            action SetVariable("cash", cash - 250), SetVariable("under4Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under5Clover == False:
                vbox xalign 0.12 yalign 0.53:
                    imagebutton:
                        idle "models/red/outfit/under/under5mini.png"
                        hover "models/red/outfit/under/under5mini-hover.png"
                        action SetVariable("shopItemSelect", 5), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 5)
                vbox xalign 0.1 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under5Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under6Clover == False:
                vbox xalign 0.240 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/under/under6mini.png"
                        hover "models/red/outfit/under/under6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 6),
                vbox xalign 0.225 yalign 0.445:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.279 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("under6Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under7Clover == False:
                vbox xalign 0.375 yalign 0.53:
                    imagebutton:
                        idle "models/red/outfit/under/under7mini.png"
                        hover "models/red/outfit/under/under7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 7)
                vbox xalign 0.35 yalign 0.455:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.405 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("under7Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under8Clover == False and slutLevel >= 3:
                vbox xalign 0.5 yalign 0.52:
                    imagebutton:
                        idle "models/red/outfit/under/under8mini.png"
                        hover "models/red/outfit/under/under8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("under8Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under9Clover == False and slutLevel >= 2:
                vbox xalign 0.11 yalign 0.8:
                    imagebutton:
                        idle "models/red/outfit/under/under9mini.png"
                        hover "models/red/outfit/under/under9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 9)
                vbox xalign 0.1 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$300{/size}{/font}"

                vbox xalign 0.153 yalign 0.836:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 300:
                            action SetVariable("cash", cash - 300), SetVariable("under9Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under10Clover == False and slutLevel >= 3:
                vbox xalign 0.245 yalign 0.8:
                    imagebutton:
                        idle "models/red/outfit/under/under10mini.png"
                        hover "models/red/outfit/under/under10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 10)
                vbox xalign 0.22 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$200{/size}{/font}"

                vbox xalign 0.28 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 200:
                            action SetVariable("cash", cash - 200), SetVariable("under10Clover", True)
                        else:
                            action Jump("shopNoCash")

            if under11Clover == False and slutLevel >= 3:
                vbox xalign 0.375 yalign 0.8:
                    imagebutton:
                        idle "models/red/outfit/under/under11mini.png"
                        hover "models/red/outfit/under/under11mini-hover.png"
                        action SetVariable("shopItemSelect", 11), SetVariable("redChest", 0), SetVariable("redBottom", 0), SetVariable("redUnder", 11)
                vbox xalign 0.35 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$300{/size}{/font}"

                vbox xalign 0.405 yalign 0.836:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 300:
                            action SetVariable("cash", cash - 300), SetVariable("under11Clover", True)
                        else:
                            action Jump("shopNoCash")


    if shopCurrentSpy == 3:

        if shopCategory == 3:
            if neck1Alex == False:
                vbox xalign 0.115 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/neck/neck1mini.png"
                        hover "models/yellow/outfit/neck/neck1mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("yellowNeck", 1)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.153 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("neck1Alex", True)
                        else:
                            action Jump("shopNoCash")

            if neck2Alex == False:
                vbox xalign 0.25 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/neck/neck2mini.png"
                        hover "models/yellow/outfit/neck/neck2mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("yellowNeck", 2)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$450{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 450:
                            action SetVariable("cash", cash - 450), SetVariable("neck2Alex", True)
                        else:
                            action Jump("shopNoCash")

            if neck8Alex == False:
                vbox xalign 0.5 yalign 0.51:
                    imagebutton:
                        idle "models/yellow/outfit/neck/neck8mini.png"
                        hover "models/yellow/outfit/neck/neck8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("yellowNeck", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("neck8Alex", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 1:
            if hat5Alex == False:
                vbox xalign 0.115 yalign 0.54:
                    imagebutton:
                        idle "models/yellow/outfit/hat/hat5mini.png"
                        hover "models/yellow/outfit/hat/hat5mini-hover.png"
                        action SetVariable("shopItemSelect", 5), SetVariable("yellowHat", 5)
                vbox xalign 0.1 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("hat5Alex", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 4:
            if top3Alex == False:
                vbox xalign 0.115 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/chest/top3mini.png"
                        hover "models/yellow/outfit/chest/top3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("yellowChest", 3)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$540{/size}{/font}"

                vbox xalign 0.153 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 540:
                            action SetVariable("cash", cash - 540), SetVariable("top3Alex", True)
                        else:
                            action Jump("shopNoCash")

            if top4Alex == False:
                vbox xalign 0.25 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/chest/top4mini.png"
                        hover "models/yellow/outfit/chest/top4mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("yellowChest", 4)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top4Alex", True)
                        else:
                            action Jump("shopNoCash")

            if top5Alex == False:
                vbox xalign 0.12 yalign 0.53:
                    imagebutton:
                        idle "models/yellow/outfit/chest/top5mini.png"
                        hover "models/yellow/outfit/chest/top5mini-hover.png"
                        action SetVariable("shopItemSelect", 5), SetVariable("yellowChest", 5)
                vbox xalign 0.1 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.15 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top5Alex", True)
                        else:
                            action Jump("shopNoCash")

            if top6Alex == False:
                vbox xalign 0.24 yalign 0.53:
                    imagebutton:
                        idle "models/yellow/outfit/chest/top6mini.png"
                        hover "models/yellow/outfit/chest/top6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("yellowChest", 6)
                vbox xalign 0.225 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.279 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top6Alex", True)
                        else:
                            action Jump("shopNoCash")

            if top8Alex == False:
                vbox xalign 0.5 yalign 0.51:
                    imagebutton:
                        idle "models/yellow/outfit/chest/top8mini.png"
                        hover "models/yellow/outfit/chest/top8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("yellowChest", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("top8Alex", True)
                        else:
                            action Jump("shopNoCash")

            if top10Alex == False and outsideRank >= 3:
                vbox xalign 0.11 yalign 0.82:
                    imagebutton:
                        idle "models/yellow/outfit/chest/top10mini.png"
                        hover "models/yellow/outfit/chest/top10mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("yellowChest", 10)
                vbox xalign 0.1 yalign 0.69:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("top10Alex", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 5:
            if wristAcc8Alex == False:
                vbox xalign 0.5 yalign 0.51:
                    imagebutton:
                        idle "models/yellow/outfit/acc2/acc8mini.png"
                        hover "models/yellow/outfit/acc2/acc8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("yellowAcces2", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("wristAcc8Alex", True)
                        else:
                            action Jump("shopNoCash")

            if wristAcc9Alex == False:
                vbox xalign 0.12 yalign 0.8:
                    imagebutton:
                        idle "models/yellow/outfit/acc2/acc9mini.png"
                        hover "models/yellow/outfit/acc2/acc9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("yellowAcces2", 9)
                vbox xalign 0.1 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.15 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("wristAcc9Alex", True)
                        else:
                            action Jump("shopNoCash")

            if wristAcc10Alex == False and outsideRank >= 2:
                vbox xalign 0.25 yalign 0.82:
                    imagebutton:
                        idle "models/yellow/outfit/acc2/acc10mini.png"
                        hover "models/yellow/outfit/acc2/acc10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("yellowAcces2", 10)
                vbox xalign 0.225 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.28 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("wristAcc10Alex", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 6:
            if bott3Alex == False:
                vbox xalign 0.115 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/bott/bott3mini.png"
                        hover "models/yellow/outfit/bott/bott3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("yellowBottom", 3)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.153 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott3Alex", True)
                        else:
                            action Jump("shopNoCash")

            if bott4Alex == False:
                vbox xalign 0.25 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/bott/bott4mini.png"
                        hover "models/yellow/outfit/bott/bott4mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("yellowBottom", 4)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$900{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 900:
                            action SetVariable("cash", cash - 900), SetVariable("bott4Alex", True)
                        else:
                            action Jump("shopNoCash")

            if bott6Alex == False:
                vbox xalign 0.25 yalign 0.52:
                    imagebutton:
                        idle "models/yellow/outfit/bott/bott6mini.png"
                        hover "models/yellow/outfit/bott/bott6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("yellowBottom", 6)
                vbox xalign 0.225 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.279 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("bott6Alex", True)
                        else:
                            action Jump("shopNoCash")

            if bott8Alex == False:
                vbox xalign 0.5 yalign 0.51:
                    imagebutton:
                        idle "models/yellow/outfit/bott/bott8mini.png"
                        hover "models/yellow/outfit/bott/bott8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("yellowBottom", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 600:
                            action SetVariable("cash", cash - 600), SetVariable("bott8Alex", True)
                        else:
                            action Jump("shopNoCash")

            if bott10Alex == False and outsideRank >= 3:
                vbox xalign 0.11 yalign 0.8:
                    imagebutton:
                        idle "models/yellow/outfit/bott/bott10mini.png"
                        hover "models/yellow/outfit/bott/bott10mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("yellowBottom", 10)
                vbox xalign 0.1 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$580{/size}{/font}"

                vbox xalign 0.155 yalign 0.832:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 580:
                            action SetVariable("cash", cash - 580), SetVariable("bott10Alex", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 7:
            if shoes3Alex == False:
                vbox xalign 0.115 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/shoes/shoes3mini.png"
                        hover "models/yellow/outfit/shoes/shoes3mini-hover.png"
                        action SetVariable("shopItemSelect", 1), SetVariable("yellowShoes", 3)
                vbox xalign 0.1 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.153 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("shoes3Alex", True)
                        else:
                            action Jump("shopNoCash")

            if shoes4Alex == False:
                vbox xalign 0.25 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/shoes/shoes4mini.png"
                        hover "models/yellow/outfit/shoes/shoes4mini-hover.png"
                        action SetVariable("shopItemSelect", 2), SetVariable("yellowShoes", 4)
                vbox xalign 0.225 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$450{/size}{/font}"

                vbox xalign 0.279 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 450:
                            action SetVariable("cash", cash - 450), SetVariable("shoes4Alex", True)
                        else:
                            action Jump("shopNoCash")

            if shoes5Alex == False:
                vbox xalign 0.12 yalign 0.53:
                    imagebutton:
                        idle "models/yellow/outfit/shoes/shoes5mini.png"
                        hover "models/yellow/outfit/shoes/shoes5mini-hover.png"
                        action SetVariable("shopItemSelect", 5), SetVariable("yellowShoes", 5)
                vbox xalign 0.1 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$450{/size}{/font}"

                vbox xalign 0.15 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 450:
                            action SetVariable("cash", cash - 450), SetVariable("shoes5Alex", True)
                        else:
                            action Jump("shopNoCash")

            if shoes6Alex == False:
                vbox xalign 0.24 yalign 0.52:
                    imagebutton:
                        idle "models/yellow/outfit/shoes/shoes6mini.png"
                        hover "models/yellow/outfit/shoes/shoes6mini-hover.png"
                        action SetVariable("shopItemSelect", 6), SetVariable("yellowShoes", 6.1)
                vbox xalign 0.225 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$450{/size}{/font}"

                vbox xalign 0.279 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 450:
                            action SetVariable("cash", cash - 450), SetVariable("shoes6Alex", True)
                        else:
                            action Jump("shopNoCash")

            if shoes8Alex == False:
                vbox xalign 0.5 yalign 0.51:
                    imagebutton:
                        idle "models/yellow/outfit/shoes/shoes8mini.png"
                        hover "models/yellow/outfit/shoes/shoes8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("yellowShoes", 8)
                vbox xalign 0.475 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("shoes8Alex", True)
                        else:
                            action Jump("shopNoCash")

            if shoes9Alex == False and slutLevel >= 3:
                vbox xalign 0.11 yalign 0.815:
                    imagebutton:
                        idle "models/yellow/outfit/shoes/shoes9mini.png"
                        hover "models/yellow/outfit/shoes/shoes9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("yellowShoes", 9)
                vbox xalign 0.1 yalign 0.69:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$550{/size}{/font}"

                vbox xalign 0.153 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 550:
                            action SetVariable("cash", cash - 550), SetVariable("shoes9Alex", True)
                        else:
                            action Jump("shopNoCash")

            if shoes10Alex == False and outsideRank >= 3:
                vbox xalign 0.245 yalign 0.82:
                    imagebutton:
                        idle "models/yellow/outfit/shoes/shoes10mini.png"
                        hover "models/yellow/outfit/shoes/shoes10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("yellowShoes", 10)
                vbox xalign 0.22 yalign 0.69:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$550{/size}{/font}"

                vbox xalign 0.28 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 550:
                            action SetVariable("cash", cash - 550), SetVariable("shoes10Alex", True)
                        else:
                            action Jump("shopNoCash")


        if shopCategory == 8:
            if under4Alex == False:
                vbox xalign 0.50 yalign 0.25:
                    imagebutton:
                        idle "models/yellow/outfit/under/under4mini.png"
                        hover "models/yellow/outfit/under/under4mini-hover.png"
                        action SetVariable("shopItemSelect", 4), SetVariable("yellowChest", 0), SetVariable("yellowBottom", 0), SetVariable("yellowUnder", 4)
                vbox xalign 0.47 yalign 0.225:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$450{/size}{/font}"

                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 450:
                            action SetVariable("cash", cash - 450), SetVariable("under4Alex", True)
                        else:
                            action Jump("shopNoCash")

            if under5Alex == False:
                vbox xalign 0.12 yalign 0.53:
                    imagebutton:
                        idle "models/yellow/outfit/under/under5mini.png"
                        hover "models/yellow/outfit/under/under5mini-hover.png"
                        action SetVariable("shopItemSelect", 5), SetVariable("yellowChest", 0), SetVariable("yellowBottom", 0), SetVariable("yellowUnder", 5),
                vbox xalign 0.1 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.15 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("under5Alex", True)
                        else:
                            action Jump("shopNoCash")

            if under7Alex == False and slutLevel >= 3:
                vbox xalign 0.38 yalign 0.53:
                    imagebutton:
                        idle "models/yellow/outfit/under/under7mini.png"
                        hover "models/yellow/outfit/under/under7mini-hover.png"
                        action SetVariable("shopItemSelect", 7), SetVariable("yellowChest", 0), SetVariable("yellowBottom", 0), SetVariable("yellowUnder", 7),
                vbox xalign 0.35 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$400{/size}{/font}"

                vbox xalign 0.405 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 400:
                            action SetVariable("cash", cash - 400), SetVariable("under7Alex", True)
                        else:
                            action Jump("shopNoCash")

            if under8Alex == False:
                vbox xalign 0.5 yalign 0.53:
                    imagebutton:
                        idle "models/yellow/outfit/under/under8mini.png"
                        hover "models/yellow/outfit/under/under8mini-hover.png"
                        action SetVariable("shopItemSelect", 8), SetVariable("yellowChest", 0), SetVariable("yellowBottom", 0), SetVariable("yellowUnder", 8),
                vbox xalign 0.47 yalign 0.45:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$300{/size}{/font}"

                vbox xalign 0.53 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 300:
                            action SetVariable("cash", cash - 300), SetVariable("under8Alex", True)
                        else:
                            action Jump("shopNoCash")

            if under9Alex == False and slutLevel >= 3:
                vbox xalign 0.12 yalign 0.8:
                    imagebutton:
                        idle "models/yellow/outfit/under/under9mini.png"
                        hover "models/yellow/outfit/under/under9mini-hover.png"
                        action SetVariable("shopItemSelect", 9), SetVariable("yellowChest", 0), SetVariable("yellowBottom", 0), SetVariable("yellowUnder", 9),
                vbox xalign 0.1 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$500{/size}{/font}"

                vbox xalign 0.15 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 500:
                            action SetVariable("cash", cash - 500), SetVariable("under9Alex", True)
                        else:
                            action Jump("shopNoCash")

            if under10Alex == False and slutLevel >= 3:
                vbox xalign 0.245 yalign 0.8:
                    imagebutton:
                        idle "models/yellow/outfit/under/under10mini.png"
                        hover "models/yellow/outfit/under/under10mini-hover.png"
                        action SetVariable("shopItemSelect", 10), SetVariable("yellowChest", 0), SetVariable("yellowBottom", 0), SetVariable("yellowUnder", 10)
                vbox xalign 0.22 yalign 0.68:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$200{/size}{/font}"

                vbox xalign 0.28 yalign 0.835:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 200:
                            action SetVariable("cash", cash - 200), SetVariable("under10Alex", True)
                        else:
                            action Jump("shopNoCash")


    if shopItemSelect == 1:
        vbox xalign 0.097 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 2:
        vbox xalign 0.235 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 3:
        vbox xalign 0.368 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 4:
        vbox xalign 0.50 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 5:
        vbox xalign 0.097 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 6:
        vbox xalign 0.235 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 7:
        vbox xalign 0.368 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 8:
        vbox xalign 0.50 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 9:
        vbox xalign 0.097 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 10:
        vbox xalign 0.235 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 11:
        vbox xalign 0.368 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 12:
        vbox xalign 0.50 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"


label shopAddup:
    $ shopTotal = 0


    if shopHeadSelect == 10:
        $ shopTotal += 1000
    if shopNeckSelect == 2:
        $ shopTotal += 500
    if shopNeckSelect == 7:
        $ shopTotal += 500

    if shopChestSelect == 3:
        $ shopTotal += 500
    if shopChestSelect == 4:
        $ shopTotal += 800
    if shopChestSelect == 5:
        $ shopTotal += 1200

    if shopBottSelect == 3:
        $ shopTotal += 400
    if shopBottSelect == 5:
        $ shopTotal += 500

    if shopShoeSelect == 5:
        $ shopTotal += 600
    if shopShoeSelect == 10:
        $ shopTotal += 1000

    if shopUnderSelect == 4:
        $ shopTotal += 450


    if 1 <= shopPubicGreenSelect <= 7:
        $ shopTotal += 100



    if shopTattooHeadSelect == 1:
        $ shopTotal += 100
    if shopTattooHeadSelect == 2:
        $ shopTotal += 100
    if shopTattooHeadSelect == 3:
        $ shopTotal += 100
    if shopTattooHeadSelect == 4:
        $ shopTotal += 100
    if shopTattooHeadSelect == 5:
        $ shopTotal += 100
    if shopTattooHeadSelect == 6:
        $ shopTotal += 50


    if shopTattooChestSelect == 1:
        $ shopTotal += 100
    if shopTattooChestSelect == 2:
        $ shopTotal += 100
    if shopTattooChestSelect == 3:
        $ shopTotal += 100
    if shopTattooChestSelect == 4:
        $ shopTotal += 100
    if shopTattooChestSelect == 5:
        $ shopTotal += 100
    if shopTattooChestSelect == 6:
        $ shopTotal += 50


    if shopTattooArmSelect == 1:
        $ shopTotal += 100
    if shopTattooArmSelect == 2:
        $ shopTotal += 100
    if shopTattooArmSelect == 3:
        $ shopTotal += 100
    if shopTattooArmSelect == 4:
        $ shopTotal += 100
    if shopTattooArmSelect == 5:
        $ shopTotal += 100
    if shopTattooArmSelect == 6:
        $ shopTotal += 50


    if shopTattooBellySelect == 1:
        $ shopTotal += 100
    if shopTattooBellySelect == 2:
        $ shopTotal += 100
    if shopTattooBellySelect == 3:
        $ shopTotal += 100
    if shopTattooBellySelect == 4:
        $ shopTotal += 100
    if shopTattooBellySelect == 5:
        $ shopTotal += 100
    if shopTattooBellySelect == 6:
        $ shopTotal += 50


    if shopTattooCrotchSelect == 1:
        $ shopTotal += 100
    if shopTattooCrotchSelect == 2:
        $ shopTotal += 100
    if shopTattooCrotchSelect == 3:
        $ shopTotal += 100
    if shopTattooCrotchSelect == 4:
        $ shopTotal += 100
    if shopTattooCrotchSelect == 5:
        $ shopTotal += 100
    if shopTattooCrotchSelect == 6:
        $ shopTotal += 50


    if shopTattooLegSelect == 1:
        $ shopTotal += 100
    if shopTattooLegSelect == 2:
        $ shopTotal += 100
    if shopTattooLegSelect == 3:
        $ shopTotal += 100
    if shopTattooLegSelect == 4:
        $ shopTotal += 100
    if shopTattooLegSelect == 5:
        $ shopTotal += 100
    if shopTattooLegSelect == 6:
        $ shopTotal += 50



    if shopTattooAnkleSelect == 1:
        $ shopTotal += 100
    if shopTattooAnkleSelect == 2:
        $ shopTotal += 100
    if shopTattooAnkleSelect == 3:
        $ shopTotal += 100
    if shopTattooAnkleSelect == 4:
        $ shopTotal += 100
    if shopTattooAnkleSelect == 5:
        $ shopTotal += 100
    if shopTattooAnkleSelect == 6:
        $ shopTotal += 50


    if shopHairGreenSelect != greenHairSet:
        $ shopTotal += 100





    if 1 <= shopPubicRedSelect <= 7:
        $ shopTotal += 100




    if shopHairYellowSelect != yellowHairSet:
        $ shopTotal += 100



    if 1 <= shopPubicYellowSelect <= 7:
        $ shopTotal += 100

    if menuSelect == 1:
        call screen bgShop1
    if menuSelect == 2:
        call screen bgShop2
    if menuSelect == 3:
        call screen bgShop3

label purchaseButton:
    if cash >= shopTotal:
        $ cash -= shopTotal


        if shopHeadSelect == 10:
            $ shopHeadSelect = 0
            $ hat10Sam = True

        if shopNeckSelect == 2:
            $ shopNeckSelect = 0
            $ neck2Sam = True
        if shopNeckSelect == 7:
            $ shopNeckSelect = 0
            $ neck7Sam = True


        if shopChestSelect == 3:
            $ shopChestSelect = 0
            $ top3Sam = True
        if shopChestSelect == 4:
            $ shopChestSelect = 0
            $ top4Sam = True
        if shopChestSelect == 5:
            $ shopChestSelect = 0
            $ top5Sam = True


        if shopBottSelect == 3:
            $ shopBottSelect = 0
            $ bott3Sam = True
        if shopBottSelect == 5:
            $ shopBottSelect = 0
            $ bott5Sam = True

        if shopShoeSelect == 5:
            $ shopShoeSelect = 0
            $ shoes5Sam = True
        if shopShoeSelect == 10:
            $ shopShoeSelect = 0
            $ shoes10Sam = True

        if shopUnderSelect == 4:
            $ shopUnderSelect = 0
            $ under4Sam = True


        if shopPubicGreenSelect == 1:
            $ greenPubicSet = 1
        if shopPubicGreenSelect == 2:
            $ greenPubicSet = 2
        if shopPubicGreenSelect == 3:
            $ greenPubicSet = 3
        if shopPubicGreenSelect == 4:
            $ greenPubicSet = 4
        if shopPubicGreenSelect == 5:
            $ greenPubicSet = 5
        if shopPubicGreenSelect == 6:
            $ greenPubicSet = 6
        if shopPubicGreenSelect == 7:
            $ greenPubicSet = 7


        if shopHairGreenSelect == 1:
            $ greenHairSet = 1
        if shopHairGreenSelect == 2:
            $ greenHairSet = 2
        if shopHairGreenSelect == 3:
            $ greenHairSet = 3
        if shopHairGreenSelect == 4:
            $ greenHairSet = 4
        if shopHairGreenSelect == 5:
            $ greenHairSet = 5
        if shopHairGreenSelect == 6:
            $ greenHairSet = 6



        if shopHeadSelect == 9:
            $ shopHeadSelect = 0
            $ hat9Clover = True


        if shopNeckSelect == 103:
            $ shopNeckSelect = 0
            $ neck2Clover = True
        if shopNeckSelect == 104:
            $ shopNeckSelect = 0
            $ neck7Clover = True

        if shopChestSelect == 103:
            $ shopChestSelect = 0
            $ top3Clover = True
        if shopChestSelect == 104:
            $ shopChestSelect = 0
            $ top4Clover = True
        if shopChestSelect == 105:
            $ shopChestSelect = 0
            $ top5Clover = True


        if shopBottSelect == 103:
            $ shopBottSelect = 0
            $ bott3Clover = True
        if shopBottSelect == 104:
            $ shopBottSelect = 0
            $ bott4Clover = True

        if shopShoeSelect == 103:
            $ shopShoeSelect = 0
            $ shoes3Clover = True
        if shopShoeSelect == 104:
            $ shopShoeSelect = 0
            $ shoes4Clover = True

        if shopUnderSelect == 104:
            $ shopUnderSelect = 0
            $ under4Clover = True


        if shopPubicRedSelect == 1:
            $ redPubicSet = 1
        if shopPubicRedSelect == 2:
            $ redPubicSet = 2
        if shopPubicRedSelect == 3:
            $ redPubicSet = 3
        if shopPubicRedSelect == 4:
            $ redPubicSet = 4
        if shopPubicRedSelect == 5:
            $ redPubicSet = 5
        if shopPubicRedSelect == 6:
            $ redPubicSet = 6
        if shopPubicRedSelect == 7:
            $ redPubicSet = 7


        if shopHairRedSelect == 1:
            $ redHairSet = 1
        if shopHairRedSelect == 2:
            $ redHairSet = 2
        if shopHairRedSelect == 3:
            $ redHairSet = 3
        if shopHairRedSelect == 4:
            $ redHairSet = 4
        if shopHairRedSelect == 5:
            $ redHairSet = 5




        if shopPubicYellowSelect == 1:
            $ yellowPubicSet = 1
        if shopPubicYellowSelect == 2:
            $ yellowPubicSet = 2
        if shopPubicYellowSelect == 3:
            $ yellowPubicSet = 3
        if shopPubicYellowSelect == 4:
            $ yellowPubicSet = 4
        if shopPubicYellowSelect == 5:
            $ yellowPubicSet = 5
        if shopPubicYellowSelect == 6:
            $ yellowPubicSet = 6
        if shopPubicYellowSelect == 7:
            $ yellowPubicSet = 7


        if shopHairYellowSelect == 1:
            $ yellowHairSet = 1
        if shopHairYellowSelect == 2:
            $ yellowHairSet = 2
        if shopHairYellowSelect == 3:
            $ yellowHairSet = 3
        if shopHairYellowSelect == 4:
            $ yellowHairSet = 4
        if shopHairYellowSelect == 5:
            $ yellowHairSet = 5
        if shopHairYellowSelect == 6:
            $ yellowHairSet = 6




        if shopNeckSelect == 201:
            $ shopNeckSelect = 0
            $ neck1Alex = True
        if shopNeckSelect == 202:
            $ shopNeckSelect = 0
            $ neck2Alex = True


        if shopChestSelect == 203:
            $ shopChestSelect = 0
            $ top3Alex = True
        if shopChestSelect == 204:
            $ shopChestSelect = 0
            $ top4Alex = True


        if shopBottSelect == 203:
            $ shopBottSelect = 0
            $ bott3Alex = True
        if shopBottSelect == 204:
            $ shopBottSelect = 0
            $ bott4Alex = True


        if shopShoeSelect == 203:
            $ shopShoeSelect = 0
            $ shoes3Alex = True
        if shopShoeSelect == 204:
            $ shopShoeSelect = 0
            $ shoes4Alex = True


        if shopUnderSelect == 204:
            $ shopUnderSelect = 0
            $ under4Alex = True


        if shopHairYellowSelect == 1:
            $ yellowHairSet = 1
        if shopHairYellowSelect == 2:
            $ yellowHairSet = 2
        if shopHairYellowSelect == 3:
            $ yellowHairSet = 3
        if shopHairYellowSelect == 4:
            $ yellowHairSet = 4
        if shopHairYellowSelect == 5:
            $ yellowHairSet = 5

        $ shopTotal = 0
        play audio "audio/sfx/cashRegister.mp3"
    if menuSelect == 1:
        call screen bgShop1
    if menuSelect == 2:
        call screen bgShop2
    if menuSelect == 3:
        call screen bgShop3
    elif True:
        y "I don't have enough money to buy this."
        call screen bgShop1

label shop1PrvSpy:
    $ shopCurrentSpy -= 1
    if shopCurrentSpy <= 0:
        $ shopCurrentSpy = 3
    if shopCurrentSpy == 1:
        hide red
        hide yellow
        show green g1:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 2:
        hide green
        hide yellow
        show red:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 3:
        hide green
        hide red
        show yellow:
            xalign 1.0 yalign -0.7
    call screen bgShop1

label shop1NxtSpy:
    $ shopCurrentSpy += 1
    if shopCurrentSpy >= 4:
        $ shopCurrentSpy = 1
    if shopCurrentSpy == 1:
        hide red
        hide yellow
        show green g1:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 2:
        hide green
        hide yellow
        show red:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 3:
        hide green
        hide red
        show yellow:
            xalign 1.0 yalign -0.7
    call screen bgShop1

label shop1SpySam:
    $ shopCurrentSpy = 1
    hide red
    hide yellow
    show green g1:
        xalign 1.0 yalign -0.7
    call screen bgShop1
label shop1SpyClover:
    $ shopCurrentSpy = 2
    hide green
    hide yellow
    show red:
        xalign 1.0 yalign -0.7
    call screen bgShop1
label shop1SpyAlex:
    $ shopCurrentSpy = 3
    hide green
    hide red
    show yellow:
        xalign 1.0 yalign -0.7
    call screen bgShop1



default shopHairGreenSelect = 0
default shopHairRedSelect = 0
default shopHairYellowSelect = 0

default shopPubicGreenSelect = 0
default shopPubicRedSelect = 0
default shopPubicYellowSelect = 0

screen bgShop2:
    add "gui/itemUI/shop2/bgShop2.png"


    text "{font=fonts/freshMarker.ttf}{size=+4}{color=#ffeda6}{color=#ffffff}[cash]{/color}{/size}{/font}" xpos 180 yalign 0.09


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action SetVariable("shopTotal", 0), Jump("exitShop")


    vbox xalign 0.075 yalign 0.99:
        imagebutton:
            idle "gui/itemUI/shop1/prv.png"
            hover "gui/itemUI/shop1/prv-hover.png"

    vbox xalign 0.565 yalign 0.99:
        imagebutton:
            idle "gui/itemUI/shop1/nxt.png"
            hover "gui/itemUI/shop1/nxt-hover.png"


    if shopCurrentSpy == 1:
        if spyGreenActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Sam"
    elif shopCurrentSpy == 2:
        if spyRedActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Clover"
    elif shopCurrentSpy == 3:
        if spyYellowActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Alex"
    hbox:
        spacing 10 xalign 0.64 yalign 0.29
        text "{color=#ffffff}{size=+12}{font=fonts/freshmarker.ttf}[shopSpyName]{/font}{/color}{/color}"



    vbox xalign 0.67 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpySam.png"
            hover "gui/itemUI/shopSpySam-hover.png"
            action Jump("shop2SpySam")

    vbox xalign 0.77 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyClover.png"
            hover "gui/itemUI/shopSpyClover-hover.png"
            action Jump("shop2SpyClover")

    vbox xalign 0.87 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyAlex.png"
            hover "gui/itemUI/shopSpyAlex-hover.png"
            action Jump("shop2SpyAlex")




    if shopCategory == 1:
        vbox xalign 0.987 yalign 0.012:
            imagebutton:
                idle "gui/itemUI/shop3/shopHead1.png"
                hover "gui/itemUI/shop3/shopHead1-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.987 yalign 0.012:
            imagebutton:
                idle "gui/itemUI/shop3/shopHead1.png"
                hover "gui/itemUI/shop3/shopHead1-hover.png"
                action SetVariable("shopCategory", 1)

    if shopCategory == 2:
        vbox xalign 0.987 yalign 0.20:
            imagebutton:
                idle "gui/itemUI/shop3/shopCrotch-hover.png"
                hover "gui/itemUI/shop3/shopCrotch-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.987 yalign 0.20:
            imagebutton:
                idle "gui/itemUI/shop3/shopCrotch.png"
                hover "gui/itemUI/shop3/shopCrotch-hover.png"
                if shopCurrentSpy == 1:
                    action SetVariable("shopCategory", 2), SetVariable("greenBottom", 0), SetVariable("greenUnder", 0)
                if shopCurrentSpy == 2:
                    action SetVariable("shopCategory", 2), SetVariable("redBottom", 0), SetVariable("redUnder", 0)
                if shopCurrentSpy == 3:
                    action SetVariable("shopCategory", 2), SetVariable("yellowBottom", 0), SetVariable("yellowUnder", 0)


    if shopCategory == 1:
        if shopCurrentSpy == 1:
            vbox xalign 0.11 yalign 0.27:
                imagebutton:
                    idle "models/green/hair/greenHair1mini.png"
                    hover "models/green/hair/greenHair1mini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenHair", 1)
            vbox xalign 0.1 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenHairSet", 1)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenHairSet", 1)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.24 yalign 0.27:
                imagebutton:
                    idle "models/green/hair/greenHair3mini.png"
                    hover "models/green/hair/greenHair3mini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenHair", 3)
            vbox xalign 0.22 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.28 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenHairSet", 3)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("greenHairSet", 3)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.27:
                imagebutton:
                    idle "models/green/hair/greenHair4mini.png"
                    hover "models/green/hair/greenHair4mini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenHair", 4)
            vbox xalign 0.345 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.405 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenHairSet", 4)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("greenHairSet", 4)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "models/green/hair/greenHair5mini.png"
                    hover "models/green/hair/greenHair5mini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenHair", 5)
            vbox xalign 0.47 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.53 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenHairSet", 5)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("greenHairSet", 5)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.11 yalign 0.52:
                imagebutton:
                    idle "models/green/hair/greenHair6mini.png"
                    hover "models/green/hair/greenHair6mini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenHair", 6)
            vbox xalign 0.1 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.153 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenHairSet", 6)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("greenHairSet", 6)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.24 yalign 0.52:
                imagebutton:
                    idle "models/green/hair/greenHair8mini.png"
                    hover "models/green/hair/greenHair8mini.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenHair", 8)
            vbox xalign 0.22 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenHairSet", 8)
                    elif cash >= 0:
                        action SetVariable("cash", cash - 0), SetVariable("greenHairSet", 8)
                    else:
                        action Jump("shopNoCash")


        if shopCurrentSpy == 2:
            vbox xalign 0.11 yalign 0.27:
                imagebutton:
                    idle "models/red/hair/hair1mini.png"
                    hover "models/red/hair/hair1mini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redHair", 1)
            vbox xalign 0.1 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redHairSet", 1)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redHairSet", 1)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.24 yalign 0.27:
                imagebutton:
                    idle "models/red/hair/hair2mini.png"
                    hover "models/red/hair/hair2mini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redHair", 2)
            vbox xalign 0.22 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.28 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redHairSet", 2)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("redHairSet", 2)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.27:
                imagebutton:
                    idle "models/red/hair/hair3mini.png"
                    hover "models/red/hair/hair3mini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redHair", 3)
            vbox xalign 0.345 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.405 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redHairSet", 3)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("redHairSet", 3)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "models/red/hair/hair4mini.png"
                    hover "models/red/hair/hair4mini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redHair", 4)
            vbox xalign 0.47 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.53 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redHairSet", 4)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("redHairSet", 4)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.11 yalign 0.53:
                imagebutton:
                    idle "models/red/hair/hair5mini.png"
                    hover "models/red/hair/hair5mini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redHair", 5)
            vbox xalign 0.1 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.153 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redHairSet", 5)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("redHairSet", 5)
                    else:
                        action Jump("shopNoCash")

        if shopCurrentSpy == 3:
            vbox xalign 0.11 yalign 0.27:
                imagebutton:
                    idle "models/yellow/hair/hair1mini.png"
                    hover "models/yellow/hair/hair1mini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowHair", 1)
            vbox xalign 0.1 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowHairSet", 1)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowHairSet", 1)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.24 yalign 0.27:
                imagebutton:
                    idle "models/yellow/hair/hair2mini.png"
                    hover "models/yellow/hair/hair2mini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowHair", 2)
            vbox xalign 0.22 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.28 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowHairSet", 2)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("yellowHairSet", 2)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.27:
                imagebutton:
                    idle "models/yellow/hair/hair3mini.png"
                    hover "models/yellow/hair/hair3mini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowHair", 3)
            vbox xalign 0.345 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.405 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowHairSet", 3)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("yellowHairSet", 3)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "models/yellow/hair/hair4mini.png"
                    hover "models/yellow/hair/hair4mini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowHair", 4)
            vbox xalign 0.47 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.53 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowHairSet", 4)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("yellowHairSet", 4)
                    else:
                        action Jump("shopNoCash")
            vbox xalign 0.11 yalign 0.53:
                imagebutton:
                    idle "models/yellow/hair/hair5mini.png"
                    hover "models/yellow/hair/hair5mini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowHair", 5)
            vbox xalign 0.1 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.153 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowHairSet", 5)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("yellowHairSet", 5)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.24 yalign 0.53:
                imagebutton:
                    idle "models/yellow/hair/hair6mini.png"
                    hover "models/yellow/hair/hair6mini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowHair", 6)
            vbox xalign 0.22 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$150{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowHairSet", 6)
                    elif cash >= 150:
                        action SetVariable("cash", cash - 150), SetVariable("yellowHairSet", 6)
                    else:
                        action Jump("shopNoCash")

    if shopCategory == 2:
        if shopCurrentSpy == 1:
            vbox xalign 0.095 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub1mini.png"
                    hover "gui/itemUI/shop2/pub1mini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenPubic", 1)
            vbox xalign 0.1 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenPubicSet", 1)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenPubicSet", 1)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub2mini.png"
                    hover "gui/itemUI/shop2/pub2mini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenPubic", 2)
            vbox xalign 0.22 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.28 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenPubicSet", 2)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenPubicSet", 2)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub3mini.png"
                    hover "gui/itemUI/shop2/pub3mini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenPubic", 3)
            vbox xalign 0.345 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.405 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenPubicSet", 3)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenPubicSet", 3)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub4mini.png"
                    hover "gui/itemUI/shop2/pub4mini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenPubic", 4)
            vbox xalign 0.47 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.53 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenPubicSet", 4)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenPubicSet", 4)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub5mini.png"
                    hover "gui/itemUI/shop2/pub5mini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenPubic", 5)
            vbox xalign 0.1 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenPubicSet", 5)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenPubicSet", 5)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub6mini.png"
                    hover "gui/itemUI/shop2/pub6mini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenPubic", 6)
            vbox xalign 0.22 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenPubicSet", 6)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenPubicSet", 6)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub7mini.png"
                    hover "gui/itemUI/shop2/pub7mini-hover.png"
                    action SetVariable("shopItemSelect", 7), SetVariable("greenPubic", 7)
            vbox xalign 0.34 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.405 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("greenPubicSet", 7)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("greenPubicSet", 7)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("greenPubic", 0), SetVariable("greenPubicSet", 0), SetVariable("shopPubicGreenSelect", 0), Jump("shopAddup")

        if shopCurrentSpy == 2:
            vbox xalign 0.095 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub1mini.png"
                    hover "gui/itemUI/shop2/pub1mini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redPubic", 1)
            vbox xalign 0.1 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redPubicSet", 1)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redPubicSet", 1)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub2mini.png"
                    hover "gui/itemUI/shop2/pub2mini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redPubic", 2)
            vbox xalign 0.22 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.28 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redPubicSet", 2)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redPubicSet", 2)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub3mini.png"
                    hover "gui/itemUI/shop2/pub3mini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redPubic", 3)
            vbox xalign 0.345 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.405 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redPubicSet", 3)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redPubicSet", 3)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub4mini.png"
                    hover "gui/itemUI/shop2/pub4mini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redPubic", 4)
            vbox xalign 0.47 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.53 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redPubicSet", 4)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redPubicSet", 4)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub5mini.png"
                    hover "gui/itemUI/shop2/pub5mini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redPubic", 5)
            vbox xalign 0.1 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redPubicSet", 5)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redPubicSet", 5)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub6mini.png"
                    hover "gui/itemUI/shop2/pub6mini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("redPubic", 6)
            vbox xalign 0.22 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redPubicSet", 6)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redPubicSet", 6)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub7mini.png"
                    hover "gui/itemUI/shop2/pub7mini-hover.png"
                    action SetVariable("shopItemSelect", 7), SetVariable("redPubic", 7)
            vbox xalign 0.34 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.405 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("redPubicSet", 7)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("redPubicSet", 7)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("redPubic", 0), SetVariable("redPubicSet", 0), SetVariable("shopPubicRedSelect", 0), Jump("shopAddup")

        if shopCurrentSpy == 3:
            vbox xalign 0.095 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub1mini.png"
                    hover "gui/itemUI/shop2/pub1mini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowPubic", 1)
            vbox xalign 0.1 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowPubicSet", 1)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowPubicSet", 1)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub2mini.png"
                    hover "gui/itemUI/shop2/pub2mini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowPubic", 2)
            vbox xalign 0.22 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.28 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowPubicSet", 2)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowPubicSet", 2)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub3mini.png"
                    hover "gui/itemUI/shop2/pub3mini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowPubic", 3)
            vbox xalign 0.345 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.405 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowPubicSet", 3)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowPubicSet", 3)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.26:
                imagebutton:
                    idle "gui/itemUI/shop2/pub4mini.png"
                    hover "gui/itemUI/shop2/pub4mini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowPubic", 4)
            vbox xalign 0.47 yalign 0.22:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.53 yalign 0.370:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowPubicSet", 4)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowPubicSet", 4)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub5mini.png"
                    hover "gui/itemUI/shop2/pub5mini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowPubic", 5)
            vbox xalign 0.1 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.153 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowPubicSet", 5)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowPubicSet", 5)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub6mini.png"
                    hover "gui/itemUI/shop2/pub6mini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowPubic", 6)
            vbox xalign 0.22 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowPubicSet", 6)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowPubicSet", 6)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.37 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/pub7mini.png"
                    hover "gui/itemUI/shop2/pub7mini-hover.png"
                    action SetVariable("shopItemSelect", 7), SetVariable("yellowPubic", 7)
            vbox xalign 0.34 yalign 0.45:
                if task12Stage >= 4:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$0{/size}{/font}"
                else:
                    text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            vbox xalign 0.405 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if task12Stage >= 4:
                        action SetVariable("cash", cash - 0), SetVariable("yellowPubicSet", 7)
                    elif cash >= 100:
                        action SetVariable("cash", cash - 100), SetVariable("yellowPubicSet", 7)
                    else:
                        action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("yellowPubic", 0), SetVariable("yellowPubicSet", 0), SetVariable("shopPubicYellowSelect", 0), Jump("shopAddup")

    if shopItemSelect == 1:
        vbox xalign 0.097 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 2:
        vbox xalign 0.235 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 3:
        vbox xalign 0.368 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 4:
        vbox xalign 0.50 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 5:
        vbox xalign 0.097 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 6:
        vbox xalign 0.235 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 7:
        vbox xalign 0.368 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 8:
        vbox xalign 0.50 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 9:
        vbox xalign 0.097 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 10:
        vbox xalign 0.235 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 11:
        vbox xalign 0.368 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 12:
        vbox xalign 0.50 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"

label shop2PrvSpy:
    $ shopCurrentSpy -= 1
    if shopCurrentSpy <= 0:
        $ shopCurrentSpy = 3
    if shopCurrentSpy == 1:
        hide red
        hide yellow
        show green g1:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 2:
        hide green
        hide yellow
        show red:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 3:
        hide green
        hide red
        show yellow:
            xalign 1.0 yalign -0.7
    call screen bgShop2

label shop2NxtSpy:
    $ shopCurrentSpy += 1
    if shopCurrentSpy >= 4:
        $ shopCurrentSpy = 1
    if shopCurrentSpy == 1:
        hide red
        hide yellow
        show green g1:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 2:
        hide green
        hide yellow
        show red:
            xalign 1.0 yalign -0.7
    if shopCurrentSpy == 3:
        hide green
        hide red
        show yellow:
            xalign 1.0 yalign -0.7
    call screen bgShop2

label shop2SpySam:
    $ shopCurrentSpy = 1
    hide red
    hide yellow
    show green g1:
        xalign 1.0 yalign -0.7
    call screen bgShop2
label shop2SpyClover:
    $ shopCurrentSpy = 2
    hide green
    hide yellow
    show red:
        xalign 1.0 yalign -0.7
    call screen bgShop2
label shop2SpyAlex:
    $ shopCurrentSpy = 3
    hide green
    hide red
    show yellow:
        xalign 1.0 yalign -0.7
    call screen bgShop2


image bgShop3 = "gui/itemUI/shop3/bgShop3.png"

default shopTattooHeadSelect = False
default shopTattooChestSelect = False
default shopTattooArmSelect = False
default shopTattooBellySelect = False
default shopTattooCrotchSelect = False
default shopTattooLegSelect = False
default shopTattooAnkleSelect = False

default shopTattooHeadPrice = 0
default shopTattooChestPrice = 0
default shopTattooArmPrice = 0
default shopTattooBellyPrice = 0
default shopTattooCrotchPrice = 0
default shopTattooLegPrice = 0
default shopTattooAnklePrice = 0

screen bgShop3:
    add "gui/itemUI/shop3/bgShop3.png"


    text "{font=fonts/freshMarker.ttf}{size=+4}{color=#ffeda6}{color=#ffffff}[cash]{/color}{/size}{/font}" xpos 180 yalign 0.09


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action SetVariable("shopTotal", 0), Jump("exitShop")


    vbox xalign 0.075 yalign 0.99:
        imagebutton:
            idle "gui/itemUI/shop1/prv.png"
            hover "gui/itemUI/shop1/prv-hover.png"

    vbox xalign 0.565 yalign 0.99:
        imagebutton:
            idle "gui/itemUI/shop1/nxt.png"
            hover "gui/itemUI/shop1/nxt-hover.png"


    if shopCurrentSpy == 1:
        if spyGreenActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Sam"
    elif shopCurrentSpy == 2:
        if spyRedActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Clover"
    elif shopCurrentSpy == 3:
        if spyYellowActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Alex"
    hbox:
        spacing 10 xalign 0.64 yalign 0.29
        text "{color=#ffffff}{size=+12}{font=fonts/freshmarker.ttf}[shopSpyName]{/font}{/size}{/color}"


    if shopCurrentSpy == 1:
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/undress.png"
                hover "gui/itemUI/undress-hover.png"
                action Jump("undressSamShop")
    if shopCurrentSpy == 2:
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/undress.png"
                hover "gui/itemUI/undress-hover.png"
                action Jump("undressCloverShop")
    if shopCurrentSpy == 3:
        vbox xalign 0.76 yalign 0.9:
            imagebutton:
                idle "gui/itemUI/undress.png"
                hover "gui/itemUI/undress-hover.png"
                action Jump("undressAlexShop")



    vbox xalign 0.67 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpySam.png"
            hover "gui/itemUI/shopSpySam-hover.png"
            action Jump("shop3SpySam")

    vbox xalign 0.77 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyClover.png"
            hover "gui/itemUI/shopSpyClover-hover.png"
            action Jump("shop3SpyClover")

    vbox xalign 0.87 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyAlex.png"
            hover "gui/itemUI/shopSpyAlex-hover.png"
            action Jump("shop3SpyAlex")





    vbox xalign 0.98 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop3/shopHead1.png"
            hover "gui/itemUI/shop3/shopHead1-hover.png"
            action SetVariable("shopCategory", 1), Jump("shopPrev")

    vbox xalign 0.98 yalign 0.20:
        imagebutton:
            idle "gui/itemUI/shop3/shopChest.png"
            hover "gui/itemUI/shop3/shopChest-hover.png"
            action SetVariable("shopCategory", 2), Jump("shopPrev")

    vbox xalign 0.98 yalign 0.38:
        imagebutton:
            idle "gui/itemUI/shop3/shopArm.png"
            hover "gui/itemUI/shop3/shopArm-hover.png"
            action SetVariable("shopCategory", 3), Jump("shopPrev")

    vbox xalign 0.98 yalign 0.56:
        imagebutton:
            idle "gui/itemUI/shop3/shopBelly.png"
            hover "gui/itemUI/shop3/shopBelly-hover.png"
            action SetVariable("shopCategory", 4), Jump("shopPrev")

    vbox xalign 0.98 yalign 0.74:
        imagebutton:
            idle "gui/itemUI/shop3/shopCrotch.png"
            hover "gui/itemUI/shop3/shopCrotch-hover.png"
            action SetVariable("shopCategory", 7), Jump("shopPrev")

    vbox xalign 0.98 yalign 0.93:
        imagebutton:
            idle "gui/itemUI/shop3/shopAnkle.png"
            hover "gui/itemUI/shop3/shopAnkle-hover.png"
            action SetVariable("shopCategory", 9), Jump("shopPrev")



    if shopCurrentSpy == 1:
        if shopCategory == 1:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenTatHead", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatHeadSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatHeadSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenTatHead", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatHeadSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatHeadSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenTatHead", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatHeadSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatHeadSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenTatHead", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatHeadSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatHeadSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenTatHead", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatHeadSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatHeadSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenTatHead", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatHeadSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatHeadSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("greenTatHead", 0), SetVariable("greenTatHeadSet", 0), Jump("shopAddup")

        if shopCategory == 2:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenTatChest", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatChestSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatChestSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenTatChest", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatChestSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatChestSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenTatChest", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatChestSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatChestSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenTatChest", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatChestSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatChestSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenTatChest", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatChestSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatChestSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenTatChest", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatChestSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatChestSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("greenTatChest", 0), SetVariable("greenTatChestSet", 0)

        if shopCategory == 3:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenTatArm", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatArmSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatArmSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenTatArm", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatArmSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatArmSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenTatArm", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatArmSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatArmSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenTatArm", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatArmSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatArmSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenTatArm", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatArmSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatArmSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenTatArm", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatArmSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatArmSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("greenTatArm", 0), SetVariable("greenTatArmSet", 0)

        if shopCategory == 4:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenTatBelly", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatBellySet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatBellySet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenTatBelly", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatBellySet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatBellySet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenTatBelly", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatBellySet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatBellySet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenTatBelly", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatBellySet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatBellySet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenTatBelly", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatBellySet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatBellySet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenTatBelly", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatBellySet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatBellySet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("greenTatBelly", 0), SetVariable("greenTatBellySet", 0)

        if shopCategory == 7:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenTatPuss", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatPussSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatPussSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenTatPuss", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatPussSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatPussSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenTatPuss", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatPussSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatPussSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenTatPuss", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatPussSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatPussSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenTatPuss", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatPussSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatPussSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenTatPuss", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatPussSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatPussSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("greenTatPuss", 0), SetVariable("greenTatPussSet", 0)

        if shopCategory == 9:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("greenTatFoot", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatFootSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatFootSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("greenTatFoot", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatFootSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatFootSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("greenTatFoot", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatFootSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatFootSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("greenTatFoot", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatFootSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatFootSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("greenTatFoot", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatFootSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatFootSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("greenTatFoot", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if greenTatFootSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("greenTatFootSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("greenTatFoot", 0), SetVariable("greenTatFootSet", 0)



    if shopCurrentSpy == 2:
        if shopCategory == 1:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redTatHead", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatHeadSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatHeadSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redTatHead", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatHeadSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatHeadSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redTatHead", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatHeadSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatHeadSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redTatHead", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatHeadSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatHeadSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redTatHead", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatHeadSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatHeadSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("redTatHead", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatHeadSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatHeadSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("redTatHead", 0), SetVariable("redTatHeadSet", 0), Jump("shopAddup")

        if shopCategory == 2:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redTatChest", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatChestSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatChestSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redTatChest", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatChestSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatChestSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redTatChest", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatChestSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatChestSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redTatChest", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatChestSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatChestSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redTatChest", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatChestSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatChestSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("redTatChest", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatChestSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatChestSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("redTatChest", 0), SetVariable("redTatChestSet", 0)

        if shopCategory == 3:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redTatArm", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatArmSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatArmSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redTatArm", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatArmSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatArmSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redTatArm", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatArmSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatArmSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redTatArm", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatArmSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatArmSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redTatArm", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatArmSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatArmSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("redTatArm", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatArmSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatArmSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("redTatArm", 0), SetVariable("redTatArmSet", 0)

        if shopCategory == 4:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redTatBelly", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatBellySet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatBellySet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redTatBelly", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatBellySet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatBellySet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redTatBelly", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatBellySet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatBellySet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redTatBelly", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatBellySet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatBellySet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redTatBelly", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatBellySet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatBellySet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("redTatBelly", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatBellySet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatBellySet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("redTatBelly", 0), SetVariable("redTatBellySet", 0)

        if shopCategory == 7:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redTatPuss", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatPussSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatPussSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redTatPuss", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatPussSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatPussSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redTatPuss", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatPussSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatPussSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redTatPuss", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatPussSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatPussSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redTatPuss", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatPussSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatPussSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("redTatPuss", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatPussSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatPussSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("redTatPuss", 0), SetVariable("redTatPussSet", 0)

        if shopCategory == 9:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("redTatFoot", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatFootSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatFootSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("redTatFoot", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatFootSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatFootSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("redTatFoot", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatFootSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatFootSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("redTatFoot", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatFootSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatFootSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("redTatFoot", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatFootSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatFootSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("redTatFoot", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if redTatFootSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("redTatFootSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("redTatFoot", 0), SetVariable("redTatFootSet", 0)



    if shopCurrentSpy == 3:
        if shopCategory == 1:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowTatHead", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatHeadSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatHeadSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowTatHead", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatHeadSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatHeadSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowTatHead", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatHeadSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatHeadSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowTatHead", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatHeadSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatHeadSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowTatHead", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatHeadSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatHeadSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowTatHead", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatHeadSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatHeadSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("yellowTatHead", 0), SetVariable("yellowTatHeadSet", 0), Jump("shopAddup")

        if shopCategory == 2:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowTatChest", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatChestSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatChestSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowTatChest", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatChestSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatChestSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowTatChest", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatChestSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatChestSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowTatChest", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatChestSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatChestSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowTatChest", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatChestSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatChestSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowTatChest", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatChestSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatChestSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("yellowTatChest", 0), SetVariable("yellowTatChestSet", 0)

        if shopCategory == 3:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowTatArm", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatArmSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatArmSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowTatArm", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatArmSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatArmSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowTatArm", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatArmSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatArmSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowTatArm", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatArmSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatArmSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowTatArm", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatArmSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatArmSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowTatArm", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatArmSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatArmSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("yellowTatArm", 0), SetVariable("yellowTatArmSet", 0)

        if shopCategory == 4:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowTatBelly", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatBellySet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatBellySet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowTatBelly", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatBellySet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatBellySet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowTatBelly", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatBellySet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatBellySet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowTatBelly", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatBellySet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatBellySet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowTatBelly", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatBellySet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatBellySet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowTatBelly", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatBellySet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatBellySet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("yellowTatBelly", 0), SetVariable("yellowTatBellySet", 0)

        if shopCategory == 7:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowTatPuss", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatPussSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatPussSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowTatPuss", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatPussSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatPussSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowTatPuss", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatPussSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatPussSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowTatPuss", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatPussSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatPussSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowTatPuss", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatPussSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatPussSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowTatPuss", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatPussSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatPussSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("yellowTatPuss", 0), SetVariable("yellowTatPussSet", 0)

        if shopCategory == 9:
            vbox xalign 0.09 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 1), SetVariable("yellowTatFoot", 1)
            vbox xalign 0.1 yalign 0.225:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatFootSet != 1:
                vbox xalign 0.155 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatFootSet", 1)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 2), SetVariable("yellowTatFoot", 2)
            vbox xalign 0.22 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatFootSet != 2:
                vbox xalign 0.28 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatFootSet", 2)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.36 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 3), SetVariable("yellowTatFoot", 3)
            vbox xalign 0.345 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatFootSet != 3:
                vbox xalign 0.405 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatFootSet", 3)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 4), SetVariable("yellowTatFoot", 4)
            vbox xalign 0.47 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatFootSet != 4:
                vbox xalign 0.53 yalign 0.370:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatFootSet", 4)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.09 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 5), SetVariable("yellowTatFoot", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatFootSet != 5:
                vbox xalign 0.153 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatFootSet", 5)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.23 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/items/tattooMini.png"
                    hover "gui/itemUI/items/tattooMini-hover.png"
                    action SetVariable("shopItemSelect", 6), SetVariable("yellowTatFoot", 6)
            vbox xalign 0.22 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$100{/size}{/font}"

            if yellowTatFootSet != 6:
                vbox xalign 0.28 yalign 0.6:
                    imagebutton:
                        idle "gui/itemUI/purchase.png"
                        hover "gui/itemUI/purchase-hover.png"
                        if cash >= 100:
                            action SetVariable("cash", cash - 100), SetVariable("yellowTatFootSet", 6)
                        else:
                            action Jump("shopNoCash")

            vbox xalign 0.50 yalign 0.78:
                imagebutton:
                    idle "gui/itemUI/shop2/shave.png"
                    hover "gui/itemUI/shop2/shave-hover.png"
                    action SetVariable("yellowTatFoot", 0), SetVariable("yellowTatFootSet", 0)

label shop3SpySam:
    $ shopCurrentSpy = 1
    hide red
    hide yellow
    show green g1:
        xalign 1.0 yalign -0.7
    call screen bgShop3
label shop3SpyClover:
    $ shopCurrentSpy = 2
    hide green
    hide yellow
    show red:
        xalign 1.0 yalign -0.7
    call screen bgShop3
label shop3SpyAlex:
    $ shopCurrentSpy = 3
    hide green
    hide red
    show yellow:
        xalign 1.0 yalign -0.7
    call screen bgShop3




screen bgShop6:
    add "gui/itemUI/shop6/bgShop6.png"


    text "{font=fonts/freshMarker.ttf}{size=+4}{color=#ffeda6}{color=#ffffff}[cash]{/color}{/size}{/font}" xpos 180 yalign 0.09


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action SetVariable("shopTotal", 0), Jump("exitShop")


    vbox xalign 0.085 yalign 0.95:
        imagebutton:
            idle "gui/itemUI/shop1/prv.png"
            hover "gui/itemUI/shop1/prv-hover.png"

    vbox xalign 0.55 yalign 0.95:
        imagebutton:
            idle "gui/itemUI/shop1/nxt.png"
            hover "gui/itemUI/shop1/nxt-hover.png"


    if shopCurrentSpy == 1:
        if spyGreenActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Sam"
    elif shopCurrentSpy == 2:
        if spyRedActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Clover"
    elif shopCurrentSpy == 3:
        if spyYellowActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Alex"
    hbox:
        spacing 10 xalign 0.64 yalign 0.29
        text "{color=#ffffff}{size=+12}{font=fonts/freshmarker.ttf}[shopSpyName]{/font}{/color}{/color}"




    vbox xalign 0.67 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpySam.png"
            hover "gui/itemUI/shopSpySam-hover.png"
            action Jump("shop6SpySam")

    vbox xalign 0.77 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyClover.png"
            hover "gui/itemUI/shopSpyClover-hover.png"
            action Jump("shop6SpyClover")

    vbox xalign 0.87 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyAlex.png"
            hover "gui/itemUI/shopSpyAlex-hover.png"
            action Jump("shop6SpyAlex")





    if shopCategory == 1:
        vbox xalign 0.972 yalign 0.012:
            imagebutton:
                idle "gui/itemUI/shopButtHead.png"
                hover "gui/itemUI/shopButtHead-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.012:
            imagebutton:
                idle "gui/itemUI/shopButtHead.png"
                hover "gui/itemUI/shopButtHead-hover.png"
                action SetVariable("shopCategory", 1), Jump("shopPrev")

    if shopCategory == 2:
        vbox xalign 0.972 yalign 0.13:
            imagebutton:
                idle "gui/itemUI/shopButtFace-hover.png"
                hover "gui/itemUI/shopButtFace-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.13:
            imagebutton:
                idle "gui/itemUI/shopButtFace.png"
                hover "gui/itemUI/shopButtFace-hover.png"
                action SetVariable("shopCategory", 2), Jump("shopPrev")

    if shopCategory == 3:
        vbox xalign 0.972 yalign 0.25:
            imagebutton:
                idle "gui/itemUI/shopButtNeck-hover.png"
                hover "gui/itemUI/shopButtNeck-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.25:
            imagebutton:
                idle "gui/itemUI/shopButtNeck.png"
                hover "gui/itemUI/shopButtNeck-hover.png"
                action SetVariable("shopCategory", 3), Jump("shopPrev")

    if shopCategory == 4:
        vbox xalign 0.972 yalign 0.37:
            imagebutton:
                idle "gui/itemUI/shopButtTop-hover.png"
                hover "gui/itemUI/shopButtTop-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.37:
            imagebutton:
                idle "gui/itemUI/shopButtTop.png"
                hover "gui/itemUI/shopButtTop-hover.png"
                action SetVariable("shopCategory", 4), Jump("shopPrev")

    if shopCategory == 5:
        vbox xalign 0.972 yalign 0.49:
            imagebutton:
                idle "gui/itemUI/shopButtWrist-hover.png"
                hover "gui/itemUI/shopButtWrist-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.49:
            imagebutton:
                idle "gui/itemUI/shopButtWrist.png"
                hover "gui/itemUI/shopButtWrist-hover.png"
                action SetVariable("shopCategory", 5), Jump("shopPrev")

    if shopCategory == 6:
        vbox xalign 0.972 yalign 0.61:
            imagebutton:
                idle "gui/itemUI/shopButtBott-hover.png"
                hover "gui/itemUI/shopButtBott-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.61:
            imagebutton:
                idle "gui/itemUI/shopButtBott.png"
                hover "gui/itemUI/shopButtBott-hover.png"
                action SetVariable("shopCategory", 6), Jump("shopPrev")

    if shopCategory == 7:
        vbox xalign 0.972 yalign 0.73:
            imagebutton:
                idle "gui/itemUI/shopButtShoes-hover.png"
                hover "gui/itemUI/shopButtShoes-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.73:
            imagebutton:
                idle "gui/itemUI/shopButtShoes.png"
                hover "gui/itemUI/shopButtShoes-hover.png"
                action SetVariable("shopCategory", 7), Jump("shopPrev")

    if shopCategory == 8:
        vbox xalign 0.972 yalign 0.85:
            imagebutton:
                idle "gui/itemUI/shopButtUndies-hover.png"
                hover "gui/itemUI/shopButtUndies-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.85:
            imagebutton:
                idle "gui/itemUI/shopButtUndies.png"
                hover "gui/itemUI/shopButtUndies-hover.png"
                action SetVariable("shopCategory", 8), Jump("shopPrev")

    if shopCategory == 9:
        vbox xalign 0.972 yalign 0.97:
            imagebutton:
                idle "gui/itemUI/shopButtSuits-hover.png"
                hover "gui/itemUI/shopButtSuits-hover.png"
                action SetVariable("shopCategory", 0)
    else:
        vbox xalign 0.972 yalign 0.97:
            imagebutton:
                idle "gui/itemUI/shopButtSuits.png"
                hover "gui/itemUI/shopButtSuits-hover.png"
                action SetVariable("shopCategory", 9), Jump("shopPrev")





    if 1 <= greenChest <= 1.9 and shopCategory == 4:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenChest", 1)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenChest", 1.3)

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 1.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenChest", 1.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 1.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenChest", 1.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 1.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenChest", 1.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 1.6)
                else:
                    action Jump("shopNoCash")
    if 3 <= greenChest <= 3.9 and shopCategory == 4:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenChest", 3)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenChest", 3.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 3.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenChest", 3.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 3.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenChest", 3.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 3.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenChest", 3.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 3.6)
                else:
                    action Jump("shopNoCash")
    if 4 <= greenChest <= 4.9 and shopCategory == 4:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenChest", 4)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenChest", 4.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 4.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenChest", 4.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 4.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenChest", 4.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 4.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenChest", 4.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 4.6)
                else:
                    action Jump("shopNoCash")

    if 7 <= greenChest <= 7.9 and shopCategory == 4:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenChest", 7)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenChest", 7.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 7.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenChest", 7.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 7.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenChest", 7.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 7.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenChest", 7.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 7.6)
                else:
                    action Jump("shopNoCash")

    if 9 <= greenChest <= 9.9 and shopCategory == 4:
        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenChest", 9.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 9.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenChest", 9.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 9.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenChest", 9.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 9.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenChest", 9.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 9.6)
                else:
                    action Jump("shopNoCash")

    if 10 <= greenChest <= 10.9 and shopCategory == 4:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenChest", 10)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenChest", 10.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 10.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenChest", 10.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 10.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenChest", 10.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 10.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenChest", 10.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 10.6)
                else:
                    action Jump("shopNoCash")

    if 12 <= greenChest <= 12.9 and shopCategory == 4:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenChest", 12)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenChest", 12.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 12.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenChest", 12.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 12.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenChest", 12.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 12.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenChest", 12.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenChestSet", 12.6)
                else:
                    action Jump("shopNoCash")


    if 7 <= greenBottom <= 7.9 and shopCategory == 6:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenBottom", 7)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenBottom", 7.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 7.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenBottom", 7.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 7.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenBottom", 7.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 7.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenBottom", 7.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 7.6)
                else:
                    action Jump("shopNoCash")

    if 9 <= greenBottom <= 9.9 and shopCategory == 6:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenBottom", 9)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenBottom", 9.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 9.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenBottom", 9.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 9.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenBottom", 9.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 9.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenBottom", 9.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenBottomSet", 9.6)
                else:
                    action Jump("shopNoCash")


    if 7 <= greenShoes <= 7.9 and shopCategory == 7:

        vbox xalign 0.5 yalign 0.78:
            imagebutton:
                idle "gui/itemUI/wardrobe/unequip.png"
                hover "gui/itemUI/wardrobe/unequip-hover.png"
                action SetVariable("greenShoes", 9)

        vbox xalign 0.12 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/blue.png"
                hover "gui/itemUI/shop6/blue.png"
                action SetVariable("greenShoes", 7.3), Jump("shop6SpySam")

        vbox xalign 0.155 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenShoesSet", 7.3)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.24 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/orange.png"
                hover "gui/itemUI/shop6/orange.png"
                action SetVariable("greenShoes", 7.4), Jump("shop6SpySam")

        vbox xalign 0.28 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenShoesSet", 7.4)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.37 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/black.png"
                hover "gui/itemUI/shop6/black.png"
                action SetVariable("greenShoes", 7.5), Jump("shop6SpySam")

        vbox xalign 0.405 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenShoesSet", 7.5)
                else:
                    action Jump("shopNoCash")
        vbox xalign 0.5 yalign 0.27:
            imagebutton:
                idle "gui/itemUI/shop6/drkBlue.png"
                hover "gui/itemUI/shop6/drkBlue.png"
                action SetVariable("greenShoes", 7.6), Jump("shop6SpySam")

        vbox xalign 0.53 yalign 0.375:
            imagebutton:
                idle "gui/itemUI/purchase.png"
                hover "gui/itemUI/purchase-hover.png"
                if cash >= 100:
                    action SetVariable("cash", cash - 100), SetVariable("greenShoesSet", 7.6)
                else:
                    action Jump("shopNoCash")


label shopNoCash:
    y "I don't have enough money for that."
    if menuSelect == 1:
        call screen bgShop1
    if menuSelect == 2:
        call screen bgShop2
    elif menuSelect == 3:
        call screen bgShop3
    elif menuSelect == 4:
        call screen bgShop4
    elif menuSelect == 5:
        call screen bgShop5
    elif menuSelect == 6:
        call screen bgShop6

label shop6SpySam:
    $ shopCurrentSpy = 1
    hide red
    hide yellow
    show green g1:
        xalign 1.0 yalign -0.7
    call screen bgShop6
label shop6SpyClover:
    $ shopCurrentSpy = 2
    hide green
    hide yellow
    show red:
        xalign 1.0 yalign -0.7
    call screen bgShop6
label shop6SpyAlex:
    $ shopCurrentSpy = 3
    hide green
    hide red
    show yellow:
        xalign 1.0 yalign -0.7
    call screen bgShop6





default loreSelect = 0
default acesEntry = 0
default acesLoreUnlock = 0

default punkEntry = 0
default punkLoreUnlock = 0

default outsidersEntry = 0
default outsidersLoreUnlock = 0

default epinesEntry = 0
default epinesLoreUnlock = 0

default huntersEntry = 0
default huntersLoreUnlock = 0

default glimmersEntry = 0
default glimmersLoreUnlock = 0

default woohpEntry = 0
default woohpLoreUnlock = 0

default miscEntry = 0
default miscLoreUnlock = 0

default loreAcesEntry1 = "The Aces have always been in Beverly Hills. A gang of rich kids, living the good life off of their parents money. They have always been involved in petty crimes and the occasional drug charge, but after WOOHP was taken over, they turned to more violent crime.\n\nMost Aces are spoiled snowflakes which run to their parents at the first sight of danger, but a few have found new purpose within the gang and are willing to fight tooth and nail to see their gang rise above all the others.\n\nWith money not being an issue for them, most Aces rob and steal just for the thrill of it. They are well equipped, but due to the exclusivity of their gang, are low in numbers."
default loreAcesEntry2 = "Despite numerous efforts to expand their influence, the Aces have never been able to establish themself outside of Beverly Hills. Many other cities and states where quickly turned off by their superiority complex and their entrance fee of $100.000.\n\nDespite their arrogance, the Aces are not without friends. They've been spotted with high ranking official of the VIK clothing label, who's under suspiscion of money laundering and drug trafficing.\n\nRecently the Aces have been spotted traveling to Spain more often and rumor has it that they're building a new headquarters for themselves."
default loreAcesEntry3 = "One of the Aces' favorite ways of spending money, is on cars. Street races and car modifying are a common occurrence and most members own at least a couple of pimped out cars. Even before the gang wars, the Aces were often busted for their races. However this didn't seem to deter them, as most of them could easily get their cars back after complaining to their parents.\n\nShop lifting doesn't happen very often within the Aces, as not paying or buying on discount is frowned upon by the gang. However, new members hoping to show off their style can sometimes rob stores if they currently lack the funds needed to keep up with the rest of the gang."
default loreAcesEntry4 = "Although no official will ever admit it, it's not a stretch to say that the Aces delve into politics from time to time. Several of their members are the children of influentiual politicians and their rivals have gone {i}'missing'{/i} in the past. The current mayor came into office with the promise to get rid of the Aces, but has since then been quiet on the subject.\n\nThat said, the Aces don't always get away scott-free. Last summer, a number of them were killed in a shoot-out with law enforcement. Which has noticibly effected the Aces, who before thought themselves to be immortal."
default loreAcesEntry5 = "The Aces set up in the marina after their nightclub burned down. Since then, they've been looking for a new place to hang out. They've made the marina their temperary head quarters because it's easily defendable and who wouldn't want to hang out near 30 milion dollar yachts?\n\nSeveral members own a boat (or rather their parents do) in the marina, so it's closely guarded without much, if any, trouble arising in the area. The Aces have a headquarters and boat owners have a safe place to store their overpriced yachts.\n\nAt one point the marina even housed a submarine for a day, but it has since then disappeared back into the ocean."
default loreAcesEntry6 = "Despite being at odds with all the other gangs in town, the Aces seem to share a personal rivalry with the Outsiders. Considered to be their absolute opposite, these two gangs often clash violently over their difference of ideology.\n\nDespite the Outsiders superior numbers, their lack of funding has lead them to be on the losing end of this conflict. Where the Outsiders see the Aces as arrogant, selfobsorbed and vain, the Aces see the Outsiders as poor, filthy and unsophisticated.\n\nAlthough not allied, the Aces seem to share a common interest with the Glimmers as they're often the ones to sell expensive jewelry to them."

default lorePunkEntry1 = "Of all the gangs in town, the Drift Punk are probably the most elusive. Popping up out of nowhere and then disappear without a trace. They hold relatively little ground, but seem to hold unto the Silicon Valley part of Beverly Hills just because they think it's theirs.\n\nBy far the weirdest mash-up, Drift Punk combined music and technology. Combining both nerd and rave cultures together. You will therefor sometimes see nerdly looking guys break dancing on the street, while miniskirt wearing rave girls play D&D.\n\nDrift Punk seems to have an edge over the other gangs, in that they're able to seemlessly blend in to their environment. Quickly going from gangmembers to your friendly everyday civillian."
default lorePunkEntry2 = "Drift Punk seems to make its money mostly with white-collar crime. Despite the occasional outburst, the Punks are mostly a non-violent gang. Obting to make their money by hacking bank accounts and espionage.\n\nUnlike their neighbors at the Marina, Drift Punk doesn't seem to waste their money like the Aces do. Most of their ill gotten goods are hardware, software and musical equipment (and of course lots of pirated songs).\n\nDespite several attempts to open a large night club for themselves, they are often foiled by rival gangs, leading them to host underground parties for members only."
default lorePunkEntry3 = "Having been pushed around for most of their life, the Drift Punks share a rivalry with the Hunters, which is mostly made up of athletes and former highschool bullies. Despite their bitter hatred, the gang is not too fuzzed about getting revenge. With many of its members being former athletes turned dancers. Drift Punk will still pull the occasional prank on the Hunters.\n\nA small point of contengion is that Malibu University is still in the hands of the Hunters, which the Punks believe should be rightfully theirs. Attempts to take the area from the Hunters has so far been unsuccesful however."
default lorePunkEntry4 = "What they lack in strength, the Punks make up with intellect and guile. Using guerrilla tactics to hit their target, before going underground again. Drift Punk owned streets usually don't show any signs of their gang and could easily be mistaken as unclaimed territory. They will often let smaller oblivious gangs move in to serve as as buffer between them and the more dangerous enemies in town.\n\nDespite their aversion to fighting, the Drift Punks are no push-overs and when other gangs push their luck too much, they are often dealt with quickly and efficiently. Using highly advanced gadgets and technology to aid them in their fight, most gangs know not to pick a fight unless absolutely necessary."
default lorePunkEntry5 = "Despite the gangs seemingly level-headed nature, the Drift Punks are dealing with a serious substance abuse problem. Many of its members seem to be addicted to some kind of drug allowing them to continue programming or partying till the small hours of the morning.\n\nChoosing not to rely on the other gangs to supply drugs, in fear of being cut off, the Drift Punk instead produce the chemicals themselves.\n\nThe Drift Punk leadership has acknowledge the rampart drug use and is attempting to curb it, although so far has not had a lot of succes in their endeavours."
default lorePunkEntry6 = "Being situated in Silicon Valley, the Drift Punks have been arming themselves with some of the finest weapons in town. Often using high-tech equipment, ranging from night vision to infra red. Using drones to scout for them and sometimes even hacking into satallites. Their weaponry seems to be purely defensive however as the gang doesn't seem too interested in actual conquest.\n\nTheir nerdy side often leads other gangs to make fun of them, but they'll quickly back off when a Drift Punk pulls a plasma gun or puts down a fully automatic sentry gun. Perhaps unsurprisingly the Drift Punks like using audio-based less-than-lethal weapons to deter their enemies from coming too close."

default loreOutsidersEntry1 = "The Outsiders originate from Beverly Hills, but were too small to be considered a gang. More like a few trouble youth who were rebelling against, as they call it, 'The System'. They had the occasional conflict with the law for skating, parkouring and tagging buildings, but were relatively harmless.\n\nThe Outsiders became more dangerous when a private security company (PSC) was brought in to stop their vandalism. The PSC's ruthless crackdown on the Outsiders lead to them fighting back.\n\nThe biggest incident happened when one of the Outsiders was shot and killed for stealing a pack of condomns from a convenience store.The Outsiders have been on the war path for revenge ever since."
default loreOutsidersEntry2 = "When WOOHP was taken over, the Outsiders were chosen to be one of the primary gangs to lead the revolt against the city. Gangsters from out of state were brought in to bolster their ranks and despite the same leaders being in charge as before, the Outsiders have changed considerably. Taking in anyone who is downtrotten, outcast or wants to fight back against a world that has wronged them in some way.\n\nTo keep up their finances, the Outsiders are in the weapon dealing business and scrap. Usually selling the scrap and other parts they've harvested from cars to a dealership out of town."
default loreOutsidersEntry3 = "The Outsiders don't consider themselves to be bad. They realize that they might not belong to Beverly Hills and have no plans for a lasting dominance over the city. They just want to kick back against the world that has excluded them and treated them like dirt. All the while fighting back against consumerism and pop-culture.\n\nBy nature, the Outsiders aren't interested in dominace, but after the aggressive expansion of the Aces, they've decided to drive them out of town before relaxing their grip on the city. The Aces, having found a rival, all but gladly return the challenge. Leading to violent conflict in the streets."
default loreOutsidersEntry4 = "The Security force that was hired to take care of the Outsiders pulled out of Beverly Hills as soon as the fighting began. Which has always been a sore spot for the gang. Seeing their chance for revenge disappear with it. In truth, it was a blessing as PSC could have easily dominated the city.\n\nAs a new goal in life, the Outsiders seem bend on showing the people of Beverly Hills the error of consumerism and will express it by destroying store windows and vandalising office buildings belong to mega corperations. So set in their ways, their rightiousness sometimes blinds them to the harm they're causing causing many in Beverly Hills to treat them with disdain. Which the Outsiders in turn see as ostracism."
default loreOutsidersEntry5 = "Although originally non-violent, the Outsiders now-a-days are hotheaded and rash. Which has lead to a lot of street violence and armed assaults. Despite their leadership attempting to temper the gang's aggression, it has shown to make little difference. Their members finally have cause worth fighting and dying for.\n\nThis armed conflict is not helped by their out of city scrap dealership, which is also supplying them with firearms. Leaving the gang in an awkward position. They need to stay on good terms with their supplier, whilst drifting further and further away from their non-violent roots."
default loreOutsidersEntry6 = "Currently the gang uses an abanddoned theme park as their headquarters. The site was suppose to be broken down last year, but instead the city decided to leave it as as hangout for teenagers. Mostly to save money on having to break it down. Now the Outsiders have made it their home, with make-shift skate ramps, graffiti covered walls and most importantly defenses.\n\nDespite the carnival grounds looking like an innocent hangout spot, the Outsiders have gone through lengths to defend the property from people who want them out. Setting up choke-points, traps and barricades. It might be a fortress of rags, but it's a fortress non-the-less."

default loreEpinesEntry1 = "One of the minor gangs, Les Epines is lead by the fanatical Silva Abegail and her desires to reclaim the earth for mother nature. Bringing in rare and exotic plantlife to do so.\n\nSeen as a threat by most other gangs, most of them have held off on attacking them due to the sheer weirdness of Les Epines. Their plants shoot venomous acids, can trap or strangle victims or in some cases even straight up eat trespassers. Bring with them many strange and sometimes horrifying diseases. The other gangs have opted to mostly stay clear of Les Epines, even as they see its vines slowly begin to creep through the once pleasant streets of Beverly Hills."
default loreEpinesEntry2 = "Joining Silva are a gang of radical eco-terrorist. Having been brought in from out of town, these maniacs share their leader's desire to bring the planet back to what it was suppose to be, without those pesky humans ruining the landscape with their concrete and car parks.\n\nMade up mostly of radicals, the gang does supplement their workforce with an assortment of nanocontrolled goons from out of town. Besides their obediance, these gangsters seem to be enthralled by Silva. Leading some to suspect that she's using more than just nanobots to control her followers."
default loreEpinesEntry3 = "Silva Abegail was originally caught in France, her home country, after planning to set off a dirty bomb in Paris. Unequipped to deal with her peculiar powers, they shipped her off to the States to have her be imprissoned by WOOHP. Here she has remained in a top security asylum for treatment. At least until the breakout.\n\nDespite being ranked as one of the weaker gangs, the name Silva is both feared and admired amongst the other gangsters of Beverly Hills. Silva has been able to accomplish by herself what others took dozens of people to do. The odd nature of the gang has prevented them to make allies though. And the more the mysterious gang hides in their jungle, the more suspicious the other gangs become."

default loreHuntersEntry1 = "Made up out of former athletes, this gang is mostly lead through nanobot control. Using its members as zombies to accomplish their goals. Finding their origins as a football club, they quickly grew up to be a considerable gang. Relying mostly on strength and brute force.\n\nDespite their strength, the gang suffers from heavy infighting. Being lead by ex-WOOHP convicts who all seem to have their own agenda, the gang suffers from direction and is therefor considered one of the minor gangs in town. They have a 'survival of the fittest' mindset and are mostly made up out of athletes, cheerleaders and their rabid fans."
default loreHuntersEntry2 = "Although originally not a gang, the members of The Hunters seem to give little thought to violent crime. Often seeing it as taking the spoils of their conquest. Although the gang uses almost no fire arms, they are known to fight hand to hand and often don't stop punching unless one of their own holds them back.\n\nLeading through intimidation, they have taken over the school and the football stadium and dared anyone to come and take them. Due to the low priority of these two areas, most other gangs have left them alone for now, though Drift Punk seems to take issues with them holding Malibu University. A fact that the Hunters seem to gloat over them."
default loreHuntersEntry3 = "Rioting is a big problem amonst the Hunter, even before WOOHP was taken over. Legions of supporters would take to the streets after a game and would cause untold damage to the city. This hasn't gone down after they were infeced with nanobots, in fact the supporters of the gang are more violent than ever.\n\nDespite being unorganised, the gang has had some experiencing fighting against riot police in the past and their love for the team unites them under a single banner. That said, the gang is easily provoked and other gangs have taunted their members by shipping opposite team jerseys to them."

default loreGlimmersEntry1 = "If you're looking to get rich and show off your wealth, the Glimmers are where it's at. Where the Aces show off by buying expensive clothes and cars, the Glimmers pour all of their ill gotten money into gold, silver and platinum. Decorated with large golden chains, rings and grills, these gangsters value precious materials above all else.\n\nThe gang was formed in Washington about 2 years back, but saw little success until a highly lucerative spree of jewelshop robberies. Having to lay low, they jumped at the opperatunity to go to Beverly Hills to continue their heists."
default loreGlimmersEntry2 = "Despite their rugged looks, the Glimmers are not known for their violence, instead obting to get what they want through intimidation. During a robbery they might shout, curse and threaten, but it is all part of an act to scare the shop owners to give them what they want before quickly exiting again.\n\nThis doesn't mean they're not dangerous. Gold plated assault rifles, guns and knuckles are common amongst the Glimmers. With weapons this expensive, it's become a running joke with the other gangs that the Glimmers are too afraid to fire their guns in fear that they might get damaged."
default loreGlimmersEntry3 = "The Glimmers are brand new in Beverly Hills and potential allies quickly lined up, attracted to the gang's shiny golden looks. They quickly found out that the Glimmers do not share their wealth with outsiders. If you want to bling, you have to join and pull your weight.\n\nThe Glimmer population saw a sharp increase of members after that. All tempted with the promise of gold. The Aces quickly disregarded the gang as 'tacky', the Outsiders were turned off by their hoarding of wealth and the Drift Punk just scratch their heads, wondering how anyone could be so interested by a shiny metal that comes out of the ground."
default loreGlimmersEntry4 = "Although the gang has a frontline of tough guys, at its core it's a lot more civilized. Expert goldsmiths work away tirelessly to make one masterpiece after another and are put on a pedestal by the gangsters. Many art collectors and those who enjoy the finer things in life have already expressed eagerness to buy beautiful pieces from the guild. Although the Glimmers aren't known to share their gold, with enough money they can buy more of it, so it's a win-win.\n\nDon't try to trick or steal from them though. The last person who thought the Glimmers were all bark and no bite tried to steal from them and didn't survive to tell the tale."

screen bgLore:

    vbox xalign 0.99 yalign 0.02:
        imagebutton:
            idle "gui/missionScreen/exitButton2.png"
            hover "gui/missionScreen/exitButton2-hover.png"
            action Jump("worldmap")

    if gang1Active or task16Stage >= 6:
        vbox xpos 0.05 ypos 50:
            imagebutton:
                idle "gui/lore/btLoreAces.png"
                hover "gui/lore/btLoreAces-hover.png" tooltip "acesLore"
                action SetVariable("loreSelect", 1)
    if gang2Active or task23Stage >= 7:
        vbox xpos 0.05 ypos 120:
            imagebutton:
                idle "gui/lore/btLorePunk.png"
                hover "gui/lore/btLorePunk-hover.png" tooltip "punkLore"
                action SetVariable("loreSelect", 2)
    if gang3Active or task25Stage >= 11:
        vbox xpos 0.05 ypos 190:
            imagebutton:
                idle "gui/lore/btLoreOutsiders.png"
                hover "gui/lore/btLoreOutsiders-hover.png" tooltip "outsidersLore"
                action SetVariable("loreSelect", 3)
    if gang4Active or socialSilva >= 7:
        vbox xpos 0.05 ypos 260:
            imagebutton:
                idle "gui/lore/btLoreEpines.png"
                hover "gui/lore/btLoreEpines-hover.png" tooltip "epinesLore"
                action SetVariable("loreSelect", 4)
    vbox xpos 0.05 ypos 330:
        imagebutton:
            idle "gui/lore/btLoreHunters.png"
            hover "gui/lore/btLoreHunters-hover.png" tooltip "huntersLore"
            action SetVariable("loreSelect", 5)
    vbox xpos 0.05 ypos 400:
        imagebutton:
            idle "gui/lore/btLoreGlimmers.png"
            hover "gui/lore/btLoreGlimmers-hover.png" tooltip "glimmersLore"
            action SetVariable("loreSelect", 6)
    vbox xpos 0.05 ypos 470:
        imagebutton:
            idle "gui/lore/btLore.png"
            hover "gui/lore/btLore-hover.png" tooltip "exchangeLore"
            action SetVariable("loreSelect", 7)
    vbox xpos 0.05 ypos 540:
        imagebutton:
            idle "gui/lore/btLoreWOOHP.png"
            hover "gui/lore/btLoreWOOHP-hover.png" tooltip "woohpLore"
            action SetVariable("loreSelect", 8)
    vbox xpos 0.05 ypos 610:
        imagebutton:
            idle "gui/lore/btLoreMisc.png"
            hover "gui/lore/btLoreMisc-hover.png" tooltip "miscLore"
            action SetVariable("loreSelect", 9)
    $ tooltip = GetTooltip()
    if tooltip == "acesLore":
        text "{font=fonts/freshMarker.ttf}ACES{/font}" xalign 0.11 yalign 0.07
    if tooltip == "punkLore":
        text "{font=fonts/freshMarker.ttf}DRIFT PUNK{/font}" xalign 0.11 yalign 0.17
    if tooltip == "outsidersLore":
        text "{font=fonts/freshMarker.ttf}OUTSIDERS{/font}" xalign 0.11 yalign 0.27
    if tooltip == "epinesLore":
        text "{font=fonts/freshMarker.ttf}LES EPINES{/font}" xalign 0.11 yalign 0.37
    if tooltip == "huntersLore":
        text "{font=fonts/freshMarker.ttf}HUNTERS{/font}" xalign 0.11 yalign 0.47
    if tooltip == "glimmersLore":
        text "{font=fonts/freshMarker.ttf}GLIMMERS{/font}" xalign 0.11 yalign 0.57
    if tooltip == "exchangeLore":
        text "{font=fonts/freshMarker.ttf}EXCHANGE{/font}" xalign 0.11 yalign 0.67
    if tooltip == "woohpLore":
        text "{font=fonts/freshMarker.ttf}WOOHP{/font}" xalign 0.11 yalign 0.77
    if tooltip == "miscLore":
        text "{font=fonts/freshMarker.ttf}MISC.{/font}" xalign 0.11 yalign 0.87

    if loreSelect == 1:
        text "{font=fonts/freshMarker.ttf}{size=+34}ACES{/size}{/font}" xalign 0.84 yalign 0.08
    if loreSelect == 2:
        text "{font=fonts/freshMarker.ttf}{size=+25}DRIFT PUNK{/size}{/font}" xalign 0.89 yalign 0.09
    if loreSelect == 3:
        text "{font=fonts/freshMarker.ttf}{size=+30}OUTSIDERS{/size}{/font}" xalign 0.89 yalign 0.09
    if loreSelect == 4:
        text "{font=fonts/freshMarker.ttf}{size=+25}LES EPINES{/size}{/font}" xalign 0.89 yalign 0.09
    if loreSelect == 5:
        text "{font=fonts/freshMarker.ttf}{size=+30}HUNTERS{/size}{/font}" xalign 0.88 yalign 0.08
    if loreSelect == 6:
        text "{font=fonts/freshMarker.ttf}{size=+30}GLIMMERS{/size}{/font}" xalign 0.88 yalign 0.08
    if loreSelect == 7:
        text "{font=fonts/freshMarker.ttf}{size=+30}EXCHANGE{/size}{/font}" xalign 0.88 yalign 0.08
    if loreSelect == 8:
        text "{font=fonts/freshMarker.ttf}{size=+36}WOOHP{/size}{/font}" xalign 0.85 yalign 0.08
    if loreSelect == 9:
        text "{font=fonts/freshMarker.ttf}{size=+33}MISC.{/size}{/font}" xalign 0.84 yalign 0.08

    if loreSelect == 1:
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 1{/size}{/font}" xalign 0.83 yalign 0.20:
            if acesLoreUnlock >= 1:
                action SetVariable("acesEntry", 1)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 2{/size}{/font}" xalign 0.83 yalign 0.25:
            if acesLoreUnlock >= 2:
                action SetVariable("acesEntry", 2)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 3{/size}{/font}" xalign 0.83 yalign 0.30:
            if acesLoreUnlock >= 3:
                action SetVariable("acesEntry", 3)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 4{/size}{/font}" xalign 0.83 yalign 0.35:
            if acesLoreUnlock >= 4:
                action SetVariable("acesEntry", 4)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 5{/size}{/font}" xalign 0.83 yalign 0.40:
            if acesLoreUnlock >= 5:
                action SetVariable("acesEntry", 5)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 6{/size}{/font}" xalign 0.83 yalign 0.45:
            if acesLoreUnlock >= 6:
                action SetVariable("acesEntry", 6)


        if acesEntry == 1:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreAcesEntry1]"
        if acesEntry == 2:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreAcesEntry2]"
        if acesEntry == 3:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreAcesEntry3]"
        if acesEntry == 4:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreAcesEntry4]"
        if acesEntry == 5:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreAcesEntry5]"
        if acesEntry == 6:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreAcesEntry6]"


    if loreSelect == 2:
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 1{/size}{/font}" xalign 0.83 yalign 0.20:
            if punkLoreUnlock >= 1:
                action SetVariable("punkEntry", 1)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 2{/size}{/font}" xalign 0.83 yalign 0.25:
            if punkLoreUnlock >= 2:
                action SetVariable("punkEntry", 2)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 3{/size}{/font}" xalign 0.83 yalign 0.30:
            if punkLoreUnlock >= 3:
                action SetVariable("punkEntry", 3)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 4{/size}{/font}" xalign 0.83 yalign 0.35:
            if punkLoreUnlock >= 4:
                action SetVariable("punkEntry", 4)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 5{/size}{/font}" xalign 0.83 yalign 0.40:
            if punkLoreUnlock >= 5:
                action SetVariable("punkEntry", 5)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 6{/size}{/font}" xalign 0.83 yalign 0.45:
            if punkLoreUnlock >= 6:
                action SetVariable("punkEntry", 6)


        if punkEntry == 1:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[lorePunkEntry1]"
        if punkEntry == 2:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[lorePunkEntry2]"
        if punkEntry == 3:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[lorePunkEntry3]"
        if punkEntry == 4:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[lorePunkEntry4]"
        if punkEntry == 5:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[lorePunkEntry5]"
        if punkEntry == 6:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[lorePunkEntry6]"


    if loreSelect == 3:
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 1{/size}{/font}" xalign 0.83 yalign 0.20:
            if outsidersLoreUnlock >= 1:
                action SetVariable("outsidersEntry", 1)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 2{/size}{/font}" xalign 0.83 yalign 0.25:
            if outsidersLoreUnlock >= 2:
                action SetVariable("outsidersEntry", 2)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 3{/size}{/font}" xalign 0.83 yalign 0.30:
            if outsidersLoreUnlock >= 3:
                action SetVariable("outsidersEntry", 3)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 4{/size}{/font}" xalign 0.83 yalign 0.35:
            if outsidersLoreUnlock >= 4:
                action SetVariable("outsidersEntry", 4)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 5{/size}{/font}" xalign 0.83 yalign 0.40:
            if outsidersLoreUnlock >= 5:
                action SetVariable("outsidersEntry", 5)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 6{/size}{/font}" xalign 0.83 yalign 0.45:
            if outsidersLoreUnlock >= 6:
                action SetVariable("outsidersEntry", 6)


        if outsidersEntry == 1:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreOutsidersEntry1]"
        if outsidersEntry == 2:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreOutsidersEntry2]"
        if outsidersEntry == 3:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreOutsidersEntry3]"
        if outsidersEntry == 4:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreOutsidersEntry4]"
        if outsidersEntry == 5:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreOutsidersEntry5]"
        if outsidersEntry == 6:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreOutsidersEntry6]"


    if loreSelect == 4:
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 1{/size}{/font}" xalign 0.83 yalign 0.20:
            if epinesLoreUnlock >= 1:
                action SetVariable("epinesEntry", 1)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 2{/size}{/font}" xalign 0.83 yalign 0.25:
            if epinesLoreUnlock >= 2:
                action SetVariable("epinesEntry", 2)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 3{/size}{/font}" xalign 0.83 yalign 0.30:
            if epinesLoreUnlock >= 3:
                action SetVariable("epinesEntry", 3)


        if epinesEntry == 1:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreEpinesEntry1]"
        if epinesEntry == 2:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreEpinesEntry2]"
        if epinesEntry == 3:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreEpinesEntry3]"


    if loreSelect == 5:
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 1{/size}{/font}" xalign 0.83 yalign 0.20:
            if huntersLoreUnlock >= 1:
                action SetVariable("huntersEntry", 1)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 2{/size}{/font}" xalign 0.83 yalign 0.25:
            if huntersLoreUnlock >= 2:
                action SetVariable("huntersEntry", 2)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 3{/size}{/font}" xalign 0.83 yalign 0.30:
            if huntersLoreUnlock >= 3:
                action SetVariable("huntersEntry", 3)


        if huntersEntry == 1:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreHuntersEntry1]"
        if huntersEntry == 2:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreHuntersEntry2]"
        if huntersEntry == 3:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreHuntersEntry3]"


    if loreSelect == 6:
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 1{/size}{/font}" xalign 0.83 yalign 0.20:
            if glimmersLoreUnlock >= 1:
                action SetVariable("glimmersEntry", 1)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 2{/size}{/font}" xalign 0.83 yalign 0.25:
            if glimmersLoreUnlock >= 2:
                action SetVariable("glimmersEntry", 2)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 3{/size}{/font}" xalign 0.83 yalign 0.30:
            if glimmersLoreUnlock >= 3:
                action SetVariable("glimmersEntry", 3)


        if glimmersEntry == 1:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreGlimmersEntry1]"
        if glimmersEntry == 2:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreGlimmersEntry2]"
        if glimmersEntry == 3:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreGlimmersEntry3]"


    if loreSelect == 8:
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 1{/size}{/font}" xalign 0.83 yalign 0.20:
            if woohpLoreUnlock >= 1:
                action SetVariable("woohpEntry", 1)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 2{/size}{/font}" xalign 0.83 yalign 0.25:
            if woohpLoreUnlock >= 2:
                action SetVariable("woohpEntry", 2)
        textbutton "{font=fonts/freshMarker.ttf}{size=+3}Entry 3{/size}{/font}" xalign 0.83 yalign 0.30:
            if woohpLoreUnlock >= 3:
                action SetVariable("woohpEntry", 3)


        if woohpEntry == 1:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreWoohpEntry1]"
        if woohpEntry == 2:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreWoohpEntry2]"
        if woohpEntry == 3:
            hbox:
                spacing 10 xalign 0.3 ypos 60 xsize 700
                text "[loreWoohpEntry3]"






define explosion1 = "audio/sfx/explosion1.mp3"
define laser1 = "audio/sfx/laser1.mp3"
define sfxText = "audio/sfx/sfxText.mp3"





init:
    $ import time

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()




default gadgetUsed = 0
default bagRadioName = "- - -"
default bagItemsName = "- - -"

default missionMode = 1



screen equipmentMenu:
    if tutStage >= 5:
        vbox xalign 0.99 yalign 0.05:
            imagebutton:
                idle "mission/bag1.png"
                hover "mission/bag1-hover.png"
                action Show("bagInteract")

    if hiddenStatus == 0:
        add "mission/hiddenStatus0.png" xalign 0.01 yalign 0.0
    if hiddenStatus == 1:
        add "mission/hiddenStatus1.png" xalign 0.01 yalign 0.0
    if hiddenStatus >= 2:
        add "mission/hiddenStatus2.png" xalign 0.01 yalign 0.0






label switchMode:
    if missionMode == 1:
        play sound "audio/sfx/modeKiss.mp3"
        $ missionMode = 2
        jump jumpStartScene
    elif True:
        play sound "audio/sfx/modeFight.mp3"
        $ missionMode = 1
        jump jumpStartScene



screen bgShop7:
    add "gui/itemUI/shop7/sam/bgShop7.png"


    text "{font=fonts/freshMarker.ttf}{size=+4}{color=#ffeda6}{color=#ffffff}[cash]{/color}{/size}{/font}" xpos 180 yalign 0.09


    vbox xalign 0.01 yalign 0.012:
        imagebutton:
            idle "gui/itemUI/shop1/exit1.png"
            hover "gui/itemUI/shop1/exit1-hover.png"
            action SetVariable("shopTotal", 0), Jump("exitShop")


    vbox xalign 0.085 yalign 0.95:
        imagebutton:
            idle "gui/itemUI/shop1/prv.png"
            hover "gui/itemUI/shop1/prv-hover.png"

    vbox xalign 0.55 yalign 0.95:
        imagebutton:
            idle "gui/itemUI/shop1/nxt.png"
            hover "gui/itemUI/shop1/nxt-hover.png"


    if shopCurrentSpy == 1:
        if spyGreenActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Sam"
    elif shopCurrentSpy == 2:
        if spyRedActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Clover"
    elif shopCurrentSpy == 3:
        if spyYellowActive == False:
            $ shopSpyName = "???"
        else:
            $ shopSpyName = "Alex"
    hbox:
        spacing 10 xalign 0.64 yalign 0.29
        text "{color=#ffffff}{size=+12}{font=fonts/freshmarker.ttf}[shopSpyName]{/font}{/color}{/color}"




    vbox xalign 0.67 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpySam.png"
            hover "gui/itemUI/shopSpySam-hover.png"
            action Jump("shop7SpySam")

    vbox xalign 0.77 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyClover.png"
            hover "gui/itemUI/shopSpyClover-hover.png"
            action Jump("shop7SpyClover")

    vbox xalign 0.87 yalign 0.050:
        imagebutton:
            idle "gui/itemUI/shopSpyAlex.png"
            hover "gui/itemUI/shopSpyAlex-hover.png"
            action Jump("shop7SpyAlex")





    if shopCurrentSpy == 1:
        if cellSamBookcase == 0:
            vbox xalign 0.12 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/bookcase.png"
                    hover "gui/itemUI/shop7/sam/bookcase-hover.png"
                    action SetVariable("shopItemSelect", 1)
            vbox xalign 0.1 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamBookcase", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamBooks == 0:
            vbox xalign 0.24 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/books.png"
                    hover "gui/itemUI/shop7/sam/books-hover.png"
                    action SetVariable("shopItemSelect", 2)
            vbox xalign 0.225 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.28 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamBooks", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamHangingChair == 0:
            vbox xalign 0.37 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/chair2.png"
                    hover "gui/itemUI/shop7/sam/chair2-hover.png"
                    action SetVariable("shopItemSelect", 3)
            vbox xalign 0.347 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.405 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamHangingChair", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamCouch == 0:
            vbox xalign 0.505 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/couch.png"
                    hover "gui/itemUI/shop7/sam/couch-hover.png"
                    action SetVariable("shopItemSelect", 4)
            vbox xalign 0.475 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.529 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamCouch", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamShoes == 0:
            vbox xalign 0.12 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/shoes.png"
                    hover "gui/itemUI/shop7/sam/shoes-hover.png"
                    action SetVariable("shopItemSelect", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamShoes", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamStatue == 0:
            vbox xalign 0.24 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/statue.png"
                    hover "gui/itemUI/shop7/sam/statue-hover.png"
                    action SetVariable("shopItemSelect", 6)
            vbox xalign 0.225 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamStatue", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamMirror == 0:
            vbox xalign 0.37 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/mirror.png"
                    hover "gui/itemUI/shop7/sam/mirror-hover.png"
                    action SetVariable("shopItemSelect", 7)
            vbox xalign 0.347 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.405 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamMirror", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamPainting == 0:
            vbox xalign 0.505 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/painting.png"
                    hover "gui/itemUI/shop7/sam/painting-hover.png"
                    action SetVariable("shopItemSelect", 8)
            vbox xalign 0.475 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.53 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamPainting", 1)
                    else:
                        action Jump("shopNoCash")

        if cellSamWatch == 0:
            vbox xalign 0.12 yalign 0.79:
                imagebutton:
                    idle "gui/itemUI/shop7/sam/watch.png"
                    hover "gui/itemUI/shop7/sam/watch-hover.png"
                    action SetVariable("shopItemSelect", 9)
            vbox xalign 0.1 yalign 0.685:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.837:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellSamWatch", 1)
                    else:
                        action Jump("shopNoCash")

    if shopCurrentSpy == 2:
        if cellCloverLaptop == 0:
            vbox xalign 0.12 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/Clover/laptop.png"
                    hover "gui/itemUI/shop7/Clover/laptop-hover.png"
                    action SetVariable("shopItemSelect", 1)
            vbox xalign 0.1 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellCloverLaptop", 1)
                    else:
                        action Jump("shopNoCash")

        if cellCloverDesk == 0:
            vbox xalign 0.24 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/Clover/desk.png"
                    hover "gui/itemUI/shop7/Clover/desk-hover.png"
                    action SetVariable("shopItemSelect", 2)
            vbox xalign 0.225 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.28 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellCloverDesk", 1)
                    else:
                        action Jump("shopNoCash")

        if cellCloverLights1 == 0:
            vbox xalign 0.37 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/Clover/lights.png"
                    hover "gui/itemUI/shop7/Clover/lights-hover.png"
                    action SetVariable("shopItemSelect", 3)
            vbox xalign 0.347 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.405 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellCloverLights1", 1)
                    else:
                        action Jump("shopNoCash")

        if cellCloverPainting == 0:
            vbox xalign 0.505 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/Clover/painting.png"
                    hover "gui/itemUI/shop7/Clover/painting-hover.png"
                    action SetVariable("shopItemSelect", 4)
            vbox xalign 0.475 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.529 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellCloverPainting", 1)
                    else:
                        action Jump("shopNoCash")

        if cellCloverVR == 0:
            vbox xalign 0.12 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/Clover/vr.png"
                    hover "gui/itemUI/shop7/Clover/vr-hover.png"
                    action SetVariable("shopItemSelect", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellCloverVR", 1)
                    else:
                        action Jump("shopNoCash")

        if cellCloverChair == 0:
            vbox xalign 0.24 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/Clover/chair.png"
                    hover "gui/itemUI/shop7/Clover/chair-hover.png"
                    action SetVariable("shopItemSelect", 6)
            vbox xalign 0.225 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellCloverChair", 1)
                    else:
                        action Jump("shopNoCash")

        if cellCloverClothes == 0:
            vbox xalign 0.37 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/Clover/clothes.png"
                    hover "gui/itemUI/shop7/Clover/clothes-hover.png"
                    action SetVariable("shopItemSelect", 7)
            vbox xalign 0.347 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.405 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellCloverClothes", 1)
                    else:
                        action Jump("shopNoCash")

    if shopCurrentSpy == 3:
        if cellAlexBear == 0:
            vbox xalign 0.12 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/bear.png"
                    hover "gui/itemUI/shop7/Alex/bear-hover.png"
                    action SetVariable("shopItemSelect", 1)
            vbox xalign 0.1 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexBear", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexBoombox == 0:
            vbox xalign 0.24 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/boombox.png"
                    hover "gui/itemUI/shop7/Alex/boombox-hover.png"
                    action SetVariable("shopItemSelect", 2)
            vbox xalign 0.225 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.28 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexBoombox", 1)
                    else:
                        action Jump("shopNoCash")



        if cellAlexCans == 0:
            vbox xalign 0.505 yalign 0.27:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/cans.png"
                    hover "gui/itemUI/shop7/Alex/cans-hover.png"
                    action SetVariable("shopItemSelect", 4)
            vbox xalign 0.475 yalign 0.22:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.529 yalign 0.374:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexCans", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexChair == 0:
            vbox xalign 0.12 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/chair.png"
                    hover "gui/itemUI/shop7/Alex/chair-hover.png"
                    action SetVariable("shopItemSelect", 5)
            vbox xalign 0.1 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexChair", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexClothes == 0:
            vbox xalign 0.24 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/clothes.png"
                    hover "gui/itemUI/shop7/Alex/clothes-hover.png"
                    action SetVariable("shopItemSelect", 6)
            vbox xalign 0.225 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.28 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexClothes", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexDesk == 0:
            vbox xalign 0.37 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/desk.png"
                    hover "gui/itemUI/shop7/Alex/desk-hover.png"
                    action SetVariable("shopItemSelect", 7)
            vbox xalign 0.347 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.405 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexDesk", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexGraffiti == 0:
            vbox xalign 0.505 yalign 0.52:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/graffiti.png"
                    hover "gui/itemUI/shop7/Alex/graffiti-hover.png"
                    action SetVariable("shopItemSelect", 8)
            vbox xalign 0.475 yalign 0.45:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.53 yalign 0.6:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexGraffiti", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexGuitar == 0:
            vbox xalign 0.12 yalign 0.79:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/guitar.png"
                    hover "gui/itemUI/shop7/Alex/guitar-hover.png"
                    action SetVariable("shopItemSelect", 9)
            vbox xalign 0.1 yalign 0.685:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.155 yalign 0.837:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexGuitar", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexNightstand == 0:
            vbox xalign 0.24 yalign 0.79:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/nightstand.png"
                    hover "gui/itemUI/shop7/Alex/nightstand-hover.png"
                    action SetVariable("shopItemSelect", 10)
            vbox xalign 0.225 yalign 0.685:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.28 yalign 0.837:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexNightstand", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexPosters == 0:
            vbox xalign 0.37 yalign 0.79:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/posters.png"
                    hover "gui/itemUI/shop7/Alex/posters-hover.png"
                    action SetVariable("shopItemSelect", 11)
            vbox xalign 0.347 yalign 0.685:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.405 yalign 0.837:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexPosters", 1)
                    else:
                        action Jump("shopNoCash")

        if cellAlexPosters2 == 0:
            vbox xalign 0.505 yalign 0.79:
                imagebutton:
                    idle "gui/itemUI/shop7/Alex/posters2.png"
                    hover "gui/itemUI/shop7/Alex/posters2-hover.png"
                    action SetVariable("shopItemSelect", 12)
            vbox xalign 0.475 yalign 0.685:
                text "{font=fonts/freshmarker.ttf}{size=-4}$600{/size}{/font}"

            vbox xalign 0.53 yalign 0.837:
                imagebutton:
                    idle "gui/itemUI/purchase.png"
                    hover "gui/itemUI/purchase-hover.png"
                    if cash >= 600:
                        action SetVariable("cash", cash - 600), SetVariable("cellAlexPosters2", 1)
                    else:
                        action Jump("shopNoCash")


    if shopItemSelect == 1:
        vbox xalign 0.097 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 2:
        vbox xalign 0.235 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 3:
        vbox xalign 0.368 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 4:
        vbox xalign 0.50 yalign 0.25:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 5:
        vbox xalign 0.097 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 6:
        vbox xalign 0.235 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 7:
        vbox xalign 0.368 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 8:
        vbox xalign 0.50 yalign 0.525:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 9:
        vbox xalign 0.097 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 10:
        vbox xalign 0.235 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 11:
        vbox xalign 0.368 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"
    if shopItemSelect == 12:
        vbox xalign 0.50 yalign 0.808:
            add "gui/itemUI/shopSelectBox.png"

label shop7SpySam:
    $ shopCurrentSpy = 1
    hide red
    hide yellow
    show green g1:
        xalign 1.0 yalign -0.7
    call screen bgShop7
label shop7SpyClover:
    $ shopCurrentSpy = 2
    hide green
    hide yellow
    show red:
        xalign 1.0 yalign -0.7
    call screen bgShop7
label shop7SpyAlex:
    $ shopCurrentSpy = 3
    hide green
    hide red
    show yellow:
        xalign 1.0 yalign -0.7
    call screen bgShop7

label jobTrickOrTreat:
    if mapSpy1Selected:
        $ greenDayJob = 102
        $ mapSpy1Selected = False
        $ spy1Status = 1
        sM "Trick or Treat!"
    if mapSpy2Selected:
        $ redDayJob = 102
        $ mapSpy2Selected = False
        $ spy2Status = 2
        cM "Trick or Treat!"
    if mapSpy3Selected:
        $ yellowDayJob = 102
        $ mapSpy3Selected = False
        $ spy3Status = 3
        aM "Trick or Treat!"
    jump worldmap




screen bagInteract:
    modal True
    default x = renpy.get_mouse_pos()[0]
    default y = renpy.get_mouse_pos()[1]
    frame:
        xpos 1093 ypos 100
        has vbox
        textbutton _("Gadgets"):
            action Show("bagInteractGadgets"), Hide("bagInteractBackup"), Hide("bagInteractItems")
        textbutton "[bagRadioName]":
            action Show("bagInteractBackup"), Hide("bagInteractGadgets"), Hide("bagInteractItems")
        textbutton "[bagItemsName]":
            if bagItemsName != "- - -":
                action Show("bagInteractItems"), Hide("bagInteractGadgets"), Hide("bagInteractBackup")
        textbutton "Cancel":
            action Hide("bagInteract")



label woohpHQ:
    scene black with fade
    pause 1.0
    scene bgHQ
    with fade
    if task26Stage == 2:
        jump task26
    call screen HQButtons
    pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
