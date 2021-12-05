default tutStage = 1

image schoolBG1 = "mission/schoolDistant1.jpg"
image schoolBG2 = "mission/schoolDistant1.jpg"

label splashscreen:
scene black with dissolve
pause 1
show text "{size=+20}{color=#f10000}АХТУНГ!{/color}\n{/size} \n Игра ещё переводиться!!! \n Статус перевода: \"сырой - не редактированный\" \n Пресутсвуют многочисленные орфографические ошибки и непонятности. \n Советую дождаться полноценного перевода. \n За новостями удобно следить в моём телеграм канале: @papawrtranslate." with dissolve
pause 10
show text "Но если ты не терпеливый(ая) и у тебя стольные яйца, то приятной игры. ©Papawr"
pause 5
scene black with dissolve
pause 1
return

label start:
    label introGame:
        pass
    $ random = renpy.random.randint(1, 4)
    if random == 1:
        $ traitorRandom = 568513
    if random == 2:
        $ traitorRandom = 870803
    if random == 3:
        $ traitorRandom = 708349

    menu:
        "Begin intro" if True:
            jump beginIntro

            "Are you sure you want to skip ahead? The intro teaches you some important game mechanics."
            menu:
                "Yes, skip the intro" if True:
                    jump skipIntro
                "Let me play the intro" if True:
                    jump beginIntro

            $ hat2Sam = True
            $ hat6Sam = True
            $ top1Sam = True
            $ top2Sam = True
            $ top3Sam = True
            $ top4Sam = True
            $ top5Sam = True
            $ top6Sam = True
            $ top7Sam = True
            $ top8Sam = True
            $ bott1Sam = True
            $ bott2Sam = True
            $ bott3Sam = True
            $ bott4Sam = True
            $ bott5Sam = True
            $ bott6Sam = True
            $ bott7Sam = True
            $ bott8Sam = True
            jump skipIntro










label beginIntro:
    scene black
    show text "{size=+20}{color=#f10000}WARNING{/color}\n{/size} \n The following game is a parody. No endorsements by any company or person parodied is intended to be inferred. The law regarding parody is based upon the CJEU parody regulations under European law. Under this doctrine, certain uses of copyrighted works, which would otherwise by considered infringing, are permissible.\n\n Totally Spies and its associated properties are owned by Marathon Media.\n\n All characters depicted in sexual conduct or in the nude are aged 18 years or older. No actual or identifiable minor was used in the creation of any character depicted herein.\n\n This game contains adult material and is only intended for viewers aged 18 or over. If you are under 18, please do not continue." with dissolve
    with d3
    $ renpy.pause(8.0, hard='True')
    hide text
    with d3
    pause 1.0
    play sound sfxText
    LOCATION "Beverly Hills, USA - Somewhere underground..."
    scene cellNeutral
    show screen cellDoor
    with fade
    pause 1.0
    yInmate "........................."
    yInmate "The World Organization Of Human Protection, better known as WOOHP...."
    yInmate "It's fine they said... It's better than spending time in prison they said..."
    yInmate "The WOOHP Asylum for the Criminally Insane is a {i}much{/i} better alternative they said..."
    yInmate "So they put me in a hole in the ground and threw away the key..."
    yInmate "I'm not insane! I just had a few very unfortunes events!"
    "Guard" "FRONT AND CENTER INMATE!"
    yInmate "Gah!"
    hide screen cellDoor
    with d3
    pause 0.5
    show scene_darkening
    with d3
    show O5O at ri
    with d3
    "Guard" "WHAT ARE YOU MUTTERING TO YOURSELF ABOUT?! THAT'S SOMETHING AN INSANE PERSON WOULD DO!"
    yInmate "......................"
    yInmate "Okay fair enough."
    "Guard" "YOU'RE ON CLEANUP DUTY TODAY! THE CLEANING STAFF HASN'T SHOWED UP SO NOW I'M MAKING YOU DO IT!"
    yInmate "Isn't that abusing your p-...?"
    "Guard" "ABUSING MY POWER! EXACTLY!"
    "Guard" "YOUR ORDERS ARE SIMPLE!{w} KEEP MOPPING THAT FLOOR UNTIL IT SPARKLES. I WANT TO SEE MY FACE IN THAT FLOOR!"
    "Guard" "I WANT IT BETTER THAN CLEAN! I WANT IT TO BE HANDSOME!"
    yInmate "Er...."
    "Guard" "I WANT THIS PLACE TO LOOK SO HANDSOME, THAT WHEN I WALK IN HERE AND SEE MY OWN REFLECTION, I THINK A HANDSOME INTRUDER HAS INVADED THIS FACILITY!"
    "Guard" "I WANT TO TAKE MY DATE TO THIS ASYLUM AND HAVE HER DUMP ME FOR MY REFLECTION, THAT'S HOW CLEAN I WANT THIS FLOOR TO BE!{w} DO I MAKE MYSELF CLEAR?!"
    yInmate "You'd take your date to an asylum?"
    "Guard" "THAT'S ENOUGH OUT OF YOU WISEGUY! HERE'S A BUCKET AND A MOP!"
    "Guard" "NOW GET MOPPING!"
    menu:
        "YES SIR!" if True:
            yInmate "YES SIR, ON IT SIR!"
            "Guard" "STOP THAT SHOUTING, THIS IS AN ASYLUM, DON'T YOU KNOW?!"
            yInmate "....................."
        "Am I getting paid for this?" if True:
            yInmate "I'm pretty sure you're legally required to pay me for this~..."
            "Guard" "HOT-DOG! YOU'RE RIGHT!{w} HERE'S A DOLLAR!"
            $ randMoney = 1
            $ cash += 1
            call missionRewardMoney from _call_missionRewardMoney_6
            yInmate "Thanks~..."
        "Say something insane" if True:
            yInmate "Did you know that the national anthem wasn't really written by Francis Scott Key?"
            yInmate "There's compelling evidence that show that a giant panda named Sir Jamie Fitzgerald-...."
            yInmate "(Oh my God!{w} I really am insane!)"
            "Guard" "THAT'S ENOUGH OUT OF YOU INMATE! {w}EVERYONE KNOWS SIR JAMIE FITZGERALD WAS THE REAL AUTHOR OF THE ANTHEM!"
            "Guard" "NOW GET TO MOPPING!"
            yInmate "................."
    "Guard" "IN THE MEANTIME I'M HEADING INTO THE MILKSHAKE BAR!"
    yInmate "The... what now?"
    "Guard" "DON'T TALK BACK TO M-...."
    play sound "audio/sfx/shockcrash.mp3"
    pause 0.7
    hide O5O
    show white
    pause 0.05
    hide white
    show bgControl
    show O5O:
        xalign 1.0 yalign 0.0
    pause 0.6
    hide bgControl
    pause 0.2
    "Guard" "......................................"
    yInmate "...?"
    "Guard" "Overthrow~....{w} Anarchy~....{w} Chaos~....."
    "The guard suddenly stops paying attention to you as he blindly stares into space."
    yInmate "Ehrm... Are you okay...?"
    hide O5O
    with d3
    "Without another word, the zombiefied guard walks out of the cellblock."
    yInmate "..........................."
    yInmate "I guess the guards are as insane as the inmates..."
    yInmate "Well...! Idle hands are the devil's playthings. Best get busy mopping."
    scene black with longFade
    pause 1.0
    "You spend a couple of hours cleaning the place."
    "The other inmates looks skittish and on edge. Quietly muttering to each other and going silent as you walk by."
    "???" "Hey pssst~...."
    scene cellNeutral
    show screen cellDoor
    with fade
    yInmate "....?"
    show silvaModel:
        xalign 0.9 yalign 0.0
    with d3
    "???" "You can stop cleaning now, mon ami.{w} Would you like to know a secret...?"
    "???" "We're busting out of zis place soon. {w}Haven't you noticed ze chaos going on upstairs?"
    play music "audio/sfx/warzone.mp3" fadein 2.0
    yInmate "Chaos...?"
    "You listen closely and hear sirens and what appears to be gunshots going off in the outside world."
    yInmate "Oh sorry. I didn't notice. I'm from Chicago so this isn't anything new."
    "???" "Just wait for ze lights to flicker~...."
    yInmate "The ligh-...?"
    play sound "audio/sfx/explosion1.mp3"
    with hpunch
    hide screen cellDoor
    scene black
    pause 0.2
    scene cellNeutral
    show screen cellDoor
    pause 0.2
    hide screen cellDoor
    scene black
    pause 0.1
    scene cellNeutral
    show screen cellDoor
    pause 0.1
    hide screen cellDoor
    scene black
    pause 0.1
    scene cellNeutral
    show screen cellDoor
    pause 0.1
    hide screen cellDoor
    scene black
    pause 1.0
    "You hear a loud explosion happening overhead."
    yInmate "What the...?!"
    "You see the inmates smirk as one by one their celldoors open."
    scene cellNeutral with fade
    show silvaModel:
        xalign 1.0 yalign 0.0
    with d2
    "???" "Zis is your chance! Come with us and escape!"
    yInmate "I appreciate the offer, but I'm not done cleaning yet."
    "???" "....................."
    "???" "You really are insane...~"
    "???" "Come on everybody! Let's get out of here!"
    hide scene_darkening
    hide silvaModel
    with d3
    "In a storm, the inmates make a run for it, rushing their way out of the cellblock."
    yInmate "..............."
    menu:
        "Finish your job (+Karma)" if True:
            $ playerKarma += 1
            yInmate "Like my old nan always says. {i}'You might scream and cry and hollar, but a dollar is still a dollar.'{/i}."
            yInmate "..........."
            yInmate "Then again, she also said the Emancipation Proclamation was a mistake...{w} We don't talk much to her anymore."
            stop music fadeout 1.0
            scene black with fade
            "You spend a little bit more time cleaning until everything sparkles."
            yInmate "Wow... my reflection {i}'is'{/i} handsome!"
            "You're satisfied with a job well done and exit the detention area."
            scene bgBase with fade
        "Escape (-Karma)" if True:
            $ playerKarma -= 1
            yInmate "Like my old nan always says. {i}'Better shoot a cop than work with a mop!'{/i}."
            yInmate "..........."
            yInmate "Then again, she also said the Emancipation Proclamation was a mistake...{w} We don't talk much to her anymore."
            "Dropping your mop, you make your way to the exit of the prisonblock."
            stop music fadeout 1.0
            scene bgBase with fade
    play music "audio/music/stealth1.mp3" fadein 2.0
    yInmate "Now let's get out of here and start my new life."
    yInmate "This elevator seems to head upstairs to the exit..."
    call screen tutBase


label tutStage2:
    $ tutSage = 2
    y "Yeah, I think I'm good to go."
    y "I can't wait to get a job and begin my new well adjusted and respectable life!{w} Maybe a doctor, a lawyer...{w} Or a telemarketeer!"
    scene black with fade
    "You step into the elevator."
    y "Hmm.... ground floor, prison block or... bullet train?"
    y "It looks like this place is connected to WOOHP HQ via train."
    "Opting not to take your chances, you head to ground level."
    play music "audio/sfx/warzone.mp3" fadein 2.0
    scene bgClub0 with fade
    y "......................."
    y "Oh right, the violence in the streets...."
    "You look around."
    y "Where am I? It looks like some old timey....{w} Milkshake bar!{w} This place looks like it hasn't been used since the 50s."
    y "Well I'm not gonna get a job in a dump like this. Best head outside."
    scene black with fade
    scene bgStreet1 with fade
    "You step outside and are greeted by armageddon."
    "Everywhere you look, you see gangs fighting in the open street."
    "Police cars are burning, shops are being looted and gunfire can be heard around every corner."
    y "..................."
    "You decided to head back inside."
    scene bgClub0 with fade
    y "Yeah... Let's wait until things calm down a bit...~"
    menu:
        "Have a milkshake" if tutMilkshake:
            y "All this violence is making me thirsty."
            y "Let's see if I can pour myself a shake!"
            "You pour yourself a milkshake."
            y "Delicious!"
            "........{w}........{w}........"
            y "........................"
            y "Funny, I expected it to-..."
            play sound "audio/sfx/punch1.mp3"
            scene black with d1
            stop music
            pause 1.0
            "You collapse from food poisoning."
            "You spend the rest of the day on the toilet. When the sun sets, the violence seems to die down a little."
        "Clean the milkshake bar" if tutClean:
            y "Again with the cleaning... Maybe I should try getting a job as janitor after this..."
            scene black with fade
            pause 0.5
            "You spend some time cleaning the milkshake bar. It looks nicer than before, but still needs some work."
            scene bgClub0
            with d3
            stop music fadeout 3.5
            y "Sounds like the fighting is dying down..."
            y "But it's also getting dark. I'm not sure if it's a smart move to go out now."
            y "Guess I'll spend the night in the base, just to be sure."
            scene black with fade
        "Head back downstairs" if True:
            y "Deadly gun violence up here... or safe living conditions downstairs..."
            y "I guess I can wait until the violence calms down a bit."
            scene black with fade
            stop music fadeout 2.0
            "You spend the rest of the day in the base. When it turns dark, the violence seems to calm down a little."
    scene bgBase with fade
    pause 1.0
    play music "audio/music/sinister.mp3" fadein 3.0
    "{b}*Beep* *Beep* *Beep*{/b}"
    y "...?"
    y "A distress signal?{w} {b}*Beep*{/b}"
    scene bgSchool1
    with fade
    pause 0.5
    show yellow y29:
        xalign 0.2 yalign 0.0 xzoom -1
    show scene_camera
    with d3
    a "{b}*Quietly:*{/b} Jerry is that you?"
    y "Er..."
    $ greenFace = 0
    hide scene_camera
    show green g34 at ri
    show scene_camera
    with d3
    s g31 "Listen, we're hiding out at school. We're okay, but we've been attacked by our own WOOHP Agents."
    show red:
        xalign -0.1 yalign 0.0 xzoom -1
    hide scene_camera
    show scene_camera
    with d3
    c "And now Beverly Hills is turning into a warzone! That's like... totally not cool!"
    s "Can you pull us out of here via the WOOHP Tunnel Network?"
    y ".............."
    y "Suuure~...."
    "You press some random buttons on the console."
    y "............"
    y "It says right here that I can only pull you out one at a time."
    s g32 "That's fine, but please just hurry."
    label tutSpySelect:
        pass
    $ firstPick = 1
    $ samHealth = "Healthy"
    $ spyGreenActive = True
    y "Ye okay."
    y "{b}*Bleep*{/b}"
    show green:
        linear 0.1 xalign 1.0 yalign 0.0
        linear 0.1 xalign 0.99 yalign 0.0
        linear 0.1 xalign 1.0 yalign 0.0
        linear 0.1 xalign 0.99 yalign 0.0
        linear 0.05 xalign 1.00 yalign 0.0
        linear 0.05 xalign 0.99 yalign 0.0
        linear 0.05 xalign 1.00 yalign 0.0
        linear 0.05 xalign 0.99 yalign 0.0
        linear 0.10 yalign 6.4
    pause 1.1
    hide green
    with d3
    "The screen shows the spy in green being sucked into a giant funnel!"
    hide yellow
    hide red
    scene black
    with fade
    "Moments later you hear a swooshing noise as a panel in the roof opens up."
    scene bgBase
    with fade
    with hpunch
    pause 0.4
    show green g33 at ri with d3
    s "Oof~...!"
    s "Just in time Jerry! Now pull out the othe-..."
    s g28 "...?"
    s "You're not Jerry!"
    y "No, actually I'm....{w} Errr...{w} The new guy! It's my first day on the jo-..."
    hide green
    with d2
    "With lightning quick reflexes, the spy jumps on you and puts you in a headlock!"
    play sound "audio/sfx/punch1.mp3"
    with hpunch
    y "................."
    y "Why?"
    show green g8 at ri with d3
    s "Don't move Agent! We've been fighting you guys all day! I don't know what's going on, but you're not getting the drop on me."
    y "K."
    s g17 "What do you mean 'K'?"
    y "I mean I won't attack."
    s g8 "Nice try! But you're not fooling anyone!"
    y "............................."
    s g32 "............................."
    "................................"
    y "I'm sorta getting a cramp in my neck, so if you could~...."
    "The spy narrows her eyes as she gives you a cautious look."
    s g31 "You... sure don't act like the other agents..."
    "The spy frees you from the neckhold."
    y "Didn't your friends need help or something...?"
    s g28 "O-oh! You're rig-...!"
    "*{b}Bleep* *Bleep* *Bleep*{/b}"
    s "It's the distress signal!"
    hide green
    with d3
    "The two of you run over to the console and answer the call."
    scene bgSchool1
    with fade
    show yellow y28:
        xalign 0.9
    show red r8:
        xalign 0.1 xzoom -1
    show scene_camera
    with d3
    a "Sam! They found us!"
    c "Please get us out of here!"
    sM "Hang on, I got you!"
    play sound "audio/sfx/static1.mp3"
    show bgStatic onlayer minigame
    pause 0.1
    hide bgStatic onlayer minigame
    pause 0.3
    show bgStatic onlayer minigame
    pause 0.2
    hide bgStatic onlayer minigame
    pause 0.2
    hide red
    hide yellow
    show bgStatic
    "{b}*Static*{/b}"
    sM "Clover?! Alex?!"
    scene bgBase
    show scene_darkening
    with d2
    show green g29 at ri with d3
    s "The tunnel system! It's not responding!"
    s g14 "No....{w} They must have destroyed it..."
    y "{i}'They'{/i}?"
    s g15 "............."
    s "WOOHP... The Agency... It's gone rogue."
    s g37 "All of our Agents just... turned on us. In the middle of school no less! I was busy studying!"
    y "........."
    s g34 "They brought in gangs from out of state and began causing chaos in the city."
    s "They've declared Beverly Hills lawless. Turning it into a playground for gangsters and thugs."
    y "Man that must suck for you."
    s g28 "It sucks for you too!"
    y "It does?"
    s g8 "Of course! You're a WOOHP Agent yourself, right?"
    y "Oh right... about that~..."
    y "I was only one day away from retirement so..."
    s g34 "You said it was your first day."
    y "........................"
    y "So about that~...."
    s g9 "Ugh, okay fine. What do you want?"
    y "Huh...?"
    s "I'm going to need your help and you must want something. Just tell me what you want in return for your help."
    y "...."
    $ task7Text = "We need to safe the world! But... let's start with saving Beverly Hills. We need to find a way to liberate the city and find out who's behind this operation."
    menu:
        "Power" if True:
            y "Absolute unchallenged POWER!"
            s g34 "Are you willing to work for it?"
            y "Huh?"
            s g31 "Are you willing to put in the time and effort?"
            s "If so, then I'll make sure you become one of the bigshots at WOOHP. Then you'll have all the power you could ever want."
            y "..........."
            y "Tempting~..."
            s "But for now WOOHP is under enemy control. So I'll need you as a plan B."
            y "Er... deal?"
        "Wealth" if True:
            y "Money would be nice."
            s g34 "How much money?"
            y "Like...{w} I dunno~...{w} A million dollars!"
            s g31 "Are you willing to work for it?"
            y "..........."
            y "Wait what?"
            s "Are you willing to work for it?"
            y "Yeeees~...?"
            s g34 "Fine, then I'll make sure that after all this is over, you'll be rewarded with a million dollars."
            y "Are you serious? Sweet!"
            s g31 "BUT!{w} You need to be willing to work for it. If we're going to take back Beverly Hills and restore order, then you're gonna have to put in the effort."
            y "Deal!"
        "Tiddies" if True:
            y "......"
            y "Tiddies."
            $ tiddyPerk = True
            s g8 "WHAT?! How vulgar!"
            s g38 "I'm not showing you mine, if that's what you're implying!"
            y "Don't flatter yourself. I want to see some good tiddies."
            play sound "audio/voice/what.mp3"
            s g16 "W-what...?!"
            y "You know the ones you want to show off to your friends and brag about."
            s g11 "................."
            s g12 "Well! .... I don't know how to get you those, okay?!"
            y "You're in college, you must know some good strippers."
            s g8 "No! I don't!"
            y "Oh well.{w} Good luck with the whole WOOHP problem."
            s g28 "Wait! Where are you going?"
            y "To find some tiddies!"
            s g9 "{b}*Groans*{/b}"
            s "If I show you mine~...{w} Do you then promise to help...?"
            y "Maybe. They gotta be good tiddies though."
            s "......................"
            s g14 "{b}*Sighs*{/b} Fine~..."
            hide green
            with d3
            play sound "audio/sfx/cloth.mp3"
            $ greenArms = 3
            $ greenOutfit = 2
            $ greenOutfitArms = 3
            show green g11 at ri with d3
            s "........................."
            y "Okay I take it back....{w} Them be some good tiddies."
            s g12 "{b}*Sarcastic*{/b} Gee~... thanks."
            s g16 "So will you help now?"
            y "Yeah why not. Not like I got anything better to do anyways."
            hide green
            with d3
            play sound "audio/sfx/cloth.mp3"
            $ greenArms = 1
            $ greenOutfit = 1
            $ greenOutfitArms = 1
            show green g38 at ri with d3
    s g38 "Fine, then let's discuss a plan of action."
    s g34 "We should focus on infiltrating WOOHP, taking out the guards and fighting our way to the top. Then, we can confront the person who's behind this and put them in handcuffs!"
    y "................"
    y "Solid plan. Now here's my proposal...{w} We don't do any of the things you just said."
    s g28 "What? Why not?!"
    y "You want us to take on an entire organization by ourselves? That's gonna get us killed."
    y "How about instead, we lay low for a while. Figure out what the situation is on the streets and why WOOHP turned rogue in the first place?"
    s g38 "Ehrm... I'm sorry, but {i}'who'{/i} is the experienced super spy here?"
    y "You are....?"
    s "Exactly. Now stop arguing and just do what I tell you."
    y "......................"
    s g39 "......................"
    s g12 "Well...."
    s "You might have a point about taking on the entire organization with just the two of us..."
    y "Told ya."
    s g32 "Okay fine. I've decided that we'll lay low first and gather some intel."
    y "........"
    y "Good! Then that's settled. {w}I'm going to bed."
    s g28 "Hey! You said you'd help me!"
    y "And I will... in the morning. Or do you fancy going outside at night with all the gangs around?"
    s g32 "................."
    s "Okay fine... We'll wait till tomorrow then..."
    hide green
    hide scene_darkening
    with d3
    "The two of you find a comfortable cell to stay in and head to bed."
    scene black with longFade
    $ renpy.pause(1.0, hard='True')
    jump tutStage3

label tutStage3:
    $ tutStage = 3
    show text "The night passes and all is quiet."
    with d5
    pause 1.5
    hide text
    with d5
    pause 1.0
    scene bgBase with fade
    pause 1.0
    show scene_darkening
    with d3
    pause 1.0
    if spyGreenActive == True:
        show green g1 at ri with d3
        s "Good morning New Guy."
        y "Good morning. Get any rest?"
        s g14 "A little. I'm eager to get started today."
        y "Let's get the lay of the land. See what's happening out there on the streets."
        s g38 "Well I think....!"
        s g39 "..................."
        s g38 "Well I also think we should get a lay of the land."
        hide green
        hide scene_darkening
        with d3
        scene black with fade
        pause 0.5
        "The two of you take the elevator upstairs and step out of the milkshake bar."
        play music "audio/sfx/warzone.mp3" fadein 1.5
        scene bgMap with longFade:
            xalign 0.63 yalign 0.3
        sM "Beverly Hills... Look what they did to it...."
        y "Yeah it looks like we got our work cut out for us."
        sM "I'll do some digging around. You keep watch here and wait for me to come back."
        y "........."
        "Sam gets ready and heads out into the city."
        y "Yeah I'm gonna do some exploring."
        $ spy1Status = 2
        call screen mapButtons
    if spyRedActive == True:
        show red:
            xalign 1.0 yalign 0.0
        with d3
        c "Good morning New Guy."
        y "Good morning. Got any rest?"
        c "A little. I'm eager to get started today."
        y "Let's get a lay of the land. See what's happening out there on the streets."
        hide red
        hide scene_darkening
        with d3
        scene black with fade
        pause 0.5
        "The two of you take the elevator upstairs and step out of the milkshake bar."
        play music "audio/sfx/warzone.mp3" fadein 1.5
        scene bgMap with longFade:
            xalign 0.63 yalign 0.3
        cM "Beverly Hills... Look what they did to it....{w} My favorite shoe store is on fire!"
        y "Yeah it looks like we got our work cut out for us."
        cM "I'll do some digging around. I'll meet you back here tonight."
        "Clover gets ready and heads out into the city."
        y "Right, let's do some exploring."
        $ spy2Status = 2
        call screen mapButtons

label tutStage4:
    $ tutStage = 4
    scene bgStreet2 with fade
    "It's still early in the morning and everything is quiet. The streets are littered with gunshell casings, burned up cars and dumpsters, shattered glass and the occassional passed out drunk."
    y "{b}*Whistling*{/b}"
    "Turning a corner you suddenly see a gangs of thugs listening to a girl on a soapbox."
    "As soon as they notice you, they come straight at you."
    y "{b}*Worried Whistling*{/b}"
    "Thug 1" "You thought you could just come in on our turf and start whistling?!"
    "Thug 2" "Hey my mom got hit by a driver who was whistling!"
    "Thug 1" "Who do you think you are? Coming here and reminding my friend of such a tragic incident. I think we need to teach you a lesson!"
    y "{b}*Paniced Whistling*{/b}"
    "???" "Un moment~... Zis one is with moi~..."
    stop music fadeout 1.5
    show scene_darkening
    with d5
    $ silHair = 2
    $ silOutfit = 2
    show silvaModel:
        xalign 1.0 yalign 0.0
    with d3
    play music "audio/music/silva2.mp3" fadein 1.5



    "???" "My my my, look who's made it out of ze asylum~..."
    "???" "Why are you dressed like a WOOHP Agent...?"
    y "Why are you dressed like a potted plant?"
    "???" "Oh! You don't know who I am? I am Silva Abegail. World famous botanist and plant-whisperer!"
    "Silva" "Look around you. Not bad, non? Our own little corner of ze world, ripe for ze plunder~..."
    y "You planned all this?"
    "Silva" "Oh heaven no! That credit goes to ze mastermind of this operation. It was his idea to use WOOHP's nanobots against zem."
    y "Nanobots?!"
    "Silva" "Nanobots."
    y "Nanobots....?"
    "Silva" "Oui... nanobots."
    y "How...{w} cliché."
    "Silva" "All that was required was a little... 'reprogramming'. And now zey are fighting for us!"
    "Silva" "Ze mastermind freed us from our cells to prove ourselves. We all took control of gangs here in ze city. I'm in command of 'Les Épines'."
    "Silva" "Ze one who manages to take over all of Beverly Hills can join ze mastermind in his conquest for world domination."
    "You turn your attention to the gangsters."
    y "And you're okay with this?"
    "Thug" "I'LL DO WHATEVER MISS ABEGAIL SAYS!!!"
    y "............................."
    "Silva" "Oh zey don't have much of a choice. {w}Afterall~... We've infected {i}them{/i} with nanobots aswell..."
    "Silva" "Now your presence here sort of leaves me in a bind~..."
    "Silva" "I have nothing against you mon ami, but I can't have a rival standing in my way..."
    menu:
        "'I'm not a threat to you!'" if True:
            y "Listen here {i}'mon cheri'{/i}~..."
            y "Just because I broke out of a insane asylum with supervillains, doesn't mean I want to take over the world."
            y "You go and have a blast taking over the world while I worry about getting a dayjob."
            sil "But zat is so boring! Wouldn't you much rather be powerful? Own your own country~...?"
            sil "Have everything you've ever wanted...."
            y "I already have Netflix. What more could I want?"
            y "Sorry lady, but the villain lifestyle is not for me."
        "'Neat, I wanna be a gangster'" if True:
            y "A rival? Starting my own gang sounds pretty cool, but I need a theme~..."
            y "What about a bee theme! Every superhero universe has a bee-themed villain!"
            sil "Really? A bee could go well with my flower theme~.... If you know what I'm saying~...."
            y "Yes I know what you're insinuating."
            sil "Well then maybe you and I shou-..."
            y "Cause bees pollinate flowers."
            sil "Yes... So maybe you and I sho-..."
            y "Sex. You're talking about sex."
            sil "..........................."
            y "Also the answer is no."
            y "You just said that you were trying to get rid of your rivals, so you'll betray me at the first opportunity you get."
            y "How about you go play gangster while I look for a respectable job! {w}Like zookeeper."
        "*Say something crazy*" if True:
            y "Je ne parle pas français!"
            sil "I'm... I'm not speaking French~..."
            y "Où est la plage?"
            sil "..............."
            y "Eiffel Tower, omelette du fromage, Napoleon!"
            sil "Now you're just shouting random phrases~..."
            y "Tour the France?"
            sil "Ah right... I forgot that you were crazy..."
    sil "{b}*Le sigh*{/b} Too bad~... I do like you. {w}Even if you are a bit coo-coo..."
    sil "Run along now~... If you're not a gangleader than I have no problem with you."
    y "Er... thanks."
    sil "Good luck out zere~... Try to not get shot~... ♥"
    hide silvaModel
    hide scene_darkening
    with d3
    "The gangsters turn away from you as you quickly return to the milkshake bar."
    stop music fadeout 1.5
    scene black with longFade
    pause 0.5
    scene bgClub0
    with d3
    pause 0.5
    show scene_darkening
    with d3
    pause 1.0
    if spyGreenActive == True:
        show green g10 at ri with d3
        s "Oh there you are, New Guy.{w} I was beginning to worry. Didn't I tell you to stay here and guard the bar?"
        y "Yeah, but I got bored. So found out anything new?"
        s "Yeah I did. Did you?"
        y "Yup."
        s "Then you go first."
        y "Well... nanobots are causing our agents to turn bad. They're now supporting local gangs in a bid for dominance over the city."
        y "The gangs are being led by Ex-WOOHP convicts. The first to take over the entire city gets to join the guy who orchestrated this whole thing."
        y "Your turn."
        s g34 "Well...."
        hide green
        scene black
        with fade
        play music "audio/music/ambient1.mp3" fadein 1.5
        scene bgMap:
            xalign 0.63 yalign 0.3
        with fade
        sM "Right now, Beverly Hills is divided by multiple gangs. The three biggest ones are..."
        show bgMap:
            linear 0.5 xalign 0.0 yalign 0.2
        pause 0.8
        sM "'Aces'. The cool rich kids that set up near the marina."
        show bgMap:
            linear 0.5 xalign 1.0 yalign 1.0
        pause 0.8
        sM "'Drift Punk', tech geeks and nerds, which are located near sillicon valley."
        show bgMap:
            linear 0.5 xalign 1.0 yalign 0.0
        pause 0.8
        sM "And the 'Outsiders'. Punkers and goth kids. Basically the freaks that never fit in. They're set up to the north."
        sM "I've managed to get in touch with a contact inside the Aces. He might be able to help us in the future."
        show screen mapButtons
        scene bgMap:
            xalign 1.0 yalign 0.0
            linear 0.8 xalign 0.0 yalign 0.0 zoom 0.5
        pause 1.3
        play sound "audio/sfx/drama1.mp3"
        image daggerAces = "gui/daggerAces.png"
        show daggerAces:
            xpos 80 ypos 150
        $ gang1Active = True
        pause 0.5
        sM "And then there's the smaller gangs. I couldn't find out what they're all about, but Beverly Hills is divided up like this."
        hide daggerAces
        show mapGangs
        with d3
        sM "The only area that's considered neutral ground is..."
        hide mapGangs
        hide screen mapButtons
        show bgMap:
            linear 0.47 xalign 0.52 yalign 0.0 zoom 1.0
        pause 0.8
        sM "The mall."
        y "The mall?"
        sM "Yeah, afterall, what good is all your stolen money if you don't have a place to spend it?"
        y "That makes a weird kind of sense."
        stop music fadeout 3.5
        scene black
        hide bgMap
        with d3
        scene bgClub0 with fade
        show green g35 at ri with d3
        s "So at least we sort of know what we're up against..."
        s "................."
        s g39 "Despite going against my direct orders for you to stay put...."
        s g38 "I guess you did well and I have to applaud the initiative."
        s "Up next I think we should..."
        s g39 "................."
        s g18 "Ehrm....."
        s "What do you think we should do next?"
        y "Well..."
        y "We should focus on breaking the nanobot control over our agents.{w} With them on our side we can begin taking steps to take back the city."
        y "So if we break the control over our agents... We could send them to help us take back the HQ."
        s g31 "But how do we do that?"
        y "I was thinking... that we bring one back here."
        y "Once here, we can figure out how to break the nanobot control over them."
        s g35 "There were plenty of Agents at the school. They might still be there. It's risky, but I bet I could sneak in again."
        s "Knocking an Agent out shouldn't be that hard. The tricky part will be transporting him back here."
        y "There's a workbench downstairs. I'm sure I can fix you something up that will help you with that."
        s "Okay good. I approve your plan."
        s "I'll leave you to craft the gadget and set up a mission via the Mission Screen."
        hide scene_darkening
        hide green
        with d3
        scene bgBase
        with fade
        call screen tutBase

    if spyRedActive == True:
        call callRed from _call_callRed_4
        c "Oh there you are, New Guy."
        y "Hey Clover. Found out anything new?"
        c "I like... brought back the biggest news! You go first though."
        y "Well... nanobots are causing our agents to turn bad. They're now supporting local gangs in a bid for dominance over the city."
        y "The gangs are being led by Ex-WOOHP convicts. The first to take over the entire city gets to join the guy who orchestrated this whole thing."
        y "Your turn."
        c "Well...."
        hide green
        scene black
        with fade
        play music "audio/music/ambient1.mp3" fadein 1.5
        scene bgMap:
            xalign 0.63 yalign 0.3
        with fade
        cM "Right now, Beverly Hills is divided by multiple gangs. The three biggest ones are..."
        show bgMap:
            linear 0.5 xalign 0.0 yalign 0.2
        pause 0.8
        cM "'Aces'. The cool rich kids that set up near the marina."
        show bgMap:
            linear 0.5 xalign 1.0 yalign 1.0
        pause 0.8
        cM "'Drift Punk', tech geeks and nerds, which are located near sillicon valley."
        show bgMap:
            linear 0.5 xalign 1.0 yalign 0.0
        pause 0.8
        cM "And the 'Outsiders'. Punkers and goth kids. Basically the freaks that never fit in. They're set up to the north."
        cM "While exploring around, I came across this one geeky looking nerd from Drift Punk. He seemed interested in me... bleh~..."
        cM "But I guess if we need a contact within the gang, then that's our in. He might be able to help us in the future."
        show screen mapButtons
        scene bgMap:
            xalign 1.0 yalign 0.0
            linear 0.8 xalign 0.0 yalign 0.0 zoom 0.5
        pause 1.3
        play sound "audio/sfx/drama1.mp3"
        image daggerPunk = "gui/daggerPunk.png"
        show daggerPunk:
            xpos 950 ypos 450
        $ gang2Active = True
        pause 0.5
        cM "And then there's the smaller gangs. I couldn't find out what they're all about, but Beverly Hills is divided up like this."
        hide daggerPunk
        show mapGangs
        with d3
        cM "Luckily the biggest thread so far has been avoided! The only area that's considered neutral ground is..."
        hide mapGangs
        hide screen mapButtons
        show bgMap:
            linear 0.47 xalign 0.52 yalign 0.0 zoom 1.0
        pause 0.8
        cM "The mall!"
        y "The mall?"
        cM "Yeah, afterall, they're not savages. They need their three daily trips to the mall as much as anyone."
        y "............."
        cM "Oh right and of course they need to place to buy stuff. What good is all your stolen money if you don't get to spend it?"
        y "That makes a weird kind of sense."
        stop music fadeout 3.5
        scene black
        hide bgMap
        with d3
        scene bgClub0 with fade
        call callRed from _call_callRed_5
        c "So at least we sort of know what we're up against..."
        c "What comes next?"
        y "We should focus on breaking the nanobot control over our agents.{w} There's a bullet train downstairs that could take us to the WOOHP HQ, but we're not going to re-capture it by ourselves."
        y "So if we break the control over our agents... We could send them to help us take back the HQ."
        c "But how do we do that?"
        y "I was thinking... that we bring one back here."
        y "Once here, we can figure out how to break the nanobot control over them."
        c "There were plenty of Agents at the school. They might still be there. It's risky, but I bet I could sneak in again."
        c "Knocking an Agent out shouldn't be that hard. The tricky part will be transporting him back here."
        y "There's a workbench downstairs. I'm sure I can fix you something up that will help you with that."
        c "Okay good. In that case I'll leave you to craft the gadget and set up a mission via the Mission Screen."
        hide scene_darkening
        hide red
        with d3
        scene bgBase
        with fade
        call screen tutBase

    if spyYellowActive == True:
        ""


default tutMilkshake = True
default tutClean = True
default tiddyPerk = True
label tutLift:
    if tutStage == 1:
        if playerOutfit == 1:
            $ tutStage = 2
            jump tutStage2
    if tutStage == 1 and playerOutfit != 1:
        yInmate "Wait... I can't head out like this! {w}I'll never get a job and reintegrate into society looking like a convict."
        yInmate "Let's look for some clothes first."
        call screen tutBase
    if tutStage == 2:
        yInmate "Nope... Not going out there right now."
        call screen tutBase
    if tutStage == 4:
        y "I gotta focus on crafting that gadget and planning a mission first."
        call screen tutBase
    if tutStage == 6:
        y "There's still penty of time left. I could spend some time cleaning the bar."
        menu:
            "Clean the milkshake bar" if True:
                scene bgBar
                with fade
                "{b}*Splosh* *Splosh* *Splosh*{/b}"
                scene black with fade
                $ clubStage += 1
                scene bgBar with fade
                pause 1.0
                hide bgBar
                scene black
                with fade
                "You spend the rest of the evening cleaning the bar. It looks better than before, but there is still a lot to be done."
                stop music fadeout 1.5
                "You decide to head to bed."
                jump tutStage7
            "Never mind" if True:
                call screen tutBase
    elif True:
        jump lift


label tutQuarters:
    if tutStage == 1:
        if playerOutfit == 1:
            y "I'm not heading back into the cellblock..."
            call screen tutBase
        elif True:
            yInmate "I'm not heading back into the cellblock..."
            call screen tutBase
    if tutStage == 2:
        menu:
            "Call Sam" if spyGreenActive:
                if tutStage == 2:
                    show scene_darkening
                    with d3
                    show green g15 at ri with d3
                    s "You called, [playerName]?"
                    label tutSocialSam:
                        pass
                    menu:
                        "???" if True:
                            jump tutSocialSam
                        "Chat" if True:
                            s "........."
                            y "What's on your mind?"
                            s g14 "My friends...{w} If I acted more quickly, I could have gotten them out before they were captured..."
                            y "Yeah, you messed up. Not one of your brightest moments."
                            s g4 "H-hey...! Don't say that..."
                            y "Oh wait... This is one of those 'make you feel better' moments. I'm sorry."
                            y "In that case, please don't worry about it. You couldn't have known that I was still one of the good guys."
                            y "And I'm sure they're fine. We're gonna get this sorted out and they'll be back before you know it. Okay?"
                            s g19 "Y-yeah... Okay~..."
                            y "No, but seriously though. Manage your priorities in the future."
                            s g4 "{b}*Sniff*{/b} H-hey..!"
                            hide green with d3
                            jump tutSocialSam
                        "Change naming" if True:
                            y "You know that my name isn't actually 'New Guy', right?"
                            s "I figured, but that's what I'm gonna keep calling you. Can't get attached."
                            y "..................."
                            jump tutSocialSam
                        "Back" if True:
                            jump tutQuarters
            "Call Clover" if spyRedActive:
                if tutStage == 2:
                    show scene_darkening
                    with d3
                    show red:
                        xalign 1.0 yalign 0.0
                    with d3
                    c "You called, [playerName]?"
                    label tutSocialClover:
                        pass
                    menu:
                        "???" if True:
                            jump tutSocialClover
                        "Chat" if True:
                            c "........."
                            y "What's on your mind?"
                            c "Like... It's nothing! Don't you have anything better to do?"
                            y "..............."
                            c "Okay fine~...{w} I'm thinking about my friends...{w} If I acted more quickly, I could have gotten them out before they were captured..."
                            y "Yeah, you messed up. Not one of your brightest moments."
                            c "H-hey...! Don't say that..."
                            y "Oh wait... This is one of those 'make you feel better' moments. I'm sorry."
                            y "In that case, please don't worry about it. You couldn't have known that I was still one of the good guys."
                            y "And I'm sure they're fine. We're gonna get this sorted out and they'll be back before you know it. Okay?"
                            c "Y-yeah... Okay~..."
                            y "No, but seriously though. Manage your priorities in the future."
                            c "{b}*Sniff*{/b} H-hey..!"
                            hide red with d3
                            jump tutSocialClover
                        "Change naming" if True:
                            y "You know that my name isn't actually 'New Guy', right?"
                            c "Well you're new around here, aren't you? It sounds like a fitting name for you."
                            y "..................."
                            jump tutSocialClover
                        "Back" if True:
                            jump tutQuarters
            "Call Alex" if spyYellowActive:
                if tutStage == 2:
                    show scene_darkening
                    with d3
                    show yellow:
                        xalign 1.0 yalign 0.0
                    with d3
                    a "You called, [playerName]?"
                    label tutSocialAlex:
                        pass
                    menu:
                        "???" if True:
                            jump tutSocialAlex
                        "Chat" if True:
                            a "........."
                            y "What's on your mind?"
                            a "I'm thinking about my friends...{w} If I acted more quickly, I could have gotten them out before they were captured..."
                            y "Yeah, you messed up. Not one of your brightest moments."
                            a "{b}*Sniff*{/b} Yeah..."
                            y "Oh wait... This is one of those 'make you feel better' moments. I'm sorry."
                            y "In that case, please don't worry about it. You couldn't have known that I was still one of the good guys."
                            y "And I'm sure they're fine. We're gonna get this sorted out and they'll be back before you know it. Okay?"
                            a "Y-yeah... Okay~..."
                            y "No, but seriously though. Manage your priorities in the future."
                            a "{b}*Sniff*{/b} H-hey..!"
                            hide yellow with d3
                            jump tutSocialAlex
                        "Change naming" if True:
                            y "You know that my name isn't actually 'New Guy', right?"
                            c "It's not?!"
                            y "..................."
                            a "Oh I'm sorry... I'm not very good with names. I'm just gonna keep calling you New Guy, okay?"
                            jump tutSocialAlex
                        "Back" if True:
                            jump tutQuarters
            "Go to sleep" if True:
                jump tutStage3
            "Never mind" if True:
                jump tutBase
        "Nope... Not going out there right now."
        call screen tutBase
    if tutStage == 4:
        y "I should craft a gadget and then set up a mission via the mission screen."
        call screen tutBase
    if tutStage == 6:
        menu:
            "Call Sam" if spyGreenActive:
                y "Sam?"
                s "I'm trying to sleep!"
                call screen tutBase
            "Call Clover" if spyRedActive:
                y "Clover?"
                c "Get lost!"
                call screen tutBase
            "Call Alex" if spyYellowActive:
                y "Alex?"
                a "I can't hear you! I'm sleeping!!"
                call screen tutBase
            "Go to sleep" if True:
                y "Sleeping at 6pm... Well I guess I don't have anything better to do."
                jump tutStage7
            "Never mind" if True:
                call screen tutBase
    elif True:
        jump quarters

label tutMissions:
    if tutStage == 1:
        $ tutMissions = True
        y "TV!"
        y "No wait...{w} It's some kind of Mission Planner. Best to not touch it."
        call screen tutBase
    if tutStage == 2:
        y "I wish this thing would show football games... Oh well, best turn in for the night. There should be plenty of cells."
        call screen tutBase
    if tutStage == 4:
        y "This is the mission screen. I should craft that gadget first though."
        call screen tutBase
    if tutStage == 6:
        y "It's getting too late to plan a mission right now."
        call screen tutBase

label tutCreditcards:
    if tutStage == 1:
        $ tutCreditCard = True
        y "(Some complicated machine. It reads: {i}'Please insert Credit Card Number'{/i})"
        call screen tutBase
    if tutStage >= 2:
        jump creditcards

label tutPrison:
    if tutStage == 1:
        if playerOutfit == 1:
            y "I've already checked this out."
            call screen tutBase
        elif True:
            yInmate "This hatch seems to lead to another room downstairs."
            yInmate "Let's have a quick peak~..."
            scene black with fade
            yInmate "...?"
            play sound "audio/sfx/itemGot.mp3"
            "You find {color=#ffeda6}Agent Suit{/color}."
            $ playerOutfit = 1
            scene bgBase with fade
            y "That's more like it!"
            y "With a gettup like this I'm sure someone will hire me!"
            call screen tutBase
    if tutStage == 2:
        y "I can sleep in the cellblock for now."
        call screen tutBase
    if tutStage == 4:
        y "This underground room would make a good place to keep the WOOHP agent if we capture him..."
        call screen tutBase
    elif True:
        "Just an underground room."
        call screen tutBase

label tutSpyCamera:
    if tutStage == 1:
        if playerOutfit == 1:
            y "Spy Drones...? I bet I could see what all of WOOHP's spies are up to by tuning into this."
            "{b}*Bleep*{/b}"
            y "Aw... It needs a password."
            call screen tutBase
        elif True:
            yInmate "Spy Drones...? I bet I could see what all of WOOHP's spies are up to by tuning into this."
            "{b}*Bleep*{/b}"
            yInmate "Aw... It needs a password."
            call screen tutBase
    if tutStage == 2:
        y "I don't have the password for it."
        call screen tutBase
    if tutStage == 4:
        y "Still don't have the password..."
        y "Wait let me just try something..."
        menu:
            "Type in: '12345'" if True:
                pass
            "Type in: 'WOOHP'" if True:
                pass
            "Type in: 'pistachios'" if True:
                pass
        "'{i}Access granted'{/i}"
        "Who do you wish to spy on?"
        menu:
            "Sam" if True:
                if spyGreenActive == True:
                    scene black with fade
                    scene bgClub0
                    with fade
                    show green g11 at ri with d3
                    show scene_camera
                    with d3
                    s "I wish I had a boyfriend who would take me to an old-timey milkshake bar..."
                    s g18 "...?"
                    s g16 "Why do I feel like someone's watching me...?"
                    hide green
                    with d3
                    scene black
                    hide scene_camera
                    with fade
                    scene bgBase with fade
                elif True:
                    "Error. Location unknown."
                call screen tutBase
            "Clover" if True:
                if spyRedActive == True:
                    scene black with fade
                    scene bgClub0
                    show red:
                        xalign 1.0 yalign 0.0
                    show scene_camera
                    with fade
                    c "I wonder how many calories are in a milkshake..."
                    c "...?"
                    c "Why do I feel like someone's watching me...?"
                    hide red
                    with d3
                    scene black
                    hide scene_camera
                    with fade
                    scene bgBase with fade
                elif True:
                    "Error. Location unknown."
                call screen tutBase
            "Alex" if True:
                if spyYellowActive == True:
                    scene black with fade
                    scene bgClub0
                    show scene_camera
                    with fade
                    show yellow:
                        xalign 1.0 yalign 0.0
                    with d3
                    a "Oh! Found a peanut! {b}*Chomps*{/b}"
                    a "..............."
                    a "I don't feel so good~..."
                    hide yellow
                    with d3
                    scene black
                    hide scene_camera
                    with fade
                    scene bgBase with fade
                elif True:
                    "Error. Location unknown."
                call screen tutBase
            "Never mind" if True:
                call screen tutBase
    if tutStage == 6:
        menu:
            "Spy on Sam" if spyGreenActive:
                scene cellSam
                show scene_camera
                with d3
                "Sam is lying face down on her bed."
                s "Stupid, stupid, stupid! Don't make assumtions like that, Sam!"
                s "Now he'll think that you're some sort of sex-freak."
                "Burying her head into her pillow she let's out a muffled scream in embarrassed frustration."
                scene black
                hide scene_camera
                with d3
                scene bgBase
                jump base
            "Spy on Clover" if spyRedActive:
                scene cellClover
                show scene_camera
                with d3
                "Clover is lying face down on her bed."
                c "Urgh, I just had to open my big mouth!"
                c "Now he's going to think that you're some sort of sex obsessed weirdo!"
                "Burying her head into her pillow she let's out a defeated sigh."
                scene black
                hide scene_camera
                with d3
                scene bgBase
                jump base
            "Spy on Alex" if spyYellowActive:
                scene sideroom
                show scene_camera
                with d3
                "Alex is lying face down on her bed."
                a "I shouldn't have said that..."
                a "It was really mean of me and now he'll think I'm some kind of witch..."
                "Alex lifts her head up briefly before letting it fall down in her pillow again as she breaths a sigh in defeat."
                scene black
                hide scene_camera
                with d3
                scene bgBase
                jump base
    if tutStage == 8:
        scene cellSam
        show scene_camera
        with d3
        hide scene_camera
        show green g11 at ri with d3
        show scene_camera
        with d3
        s ".............."
        s "My clothes aren't that stupid... Are they....?"
        s g4 "Right...?"
        hide green
        scene black
        hide scene_camera
        with d3
        scene bgBase
        with fade
        jump base
    if tutStage == 10:
        scene cellSam
        show green g12 at ri
        show scene_camera
        with d3
        s "{b}*Yawns*{/b} It's so noisy outside, I barely get any sleep. I hope we're safe here..."
        s "All things considered, this is probably one of the safest places in Beverly Hills."
        s g1 "I guess I shouldn't worry too much."
        hide green
        scene black
        hide scene_camera
        with d3
        scene bgBase
        with fade
        jump base
    elif True:
        "DEV: NO EVENT AT THIS TIME INTRO.RPY"
        call screen tutBase

default holeinwall = 0
label tutDesk:
    if tutStage == 1:
        $ tutDesk = True
        if playerOutfit == 1:
            y "(A sturdy desk, filled with advanced tools for crafting gadgets.{w} I'm pretty sure I'm not allowed to mess around with this.)"
            y "..........................."
            menu:
                "Mess around with it" if True:
                    show screen tutHole
                    "You begin rumaging through the gadgets."
                    y "(Camouflage Mascara, Tornado Hairdryer, Instant Freeze Parfume...)"
                    y "(I wonder why all of these are so femininely themed....)"
                    "You pick up a lipstick and begin to examin it."
                    play sound laser1
                    $ holeinwall = 1
                    with bloodbulb
                    pause 0.2
                    y "(Crap, crap, crap, crap!)"
                    y "Let's hope nobody saw that...."
                    $ holeinwall = 0
                    with d3
                    hide screen tutHole
                    call screen tutBase
                "Leave it be" if True:
                    call screen tutBase
        elif True:
            yInmate "(A sturdy desk, filled with advanced tools for crafting gadgets.{w} I'm pretty sure I'm not allowed to mess around with this.)"
            yInmate "..........................."
            menu:
                "Mess around with it" if True:
                    show screen tutHole
                    "You begin rumaging through the gadgets."
                    yInmate "(Camouflage Mascara, Tornado Hairdryer, Instant Freeze Parfume...)"
                    yInmate "(I wonder why all of these are so femininely themed....)"
                    "You pick up a lipstick and begin to examin it."
                    play sound laser1
                    $ holeinwall = 1
                    with bloodbulb
                    pause 0.2
                    yInmate "(Crap, crap, crap, crap!)"
                    yInmate "Let's hope nobody saw that...."
                    $ holeinwall = 0
                    with d3
                    hide screen tutHole
                    call screen tutBase
                "Leave it be" if True:
                    call screen tutBase
    if tutStage == 2:
        y "I'll worry about this stuff later."
        call screen tutBase
    if tutStage == 4:
        $ spy1Status = 0
        y "Okay let's see what I can craft here..."
        y "................."
        y "{i}'Hypno Earrings'{/i}"
        y "{i}'Toss the hypnotic earrings near a target to unleash hypnotic gas.'{/i}"
        y "That sounds useful. Let's craft one of those."
        scene basedesk
        show screen gadgetButtons
        with d3
        call screen deskToolsInterface
    if tutStage == 6:
        y "We're going to have to gather more materials first."
        scene bgBase
        call screen tutBase
    elif True:
        jump desk

label tutBase:
    scene bgBase
    call screen tutBase




image tutMisScreen1 = "gui/tut/tutMisScreen1.jpg"
image tutMisScreen2 = "gui/tut/tutMisScreen2.jpg"
image tutMisScreen3 = "gui/tut/tutMisScreen3.jpg"
image tutMisScreen4 = "gui/tut/tutMisScreen4.jpg"


label tutMissionSetup:
    pause 1.0
    hide baseDesk
    hide screen deskButtons
    hide screen gadgetButtons
    hide screen deskToolsInterface
    show bgBase
    with d3
    pause 1.0
    show scene_darkening
    with d3
    y "I followed the instructions to a T, so this should work... {w}Hopefully."
    y "Now to set up a mission via the Mission Screen."
    "You walk over to the mission screen and boot it up."
    "New User Detected. Playing tutorial."
    show tutMisScreen1
    with d3
    pause 0.5
    "First choose your frontline spy over here."
    hide tutMisScreen1
    show tutMisScreen2
    with d3
    pause 0.5
    "Followed by picking a location..."
    hide tutMisScreen2
    show tutMisScreen3
    with d3
    pause 0.5
    "Finally, you can add gadgets to support your spy during a mission here."
    show tutMisScreen4
    with d3
    pause 0.5
    "Once you're done, simply click on FINISH >>."
    y "That's pretty straight forward."
    if spyGreenActive == True:
        sM "Did you get it to work?"
    if spyRedActive == True:
        c "Did you get it to work?"
    if spyYellowActive == True:
        a "Did you get it to work?"
    y "Yeah I think so. Let's set up a mission."
    $ tod = 2
    hide tutMisScreen4
    scene missionScreenBG
    with d3
    call screen missionScreenButtons




screen tutorialStun:
    vbox xalign 0.451 yalign 0.412:
        imagebutton:
            idle "mission/castle/props/obst/agentNeutralFull2.png"
            hover "mission/castle/props/obst/agentNeutralFull2-hover.png"
            action Jump("tutorialStun")

label tutStage5:
    $ capturedAgents += 1
    hide spyCornerSide
    $ randomObst2 = 0
    y "Wait! Someone's coming!"
    pause 0.4
    show agentNeutral:
        xalign 0.68 yalign 0.50 zoom 0.20 rotate 5
    with d3
    pause 0.9
    hide agentNeutral
    with d3
    pause 0.5
    show agentNeutral:
        xalign 0.365 yalign 0.43 rotate 2 zoom 0.55
    with d3
    pause 0.5




    play sound "audio/voice/agent/agentAgentHere.mp3"
    "Agent" "Hallway clear and everything is A-OK!"
    if missionScreenGadget1Select == 0 and missionScreenGadget2Select == 0 and missionScreenGadget3Select == 0 and missionScreenGadget4Select == 0:
        $ missionScreenGadget1Select = 1
    y "Now is your chance!"
    if activeSpy == 1:
        s "Right!"
    if activeSpy == 2:
        c "Right!"
    if activeSpy == 3:
        a "Right!"
    play sound "audio/sfx/compowder.mp3"
    $ randomObst1 = 1
    $ tutStage = 5
    show screen equipmentMenu
    $ renpy.pause(hard='True')

label tutHypno:
    hide spyCorner
    with d2
    show spyThrowBack1:
        xalign 0.75 yalign 0.77 zoom 0.71 xzoom -1
    with d2
    pause 0.3
    hide agentNeutral
    show agentNeutral:
        xalign 0.365 yalign 0.43 rotate 2 zoom 0.55 xzoom -1
    with d3
    "Agent" "Hey, you're that spy-..."
    hide spyThrowBack1
    show spyThrowBack2:
        xalign 0.75 yalign 0.77 zoom 0.71 xzoom -1
    with d1
    pause 0.1
    $ gadgetEarrings -= 1
    $ randomObst1 = 0
    hide agentNeutral
    show agentGuardTut:
        xalign 0.365 yalign 0.49 rotate 2 zoom 0.50 xzoom -1
    play sound "audio/sfx/poof1.mp3"
    show gadgetCloud1:
        xalign 0.40 yalign 0.3
    pause 0.2
    hide gadgetCloud1
    with d5
    pause 0.2
    jump tutorialStun





layeredimage spyFallingTut:
    always:
        "mission/models/spyFallBase1.png"
    if activeSpy == 3:
        "mission/models/sam/spyFallingSuit1.png"
    if activeSpy == 3:
        "mission/models/sam/spyFallingHair1.png"
    if activeSpy == 3:
        "mission/models/sam/spyFallingFace1.png"
    if activeSpy == 1:
        "mission/models/clover/spyFallingSuit1.png"
    if activeSpy == 1:
        "mission/models/clover/spyFallingHair1.png"
    if activeSpy == 1:
        "mission/models/clover/spyFallingFace1.png"
    if activeSpy == 2:
        "mission/models/alex/spyFallingSuit1.png"
    if activeSpy == 2:
        "mission/models/alex/spyFallingHair1.png"
    if activeSpy == 2:
        "mission/models/alex/spyFallingFace1.png"


image evilSamDrama = "gui/tut/evilSam.png"
image evilCloverDrama = "gui/tut/evilClover.png"
image evilAlexDrama = "gui/tut/evilAlex.png"
image evilCloverShoot = "gui/tut/evilCloverShoot.png"
image evilAlexShoot = "gui/tut/evilAlexShoot.png"
image evilCloverShoot = "gui/tut/evilCloverShoot.png"
image dramaShotGreen = "gui/tut/dramaShotGreen.png"
image dramaShotRed = "gui/tut/dramaShotRed.png"
image dramaShotYellow = "gui/tut/dramaShotYellow.png"

label tutorialStun:
    $ _skipping = True
    "Agent" "{b}*Cough* *Cough*{/b}"
    "Agent" "I feel funny!"
    if activeSpy == 1:
        s "It's working!"
        y "Quickly, tell him to return to the Safehouse."
        s "{b}*Ahem*{/b} {i}'Agent! Listen closely...'{/i}"
        s "{i}'Return to the old Milkshake bar downtown, right away!'{/i}"
        hide agentGuardTut
        show agentNeutral:
            xalign 0.365 yalign 0.43 rotate 2 zoom 0.55 xzoom -1
        with d3
        play sound "audio/voice/agent/agentSmokeIsFilling.mp3"
        "Agent" "{i}'Smoke is filling my lungs, but I am always interested in a dairy beverage!'{/i}"
        hide agentNeutral
        with d3
        pause 0.4
        "The zombiefied guard slowly begins making his way down the hallways, towards the exit."
        s "It worked!"
    if activeSpy == 2:
        c "It's working!"
        y "Quickly, tell him to return to the Safehouse."
        c "Totally. {b}*Ahem*{/b} Hey Agent! Like... head over to the milkshake bar downtown! Chop chop!"
        hide agentGuard
        show agentNeutral:
            xalign 0.365 yalign 0.43 rotate 2 zoom 0.55 xzoom -1
        with d3
        play sound "audio/voice/agent/agentSmokeIsFilling.mp3"
        "Agent" "{i}'Smoke is filling my lungs, but I am always interested in a dairy beverage!'{/i}"
        hide agentNeutral
        with d3
        pause 0.4
        "The zombiefied guard slowly begins making his way down the hallways, towards the exit."
        c "It worked!"
    if activeSpy == 3:
        a "It's working!"
        y "Quickly, tell him to return to the Safehouse."
        a "{b}*Ahem*{/b} {i}'Agent! Listen closely...'{/i}"
        a "{i}'Return to the old Milkshake bar downtown, right away!'{/i}"
        hide agentGuard
        show agentNeutral:
            xalign 0.365 yalign 0.43 rotate 2 zoom 0.55 xzoom -1
        with d3
        "Agent" "{i}'Smoke is filling my lungs, but I am always interested in a dairy beverage!'{/i}"
        hide agentNeutral
        with d3
        pause 0.4
        "The zombiefied guard slowly begins making his way down the hallways, towards the exit."
        a "Yes! It worked!"

    y "Good. Get out of there befor-...."
    hide spyThrowBack2
    stop music
    play sound "audio/sfx/glassBreaking.mp3"
    show spyCorner:
        xalign 0.90 yalign 0.83 zoom 0.78
    with d2
    pause 0.6
    show spyFallingTut:
        xalign 0.67 yalign -0.5 zoom 0.21
        linear 0.32 xalign 0.67 yalign 0.535
    pause 0.34
    hide spyFallingTut
    show spyFightTut:
        xalign 0.70 yalign 0.515 rotate 4 zoom 0.265
    with d1
    pause 0.3
    if activeSpy == 1:
        $ hiddenStatus = 1
        s "!!!"
        y "!!!"
        s "Clover!"
        y "Another spy?!"
        play sound "audio/sfx/drama1.mp3"
        show drama3:
            xalign 0.0 yalign 0.2
        show evilCloverDrama:
            xalign 0.5 yalign 0.295
        with quickflash
        pause 1.0
        hide drama3
        hide evilCloverDrama
        with quickflash
        c "I've spotted her. Quickly send your agents here!"
        s "Clover...?"
        y "[greenName] we're picking up a lot of radio chatter. You've got to get out of there."
        s "I'm not leaving her behind!"
        y "It's the nanobots, [greenName]. She's one of them now."
        y "We'll come back for her later. Now get out of there!"
        s "O-okay...!"
        $ _skipping = False
        $ missionProgression = 9
        hide spyReadyTut
        $ propInteract = -1
        hide tutExit1
        scene black
        with fade
        $ propInteract = 0
        $ missionProgression = 7
        play music "audio/music/crisis.mp3" fadein 1.0
        jump missionBegin
    if activeSpy == 2:
        $ hiddenStatus = 1
        c "!!!"
        y "!!!"
        c "[yellowName]!"
        y "Another spy?!"
        play sound "audio/sfx/drama1.mp3"
        show drama3:
            xalign 0.0 yalign 0.2
        show evilAlexDrama:
            xalign 0.5 yalign 0.295
        with quickflash
        pause 1.0
        hide drama3
        hide evilAlexDrama
        with quickflash
        a "I've spotted her. Quickly send your agents here!"
        c "[yellowName]...?"
        y "Clover we're picking up a lot of radio chatter. You've got to get out of there."
        c "I'm like... not leaving her behind!"
        y "She's with them now, Clover. We'll come back for her later. Now get out of there!"
        c "O-okay...!"
        $ missionProgression = 9
        hide spyReadyTut
        $ propInteract = -1
        hide tutExit1
        scene black
        with fade
        $ propInteract = 0
        $ missionProgression = 7
        play music "audio/music/crisis.mp3" fadein 1.0
        jump missionBegin
    if activeSpy == 3:
        $ hiddenStatus = 1
        a "!!!"
        y "!!!"
        a "[greenName]!"
        y "Another spy?!"
        play sound "audio/sfx/drama1.mp3"
        show drama3:
            xalign 0.0 yalign 0.2
        show evilSamDrama:
            xalign 0.5 yalign 0.295
        with quickflash
        pause 1.0
        hide drama3
        hide evilSamDrama
        with quickflash
        s "I've spotted her. Quickly send your agents here!"
        a "[greenName]...?"
        y "[yellowName] we're picking up a lot of radio chatter. You've got to get out of there."
        a "I'm not leaving her behind!"
        y "She's with them now, [yellowName]. We'll come back for her later. Now get out of there!"
        a "O-okay...!"
        $ missionProgression = 0
        hide spyReadyTut
        $ propInteract = -1
        hide tutExit1
        scene black
        with fade
        $ propInteract = 0
        $ tutStage = 4
        $ missionProgression = 7
        jump missionBegin
    pause

label tutStage6:
    $ tutStage = 6.5
    $ randomBackground = 4
    $ randomObst1 = 1
    $ obst1FoV = 2
    $ randomAgent1 = 1
    $ randomAgent2 = 1
    $ randomObst2 = 1
    $ randomExit = 2
    $ randomCover1 = 1
    show globalImage:
        xalign 1.0 yalign 0.75 zoom 0.36
    show obst1:
        xalign 0.64 yalign 0.99 zoom 0.49
    show spyCornerSide:
        xalign 0.97 yalign 0.90 zoom 0.39
    if activeSpy == 1:
        $ randomObst1 = 1
        $ randomCover2 = 4
        $ missionProgression = 9
        s "More agents!"
        y "They know you're there. You're going to have to fight your way through!"
        s "On it!"
        $ CoS1 = 100
        $ CoS2 = 100
        jump jumpStartScene
    if activeSpy == 2:
        $ randomObst1 = 1
        $ randomCover2 = 4
        $ missionProgression = 9
        c "More agents!"
        y "They know you're there. You're going to have to fight your way through!"
        c "On it!"
        $ CoS1 = 100
        $ CoS2 = 100
        jump jumpStartScene






layeredimage spyBG1ShootingUp:
    always:
        "mission/models/spyShoot1.png"
    if activeSpy == 1:
        "mission/models/sam/spyFallingSuit1.png"
    if activeSpy == 1:
        "mission/models/sam/spyShootUpHair1.png"

    if activeSpy == 2:
        "mission/models/clover/spyFallingSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyShootUpHair1.png"

    if activeSpy == 3:
        "mission/models/alex/spyFallingSuit1.png"
    if activeSpy == 3:
        "mission/models/alex/spyShootUpHair1.png"

layeredimage spyReadyTut:
    always:
        "mission/models/spyReady1.png"
    if activeSpy == 1:
        "mission/models/clover/spyReadyFace1.png"
    if activeSpy == 1:
        "mission/models/clover/spyReadySuit1.png"
    if activeSpy == 2:
        "mission/models/alex/spyReadyFace1.png"
    if activeSpy == 2:
        "mission/models/alex/spyReadySuit1.png"
    if activeSpy == 3:
        "mission/models/sam/spyReadyFace1.png"
    if activeSpy == 3:
        "mission/models/sam/spyReadySuit1.png"

layeredimage spyFightTut:
    always:
        "mission/models/spyFight1.png"
    if activeSpy == 1:
        "mission/models/clover/spyFight1Suit.png"
    if activeSpy == 1:
        "mission/models/clover/spyFight1Face.png"
    if activeSpy == 1:
        "mission/models/clover/spyFight1Hair.png"
    if activeSpy == 2:
        "mission/models/alex/spyFight1Suit.png"
    if activeSpy == 2:
        "mission/models/alex/spyFight1Face.png"
    if activeSpy == 2:
        "mission/models/alex/spyFight1Hair.png"
    if activeSpy == 3:
        "mission/models/sam/spyFight1Suit.png"
    if activeSpy == 3:
        "mission/models/sam/spyFight1Face.png"
    if activeSpy == 3:
        "mission/models/sam/spyFight1Hair.png"

image lockerWOOHP = "mission/school/lockerWOOHP.png"

layeredimage spyHidingTut:
    always:
        "mission/models/spyHidingBase1.png"
    if activeSpy == 3:
        "mission/models/sam/spyHidingSuit1.png"
    if activeSpy == 3:
        "mission/models/sam/spyHidingHair1.png"
    if activeSpy == 3:
        "mission/models/sam/spyHidingFace1.png"
    if activeSpy == 1:
        "mission/models/clover/spyHidingSuit1.png"
    if activeSpy == 1:
        "mission/models/clover/spyHidingHair1.png"
    if activeSpy == 1:
        "mission/models/clover/spyHidingFace1.png"
    if activeSpy == 2:
        "mission/models/clover/spyHidingSuit1.png"
    if activeSpy == 2:
        "mission/models/clover/spyHidingHair1.png"
    if activeSpy == 2:
        "mission/models/clover/spyHidingFace1.png"

layeredimage spyShootingTut:
    always "mission/models/spyShoot1.png"
    if activeSpy == 1:
        "mission/models/clover/spyShootingSuit1.png"
    if activeSpy == 1:
        "mission/models/clover/spyShootUpHair1.png"
    if activeSpy == 2:
        "mission/models/alex/spyShootingSuit1.png"
    if activeSpy == 2:
        "mission/models/alex/spyShootUpHair1.png"
    if activeSpy == 3:
        "mission/models/sam/spyShootingSuit1.png"
    if activeSpy == 3:
        "mission/models/sam/spyShootUpHair1.png"

image tutDart = "gui/tut/tutDart.png"
label tutStage65:
    $ _skipping = True
    $ task7Name = "Retaking the Taken"
    $ task7Text = "After my spy returned from her first mission we figured out oxytocin seems to help suppress the nanobots. We can capture agents and use sex to break the control over them. Then use them to help liberate Beverly Hills."
    hide screen interactScreen
    hide spyCrouchCorner
    hide spyCornerSide
    hide spyCorner
    $ currentPosition = 0
    $ tutStage = 6
    $ randomBackground = 1
    $ randomObst1 = 0
    $ randomObst2 = 0
    $ randomCover1 = 1
    show globalImage:
        zoom 0.25
    show spyCorner:
        xalign 0.90 yalign 0.83 zoom 0.78
    pause 0.5
    hide spyCorner
    show jumpGraphic:
        xalign 0.75 yalign 0.87
    pause 0.09
    hide jumpGraphic
    show spyCrouchCorner:
        xalign 0.25 yalign 0.48 rotate 7 zoom 0.24
    if activeSpy == 1:
        s "I'm in position for extraction."
        y "Good, I'm pulling you out of there!"
        show lockerWOOHP:
            zoom 0.25
        with d2
        s "Thanks, New Guy. I'm on my way back."
        c "(Not so fast, missy...~)"
        pause 0.3
        hide spyHidingTut
        show spyShootingTut:
            xalign 0.83 yalign 0.79 zoom 0.75 xzoom -1
        show expression "mission/models/shootGun.png":
            xalign 0.83 yalign 0.79 zoom 0.75 xzoom -1
        with d3
        pause 0.5
        play sound "audio/sfx/drama1.mp3"
        show drama1:
            xalign 0.0 yalign 0.0
        show evilCloverShoot:
            xalign 0.45 yalign 0.0 zoom 0.96
        with quickflash
        pause 0.4
        play sound "audio/sfx/shoot1.mp3"
        pause 0.6
        play sound "audio/sfx/drama2.mp3"
        show drama2:
            xalign 0.0 yalign 1.0
        show dramaShotGreen:
            xalign 0.5 yalign 0.88
        with quickflash
        pause
        pause 0.9
        hide drama1
        hide drama2
        hide evilCloverShoot
        hide dramaShotGreen
        with d1
        $ spy1Status = 0
    if activeSpy == 2:
        c "I'm in position for extraction."
        y "Good, I'm pulling you out of there!"
        show lockerWOOHP:
            zoom 0.25
        with d2
        c "Thanks, New Guy. I'm on my way back."
        a "(Not so fast, missy...~)"
        pause 0.3
        hide spyHidingTut
        show spyShootingTut:
            xalign 0.83 yalign 0.79 zoom 0.75 xzoom -1
        with d3
        pause 0.5
        play sound "audio/sfx/drama1.mp3"
        show drama1:
            xalign 0.0 yalign 0.0
        show evilAlexShoot:
            xalign 0.45 yalign 0.157 zoom 0.98
        with quickflash
        pause 0.4
        play sound "audio/sfx/shoot1.mp3"
        pause 0.6
        play sound "audio/sfx/drama2.mp3"
        show drama2:
            xalign 0.0 yalign 1.0
        show dramaShotRed:
            xalign 0.5 yalign 0.878
        with quickflash
        pause 0.9
        hide drama1
        hide drama2
        hide evilAlexShoot
        hide dramaShotRed
        with d1
        "DEV: CLOVER GETS WOOHPED GRAPHIC HERE"
        $ spy2Status = 0
    stop music fadeout 3.5
    scene black
    hide spyShootingTut
    hide screen equipmentMenu
    hide globalImage
    with d5
    pause 2.0
    scene bgBase
    with fade
    pause 0.3
    with hpunch
    if activeSpy == 1:
        pause 0.3
        show scene_darkening
        with d3
        show green g39 at ri with d3
        s "I'm... back..."
        y "[greenName] are you okay?"
        s g38 "Yeah.. I think so..."
        y "Just before I recalled you, that spy in red shot something at you."
        s g37 "I thought I felt something...."
        hide green
        with d3
        show scene_fighting
        with d3
        show tutDart:
            xalign 0.5 yalign 0.5
        with d3
        pause
        hide tutDart
        hide scene_fighting
        with d3
        y "Is that a poison dart...?"
        show green g16 at ri with d3
        s "I'm not sure..."
        y "..............."
        s g34 "..............."
        y "You're thinking what I'm thinking?"
        s g16 "Nanobots...?"
        y "Aaaand that leaves me as the only uneffected WOOHP employee."
        y "And I don't even work here!"
        s "What?"
        y "Nothing."
        s g11 "................."
        s g12 "I don't.... feel any different."
        s "Honestly, I feel fin-..."
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
        y "Sam~....?"
        s "{b}*Growls*{/b}"
        s "Anarchy...! Destruction! Rebellion!"
        hide green with d2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        play music "audio/music/sinister.mp3" fadein 1.5
        "Sam attacked you!"
        y "Ow!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        "The spy jumps on you and begins wailing away. Punching you in the ribs, face, chest and anywhere else she can get a hit in."
        y "Ow you crazy brat. Get off of me!"
        y "(I need a weapon!)"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.2
        "You stretch out your arm."
        y "(Almost....{w} Almost....!)"
        "Inches away from you is the mop! You stretch yourself out and snatch it off of the floor. Followed by wacking Sam in the face with it!"
        play sound "audio/sfx/splat.mp3"
        "{b}*SPLOSH!*{/b}"
        "For a moment the taken aback spy is distracted and you manage to get the upper hand, pinning her down to the floor as the struggle continues."
        "Clothes are ripped, arms are bitten and shins are kicked."
        $ greenOutfit = 3
        show green g100 at ri with d3
        s "{b}*Pant* *Pant*{/b}"
        s g39 "..........................?"
        s g28 "{b}*Blinks*{/b}{w} O-oh!"
        "Raising her hands to her mouth, she stares at you in shock."
        s "New Guy! I'm...! I'm sorry! I don't know what came over me!"
        y "Ow~....{w} Are you back to normal now....?"
        s g29 "I think so...?"
        y "Whelp...! Let's hope this doesn't become a trend. I only have so many spare suits lying around."
        y "I'm heading into the cells to get changed. You stay here and get changed yourself."
        s "{b}*Nods*{/b} Y-yeah... I will."
        y "After that we can talk about making sure this doesn't happen again."
        stop music fadeout 2.0
        hide green
        with d3
        pause 0.3
        hide scene_darkening
        with d3
        scene black
        with longFade
        play music "audio/music/nighttime.mp3" fadein 1.5
        pause 0.2
        y "Yup... That's gonna leave a bruise. Maybe there's still time for me to get out of h-..."
        s "{b}*Yelps*!{/b}"
        "???" "Reporting to the milkshake bar as ordered!"
        "???" "Woah!"
        y "Uh oh... I forgot about him..."
        pause 1.0
        scene bgBase
        with d3
        pause 0.5
        show scene_darkening
        with d3
        pause 0.5
        $ greenOutfit = 0
        $ greenUnder = 0
        $ greenOutfitArms = 0
        $ greenArms = 2
        show green g9:
            xalign 0.0 yalign 0.0 xzoom -1
        show agentModel:
            xalign 0.9 yalign 0.0
        with d3
        pause
        y "Woah!"
        "Agent" "That's what I said!"
        s g40 "Let me through!"
        "The buttnaked spy pushes her way past you and runs into the cellblock."
        show green:
            linear 0.3 xalign 1.5 yalign 0.0
        pause 0.25
        hide green with d2
        pause 1.0
        y "Well that was fun."
        y "................"
        y "So are you still evil?"
        "Agent" "My oxytocin levels are off the charts and I believe they are suppressing my desires for chaos and anarchy!"
        y "........"
        y "Wait seriously?"
        y "On a scale of 1 to 10, how badly do you want to overthrow the US government?"
        "Agent" "A pretty solid 5 out of 10!"
        y "Sam! Get back in here!"
        s "{b}Distant:{/b} I'm not dressed yet!"
        y "Perfect, I need you naked!"
        s "What?!"
        y "Just do it, please."
        s "No!"
        y "Sam....! Get in here!"
        s "No I won't!"
        y "{size=+8}Just do it, you green cucumber!{/size}"
        s "{b}This better have a good reason!{/b}"
        y "It'll be educational!"
        show green g11:
            xalign 0.5 xzoom -1
        with d5
        pause 0.5
        s "................"
        y "Now, agent! On a scale from 1 to 10, how badly do you want to conquer the world?"
        "Agent" "Any and all desire for chaos has left me completely!"
        s g16 "...?"
        y "It does work~..."
        y "Sam, your titties may have saved the world!"
        s g8 "You're crazy! I'm going to find my clothes!"
        hide green
        with d3
        pause 1.0
        y "As the only uncompromised WOOHP employee, I'm pretty sure I'm your boss now."
        "Agent" "Such logic cannot be argued with!{w} What are your orders, sir?"
        y "Er..."
        y "Why don't you go down this hatch and wait until I find something for you to do.."
        play sound "audio/voice/agent/yourwish.mp3"
        "Agent" "Your wish is my contractual obligation!"
        hide agentModel
        with d3
        pause 2.0
        $ greenChest = 1
        $ greenOutfit = 0
        $ greenArms = 1
        $ greenOutfitArms = 0
        $ greenBottom = 1
        $ greenShoes = 1
        $ greenNeck = 1
        show green g11 at ri with d3
        s "................................"
        s g12 "Well that was the most embarrassing thing I've ever done..."
        y "Yup and you'll be doing a lot more of it!"
        s g16 "I will...?"
        y "Sex seems to surpress the nanobot's control."
        y "And talking about nanobot control..."
        s g37 "............"
        s g12 "Ehrm.... Again, I'm sorry about earlier..."
        y "That's okay. You didn't knock out any teeth that were actually mine."
        y "More importantly, now we know how to suppress your own nanobots."
        s "............."
        s g19 "Ehrm well.... Do you mean-...?"
        y "SEX!"
        y "Sex raises your oxytocin levels and seems to surpress the nanobot control!"
        s g29 "O-oh... I think I read about oxytocin in school. I'm pretty sure there's other ways to raise it other than se-..."
        y "Exactly! There is {i}NO{/i} other way to raise them, other than sex!"
        y "Which means to keep you from becoming controlled again...."
        y "You're going to have to get-it-on!"
        s "You mean you want me to....?!"
        $ greenBlush = 1
        with d3
        s g19 "Oh boy~... It's all so sudden! I don't know if I'm prepared!"
        s "I haven't done any research on it!"
        y "........................"
        s g28 "Do I bring a condom? I've never bought one before!"
        s "I don't know if I can even sleep with a WOOHP Agent! I'm pretty sure that's against company guidelines!"
        y "Sam...."
        s g9 "What am I saying?! I'm suppose to be saving myself for marriage!"
        s g8 "How can you suggest such a thing?! I can't just sleep with you!"
        y "I didn't say you should."
        s "You were implying it!"
        y "No I wasn't.{w} I think you jumped to that conclusion yourself."
        s g28 "..........!"
        y "Ever heard of {i}'masturbation'{/i} before?"
        s g38 "{b}*Ahem*{/b} Yes I have...{w} I'm sorry, I didn't think of that... {w}I'll try keeping the nanobots supressed, [playerName]...."
        y "Look at you. Red as a tomato~...."
        s "Now if you'll excuse me! I'm going to bed!"
        y "It's 6 pm."
        s g40 "Good night!"
        y "Are you going to masturb-...?"
        s g8 "GOOD NIGHT!"
        hide green
        with d2
        "The blushing girl rushes off to her cell."
        hide scene_darkening
        with d3
        $ greenBlush = 0
        call screen tutBase
    if activeSpy == 2:
        pause 0.3
        show scene_darkening
        with d3
        show red:
            xalign 1.2
        with d3
        c "I'm... back..."
        y "[redName] are you okay?"
        c "Yeah.. I think so..."
        y "Just before I recalled you, that spy in yellow shot something at you."
        c "I thought I felt something...."
        hide red
        with d3
        show scene_fighting
        with d3
        show tutDart:
            xalign 0.5 yalign 0.5
        with d3
        pause
        hide tutDart
        hide scene_fighting
        with d3
        y "Is that a poison dart...?"
        show red
        with d3
        c "It better not leave a mark!"
        y "..............."
        c "..............."
        y "You're thinking what I'm thinking?"
        c "Nanobots...?"
        y "Aaaand that leaves me as the only uneffected WOOHP employee."
        y "And I don't even work here!"
        c "What?"
        y "Nothing."
        c "................."
        c "I don't.... feel any different."
        c "Honestly, I feel fin-..."
        play sound "audio/sfx/shockcrash.mp3"
        pause 0.7
        hide red
        show white
        pause 0.05
        hide white
        show bgControl
        show red
        $ redFace = 100
        pause 0.6
        hide bgControl
        y "Clover~....?"
        c "{b}*Growls*{/b}"
        c "Anarchy...! Destruction! Rebellion!"
        hide red with d2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        "Clover attacked you!"
        y "Ow!"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.3
        "The spy jumps on you and begins wailing away. Punching you in the ribs, face, chest and anywhere else she can get a hit in."
        y "Ow you crazy brat. Get off of me!"
        y "(I need a weapon!)"
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.2
        play sound "audio/sfx/punch1.mp3"
        with hpunch
        pause 0.2
        "You stretch out your arm."
        y "(Almost....{w} Almost....!)"
        "Inches away from you is the mop! You stretch yourself out and snatch it off of the floor. Followed by wacking Clover in the face with it!"
        play sound "audio/sfx/splat.mp3"
        "{b}*SPLOSH!*{/b}"
        "For a moment the taken aback spy is distracted and you manage to get the upper hand, pinning her down to the floor as the struggle continues."
        "Clothes are ripped, arms are bitten and shins are kicked."
        $ redOutfit = 3
        call callRed from _call_callRed_6
        c "{b}*Pant* *Pant*{/b}"
        "EYES TURN NORMAL HERE"
        $ redFace = 1
        c "..........................?"
        c "O-oh!"
        "Raising her hands to her mouth, she stares at you in shock."
        c "New Guy! I'm...! I'm sorry! I don't know what came over me!"
        y "Are you back to normal now....?"
        c "I think so...?"
        y "Whelp...! Let's hope this doesn't become a trend. I only have so many spare suits lying around."
        y "I'm heading into the cells to get changed. You stay here and get changed yourself."
        c "{b}*Nods*{/b} Y-yeah... Okay."
        c "(Is my make-up still looking okay...?)"
        y "After that we can talk about making sure this doesn't happen again."
        pause 0.4
        hide scene_darkening
        hide red
        with d3
        scene black
        with d3
        pause 1.0
        y "Yup... That's gonna leave a bruise. Maybe there's still time for me to get out of h-..."
        c "{b}*Yelps*!{/b}"
        "???" "Reporting to the milkshake bar as ordered!"
        "???" "Woah!"
        y "Uh oh... I forgot about him..."
        pause 1.0
        scene bgBase
        with d3
        pause 0.5
        show scene_darkening
        with d3
        pause 0.5
        $ redOutfit = 0
        $ redUnder = 0
        $ redOutfitArms = 0
        $ redArms = 2
        show red:
            xalign 0.0 yalign 0.0 xzoom -1
        show agentModel:
            xalign 0.9 yalign 0.0
        with d3
        pause
        y "Woah!"
        "Agent" "That's what I said!"
        c "Let me through!"
        "The buttnaked spy pushes her way past you as you and runs into the cellblock."
        show red:
            linear 0.3 xalign 1.5 yalign 0.0
        pause 0.25
        hide red with d2
        pause 1.0
        y "Well that was fun."
        y "................"
        y "So are you still evil?"
        "Agent" "My oxytocin levels are off the charts and I believe they are supressing my desires for chaos and anarchy!"
        y "........"
        y "Wait seriously?"
        y "On a scale of 1 to 10, how badly do you want to overthrow the US government?"
        "Agent" "A pretty solid 5 out of 10!"
        y "Clover! Get back in here!"
        c "{b}Distant:{/b} I'm not dressed yet!"
        y "Perfect, I need you naked!"
        c "What?!"
        y "Just do it, please."
        c "No!"
        y "Clover....! Get in here!"
        c "You dirty perv! I'm not coming out there!"
        y "{size=+8}Just do it, you red ass chili pepper!{/size}"
        c "{b}*Yelps*{/b}"
        show red:
            xalign 0.5 xzoom -1
        with d5
        pause 0.5
        y "Now, agent! On a scale from 1 to 10, how badly do you want to conquer the world?"
        "Agent" "Any and all desire for chaos and power have left me completely!"
        c "...?"
        y "It does work~..."
        y "Clover, your tiddies may have saved the world!"
        c "If I had a nickle for everytime some guy said that to me..."
        c "Also, you're crazy. I'm gonna go find my clothes!"
        hide red
        with d3
        pause 1.0
        y "As the only uncompromised WOOHP employee, I'm pretty sure I'm your boss now."
        "Agent" "Such logic cannot be argued with!{w} What are your orders, sir?"
        y "Er..."
        y "Why don't you go down this hatch and wait for further orders."
        play sound "audio/voice/agent/yourwish.mp3"
        "Agent" "Your wish is my contractual obligation!"
        hide agentModel
        with d3
        pause 2.0
        $ redChest = 1
        $ redOutfit = 0
        $ redArms = 1
        $ redOutfitArms = 0
        $ redBottom = 1
        $ redShoes = 1
        $ redNeck = 1
        call callRed from _call_callRed_7
        c "................................"
        c "I want to say that's the most embarrassing thing I've ever done..."
        y "Yup and you'll be doing a lot more of it!"
        c "Er... Like... No, taking a hard pass on that."
        y "Sex seems to surpress the nanobot's control."
        y "And talking about nanobot control..."
        c "............"
        c "Ehrm.... So about earlier... I think I get a free pass on that, seeing as it wasn't really my fault."
        y "It's okay. You didn't knock out any teeth that were actually mine."
        y "More importantly, now we know how to suppress your own nanobots."
        c "............."
        c "Ehrm well.... Do you mean-...?"
        y "SEX!"
        y "Sex raises your oxytocin levels and seems to surpress the nanobot control!"
        c "Oxytocin? I just looked it up online and it says here it can be raised by other ways than se-..."
        y "Exactly! There is {i}no{/i} other way to raise them, other than sex!"
        y "Which means to keep you from becoming controlled again...."
        y "You're going to have to get-it-on!"
        c "You mean you want me to....?!"
        $ redBlush = 1
        with d3
        c "Okay, so I know I'm totally irresistible. And 'obviously' you'd like to bang me, but it's a little sudden...!"
        y "........................"
        c "Do you even have a condom? I don't!"
        c "HR is going to have my ass for this! We can't do this!"
        y "Clover...."
        c "Okay, if it's for the good of mankind, then...{w} then let's do it! We can do it right now if you want!"
        y "Wait.. really?"
        c "Yes. If it's for the greater good, then I want you to bend me over and go to town on me!"
        y "Well I mean.. {w}if you insist...!"
        c "I want you to rip my clothes off and pull my hair. I want to feel myself full up and I want it to hurt."
        y "Wait a second..."
        y "You're being sarcastic."
        c "Of course I'm being sarcastic! I'm not gonna sleep with someone at the drop of a hat! Why would you even suggest something like that?!"
        y "I didn't."
        c "Yes you did. You suggested we'd have sex!"
        y "No I wasn't.{w} I think you jumped to that conclusion yourself."
        c "..........!"
        y "Ever heard of {i}'masturbation'{/i} before?"
        c "Oh... er... I didn't think about that..."
        c "{b}*Ahem*{/b} Yes well... I guess that's a good way to keep the nanobots supressed... I'll try that, [playerName]...."
        y "Look at you. Red as a tomato~...."
        c "Now if you'll excuse me! I'm going to bed!"
        y "It's 6 pm."
        c "Good night!"
        y "Are you going to masturb-...?"
        c "GOOD NIGHT!"
        hide red
        with d2
        "The blushing girl rushes off to her cell."
        hide scene_darkening
        with d3
        $ redBlush = 0
        call screen tutBase

label tutStage7:
    $ tutStage = 7
    $ daysPlayed += 1
    $ task7Text = "After my spy returned from her first mission we figured out oxytocin seems to help suppress the nanobots. We can capture agents and use sex to break the control over them. Then use them to help liberate Beverly Hills.\n\nWe will need money and intel to go on future mission, so I should send my spy out to go undercover and collect some intel with the different gangs around town.\n\n-Send your spy undercover with one of the gangs in town."
    $ mainQuestUpdate = True
    pause 0.3
    scene black with fade
    show text "The night passes and all is quiet."
    with d5
    pause 3.0
    hide text
    with d5
    scene bgBase with fade
    pause 1.0
    $ tod = 1
    y "Hey one more night and we didn't die in our sleep!"
    y ".............."
    y "Funny, I used to say this to myself even before the riots broke out.{w} They say paranoia is a form of insanity..."
    "Inner Voice" "You shouldn't listen to what others are saying."
    y "Yeah, you're right disembodied voice. What was I thinking?"
    if spyGreenActive:
        $ mapSpy1Active = True
        show green g16 at ri with d3
        s "Who are you talking to?"
        y "......................."
        s g35 "Aaanyways.... About what happened yesterday..."
        y "Yesterday?"
        s g29 "T-the whole nanobot discussion!"
        s g38 "{b}*Deep sigh*{/b} {w}I decided I have to apologize for my comment."
        s "I made assumptions and I shouldn't have. I'm just shy when it comes to talking about...{w} {size=-10}sex{/size} a-and... I may have jumped to conclusion."
        s "After going through it in my head, I realised you weren't implying that... you... and I would have... {b}*Ahem*{/size} you know."
        y "Oh no, I totally was."
        s g29 "What?"
        y "I was totally implying we'd get it on."
        s g8 "I KNEW IT!"
        y "Did you lie awake all night running it through your head?"
        s "NO!"
        y g37 "................"
        s g12 "Okay well maybe I did!"
        s g7 "You can't just say such things!"
        y "Keep your socks on. I was just kidding. We have more pressing matters to deal with anyways."
        s g15 "{b}*Ahem*{/b}... yes of course."
        play music "audio/music/daytime.mp3" fadein 2.0
        hide green
        scene black
        with fade
        scene bgMap:
            xalign 0.0 zoom 0.5
        with fade
        pause 0.5
        sM "The city is in chaos, my friends are missing, we lost all control over WOOHP and I'm missing school..."
        y "School?{w} That's what you're worried about?"
        sM "I'm an Honor Roll student! I can't just miss out on schoolwork!"
        y "........................"
        y "Well then, let's not waste any time."
        sM "We've freed one agent from nanobot control. It's a start, but if we want to take back the HQ we're going to need more."
        sM "Send me out on another mission and I'll bring back as many as you need!"
        y "Easier said than done."
        y "The gadget you used last time costs money to make... and I'm kinda broke."
        y "Also after your last mission at the school, they probably buffed up security. We can't charge back in there without getting some good intel first."
        sM "Oh... I guess you're right. Then what do you suggest?"
        y "Well, the villains shot you with Nanobots, right? Which probably means they think you're under their control now."
        y "You could go undercover with the different gangs around the city and bring back the intel we need for missions."
        sM "That's... That's a good idea actually!"
        y "You said you had a contact in the Aces? That sounds as good of a start as any."
        $ spy1Status = 0
        sM "Can do!"
    if spyRedActive:
        $ mapSpy2Active = True
        call callRed from _call_callRed_8
        c "Who are you talking to?"
        y "......................."
        c "Aaanyways.... About what happened yesterday..."
        y "Yesterday?"
        c "T-the whole nanobot discussion!"
        c "Can we just pretend that nothing happened...?"
        y "I dunno. I thought it was pretty hot."
        c "Stop it please."
        y "So did you keep the nanobots supressed like I suggested?"
        c "That's.... That's private!"
        y "As the only uncompromised agent of this organization, I'm pretty sure I outrank you."
        y "Remember that this is a matter of national security!"
        c "......................."
        c "Fine... Yes, I kept them surpressed last night..."
        y "I know you were. I was watching you through the cameras."
        c "WHAT?!"
        y "Just kidding, just kidding."
        y "Please put down the chair."
        c "Argh! Of all the agents, why did the only uncompromised one have to be a smartass?!"
        y "Keep your socks on. We have more pressing matters to deal with anyways."
        c "Oh yes... you're right."
        hide red
        scene black
        with fade
        scene bgMap:
            xalign 0.0 zoom 0.5
        with fade
        pause 0.5
        cM "The city is in chaos, my friends are missing, we lost all control over WOOHP and I missed my date...."
        y "Your date?{w} That's what you're worried about?"
        cM "He's the musician 'AND' a poet!{w} I'm pretty sure we were meant to be together."
        y "........................"
        y "Well then, let's not waste any time."
        cM "We've freed one agent from nanobot control. It's a start, but if we want to take back the HQ we're going to need more."
        cM "Send me out on another mission and I'll bring back as many as you need!"
        y "Easier said than done."
        y "The gadget you used last time costs money to make... and i'm kinda broke."
        y "Also after your last mission at the school, they probably buffed up security. We can't charge back in there without some good intel."
        cM "Oh... I guess you're right. Then what do you suggest?"
        y "Well, the villains shot you with Nanobots, right? Which probably means they think you're under their control now."
        y "You could go undercover with the different gangs around the city and bring back the intel we need for missions."
        cM "That's... That's a good idea actually!"
        y "You said you had a contact within Drift Punk? That sounds as good of a start as any."
        $ spy1Status = 0
        cM "Those grody nerds? Ew, no thank you."
        y "..................."
        cM "Okay fine...{w} But if they start bringing out their 20 sided dice, I'm out."
        play music "audio/music/daytime.mp3" fadein 1.5
    call screen mapButtons

label tutStage8:
    $ mainQuestUpdate = True
    $ task7Text = "After my spy returned from her first mission we figured out oxytocin seems to help suppress the nanobots. We can capture agents and use sex to break the control over them. Then use them to help liberate Beverly Hills.\n\nWe will need money and intel to go on future mission, so I should send my spy out to go undercover and collect some intel with the different gangs around town.\n\n{color=#A3A3A3}-Send your spy undercover with one of the gangs in town.{/color} \n\n-Clean up the milkshake bar and convince your spy to work there."
    if spyGreenActive and greenDayJob == 0:
        y "I should probably send Sam out to bring back some intel."
        call screen mapButtons
    if spyRedActive and redDayJob == 0:
        y "I should probably send Clover out to bring back some intel."
        call screen mapButtons
    if spyYellowActive and yellowDayJob == 0:
        y "I should probably send Alex out to bring back some intel."
        call screen mapButtons
    $ tutStage = 8
    $ tod = 2
    $ greenDayJob = 0
    pause 1.0
    show scene_darkening
    with d3
    if spyGreenActive:

        $ neck1Sam = True
        $ top1Sam = True
        $ bott1Sam = True
        $ shoes1Sam = True

        $ greenOutfit = 0
        $ greenOutfitArms = 0
        $ greenNeck = 1
        $ greenChest = 1
        $ greenBottom = 1
        $ greenShoes = 1
        show green g12 at ri with d3
        pause 0.5
        $ spy1Status = 0
        $ greOutfit3Set = 1
        $ greOutfit4Set = 1
        $ greOutfit6Set = 1
        s "I'm back from working at the Aces."
        y "So how did it go?"
        s g10 "Well... {w}They're a bunch of vain idiots. Most of them don't even bother stealing money, simply because they don't need it."
        s ".............................."
        y "Yes....?"
        s g11 "And they made fun of my clothes..."
        y "Your clothes?"
        s "They're rich kids. They all wear the latest fashion of expensive labels. I might aswell have been wearing garbage bags in the way they looked at me."
        y "Sounds like a great bunch..."
        s g12 "Here's my report."
        $ intel += 100
        $ randIntel = 100
        call missionRewardInt from _call_missionRewardInt_2
        pause 0.4
        "................................................."
        "You spend some time reading through the report."
        y "Hmm...{w} Ah, they mention a back entrance into the school."
        y "This should give us enough intel to sneak in again"
        s g35 "But I'm going to need another one of those gadgets, and those cost money."
        y "Exactly."
        s ".................."
        s "How do we get that...?"
        s g35 "Working for the Aces isn't a reliable way to make money. They're so rich that they forget to pay you for work you've done."
        y "............"
        y "Okay... What else is in this report...?"
        "................................................."
        y "Wait... the gangs are hoping to open up another neutral zone?"
        s g29 "Oh right! The only neutral zone right now is the mall. They'd like a hangout spot where they can relax."
        y "....."
        y "Like...{w} a milkshake bar?"
        s g18 "I'm not sure if gangsters are interested in milkshakes, [playerName]..."
        y "We'd just have to do some re-branding! We could sell burgers, beer and dress the waitress in skimpy outfits."
        s "But... don't we want to avoid bringing the gangs here?"
        y "We'll be hiding in plain sight. Plus no one would dare lift a finger against us if we're on neutral ground."
        s g37 "Well.. It would provide us with a source of income..."
        s g1 "Okay I'm convinced! Let's clean this place up and turn it into a bar!"
        y "Great! Now I just need to get you a sexy waitress uniform."
        s g29 "....................."
        s "Ehrm... maybe we could do it without the sexy waitress uniform...?"
        y "Naked staff? That's a great idea!"
        s g28 "N-no! That's not what I meant!"
        y "See what we can accomplish when we put our heads together?{w} Okay, let's get busy cleaning this place up."
        hide green with d3
        hide scene_darkening with d3
        $ task1Name = "Open for Business"
        $ task1Text = "Needing a source of income, you've decided to rebuild the milkshake bar and turn it into a sleazy restaurant.\nFix up the bar by either working on it yourself, sending your spy to clean it for you, or both."
        $ task1Stage = 1
        call qAccept from _call_qAccept
        pause 1.0
        scene bgBase
        with fade
        jump base

    if spyRedActive:
        ""
    if spyYellowActive:
        ""

label tutStage9:
    if tutStage <= 7:
        "error happens here"
    if tutStage == 8:
        $ tutStage = 9
        $ clubStage = 5
        "The bar is looking immaculate!"
        y "That's better. Now to start wi-..."
        stop music fadeout 1.0
        show scene_darkening
        with d3
        play music "audio/music/sinister.mp3" fadein 1.5
        "???" "Hey check this out. This place looks way too nice!"
        "A group of gangmembers just entered the bar!"
        "Aces Thug" "Let's tear it up a bit. This is Aces territory now!"
        y "..............................."
        "Aces Thug 2" "Woah, you're one of those WOOHP Agents...!"
        "Aces Thug 1" "Whatever, these WOOHP goon are just for show. You guys act all high and mighty, but I'd like to see you stop all of us!"
        "Aces Thug 2" "Yeah, you tell him! Maybe we should tear his face up a bit too!"
        y "So much for this being a neutral zone..."
        "Aces Thug 2" "Hah! We don't need your lame neutral zone! We're the Aces! We can just 'BUY' a neutral zone if we wanted to!"
        "Aces Thug 1" "I've got a better idea... Let's just kill him and take this bar from him...."
        y "........................."
        menu:
            "Shoot one of them" if True:
                y "You picked the wrong place to rob."
                y "Nothing {w}personal {w}kid."
                play sound "audio/sfx/gunshot1.mp3"
                scene white
                pause 0.1
                scene bgClub1
                with hpunch
                "You pull out your gun and shoot one straight through the fucking cranius!!!"
                "......................."
                "At least you would have, if you had a gun.{w} But you don't...."
                "Instead you're just pointing fingerguns at the gangster."
                show scene_darkening
                with d2
                "Aces Thug 1" "..............?"
                "Aces Thug 2" "..............?"
                y "........................{w} Boom. {w}You're dead."
                "???" "I don't know what's going on over here, but it's pretty amusing. How come nobody invited us to the party?!"
            "Surrender the bar" if True:
                y "Yeah okay, you can have the bar."
                "Aces Thug 1" "See? That wasn't so hard, was it? You WOOHP goons are all bark and no bite!"
                y "Good luck paying the property tax on this place."
                "Aces Thug 1" "Hah! You're joking right? We're the Aces! {w}We could buy this place, set it on fire, then pay for the renovations just so we could light it on fire again!"
                y "I dunno... The other guy maybe, but you don't look so rich to me..."
                "Aces Thug 2" "He's kinda got you there, bro. Those shoes are at least two weeks old."
                "Aces Thug 1" "These shoes cost $3500 dollars!"
                "Aces Thug 1" "I bought a $1500 dollar jacket just this morning!"
                "Aces Thug 2" "It was on discount."
                "Aces Thug 1" "I got a discount {i}'after'{/i} I threatend the guy's life to give me a discount!"
                "Aces Thug 2" "I'm just saying man. People might start to talk~...."
                "???" "{b}*Laughs*{/b} Look at these rich kids flaunting their money. I'd say we help relief them of it...."
            "Say something crazy" if True:
                y "You sure you want to do that?"
                y "I cleaned this place with non-brand cleaning supplies."
                "Aces Thug 1" "So what?!"
                y "They're 'non-brand'. You realise what the means, right?"
                "Aces Thug 2" "...?"
                y "It means I used cheap, unregulated products, which are probably highly flamable."
                y "Smell that nice lemony scent in the air? Strike a match now and everything a ten miles radius gets evaporated."
                "Aces Thug 2" "!!!"
                "Aces Thug 2" "Listen dude...! Maybe we shouldn't shoot him...!"
                "Aces Thug 1" "He's bluffing! He's got to be!"
                "Aces Thug 2" "Dude, I don't know anything about cleaning products. Do you?"
                "Aces Thug 2" "I heard that terrorists can make bombs out of simple household equipment!"
                "Aces Thug 1" "R-really...?"
                "Aces Thug 2" "Yeah, my cleaning lady once threatend to blow up our house after we fired her on Christmas morning."
                "Aces Thug 1" "Dude, that's so not cool of her!"
                "???" "Look, the kids are talking about making bombs. Good thing the experts have arrived~..."
        "Aces Thugs" "!!!"
        "A group of Outsiders thugs walked into the bar weapons drawn!"
        "Outsider Thug" "This is {i}'our'{/i} place now..."
        "???" "Correction. It is {i}'our'{/i} place now!"
        "Another gang came in! The thugs from Drift Punk enter brandishing their own guns, turning your bar into a Mexican standoff."
        y "Well that escalated quickly...."
        "Tension is rising as the gangmembers cautiously glare at each other."
        "Aces" "We claimed this place first. So buzz off."
        "Outsiders" "You wouldn't know what to do with it. Go back to your million dollar mansions and leave the street warfare to the professionals."
        "Drift Punks" "Hah! {i}'professionals'{/i}. The only thing you're a pro at is misspelling your name while writing your graffiti!"
        "Anything could set these guys off at any moment. Turning your milkshake bar into Swiss cheese."
        "Aces" "....................................."
        "Outsiders" "....................................."
        "Drift Punks" "....................................."
        y "......................................"
        y "Hey does anyone have a bandaid? Cause I'm here to {i}'CUT'{/i} the tension."
        "Stunned, the gangmembers turn their attention to you."
        y "Eh? Eeeeh? Get it? {i}'Cut the tension'{/i}?{w} I thought it was pretty clever myself."
        y "Also this is now a neutral zone. I'm with WOOHP, so I get to do that."
        "Outsiders" "A neutral zone...?"
        "Punks" "Can he do that...?"
        "Aces" "I don't know... Can he?"
        "Slowly, the gangmembers begin lowering their guns."
        "Outsiders" "Fine... neutral zone."
        "The other gangsters nod in agreement as soon the tension seems to disappear from the bar."
        stop music fadeout 3.0
        hide scene_darkening
        with d10
        "With the catastrophe avoided, you manage to usher everyone out of the door and breath a sigh of relief."
        y "I can't believe that worked..."
        y "............................"
        y "The place is fixed up nicely. I can probably start serving people here now..."
        y "But first I need to figure out a suitable work uniform for my willing waitress."
        if greenDayJob == 4:
            $ greenDayJob = 0
        $ mallActive = True
        $ beachActive = True
        $ task1Stage = 2
        call qUpdated from _call_qUpdated
        $ task1Text = "Needing a source of income, you've decided to rebuild the milkshake bar and turn it into a sleazy restaurant.\n \n-Fix up the bar by either working on it yourself, sending your spy to clean it for you, or both.\n \n-The bar has been fixed now all that's left to do is pick up a sexy waitress uniform for your spy."
        scene black with fade
        if tod == 1:
            "You finish off the last bit of work that needs to be done and it soon turns to evening."
            jump jobReport
        if tod == 2:
            "Having had quite enough excitement for one day, you decide to head to bed."
            jump nightCycle

default uniformLoan = 0
label tutStage10:
    $ tutStage = 10

    $ hat2Sam = True
    $ top2Sam = True
    $ bott2Sam = True
    $ shoes2Sam = True
    $ hat2Clover = True
    $ top2Clover = True
    $ bott2Clover = True
    $ shoes2Clover = True
    $ hat2Alex = True
    $ top2Alex = True
    $ bott2Alex = True
    $ shoes2Alex = True
    pause 0.5
    show scene_darkening
    with d3
    y "Now where would I go for some kinky roleplaying gear..."
    "You walk into the nearest store and see a bored salesgirl behind the counter."
    y "I'm looking for your kinkiest, filthiest fetish gear!"
    $ clerkFace = 2
    show clerk at ri with d3
    "Clerk" ".........................."
    "Clerk" "Sir, this is a bookstore...."
    y "............................"
    $ clerkFace = 1
    "Clerk" "It's on the fourth floor."
    y "I {i}fuckin'{/i} knew it!"
    "The two of you make your way upstairs."
    scene mallBG
    show scene_darkening
    with fade
    pause 0.5
    show clerk at ri with d3
    y "Quite the collection you got here~..."
    "Clerk" "All bookish girls are secretly kinky as fuck."
    "Clerk" "Now then... A waitress outfit...{w} We've got this one..."
    hide clerk with d3
    $ dummyOutfit = 1
    show dummy:
        xalign 0.5 yalign 0.5
    with d3
    pause
    y "It's perfect!"
    y "......................"
    y "(Crap... I don't have any money!)"
    menu:
        "Take a loan (+Karma)" if True:
            $ outfitSamUniformActive = True
            $ outfitCloverUniformActive = True
            $ outfitAlexUniformActive = True
            $ playerKarma += 1
            $ uniformLoan = 1
            y "So I don't have the money right now...."
            show clerk at ri with d3
            "Clerk" "D'aww that's too bad! {w}Get out."
            y "Hey now wait a second! I don't have money 'now', but I can pay you for it later!"
            "Clerk" "No."
            y "Please?"
            "Clerk" "No."
            y "Pretty please?"
            "Clerk" "Get out."
            y "No."
            "Clerk" "Yes."
            y "No. Gimme that outfit."
            "Clerk" "..............."
            $ clerkFace = 2
            "Clerk" "Y-...{w} No."
            y "(Damn it, so close!)"
            y "Okay fine! How can I convince you?"
            $ clerkFace =1
            "Clerk" "........................"
            $ clerkFace = 2
            "Clerk" "Who's the outfit for?"
            y "Er..."
            "Clerk" "Is she hot?"
            y "Yes."
            $ clerkFace = 1
            "Clerk" ".................................."
            "Clerk" "Okay fine, you can have it.{w} On one condition."
            y "Pics?"
            "Clerk" "Pics."
            hide clerk
            hide dummy
            hide scene_darkening
            with d3
            play sound "audio/sfx/itemGot.mp3"
            "You got the Waitress Uniform!"
            scene bgMap:
                zoom 0.5
            with fade
            y "Now I just gotta convince her to put it on..."
            jump worldmap
        "Grab and run! (-Karma)" if True:
            $ outfitSamUniformActive = True
            $ playerKarma -= 1
            $ uniformLoan = 2
            y "Yoink!"
            hide dummy
            with d3
            "You snatched the uniform out of the clerk's hands and make a run for it!"
            $ clerkFace = 2
            "Clerk" "Hey! Get back here!"
            "Clerk" "You can't just-..."
            $ clerkFace = 1
            "Clerk" ".........................."
            "Clerk" "Whatever... I get paid minimum wage. I don't care."
            hide clerk with d3
            hide scene_darkening
            with d3
            play sound "audio/sfx/itemGot.mp3"
            "You got the Waitress Uniform!"
            scene bgMap:
                zoom 0.5
            with fade
            y "Now I just gotta convince her to put it on..."
            jump worldmap

label tutStage11:
    hide screen nanoLevelSam
    $ greenChest = 1
    $ greenBottom = 1
    $ greenShoes = 1
    $ greenArms = 1
    $ task7Text = "After my spy returned from her first mission we figured out oxytocin seems to help suppress the nanobots. We can capture agents and use sex to break the control over them. Then use them to help liberate Beverly Hills.\n\nWe will need money and intel to go on future mission, so I should send my spy out to go undercover and collect some intel with the different gangs around town.\n\n{color=#A3A3A3}-Send your spy undercover with one of the gangs in town.{/color} \n\n{color=#A3A3A3}-Clean up the milkshake bar and convince your spy to work there.{/color}\n\n-???"
    $ tutorialActive = False
    $ tutStage = 11
    show scene_darkening
    with d3
    if spyGreenActive:
        show green:
            xalign 1.0 yalign 0.0
        with d3
        s g1 "[playerName]! Good, I was hoping to talk to you."
        s g16 "You know how you mentioned wearing a sexy waitress uniforms...?"
        s g33 "Well I'm not comfortable with that, so I was thinking that I would be a cook instead."
        y "..........................."
        s g1 "And you can be a waiter! Instead of wearing a skimpy uniform you could wear a nice suit and we can turn this into a classy establishment!"
        s "Also think of how progressive it would be! A man doing all the talking and a woman in the...{w} kitchen..."
        y "Didn't think this one through, did you?"
        s g15 "O-okay it sounds bad when I say it like that!"
        y "Here's your uniform. You're a waitress now."
        "You give Sam her uniform."
        hide green with d3
        pause 1.0
        $ greenChest = 2
        $ greenBottom = 2
        $ greenShoes = 2
        $ greenHat = 2
        $ greenArms = 1
        show green g18 at ri with d3
        s g18 "O-oh...! That's a little more revealing than I hoped. Where's the rest of it?"
        y "....................."
        s g28 "T-there is no rest of it?!"
        y "Welcome to the service industry!"
        $ mapSpy1Selected = False
    if spyRedActive:
        show red
        with d3
    if spyYellowActive:
        show yellow
        with d3
    hide scene_darkening
    hide green
    hide red
    hide yellow
    with d3
    $ task1Stage = 3
    $ task1Name = "Open for Business (completed)"
    $ task1Text = "Needing a source of income, you've decided to rebuild the milkshake bar and turn it into a sleazy restaurant.\n \n-Fix up the bar by either working on it yourself, sending your spy to clean it for you, or both.\n \n-The bar has been fixed now all that's left to do is pick up a sexy waitress uniform for your spy.\n \n-Quest completed!"
    call qCompleted from _call_qCompleted
    scene bgBase
    with fade
    $ greenShoesSet = 1
    call greenOutfitSet from _call_greenOutfitSet_3
    jump base

    "DEV END WARNING!!!! YOU SHOULD NOT SEE THIS"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
