label nightCycle:

    if task26Stage == 27:
        stop music fadeout 3.0
        scene black with fade
        show text "Despite the chaos, you manage to get some rest."
        $ tod = 1
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
        call screen mapButtonsRaidFinale


    hide scene_darkening
    hide green
    hide red
    hide yellow

    define task5Counter = 0
    if task5Stage == 5:
        $ task5Counter += 1
    if task5Counter == 3:
        $ task5Counter = 0
        $ task5Stage = 6

    if task9Stage == 2:
        $ task9Stage = 3


    if greenStrip >= 1:
        $ greenStrip = 0
        $ greenStripXP += 1
        $ randStripRwd = renpy.random.randint(100, 180)
        if greenStripXP >= 5:
            $ randStripRwd += 25
        if greenStripXP >= 10:
            $ randStripRwd += 25
        if greenStripXP >= 15:
            $ randStripRwd += 25
        if greenStripXP >= 20:
            $ randStripRwd += 25
        if greenStripXP >= 25:
            $ randStripRwd += 25
        if skillRank >= 6:
            $ randStripRwd += 25
        $ cash += randStripRwd
        "Sam made $[randStripRwd] working at the stripclub."
        $ randMoney = randStripRwd
        call missionRewardMoney from _call_missionRewardMoney_78
        $ randStripRwd = 0
    if redStrip >= 1:
        $ redStrip = 0
        $ redStripXP += 1
        $ randStripRwd = renpy.random.randint(100, 200)
        if redStripXP >= 5:
            $ randStripRwd += 25
        if redStripXP >= 10:
            $ randStripRwd += 25
        if redStripXP >= 15:
            $ randStripRwd += 25
        if redStripXP >= 20:
            $ randStripRwd += 25
        if redStripXP >= 25:
            $ randStripRwd += 25
        if skillRank >= 6:
            $ randStripRwd += 25
        $ cash += randStripRwd
        "Clover made $[randStripRwd] working at the stripclub."
        $ randMoney = randStripRwd
        call missionRewardMoney from _call_missionRewardMoney_79
        $ randStripRwd = 0
    if yellowStrip >= 1:
        $ yellowStrip = 0
        $ yellowStripXP += 1
        $ randStripRwd = renpy.random.randint(100, 180)
        if yellowStripXP >= 5:
            $ randStripRwd += 25
        if yellowStripXP >= 10:
            $ randStripRwd += 25
        if yellowStripXP >= 15:
            $ randStripRwd += 25
        if yellowStripXP >= 20:
            $ randStripRwd += 25
        if yellowStripXP >= 25:
            $ randStripRwd += 25
        if skillRank >= 6:
            $ randStripRwd += 25
        $ cash += randStripRwd
        "Alex made $[randStripRwd] working at the stripclub."
        $ randMoney = randStripRwd
        call missionRewardMoney from _call_missionRewardMoney_80
        $ randStripRwd = 0
    if kimStrip >= 1:
        $ kimStrip = 0
        $ kimStripXP += 1
        $ randStripRwd = renpy.random.randint(100, 180)
        if kimStripXP >= 5:
            $ randStripRwd += 25
        if kimStripXP >= 10:
            $ randStripRwd += 25
        if kimStripXP >= 15:
            $ randStripRwd += 25
        if kimStripXP >= 20:
            $ randStripRwd += 25
        if kimStripXP >= 25:
            $ randStripRwd += 25
        $ cash += randStripRwd
        "Kim made $[randStripRwd] working at the stripclub."
        $ randMoney = randStripRwd
        call missionRewardMoney from _call_missionRewardMoney_81
        $ randStripRwd = 0
    if silvaStrip >= 1:
        $ silvaStrip = 0
        $ randMoney = 100
        "Silva made $[randMoney] working at the stripclub."
        call missionRewardMoney from _call_missionRewardMoney_92
    if britneyStrip >= 1:
        $ britneyStrip = 0
        $ randMoney = 100
        "Britney made $[randMoney] working at the stripclub."
        call missionRewardMoney from _call_missionRewardMoney_93



    if dlc1Active == False:
        $ dlc1Active = True


    if injectorSmall <= 0:
        $ injectorSmall = 0
    if task26Stage == 17 and HQLiberated == 6:
        $ HQLiberated = 5


    if specialCandyStatus == 2 and task16Stage <= 3:
        $ task16Stage = 4
        "(WARNING: Noticing a bug in the script. Attempting to fix....)"
        jump task16


    $ acesBounty1 = 0
    $ acesBounty2 = 0
    $ acesBounty3 = 0

    if task26Stage >= 4 and britneyHidden == True:
        $ britneyHidden = False

    if task26Stage >= 11 and backupBritneyActive != True:
        $ backupBritneyActive = True

    if outfitSamUniformActive == True:
        $ outfitCloverUniformActive = True
        $ outfitAlexUniformActive = True
    if mallActive:
        $ beachActive = True

    if specialCandyStatus == 3 and task16Stage == 5:
        $ specialCandyStatus = 2
        $ prisonersNew = True


    $ _skipping = True


    if bagItemsName != "bagItemsName":
        if 3 <= task25Stage <= 8:
            pass
        elif True:
            $ bagItemsName = "Items"


    if task25Stage == 4:
        $ task25Stage = 3


    if task26Stage <= 6 and HQLiberated == 2:
        $ HQLiberated = 1


    $ aniStage = 1


    if hackPart >= 3 and gadgetHackActive == False:
        $ gadgetHackActive = True


    if task5Stage >= 5 and samSupLvl == 0:
        $ samSupLvl = 2
    if task5Stage >= 4 and cloverSupLvl == 0:
        $ cloverSupLvl = 2
    if task5Stage >= 4 and alexSupLvl == 0:
        $ alexSupLvl = 2


    if task5Stage == 8 and slutLevel == 1:
        $ slutLevel = 2


    if task3Stage >= 4 and specialMaggieStatus == 0:
        $ specialMaggieStatus = 1

    if task16Stage <= 4 and specialCandyStatus == 3:
        $ task16Stage = 5


    if nighttime4Event == False and task26Stage == 0:
        $ task26Stage = 1

    if month11CardClaimed == True:
        $ top5Alex = True

    if task2Stage >= 8:
        $ spyRedActive = True
        $ mapSpy2Active = True

    if cellSamBed == 0:
        $ cellSamBed = 1
    if cellCloverBed == 0:
        $ cellCloverBed = 1
    if cellAlexBed == 0:
        $ cellAlexBed = 1

    if task13Stage >= 5 and slutLevel <= 3:
        $ slutLevel = 4

    if sexAct3 == "Foreplay" and slutLevel <= 2:
        $ slutLevel = 3

    if task13Stage >= 4 and task5Nudes == False:
        $ task5Nudes = True

    hide screen progressSexScene4Alex

    if carlaSocial >= 1 and specialDragonStatus != 3:
        $ carlaSocial = 0

    if cellSamBed != 1:
        $ cellSamBed = 1
    if cellCloverBed != 1:
        $ cellCloverBed = 1
    if cellAlexBed != 1:
        $ cellAlexBed = 1


    hide screen nanoLevelSam
    hide screen nanoLevelClover
    hide screen nanoLevelAlex

    if specialTaliaStatus == 3 and punkRank == 2:
        pause 1.0
        $ punkRank = 3
        $ punkRep = 0



    if samSocial >= 4:
        $ samFriend = "Friend"
    if samSocial >= 8:
        $ samFriend = "Good Friend"
    if samSocial >= 12:
        $ samFriend = "Best Friend"

    if cloverSocial >= 4:
        $ cloverFriend = "Friend"
    if cloverSocial >= 8:
        $ cloverFriend = "Good Friend"
    if cloverSocial >= 12:
        $ cloverFriend = "Best Friend"

    if alexSocial >= 4:
        $ alexFriend = "Friend"
    if alexSocial >= 8:
        $ alexFriend = "Good Friend"
    if alexSocial >= 12:
        $ alexFriend = "Best Friend"


    $ greenStrip = 0
    $ redStrip = 0
    $ yellowStrip = 0




    if greenDayJob == 4:
        if clubStage <= 6:
            $ greenDayJob = 0
            $ clubStage += 1
            "Sam spent her evening cleaning up the bar."
            if clubStage >= 7:
                scene bgClub1
                with fade
                jump tutStage9
        elif True:
            "Sam spent the evening working."
            $ randMoney = renpy.random.randint(20, 80)
            call missionRewardMoney from _call_missionRewardMoney_10
            pause 0.2
    if redDayJob == 4:
        "Clover spend the evening working."
        $ randMoney = renpy.random.randint(20, 80)
        call missionRewardMoney from _call_missionRewardMoney_11
        pause 0.2
    if yellowDayJob == 4:
        "Alex spend the evening working."
        $ randMoney = renpy.random.randint(20, 80)
        call missionRewardMoney from _call_missionRewardMoney_12
        pause 0.2



    if spy1Status == 999:
        $ returnChance = renpy.random.randint(1,2)
        if returnChance == 1:
            $ greenDayJob = 0
            $ spy1Status = 0
            $ samMood -= 30
            "Sam managed to escape her captors and returns to the base. The kidnapping has negatively impacted her mood."

    if spy2Status == 999:
        $ returnChance = renpy.random.randint(1,2)
        if returnChance == 1:
            $ redDayJob = 0
            $ spy2Status = 0
            $ cloverMood -= 30
            "Clover managed to escape her captors and returns to the base. The kidnapping has negatively impacted her mood."

    if spy3Status == 999:
        $ returnChance = renpy.random.randint(1,2)
        if returnChance == 1:
            $ yellowDayJob = 0
            $ spy3Status = 0
            $ alexMood -= 30
            "Alex managed to escape her captors and returns to the base. The kidnapping has negatively impacted her mood."



    if samHealth <= 2:
        $ samHPTimer += 1
    if samHPTimer == 7:
        $ samHealth += 1
        $ samHPTimer = 0

    if cloverHealth <= 2:
        $ cloverHPTimer += 1
    if cloverHPTimer == 7:
        $ cloverHealth += 1
        $ cloverHPTimer = 0

    if alexHealth <= 2:
        $ alexHPTimer += 1
    if alexHPTimer == 7:
        $ alexHealth += 1
        $ alexHPTimer = 0

    if samHealth <= 1:
        $ samHealth = 1
    if cloverHealth <= 1:
        $ cloverHealth = 1
    if alexHealth <= 1:
        $ alexHealth = 1

    if samHealth >= 3:
        $ samHealth = 3
    if cloverHealth >= 3:
        $ cloverHealth = 3
    if alexHealth >= 3:
        $ alexHealth = 3


    if spy1Status == 999 or spy2Status == 999 or spy3Status == 999:
        pass
    elif emergencyCrimeSpree == 0:

        $ spy1Status = 0
        $ spy2Status = 0
        $ spy3Status = 0
    elif True:
        $ spy1Status = 10
        $ spy2Status = 10
        $ spy3Status = 10
        $ emergencyCrimeSpree -= 1
        $ coverCounter += 15
        if emergencyCrimeSpree <= 0:
            scene black with d3
            $ emergencyCrimeSpree = 0
            $ spy1Status = 0
            $ spy2Status = 0
            $ spy3Status = 0
            if spyGreenActive:
                $ samHealth -= 1
            if spyRedActive:
                $ cloverHealth -= 1
            if spyYellowActive:
                $ alexHealth -= 1
            "Your spies return from their crime rampage across the city. They're injured, but your notoriety has increased."


    $ mapSpy1Selected = False
    $ mapSpy2Selected = False
    $ mapSpy3Selected = False


    $ samSpySex = 0
    $ cloverSpySex = 0
    $ alexSpySex = 0


    $ greenDayJob = 0
    $ jobEventSam = 0
    $ redDayJob = 0
    $ jobEventClover = 0
    $ yellowDayJob = 0
    $ jobEventAlex = 0
    $ dailyStaffReport = False


    $ greenStripStage = 0
    $ redStripStage = 0
    $ yellowStripStage = 0
    $ kimStripStage = 0
    $ britneyStripStage = 0
    $ silvaStripStage = 0


    $ missionScreenGadget1Select = 0
    $ missionScreenGadget2Select = 0
    $ missionScreenGadget3Select = 0
    $ missionScreenGadget4Select = 0

    $ missionScreenFrontlineSelect = 0
    $ missionScreenSupportSelect = 0
    $ missionScreenDistractSelect = 0

    $ hiddenStatus = 0
    $ missionScreenCurrentLocation = 0

    hide screen gadgetMenu
    hide screen glassScreen
    hide screen spyMasturbate
    hide globalImage
    hide screen interactScreen
    hide screen equipmentMenu
    $ gadgetActive = 0

    $ greenBlush = 0
    $ redBlush = 0
    $ yellowBlush = 0

    if greenArms != 1:
        $ greenArms = 1
    if redArms != 1:
        $ redArms = 1
    if yellowArms != 1:
        $ yellowArms = 1


    if landgrabMessage == False:
        $ landgrabMessage = True


    if month != 10:
        $ spiritEncounter = 0
        if cellSamHall1 == 1:
            $ cellSamHall1 = 0
        if cellCloverHall1 == 1:
            $ cellCloverHall1 = 0
        if cellAlexHall1 == 1:
            $ cellAlexHall1 = 0

    if month != 12:
        if cellSamChrist1 == 1:
            $ cellSamChrist1 = 0
        if cellCloverChrist1 == 1:
            $ cellCloverChrist1 = 0
        if cellAlexChrist1 == 1:
            $ cellAlexChrist1 = 0


    if hackerUnlocked == True:
        $ hackProgress += 11
        if hackProgress >= 100:
            $ hackProgress = 100

    hide screen spyHacking


    call greenOutfitSet from _call_greenOutfitSet_1
    call redOutfitSet from _call_redOutfitSet_1
    call yellowOutfitSet from _call_yellowOutfitSet

    $ silOutfit = silOutfitSet


    if task2Stage >= 14 and gadgetVIBActive == False:
        $ gadgetVIBActive = True


    if slutLevel == 0 and greenChest == 0 or slutLevel == 0 and greenBottom == 0:
        if spyGreenActive:
            $ greenChestSet = 1
            $ greenBottomSet = 1
            $ greenChest = 1
            $ greenBottom = 1
        elif True:
            pass
    if slutLevel == 0 and redChest == 0 or slutLevel == 0 and redBottom == 0:
        if spyRedActive:
            $ redChestSet = 1
            $ redBottomSet = 1
            $ redChest = 1
            $ redBottom = 1
        elif True:
            pass


    $ samDailyChat = 0
    $ cloverDailyChat = 0
    $ alexDailyChat = 0


    $ dailyMagAgent = False


    $ dailyHerb = True


    if task4Stage >= 4 and task26Stage <= 1:
        $ coverCounter -= 2
    if coverCounter >= 100:
        $ coverCounter = 100
    if coverCounter <= 1:
        $ coverCounter = 1


    if skillRank >= 7 and coverCounter <= 24:
        $ coverCounter = 25


    if samMood <= 0:
        $ samMood = 0
    if cloverMood <= 0:
        $ cloverMood = 0
    if alexMood <= 0:
        $ alexMood = 0


    $ samMood += 2
    $ samMood += cellSamHappiness

    $ cloverMood += 2
    $ cloverMood += cellCloverHappiness

    $ alexMood += 2
    $ alexMood += cellAlexHappiness


    if skillRank >= 5:
        $ samMood += 1
        $ cloverMood += 1
        $ alexMood += 1

    if samMood > 100:
        $ samMood = 100
    if cloverMood > 100:
        $ cloverMood = 100
    if alexMood > 100:
        $ alexMood = 100



    if task4Stage >= 5:
        if samSupLvl == 1:
            $ nanoLevelSam += 8
            if nanoLevelSam >= 100:
                $ nanoLevelSam = 100
        elif samSupLvl == 2:
            $ nanoLevelSam += 4
            if nanoLevelSam >= 100:
                $ nanoLevelSam = 100
        elif samSupLvl == 3:
            $ nanoLevelSam += 0
            if nanoLevelSam >= 100:
                $ nanoLevelSam = 100

        if cloverSupLvl == 1:
            $ nanoLevelClover += 8
            if nanoLevelClover >= 100:
                $ nanoLevelClover = 100
        elif cloverSupLvl == 2:
            $ nanoLevelClover += 4
            if nanoLevelClover >= 100:
                $ nanoLevelClover = 100
        elif cloverSupLvl == 3:
            $ nanoLevelClover += 0
            if nanoLevelClover >= 100:
                $ nanoLevelClover = 100

        if alexSupLvl == 1:
            $ nanoLevelAlex += 8
            if nanoLevelAlex >= 100:
                $ nanoLevelAlex = 100
        elif alexSupLvl == 2:
            $ nanoLevelAlex += 4
            if nanoLevelAlex >= 100:
                $ nanoLevelAlex = 100
        elif alexSupLvl == 3:
            $ nanoLevelAlex += 0
            if nanoLevelAlex >= 100:
                $ nanoLevelAlex = 100



    if nanoLevelSam >= 100:
        $ nanoLevelSam = 100
    if nanoLevelSam <= 0:
        $ nanoLevelSam = 0
    if nanoLevelClover >= 100:
        $ nanoLevelClover = 100
    if nanoLevelClover <= 0:
        $ nanoLevelClover = 0
    if nanoLevelAlex >= 100:
        $ nanoLevelAlex = 100
    if nanoLevelAlex <= 0:
        $ nanoLevelAlex = 0



    if task3Stage == 3:
        $ spy1Status = 10
    if task6Stage == 8 or task6Stage == 10 or task6Stage == 11:
        $ spy1Status = 10
    if 1 <= task9Stage <= 3:
        $ spy2Status = 10
    if task16Stage == 1:
        $ spy1Status = 10
        $ spy2Status = 10
        $ spy3Status = 10
    if task26Stage == 4:
        $ spy1Status = 10
        $ spy2Status = 10
        $ spy3Status = 10




    $ daysPlayed += 1
    $ tod = 1
    $ landgrabTimer += 1
    if landgrabTimer >= 31:
        if landgrabTut2 == True and task3Stage >= 7 and daysPlayed <= 130:
            $ landgrabTut2 = False
            scene black with fade
            scene skipLandgrabTut with fade
            "The Landgrab is over. Remember that you can click the Agents button at the top of the screen to see how many days until the next Landgrab."
            "You will need to participate in Landgrabs to reveal the identity of gang leaders. New agents can be captured by using Hypno Earrings during missions."
        $ landgrabTimer = 1


    if task4Stage >= 4:
        $ randNotMission = renpy.random.randint(1,15)


    if daysPlayed == 5:
        jump nightCutscenes
    if specialMaggieStatus >= 3 and specialMuffyStatus >= 3 and specialDragonStatus >= 3 and nighttime2Event:
        jump nightCutscenes
    if specialMelodyStatus >= 3 and specialTaliaStatus >= 3 and specialFelicityStatus >= 3 and nighttime3Event:
        jump nightCutscenes
    if specialCandyStatus >= 3 and specialSebStatus >= 3 and specialKandStatus >= 3 and nighttime4Event:
        jump nightCutscenes
    if task7Stage == 2 and spyYellowActive:
        jump task7

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

    if task4Stage == 1:
        $ task4Timer += 1
    if task4Timer >= 5 and spyYellowActive == False:
        y "We really should visit the school and see what this meeting is all about."

    jump worldmap
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
