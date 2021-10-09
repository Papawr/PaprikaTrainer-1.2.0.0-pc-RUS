

label spyCameraGreen:
    $ spyRoomRand = 0
    if tutorialActive and tutStage == 3:
        if activeSpy == 1:
            "You tune in to see what [greenName] is up to."
            hide screen spyScreens
            scene black with fade
            scene bgSideroom
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[greenName] is currently located at the safehouse. She is standing in the sideroom, waiting for you to help her clean up."
        if activeSpy == 2:
            "You tune in to see what [redName] is up to."
            hide screen spyScreens
            scene black with fade
            scene bgSideroom
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[redName] is currently located at the safehouse. She is standing in the sideroom, waiting for you to help her clean up."
        if activeSpy == 3:
            "You tune in to see what [yellowName] is up to."
            hide screen spyScreens
            scene black with fade
            scene bgSideroom
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[yellowName] is currently located at the safehouse. She is standing in the sideroom, waiting for you to help her clean up."
        hide green
        hide red
        hide yellow
        scene black
        with d5
        jump tutBase
    if tutorialActive and tutStage == 5:
        if activeSpy == 1:
            "You tune in to see what [greenName] is up to."
            hide screen spyScreens
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[greenName] is currently located at the safehouse. She is standing in the main room next to you.."
            s "What are you doing....?"
            y "Nothing!"
        if activeSpy == 2:
            "You tune in to see what [redName] is up to."
            hide screen spyScreens
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[redName] is currently located at the safehouse. She is standing in the main room next to you.."
            c "What are you doing....?"
            y "Nothing!"
        if activeSpy == 3:
            "You tune in to see what [greenName] is up to."
            hide screen spyScreens
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[yellowName] is currently located at the safehouse. She is standing in the main room next to you.."
            a "What are you doing....?"
            y "Nothing!"
        hide green
        hide red
        hide green
        scene black
        with d5
        jump tutBase
    if tutStage == 11:
        $ tutStage = 12
        $ samUnder = 1
        scene cellSam
        show scene_camera
        with d3
        hide scene_camera
        show green g11 at ri with d3
        show scene_camera
        with d3
        s ".............."
        s "Well Sam... You secretly always wanted to be a black widow operative..."
        s "I guess that time starts now. You just gotta be brave and show a bit more of yourself."
        s ".................."
        s g2 "Y-yeah... I could be a sex bomb!"
        s "Seduce men into giving up their valuable information. Sleeping with super spies who drink their martini's shaken, not stirred!"
        s g11 "................."
        s g14 "Oh who am I kidding..."
        hide green
        scene black
        hide scene_camera
        with d3
        scene bgBase
        with fade
        jump base
    if task2Stage == 10:
        scene cellSam
        $ greenOutfit = 0
        $ greenOutfitArms = 0
        $ greenChest = 0
        $ greenBottom = 0
        $ greenUnder = 1
        show green g4 at ri with d3
        show scene_camera
        with d3
        s "Well.... that was one of the most embarrassing days of my life..."
        s "At least I got to safe a little of my dignity...{w} Nobody saw me in my underwear."
        s g15 "Although I feel like it's only a matter of time before that happens...."
        scene black
        hide green
        hide scene_camera
        with fade
        $ greenChest = 1
        $ greenNeck = 1
        $ greenBottom = 1
        $ greenShoes = 1
        scene bgBase with fade
        jump base
    if task2Stage == 15:
        scene cellSam
        $ greenOutfit = 0
        $ greenOutfitArms = 0
        $ greenUnder = 1
        show green g4 at ri
        show scene_camera
        with d3
        s "Okay... don't worry Sam. This might all be new for you, but a lot of girls have toys like this. It's no big deal..."
        s "......................."
        menu:
            "Turn on V.I.B." if True:
                play sound "audio/sfx/vib.mp3"
                s g28 "{b}*Yelps*{/b}"
                s "[playerName]!!"
            "Never mind" if True:
                pass
        hide green
        hide scene_camera
        scene bgBase
        with d3
        jump base
    if task4Stage == 4:
        scene cellAlex
        show red r4 at ri
        show green at ce
        show yellow at le
        show scene_camera
        with d3
        c "So about the kiss..."
        a "Yeah you went all out, didn't you. Full tongue and everything!"
        c "Heh heh heh....{w}........"
        s "We thought you were still under nanobot control. It er... worked in the past."
        a "Oh."
        a "..........................."
        a "Wait, it worked in the past?"
        c "You know what! That's a long and awkward story, let's skip over that part!"
        a "No, now I wanna know...!!!"
        scene bgBase
        hide red r4 at ri
        hide green at ce
        hide yellow at le
        hide scene_camera
        with d3
        jump base
    if samSpySex == 2:
        $ sexScene = 1
        "You tune in to see what Sam is up to."
        scene black with fade
        $ sexScene = 2
        jump samSex2
    elif True:
        if spy1Status == 10:
            "Sam isn't at the base at the moment."
            jump base
        $ randSpy = renpy.random.randint(1,4)
        if slutLevel <= 1:
            if randSpy == 1:
                scene cellSam
                show green g38 at ri
                show scene_camera
                with d3
                pause 0.5
                s "I still can't believe that teacher gave me a D-minus for that last test."
                s "Next time I see him I'll tell him his dick is a D-minus!"
                s g15 "..............................."
                s g19 "{b}*Sighs*{/b} No you won't Sam, you're too much of a little goody-two-shoes for that..."
            if randSpy == 2:
                scene cellSam
                show green g4 at ri
                show scene_camera
                with d3
                pause 0.5
                s "If we hurry and clear up this gang problem fast, then things will be back to normal before exams."
                s "........."
                s "Sam listen to yourself... We're in it for the long haul~..."
                s "............................"
                s "But I mean...{w} It wouldn't hurt to study a bit in the meantime."
            if randSpy == 3:
                scene cellSam
                show green g43 at ri
                show scene_camera
                with d3
                pause 0.5
                "Sam is checking her phone."
                s "Hey, I remember this cartoon from when I was young!"
                "{size=-6}Phone: {i}'My leg!'{/i}{/size}"
                s g48 "{b}*Snickers*{/b} Still holds up."
            if randSpy == 4:
                scene cellSam
                show green g10 at ri
                show scene_camera
                with d3
                pause 0.5
                s "I wonder how my parents are doing now..."
                s g11 "Probably absolutely fine. Knowing them, they might even notice the city is in an uproar."
                s ".........................................."
                s g15 "Too bad I can't call them to let them know I'm okay. Gotta stay undercover for now."
        if slutLevel == 2:
            if randSpy == 1:
                scene cellSam
                $ greenOutfit = 0
                $ greenOutfitArms = 0
                $ greenTop = 0
                $ greenBottom = 0
                if greenUnder == 0:
                    $ greenUnder = 1
                show green g18 at ri
                show scene_camera
                with d3
                pause 0.5
                s "Maybe this pair of panties with this bra...."
                s g15 "{b}*Sighs*{/b} I never had to bother matching my top with my bottom, but now that [playerName] is asking us to strip, I don't wanna look silly..."
                s g37 "Then again... He seems more interested in what's {i}'underneath'{/i} the underwear anyways..."
            if randSpy == 2:
                scene cellSam
                show green g29 at ri
                show scene_camera
                with d3
                pause 0.5
                s g29 "Oh no, I just realized!"
                s "With all this fighting going on, I won't get to read my monthly edition of {i}'Girls with Brain'{/i} magazine!"
                s g5 "Aw... and I was looking forward to reading that..."
            if randSpy == 3:
                scene cellSam
                show green g18 at ri
                show scene_camera
                with d3
                pause 0.5
                s "I wonder where [playerName] hides his spy cameras..."
                s g29 "Hey [playerName], you're not spying on me right now, right?"
                s "............................."
                s g14 "I'll take that as a no..."
            if randSpy == 4:
                call undressSam from _call_undressSam
                scene cellSam
                $ greenArms = 2
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "..........................."
                s g14 "Heh~... See Sam? You've got nothing to worry about. You look good naked!"
                s g15 "..........................."
                hide green with d3
                $ greenArms = 4
                show green g1 at ri with d3
                s "I bet guys would fight to have a girlfriend like me."
                s "[playerName] seemed pretty excited to see me naked..."
                s g5 "I mean... he wouldn't lie, would he? Did he spy on my because he thinks I'm {i}hot{/i} or did he just want to make fun of me...?"
                s g9 "Gah, stop it Sam. You're overthinking again!"
                hide green
                hide scene_camera
                scene bgBase
                with d3
                $ greenArms = 1
                $ greenHat = greenHatSet
                $ greenAcces1 = greenAcc1Set
                $ greenNeck = greenNeckSet
                $ greenChest = greenChestSet
                $ greenAcces2 = greenAcc2Set
                $ greenBottom = greenBottomSet
                $ greenShoes = greenShoesSet
                $ greenUnder = greenUnderSet
                jump base

        if slutLevel == 3:
            if randSpy == 1:
                scene cellSam
                $ greenBlush = 1
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                "Sam is on her phone."
                s "Okay... things are moving a little quickly. Don't panic Sam."
                s g18 "{i}'Intercrural sex is a type of non-penetrative sex, where the p-...{w}penis...{w} is placed between the receiving partner's thighs...{/i}"
                s g15 "{b}*Whines*{/b }Why did I get the most intimate foreplay job..."
            if randSpy == 2:
                scene cellSam
                show green g40 at ri
                show scene_camera
                with d3
                pause 0.5
                s "I hate this stupid VIB. Hate it, hate it, hate it!"
                s "It's unlady-like, perverse and depraved!"
                play sound "audio/sfx/vib.mp3"
                s g14 "Ngh~...."
                s "But...{w} It feels so good~.... ♥"
            if randSpy == 3:
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "It's a little disturbing that I'm already getting used to [playerName] watching me when I use my dildo..."
                s "Wait... do I enjoy him watching me?"
                s "Urgh! Stop it, Sam! You're overthinking this again! Of course you don't enjoy it!"
            if randSpy == 4:
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "There's no gunfire happening outside..."
                s "Must be a quiet evening. Even gangsters need sleep afterall."
                s "The citizens of Beverly Hills must be so scared... We gotta put an end to this as fast as possible."

        if slutLevel == 4:
            if randSpy == 1:
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "Blowjob! Even the word is disgusting!"
                s "I don't even wanna think of the taste...!"
                "Sam recoils visibly."
                s "Why did I have to have these stupid nanobots inside me~..."
            if randSpy == 2:
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "Clover seemed okay with the suggestion of...{w} going down on each other..."
                s "They're my best friends.... this shouldn't be weird, right?"
                s "I bet there's loads of girls who experiment with their friends..."
                s "......................"
                s "Argh! This is going to be so awkward!"
            if randSpy == 3:
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "I can't believe I let out a moan during our last thighjob session..."
                s "[playerName] must think I was enjoying it! Now he will want to do it more often!"
                s "........................."
                $ greenBlush = 1
                s "Wait... was I enjoying it?"
                s "What's happening to you, Sam....?"
            if randSpy == 4:
                scene cellSam

                play music "audio/sfx/shower.mp3"
                show expression "bgs/cells/green/spyShower.png":
                    xalign 0.282 ypos 185
                if cellSamCurtain == 1:
                    show expression "bgs/cells/green/cellCurtain1.png"
                show scene_camera
                with d3
                pause 0.5
                "Sam is in the shower."
                s "♫♪ {i}Come wander with me, love.... Come wander with me~...{/i} ♫♪"
                s "{b}*Hums a melody*{/b}"
                stop music fadeout 2.0
                hide expression "bgs/cells/green/spyShower.png"
                hide expression "bgs/cells/green/cellCurtain1.png"


        if slutLevel == 5:
            if randSpy == 1:
                call undressSam from _call_undressSam_1
                $ greenArms = 4
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "What set of underwear shall I wear tomorrow...?"
                s "I wonder which [playerName] likes..."
                s "Oh who am I kidding...? He only wants to see me in lingerie..."
                s "...................."
                s "Maybe I should wear that tomorrow...."
            if randSpy == 2:
                call undressSam from _call_undressSam_2
                scene cellSam
                $ greenArms = 5
                show green g1 at ri
                show scene_camera
                with d3
                pause 0.5
                "Sam is looking in a mirror."
                s "Jeeze Sam, stop being so hard on yourself. You look really good!"
                s "Look at those boobies! [playerName] should count himself lucky!"
                s "And with this pussy I can wrap any man around my finger!"
                s g22 "You are so hot, Sam!"
                c "Distant: {i}'Did you say something Sam?'{/i}"
                s g29 "N-nothing!"
            if randSpy == 3:
                call undressSam from _call_undressSam_3
                $ greenUnder = 1
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "So it's come to this..."
                s "Sleeping with fellow WOOHP Agents..."
                s "I can't believe how low you've fallen, Sam.{w} You used to be an A+ student and a super spy!"
                s g40 "Now you're turning into a whore...!"
                s g9 "A common street slut!"
                s "A cumdump! A semen rag, meant to be used and discarded...!"
                s g13 "............................."
                s g12 "Jesus that's turning me on...♥{w} What's wrong with you, Sam...?"
            if randSpy == 4:
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                "Sam is checking her phone."
                s "{i}'10 ways to become unresistable for the opposite gender.'{/i}"
                s g16 "Who would write this trash...? The sentence structure is boring and it fails to convey a deeper meaning!"
                s g18 "........................."
                s g19 "Okay maybe I'll read a bit more...."

        if slutLevel == 6:
            if randSpy == 1:
                scene cellSam
                $ greenArms = 4
                call undressSam from _call_undressSam_4
                call undressClover from _call_undressClover
                call undressAlex from _call_undressAlex
                $ greenUnder = 1.1
                $ redUnder = 1
                $ yellowUnder = 1
                show green g55:
                    xalign 0.74 yalign 0.0
                show red r23:
                    xalign 0.5 yalign 0.0 xzoom -1
                show yellow y56:
                    xalign 0.25 yalign 0.0 xzoom -1
                show scene_camera
                with d3
                pause 0.5
                "All three of the girls seem to be hanging out."
                s "So I said to him...-"
                menu:
                    "Active VIBs" if True:
                        play sound "audio/sfx/vib.mp3"
                        s g28 "!!!"
                        c r29 "!!!"
                        a y42 "!!!"
                        s g8 "[playerName]!!!"
                        y "{b}*Smirk*{/b}"
                        c r25 "Oh... God....! ♥♥♥"
                        a "Ngh~...! ♥"
                        hide red
                        hide green
                        hide yellow
                        with d3
                    "Listen in" if True:
                        a "Hey, you guys wanna practise making out?"
                        c r35 "I think we already get plenty of practise, Alex."
                        a y55 "Come ooooon~... please? Like old times. ♥"
                        s g13 "Heh~... yeah why not. Let's have a threeway kiss...!"
                        c r24 "I've got an even better idea~...."
                        hide green
                        hide red
                        hide yellow
                        with d3
                        "The three girls are going down on each other!"
                        y "Where's a bucket of popcorn when you need it...."
                "Girls" "Ahhhh!!! ♥♥♥♥♥"
            if randSpy == 2:
                scene cellSam
                show expression "bgs/cells/green/dildoBed.png"
                show scene_camera
                with d3
                pause 0.5
                "Sam is lying on her bed."
                s "Y-yes... deeper!"
                s "Ahhh! Ahh! Call me a slut!"
                s "Pull my hair... ♥"
                s "Ah, ah, ah, ahhh!"
                s "Fffffuuuuucck!!!! ♥♥♥♥"
                hide expression "bgs/cells/green/dildoBed.png"
            if randSpy == 3:
                scene cellSam
                show green g5 at ri
                show scene_camera
                with d3
                pause 0.5
                s "I got some free time. I should probably do something productive with that..."
                s "I haven't opened a study book in weeks..."
                s "But I might just do some internet browsing instead."
            if randSpy == 4:
                s "Wait, did I just hear a fly? How did that get in here...?"
                s "...................."
                s "...................."
                s "Gotcha!"
                play sound "audio/sfx/punch1.mp3"
                scene black
                s "Oops... that was a spy drone..."

        if slutLevel == 7:
            "NOT IN YET"

        hide green
        hide scene_camera
        scene bgBase
        with d3
        $ greenBlush = 0
        $ greenArms = 1
        call greenOutfitSet from _call_greenOutfitSet_6
        jump base

label spyCameraRed:
    $ spyRoomRand = 0
    if tutorialActive and tutStage == 3:
        if activeSpy == 1:
            "You tune in to see what [greenName] is up to."
            hide screen spyScreens
            scene black with fade
            scene bgSideroom
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[greenName] is currently located at the safehouse. She is standing in the sideroom, waiting for you to help her clean up."
        if activeSpy == 2:
            "You tune in to see what [redName] is up to."
            hide screen spyScreens
            scene black with fade
            scene bgSideroom
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[redName] is currently located at the safehouse. She is standing in the sideroom, waiting for you to help her clean up."
        if activeSpy == 3:
            "You tune in to see what [yellowName] is up to."
            hide screen spyScreens
            scene black with fade
            scene bgSideroom
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[yellowName] is currently located at the safehouse. She is standing in the sideroom, waiting for you to help her clean up."
        hide green
        hide red
        hide yellow
        scene black
        with d5
        jump tutBase
    if tutorialActive and tutStage == 5:
        if activeSpy == 1:
            "You tune in to see what [greenName] is up to."
            hide screen spyScreens
            show green:
                xalign 1.0 yalign 0.0
            with d3
            "[greenName] is currently located at the safehouse. She is standing in the main room next to you.."
            s "What are you doing....?"
            y "Nothing!"
        if activeSpy == 2:
            "You tune in to see what [redName] is up to."
            hide screen spyScreens
            show red:
                xalign 1.0 yalign 0.0
            with d3
            "[redName] is currently located at the safehouse. She is standing in the main room next to you.."
            c "What are you doing....?"
            y "Nothing!"
        if activeSpy == 3:
            "You tune in to see what [greenName] is up to."
            hide screen spyScreens
            show yellow:
                xalign 1.0 yalign 0.0
            with d3
            "[yellowName] is currently located at the safehouse. She is standing in the main room next to you.."
            a "What are you doing....?"
            y "Nothing!"
        hide green
        hide red
        hide green
        scene black
        with d5
        jump tutBase
    if tutStage == 11:
        $ tutStage = 12
        scene cellClover
        show red at ri
        show scene_camera
        with fade
        c r11 "So I kissed my best friend today..."
        c "................"
        c "Let's not try to think about it too much."
        show bgBase
        hide red
        hide scene_camera
        with fade
        jump base
        if task2Stage == 10:
            scene cellClover
            show red:
                xalign 1.0 yalign 0.0
            show scene_camera
            with d3
            c "I've had one hell of a day... I can't wait for it to be over..."
            c "Now to go to sleep and ignore any sexually confused thoughts I might have after today."
            scene black
            hide red
            hide scene_camera
            with fade
            $ redChest = 1
            $ redBottom = 1
            $ redShoes = 1
            scene bgBase with fade
            jump base
    if task2Stage == 15:
        scene cellClover
        $ redOutfit = 0
        $ redOutfitArms = 0
        $ redUnder = 1
        show red r4 at ri
        show scene_camera
        with d3
        c "{i}'The Vitals Indecator Bug, also known as the V.I.B. Highly experimental and remains untested.'{/i} That's some grade A technology for you there..."
        c "Guess we'll have to be the guinea pigs for this one."
        menu:
            "Turn on V.I.B." if True:
                play sound "audio/sfx/vib.mp3"
                c "Ah!!"
                c "{size=+4}[playerName]!!!!{/size}"
                c "......................."
                c "Oh boy I gotta get used to this...!"
            "Never mind" if True:
                pass
        hide red
        hide scene_camera
        scene bgBase
        with d3
        jump base
    if task4Stage == 4:
        scene cellAlex
        show red r4 at ri
        show green at ce
        show yellow at le
        show scene_camera
        with d3
        a "So you guys opened a restaurant...?"
        s "Yes. It's to keep a low profile and make money. [playerName] will probably ask you to work there every now and then."
        c "You have to wear a skimpy uniform, but it's not so bad. The tips are actually pretty good!"
        c "The only downside is that customers will slap your ass every now and then."
        a "W-what?! I don't want that!"
        play sound "audio/sfx/spank1.mp3"
        with hpunch
        a "Eep!"
        c "See? It's not so bad, you'll get used to it."
        a "Ow~..."
        scene bgBase
        hide red r4 at ri
        hide green at ce
        hide yellow at le
        hide scene_camera
        with d3
        jump base
    if cloverSpySex == 2:
        $ sexScene = 1
        "You tune in to see what Clover is up to."
        scene black with fade
        $ sexScene = 2
        jump cloverSex2
    elif True:
        if spy2Status == 10:
            "Clover isn't at the base at the moment."
            jump base
        $ randSpy = renpy.random.randint(1,4)
        if slutLevel <= 1:
            if randSpy == 1:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "These cells are bigger than the ones I'm used to by WOOHP..."
                c "I guess crazier get a little more space. There's room for a couch... maybe a hanging chair."
                c "Too bad the door is transparent. Makes me feel like someone is watching me..."
                c "........................"
                c "Nah you're just being paranoid."
            if randSpy == 2:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "{b}*Whines*{/b} I could be going on a date with the cute boy from musical class right now, but instead I'm locked up in here!"
                c "These super villains have the worst timing!"
                c "Atleast I still get to put on my make-u-..."
                c "...................."
                c "There's no mirror...{w} Can this day get any worse?"
            if randSpy == 3:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Ugh, what villains did they lock up in here?! It smells like fish!"
                c "Let's do some exploring~...."
                c "Hmm... Nothing....{w} Nothing....{w} Wait... what's this?"
                c "It's a newspaper article that reads 'We should all bow down to our whale overlords'."
                c "............................."
            if randSpy == 4:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Nooooo!"
                c "The city being over taken over is one thing, but a bad hair day two days in a row?!"
                c "What almighty cosmic force did I piss off to be this cursed?!"
                "Clover is seen frantically straightening out her hair."
        if slutLevel == 2:
            if randSpy == 1:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Today has been crazy!"
                c "I've gotten so much work done. Gold star for Clover!"
                c "Maybe I should work hard more often. I didn't know it could be this rewarding!"
                c "................................"
                c "But probably not. They say stress causes wrinkles."
            if randSpy == 2:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Not having to go to school is pretty cool, but I miss seeing all the cute boys..."
                c "Whoever's behind this attack will pay from keeping me from my true love....{w}s!"
                c "Well at least the mall is still open, so it's not all bad."
            if randSpy == 3:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "I wonder what [playerName] thought when he saw me naked..."
                c "Tsk, I know what he thought. He was going 'DAAAAAAYUM'!"
                c "And who can blame him. He's a lucky guy."
            if randSpy == 4:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Where did I leave that toe clipper?!"
                c "........................"
                c "SERIOUSLY! WHERE DID I LEAVE THAT FREAKING TOE CLIPPER!"
                "You see Clover frantically turn over her bed."
        if slutLevel == 3:
            if randSpy == 1:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Oh wait, that's it..."
                c "Windows. That's what this place is missing."
                c "Too bad we're underground..."
                c "Maybe I'll look into getting some posters or paintings."
            if randSpy == 2:
                call undressClover from _call_undressClover_1
                $ redArms = 5
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                "Clover is looking in a mirror."
                c "Man look at you two."
                c "No wonder [playerName] likes to play with you guys. I've got the best tits in Beverly Hills."
                "She bounces her breasts up and down a few times."
                c "Jiggle, jiggle..."
            if randSpy == 3:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                if punkRank >= 3:
                    c "I wish the tabletop game store didn't burn down..."
                    c "Now where am I going to get my glow in the dark dice...?"
                    c "Oh! And I can't forget about my online game later tonight.{w} Busy busy."
                elif True:
                    c "The boredom is killing me. I really need a hobby."
                    c "Knitting. No, I'm not a grandma yet."
                    c "Gardening. Having one insane plant lady running around is enough."
                    c "Checking out hot boys on the beach. Now that I can do~...{w} I hope [playerName] gives me a day off again soon."
            if randSpy == 4:
                scene cellClover
                show expression "bgs/cells/red/dildoBed.png"
                show scene_camera
                with d3
                pause 0.5
                c "Ah~... ahhh~...! ♥♥♥"
                c "Fuck me, daddy~... ♥"
                c "Oh man this is so good, thank you [playerName]!!"
                hide expression "bgs/cells/red/dildoBed.png"
        if slutLevel == 4:
            if randSpy == 1:
                scene cellClover
                show red r42 at ri
                show scene_camera
                with d3
                pause 0.5
                "Clover is preparing her toothbrush."
                c "Ugh... lemme brush my teeth..."
                c "Blowjobs are fun, but they taste so bad..."
                c r18 "I wonder if it feels the same for men as it feels for women..."
            if randSpy == 2:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c r12 "I want some VR glasses. I don't think they deliver to warzones though...."
                c "Guess I'm stucking watching funny videos online..."
                c "Hey... what's this ERP thing people are talking... about..."
                c r29 "Oh...{w} Oooooh.{w} So that's what ERP is...."
            if randSpy == 3:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c r11 "I kinda wanna give another boobjob..."
                c r23 "I can't believe how reluctant I was to give one before. These are so hot..."
                c "And when he cums on your face~...♥{w} {b}*Sighs*{/b} You're such a hoe Clover..."
            if randSpy == 4:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c r14 "Oof~... going undercover with the Drift Punk is cool, but they turn their music up so loud..."
                c "I don't think I'll get a lot of sleep tonight...!"
                c r13 "All in all, I got to go undercover in a pretty awesome gang."
        if slutLevel == 5:
            if randSpy == 1:
                scene cellClover
                play music "audio/sfx/shower.mp3"
                show expression "bgs/cells/red/spyShower.png":
                    xalign 0.282 ypos 185
                if cellCloverCurtain == 1:
                    show expression "bgs/cells/red/cellCurtain2.png"
                show scene_camera
                with d3
                pause 0.5
                "Clover is taking a shower."
                c "Oh man... I should get one of those wall mounted dildos for in here."
                c "Okay... step back Clover!{w} You already have a dildo and the VIB. You're not going to build up an arsenal of sex toys."
                c "At least not yet~.... ♥"
                stop music fadeout 1.0
                hide expression "bgs/cells/red/spyShower.png"
                hide expression "bgs/cells/red/cellCurtain1.png"
            if randSpy == 2:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c r11 "I can't believe I'm fucking, [playerName]..."
                c r23 "He is pretty cute in his own way~..."
                c r14 "Ngh~... and that body~..."
                c "Maybe I should stop chasing after boys and get myself a {i}man{/i}."
            if randSpy == 3:
                call undressClover from _call_undressClover_2
                $ redChest = 11
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Showering is nice, but I wish we could bring a hottub in here..."
                c "Ngh~... I miss going to the spa..."
                c "I'm a little jealous of Sam. She and the Aces can go into those fancy expensive spa's that haven't been destroyed yet..."
            if randSpy == 4:
                scene cellClover
                show red r24 at ri
                show scene_camera
                with d3
                pause 0.5
                "Clover is on her phone."
                c "69 ways to please your man."
                c r23 "I bet I can guess what number 69 is going to be~...."
                c "{i}'Cook him a nice dinner'{/i}"
                c r18 "Oh... not what I expected..."
        if slutLevel == 6:
            if randSpy == 1:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "I feel like I'm going to be walking bow-legged for a while..."
                c "Anything to satisfy a man.... right Clover...?"
                c "{b}*Sighs*{/b} I guess I shouldn't complain. It's a pretty interesting way to reduce my nanobots...♥"
            if randSpy == 2:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "Maybe I should do some push-ups to improve my strength... or jumping rope to improve my agility..."
                c "I guess I could read a book to improve my intelligence..."
                c ".........................."
                c "None of these things sounds very fun... It's so much easier in a game..."
            if randSpy == 3:
                call undressClover from _call_undressClover_3
                $ redArms = 2
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "I sometimes wonder if this is a two-way mirror..."
                c "[playerName] can you see me right now...?"
                c "........................................."
                $ redArms = 5
                pause 0.5
                c "I'm just being paranoid...."
            if randSpy == 4:
                scene cellClover
                show red r1 at ri
                show scene_camera
                with d3
                pause 0.5
                c "I miss going to the beach..."
                c "I mean.. I still go there, but there's always that nagging feeling in the back of your mind."
                c "Like a gang could should up and attack you when you least expect it."
                c "............................."
                c "Come to think of it, I used to have that feeling before the riots broke out aswell... {w}Being a spy does that to you."
        if slutLevel == 7:
            "NOT YET IN."

        hide red
        hide scene_camera
        scene bgBase
        with d3
        $ redBlush = 0
        $ redArms = 1
        call redOutfitSet from _call_redOutfitSet_5
        jump base


label spyCameraYellow:
    $ spyRoomRand = 0
    if task4Stage == 4:
        scene cellAlex
        show red r4 at ri
        show green at ce
        show yellow at le
        show scene_camera
        with d3
        s "So you're saying there's a whale themed villain out there...?"
        a "No, a whale biologist themed villain. She's not an actual whale."
        s "Oh okay. For a second there I th-..."
        a "Her boyfriend is."
        c "What?"
        a "She's dating a whale."
        c ".................."
        c "I'm beginning to see why these guys were locked up in an insane asylum."
        scene bgBase
        hide red r4 at ri
        hide green at ce
        hide yellow at le
        hide scene_camera
        with d3
        jump base
    if alexSpySex == 2:
        $ sexScene = 1
        "You tune in to see what Alex is up to."
        scene black with fade
        $ sexScene = 2
        jump alexSex2
    elif True:
        if spy3Status == 10:
            "Alex isn't at the base at the moment."
            jump base
        $ randSpy = renpy.random.randint(1,4)
        if slutLevel <= 1:
            if randSpy == 1:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "I wonder what it's like being a shark..."
                a "................................."
                a "{b}*Snickers*{/b}"
                y "(Another rifiting look inside the mind of Alex...)"
            if randSpy == 2:
                call undressAlex from _call_undressAlex_1
                $ yellowUnder = 1
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "You have to be a big girl, Alex!"
                a "Next time [playerName] asks to see your boobies, you tell him {b}'no'{/b}."
                a "Only you get to see them!{w} And Sam...{w} And Clover..."
                a "But nobody else!"
            if randSpy == 3:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "I don't understand why everyone's fighting..."
                a "Are these nanobots really that dangerous...?"
                a "You have to be tough, Alex! {w}Everyone is relying on you! Together with your friends and [playerName] you will retake the city!"
            if randSpy == 3:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "..............."
                a "This is actually a cool bed~..."
                a "I bet I could stack pillows and make it a pillow fortress!"
                a "I'll just borrow some pillows from the empty cells.{w} Call me Queen Alex! Ruler of the underground!"
            if randSpy == 4:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "It's pretty late..."
                a "But I really want a milkshake..."
                a "I wonder if [playerName] would get angry if I snuck upstairs to the bar~...."
        if slutLevel == 2:
            if randSpy == 1:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                "Alex is sitting on her bed."
                a "........................."
                y "...?"
                a "........................."
                y "(What is she doing...?)"
                a "........................"
                a "Huh?{w} Oh! I was daydreaming again!"
                a "How many hours passed this time....?"
            if randSpy == 2:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                "Alex is playing a game on her phone."
                a "Crush, crush, crush, crush~...."
                a "CRUSH, CRUSH, CRUSH, CRUSH!"
                a "Hah! Take that empty calories! You won't be tempting me anymore!"
            if randSpy == 3:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "So your plan for not showing your nudies didn't exactly work..."
                a "Oh well, in for a nickle in for a buck I guess."
                a "........................."
                a "I feel like I got that saying wrong..."
            if randSpy == 4:
                call undressAlex from _call_undressAlex_2
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                "Alex is looking in a mirror."
                a "I can kinda get why [playerName] likes looking at these..."
                a "Bounce!"
                "Alex hops on the spot, causing her tits to jiggle up and down."
                a "Bounce! Bounce!"
                y "(........................)"
                a "Bounce! Bounce! Bounce!"
                y "(Alex you're killing me and you don't even know it...)"
        if slutLevel == 3:
            if randSpy == 1:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                "Alex is reading her phone."
                a "Buttjobs~....."
                a "Lemme check this video..."
                a "..............................."
                a "This shouldn't be too har-..."
                a "!!!"
                a "Noooo, that's not suppose to go there!"
                a "Oh no, there's another one!"
                a "They're so big, how does she even breath?!"
                "You see a traumatized Alex throw her phone into the corner of the room."
            if randSpy == 2:
                call undressAlex from _call_undressAlex_3
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "I think I'm gonna walk around naked from now on..."
                a "Everyone here has already seen my nudies and I don't have to do the laundry as often!"
                a "I'm gonna tell Clover!"
                hide yellow
                with d2
                a "Distant: CLOVER!"
                c "Distant: Alex? Why are you naked?!"
            if randSpy == 3:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "I wonder how Jerry is doing right now..."
                a "I must work extra hard! We'll free the city and then safe Jerry!"
                a "........................"
                a "I just hope he's not hurt..."
            if randSpy == 4:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "Hmpf~..."
                a "Why is it so hard to find a boyfriend who shares my interest!"
                a "He's gotta be a athletic, fun-loving, good looking....{w} and a pony."
                a "I don't know what {i}'beastiality'{/i}means, but I'm sure they're just overreacting."
        if slutLevel == 4:
            if randSpy == 1:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "Blowjob is such a silly word..."
                a "You don't do a whole lot of blowing..."
                a "Wait! Maybe I've been doing it wrong! Next time I'll blow really hard!"
                a "I just hope [playerName] doesn't blow up like a balloon..."
            if randSpy == 2:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "Boobjobs, blowjobs, buttjobs... [playerName] is sure letting us to a lot of jobs..."
                a "I wonder if he'll actually pay us for them..."
                a "I'll ask him, next time I see him!"
            if randSpy == 3:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "I should get a gun!"
                a "It would make my job so much easier. Just point and pull the trigger and BOOM! All your problems are gone!"
                a "Well there's the whole worry about killing people of course..."
                a "Maybe I'll just get a toy gun! Best of both worlds!"
            if randSpy == 4:
                if cellAlexGuitar == 0:
                    scene cellAlex
                    show yellow y5 at ri
                    show scene_camera
                    with d3
                    pause 0.5
                    a "I miss my guitar..."
                    a "I saw one in the mall yesterday, but I can't waste our money on that..."
                    a "Still..."
                    "Alex proceeds to rock out to an air guitar."
                elif True:
                    scene cellAlex
                    show yellow y20 at ri
                    show scene_camera
                    with d3
                    pause 0.5
                    a "I do love you Mr. Wiggles, but nothing compares to a real dick."
                    a "Don't be jealous, okay?"
        if slutLevel == 5:
            if randSpy == 1:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a y20 "Having sex... does that make me a slut?"
                a y16 "Or do I need to have loads of it...?"
                a "Maybe I need to have loads of it with lots of people..."
                a y19 "Man, being a slut is hard."
            if randSpy == 2:
                scene cellAlex
                show yellow y20 at ri
                show scene_camera
                with d3
                pause 0.5
                "Maybe I should read up on sex..."
                a "Let's see here... {i}'10 interesting sex positions'{/i}."
                "Alex looks confused and turns her head."
                a y16 "But where does that...?"
                a y29 "Wait... I thought you were only suppose to have one of those..."
                a "This one looks interesting, but we don't have a ceiling fan..."
                a y28 "I'm pretty sure this one is illigal!"
                a y21 "..................."
                a "Sex is complicated..."
            if randSpy == 3:
                scene cellAlex
                show yellow y5 at ri
                show scene_camera
                with d3
                pause 0.5
                a y5 "I want to call mom and dad..."
                a "The girls told me to stay undercover though..."
                a "{b}*Sniff*{/b} They must be so worried..."
            if randSpy == 4:
                scene cellAlex
                show expression "bgs/cells/yellow/dildoBed.png"
                show scene_camera
                with d3
                pause 0.5
                a "Ah~... Ahhh~... deeper Mr. Wiggles~... ♥♥♥"
                a "Deeper~... fill me up~...!"
                a "Ahhhhhh!! ♥♥♥♥♥"
                a "{b}*Pant* *Pant* *Pant*{/b}"
                a "Best... gift... ever!"
                hide expression "bgs/cells/yellow/dildoBed.png"
        if slutLevel == 6:
            if randSpy == 1:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "Looks like not even my butt is safe now..."
                a "Maybe Mr. Wiggles will help me practise~... ♥"
                hide yellow with d2
                call undressAlex from _call_undressAlex_4
                show yellow y1 at ri
                a "Ooooh Mr. Wiggles~....!"
                a "I have a surprise for youuuuu~...."
            if randSpy == 2:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "{b}*Sighs*{/b} Reading dark and depressing poetry is nice and all, but sometimes I wish I could read something less cynical."
                a "Maybe I could borrow some comics from Clover~..."
                a "She doesn't need to know they're missing~... ♥"
            if randSpy == 3:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "Hm... I wonder how I become a {i}'big tittied goth gf'{/i}."
                a "Big titties. {w}Check."
                a "Goth... {w}half-check."
                a "GF... {w}I'll need to get a BF first..."
                a "But I don't think [playerName] would let me have any..."
            if randSpy == 4:
                scene cellAlex
                show yellow y1 at ri
                show scene_camera
                with d3
                pause 0.5
                a "I hope [playerName] will ask me to have sex again soon..."
                a "It's so much fun!"
                "Alex is visibly shaking with excitement."
                a "I want to do it every day and in all kinds of positions!"
        if slutLevel == 7:
            "NOT YET IN"

        hide yellow
        hide scene_camera
        scene bgBase
        with d3
        $ yellowBlush = 0
        $ yellowArms = 1
        call yellowOutfitSet from _call_yellowOutfitSet_3
        jump base

"OOP, YOU'RE NOT SUPPOSE TO SEE THIS. JUMPING TO BASE."
jump base
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
