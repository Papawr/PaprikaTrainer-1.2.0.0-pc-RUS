default randMoney = 0
default randBikini = 0

label jobReport:

    hide scene_darkening
    if landgrabTimer == 31:
        $ landgrabTimer = 32
    if tutStage == 3:
        y "I can't just wait around until evening. It's my first day on the job afterall."
        call screen mapButtons
    if tutStage == 7 and spyGreenActive and greenDayJob == 0 or tutStage == 7 and spyRedActive and redDayJob == 0 or tutStage == 7 and spyYellowActive and yellowDayJob == 0:
        y "I should probably send my spy out to bring back some intel first."
        call screen mapButtons
    stop music fadeout 1.0
    if month == 10 and 14 <= day <= 31:
        play sound "audio/sfx/howl.mp3"
    elif month == 12 and 14 <= day <= 31:
        play sound "audio/sfx/bells.mp3"
    elif True:
        play sound "audio/sfx/owl.mp3"
    scene bgMapNight:
        zoom 0.5
    with d10
    play music "audio/music/nighttime.mp3" fadein 1.5
    $ tod = 2
    pause 0.3
    if month == 10 and 14 <= day <= 31:
        scene bgBaseHalloween with fade
    elif month == 12 and 14 <= day <= 31:
        scene bgBaseChristmas with fade
    elif True:
        scene bgBase with fade

    if tutStage == 7:
        jump tutStage8


    if decorationStyle == 1:
        $ acesRep += 1
    elif decorationStyle == 2:
        $ punkRep += 1
    elif decorationStyle == 3:
        $ outsideRep += 1



    if playerMilkshake == True:
        $ playerMilkshake = False
        $ playerMilkshakeMoney = renpy.random.randint(10, 20)
        if playerMilkshakeLvl >= 2:
            $ playerMilkshakeMoney += 5
        if playerMilkshakeLvl >= 3:
            $ playerMilkshakeMoney += 10
        if playerMilkshakeLvl >= 4:
            $ playerMilkshakeMoney += 15
        if playerMilkshakeLvl >= 5:
            $ playerMilkshakeMoney += 20
        if playerMilkshakeLvl >= 6:
            $ playerMilkshakeMoney += 25
        $ exoticPrice = 10 * exoticMilk
        $ randMoney = playerMilkshakeMoney + exoticPrice
        $ cash += randMoney
        "Today you made $ [randMoney] selling milkshakes."
        call missionRewardMoney from _call_missionRewardMoney_75



    label nextReport:
        pass


    $ randRap = renpy.random.randint(1, 5)


    $ randIntel = renpy.random.randint(20, 35)
    if landgrabTimer == 31:
        $ randIntel += 25


    $ moneyChanceReward = renpy.random.randint(1, 2)
    if moneyChanceReward == 2:
        $ randMoney = renpy.random.randint(5, 20)
    if landgrabTimer == 31:
        $ randMoney += 150


    $ loreChanceReward = renpy.random.randint(1, 10)




    default repGain = 0
    $ repGain = 0
    $ repGain += 1
    if greenDayJob == 1:
        $ repGain += 2
        $ repGain += repGreenOutfitAces
    if redDayJob == 1:
        $ repGain += repRedOutfitAces
    if yellowDayJob == 1:
        $ coverCounter += 2
        $ repGain += repYellowOutfitAces


    default injectChanceReward = renpy.random.randint(1,8)





    if month == 10 and 14 <= day <= 31 and greenDayJob >= 1:
        $ randTreat = renpy.random.randint(1,4)
        if randTreat == 1:
            $ randTreat = 0
            $ treatBag += 1
            "Sam brought home a Trick or Treat bag today. Check your ITEMS to see what's inside!"
        elif True:
            pass


    if task19Stage == 1 and greenDayJob == 1:
        jump task19
    if task19Stage == 2 and greenDayJob == 1:
        jump task19
    if task19Stage == 3 and greenDayJob == 1:
        jump task19
    if task6Stage == 1 or task6Stage == 5 or task6Stage == 7 or task6Stage == 8 or task6Stage == 10 or task6Stage == 11:
        jump task6
    if greenDayJob == 1:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ greenDayJob = 0
        $ acesRep += 3
        $ spy1Status = 0
        s "I'm back from working with the Aces."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Sam was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Here's my report."


        call missionRewardRep from _call_missionRewardRep_2


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_1


        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_2


        if loreChanceReward == 10:
            $ acesLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore


        if injectChanceReward >= 7:
            $ injectorSmall += 1
            call missionRewardItem from _call_missionRewardItem_12
            $ injectChanceReward = 0


        $ randBounty = renpy.random.randint(99,99)

        menu:
            "{color=#EFD66D}Hacking Codes{/color}" if acesBounty1 == 2:
                $ acesBounty1 = 0
                y "So how did it go?"
                s g1 "Good, I gave them the codes. Their bank accounts should be safe now."
                $ randMoney = renpy.random.randint(170, 250)
                $ cash += randMoney
                call missionRewardMoney from _call_missionRewardMoney_94
                y "Not bad, well done [samNick]."
            "{color=#EFD66D}Spray Cans{/color}" if acesBounty2 == 2:
                $ acesBounty2 = 0
                y "So how did it go?"
                s g1 "Good, we got rid of the spray cans. At least for now."
                $ randMoney = renpy.random.randint(170, 250)
                $ cash += randMoney
                call missionRewardMoney from _call_missionRewardMoney_95
                y "Not bad, well done [samNick]."
            "{color=#EFD66D}Test Answers{/color}" if acesBounty3 == 2:
                $ acesBounty3 = 0
                y "So how did it go?"
                s g1 "Good, I traded her the test answers and got this out of it."
                $ randMoney = renpy.random.randint(170, 250)
                $ cash += randMoney
                call missionRewardMoney from _call_missionRewardMoney_69
                y "Not bad, well done [samNick]."
                s g19 "I feel a little bad in having helped her cheating though..."
            "{color=#EFD66D}Bounty{/color}" if randBounty <= 3 and acesBounty3 == 0 and gadgetHackActive:
                s "So I overheard the Aces talking today..."
                if randBounty == 1 and missionAreaDatabaseActive:
                    $ acesBounty1 = 1
                    s "Drift Punk keeps hacking Aces bank accounts, and they're getting really sick of it."
                    s "Apperantly they're hiding the hacking software somewhere in Punk Web."
                    s "We should keep an eye out for it during our next Punk Web mission."
                elif randBounty == 2 and missionAreaFaireActive:
                    $ acesBounty2 = 1
                    s "Apperantly they're getting real sick of the Outsiders. Last night they came around and spraypainted a fleet of expensive cars."
                    s "If we end up going to the abandoned amusement park, we should try stealing those spray cans. They Aces are willing to reward us for it."
                elif True:
                    $ acesBounty3 = 1
                    s "One of the girls was threatened by her parents that if her grades didn't improve, she'd be cut off."
                    s "Ofcourse in true gangster fashion... instead of studying, she wants us to steal the anwser sheet from the school."
                    s "We should keep an eye out during our next mission to the school. She's willing to pay a pretty penny for it."
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Sam doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if acesRank <= 1:
                        if randRap == 1:
                            s g28 "Working with the Aces is... {i}'challenging'{/i}. I've never seen anyone spent money so frivolously. I saw someone buy sneakers for a thousand dollars today. Sneakers!"
                            s "The ones that are probably made in a sweat shop for 15 bucks."
                            y "When you can no longer impress others with your money, you gotta step it up."
                            y "People buy all kinds of overpriced shit. Art, clothing, furniture. Just to impress."
                            s g10 "I know, but it's still a little frustrating to watch."
                            s "Later on, I held the door open for one of them and he gave me this..."
                            $ randMoney = 10
                            $ cash += 10
                            call missionRewardMoney from _call_missionRewardMoney_43
                            y "Just for holding the door open?"
                            s "Yup. Money is money, right?"
                            y "I'm not complaining."
                        if randRap == 2:
                            s g12 "Another day another bucked of money wasted."
                            y "That bad?"
                            s "It's like throwing around candy for them. The money just keeps coming and never runs out."
                            s "I saw someone buy a sportscar, and I asked him if he had to take it easy with spending for a while now. He just laughed and showed me his bank account."
                            s g39 "The time it took him to buy the car, he already made it all back. He could have given it to people in need!"
                            y "......................"
                            y "Not gonna lie. I'm so jealous right now."
                            s g15 "Yeah me too...."
                            s "I managed to overhear some things though. So I gathered a bit more intel."
                            $ randIntel = 25
                            $ intel += 25
                            call missionRewardInt from _call_missionRewardInt_18
                        if randRap == 3:
                            s g9 "Argh! I'm so angry right now!"
                            y "You always profess to the world how you feel?"
                            s g40 "Sorry... It's just that the Aces went to a charity event today..."
                            y "Charity? They don't seem the type..."
                            s g8 "It was mostly a PR stunt. Together they donated ten-thousand dollars!"
                            y "Woah, not bad!"
                            s g28 "No, you don't understand! I saw a guy spent ten-thousand on clothes yesterday!"
                            s g31 "They don't care about the charity! That donation was pocket change for them! I've seen them spent that much on drugs!"
                            y "Well at least it's still money that goes to charity."
                            s g33 "I know... it's something at least... but... it still irks me to see someone so rich basically throwing his loose change to the impoverished masses..."
                            y "Very poetic. All right you're dismissed. Don't let it get to you."
                        if randRap == 4:
                            y "And? How much money was wasted today?"
                            s g37 "{b}*Scoffs*{/b} Do you really need to ask?{w} We went almost the entire day without spending a dime and then came across a street art store."
                            s "One of the guys bought the artists full inventory on the spot... And then threatened him that if he ever made art again, he'd kill him."
                            y "I'm confused..."
                            s g34 "He wanted to own the whole collection, just so no one else could have his work. It was just him flexing on is friends..."
                            y "Seems like a great guy..."
                            s g37 "Yeah..."
                        if randRap == 5:
                            s g43 "{b}*Mutters*{/b}"
                            y "Uh oh. What happened today?"
                            s "Something petty. It annoys me that I'm letting it get to me."
                            s "There was a really cute dress that I wanted and one of the Aces offered to buy it for me."
                            y "Well that's nice of them."
                            s g38 "But before she could, another gangmember declared that the shop was 'so not fashionable'. And suddenly no one was interested in the clothes anymore."
                            s "I had to play along of course and we end up not getting the dress..."
                            y "But you secretly still wanted it."
                            s g19 "Yeah..."
                    if acesRank == 2:
                        if randRap == 1:
                            s g9 "They are so insufferable! I thought I'd take all my saving out of the bank so I could impress them, but they just laughed!"
                            y "Laughed?"
                            s g40 "Yeah... something about them having so much money that they could no longer carry all of it... Me carrying cash was a sign of poverty!"
                            y "Maybe they can tell that you're trying too hard."
                            s g15 "{b}*Sighs*{/b} Maybe. I returned it all to the bank... hopefully before my parents find out. "
                            s "So I didn't impress anyone today..."
                            y "Better luck next time."
                        if randRap == 2:
                            s g41 "Did you know that the majority of the world's gold reserves are in the hands of Indian women?"
                            y ".........."
                            y "What?"
                            s g14 "It's because of the dowery when they get married. If Indian households put all their gold together, they'd have even more than the United States."
                            y "Facinating... What brought this up?"
                            s g37 "Oh... the Aces held up a jewelry store today and they refused to take anything that was worth less than gold."
                            s "They actually look at silver with disdain..."
                            s "I mean, it's not worth that much in comparison to gold, but I still think it can look nice."
                            y "{i}'Speech is siver, silence is gold.'{/i}"
                            s g1 "Yeah exactly! .... Wait was that a hint for me to be quiet?"
                        if randRap == 3:
                            s g16 "Do you know what music artists are popular at the moment?"
                            y "I'm probably the last person you should ask that. Why?"
                            s g37 "Well the Aces are bragging about popular musicians showing up at their parties and I didn't recognise any of them."
                            s "I'm afraid that I might be out of touch."
                            y "You're a bookworm who spends all her time saving the world or studying. I don't think you were ever in touch to begin with."
                            s g10 "Harsh... I'll look it up online. Before I blow my cover."
                        if randRap == 4:
                            s g38 "Today got pretty bad. We had to fight a rival gang and things got hairy."
                            y "Oh! Were you hurt?"
                            s g3 "Nah, I can take most of these guys on blindfolded, but I didn't want to blow my cover."
                            s "I ended up disarming a gangmember who almost killed one of the Aces. We managed to scare them off afterwards. Luckily nobody was seriously hurt."
                            s "Afterwards we went for a drink and they clued me in on some extra stuff."
                            $ randIntel = 20
                            $ intel += 20
                            call missionRewardInt from _call_missionRewardInt_17
                        if randRap == 5:
                            s g28 "This is crazy..."
                            s "They eat icecream covered in gold! GOLD!"
                            y "What are you talking about?"
                            s "We went to this fancy restaurant and afterwards they ordered icecream covered in a thin layer of gold. It was insane!"
                            s g11 "Of course I just got to tag along as a bodyguard, so I didn't get to try any, but I'm not sure if I'd enjoy it..."
                            s "I don't know... maybe I just don't understand rich people..."
                    if acesRank == 3:
                        if randRap == 1:
                            s g1 "The Aces actually did something good for once today."
                            y "They did?"
                            s "Yeah, they pranked a homeless guy."
                            y "That doesn't... sound very good."
                            s g29 "No hear me out. They got a lottery ticket and pretended that the ticket had won a cash amount."
                            s "They took him to a shop and the shopkeeper who was in on it handed him 1000 dollars!"
                            y "That's surprisingly kind of the Aces..."
                            s g1 "Yeah... I guess they're not all bad guys."
                        if randRap == 2:
                            s g1 "You know what? I think I'm getting used to all the spending they do."
                            s g2 "I mean sure, it's a lot of money, but after you've bought your 4th sports car, it sorta blends together."
                            y "If you say so. Are they paying you yet?"
                            s g12 "Well... not as much as I hoped..."
                            s "I got to keep up appearances in the gang. You wouldn't so happen to have a spare ten-grand lying around, do you?"
                            if cash >= 10000:
                                y "Yes, but you're not getting it."
                            elif True:
                                y "............................"
                            s "Never mind...."
                        if randRap == 3:
                            s g1 "Today I went on a spending spree."
                            y "You did?"
                            s "Yeah, one of the gangleaders wanted something new and gave me their creditcard."
                            s "I could spent it on whatever I wanted."
                            y "But not for yourself, I take it?"
                            s g10 "Pfff no, I wish."
                            y "Going undercover with the Aces sure isn't the cashcow I hope'd it be."
                        if randRap == 4:
                            s g38 "Today was rough. A lot of fighting. Some people were injured, but no casualties thankfully."
                            s "One of the members brought a gaudy gold plated pistol that he wanted to try out."
                            s g22 "It was trashed during the fight and he was {b}pissed{/b}!"
                            y "........................"
                            s "Well that's what you get I guess."
                        if randRap == 5:
                            s g1 "Today wasn't half bad, I even got a tip!"
                            y "A tip?"
                            s "Yeah, you know how I've been doing a lot of fighting and not making any money?"
                            s "Well today I helped move some guy's stuff and he handed me this."
                            $ randMoney = 50
                            $ cash += 50
                            call missionRewardMoney from _call_missionRewardMoney_44
                            y "Just for helping him move some things?"
                            s g35 "{b}*Shrugs*{/b} I didn't question it. Apperantly moving a couch is worth more to them than risking your life."
                    if acesRank == 4:
                        if randRap == 1:
                            s g1 "Today went great! I got a bonus for all the hard work I did!"
                            y "Gangs give out bonuses now?"
                            s "It seems so. Here's the extra money I earned."
                            $ randMoney = 100
                            $ cash += 100
                            call missionRewardMoney from _call_missionRewardMoney_45
                            y "Looks like you're finally beginning to fit in."
                            s "That's what I was thinking. I'm a lot more at ease and they're a lot nicer to me."
                            s g45 "Too bad I'm not that rich..."
                        if randRap == 2:
                            s g39 "It got dangerous today. We were ambushes by a rival gang and had to pull back. I was left behind as a distraction."
                            y "Sounds like you were sacrificed so the others could make a get-a-way."
                            s g29 "N-no they wouldn't do that. I met up with them again later and they were happy to see me."
                            s g1 "It's amazing we got out of that one unscathed."
                            y "In the future, be more careful. I don't want you ending up as their sacrificial lamb for the slaughter."
                            s "They don't see me like that! I'm finally becoming one of them."
                            y "Well all right, but be careful."
                        if randRap == 3:
                            s g19 "Hey [playerName], I have a request for you."
                            y "A request?"
                            s "Now before you say no, please hear me out."
                            y "............................"
                            s "The gang's been looking at this one yacht~..."
                            y "No."
                            s g29 "But image how much I'd impress them if I had one!"
                            s "WOOHP has a few yachts already, we could write this off as a business expense."
                            y "No."
                            s "But [playerName]...!"
                            y "Nooooooo."
                        if randRap == 4:
                            s g1 "Man, I'm so glad I actually got to go undercover with the Aces."
                            y "You are?"
                            s g2 "Of all the gangs out there, they're probably the best. They donate to charity and I've seen them help out people a number of times."
                            y "What about all the violence, theft and drugs?"
                            s g12 "Well I mean... those are bad, but all the gangs have those. I'm not saying they're the good guys, but they're not all bad either."
                            s g28 "Oh and the food! They usually bring me along to eat and it's always to these super expensive restaurants. The food is amazing!"
                            s "Oh! Oh! And they've got gadgets!"
                            y "We have gadgets..."
                            s "Yeah, but they've got rich people gadgets! Like a watch that has a pin in it, and when you pull out the pin a helicopter flies out to come pick you up."
                            y "...................."
                        if randRap == 5:
                            s g29 "They are so crazy sometimes."
                            s "This one girl has a crush on a guy who likes video games. To try and get into them, she bought a game system."
                            s "Afterwards she spend thousands of dollars on games. She picked one up, said she didn't like it and gave up."
                            y "What about all the video games...?"
                            s g14 "Probably gathering dust."
                            if punkRep >= 3:
                                y "Don't let Clover find out."
                            elif True:
                                y "What a waste...!"
                            s g1 "Still, willing to spend all that, just to get to know your crush's hobbies. That's pretty romantic."
                            y "......................"
            "Dismissed" if True:
                pass
        hide green
        hide scene_darkening
        with d2
        jump nextReport



    if greenDayJob == 2:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ greenDayJob = 0
        $ punkRep += 1
        $ spy1Status = 0
        s "I'm back from working with the Drift Punks."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Sam was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Here's my report."


        call missionRewardRep from _call_missionRewardRep_3


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_3
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_7
        if loreChanceReward == 10:
            $ punkLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_1

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Sam doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if punkRank <= 1:
                        if randRap == 1:
                            s g13 "As expected, today went really well."
                            s "They were having some trouble with their code, so I spend all day figuring out what could be the problem. In the end, I managed to fix it!"
                            s "I mean... sure it took a couple of hours, but I did it!"
                            s g11 "Not sure how I feel about writing hacking software though..."
                        if randRap == 2:
                            s g11 "All in all, not that bad of a day."
                            s "..........................."
                            y "What?"
                            s "I er..."
                            s g12 "Had to clean the toilets."
                            s g29 "Not that there's anything wrong with that! I just... erm... it wasn't what I expected really."
                        if randRap == 3:
                            s g1 "I think Drift Punk really are my people. They enjoy music, intelligent conversation, discussing politics."
                            s g13 "I mean... obviously they're wrong about all of these things, but it's good to have a dialogue!"
                            y "..................."
                        if randRap == 4:
                            s g38 "We actually got into a fight today. A bunch of cavemen from the Outsiders."
                            s "They smashed a music station we spent all day setting up. They got scared away when our armed response unit arrived, so luckily nobody got badly hurt."
                            y "Drift Punk has a armed response unit?"
                            s g29 "Yeah, these guys are like an army! It's crazy. They're probably the biggest thread to WOOHP as well. They've got hightech gadgets, state of the art equipment and more."
                            y "All right we'll have to keep an eye on them. Head back to your cell for now."
                        if randRap == 5:
                            s g10 "We er... hacked a bank today. And..."
                            s "We stole a 'lot' of money."
                            y "Impressive."
                            s g11 "Yeah... the money has to be launderd first, so we didn't get any of it yet of course. It's sorta funny how Drift Punk is planning much larger heists than the other gangs, yet it's all done from behind a computer screen."
                    if punkRank >= 2:
                        if randRap == 1:
                            s g17 "You think modern art, is art. Right?"
                            y "Er...."
                            s g38 "I had this big argument with one of the Drift Punks who said only classical art is art and modern is just an ugly mess!"
                            s "I tried explaining to him how wrong he was, but he just brushed it off!"
                            y "Different strokes for different folks."
                            s "{b}*Hmpf*~{/b}..."
                        if randRap == 2:
                            s g38 "I'm starting to change my opinion of Drift Punk..."
                            y "Yeah?"
                            s g39 "They're experimenting with different types of weapons and... well it gets scary."
                            s "Their scientists are driven purely by logic and any ethics are out of the window..."
                            s "Biologic warfare, gas based toxins, microwave technology."
                            y "That sounds... bad."
                            s g12 "It is. Luckily they're being held in check by the gang's leadership, but I'm amazed that these normal people can be researching something as bad as this."
                        if randRap == 3:
                            s g39 "We got into a fight today. Like... a real fight. Guns and all."
                            y "Uh oh..."
                            s g12 "Yeah it got pretty nasty, but the Drift Punk tried out their less-than-lethal weapons and they were... surprisingly effective."
                            s "We got a scrap here or there, but in the end nobody was killed and we got real quick control over the situation."
                            s "I'm just a little worried about how ruthless and effective they were."
                            y "We'll have to keep an eye on the gang for sure."
                        if randRap == 4:
                            s g1 "Making it rain...!"
                            y "What the...?"
                            $ randMoney = 50
                            $ cash += 50
                            call missionRewardMoney from _call_missionRewardMoney_46
                            y "Where you get this?"
                            s "From the Punks. Everyone got some extra cash to spend on gas for their cars, but seeing as I don't have one so I just got us some extra money."
                        if randRap == 5:
                            s g15 "Ow ow ow~..."
                            y "Sam? Are you hurt?!"
                            s "No... just a headache. I've been fine-tuning speakers for a party tonight and it was loud!"
                            s "My ears are still ringing."
                            y "A party? Don't you wanna go?"
                            s g1 "Oh, no that's all right. I'm not a big party person. I'd rather curl up with a book."
                            y "Why am I not surprised..."
            "Dismissed" if True:
                pass
        hide green
        hide scene_darkening
        with d2
        jump nextReport



    if greenDayJob == 3:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ greenDayJob = 0
        $ outsideRep += 1
        $ spy1Status = 0
        s "I'm back from working with the Outsiders."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Sam was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Here's my report."


        call missionRewardRep from _call_missionRewardRep_4


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_5
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_9
        if loreChanceReward == 10:
            $ outsidersLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_2

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Sam doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if outsideRank <= 1:
                        if randRap == 1:
                            s "The Outsiders are a little rough around the edges, but some of them are good kids."
                            s "Once this whole situation blows over, I think we can get some of them on the straight and narrow."
                            y "I want to believe that, but right now they should be treated as dangerous gangsters, not poor misunderstood kids."
                            s "Yeah you're right."
                        if randRap == 2:
                            s "I got talking to one of the street artists today. He actually took a lot of inspiration from an artist I really like."
                            y "Really?"
                            s "I always sorta saw street art as just... funny scribbles. I never paid much attention to it, but some of these guys really know what they're doing."
                            s "He promised to make me a print sometime and love to have it."
                        if randRap == 3:
                            s "There's some fierce fightings in the Outsiders."
                            s "Some of them have sworn off guns, believing they can only cause harm. Instead they fight with their fists."
                            s "We were attacked by a rival gang today and I saw them beat up an armed guy with their bare hands."
                            s "When he ran away he dropped his gun and they didn't even bother looking at it. I guess there's still some hope for these kids."
                        if randRap == 4:
                            s "With so many people from so many walks of life, there's bound to be trouble..."
                            s "Some of the goth kids got into an argument with the punkers today. It came to blows, but nobody was seriously hurt."
                            y "What was the argument about?"
                            s "Not sure, but they seemed quite resentful of eachother afterwards."
                        if randRap == 5:
                            s "I'm no good on a skateboard, but I used to love using skates when I was younger."
                            s "They allowed me to borrow some and we went racing. I wasn't half bad if I do say so myself."
                            y "Yeah? What place did you come in?"
                            s ".............."
                            s "Okay I don't want to talk about this anymore now."
                    elif outsideRank >= 2:
                        if randRap == 1:
                            s "They can get rough... I mean... Their hearts are in the right place most of the times, but they're just so extreme."
                            s "We saw some Aces ganging up on an Outsider, beating him up in the streets, so of course we ran in to help."
                            s "We managed to overpower them pretty easily, but the Outsiders just kept punching and kicking them... Even after they stopped moving."
                            s "I checked their pulse before leaving and they survived, but they could've easily killed them."
                        if randRap == 2:
                            s "The Outsiders can sometimes be incredibly immature."
                            s "They scratched a fancy looking car, just to upset the owner. {i}'Serves him right for being so rich.'{/i}"
                            s "For all their talks about equality, they sure seem to only think about 'their' vision of equality and not so much everyone else's."
                        if randRap == 3:
                            s "I actually made some money today."
                            y "You did?"
                            s "Yeah, I got my hands on some spraycans and did some street art."
                            s "One of the Outsiders really liked it and paid me $50 bucks for it."
                            $ cash += 50
                            $ randMoney = 50
                            call missionRewardMoney from _call_missionRewardMoney_47
                            y "Hey, every little bit helps."
                        if randRap == 4:
                            s "Down with the government!"
                            y "Wow... That's probably the least convincing protest yell I've ever heard."
                            s "{b}*Sighs*{/b} I've never been one to stir up the ranks. I actually 'like' our government."
                            y "Well you gotta be more convincing if you wanna pull that off."
                            s "I know..."
                        if randRap == 5:
                            s "More guns."
                            y "What?"
                            s "The Outsiders brought in another shipment of weapons today. It's getting out of control."
                            s "Soon everyone in Beverly Hills and their dog will have a firearm."
                            y "It's their number one import. It's how they make their money."
                            s "Yeah, but we gotta gain control of it soon."
            "Dismissed" if True:
                pass
        hide green
        hide scene_darkening
        with d2
        jump nextReport


    if greenDayJob == 99:
        $ greenDayJob = 0
        $ spy1Status = 0
        $ greenChest = 0
        $ greenBottom = 0
        $ greenNeck = 0
        $ greenHat = 0
        $ greenShoes = 0
        if under4Sam:
            $ greenUnder = 4
        elif True:
            $ greenUnder = 6
        show green g1 at ri with d3
        s "I'm back from Mathias' place."
        if gadgetJetpackActive == True:

            $ randMoney = renpy.random.randint(25, 40)
            $ cash += randMoney
            call missionRewardMoney from _call_missionRewardMoney_48
            hide green with d3
        elif task2Stage == 12.6:
            $ hackProgress = 100
            $ task2Stage = 13
            s g11 "........................"
            y "Well, how was it?"
            s g12 "I guess it wasn't {i}that{/i} bad."
            s "Mathias seemed surprise when I showed up. Apperantly he didn't think you were serious when you promised him a bikini model."
            y "I like to stick to my word......{w} sometimes."
            y "So how did his research go?"
            s g34 "Good actually. I ended up serving him soda's and chips in my bikini and he was more than happy to 'repay the favor'. So to speak."
            s "Anyways, he said that he had a breakthrough and that you should visit him tomorrow."
            y "I might just do that! Well done, Sam."
            s g37 "I... didn't actually do much, but thanks I guess."
            s "Not looking forward to doing it more often."
            hide green with d3
        elif True:
            y "How did it go?"
            $ randMathias = renpy.random.randint(1,3)
            if randMathias == 1:
                $ hackProgress += 5
                s g37 "It went as well as you'd expect. He has more attention for the girl wearing a bikini than for the work he's suppose to do."
                y "..............."
            if randMathias == 2:
                $ hackProgress += 9
                s g34 "Pretty average day. He moved some stuff off his agenda to work on hacking the WOOHP database. I'd say we made some progress."
                y "That's good to hear."
            if randMathias == 3:
                $ hackProgress += 15
                s g34 "Today went really well. He suddenly had a breakthrough when he was...."
                s g37 "......................"
                s "When he was staring at my breasts~....{w} And he suddenly lost all interest in me and started working on his computer."
                s "He made great progress on his research today."
                y "Now that's what I wanted to hear!"
            hide green with d3



    if greenDayJob == 4:
        $ spy1Status = 0
        if clubStage <= 3:
            $ greenDayJob = 0
            $ clubStage += 1
            "Sam spent the day cleaning the milkshake bar and headed back to her cell."
            if clubStage >= 4:
                scene bgClub1
                with fade
                jump tutStage9
        elif True:

            if greenDayJob == 4:
                $ greenDayJob = 0
                call undressSam from _call_undressSam_29
                $ greenChest = 2.1
                $ greenBottom = 2.1
                $ greenShoes = 2
                $ greenHat = 2
                show scene_darkening with d3
                show green g1 at ri with d3
                s "I'm back from working at the milkshake bar."

                $ randMoney = renpy.random.randint(35, 50)

                if checkMark1 == True:
                    $ randMoney += 50
                if checkMark2 == True:
                    $ randMoney += 60
                if checkMark3 == True:
                    $ randMoney += 70
                if checkMark4 == True:
                    $ randMoney += 80
                if checkMark5 == True:
                    $ randMoney += 90
                if checkMark6 == True:
                    $ randMoney += 100

                $ randPenalty = renpy.random.randint(1, 3)
                if randPenalty == 3:
                    if 80 <= nanoLevelSam <= 100:
                        $ randMoney = randMoney / 2
                        "There seems to be some money missing..."
                    if 60 <= nanoLevelSam <= 79:
                        $ randMoney -= randMoney / 3
                        "There seems to be some money missing..."
                    if 40 <= nanoLevelSam <= 59:
                        $ randMoney -= randMoney / 4
                        "There seems to be some money missing..."

                $ cash += randMoney
                call missionRewardMoney from _call_missionRewardMoney_3
                pause 0.2

            menu:
                "Tell me about your day" if True:
                    if slutLevel <= 1:
                        if randRap == 1:
                            s g11 "Not gonna lie... this place is kind of dead."
                            y "We haven't been open for long yet. People will come."
                            y "Afterall, who wouldn't want to see you in that cute waitress uniform~..."
                            s g9 "I prefer noone did...!"
                        elif randRap == 2:
                            s g38 "We should restock on milk."
                            y "Milk?"
                            s "Yeah, we {i}'are'{/i} a milkshake bar after all."
                            y "No, we're a tittie place that pretends to be a milkshake bar."
                            s g10 "Call it what you want. We still get a lot of orders for milkshakes."
                        elif randRap == 3:
                            s g9 "Customers are ogling me while I serve them..."
                            y "Great!"
                            s g29 "G-great...?! It's demeaning!"
                            y "But you get bigger tips, right?"
                            s g11 "................"
                            y "Right?"
                            s g12 "{b}*Sighs*{/b} Yeah..."
                            $ randMoney = 15
                            $ cash += randMoney
                            call missionRewardMoney from _call_missionRewardMoney_4
                        elif randRap == 4:
                            s g9 "Ngh... I don't like this uniform..."
                            y "What's wrong with it?"
                            s g38 "The shorts keep sliding up my butt. I'm looking like a damn stripper."
                            y "I still don't see what the problem is here."
                            s g39 "{b}*Annoyed Mutter*{/b}"
                        elif randRap == 5:
                            s g8 "A customer tried to slap my butt today!"
                            y "Without paying?!"
                            s g17 "What do you mean {i}'Without paying'{/i}?! I'm not getting my butt slapped for money!"
                            y "You do it for free? Wow, kinky Sam."
                            s g39 "{b}*Groans*{/b}"
                    if slutLevel == 2:
                        if randRap == 1:
                            s g43 "I tried being a little more sexy today~..."
                            y "Let me guess...{w} total disaster."
                            s g31 "Hey! I'll have you know that I did very well, thank you!"
                            s g12 "I figured... if we're letting you watch us masturbate... Then I guess being a little sexy at the bar won't hurt either."
                            y "I'm glad you're taking your job more serious!"
                            s g33 "I always take my job serious...{w} B-but maybe I was a little unsure on how to be sexy..."
                        elif randRap == 2:
                            s g38 "We should post a sign outside that says 'no guns allowed'."
                            s g12 "A bunch of Outsider thugs came in, showing off how {i}'bad'{/i} they were."
                            s "They wouldn't be stupid enough to try anything on neutral ground, but I'm still not comfortable around firearms when they're in the hands of these morans."
                        elif randRap == 3:
                            s g1 "..................."
                            y ".......?"
                            y "What?"
                            s g2 "Notice anything... different about me?"
                            y "Different...?"
                            "Voice" "Oh no, it's a trap! Its her hair! No wait... maybe she got her nails done! No wait, maybe she's using a new shampoo...!"
                            y "(She looks exactly the same as always! What do I do?!)"
                            "Voice" "Abort! Abort!"
                            y "ABORT!"
                            s g29 "W-what...?!"
                            hide green with d1
                            pause 0.5
                            "You ran away..."
                        elif randRap == 4:
                            s g14 "Another day another lousy till."
                            y "Still not making money?"
                            s g12 "It's not as bad as before. Ever since the girls starting spicing things up a little bit more the amount of customers has increased."
                            s "However... we won't be buying a pent house downtown anytime soon."
                            y "We'll get there. Also since when did you want a pent house in Beverly Hills?"
                            s g41 "I mean... who doesn't?"
                            y "Good point."
                        elif randRap == 5:
                            hide green
                            $ greenChest = 99
                            show green g39 at ri with d3
                            y "Sam...? Where's your top?"
                            s ".................."
                            y "Er... I can see you-..."
                            s g40 "Tits! Yes, I know!"
                            s "Some asshole customer spilled his drink on me. I changed out into this and he did it again!"
                            y "He did it on purpose."
                            s g32 "Yep... So now I have two shirts that need to go in the wash."
                    if slutLevel == 3:
                        if randRap == 1:
                            s g33 "A customer got handsy again today."
                            y "Did you kick him out?"
                            s "No..."
                            s g45 "I.. sorta let him and in return he gave me a big tip. Here..."
                            $ randMoney = 30
                            $ cash += randMoney
                            call missionRewardMoney from _call_missionRewardMoney_5
                            s g43 "............"
                            s "In the future... should I allow people to grope me more? I mean... the tips are nice."
                            menu:
                                "Encourage sluttiness" if True:
                                    $ slutPublic += 1
                                    y "Oh hell yeah. Imagine how much money we can make if you get your melons squeezed every now and then."
                                    s g45 "That's true, but..."
                                    y "And you've got a peach worth slapping!"
                                    $ greenBlush = 1
                                    s g48 "W-Well...."
                                    y "And a pear shaped figure nobody could say no to!"
                                    s g1 "That's... a lot of fruit analogies..."
                                    y "I'm hungry, gimmi a break."
                                "Discourage sluttiness" if True:
                                    y "If you know they pay well, maybe. But in general I would discourage it."
                                    y "Don't want all those filthy hands on my slave girls!"
                                    s g3 "We're not slave girls..."
                                    y "Yet~...."
                                    s "Keep your sexual fantasies to yourself, [playerName]."
                        elif randRap == 2:
                            s g11 "Maybe we should stop selling alcohol in this place. It is a milkshake bar after all."
                            y "Yeah good idea. Maybe bring the wife and kids while you're at it."
                            s g10 "..................."
                            y "It's a tittie bar Sam. People come here for beer and well endowed women."
                            s "Fine..."
                        elif randRap == 3:
                            s g43 ".............."
                            y "Yeees...?"
                            s g45 "There was this one guy... right?"
                            s "He said he was going back to school..."
                            y "Okay~..."
                            s "Said he was going to study interior designing."
                            s "And then asked if he could practise redesigning my interiors."
                            y "{b}*Snicker*{/b}"
                            s g29 "It was a sex thing, wasn't it!? I knew it! All the other guys were laughing aswell!"
                            s "I don't get it! How does redesigning my inte-...."
                            $ greenBlush = 1
                            s g30 ".....!"
                            y "Now she gets it~...."
                            s g40 "I'm going back to my cell!!"
                            "Sam storms off."
                        elif randRap == 4:
                            s g1 "Hey [playerName]. I added hot wings to the menu. Customers were asking for them."
                            y "Goo-... wait... we didn't serve hotwings yet?"
                            s g11 "No... we just kinda serve crap. No wonder people aren't visiting."
                            y "Well... the food is probably not the reason why they're visiting~..."
                            s g1 "Yeah well... I like hot wings too, so now everyone's happy."
                        elif randRap == 5:
                            s g42 "[playerName] we have to do something about the slippery floor in the kitchen."
                            s "I almost slipped twice now and it's causing me to spill drinks on myself."
                            y "................"
                            s g10 "[playerName]... I'd rather go ahead and spill these drinks on myself voluntarily, than risk breaking my neck."
                            y "Okay fair enough. I'll see what I can do."
                    if slutLevel == 4:
                        if randRap == 1:
                            s g3 "So... I tried something new today~..."
                            s g22 "I erm... danced."
                            y "Danced?"
                            s "Heh yeah... I got up on the bar and put on a show to the patrons."
                            if slutPublic >= 5:
                                s g48 "And I er... took my top off..{w} and my bottom...."
                                y "You gave a strip show."
                                s g28 "It was so sexy! Getting naked in front of a crowd of people as they cheered and hollered!"
                                if hiredStaff >= 1:
                                    s g48 "Then some of the staff joined in aswell~.... ♥"
                                s "Basicaly we gave a stripshow in broad daylight."
                            y "Made any tips?"
                            s g1 "I sure did! Here..."
                            $ randMoney = 30
                            if slutPublic >= 5:
                                $ randMoney = 120
                            $ cash += randMoney
                            call missionRewardMoney from _call_missionRewardMoney_13
                            y "Nice. You should do this more often."
                            s g48 "Heh~... maybe..."
                        if randRap == 2:
                            s g14 "Had some guy grope me again today."
                            s "And... I sorta let him."
                            y "You didn't get upset?"
                            s g15 "{b}*Sighs*{/b} What is there to get upset about really?"
                            s "It makes the customers happy and I don't really mind anymore."
                            y "What changed?"
                            s g41 "Getting fucked by my boss."
                            y "{b}*Grin*{/b} Oh right."
                        if randRap == 3:
                            s g10 "Here."
                            y "What's this?"
                            s "The laundry bill for having our uniforms cleaned... daily."
                            y "Daily?!"
                            s g18 "I think you underestimate how {i}'clumsy'{/i} the customers can be with their drinks."
                            y "............."
                            y "Let's just take this bill and hide it somewhere~... I'm sure Jerry will pick up the tab once he gets his company back."
                        if randRap == 4:
                            if slutPublic >= 5:
                                hide green
                                call undressSam from _call_undressSam_30
                                $ greenArms = 2
                                show green at ri
                                y "Sam! Where are your clothes?!"
                                s g12 "I took them off."
                                y "I can see that..."
                                y "The question is {i}'why'{/i}?"
                                s g1 "The guy I was serving had some pretty juicy information for me if I did."
                                s "Here..."
                                $ randIntel = 50
                                $ intel += randIntel
                                call missionRewardInt from _call_missionRewardInt_36
                                y "Yessss, bonus intel. I'll take it."
                            elif True:
                                s g10 "Pretty boring day today. I think I'll just undress, take a shower and relax."
                                hide green with d2
                                play sound "audio/sfx/cloth.mp3"
                                call undressSam from _call_undressSam_31
                                show green at ri with d2
                                y "............"
                                s g16 "What...?"
                                y "Comfortable enough to undress of front of me now?"
                                $ greenblush = 1
                                s g48 "Oh heh~... I didn't even think about it.{w} I guess I am."
                        if randRap == 5:
                            s g20 "[playerName] be honest... what do you think of my boobs?"
                            y "Your.... boobs?"
                            s "Yeah..."
                            s g19 "I just had a customer who refused to be served by me... saying he came for Clover cause her boobs were better..."
                            s g17 "What does that even mean? {i}'Better'{/i}. You like my boobs, right?"
                            menu:
                                "Your boobs are amazing!" if True:
                                    y "[samNick]. Your boobs are amazing!"
                                    s g48 "You think so?"
                                    y "Yes, and they're so much fun to play with!"
                                    s "Heh... yes I guess they are."
                                    y "To pinch and to grope! To flick and to suck! To slap arou-...!"
                                    $ greenBlush = 1
                                    s g28 "Y-yeah... okay I get the idea!"
                                    s g1 "Thanks [playerName]. That's just what I needed to hear."
                                "They're okay" if True:
                                    y "Yeah, they're all right."
                                    s g19 "Just... all right...?"
                                    y "Huh? What did you want me to say?"
                                    s "Oh it's nothing... I just always thought they were pretty great..."
                                    y "Oh yeah no they're...{w} fine."
                                    s g20 "............."
                                    y "On a scale from one to ten I'd give them a six. They're above average."
                                    s g5 "O-only a six...?"
                                    "Sam slums off to her cell distraught."
                                    y "................"
                                    y "Was it something I said?"
                                "Say something insane" if True:
                                    y "This is a very delicate situation and I'm afraid if I awnser truthfully I'm going to get in trouble."
                                    y "And to get out of it I'm just going to say something crazy."
                                    s g10 "...."
                                    s g12 "You could just say if you don't like th-..."
                                    y "The Yermak was the first icebreaker in the world. It was build in 1897 by the English."
                                    s g10 "..............."
                                    s g45 "That's not even crazy... just obscure trivia..."
                                    y "Yeah well, if there were more icebreakers, maybe we'd have less icebergs ready to collide with fuel trucks!"
                                    s g10 "................"
                                    s "Okay, you see... {i}'that'{/i} was crazy."
                    if slutLevel >= 5:
                        if randRap == 1:
                            s g28 "[playerName]! I just had a great idea!"
                            s g22 "What if...{w} we offer customers a dish on the menu that allows them to~..."
                            s "Control our VIBs~..."
                            y "Hah, you wish!"
                            s g29 "N-not a good idea...?"
                            y "And have you and the girls all day writhing in pleasure while you're suppose to be working? I think not!"
                            s "Oh..."
                        if randRap == 2:
                            s g1 "The bar has become so popular lately!"
                            s "We get plenty of regulars and more new people are showing up every day."
                            y "And all of them want a piece of that ass."
                            $ greenBlush = 1
                            s g48 "Yeah..."
                            s "I never expected to become this popular..."
                            y "It's easy to be popular. Just dress slutty and look great in a bathing suit."
                            y "Just like me in my youth!"
                            s g41 "Yeah? You were popula-...?{w} Wait, you wore a bathing suit...?"
                            y "........."
                            y "No more questions."
                        if randRap == 3:
                            s g42 "I'm exausted..."
                            y "Tough day?"
                            s g14 "It was so busy... and my butt hurts."
                            y "Your... butt?"
                            s "From getting pinched all the time."
                            s g10 "Don't get me wrong... I sorta love all the attention I'm getting, but come on. It hurts to sit."
                            y "Hey, gotta squeeze the produce to feel if it's fresh."
                            s g12 "It's not gonna stay fresh for long if everybody keeps squeezing it."
                        if randRap == 4:
                            s g18 "Remember that you mentioned naked staff at the very start of this bar?"
                            y "I vaguely remember. Why?"
                            s g1 "Well... it might not be such a bad idea after all."
                            s g3 "I bet we'd get even more customers if we did that!"
                            y "Yeah, we're not doing that."
                            s g28 "We're not...?"
                            y "We want you to reveal just enough for them to keep coming back."
                            y "If you go naked, it puts an end to the mystery and people will stop showing."
                            s g19 "But you suggested it..."
                            y "At that time I thought the bar idea was going to be a disaster. I just wanted to see you walking around naked."
                            s g10 ".............."
                            s "Perv."
                            y "And don't you forget it."
                        if randRap == 5:
                            s g13 "Mmmm strawberry~..."
                            y "Huh..?"
                            s g22 "I was dared to make out with one of the girls who visited the bar."
                            s "It sorta was a {i}'just on the lips'{/i} kinda dare, but it ended up in a full blown make-out sessions."
                            y ".............."
                            y "And I was not informed of this event, why?"
                            s "Better luck next time, [playerName]."
                            s g23 "I'll make it up to you the next time we do something naughty~..."
                "Dismissed" if True:
                    pass
            hide scene_darkening
            hide green
            with d2
            $ greenBlush = 0
            call greenOutfitSet from _call_greenOutfitSet_10



    if greenDayJob == 5:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ greenDayJob = 0
        $ spy1Status = 0
        s "I'm back from working with Les Epines."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Sam was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Here's my report."


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_12

        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_39

        if loreChanceReward == 10:
            $ epinesLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_9

        if injectChanceReward >= 7:
            $ injectorSmall += 1
            call missionRewardItem from _call_missionRewardItem_13
            $ injectChanceReward = 0

        $ randHerbChance = renpy.random.randint(1, 10)
        if randHerbChance >= 1:
            call missionRewardItem from _call_missionRewardItem
            $ randHerb = renpy.random.randint(1, 7)
            if randHerb == 1:
                $ herbHeal += 1
            if randHerb == 2:
                $ herbAphro += 1
            if randHerb == 3:
                $ herbWeed += 1
            if randHerb == 4:
                $ herbMutant += 1
            if randHerb == 5:
                $ herbGold += 1
            if randHerb == 6:
                $ herbWhisper += 1
            if randHerb == 7:
                $ herbRebel += 1

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Sam doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if randRap == 1:
                        s g32 "Silva can become a real threat if we leave her to enact her plans."
                        s "Luckily it takes time to grow all of her monstrosities, but we should bust her before it gets out of hands."
                        s g31 "She brought something called a 'Death Willow' today. Which can spew its toxins up to two miles and kill any living being in range."
                        s "Luckily it won't mature for another ten years."
                    if randRap == 2:
                        s g10 "I robbed a botanical shop today. Apperantly Silva was running out of seeds."
                        y "Anything dangerous?"
                        s g12 "Not really, she just wanted some beautilful flowers to plant."
                        y "That sounds like Abegail all right."
                    if randRap == 3:
                        s g40 "Her tentacles needs to learn how to behave!"
                        y "................"
                        s g9 "Or vines or whatever they are! I had one wrap itself around my ankles today and lift me up."
                        y "You have my undivided attention."
                        s g10 "Get your mind out of the gutter. Silva intervened before anything happened luckily."
                        y "Better luck next time."
                        s g11 "........................"
            "Dismissed" if True:
                pass
        hide green
        hide scene_darkening
        with d2
        jump nextReport



    if greenDayJob == 6:
        $ coverCounter += 10
        $ greenDayJob = 0
        $ spy1Status = 0
        $ randMoney = renpy.random.randint(150, 250)
        s "I'm back from robbing a store."

        $ cash += randMoney
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Our notoriety went up a lot. Here's the money I got out of it..."
        call missionRewardMoney from _call_missionRewardMoney_14
        hide green
        hide scene_darkening
        with d2

    if greenDayJob == 7:
        $ coverCounter += 8
        $ greenDayJob = 0
        $ spy1Status = 0
        s "I'm back from setting fire to things."
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Our notoriety went up quite a bit."
        hide green
        hide scene_darkening
        with d2

    if greenDayJob == 8:
        $ coverCounter += 6
        $ greenDayJob = 0
        $ spy1Status = 0
        $ randMoney = renpy.random.randint(20, 60)
        s g38 "I'm back from pickpocketing."

        $ cash += randMoney
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Our notoriety went up a bit and I made a few dollars. Here..."
        call missionRewardMoney from _call_missionRewardMoney_15
        hide green
        hide scene_darkening
        with d2

    if greenDayJob == 9:
        $ coverCounter += 5
        $ greenDayJob = 0
        $ spy1Status = 0
        s "I'm back from spraypainting the mall."
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Our notoriety went up a little bit."
        hide green
        hide scene_darkening
        with d2

    if greenDayJob == 10:
        $ coverCounter += 10
        $ greenDayJob = 0
        $ spy1Status = 0
        $ randMoney = renpy.random.randint(100, 200)
        s "I'm back from stealing cars."

        $ cash += randMoney
        show scene_darkening
        with d3
        show green g38 at ri with d3
        s "Our notoriety went up. I traded the car in a dealership and got this much money..."
        call missionRewardMoney from _call_missionRewardMoney_21
        hide green
        hide scene_darkening
        with d2

    if greenDayJob == 11:
        if capturedAgents >= 1:
            $ capturedAgents -= 1
            $ freedAgents += 1
        $ greenDayJob = 0
        $ spy1Status = 0
        $ greenChest = 0
        $ greenUnder = 0
        $ greenBottom = 0
        $ greenArms = 2
        show green at ri with d3
        s g12 "So I spend the day breaking agent nanobot-control."
        s g35 "At least I got some time catching up on missed schoolwork."
        hide green with d3
        $ greenArms = 1
        $ greenChest = greenChestSet
        $ greenBottom = greenBottomSet



    if greenDayJob == 100:
        $ greenDayJob = 0
        $ spy1Status = 0
        "Sam returns from spending the day relaxing at the mall."
        if task6Stage == 3:
            jump task6



    if greenDayJob == 101:
        $ spy1Status = 0
        $ greenDayJob = 0
        $ greenChest = 0
        $ greenBottom = 0
        $ greenShoes = 0
        $ randSwimsuit = renpy.random.choice([4, 5, 6, 7])
        if randSwimsuit == 4 and under4Sam:
            $ greenUnder = 4
        elif randSwimsuit == 5 and under5Sam:
            $ greenUnder = 5
        elif randSwimsuit == 6 and under6Sam:
            $ greenUnder = 6
        elif randSwimsuit == 7 and under7Sam:
            $ greenUnder = 7
        elif True:
            call greenOutfitSet from _call_greenOutfitSet_4
            pass
        "Sam returns from spending the day relaxing at the beach."
        if samMood <= 25:
            show green g4 at ri with d3
            y "Did you have a good time at the beach?"
            s "Yeah it was okay..."
            hide green with d3
        if 26 <= samMood <= 50:
            show green g35 at ri with d3
            y "Did you have a good time at the beach?"
            s "Yeah I had fun. I feel a little guilty about shirking my responsibilities though."
            hide green with d3
        if 51 <= samMood <= 75:
            show green g1 at ri with d3
            y "Did you have a good time at the beach?"
            s "Yeah it was a beautiful day! I had a good time."
            hide green with d3
        if samMood >= 76:
            show green g1 at ri with d3
            y "Did you have a good time at the beach?"
            s "I had a great time! Thank you for sending me out there, [playerName]."
            hide green with d3


    if greenDayJob == 102:
        $ spy1Status = 0
        $ greenDayJob = 0
        $ treatBag += 1
        play sound "audio/sfx/itemGot.mp3"
        "Sam brought home a Trick or Treat bag today. Check your ITEMS to see what's inside!"





    if month == 10 and 14 <= day <= 31 and redDayJob >= 1:
        $ randTreat = renpy.random.randint(1,4)
        if randTreat == 1:
            $ randTreat = 0
            $ treatBag += 1
            "Clover brought home a Trick or Treat bag today. Check your ITEMS to see what's inside!"
        elif True:
            pass


    if redDayJob == 1:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ redDayJob = 0
        $ acesRep += 1
        $ spy2Status = 0
        c "I'm back from working with the Aces."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Clover was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Here's my report."


        call missionRewardRep from _call_missionRewardRep_5


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_6
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_16
        if loreChanceReward == 10:
            $ acesLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_3

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Clover doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if acesRank <= 1:
                        if randRap == 1:
                            c "They got like... the biggest boat in the harbor!"
                            c "I got to go on it today and it's beautiful! The insane is even pretty than the outside!"
                            c "I mean... it was probably bought with drug money, but still!"
                        if randRap == 2:
                            c "Not sure why'd anyone would actually want to fight for the Aces. If you don't have money, you're just a meatshield to them."
                            c "And I mean a 'lot' of money. Having in villa in Beverly Hills is considered poor to them."
                            y "I guess people just want a taste of the good life."
                            c "{b}*Scoffs*{/b} I guess there are hopefulls who try to climb the ranks to see if some of that money is coming their way, but I don't see the Aces letting anyone into their little club."
                        if randRap == 3:
                            c "I feel like I'm really fitting in with the Aces! I bought all kinds of expensive designer clothes and I already put a downpayment on a car!"
                            y "Wait... you what?!"
                            c "Relax, it's my daddy's creditcards."
                            y "Oh..."
                        if randRap == 4:
                            c "THEY{w} GOT{w} A{w} CHOCOLATE FOUNTAIN!"
                            c "And not just a regular one, a big, gigantic one! With Belgian chocolate!"
                            c "Oooooh it was sooo dreamy~...."
                            c "Of course nobody had any... cause you know... we'd no longer fit in our designer clothes, but just being this close to one felt like a blessing~..."
                            y ".............."
                        if randRap == 5:
                            c "The Aces are full of cute boys! I mean sure, they're all a bunch of velvet graced softies who never worked a hard day in their lives, but they're so handsome!"
                            c "They just have this weird obsession with redheads. I got rejected two times today because they said they weren't into blondes! I'm jealous of Sam..."
                            c "Sam needs to be more appreciate of working for the Aces! Sure, they're a bunch of rich jerks who do crime just for fun, but they're so hot!"
                            y "Go to your cell, Clover..."
                    if acesRank >= 2:
                        if randRap == 1:
                            c "I was so wrong about the Aces... They're mean and not for a good reason."
                            c "I get wanting to show off your money, but they paid a homeless man $1000 to allow them to beat him up."
                            c "It was... hard to watch..."
                            y "They paid a homeless man to beat him up?"
                            c "They just wanted to know what it felt like... I took him to the hospital afterwards."
                            c "Even the doctors were shocked..."
                            y "....................."
                        if randRap == 2:
                            c "..................."
                            y "What?"
                            c "You know that one of the Aces have a gold plated thesaurus?"
                            y "A what?"
                            c "You know, a thesaurus. A book that has synonyms for words in it... He's got one... only its cover is decorated in gold..."
                            y "....................."
                            y "What?"
                            c "I don't know, [playerName]. Sometimes the shit they spend their money on even goes beyond me..."
                        if randRap == 3:
                            c "Well the Aces got money, I'll give 'em that much. But deep down they're just ordinary gangsters."
                            c "We robbed a clothing store today just for {i}'fun'{/i}. The clothes weren't even that expensive, they just did it for the cheap thrill of it."
                            c "Poor shop owner was shaking in his boots. Luckily nobody got hurt."
                        if randRap == 4:
                            c "The Aces held a charity event today."
                            y "Oh that's good of them."
                            c "........................."
                            y "Not good of them...?"
                            c "You don't think they're actually going to donate that money to charity, do you?"
                            c "When the event was over, they took the donation bowl out back and used it to bail out a nightclub that was owned by a friend."
                            y "........."
                            c "Not a cent went to charity."
                        if randRap == 5:
                            c "Don't get me wrong , [playerName]. I have never been poor."
                            y "Okay...?"
                            c "I've lived in Beverly Hills, bought expensive brand clothes and drove expensive cars."
                            y "Your point...?"
                            c "But at least I didn't spend it on sex, drugs and violence. The Aces bought a truckload of explosives today."
                            y "!!!"
                            c "They were going to blow up the stadium. Just in time I managed to convice them that being a terrorist was not fashionable, and instead they blew it up out of town."
                            c "Hundreds of people might've died... Just cause they wanted to see an explosion..."
                            y ".................."
            "Dismissed" if True:
                pass
        hide red
        hide scene_darkening
        with d2
        jump nextReport


    if redDayJob == 2:
        if task23Stage == 1:
            jump task23
        if task2Stage == 16:
            jump task2
        elif task18Stage == 1:
            jump task18
        elif 1 <= task17Stage <= 5:
            $ coverCounter += 2
            $ cash += randMoney
            $ intel += randIntel
            $ redDayJob = 0
            $ spy2Status = 0
            jump task17
        elif True:
            pass
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ redDayJob = 0
        $ punkRep += 3
        $ spy2Status = 0
        c "I'm back from working with the Drift Punks."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Clover was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Here's my report."


        call missionRewardRep from _call_missionRewardRep_6


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_7
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_18
        if loreChanceReward == 10:
            $ punkLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_4

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Clover doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if punkRank <= 1:
                        if randRap == 1:
                            c "Ew ew ew!"
                            y "What?"
                            c "One of those hackers wanted me to do some work today, so I sat in his chair."
                            y "So?"
                            c "And it was sticky! That thing probably hasn't been washed in years. I'm going for a shower!"
                        if randRap == 2:
                            c "I got to check out the trucks today, which was pretty cool."
                            c "The Drift Punks take really good care of their cars, and got some really sweet modifications."
                            y "I didn't expect you to be into cars."
                            c "Well I don't know much about cars, but I know when something is neat. This one car had speakers build into where the headlights should be."
                            c "And the bumper had build in headlights instead. He also had some custom made rims on his wheels."
                            c "Modifying a car is like taking a big build-a-bear box. You can add or remove from it as you see fit."
                            y "Sounds expensive."
                            c "Oooh yeah."
                        if randRap == 3:
                            c "Another boring day of breaking into people's bank accounts..."
                            y "Boring?"
                            c "Yeah... when you think bankrobbery, you don't think of sitting behind a computer, watching code..."
                            c "I guess there's no risk of anything being hurt this way, but it's not exactly exciting either."
                            c "Unless you can call dodging greasy nerds exciting."
                        if randRap == 4:
                            c "There was a party planned for tonight and for a moment I actually got excited."
                            c "There seems to be a clear difference between the tech nerds and the music nerds in the Punks."
                            c "The music geeks are way more fun. There's some cute guys, cool gadgets and awesome DJ's!"
                            y "Oh, so you had fun today?"
                            c "{b}*Scoffs*{/b} No. Only the higher ranking members are invited to those parties... I had to keep busy preparing for the party without getting an invite!"
                        if randRap == 5:
                            c "I saw the Punks play a really mean prank on somebody today."
                            y "Oh?"
                            c "This mom with her kids went to get some money out of the ATM and they hacked it from a distance. Made it seem as if her back account was empty."
                            c "I saw her almost broke down in tears..."
                            y "Wow... that is mean. What happened next?"
                            c "Well the Punks were laughing their ass off of course. When they headed back to the base, I snuck off to let the mother know what happened."
                            c "I also showed her how to get her money back and she thanked me for the help... Not knowing I was part of the jerks who did this to her..."
                            y "At least there's a happy ending this time."
                            c "Yeah... this time."
                    elif punkRank == 2:
                        if randRap == 1:
                            c "I don't understand those Punks! I actually put in effort today into learning about their hobbies and it backfired!"
                            c "I told them I was interested in games, expecting them to show me some. Instead they just started asking me stupid questions and telling me I wasn't a {i}'real gamer girl'{/i}."
                            y "Sounds like a great bunch."
                        if randRap == 2:
                            c "I asked someone what kind of music they liked and they just said 'nightcore'."
                            y "What's nightcore?"
                            c "Apperantly it's just regular songs, sped up and a beat put underneath them. You can find it online."
                            y "Well let's see then..."
                            y "............................."
                            y "Why do you all of these videos have half naked anime girls of questionable age?"
                            c "Beats me..."
                        if randRap == 3:
                            c "I got to try out some of their gadgets today."
                            y "Do tell."
                            c "Well... I'll be honest, WOOHP has like... kinda spoiled me. I wasn't impressed."
                            c "They seemed to notice and slumped back in disappointment."
                            c "So yay~... Another day of me making friends~..."
                        if randRap == 4:
                            c "Payday."
                            y "Payday?"
                            c "Yup.... I made four-thousand dollars."
                            y "No way! That's great ne-...{w} Why aren't you smiling?"
                            c "It's in Bitcoins."
                            y "Oh... What are Bitcoins?"
                            c "Some kind of fake currency, I'm still figuring out how it works..."
                            y "..................."
                            y "So no money then?"
                            c "Nope. Unless our local supermarket accepts Bitcoin, which I doubt."
                            y "....................."
                        if randRap == 5:
                            c "Urgh! I got so upset today!"
                            y "Being harressed by nerds again?"
                            c "No, I tried to play a video game, but I just couldn't do it!"
                            c "The story was really good though, so I wanted to see what happened next!"
                            y "You could ask one of the Punks to help you out?"
                            c "Yeah right, as if they'd help out a girl with 'their' hobby."
                            y "Next time just try asking them. You want to see how the story continues, right?"
                            c "......................."
                    elif punkRank == 3:
                        if randRap == 1:
                            c "So er... Like... today wasn't a complete disaster."
                            c "They asked me to come join a board game they were playing."
                            y "Let me guess. Dungeons & Dragons."
                            c "Y-yes! How did you know?!"
                            y "Stereotypes exist for a reason."
                            c "Anyways, it was a little complex, but I made my own character and it was sort of like playing a video game."
                            c "I expected them to get fed up with me not knowing the rules, but they were really patient and I had a good time."
                            y "A yes, Dungeons and Dragons. The truest test of your friendship comes after looting the boss and fighting over who gets the loot."
                        if randRap == 2:
                            c "Hiya, [playerName]!"
                            y "You're... in a good mood."
                            c "Yeah I finished a game today and it was amazing! My first game that I ever completed!"
                            y "I thought you didn't like video games."
                            c "Well I don't... but this one was really good. The guys promised to not help me unless I got stuck and it was a lot of fun."
                        if randRap == 3:
                            c "Oh man, we robbed a bank today!"
                            c "I mean... that's a bad thing, but it was spectacular. There were choppers, guns and disco lights..."
                            y "What was that last one?"
                            c "Oh right, it's one of the gadgets they've got. They call it a disco grenade. Basically it starts blasting music and lights up like a discoball."
                            c "Before anyone knew what hit them, we were already inside the vault."
                            y "Neat, did you earn anything?"
                            c "Oh... er..."
                            y "They paid you in Bitcoin again, didn't they?"
                            c "They did... one day I'll figure out how to cash those and we'll be rich..."
                            c "I did manage to sneak this into my pocket though."
                            $ randMoney = 100
                            $ cash += 100
                            call missionRewardMoney from _call_missionRewardMoney_49
                        if randRap == 4:
                            c "Working for the Drift Punk has its ups and downs..."
                            c "I spent all day working on code again and it was hell. 'Crunch' they called it. Had to get it out before tomorrow. I'm wrecked..."
                            c "But we got free pizza and soda so it's not all bad..."
                        if randRap == 5:
                            c "We got into a fight with a rival gang today. Gotta say... the Drift Punk really really cool with their chrome guns and LED lights."
                            c "The way they blast Ride of the Valkerie when storming their decked out cars into battle."
                            y "Sounds like you caused some serious damage today."
                            c "We did, but we were trying out our new taser gadgets, so I don't think anyone was killed."
                            c "We did take some gunfire though. Some fleshwounds, but nothing serious."
                            y "All right, head back to your cell. You've earned your rest."
                    elif punkRank == 4:
                        if randRap == 1:
                            c "Uuuuuuugh!"
                            y "Okay... So what happ-..."
                            c "Uuuuuuuuugh!"
                            y "................."
                            c "Just one bug... Just one bug that took us all day to fix. ALL DAY!"
                            c "You know how frustrating it is to test the same code over and over and over again and not being able to figure out why it's not working?"
                            y "I imageine very."
                            c "I'm going to bed."
                        if randRap == 2:
                            c "{b}*Humming*{/b}"
                            y "Good mood?"
                            c "Good day. Got a new video game, gonna be playing D&D again soon and there's a big super hero movie coming out soon."
                            y "I see, I see...."
                            y ".............."
                            c "What?"
                            y "Cinema has been bombed by the Outsiders. Calling it a propaganda machine."
                            c "NO! {b}*Whines*{/b} Noooooo, I was looking forward to seeing that movie on the big screen."
                            y "You're surrounded by hackers, just pirate it."
                            c "It's not the same~...."
                        if randRap == 3:
                            c "Did any package arrive while I was gone?"
                            y "I don't think so. What did you order?"
                            c "One of those headphones with the cat ears. The expensive ones, with the LED lights. They've been difficult to get a hang off."
                            y "Nothing came in I fear."
                            c "Bah... all my friends at Drift Punk have them."
                            c "I-I mean...! All those criminals at Drift Punk have them...!"
                            y "Don't go too deep undercover, Clover. Remember that these are the bad guys."
                            c "I know...."
                        if randRap == 4:
                            c "I'm just gonna go grab a soda from the bar."
                            y "Wait, how was your day at the Drift Punk?"
                            c "Oh, fun actually. Someone brought their manga collection and it's got a soda hero."
                            c "Which made me thirsty for soda."
                            y "Marketing at it's finest."
                        if randRap == 5:
                            c "Hah! Critical success!"
                            y "What...?"
                            c "We were robbing a jeweler and just for fun we rolled a D20 after we were done robbing him."
                            c "It was a natural twenty and that means there's always more treasure!"
                            c "Turns out he was hiding a box of loose gems aswell. So we scored the motherload!"
                            y "Too bad you only get paid in Bitcoin."
                            c "Yeah..."
            "Dismissed" if True:
                pass
        hide red
        hide scene_darkening
        with d2
        jump nextReport


    if redDayJob == 3:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ redDayJob = 0
        $ outsideRep += 1
        $ spy2Status = 0
        c "I'm back from working with the Outsiders."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Clover was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Here's my report."


        call missionRewardRep from _call_missionRewardRep_7


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_8
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_19
        if loreChanceReward == 10:
            $ outsidersLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_5

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Clover doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if outsideRank <= 1:
                        if randRap == 1:
                            c "Ew I still smell like spraypaint."
                            y "Didn't know you were into arts and crafts."
                            c "I'm not..."
                            c "The Outsiders organized a 'street art' day to let the members express themselves and unwind a bit."
                            y "And you participated?"
                            c "I was sorta forced to. I don't think I impressed anyone."
                        if randRap == 2:
                            c "Well I just saved a couple of lives today."
                            y "Yeah?"
                            c "Yeah, some of the more bullheaded members thought up a plan to parachute into the Drift Punk base and take them by surprise."
                            c "After a lot of argueing, I managed to talk them out of it. It was a suicide mission, even if they won't admit it."
                        if randRap == 3:
                            c "Well I got to fire an assault rifle today, which was kinda fun."
                            c "The Outsiders are smuggling in so many guns, you get to try some of them out. A little worried to see this much hardware get into the city though."
                            c "You ever use guns?"
                            y "Hardly. So far I haven't had the use for one yet."
                            c "Let's hope it stays that way."
                        if randRap == 4:
                            c "Robbed a designer clothing store today."
                            y "That must've been painful."
                            c "Yeah I had to grit my teeth. They were only there for the money and when I tried to sneak out a cute top, they said not to touch the stuff. That it was probably made by child labor."
                            c "I mean... They're not wrong... but it was a really cute top."
                        if randRap == 5:
                            c "Somehow the Outsiders got their hands on some valuable gemstones and decided to trade them with the Glimmers."
                            y "And?"
                            c "Turned sour when the Aces showed up and turned into a big three way fight."
                            c "The Aces and the Glimmers had more attention for eachother though, so we managed to sneak off unharmed."
                    if outsideRank >= 2:
                        if randRap == 1:
                            c "Yeah I'm pretty much done with the Outsiders."
                            y "How come?"
                            c "They can't play the 'misunderstood youth' card forever. They drove a truck into a restaurant today!"
                            c "A truck! There were people in that place!"
                            y "Casualties?"
                            c "I don't know, I don't think so. But what if there had been?"
                            c "Just cause the restaurant was owned by a big corperation, doesn't mean the people visiting it are just collateral damage."
                        if randRap == 2:
                            c "Some guys were making molotov cocktails today."
                            c "Luckily they 'mysteriously' blew up before anyone got hurt."
                            y "Well done, Clover. The fewer bombs the better."
                        if randRap == 3:
                            c "Got some extra cash."
                            y "Oh nice, how did you get it?"
                            c "Dared someone to get a tattoo, but she chickened out at the last second. Made a cool $50 bucks."
                            $ randMoney = 50
                            $ cash += 50
                            call missionRewardMoney from _call_missionRewardMoney_50
                        if randRap == 4:
                            c "{b}*Sighs*{/b} I can see why the Outsiders are so cautious of the world."
                            c "They were just skating when an angry mob of citizens showed up. They banded together to scare the gangsters away."
                            c "Meanwhile the Outsiders were just minding their own business so when they saw the mob they paniced and drew their weapons."
                            c "I managed to get in between them and calm the situation down, but the city is a powderkeg ready to go off."
                        if randRap == 5:
                            c "You ever read Romeo and Juliet?"
                            y "No. You?"
                            c "No, but I know the story and I saw it re-lived today."
                            c "I caught a girl from the Outsiders and a boy from Drift Punk playing a video game together."
                            c "Turns out they've been seeing each other regularly. I promised not to tell anyone."
            "Dismissed" if True:
                pass
        hide red
        hide scene_darkening
        with d2
        jump nextReport


    if redDayJob == 4:
        $ spy2Status = 0
        if clubStage <= 3:
            $ redDayJob = 0
            $ clubStage += 1
            "Clover spent the day cleaning the milkshake bar and headed back to her cell."
            if clubStage >= 4:
                scene bgClub1
                with fade
                jump tutStage9
        elif True:

            if redDayJob == 4:
                $ redDayJob = 0
                call undressClover from _call_undressClover_19
                $ redChest = 2
                $ redBottom = 2
                $ redShoes = 2
                $ redHat = 2
                show scene_darkening with d3
                show red r1 at ri with d3
                c "I'm back from working at the milkshake bar."

                $ randMoney = renpy.random.randint(35, 50)

                if checkMark1 == True:
                    $ randMoney += 50
                if checkMark2 == True:
                    $ randMoney += 60
                if checkMark3 == True:
                    $ randMoney += 70
                if checkMark4 == True:
                    $ randMoney += 80
                if checkMark5 == True:
                    $ randMoney += 90
                if checkMark6 == True:
                    $ randMoney += 100

                $ randPenalty = renpy.random.randint(1, 3)
                if randPenalty == 3:
                    if 80 <= nanoLevelClover <= 100:
                        $ randMoney = randMoney / 2
                        "There seems to be some money missing..."
                    if 60 <= nanoLevelClover <= 79:
                        $ randMoney -= randMoney / 3
                        "There seems to be some money missing..."
                    if 40 <= nanoLevelClover <= 59:
                        $ randMoney -= randMoney / 4
                        "There seems to be some money missing..."

                $ cash += randMoney
                call missionRewardMoney from _call_missionRewardMoney_17
                pause 0.2

            menu:
                "Tell me about your day" if True:
                    if slutLevel <= 1:
                        if randRap == 1:
                            c r11 "I've never gone undercover in a place like this before."
                            c r23 "If I'm honest... it's kinda fun~... ♥"
                            y "Fun? I'm glad you think so. Sam doesn't seem to feel the same."
                            c r10 "Oh she's just being prudish. She gets flustered easily."
                            c "As long as the customers keep their hands to themselves, I have no complaints."
                        elif randRap == 2:
                            c r24 "There was this one really cute guy at the bar today~...."
                            c "I gave him a milkshake on the house and sat on his lap."
                            y "So instead of working you were flirting with the customers..."
                            c r28 "O-oh...! Right, I guess I was. Sorry about that boss."
                        elif randRap == 3:
                            c r1 "Somebody left a big tip for me today!"
                            y "Nice! What did you have to do to earn that?"
                            c r18 "What do you mean...? She was just nice and left me a tip for my service."
                            y "Oooh your {i}'service'{/i}. I see what you're getting at. Wink wink, nudge nudge."
                            c r10 ".................."
                            c "You're an idiot. Am I dismissed now...?"
                        elif randRap == 4:
                            c r11 "Hmm...."
                            y "You seem to be pondering."
                            c r12 "No it's just that..."
                            c r22 "I remember seeing this really cute orange thong at the mall. It would go great with this uniform."
                            y "Thong you say...?"
                            c "Bet I got your attention that way~..."
                            c r42 "Last time I looked it was sold out, but if you come across it. Please buy it for me~..."
                        elif randRap == 5:
                            c r12 "Well it happened..."
                            y "What happened?"
                            c "First customer spilled his beer on me. Bastard was aiming for my top."
                            y "You don't look very soaked."
                            c r10 "Nah I managed to dodge most of it. I'm too sly for those kinds of tricks."
                    if slutLevel == 2:
                        if randRap == 1:
                            c r1 "Today was a pretty fun day."
                            c "Had a few customers come up to me and ask me questions."
                            y "Questions?"
                            c "Yeah, they were interested in how and why I got this job."
                            c r2 "I made up a cover story of course, but they ate it up."
                            c "I guess sometimes the customers just want to come in for a chat."
                            y "A chat with a hot girl in a revealing uniform."
                            c r10 "Well yeah... obviously."
                        elif randRap == 2:
                            $ redBlush = 1
                            c r16 "Can you see them...?"
                            y "See them? See what?"
                            c r19 "My... nipples..."
                            y "..............."
                            c r31 "Listen, I know it sounds crazy, but this guy was laughing about how my nipples were poking through my top."
                            y "I don't see anything. He was probably just trying to get a rise out of you."
                            c "But what if he did see them...?"
                            y "Then you probably got a rise out of him instead~..."
                        elif randRap == 3:
                            c r38 "Darn it... bastard got me."
                            y "Bastard? Were you attacked?!"
                            c r10 "Nah, nothing like that. This one creepy guy kept glancing at me when he thought I wasn't looking."
                            c "I knew it was coming. I just didn't know when."
                            y "I'm confused. Saw what coming?"
                            c r12 "A spank loud enough to be heard by the whole bar."
                            c "I kicked him out, but judging by the shit-eating grin on his face, he already got what he came for."
                            "Clover painsfully rubs her butt and shrugs."
                        elif randRap >= 4:
                            c r18 "Someone made a suggestion today..."
                            y "Yeah? Let's hear it."
                            c "Milkshakes... made with...."
                            y "..........."
                            c r16 "Breast milk."
                            y "............"
                            y "Did you kick his ass out?"
                            c r3 "Oooh yeah."
                    if slutLevel == 3:
                        if randRap == 1:
                            y "Hey Clover. Are you putting your training to good use?"
                            c r18 "Training?"
                            y "Y'know... our evening sexy times. Does it help you improve your customer skills at the bar?"
                            c r16 "Er... not really.{w} Are you suggesting I start giving the customers boobjobs?"
                            y "No!{w} Well actually..."
                            menu:
                                "Encourage sluttiness" if True:
                                    $ slutPublic += 1
                                    y "Maybe we could add that to the menu~..."
                                    c r10 "I'm not going to start giving the customers boobjobs, [playerName]..."
                                    y "Handjobs?"
                                    c r17 "What? No!"
                                    y "Buttjobs?{w} What other jobs are there...?"
                                    c r39 "I'm not doing any of those. I might act like a whore sometimes, but I'm not really."
                                    y "But maybe you should be~..."
                                    y "Okay wait, before you throw me a glare, just hear me out."
                                    y "How many more customers would we get if your cute slutty butt was on the menu~..."
                                    y "We'd have a full house every night!"
                                    c r10 ".............."
                                    y "..............."
                                    y "Blowjob! I knew I had forgotten one!"
                                    c r12 "I'm going back to my cell..."
                                "Discourage sluttiness" if True:
                                    y "Actually no, what am I saying?"
                                    y "You should stay my private play toy."
                                    c r10 "................."
                                    c r11 "I'm nobodies {i}'playtoy'{/i}"
                                    y "Then what do you call it when you get naked for me...?"
                                    c r12 "I don't now! Not playing! And not toying either...! It's different."
                                    c r11 "................."
                                    c "Okay maybe not that different, but you know what I mean!"
                                    y "I honestly have no idea."
                                    c "{b}*Sighs*{/b} I'm going back to my cell..."
                        elif randRap == 2:
                            c r1 "Hey [playerName]. I love this uniform."
                            y "Yeah?"
                            c r3 "It's so sexy. Normally I don't wear anything this revealing. So I've grown kind of attached to it."
                            c "Kinda like... my first {i}'slutwear'{/i}."
                            c "Maybe I should wear it during boobjobs!"
                            y "Tempting...! But you don't want your uniform covered in stains when you have to go serve the customers."
                            c r29 "Oh right..."
                        elif randRap == 3:
                            c r10 "This one really hot guy showed up today."
                            c "Unfortunately he had his girlfriend with him..."
                            c r12 "She was equally hot though..."
                            y "Could always have a threesome."
                            c r8 "What? No! Ew!"
                            c r11 ".................."
                            y "You thinkin' about it, aren't you?"
                            $ redBlush = 1
                            c r49 "{b}*Sputters*{/b} N-no! Never!"
                            c "I'm going back to my cell...!"
                            "Clover rushes off."
                        elif randRap == 4:
                            c r1 "I found a silver dollar on the floor today."
                            y "Sweet."
                            c "I'm not really a coin collector though, so I sold it to one of the guests."
                            c "Still... made some nice pocket money. Here."
                            $ randMoney = 30
                            $ cash += randMoney
                            call missionRewardMoney from _call_missionRewardMoney_52
                        elif randRap == 5:
                            c r40 "Oh my God, today there was this one girl who came in. Total slut!"
                            y "Okay...?"
                            c r31 "She wore basically nothing, and showed so much cleavage!"
                            y "..........."
                            c "Her outfit had these gaudy colors and you could tell that she was just wearing it to get attention."
                            y "So...{w} kinda like your outfit."
                            c r29 "What? No! She looked like a whore!"
                            y "............"
                            c r12 "I mean... more like a whore than I do..."
                            c r30 "Oh God... she probably is saying the same thing about me..."
                            y "Pot calling the kettle a hoe."
                            c r10 "Hah hah, very funny."
                    if slutLevel == 4:
                        if randRap == 1:
                            c r11 "The bar is getting more female visitors and I don't know how to feel about that..."
                            y "Oh?"
                            c "[playerName] I already get seen as a lust object by half the population. I was hoping to still be seen as a human being by the other half."
                            y "Nah, waitresses aren't human beings. That's why it's okay to scream and yell at them for messing up your order."
                            c r10 ".............."
                            c "I know you are joking, but damn it feels like that sometimes."
                        elif randRap == 2:
                            c r11 "So..."
                            c "A customer suggested we should do a Royal Goblet, but instead of beer do it with milkshakes."
                            y "Wouldn't that ruined the aesthetic of a fresh milkshake?"
                            c r12 "It gets better. He then suggested he'd lick the wiped cream off of the tit afterwards."
                            y ".........."
                            c r18 "Should we do this...?"
                            menu:
                                "Encourage sluttiness" if True:
                                    $ slutPublic += 1
                                    y "Sugary nipples."
                                    c r3 "Yup..."
                                    y "That sounds... fun."
                                    c r14 "It would involve my nipples being sucked by strangers though."
                                    c "I mean... if you're okay with it, then so am I."
                                "Discourage sluttiness" if True:
                                    y "Do you want to?"
                                    c r18 "Er... I don't know. Do I?"
                                    y "You tell me. It's your titty getting sucked."
                                    c "Well... maybe not by random customers..."
                                    y "I thought as much."
                        elif randRap == 3:
                            c r10 "The floor in the bar is getting sticky from all the spilled milkshakes."
                            y "Ah come on, it can't be {i}'that'{/i} bad, right?"
                            c "A customer's chiwawa got stuck, glued to the floor."
                            y "Oh... I'll go get the mop."
                        elif randRap == 4:
                            c r1 "Cherry?"
                            y "Cherry?"
                            "Clover holds up a cherry for you."
                            y "Oh... sure. Thanks."
                            c "We got too many of these. Normally we put them on top of the milkshakes, but there's more cherries than milk now."
                        elif randRap == 5:
                            c "Bounce bounce bounce~..."
                            y "What are you doing...?"
                            c "Bouncing my boobs."
                            y "I can see that.... Why?"
                            c r22 "Well cause y'know...{w}{i} My milkshakes bring all the boys to the yard. ♫♪{/i}"
                            y ".................."
                    if slutLevel >= 5:
                        if randRap == 1:
                            c r11 "I've got a problem..."
                            c "A customer called me a whore today and my nipples got hard."
                            y "Well you are a whore."
                            c r42 "No, don't you start aswell...!"
                            y "Go on, undress whore."
                            c r30 "R-right here?"
                            y "Did I stutter?"
                            c r29 "................"
                            hide red with d2
                            play sound "audio/sfx/cloth.mp3"
                            call undressClover from _call_undressClover_20
                            show red at ri with d2
                            y "Hmmm...."
                            y "Yup, hard enough to cut glass with."
                            $ redArms = 4
                            c r10 "............."
                            c "Can I go back to my cell now...?"
                            y "Didn't say the magic word~..."
                            c r14 "Can I go back to my cell now... master?"
                            y "There we go. Off you go slut."
                        if randRap == 2:
                            if slutPublic >= 5:
                                c r1 "I gotta say. Serving customers naked is really fun."
                                y "Oh?"
                                c r1 "Some meals come with perks like getting your food served by a naked waitress."
                                c "They're expensive, but if someone orders them, the whole bar starts cheering."
                                c "It's fun for the customer and it's making me feel great about myself."
                                c r1 "Plus the guests leave much better tips."
                                y "I'm glad that you're taking your role as a waitress so serious."
                            elif True:
                                c r10 "Pretty boring day. Not much to talk about."
                        if randRap == 3:
                            if slutPublic >= 5:
                                c r1 "Those boobjobs we practised are really coming in handy."
                                c "Everyone wants a piece of them."
                                y "You're giving customers boobjobs now?"
                                c r2 "Nah, but they can grope if they want."
                                c r3 "Plus I learned all kinds of ways of moving without using my hands."
                                "Closer stands on the spot and bounces her boobs around."
                                y "Truly a talent to be treasured."
                            elif True:
                                c r10 "Well... you did it."
                                y "Huh?"
                                c "I nearly choked on a hotdog today and didn't even have a gag reflex."
                                y "{b}*Smirk*{/b} I'm happy to have helped you develop that skill."
                        if randRap == 4:
                            c r1 "Moneeeey!"
                            $ randMoney = 150
                            $ cash += randMoney
                            call missionRewardMoney from _call_missionRewardMoney_87
                            y "Woah, how'd you get this?"
                            c r3 "Not saying~...."
                            y "...?"
                            y "You smell sweet..."
                            "{b}*Poke*{/b}"
                            y "And you're sticky..."
                            c r2 "Er... hehe~..."
                            y "Almost like you were drenched in milkshakes~..."
                            c "All right, I'm off to my cell now!"
                        if randRap == 5:
                            c r22 "Hey [playerName]. Are we going to have sex tonight?"
                            y "Eager, aren't we?"
                            c r24 "It has been an incredibly hot day today. With waitresses getting naked and dancing on tables, to getting my whole body groped."
                            c r42 "I'm so pent-up with sexual frustration right now, I could anyone."
                            y "Anyone?"
                            c r15 "Yeah."
                            y "What about Tim Scam?"
                            c "Yeah I could fuck him."
                            y "What about the bookstore clerk?"
                            c "I'd be pegging that girl all night."
                            y "What about Mathias?"
                            c r29 "Ma-...?"
                            $ redBlush = 1
                            c r48 ".................."
                            y "Yeah yeah, maybe after all of this is over you two can get together."
                            y "For now head back to your cell. I might visit you later."
                "Dismissed" if True:
                    pass
            hide scene_darkening
            hide red
            with d2
            $ redBlush = 0
            call redOutfitSet from _call_redOutfitSet_8


    if redDayJob == 5:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ redDayJob = 0
        $ spy2Status = 0
        c "I'm back from working with Les Epines."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Sam was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Here's my report."


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_13
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_40

        if loreChanceReward == 10:
            $ epinesLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_10

        if injectChanceReward >= 7:
            $ injectorSmall += 1
            call missionRewardItem from _call_missionRewardItem_14
            $ injectChanceReward = 0

        $ randHerbChance = renpy.random.randint(1, 8)
        if randHerbChance >= 2:
            call missionRewardItem from _call_missionRewardItem_1
            $ randHerb = renpy.random.randint(1, 6)
            if randHerb == 1:
                $ herbHeal += 1
            if randHerb == 2:
                $ herbAphro += 1
            if randHerb == 3:
                $ herbWeed += 1
            if randHerb == 4:
                $ herbMutant += 1
            if randHerb == 5:
                $ herbGold += 1
            if randHerb == 6:
                $ herbWhisper += 1

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Clover doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if randRap == 1:
                        c r32 "............."
                        y r31 "Clover?"
                        c "Shh!"
                        y "................"
                        c r38 "Okay, I think I lost him."
                        c r10 "I angered a bee and it's been following me around all day."
                    if randRap == 2:
                        c r10 "Do you think Silva will get angry if I bring some weed killer?"
                        c "Some of her vines were getting a little too comfortable.... If you get what I'm saying."
                    if randRap == 3:
                        c r10 "Silva is a weird one... She seems to love company and at the same time has an intense hatred of humanity."
                        c r12 "Anyways, I had to steal these seeds for her. They're used to grow this dangerous killer plant."
                        y "That sounds risky..."
                        c "Well it takes ten years for them to mature, so as long as we deal with this situation before then, I think we'll be fine."
                    if randRap == 4:
                        c r16 "Have you ever noticed the smell at Abegail's jungle?"
                        c "You'd think it would smell nice, with all the flowers and all."
                        c r12 "But she has these nasty inspect eating plants that just smell like rotting flesh."
                    if randRap == 5:
                        c r14 "{i}♫♪ Ring around the rosie. Pocket full of posies. ♫♪{/i}"
                        c r1 "Did you know that posies were a small bouquet of flowers worn during the bubonic plague in England?"
                        y ".............."
                        y "Learned that from Silva?"
                        c r3 "Yuuuup."
            "Dismissed" if True:
                pass
        hide red
        hide scene_darkening
        with d2
        jump nextReport



    if redDayJob == 6:
        $ coverCounter += 10
        $ redDayJob = 0
        $ spy2Status = 0
        $ randMoney = renpy.random.randint(150, 250)
        c "I'm back from robbing a store."

        $ cash += randMoney
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Our notoriety went up a lot. I did make some money so you can have it..."
        call missionRewardMoney from _call_missionRewardMoney_20
        hide red
        hide scene_darkening
        with d2

    if redDayJob == 7:
        $ coverCounter += 8
        $ redDayJob = 0
        $ spy2Status = 0
        c "I'm back from setting fire to things."
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Our notoriety went up quite a bit."
        hide red
        hide scene_darkening
        with d2

    if redDayJob == 8:
        $ coverCounter += 6
        $ redDayJob = 0
        $ spy2Status = 0
        $ randMoney = renpy.random.randint(20, 60)
        c "I'm back from pickpocketing."

        $ cash += randMoney
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c r12 "Our notoriety went up a bit. It's not much, but it's a payday...."
        call missionRewardMoney from _call_missionRewardMoney_35
        hide red
        hide scene_darkening
        with d2

    if redDayJob == 9:
        $ coverCounter += 5
        $ redDayJob = 0
        $ spy2Status = 0
        c "I'm back from spraypainting the mall."
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Our notoriety went up a little bit."
        hide red
        hide scene_darkening
        with d2

    if redDayJob == 10:
        $ coverCounter += 10
        $ redDayJob = 0
        $ spy2Status = 0
        $ randMoney = renpy.random.randint(100, 200)
        c "I'm back from stealing cars."

        $ cash += randMoney
        show scene_darkening
        with d3
        show red r38 at ri with d3
        c "Our notoriety went up. I had to get rid of the car, so I sold it to a dealership. They paid me this much..."
        call missionRewardMoney from _call_missionRewardMoney_36
        hide red
        hide scene_darkening
        with d2



    if redDayJob == 11:
        if capturedAgents >= 1:
            $ capturedAgents -= 1
            $ freedAgents += 1
        $ redDayJob = 0
        $ spy1Status = 0
        $ redChest = 0
        $ redBottom = 0
        $ redArms = 2
        $ redUnder = 0
        show red at ri with d3
        c r12 "Boooring.... I spend the days breaking agents out of their nanobot control."
        hide red with d3
        $ redArms = 1
        $ redChest = redChestSet
        $ redBottom = redBottomSet


    if redDayJob == 100:
        $ redDayJob = 0
        $ spy2Status = 0
        "Clover returns from spending the day relaxing at the mall."


    if redDayJob == 101:
        $ spy2Status = 0
        $ redDayJob = 0
        $ redChest = 0
        $ redBottom = 0
        $ redShoes = 0
        $ randSwimsuit = renpy.random.choice([4, 5, 6])
        if randSwimsuit == 4 and under4Clover:
            $ redUnder = 4
        elif randSwimsuit == 5 and under5Clover:
            $ redUnder = 5
        elif randSwimsuit == 6 and under6Clover:
            $ redUnder = 6
        elif True:
            call redOutfitSet from _call_redOutfitSet_3
            pass
        "Clover returns from spending the day relaxing at the beach."
        if cloverMood <= 25:
            show red r4 at ri with d3
            y "Did you have a good time at the beach?"
            c "I guess so..."
            hide red with d3
        if 26 <= cloverMood <= 50:
            show red r4 at ri with d3
            y "Did you have a good time at the beach?"
            c "Yeah it wasn't bad, though my mind was elsewhere..."
            hide red with d3
        if 51 <= cloverMood <= 75:
            show red r1 at ri with d3
            y "Did you have a good time at the beach?"
            c "Yeah it was fun! I look so good in a swimsuit."
            hide red with d3
        if cloverMood >= 76:
            show red r1 at ri with d3
            y "Did you have a good time at the beach?"
            c "I did! I had a great time!"
            hide red with d3


    if redDayJob == 102:
        $ spy2Status = 0
        $ redDayJob = 0
        $ treatBag += 1
        play sound "audio/sfx/itemGot.mp3"
        "Clover brought home a Trick or Treat bag today. Check your ITEMS to see what's inside!"


    if redDayJob == 99:
        $ redDayJob = 0
        $ spy2Status = 0
        $ redChest = 0
        $ redBottom = 0
        $ redNeck = 0
        $ redHat = 0
        $ redShoes = 0
        if under4Clover:
            $ redUnder = 4
        if under5Clover:
            $ redUnder = 5
        if under6Clover:
            $ redUnder = 6
        show red r1 at ri with d3
        c "I'm back from Mathias' place."
        if gadgetJetpackActive == True:

            $ randMoney = renpy.random.randint(25, 40)
            $ cash += randMoney
            call missionRewardMoney from _call_missionRewardMoney_51
            hide red with d3
        elif task2Stage == 12.6:
            $ hackProgress = 100
            $ task2Stage = 13
            c r11 "........................"
            y "Well, how was it?"
            c r12 "I guess it wasn't {i}that{/i} bad."
            c "Mathias seemed surprise when I showed up. Apperantly he didn't think you were serious when you promised him a bikini model."
            y "I like to stick to my word......{w} sometimes."
            y "So how did his research go?"
            c r34 "Good actually. I ended up serving him soda's and chips in my bikini and he was more than happy to 'repay the favor'. So to speak."
            c "Anyways, he said that he had a breakthrough and that you should visit him tomorrow."
            y "I might just do that! Well done, Clover."
            c r37 "I... didn't actually do much, but thanks I guess."
            c "Not looking forward to doing it more often."
            hide red with d3
        elif True:
            y "How did it go?"
            $ randMathias = renpy.random.randint(1,3)
            if randMathias == 1:
                $ hackProgress += 6
                c r18 "Today he showed me his collection of figurines..."
                y "Oh boy, that must've been b-..."
                c r28 "It was so cool. He was talking really passionate about them too."
                y "Er... okay?"
                c r29 "He allowed me to borrow some of his comic books aswell."
                y "Since when are you into comics?"
                c r35 "{b}*Scoffs*{/b} I'm not, I'm just humoring him..."
                y "............"
                y "Did you two get {i}'any'{/i} work done today?"
                c "Erm... very little."
                y "............................."
                $ cellCloverComicsUnlock = True
            if randMathias == 2:
                $ hackProgress += 10
                c "It wasn't half bad. I walked around in my swimsuit, did some poses, showed off my butt."
                c "Mathias seemed more than pleased and made some decent progress today."
                y "All right, I might send you out again soon."
            if randMathias == 3:
                $ hackProgress += 16
                c "Mathias isn't that bad. He's kind of cute~..."
                y "Clover, focus."
                c "We got a lot of work done today and he's made great progress."
                y "That's what I like to hear."
            hide red with d3






    if month == 10 and 14 <= day <= 31 and yellowDayJob >= 1:
        $ randTreat = renpy.random.randint(1,4)
        if randTreat == 1:
            $ randTreat = 0
            $ treatBag += 1
            "Alex brought home a Trick or Treat bag today. Check your ITEMS to see what's inside!"
        elif True:
            pass


    if yellowDayJob == 1:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ yellowDayJob = 0
        $ acesRep += 1
        $ spy3Status = 0
        a "I'm back from working with the Aces."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Alex was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Here's my report."


        call missionRewardRep from _call_missionRewardRep_8


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_9
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_22
        if loreChanceReward == 10:
            $ acesLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_6

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Alex doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if acesRank <= 1:
                        if randRap == 1:
                            a "What does proletariat mean...?"
                            y "What?"
                            a "That's what they called me today. That I'm a proletariat."
                            y "Let me guess, and they called themselves the bourgeoisie?"
                            a "Yes! How did you know?"
                            y "I had a hunge..."
                        if randRap == 2:
                            a "I suggested we'd go to the candy store today!"
                            y "And how did that go?"
                            a "Everyone was down for it! I've had so much candy...!"
                            a "When I wanted to pay, they just laughed and pointed a gun at the cashier..."
                            a "That maybe wasn't so fun..."
                            a "I'm feeling a bit sick from all the candy, so I think I'm gonna lie down now..."
                        if randRap == 3:
                            a "You know the tattoo place at the mall? A few of the gang members were getting tattoos, but before we got there, a rival gang showed up."
                            a "They were acting all big and tough, but then I kicked one in the face and everyone was so surprised that we split up without anymore fighting."
                            a "It was fun! They treated me to milkshakes afterwards."
                        if randRap == 4:
                            a "Today we stole a diamond! They even gave me a piece of the profit!"
                            $ randMoney = 50
                            $ cash += 50
                            call missionRewardMoney from _call_missionRewardMoney_53
                            y "............."
                            y "They gave you 50 bucks for a diamond?"
                            a "I never said it was a big cut..."
                        if randRap == 5:
                            a "One of the Aces came on to me today."
                            a "He was kinda cute, but he wanted me to dye my hair red."
                            a "Red is not my color! He was really weird about it. I bet they love Sam."
                    if acesRank >= 2:
                        if randRap == 1:
                            a "Another day out fighting with the Aces! This time we got a big ol' truck and smashed it into a store window."
                            a "I quickly got out and began loading things into the truck, but they just laughed and told me to stop."
                            a "I don't think they were actually in it for the money... They just did it for fun..."
                        if randRap == 2:
                            a "Pretty much the same as always. We robbed some people and stole a car."
                            a "After a short joyride, they lost control over the wheel and landed in the water. I had to drag their dumb butts out of there before they drowned."
                            a "They acted like they planned to drive into the water all along. The Aces are jerks."
                        if randRap == 3:
                            a "I had to beat up an old man today..."
                            y "Woah, what?"
                            a "This old man came out and started yelling to the gangsters I was with. Saying that they were ruining this nice town."
                            a "Then the Aces told me to beat him up."
                            y "And did you....?"
                            a "Well... I had to stay undercover, so I pushed him to the group and whispered that I wasn't gonna hurt him."
                            a "I pretended to beat him up and he played along. Eventually he whispered that I should get out of the gang because I was too sweet of a girl."
                            a "I kinda agree... I don't like working for the Aces...."
                        if randRap == 4:
                            a "Not... much happened today. A truck pulled up with a bunch of unmarked boxes that I had to help move into a warehouse."
                            y "What was in them?"
                            a "I... don't know, we weren't allowed to check."
                            a "Something tells me we weren't suppose to have whatever was in those boxes. Let's hope it wasn't anything too bad."
                        if randRap == 5:
                            a "We got into a big fight today with a rival gang. Some of us got hurt. One was even shot."
                            a "We got him back to the marina and I think he will be okay, but it was scary for a moment."
                            a "......................"
                            y "Alex?"
                            a "He said that if he survived, he'd stop being a gangster and live an honest life..."
                            a "I hope he'll remember that."
            "Dismissed" if True:
                pass
        hide yellow
        hide scene_darkening
        with d2
        jump nextReport


    if yellowDayJob == 2:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ yellowDayJob = 0
        $ punkRep += 1
        $ spy3Status = 0
        a "I'm back from working with the Drift Punks."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Alex was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Here's my report."


        call missionRewardRep from _call_missionRewardRep_9


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_10
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_24
        if loreChanceReward == 10:
            $ punkLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_7

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Alex doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if punkRank <= 1:
                        if randRap == 1:
                            a "I tried playing some video games with the Drift Punk today, but I didn't really understand them..."
                            y "How come?"
                            a "It was as if they were speaking another language! Using words with DOTA, MMO and MOBA... I didn't really understand..."
                            y "Sounds like crazy talk to me."
                            a "I know, right?"
                        if randRap == 2:
                            a "I got to fly a drone today!"
                            a "The Punks are practising drone flying to scout areas without putting themselves in harm. I got to fly one, it was so cool!"
                            a "They gave me like a science-fiction space helmet so I could see through the eyes of the drone and it felt like I was flying!"
                            a "Afterwards I bought googly eyes for the drone and they loved it and put them on. I named him Herbert."
                        if randRap == 3:
                            a "Today was kind of spooky... They tested out some new mindcontrol weapons through music."
                            y "Mindcontrol?"
                            a "Yeah, like the nanobots. Anyone who listens to a song can be programmed to do something."
                            a "For now they were only testing fun stuff like forcing people to sing theme songs, but..."
                            a "Who knows what they'll do with it in the future..."
                        if randRap == 4:
                            a "Today we beat up some bad guys! Although technically the Drift Punks are the badguys aswell."
                            a "A rival gang tried to take some of the Punk's ground, so we scared them off and gave them a few bruises. Nothing too bad luckily."
                            a "The Punks have these cool pick-up trucks, modified to have their speakers on it. It's a fight and a party at the same time!"
                        if randRap == 5:
                            a "There was some big shot visiting today, but I didn't get to see them."
                            a "Instead I was stuck in the garage, cleaning the trucks! It was so boring! Just me and a few other college girls getting wet and soapy in our see-through white T-shirts..."
                            y "!!!"
                            y "{b}*Ahem*{/b} I'm going to need a 'full' report on this."
                            a "...?"
                    if punkRank >= 2:
                        if randRap == 1:
                            a "Sometimes I think Drift Punk is a little bit scary..."
                            a "They're all happy and parties one moment, and next moment they're these cold ruthless machines who do everything by calculated logic."
                            a "Today they robbed a store because they needed some extra money and they were so brutally effecient. They didn't even bring guns."
                            a "They just went in, forced the shop owner to the ground, tied him up, took the money and left. It took less than a minute."
                            a "I guess he wasn't hurt, but it was scary all the same."
                        if randRap == 2:
                            a "They were developing ways to drop bombs from drones today..."
                            y "That sounds... risky."
                            a "I managed to sabotage the test flight so they're going back to the drawing board, but I'm not sure if I want to gave these guys dropping bombs from the sky."
                            y "Agreed. Drift Punk certainly seems the have the other gangs beat in terms of technology. Let's hope we can keep them in check."
                        if randRap == 3:
                            a "I tried washing a harddrive today..."
                            y "Uh oh... Let me guess, they got mad at you."
                            a "........................."
                            a "It looked so dirty, I figured it was probably better off in the wash!"
                            a "I sorta deleted a guy's porn stash..."
                            y "Rest in Peace porndrive. I feel his pain."
                        if randRap == 4:
                            a "Pew pew pew!"
                            y "What are you doing?"
                            a "Lazers! The Punks have lazer guns now! And they go: pew pew pew!"
                            a "I didn't get to hold one, but I saw guys using them. They're cool...!"
                            y "Sounds like something to be worried about."
                            a "Well... all they do now is cause burn wounds. They're not actually strong enough to kill anyone yet."
                            a "So better they use lazers than normal guns, right?"
                            y "You have a point..."
                        if randRap == 5:
                            a "I don't like techno!"
                            y "Huh?"
                            a "Today the Drift Punk had a 'music education day'. Basically a giant rave party where they played loud techno music!"
                            a "The speakers were so loud, I can still feel the vibration. I don't think I'll be able to sleep tonight."
                            y "Better prepare for the dubstep education day then."
                            a "{b}*Whines*{/b}"
            "Dismissed" if True:
                pass
        hide yellow
        hide scene_darkening
        with d2
        jump nextReport



    if yellowDayJob == 3:
        if task4Stage == 5 and spy1Status == 0:
            jump task4
        if task4Stage == 6 and spy1Status == 0:
            jump task4
        if 1 <= task20Stage <= 3:
            jump task20
        if 1 <= task21Stage <= 3:
            jump task21
        if task21Stage == 5:
            jump task21
        if task25Stage == 1:
            jump task25
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ yellowDayJob = 0
        $ outsideRep += 3
        $ spy3Status = 0
        a "I'm back from working with the Outsiders."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Alex was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Here's my report."


        call missionRewardRep from _call_missionRewardRep_10


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_11
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_25
        if loreChanceReward == 10:
            $ outsidersLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_8

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Alex doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if outsideRank <= 1:
                        if randRap == 1:
                            a "They made me do all kinds of weird and scary things!"
                            y "Like what?"
                            a "Like read poetry and talk about how evil big businesses are!"
                            y ".................."
                            with hpunch
                            y "Boo!"
                            a "EEP!"
                            y "You scare easily, don't you."
                            a "{b}*Whines*{/b}"
                        if randRap == 2:
                            a "So I'm pretty sure there are no mummies in the Outsiders."
                            y "You don't say."
                            a "I saw a guy walk around in bandages, but apperantly he tried breaking in through a broken window and just cut himself all over."
                            y "That's what you get for trespassing... you get turned into a mummy. Head to your cell for now."
                        if randRap == 3:
                            a "You know the Outsiders are set up at a creepy abandoned amusement park, right?"
                            y "Yeah...?"
                            a "Someone thought it was a good idea to dress up as a creepy clown today to fit the theme."
                            a "Everyone was freaked out and he got his butt kicked for it, but that creepy clownmask is going to give me nightmares..."
                        if randRap == 4:
                            a "The Outsiders are kinda mean..."
                            a "They robbed an old man today. Saying he had way too much money anyways."
                            a "But if you take all of the money from a rich man, wouldn't that make him a poor man?"
                            a "If you take from the rich and give to the poor... doesn't that mean you need to give at least a little money back to him?"
                            y "You seem to forget that the Outsiders are criminals."
                            a "Oh right..."
                        if randRap == 5:
                            a "Ow my back hurts..."
                            y "Worked hard?"
                            a "Yeah they smuggled guns into the city and I had to help out carrying them."
                            y "More guns... as if we didn't have enough trouble to deal with."
                            a "Yeah, they were given out to their supplies and will probably hit the streets soon. We gotta be careful."
                    elif outsideRank == 2:
                        if randRap == 1:
                            a "We watched a horror movie today!"
                            y "Poor you."
                            a "Whadda ya mean? I love horror movies."
                            y "..........................."
                            y "You love horror movies?"
                            a "Yeah! I know they're not real so it's fine."
                            a "Real zombies and monsters on the other hand....."
                            y "Just.... Just go to your cell..."
                        if randRap == 2:
                            a "They gave me a big boring cookbook to read today..."
                            y "A cookbook?"
                            y "Wait... is it the Anarchist Cookbook?"
                            a "Hmm... yup, I think so."
                            y "Should've known. Get rid of it, we have enough trouble as it is. Don't need you creating explosives on top of it."
                        if randRap == 3:
                            a "The Outsiders are weird... We went out to a shopping street to hit in all the windows of the shops."
                            a "But then when we came across a homeless guy, they all gave him money and food."
                            a "I'm like... 'Make up your mind! Be a good guy or a bad guy!'"
                            y "In their eyes they're the good guys."
                            a "By smashing into shop windows...?"
                            y "Yeah you're right. They are weird."
                        if randRap == 4:
                            a "So I tried fitting in today by putting my hair down and looking all depressed and you know what they said...?"
                            y "They called you a poster?"
                            a "They called me a poser!"
                            a "Then I went up to one of the punk girls and asked her how to fit in, and she wanted to give me a mohawk haircut!"
                            a "Eventually I ended up with the skaters, but they don't even talk to you unless you can do a kickflip on your skateboard..."
                            y "Seems like a diverse bunch."
                            a "Tell me about it..."
                        if randRap == 5:
                            a "So I may give the Outsiders a hard time, but... I sorta begin to see where they're coming from."
                            a "A lot of them have been pushed around all their lives and told they didn't fit in. It's actually kinda sad..."
                            a "That doesn't excuse all their looting and vandalism of course! But I wonder how I would've grown up if everyone told me I was unwanted."
                    elif outsideRank == 3:
                        if randRap == 1:
                            a "I'm finally beginning to fit in! They're teaching me how to skateboard!"
                            a "They got so much money from their last haul that they bought some of the coolest skateboard out there. They gave me one of their old ones."
                            a "I still can't stay on it for more than 30 seconds, but I'm getting better! And they're don't point and laugh if I fall."
                            y "Beginning to find your role in the gang, huh?"
                            a "Yup!"
                        if randRap == 2:
                            a "You know... some of the things these guys say make sense."
                            y "Careful with that. Remember that they're the bad guys."
                            a "I know, but listen to this!"
                            a "The ones in power will always abuse that power. Therefor the common man needs to be able to arm themselves against tyranny!"
                            y "...................."
                            y "Alex, that's the Second Amendment. That's been around for hundreds of years."
                            a "Oh..."
                        if randRap == 3:
                            a "Hiya [playerName]! We did something good today!"
                            y "You did?"
                            a "Yup! We stopped a bully!"
                            a "We came across one of the Aces picking on someone in the streets."
                            a "Then we beat him up!"
                            y "..................."
                            y "How many were you with?"
                            a "Er... like... six of us. Why?"
                            y "So you ganged up with six people against one person. Are you sure {i}'you're'{/i} not the bully?"
                            a "Noooo, we're the Guardians of Justice! I think."
                            y "Call it what you want. At least you saved one innocent bystander."
                        if randRap == 4:
                            a "There are so many different groups within the Outsiders, it's hard to keep track of them all."
                            a "There's the skaters, the punks, the goth, the emos."
                            a "They're similar, but a little different in their own ways."
                            a "I really love the emo kids. I just wanna hug them! Of course they won't let me..."
                            a "We all have our differences, but we fight together as one, which is what I love about the gang."
                            a "Everyone is welcome and we don't fight for money and fame, but for equality!"
                        if randRap == 5:
                            a "We fought the Drift Punk today. We managed to ambush them and pull them off their trucks."
                            a "Then we hooked our own music up to their speakers and forced them to listen to it!"
                            a "Apperantly they didn't like skater music much and at the end we drove off in their cars. Went for a joyride."
                    elif outsideRank == 4:
                        if randRap == 1:
                            a "I may have been a little too positive about the Outsiders..."
                            a "Today they talked about setting off a bomb at the school and blaming it on another gang."
                            a "I was able to talk them out of it, I don't wanna see them turning into terrorists."
                        if randRap == 2:
                            a ".................."
                            y "Alex?"
                            a ".................."
                            y "Are you okay...?"
                            a "Yeah... I'm like... whatever."
                            y "I normally don't see you this down. Did something bad happen?"
                            a "No, I'm just trying to fit in more with the emo crowd or whatever...."
                            y "Oh..."
                            y "How's that working out for you?"
                            a "Not bad... they gave me some money to buy cigarettes...."
                            a "Here, you can have it or whatever..."
                            $ cash += 50
                            $ randomMoney = 50
                            call missionRewardMoney from _call_missionRewardMoney_54
                            y "............."
                            y "Can you act normal again now? I miss cheerful Alex."
                            a "Okay!"
                        if randRap == 3:
                            a "I asked where all the money went that we make off of these robberies."
                            a "It's going to... {i}'investors'{/i}."
                            y "Investores? That doesn't sound very Outsider-ish."
                            a "Apperantly there some big clothing brands out there that support the Outsiders, and we're feeding them money to help them grow and to show us in a positive light in the media."
                            a "They send us cool clothes and skateboards in return."
                            a "Plus, the Outsiders don't seem to value money much. They say too much money rots your soul."
                        if randRap == 4:
                            a "I found out where the Outsiders get all their guns. Apperantly there's a big junkyard dealer outside of Beverly Hills that smuggles them in."
                            a "Then afterwards the Aces smuggle them into the city."
                            a "Kids who needed to lie low and avoid the cops for a while used to go there. Which is how they got to know eachother."
                            a "I'm really worried about all the weapons being brought into the city though..."
                            y "We'll have to keep monitoring the situation. Make sure it doesn't get out of hand."
                            a "If it hasn't already..."
                        if randRap == 5:
                            a "Money money money!"
                            "Alex bursts in and hands you a large stack of cash."
                            y "Woah! Did you make all this today?!"
                            a "I sure made it!"
                            y "That's incredible, what did you have to do to make it?"
                            a "Work a printing press!"
                            y "You made all this money just working a printing pre-..."
                            y "................"
                            y "It's counterfeit money, isn't it?"
                            a "Yes! Whatever that means!"
                            y ".........................."
            "Dismissed" if True:
                pass
        hide yellow
        hide scene_darkening
        with d2
        jump nextReport


    if yellowDayJob == 4:
        $ spy3Status = 0
        if clubStage <= 3:
            $ yellowDayJob = 0
            $ clubStage += 1
            "Alex spent the day cleaning the milkshake bar and headed back to her cell."
            if clubStage >= 4:
                scene bgClub1
                with fade
                jump tutStage9
        elif True:

            if yellowDayJob == 4:
                $ yellowDayJob = 0
                call undressAlex from _call_undressAlex_23
                $ yellowChest = 2
                $ yellowBottom = 2
                $ yellowShoes = 2
                $ yellowHat = 2
                show scene_darkening with d3
                show yellow y1 at ri with d3
                a "I'm back from working at the milkshake bar."

                $ randMoney = renpy.random.randint(35, 50)

                if checkMark1 == True:
                    $ randMoney += 50
                if checkMark2 == True:
                    $ randMoney += 60
                if checkMark3 == True:
                    $ randMoney += 70
                if checkMark4 == True:
                    $ randMoney += 80
                if checkMark5 == True:
                    $ randMoney += 90
                if checkMark6 == True:
                    $ randMoney += 100

                $ randPenalty = renpy.random.randint(1, 3)
                if randPenalty == 3:
                    if 80 <= nanoLevelAlex <= 100:
                        $ randMoney = randMoney / 2
                        "There seems to be some money missing..."
                    if 60 <= nanoLevelAlex <= 79:
                        $ randMoney -= randMoney / 3
                        "There seems to be some money missing..."
                    if 40 <= nanoLevelAlex <= 59:
                        $ randMoney -= randMoney / 4
                        "There seems to be some money missing..."

                $ cash += randMoney
                call missionRewardMoney from _call_missionRewardMoney_88
                pause 0.2

            menu:
                "Tell me about your day" if True:
                    if slutLevel <= 1:
                        if randRap == 1:
                            a y42 "{size=-10}Milkshake for sale~....{/size}"
                            y "Alex...? What happened to your voice?"
                            a y4 "{size=-10}I've been on the corner all day yelling advertisement...{/size}"
                            a "{size=-10}I lost my voice...!{/size}"
                        elif randRap == 2:
                            a y28 "A customer offered me $200 dollars today if I took my top off."
                            y "Wow, nice!"
                            a y1 "I didn't of course."
                            y "..............."
                            y "Alex, why do you do this to me?"
                            a y28 "Nobody can see my nudies. Not even the doctor!"
                            y "Yes yes... go back to your cell, Alex..."
                        elif randRap == 3:
                            a y1 "I'm a barista!"
                            y "No you're not. You're a slutty milkshake waitress."
                            a y4 "B-but... someone ask me to make them a coffee today..."
                            y "It takes more than putting on a pot of coffee to be a barista, Alex."
                            a y5 "Oh..."
                        elif randRap == 4:
                            a y1 "I learned a new dance today! Want to see it?"
                            y "Sure why not."
                            "Alex gets in front of you and begins shaking her hips from left to right."
                            "Her hands touch and caresses her body and she uses her arms to push her breasts forward."
                            "It's very sexually provoking...!"
                            y "Wow Alex... I didn't know you could be this sexy!"
                            a y28 "{b}*Gasp*{/b}! It wasn't meant to be sexy! I thought it was cute...!"
                            y "Er... yes. Very cute indeed. Please keep doing it when there's customers around..."
                        elif randRap == 5:
                            a y1 "Can we get a kitten, [playerName]?"
                            y "No."
                            a y29 "But it'd be so cute to have a kitty walking around the bar!"
                            y "Also unhygienic. We're not getting a cat."
                            a y28 "{b}*Inhales*{/b}"
                            a y32 "...........!"
                            y "......................."
                            y "Alex... What are you doing?"
                            a ".................!"
                            y "Are you holding your breath...?"
                            a "{b}*Mpfh~....*{/b}"
                            y "Well.... good luck with that."
                            a y28 "{b}*Gasp* *Cough* *Cough*{/b}!"
                    if slutLevel == 2:
                        if randRap == 1:
                            a y28 "Aaaaaaaaah!"
                            y "Alex?! What's wrong?!"
                            a y29 "Look at this cute zombie girl!"
                            y "Zomb-... Alex, what are you talking about?!"
                            "Alex holds up a selfy with her and a very cute looking goth girl."
                            y "She does look like a zombie..."
                            a y42 "But she's so cute!"
                            y "And here you are thinking all zombies are scary."
                            a y20 "Well... maybe not all of them..."
                        elif randRap == 2:
                            a y1 "I fired a gun today!"
                            y "!!!"
                            y "Oh no... who got hurt?"
                            a "Oh no, I just shot it up in the air. Nobody got hurt."
                            y "And when the bullet came back down....?"
                            a y21 "Er... heh heh~... It might've seriously damaged the car of one of the Aces..."
                            y ".........."
                            y "Did he see who did it?"
                            a "I don't think so."
                            y "Good, we'll just blame it on gang violence then.{w} Oh and Alex? No more guns okay?"
                            a y20 "Fine..."
                        elif randRap == 3:
                            a y38 "{b}*Grumbles*{/b}"
                            y "Uh oh, is someone mopey?"
                            a "I feel like I'm getting the least tips out of all the girls..."
                            a y31 "Clover makes like ten times as much as I do!"
                            y "Yeah well that's cause Clover is a hopeless flirt and you think it's more important to discuss your favorite crayons with customers."
                            a y29 "There's nothing wrong with art!"
                            y "Try using that artistic expression to draw some naked ladies next. Maybe then you'll start getting tips."
                            a y32 "{b}*Grumbles*{/b}"
                        elif randRap == 4:
                            a y15 "Ugh... I feel sick~..."
                            y "You okay there Alex?"
                            a "I've had way too many milkshakes today..."
                            a "I'm going back to my cell..."
                            y "............"
                        elif randRap == 5:
                            a y1 "I got to play a little bit of guitar today."
                            a "One of the Drift Punk gangsters came by with his equipment and let me try it."
                            a y12 "It didn't get me any tips though..."
                            y "Next time play while naked. Trust me, you get tips then."
                            a y29 "Nooooo!"
                    if slutLevel == 3:
                        if randRap == 1:
                            label jump2me:
                                pass
                            a y22 "Hey [playerName]. You know that naughty thing we've been doing at night~...?"
                            y "The buttjobs, yes."
                            a "Look at what one of the guests taught me today."
                            hide alex
                            "Alex turns around and twerks her ass in front of you."
                            y "................"
                            show yellow y1 at ri with d3
                            a "I might do that for our next buttjob~... Whadda ya think?"
                            y "My mind is trying to process how someone as sweet and wholesome as you can sometimes be such a hot slut."
                            a y1 "Thanks! ... I think!"
                        elif randRap == 2:
                            a y8 "Slap my ass!"
                            y "..............."
                            y "Er... Why~...?"
                            a y22 "Don't you want to~...?"
                            y "Is this a trick? What are you getting at?!"
                            a y42 "C'mooon [playerName]~... slap iiiit~..."
                            y "Alex you're freaking me out. Go back to your cell!"
                            a y22 "Okaaaay~...."
                            hide yellow with d3
                            y "..............."
                            y "What the fuck was that all about...?!"
                        elif randRap == 3:
                            a y18 "One... two... three..."
                            y "What are you counting?"
                            a y1 "The coins I found underneath the vending machine."
                            a y29 "There's like 3 dollars here!"
                            y "Er..."
                            a y5 "I was hoping to buy a candy bar with it, but I know the mission is more important so... here..."
                            menu:
                                "Let her keep the 3 dollars" if True:
                                    y "Just go buy your candy bar Alex."
                                    a y1 "Yay!"
                                    $ alexMood += 2
                                    "Alex rushes off."
                                "Take the three dollars" if True:
                                    $ randMoney = 3
                                    $ cash += randMoney
                                    call missionRewardMoney from _call_missionRewardMoney_89
                                    y "Yeeessss~... more money for my treasure hoard...!"
                                    a y16 "You sound like a dragon...!"
                                    a y28 "You're not a dragon, right [playerName]...?"
                                    y "........"
                                    y "No Alex... I'm not a dragon."
                        elif randRap == 4:
                            hide yellow
                            $ yellowChest = 0
                            $ yellowArms = 4
                            show yellow at ri with d3
                            y "Alex... Where is your top?"
                            a y21 "................."
                            y "Alex...."
                            a y19 "It got stolen..."
                            y "Stolen?"
                            a y14 "I took it off during work because someone had spilled something on it and when I turned around for a moment, they stole it!"
                            a "I've been working all day, trying to keep my nudies hidden~...."
                            y "..........."
                            y "We have spare tops y'know."
                            a y29 "...!"
                        elif randRap == 5:
                            a y2 "I had a customer squeeze my boobs today."
                            a "But when others saw it, they wanted a squeeze aswell."
                            a y1 "I didn't get much work done today. I just got squeezed a lot."
                            y "Okay...?"
                            a "..............."
                            y "You're going to masturbate, aren't you?"
                            a y28 "Yes! I've been pend up all day!"
                    if slutLevel == 4:
                        if randRap == 1:
                            a y18 "The music playlist playing in the bar is getting a bit dull. Maybe we should find a new one."
                            y "Or maybe... {b}I{/b} should play live piano music! Like Billy Joel!"
                            a y1 "Do you play piano?"
                            y "Well... no..."
                            a y16 "Can you sing?"
                            y "No..."
                            a y3 "Let's just stick to a playlist, piano man."
                            y "Okay..."
                        elif randRap == 2:
                            a y1 "Hey I was thinking. How about we do 'theme' nights?"
                            a "Like a cartoon theme where everybody has to dress up like sexy cartoon characters."
                            y "Sexy cartoon characters...?"
                            y "How many cartoons do you know that have sexy characters in them...?"
                            a y23 "Oh you'd be surprised."
                        elif randRap == 3:
                            a y42 "I don't like this idea! Not at all!"
                            y "...?"
                            a "My butt feels like it's on fire!"
                            y "I have no honest idea of what you're talking about."
                            a y21 "The spank paddles. There's a paddle at every table!"
                            a y20 "My butt hurts..."
                            y "Although I wholeheartedly approve, it wasn't one of my ideas."
                            y "Someone must've snuck them into the bar as a prank."
                            a y28 "Those jerks...!"
                        elif randRap == 4:
                            a y18 "I had a customer today pay extra if I served him his drink in my bare feet."
                            y "What?"
                            a y1 "He has a thing for feet I guess."
                            y "Is it even possible to have a fetish for feet...?"
                            a "Oh yes. It's quite common actually."
                            y "It's unhygienic, is what it is!{w} Tell me you kicked him out."
                            a y30 "Er.. I did what he asked. Here's the tip he left."
                            $ randMoney = 70
                            $ cash += randMoney
                            call missionRewardMoney from _call_missionRewardMoney_90
                            y "That's a lot of money..."
                            y "Okay I changed my mind! Carry on walking around bare footed."
                        elif randRap == 5:
                            if slutPublic >= 5:
                                a y41 "I had a customer ask me if I could turn my boobs into snow covered mountains today."
                                y "Snow covered mountains?"
                                a "I didn't get it at first either,but he just wanted to cover my naked tits in whipped cream while I lay on his table."
                                a y1 "Then he and his friend licked me clean! Which was very throughful of them."
                                y "Fine, but next time when they suggest 'cave diving' you say no."
                                a y29 "O-oh...! Okay!"
                            elif True:
                                a "Just an average day today. Not much happened."
                    if slutLevel >= 5:
                        if randRap == 1:
                            hide yellow
                            $ yellowArms = 2
                            call undressAlex from _call_undressAlex_24
                            show yellow y1 at ri with d3
                            a y1 "I got tips!"
                            $ randMoney = 70
                            $ cash += randMoney
                            call missionRewardMoney from _call_missionRewardMoney_91
                            y "Nice. How'd you get these?"
                            a "Oh my uniform was still wet from the wash, so I worked in the nude all day."
                            y "................."
                            y "Yeah okay, that would explain it. What ever happened to not showing off your nudies?"
                            a y11 "Oh that. Well I sorta gave up on that rule after we started fucking like rabbits."
                            a y28 "{b}*Gasp*{/b}! Maybe I should start banging customers next!"
                            y "And be too exausted to do any actual work? I think not missy!"
                            a y4 "Aww..."
                        elif randRap == 2:
                            a y1 "I won!"
                            y "You won?"
                            a "In a tit measuring competition! A bunch of gangsters came in with their girlfriends and we were dared to see who had the biggest rack."
                            a y13 "I am proud to say I was the most mature woman there."
                            y "Mature is not the right word... I'd use {i}'developed'{/i}."
                            a y3 "From now on I'm going to challenge any girl I see to a tit measuring competition!"
                            y "................"
                            y "I have no objections."
                        elif randRap == 3:
                            a y18 "Sometimes I worry that all I think about is sex lately..."
                            y "That's a good thing. Don't want your nanobot acting up again."
                            a y5 "But I miss the time I dreamt of puppies, flowers and rainbows! Now all I daydream about is dick!"
                            a "Morning cereal? Dick."
                            a "Wiping tables? Big dick."
                            a y29 "Taking out the trash? Double penetration!"
                            y "........................."
                            a "I used to get angry when customers wiped out their dicks. Now it makes my heart beat faster!"
                            y "Okay okay, calm down. You're reaching a new stage in your life.... Like puberty!"
                            a y28 "Second puberty?"
                            y "Yup. I call it slutery. It's when you realise you love nothing more than being a cockwarmer and sucking dicks."
                            a y20 "Oh..."
                            a y28 "WAIT! Does that mean my boobs are going to grow even bigger, like in the last puberty?!"
                            y "One can only hope Alex."
                        elif randRap == 4:
                            a y1 "Today a customer asked how many cherries I could fit up my ass..."
                            y "Jesus... why do we get so many crazy customers? What did you tell him?"
                            a "I asked him if he wanted to find out!"
                            y "................."
                            a y18 "However before we did anything he got kicked out by the other staff for being a creep."
                            y "I'll buy you some anal beats instead if you really want to finding out."
                        elif randRap == 5:
                            a y1 "Just a boring day really. Nothing happened."
                            y "Nothing sexy?"
                            a "Nope."
                            y "Nothing crazy?"
                            a "No, nothing."
                            y "Huh..."
                            a y2 "It's nice to have a normal day once in a while!"
                "Dismissed" if True:
                    pass
            hide scene_darkening
            hide yellow
            with d2
            call yellowOutfitSet from _call_yellowOutfitSet_6


    if yellowDayJob == 5:
        $ coverCounter += 2
        $ cash += randMoney
        $ intel += randIntel
        $ yellowDayJob = 0
        $ spy3Status = 0
        a "I'm back from working with Les Epines."
        if landgrabTimer == 31:
            $ randInjury = renpy.random.randint(1, 2)
            if randInjury == 1:
                "Alex was hurt during the landgrab! Best give her some time to recover."
            elif True:
                pass
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Here's my report."


        if randIntel >= 1:
            call missionRewardInt from _call_missionRewardInt_14
        if moneyChanceReward == 2:
            call missionRewardMoney from _call_missionRewardMoney_41

        if loreChanceReward == 10:
            $ epinesLoreUnlock += 1
            call missionRewardLore from _call_missionRewardLore_11

        if injectChanceReward >= 7:
            $ injectorSmall += 1
            call missionRewardItem from _call_missionRewardItem_15
            $ injectChanceReward = 0

        $ randHerbChance = renpy.random.randint(1, 8)
        if randHerbChance >= 2:
            call missionRewardItem from _call_missionRewardItem_2
            $ randHerb = renpy.random.randint(1, 6)
            if randHerb == 1:
                $ herbHeal += 1
            if randHerb == 2:
                $ herbAphro += 1
            if randHerb == 3:
                $ herbWeed += 1
            if randHerb == 4:
                $ herbMutant += 1
            if randHerb == 5:
                $ herbGold += 1
            if randHerb == 6:
                $ herbWhisper += 1

        menu:
            "Tell me about your day" if True:
                if landgrabTimer >= 31:
                    "Alex doesn't feel like talking about her day and returns to her cell."
                elif True:
                    if randRap == 1:
                        a y42 "Ew ew ew ew!"
                        a "I walked into a spiderweb today!"
                        a y4 "Silva ensured me I didn't have any spiders on me, but I still got all creeped out!"
                    if randRap == 2:
                        a y4 "I got stung today..."
                        y "Uh oh... Something bad?"
                        a y29 "Well... the plant is suppose to kill me within 24 hours."
                        y "!!!"
                        a y1 "But luckily Silva had the antidote so we're all good!"
                        y "....................."
                    if randRap == 3:
                        a y1 "I danced in the flowers today!"
                        y "You frolicked?"
                        a y18 "Wha...?"
                        y "You frolicked in the flowers...?"
                        a y19 "I don't know what that words means..."
                        y "....................."
                        y "It means to dance."
                        a y1 "Oh! Then yes I did!"
                    if randRap == 4:
                        a y1 "I think my favorite flowers are daffodils."
                        y "How so?"
                        a y29 "Cause they're yellow! Just like my spy suit!"
                    if randRap == 5:
                        a y1 "Here you go [playerName]!"
                        "Alex hands you a flower."
                        y "Oh a sunflower. That's kind of you Alex."
                        a y29 "It's not a sunflower... It's a Blacked-eyed Susan."
                        y "................."
                        y "What is this? A domestic abuse flower?"
                        a y28 "No! Black-eyed Susans stand for Justice in flower language!"
                        y "I didn't know that. Thank you Alex... I also didn't know I needed to know that."
            "Dismissed" if True:
                pass
        hide yellow
        hide scene_darkening
        with d2
        jump nextReport



    if yellowDayJob == 6:
        $ coverCounter += 10
        $ yellowDayJob = 0
        $ spy3Status = 0
        $ randMoney = renpy.random.randint(150, 250)
        a "I'm back from robbing a store."

        $ cash += randMoney
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Our notoriety went up a lot. This is all they had in the cash register..."
        call missionRewardMoney from _call_missionRewardMoney_26
        hide yellow
        hide scene_darkening
        with d2

    if yellowDayJob == 7:
        $ coverCounter += 8
        $ yellowDayJob = 0
        $ spy3Status = 0
        a "I'm back from setting fire to things."
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Our notoriety went up quite a bit."
        hide yellow
        hide scene_darkening
        with d2

    if yellowDayJob == 8:
        $ coverCounter += 6
        $ yellowDayJob = 0
        $ spy3Status = 0
        $ randMoney = renpy.random.randint(20, 60)
        a "I'm back from pickpocketing."

        $ cash += randMoney
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a y19 "Our notoriety went up a bit. After all the pockets were emptied, I made this much..."
        call missionRewardMoney from _call_missionRewardMoney_27
        hide yellow
        hide scene_darkening
        with d2

    if yellowDayJob == 9:
        $ coverCounter += 5
        $ yellowDayJob = 0
        $ spy3Status = 0
        a "I'm back from spraypainting the mall."
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Our notoriety went up a little bit."
        hide yellow
        hide scene_darkening
        with d2

    if yellowDayJob == 10:
        $ coverCounter += 10
        $ yellowDayJob = 0
        $ spy3Status = 0
        $ randMoney = renpy.random.randint(100, 200)
        a "I'm back from stealing cars."

        $ cash += randMoney
        show scene_darkening
        with d3
        show yellow y38 at ri with d3
        a "Our notoriety went up a lot. And I made some money..."
        call missionRewardMoney from _call_missionRewardMoney_37
        hide yellow
        hide scene_darkening
        with d2

    if yellowDayJob == 11:
        if capturedAgents >= 1:
            $ capturedAgents -= 1
            $ freedAgents += 1
        $ yellowDayJob = 0
        $ spy3Status = 0
        $ yellowChest = 0
        $ yellowBottom = 0
        $ yellowArms = 2
        $ yellowUnder = 0
        show yellow at ri with d3
        a y19 "Just another boring day showing off my bewbs..."
        a y1 "At least I helped break some nanobot control."
        hide yellow with d3
        $ yellowArms = 1
        $ yellowChest = yellowChestSet
        $ yellowBottom = yellowBottomSet



    if yellowDayJob == 99:
        $ alexDayJob = 0
        $ spy3Status = 0
        $ yellowChest = 0
        $ yellowBottom = 0
        $ yellowNeck = 0
        $ yellowHat = 0
        $ yellowShoes = 0
        if under4Alex:
            $ alexUnder = 4
        if under5Alex:
            $ alexUnder = 5
        if under6Alex:
            $ alexUnder = 6
        show scene_darkening with d3
        show yellow y1 at ri with d3
        a "I'm back from Mathias' place."
        if gadgetJetpackActive == True:

            $ randMoney = renpy.random.randint(25, 40)
            $ cash += randMoney
            call missionRewardMoney from _call_missionRewardMoney_55
            hide yellow with d3
        elif task2Stage == 12.6:
            $ hackProgress = 100
            $ task2Stage = 13
            a y11 "........................"
            y "Well, how was it?"
            a y12 "I guess it wasn't {i}that{/i} bad."
            a "Mathias seemed surprise when I showed up. Apperantly he didn't think you were serious when you promised him a bikini model."
            y "I like to stick to my word......{w} sometimes."
            y "So how did his research go?"
            a y34 "Good actually. I ended up serving him soda's and chips in my bikini and he was more than happy to 'repay the favor'. So to speak."
            a "Anyways, he said that he had a breakthrough and that you should visit him tomorrow."
            y "I might just do that! Well done, Alex."
            a y37 "I... didn't actually do much, but thanks I guess."
            a "Not looking forward to doing it more often."
            hide yellow with d3
        elif True:
            y "How did it go?"
            $ randMathias = renpy.random.randint(1,3)
            if randMathias == 1:
                $ hackProgress += 5
                a y5 "................."
                a "Well it was a little awkward..."
                a "I didn't know exactly what to do and he didn't know either."
                a y1 "I went home early and got a smoothie!"
                y "......................................."
            if randMathias == 2:
                $ hackProgress += 9
                a "It went pretty good, I think! I went to get a swim cause... you know I'm already in my swimsuit."
                a "Then when I came back he suddenly got inspiration and continued working. He's made some decent progress today."
            if randMathias == 3:
                $ hackProgress += 15
                a "It went really well! I just practised my dancing while I was there which seemed to give him the motivation he needed to get to work!"
                a "He said he got a lot done today."
            hide yellow
            hide scene_darkening
            with d3


    if yellowDayJob == 100:
        $ yellowDayJob = 0
        $ spy3Status = 0
        "Alex returns from spending the day relaxing at the mall."


    if yellowDayJob == 101:
        $ spy3Status = 0
        $ yellowDayJob = 0
        $ yellowChest = 0
        $ yellowBottom = 0
        $ yellowShoes = 0
        $ randSwimsuit = renpy.random.choice([4, 5, 6])
        if randSwimsuit == 4 and under4Alex:
            $ yellowUnder = 4
        elif randSwimsuit == 5 and under5Alex:
            $ yellowUnder = 5
        elif randSwimsuit == 6 and under6Alex:
            $ yellowUnder = 6
        elif True:
            call yellowOutfitSet from _call_yellowOutfitSet_1
            pass
        "Alex returns from spending the day relaxing at the beach."
        if cloverMood <= 25:
            show yellow y4 at ri with d3
            y "Did you have a good time at the beach?"
            a "Hmm... I guess it wasn't so bad..."
            hide yellow with d3
        if 26 <= cloverMood <= 50:
            show yellow y5 at ri with d3
            y "Did you have a good time at the beach?"
            a "It's hard to keep my mind off of things, but.... I guess I had a good time."
            hide yellow with d3
        if 51 <= cloverMood <= 75:
            show yellow y1 at ri with d3
            y "Did you have a good time at the beach?"
            a "Yes, I went for a swim!"
            hide yellow with d3
        if cloverMood >= 76:
            show yellow y1 at ri with d3
            y "Did you have a good time at the beach?"
            a "It was the best day ever! I built a sandcastle and got icecream!"
            hide yellow with d3


    if yellowDayJob == 102:
        $ spy3Status = 0
        $ yellowDayJob = 0
        $ treatBag += 1
        play sound "audio/sfx/itemGot.mp3"
        "Alex brought home a Trick or Treat bag today. Check your ITEMS to see what's inside!"





    if hiredStaff >= 1 and dailyStaffReport == False and landgrabTimer <= 29:
        $ dailyStaffReport = True
        $ staffMoney = hiredStaff * 30

        $ cash += staffMoney
        $ randMoney = staffMoney
        call missionRewardMoney from _call_missionRewardMoney_70
        $ staffMoney = 0





    if greenArms != 1:
        $ greenArms = 1
    if redArms != 1:
        $ redArms = 1
    if yellowArms != 1:
        $ yellowArms = 1





    if acesRep >= 18 and task3Stage == 0:
        $ task3Stage = 1

    if task3Stage == 3:
        jump task3


    if task3Stage == 5:
        jump task3


    if task9Stage == 1:
        jump task9
    if task9Stage == 3:
        jump task9

    if task10Stage == 1:
        jump task10

    if task11Stage == 1:
        jump task11
    if task11Stage == 3:
        jump task11

    if task12Stage == 1:
        jump task12

    if 7 <= task3Stage <= 8 and firstLandgrab and acesStrength <= 45:
        $ task3Stage = 9
        jump task3

    if task16Stage == 1:
        $ task16Stage = 2

    if task30Stage == 2:
        jump task30

    if task25Stage == 9:
        jump task25

    if task26Stage == 9 and britCaptured:
        jump task26


jump base

default daysTillMissle = 30
default finaleAirportDef = 80
label jobReportFinale:
    $ tod = 2
    scene black with fade
    scene bgBase with fade
    pause 0.5
    if task26Stage == 21:
        if spy0Status == 1:
            $ finaleAirportDef -= 20
            $ spy0Status = 0
            "Agent O5O came home from assaulting the airport."
        if spy4Status == 1:
            $ finaleAirportDef -= 20
            $ spy4Status = 0
            "Britney came home from assaulting the airport."
        if spy5Status == 1:
            $ finaleAirportDef -= 20
            $ spy5Status = 0
            "Kim came home from assaulting the airport."
        if spy6Status == 1:
            $ finaleAirportDef -= 20
            $ spy6Status = 0
            "Silva came home from assaulting the airport."
        "The airport defenses are now at [finaleAirportDef]%%"
        if finaleAirportDef <= 0:
            jump task26
        elif True:
            jump base
    if 26 <= task26Stage <= 29:
        $ spy1Status = 0
        $ spy2Status = 0
        $ spy3Status = 0
        jump base
    elif True:
        stop music fadeout 3.0
        hide screen mapButtonsRaidFinale
        scene black with fade
        scene bgBasement with fade
        show scene_darkening with d3
        play music "audio/music/nighttime.mp3" fadein 2.0
        if spy0Status == 1:
            $ spy0Status = 0
            show O5O at ri with d3
            $ findKeyMember = renpy.random.randint(1,3)
            if findKeyMember == 1:
                if spy5Status == -1 and task30Stage >= 3:
                    $ spy5Status = 0
                    O5O "YOU ARE GOING TO BE SO PROUD OF ME!"
                    O5O "LOOK WHO I FOUND!"
                    show kim:
                        xalign 0.5 yalign 0.0 zoom 0.9
                    with d3
                    kim "Hey Boss!"
                    y "Kim! Man, am I glad to see you!"
                    kim "Quite the situation you got us in, I'm charging overtime for this."
                    y "......................"
                    kim "Just kidding boss... It's good to see you again aswell.{w} So what's the sitch?"
                    y "We're searching for Mathias. Can you help out?"
                    kim "Oooh Clover's boyfriend?"
                    y "..................."
                    y "Not her boyfriend."
                    kim "Eh... whatever. I ship it."
                    hide kim
                    hide O5O
                    with d3
                    play sound "audio/sfx/itemGot.mp3"
                    "Kim was found! She can now help in the search."
                elif spy6Status == -1 and socialSilva >= 12:
                    $ spy6Status = 0
                    O5O "I BROUGHT BACK A LITTLE FLOWER TODAY!"
                    y "A little flow-..."
                    show silvaModel:
                        xalign 0.5 yalign 0.0 zoom 0.9
                    with d3
                    y "Silva!"
                    sil "Bonjour mon ami. I am glad to zee you alive."
                    y "How did you manage to escape capture?"
                    sil "Oh I hid in ze jungle I created. Luckily you found me before WOOHP did."
                    sil "I was briefed on the way. I zhall 'elp you find Mathias!"
                    hide silvaModel
                    hide britney
                    hide O5O
                    with d3
                    play sound "audio/sfx/itemGot.mp3"
                    "Silva Abegail was found! She can now help in the search."
                elif True:
                    O5O "LOOK WHO I FOUND!"

                    jump task26
            if findKeyMember == 2:
                O5O "NO ONE IN SIGHT, SIR!"
                O5O "BUT I DID FIND THIS LYING ON THE FLOOR."
                play sound "audio/sfx/itemGot.mp3"
                $ matsDust += 3
                "Agent O5O hands you {color=#ffeda6}Saltpeter{/color} x3."
                hide O5O with d3
            if findKeyMember == 3:
                O5O "I DIDN'T FIND ANYONE IMPORTANT..."
                O5O "HOWEVER I CAME ACROSS THIS WHILE EXPLORING!"
                play sound "audio/sfx/itemGot.mp3"
                $ matsGlue += 3
                "Agent O5O hands you {color=#ffeda6}Cooling Agent{/color} x3."
                hide O5O with d3
            if findKeyMember == 4:
                O5O "NO ONE SIGHTED! WHERE EVER THEY'RE HIDING, THEY'RE GOOD!"
                O5O "I'LL CONTINUE SEARCHING AGAIN TOMORROW!"
                hide O5O with d3

        if spy4Status == 1:
            $ spy4Status = 0
            show britney at ri with d3
            $ findKeyMember = renpy.random.randint(1,3)
            if findKeyMember == 1:
                if spy5Status == -1 and task30Stage >= 3:
                    $ spy5Status = 0
                    brit "Here's someone you'll recognize. I found them hiding in the streets."
                    show kim:
                        xalign 0.5 yalign 0.0 zoom 0.9
                    with d3
                    kim "Hey Boss!"
                    y "Kim! Man, am I glad to see you!"
                    kim "Quite the situation you got us in, I'm charging overtime for this."
                    y "......................"
                    kim "Just kidding boss... It's good to see you again aswell.{w} So what's the sitch?"
                    y "We're searching for Mathias. Can you help out?"
                    kim "Oooh Clover boyfriend?"
                    y "..................."
                    y "Not her boyfriend."
                    kim "Eh... whatever. I ship it."
                    hide kim
                    hide britney
                    with d3
                    play sound "audio/sfx/itemGot.mp3"
                    "Kim was found! She can now help in the search."
                elif spy6Status == -1 and socialSilva >= 12:
                    $ spy6Status = 0
                    brit "Found someone important today!"
                    show silvaModel:
                        xalign 0.5 yalign 0.0 zoom 0.9
                    with d3
                    y "Silva!"
                    sil "Bonjour mon ami. I am glad to zee you alive."
                    y "How did you manage to escape capture?"
                    sil "Oh I hid in ze jungle I created. Luckily you found me before WOOHP did."
                    sil "I was briefed on the way. I zhall 'elp you find Mathias!"
                    hide silvaModel
                    hide O5O
                    hide britney
                    with d3
                    play sound "audio/sfx/itemGot.mp3"
                    "Silva Abegail was found! She can now help in the search."
                elif True:
                    brit "Found him!"

                    jump task26
            if findKeyMember == 2:
                brit "I spent the day searching... no luck so far."
                brit "I came across this lying on the street though. Maybe it'll be useful."
                play sound "audio/sfx/itemGot.mp3"
                $ matsWires += 1
                "Britney hands you {color=#ffeda6}Wiring Kit{/color} x1."
                hide britney with d3
            if findKeyMember == 3:
                brit "Couldn't find anyone important today."
                brit "I'll try again tomorrow. In the meantime, I found this. Maybe it'll be useful."
                play sound "audio/sfx/itemGot.mp3"
                $ matsGlue += 2
                "Britney hands you {color=#ffeda6}Cooling Agent{/color} x2."
                hide britney with d3
            if findKeyMember == 4:
                brit "I didn't find anyone who could help us today."
                brit "Fingers crossed we'll have better luck tomorrow."
                hide britney with d3

        if spy5Status == 1:
            $ spy5Status = 0
            show kim at ri with d3
            $ findKeyMember = renpy.random.randint(1,3)
            if findKeyMember == 1:
                if spy6Status == -1 and socialSilva >= 12:
                    $ spy6Status = 0
                    kim "I found someone really important today!"
                    y "You did?"
                    show silvaModel:
                        xalign 0.5 yalign 0.0 zoom 0.9
                    with d3
                    y "Silva!"
                    sil "Bonjour mon ami. I am glad to zee you alive."
                    y "How did you manage to escape capture?"
                    sil "Oh I hid in ze jungle I created. Luckily you found me before WOOHP did."
                    sil "I was briefed on the way. I zhall 'elp you find Mathias!"
                    hide silvaModel
                    hide britney
                    hide O5O
                    with d3
                    play sound "audio/sfx/itemGot.mp3"
                    "Silva Abegail was found! She can now help in the search."
                    hide kim with d3
                elif True:
                    kim "Look who I found! And this is why you're paying me the big bucks...!"

                    jump task26
            if findKeyMember == 2:
                kim "I went around the place, but didn't find anyone out and about."
                kim "This will probably help though."
                play sound "audio/sfx/itemGot.mp3"
                $ matsValu += 1
                "Kim hands you {color=#ffeda6}Valuables{/color} x1."
                hide kim with d3
            if findKeyMember == 3:
                kim "I spent most of the day dodging WOOHP patrols. Didn't find anyone."
                kim "I did come across a box full of this. Hope that's useful."
                play sound "audio/sfx/itemGot.mp3"
                $ matsChip += 3
                "Kim hands you {color=#ffeda6}Computer Chip{/color} x3."
                hide kim with d3
            if findKeyMember == 4:
                kim "No luck today boss."
                kim "The streets are crawling with WOOHP agents. I'll try again tomorrow."
                hide kim with d3

        if spy6Status == 1:
            $ spy6Status = 0
            show silvaModel at ri with d3
            $ findKeyMember = renpy.random.randint(1,3)
            if findKeyMember == 1:
                sil "I found 'im!"

                jump task26
            if findKeyMember == 2:
                sil "He iz zo sneaky. No sign of Mathias."
                sil "I found a whole box of theze though...."
                play sound "audio/sfx/itemGot.mp3"
                $ matsDust += 5
                "Sil hands you {color=#ffeda6}Valuables{/color} x5"
                hide silvaModel with d3
            if findKeyMember == 3:
                sil "I nearly got caught! Thoze WOOHP agents are everywhere!"
                sil "I managed to pickpocket one of zhem though~..."
                play sound "audio/sfx/itemGot.mp3"
                $ cash += 500
                "Silva hands you {color=#ffeda6}$500{/color}."
                hide silvaModel with d3
            if findKeyMember == 4:
                sil "I have failed you mon ami... I searched and searched, but no Mathias in sight..."
                sil "I zhall try again tomorrow!"
                hide silvaModel with d3

    label finaleNightCycle:
        pass
    hide scene_darkening with d3
    scene black with fade
    show text _("Despite the chaos, you manage to get some rest.")
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
    if daysTillMissle <= 0:
        $ daysTillMissle = 30
        pause 0.5
        ".............................................."
        "Due to... {i}'difficulty issues'{/i} the launch has been delayed."
        y "......."
    call screen mapButtonsRaidFinale


label jobReportFinale2:
    hide scene_darkening with d3
    stop music fadeout 3.0
    scene black with fade
    show text _("Despite the chaos, you manage to get some rest.")
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
    $ tod = 1
    "DAYS UNTIL MISSILE LAUNCH: [daysTillMissle]."
    if daysTillMissle <= 0:
        $ daysTillMissle = 30
        pause 0.5
        ".............................................."
        "Due to... {i}'difficulty issues'{/i} the launch has been delayed."
        y "......."
    call screen mapButtonsRaidFinale
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
