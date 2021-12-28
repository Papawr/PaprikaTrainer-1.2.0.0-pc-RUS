
default spyRoomRand = 0
default sam1SecMiss = "Expose yourself to strangers \n[on\n]"





screen nanoLevelSam:
    vbox xalign 0.5 yalign 0.0:
        imagebutton:
            idle "gui/nanobotLvlBg.png"
            hover "gui/nanobotLvlBg.png" tooltip "ttNanoControl"
            action Jump("samCall")
    $ tooltip = GetTooltip()
    if tooltip == "ttNanoControl":
        text "{font=fonts/freshMarker.ttf}{size=-4}Nanobot Control{/size}{/font}" xpos 560 yalign 0.07
    vbox xalign 0.51 yalign 0.025:
        text "{font=fonts/freshmarker.ttf}[nanoLevelSam]/100{/font}"

label samCall:

    show screen nanoLevelSam
    if spyRoomRand == 1:
        call undressSam from _call_undressSam_8
        $ top11Sam = True
        $ hat11Sam = True
        $ greenChest = 11
        $ greenHat = 11
    if spyRoomRand == 2:
        call undressSam from _call_undressSam_9
        $ greenArms = 2

    $ mapSelectButton = 0
    if spy1Status == 0:
        menu:
            "{color=#EFD66D}'Party till you drop'{/color}" if task15Stage == 1 and task15Music and task15Fireworks and task15Girls and cash >= 2000:
                jump task15
            "{color=#EFD66D}'Let's have sex already'{/color}" if task13Stage == 1:
                jump task13
            "{color=#EFD66D}'Foot in The Door'{/color}" if task6Stage == 2:
                jump task6
            "{color=#EFD66D}'Open for Business'{/color}" if tutStage == 10:
                jump tutStage11
            "???" if slutLevel == 0:
                jump samCall
            "{color=#EFD66D}'Retaking the Taken'{/color}" if task26Stage == 22:
                jump task26
            "Nanobot control" if slutLevel >= 1 and task26Stage != 22:
                jump sexScenesSam
            "Chat" if tod == 2 and spy1Status == 0 and task26Stage != 22 and samSocial <= 12:
                if spyRoomRand >= 1:
                    hide screen nanoLevelSam
                    $ spyRoomRand = 0
                jump samSocial
            "Change naming" if True:
                menu:
                    "Call me..." if True:
                        menu:
                            "New Guy" if True:
                                $ playerName = _("New Guy [#ngpn]")
                                s "Sure, I can call you New Guy."
                            "Lowlife" if cardSWTitle == True:
                                $ playerName = "Lowlife"
                                s "That's a weird nickname... But I guess I can call you that from now on."
                                jump samCall
                            "Boss" if True:
                                if slutLevel <= 2:
                                    s "Let's not get carried away now..."
                                    s "I think I'll keep calling you [playerName] for now."
                                elif True:
                                    $ playerName = "Boss"
                                    s "Well you do order me around a lot..."
                                    s "I guess I might aswell call you Boss."
                            "Master" if True:
                                if slutLevel <= 3:
                                    s "I don't know... That sounds kind of wrong."
                                    s "I think I'll keep calling you [playerName] for now."
                                elif True:
                                    $ playerName = "Master"
                                    s "Master...? Oh well... I mean I guess that's okay."
                                    s "Okay fine, I'll call you my Master from now on."
                        jump samCall
                    "Call yourself..." if True:
                        menu:
                            "Girl" if True:
                                $ samNick = "Girl"
                                s "Girl? Er... sure why not."
                            "Cucumber{#CM}" if True:
                                $ samNick = "Cucumber{#CM}"
                                s "{b}*Sighs*{/b} Fine... Cucumber it is..."
                            "Bitch" if True:
                                if slutLevel <= 2:
                                    s "B-... That's so rude! Why would you even say that?!"
                                    s "I'm not your or anyone's bitch. So you can just forget it!"
                                elif True:
                                    $ samNick = "Bitch"
                                    s "Bitch...? Like those girls online who wear the collars...?"
                                    s "I dunno. I guess I wouldn't mind if you called me Bitch."
                            "Whore" if True:
                                if slutLevel <= 3:
                                    s "What?! I'm only doing this to help safe WOOHP! I am 'not' a whore!"
                                    s "I can't believe you just said that to me! There's no way I'll call myself that!"
                                elif True:
                                    $ samNick = "Whore"
                                    s "Heh heh~... Whore, huh?"
                                    s "That seems... oddly fitting for someone like me, doesn't it~...?"
                                    s "Heh... Okay! I'll be your Whore, [playerName]!"
                            "Gang Trash" if True:
                                if slutLevel <= 4:
                                    s "Listen [playerName]... Just because I'm going undercover doesn't mean you can call me that."
                                    s "I'm still a spy and I'm still one of the good guys. So please don't call me that."
                                elif True:
                                    $ samNick = "Gang Trash"
                                    s "Gang Trash?! But I'm not...!"
                                    s "I'm..."
                                    s "......................"
                                    s "Man... I really have turned into that, haven't I?{w} Fine, no other way around it. I'm Gang Trash and you can call me that."
                            "Fuck Toy" if True:
                                if slutLevel <= 4:
                                    s "F-fuck toy?!"
                                    s "That is very inappropriate, [playerName]!"
                                    s "Please don't suggest that to me again!"
                                elif True:
                                    $ samNick = "Fuck Toy"
                                    s "Heh~... Is that how you see me? As your toy?"
                                    s "Well I do let you play with me a lot~... I guess being called a Fuck Toy isn't so bad~..."
                            "Cum Dumpster" if True:
                                if slutLevel <= 4:
                                    s "C-...! [playerName] are you feeling okay...?"
                                    s "You shouldn't call girls that! I'll pretend that I didn't hear it."
                                elif True:
                                    $ samNick = "Cum Dumpster"
                                    s "Cum Dumpster...? That sounds so wrong!"
                                    s "Like I'm just a deposit for your semen...."
                                    s "................."
                                    s "Well I mean... That is kinda what I'm being used for."
                                    s "Fine. I'll be your Cum Dumpster, [playerName]."
                            "Semen Demon" if True:
                                if slutLevel <= 4:
                                    s "......................."
                                    s "Is that a normal thing to say to a girl?"
                                    s "You should be ashamed of yourself! Let's not bring this up again!"
                                elif True:
                                    $ samNick = "Semen Demon"
                                    "{b}*Smirks*{/b} That's so wrong~..."
                                    s "But I kinda like it~... All right, [playerName]. I'll be your little Semen Demon~..."
                            "Anal Agent" if True:
                                if slutLevel <= 4:
                                    s "A-anal what?! Listen here [playerName], let's not talk about this right now!"
                                    s "Or ever! Let's drop it completely!"
                                elif True:
                                    $ samNick = "Anal Agent"
                                    s "Anal Agent. Literacy, I like it. Also it's weirdly appropriate~..."
                                    s "I guess I've earned that nickname by now~... Sure call me whatever you like, [playerName]."
                        jump samCall
                    "Back" if True:
                        jump samCall
            "Decorate Cell" if True:
                label decorateSamCell:
                    pass
                call screen cellSamDeco
            "Never mind" if True:
                hide screen nanoLevelSam
                $ spyRoomRand = 0
                hide cellSam
                jump base
    elif True:
        "Sam isn't available right now."
        jump base

label samSocial:
    $ greenArms = 1
    if spy1Status == 1:
        "Sam isn't home right now."
        jump base
    if spy1Status == 2:
        "Sam isn't available right now."
        jump base
    elif samDailyChat == 0:
        if greenChest == 0 and greenUnder == 0:
            $ greenUnder = 1
            $ greenArms = 1
    if samMiniQ1 == 2:
        $ samMiniQ1 = 3
        y "Sam, I got you something from the museum."
        show scene_darkening with d3
        show green g29 at ri with d3
        s "You did? Can I see it?!"
        y "Here..."
        "You hand Sam the small figure you picked up at the museum."
        s "It's...!"
        s "It's.... erm...."
        y "What is it?"
        "Sam shrugs her shoulders."
        s "I dunno."
        s "But you went through the trouble of getting it for me..."
        s "Thank you, [playerName]."
        y "Don't mention it."
        hide scene_darkening
        hide green
        with d3
        jump samCall
    elif samDailyChat == 0:
        if samSocial == 0:
            $ samSocial = 1
            $ samDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            y "Quite a day it's been, don't you think?"
            show green g10 at ri with d3
            s "Hm? Oh yes, I guess so.{w} What can I do for you, [playerName]?"
            y "Oh nothing. Just figured we'd have a chat. Get to know eachother a little better."
            s g39 "......................"
            s g38 "Although I understand where you're coming from, I respectfully decline."
            y "You... what?"
            s "Don't take this the wrong way, but we need to focus and be on our guard at all times."
            s g32 "We can't let our guards down. Not even for a moment."
            y "Not even for a simple chat?"
            s "No, not even for that."
            y "Then what are we doing right now?"
            s g28 "Oh! You're right! Were you testing me?"
            y "No not really. You gotta relax a bit Sam. You're no good to the mission if you're stressed out all the time."
            s g11 "................."
            s "I guess you're right... Okay fine. I'll try to lighten up a little bit."
            s "It's getting late now, but I'd be up for a chat tomorrow, if you like."
            hide scene_darkening
            hide green
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if samSocial == 1:
            $ samSocial = 2
            $ samDailyChat = 1
            $ samNick = "Cucumber"
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            y "Hey [samNick]."
            show green g10 at ri with d3
            s "[samNick]...?"
            s "Is that your nickname for me?"
            y "It is now."
            s g38 "Now listen here, [playerName]. I don't think it's very professional for you to address me like that."
            y "It's not?"
            s "No. After all, we're on a very serious mission and we don't have time for silly nicknames."
            y "Oh..."
            y "Then I guess you wouldn't mind me telling you my real name either. It's-..."
            s g12 "Although having some silly nicknames might improve morale around here."
            y "..........."
            s g39 "But does it have to be Cucumber of all things?"
            y "Yes, Sam.{w} This is important to me."
            s "................"
            s g12 "{b}*Sighs*{/b} Cucumber it is~...."
            hide scene_darkening
            hide green
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if samSocial == 2:
            $ samSocial = 3
            $ samDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            y "Hey [samNick]. Getting ready for bed?"
            show green g10 at ri with d3
            s g14 "Yeah, hopefully I'll be able to get some sleep tonight."
            y "You haven't been sleeping?"
            s "It's a little difficult with all the fighting going on outside."
            s g15 "I can't begin to imagine how scared the people of Beverly Hills must be!"
            s g38 "The mastermind who's behind this has some nerve, messing with people's lives like this."
            s g31 "We're gonna hunt him down, arrest him and have him confess his crimes!"
            y "I like your dedication, though making him confess might be a little tricky."
            s g1 "Nah, that'll be the easy part. The villains we capture always end up confessing in the end."
            y "They do?"
            s "Yeah, WOOHP has specially trained agents who sit down to talk to the villains in special rooms and make them see the error of their ways."
            s "Then they confess and we put them away behind bars!"
            y "Okay... A little strange, but who am I to question it!{w} Good chat, [samNick]."
            hide scene_darkening
            hide green
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if samSocial == 3:
            $ samSocial = 4
            $ samDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show green g1 at ri with d3
            s "Oh hey, [playerName]. What can I do for you?"
            y "Ah not much. I was just wondering....{w} Last time you mentioned special rooms where agents had a {i}'chat'{/i} with villains, right?"
            s "Yeah and afterwards they confess."
            y "I see... I see..."
            y "...................."
            y "So we just so happen to have a hatch leading to the basement. Is this one of those {i}special rooms{/i}?"
            s g14 "Oh, yes it is actually. I haven't gone down to it myself though."
            y "................"
            y "The room is padded to cancel out noise.{w} And it was full of tools..."
            s g18 "Oh... It was under construction, maybe?"
            y "And I'm pretty sure there was a chair with restrainers in the middle of the room..."
            s g1 "Well this is a insane asylum after all. It makes sense that patients will need to be restrained for their own good."
            y "Yeah...."
            y "Actually yeah, you're right! For a short moment I thought they might've been used for much darker purposes, but you've convinced me!"
            y "I'm sure the red stains on the floor and wall are just spilled paint or tabasco sauce."
            s g29 "T-the what...?"
            y "Thank you for setting my mind at ease, Sam!{w} Silly of me to think badly on a prestigious organization like WOOHP."
            s g30 "What was this about red stains...?"
            y "Good chat, [samNick]. Get ready for bed and sleep tight."
            s "Er....~"
            hide scene_darkening
            hide green
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if samSocial == 4:
            $ samFriend = "Friend"
            $ samSocial = 5
            $ samDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            y "Hey [samNick]. I wanted to know a bit more about you."
            show green g41 at ri with d3
            s "About me...? Not sure what's there to say really."
            y "Well what do you like to do for fun?"
            s g1 "Studying."
            y "No for fun. You know... to relax."
            s g11 "Oh well I mostly study to relax."
            y "......................."
            y "WOOOOOWOOOOOOHWOOOOO BORING ALERT!"
            s g32 "!!!!"
            s "Hey! There's nothing boring about studying!"
            s g37 ".................."
            s "Okay well maybe it can be boring. But if you get as much action as I do in life, then studying suddenly becomes a lot more relaxing."
            s "Most of the time when I'm reading, I don't have to worry about snipers or werewolves or deathrays...{w} Most of the time."
            s "Plus, there's nothing more important than a P.H.D."
            y "I've got a P.H.D. if you know what I mean!"
            s g29 "Oh, you do?"
            y "No... it's a joke...{w} It stands for Pretty Huge D-..."
            s g4 "Oh that's too bad. I've been hoping to befriend someone with a P.H.D. so they could help me prepare for tests. Gotta make my parents proud after all."
            y "Your parents?"
            s g11 "..................."
            s g12 "So anyways, it's getting late. Let's continue this later."
            y "As you wish. Good night."
            hide scene_darkening
            hide green
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if samSocial == 5:
            $ samSocial = 6
            $ samDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            y "Hey Sam. You up for a chat?"
            show green g1 at ri with d3
            s "I got a minute. Sure."
            y "Just checking to see how you're holding up."
            s g10 "Hm? Well all things considering I guess I'm fine."
            s g10 "It's been [daysPlayed] days and we're no closer to saving the city and WOOHP though."
            if spyRedActive == False:
                s g4 "And of course I'm worried about how my friends are doing."
            s g4 "I guess we're in this for the long haul..."
            y "Don't be down in the dumps, [samNick]. We'll find a way to safe everyone."
            s "Yeah..? Any suggestions would be great about now..."
            menu:
                "'Keep your head up and don't lose spirit'" if True:
                    $ samMood += 5
                    y "We're making progress. Just hang in there for a bit longer and we'll start making a real difference."
                    s g16 "You think?"
                    y "Trust me. Before you know it we'll have WOOHP back under our control and Beverly Hills nice and safe."
                    s g2 "Heh... I know you're just trying to make me feel better but...{w} It's sorta working. Thanks, [playerName]."
                    s "Maybe I'm just having an off-day. I'm sure I'll see things in a more positive light tomorrow."
                    hide scene_darkening
                    hide green
                    with d2
                    "The two of you spend a little more time chatting before Sam heads off to bed."
                    scene bgBase
                    with d3
                    jump base
                "'You just gotta work harder" if True:
                    $ samMood -= 5
                    s g28 "H-hey..! I work hard!"
                    y "Really?"
                    s "Yes!"
                    y "Reaaally?"
                    s g42 "Of course I am!{w} I mean... I am, right?"
                    y "I dunno. The WOOHP handbook tells to drive your employees past their breaking point and you don't look broken to me yet."
                    s g10 "..................."
                    y "So be better."
                    s g11 "That's-...."
                    y "Work harder."
                    s "That's not very motivatio-..."
                    y "Work 23 hour shifts."
                    s g38 "Okay okay, fine! Forget I asked anything!"
                    y "And no breaks."
                    "Sam groans and rolls her eyes before heading off to bed."
                    hide green with d3
                    y "(I am an awesome motivational speaker!)"
                    hide scene_darkening with d3
                    scene bgBase with fade
                    jump base
                "Say something insane" if True:
                    y "Trust in the heart of the cards."
                    s g38 "What does that even mean?"
                    y "I'm talking about blackjack!{w} Gambling will solve all our problems!"
                    s g28 "Gambling? No no no, you can't go throwing away all our hard earned money!"
                    y "But I'm feeling lucky!"
                    y "I haven't felt this lucky since the day I got arrested and they threw me in he-...."
                    s g18 "You got arrested?"
                    y "Oh ehrm...!"
                    s "Are you... sweating?"
                    y "Erm...!!"
                    s g17 "Wait, you have a criminal past?!"
                    y "{b}ERM...!!!!{/b}"
                    show scene_fighting with d3
                    y "(Voice in my head, I need some advice right now!)"
                    "Voice" "Dude, don't look at me, I'm sweating as badly as you are!"
                    "Voice" "Sam can't find out that you were an inmate! She'll go crazy!"
                    y "(You think I don't know that?!)"
                    y "(Okay, let's not panic. Deep breaths... I just need a clever and nuanced way to end the conversation and hopefully she'll forget all about it.)"
                    hide scene_fighting with d3
                    s g16 "Are you okay, [playerName]...?"
                    y "Goodbye."
                    hide scene_darkening
                    hide green
                    with d2
                    "You left the cell and locked the door behind you."
                    s "{b}*Knock* *Knock*{/b} Hey! What's the big idea?!"
                    scene bgBase
                    with d3
                    y "Phew~... nailed it."
                    jump base
            hide scene_darkening
            hide green
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if samSocial == 6:
            $ samSocial = 7
            $ samDailyChat = 1
            show scene_darkening with d3
            show green g1 at ri with d3
            s "Hey [playerName]. How've you been?"
            y "Peachy. What about you? You've been here for [daysPlayed] days now."
            s g12 "Well..."
            s "I think it's a bit silly how we're trying to take back WOOHP. It's certainly not a very orthodox way."
            s g1 "But I'm slowly getting used to it, I guess."
            s "What about you? Getting used to being trapped in here?"
            y "Yeah I got used to this place a long time ago."
            s g18 "...?"
            y "I mean I got used to it really quickly!"
            y "................"
            y "Say, can I ask you something?"
            s g1 "Sure."
            y "Why are you so concerned with studying?"
            s g41 "Huh? Oh well... isn't everyone?"
            y "Sure, everyone puts {i}'some'{/i} effort into it, but you seem to be going far and beyond."
            s g11 "I just have a lot to live up to I guess."
            y "Your parents?"
            s g29 "Yeah... How did you know?"
            y "You mentioned them before."
            s g37 "..................."
            s "They're... good people, but maybe a bit over protective."
            s g33 "My mom constantly worries about me and they both have good jobs. Mom's a succesful bio engineer and dad's a surgeon."
            y "That's some big shoes to fill."
            s "At a young age they decided that I had to become a scienist. They hoped I'd go to Harverd, but I begged them to stay with my friends here in Beverly Hills."
            s "They agreed, but on the condition that I took pretty much every side course there was available."
            s g18 "Did you know that STOP signs used to be yellow? Or that the hottest temperature ever recorded on earth was 2 billion degrees kelvin?"
            y "Well I know now... {w}What does this have to do with science...?"
            s g12 "I don't know! They just keep signing me up for courses!"
            s g11 "..........................."
            s "{size=-8}And I don't want to disappoint them...{/size}"
            y "I don't think you'll disappoint your parents by dropped out of a few courses, right?"
            s g12 "No you don't understand... When I was little..."
            s "............................."
            s "Actually, never mind. It's not important. Let's focus on the mission for now."
            y "Er... Sure."
            hide scene_darkening
            hide green
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if samSocial == 7:
            $ samSocial = 8
            $ samDailyChat = 1
            show scene_darkening with d3
            show green g1 at ri with d3
            y "{b}[samNick], CATCH!{/b}"
            s g28 "Argh!"
            play sound "audio/sfx/splat.mp3"
            with hpunch
            s g10 "................................."
            y "................................."
            s "[playerName]~....."
            y "Sam~....?"
            s "Did you just throw a wet mop at my head~....?"
            y ".........."
            y "Yes."
            s g18 "Why?"
            y ".................."
            y "I'll be completely honest with you, [samNick]. I have no idea."
            s "..............."
            s "Your insane antics seem to be happening more often, [playerName]."
            s g16 "Didn't WOOHP give you a psychoanalysis test before hiring you?"
            y "Nope, I just put on the suit and off I went to save the world."
            s "Right..."
            s g18 "And what did you do before joining WOOHP?"
            y "I was a zoo-keeper."
            y "But... we don't talk about that..."
            stop music
            play sound "audio/sfx/panic2.mp3" fadein 5.0
            show black:
                xalign 0.0 yalign 0.0 alpha 0.0
                linear 8.0 alpha 0.8
            y "...............................................................................................................\n...............................................................................................................\n...................................................................................................................\n............................................................{nw}"
            $ renpy.pause(7.0, hard='True')
            hide black
            stop sound
            s g16 "Wha-...?"
            y "Nothing! {w}Good chat, [samNick]. Be a dear and clean up that mop will you?"
            s g32 "............."
            hide scene_darkening
            hide green
            with d3
            scene bgBase with fade
            play sound "audio/music/nighttime.mp3" fadein 1.5
            jump base
        if samSocial == 8:
            if acesRank >= 1:
                $ samFriend = "Good Friend"
                $ samSocial = 9
                $ samDailyChat = 1
                show scene_darkening with d3
                show green g1 at ri with d3
                s "Hey [playerName]."
                y "Hey Sam, I wanted to talk about your role in the Aces."
                s g28 "My role?"
                y "Yeah, how are you getting on with your undercover missions? How is your reputation with the gang?"
                s g33 "Well I'm only a new member and things have been rough."
                s "They can smell money from a mile away and they can tell I don't have any."
                y "But they allow you to stay?"
                s g35 "Well some of them have taken a liking to me I guess. The same way you feel when seeing a stray puppy."
                s "They've taken me in, but haven't really accepted me yet."
                y "Any idea how we can win their trust? And don't say money... cause we don't have any."
                s g43 "I'm mostly hoping for a chance to prove myself. They already invited me to their castle in Spain so I think there's hope."
                s "It really puts my acting chops to the test though. I can't stand being around them and their careless waste of money."
                y "Let's just give it time, you might get close to them the better you get to know them."
                s g35 "I hope so..."
                hide green with d3
                scene bgBase with d3
                jump base
            elif True:
                "You can't think of anything to talk about."
                hide green with d3
                scene bgBase with d3
                jump base
        if samSocial == 9:
            $ samSocial = 10
            $ samDailyChat = 1
            show scene_darkening with d3
            show green g1 at ri with d3
            s "Oh hi, [playerName]. Had a good day?"
            y "Same as all the others. What about you?"
            s g37 "Sorta the same. Going undercover and even serving milkshakes has its own excitement I guess, though I miss when we weren't in a constant state of war."
            y "What did you like to do before this mess?"
            s "Well... I spent most my time studying of course, but when I wasn't I'd go to mall or beach."
            s "I guess not that much has changed..."
            y "Not counting for the violence in the streets."
            s g35 "Yeah."
            y "What about music?"
            s g1 "Alex is more of the music person. I do enjoy going to see art galleries though."
            y "Modern or classic?"
            s g30 "Er..."
            y "It's modern, isn't it?"
            s g41 "What can I say? I enjoy seeing something new and interesting."
            y "Fair enough. So what gallery did you visit?"
            s "One downtown...{w} It's been destroyed by hooligans though."
            s "I just wish some of it was saved..."
            menu:
                "'I'll find you some'" if True:
                    $ samMiniQ1 = 1
                    y "I could try and see if some of it survived."
                    s g2 "That'd be great, but I'm not holding out much hope."
                "'That's too bad'" if True:
                    y "That's a shame, maybe once all of this is over we'll be able to recover some."
                    s g5 "Yeah, maybe..."
            s g41 "What about you? Do you enjoy art?"
            y "Of course I do! I'm a great fan of nude photography!"
            s g10 "................."
            s "You're talking about porn, aren't you?"
            y "Yup. Good chat [samNick]. I'll come see you again soon!"
            hide scene_darkening
            hide green
            with d3
            pause 0.5
            scene bgBase with d3
            jump base
        if samSocial == 10 and acesRank >= 2:
            $ samSocial = 11
            $ samDailyChat = 1
            show scene_darkening with d3
            show green g1 at ri with d3
            s g18 "I wasn't always an A+ student you know."
            y "No?"
            s g1 "Believe it or not, I was quite an unruly child. It's only in my teens that I started working this hard."
            y "What made you change?"
            s g12 "Well..."
            s ".................."
            s g20 "{b}*Sighs*{/b} My parents were gonna split up..."
            s "It's part of why I was so unruly. There was a lot of turmoil in the house."
            s "Eventually both of them started coming home later and later from work, simply because they didn't want to be around each other anymore."
            s g21 "One night I overheard them argueing and mentioning my name. Each blaming each other for the way I behaved..."
            s "I felt like I was the reason they were breaking up. That night I made a vow to change who I was. I was going to study as hard as I could."
            s g19 "And it worked..."
            y "..................."
            s "As my grades went up, my parents had something they could both be proud of."
            s "They spend more time in the house, tutoring me. They were nicer to each other..."
            s g20 "In the end it saved their marriage."
            y "But you had to change who you were."
            s "Yes... I did."
            y "That's rough."
            s "I sometimes wonder how it would have turned out if I hadn't."
            s g19 "But every scenario I think up would be more negative than this one."
            y "Do they know you're a WOOHP spy?"
            s g14 "Oh God no. They'd be so worried. They do love me... I just had to put in some extra effort."
            y "By spending one half of your life studying and the other half doing missions."
            s g15 "........................"
            s "Maybe when this is all over I'll talk to them."
            y "........................"
            hide scene_darkening
            hide green
            with d3
            pause 0.5
            scene bgBase with d3
            jump base
        if samSocial == 11 and acesRank >= 3:
            if acesRank >= 2:
                $ samSocial = 12
                $ samDailyChat = 1
                show scene_darkening with d3
                show green g1 at ri with d3
                s "Hey [playerName]. You know how I talked about my parents before?"
                y "Yeah?"
                s "I feel like I should tell them once this is all over.{w} Let them know I love them, but that I had to give up a lot of my youth to their marriage."
                y "Would you tell them you're a spy as well?"
                s g12 "No... probably not..."
                s "I want to stop my every waking minute studying though. But I'm afraid that if my grades go down, they'll start bickering again."
                y "It's not the child's responsibility to save their parents' marriage. You're an adult now Sam, but so are they. You have to live your own life."
                s g20 "But what if they break up?"
                y "Better to have them break up than be miserable together. You own a car, you can still see them both."
                y "And you no longer live at home, so you're not tied to either one of them."
                y "You got a good head on your shoulders. You might even be able to mediate the break-up. Keep it civil, but again... it's not your responsibility."
                s g19 "Yeah... I guess you're right."
                s g1 "Thanks [playerName]. You've given me a lot to think about."
                hide scene_darkening
                hide green
                with d3
                pause 0.5
                scene bgBase with d3
                jump base
            elif True:
                "You can't think about anything to talk about."
        if samSocial == 12 and acesRank >= 4:
            $ samFriend = "Best Friend"
            $ samSocial = 13
            $ samDailyChat = 1
            show scene_darkening with d3
            show green g1 at ri with d3
            s g41 "So I've been thinking..."
            s "Once I stop being a goodie two shoes student, I'll have so much free time!"
            s "More time for shopping, more time for going to the beach!"
            s g28 "I can finally take up painting! That's something I've always wanted to try."
            y "I bet you'd draw something ugly and modern art."
            s g20 "............................"
            y "Something wrong?"
            s g19 "No nothing... It's just that... I'm worried that Beverly Hills will never be the same after this."
            s "Like how this WOOHP uprising is going to leave the city wounded for years to come..."
            y "Yeah... I wouldn't worry about that."
            s g16 "No?"
            y "Beverly Hills is a sunny place with a {b}lot{/b} of money."
            y "Investers from all over the world will be jumping to pour money into restoring the city. This place is going to turn out even better than before all this started."
            y "It's going to have more shopping centers. A petting zoo. The newest and greatest spas."
            s g29 "...!"
            s "I hadn't thought about that yet!"
            stop music fadeout 3.0
            s "New penthouse parties, new movie theatres, new museums...!"
            s g13 "It will have a mall big enough to get lost in...!"
            s g14 "And everyone will be safe and.....! {b}*Sniff*{/b}"
            s "And..."
            s g15 "And I don't have to be so scared anymore."
            play music "audio/music/ahsoka.mp3" fadein 3.0
            hide green with d3
            y "Sam...?"
            "Sam takes a step closer and stands before you looking at her feet. Avoiding eye contact."
            s "........................"
            s "I've been so scared, [playerName]..."
            s "I didn't want to show it, but I'm afraid...{w} Afraid my friends will get hurt... afraid of my family being hurt..."
            y ".........."
            s "{b}*Sniff*{/b} There's been so many times where I wanted to quit..."
            s "So many moments that I felt scared or alone..."
            s "But you...{w} as crazy as you are sometimes. You never give up. You never back down."
            s "Thank you... for having always been there for us...{w} thank you for aways being there for me..."
            y "Sam..."
            s "We're all going to live through this... You hear me...?"
            s "And we'll be friends forever..."
            y "Forever."
            "You throw your arms around Sam and hug her in a tight embrace."
            scene black with fade
            pause 2.0
            stop music fadeout 3.0
            scene bgBase with longFade
            jump base
        elif True:
            "You can't think of anything to talk about right now. Maybe try raising your rank with the Aces first."
    elif True:
        "You already spoke with Sam today."
        jump samCall
    jump base

label cloverSocial:
    $ redArms = 1
    if spy2Status == 1:
        "Clover isn't home right now."
    if spy2Status == 2:
        "Clover isn't available right now."
    elif cloverDailyChat == 0:
        if redChest == 0 and redUnder == 0:
            $ redUnder = 1
            $ redArms = 1
        if cloverSocial == 0:
            $ cloverSocial = 1
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red r10 at ri with d3
            c "[playerName]? How can I help you?"
            y "Just chatting."
            c r16 "Er... well okay. What do you wanna chat about?"
            y "I don't know. Figured if we're working together, we should get to know one another."
            c r10 "Fair enough. So what did you want to know?"
            y "How'd you end up joining WOOHP?"
            if traitorRandom == 870803:
                c "That's an... interesting story. It wasn't entirely voluntairy."
                y "...?"
            c r11 "Same as Alex and Sam. We were scouted out by Jerry when we were young and recruited when we were teenagers."
            y "Teenagers?"
            c "Yeah, I think we were sixteen at the time."
            y "Sixteen? Isn't that a bit young to join a anti-terrorist organization?"
            if traitorRandom == 870803:
                c "Yes. Yes it is."
            c r12 "Well it was weird at first..."
            c "But we got used to it pretty soon. Plus not everybody gets to be a spy. It is pretty exciting."
            y "Do you ever regret it?"
            if traitorRandom == 870803:
                c ".........................."
            elif True:
                c "No, not really. Sure it gets in the way of important stuff, but saving the world on a regular basis is pretty cool aswell."
            c r3 "Anyways, is that all you wanted to know or want to interrogate me a bit more?"
            y "I'd like to know more, but we'll leave it here for now."
            c "Sure."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 1:
            $ cloverSocial = 2
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red at ri with d3
            y "Let's talk."
            c r10 "Like... sure, what's on your mind?"
            y "Let's talk about your Valley Girl accent."
            play sound "audio/voice/clover/what2.mp3"
            c r16 "{b}*Scoffs*{/b} What?"
            y "You know what I mean. When I think spy, I think sophistication and class. {w}\nNot pervasion and sass."
            c r10 "...................."
            c "You've been waiting to use that one."
            y "Yes!"
            c r12 "Like... not as if it's any of your business, but I grew up in a well-off family and we like... just sorta talked like this."
            c "Like... it's not that strange when you like... live in Beverly Hills."
            show likelikelike:
                xalign 0.5 yalign 0.5 alpha 0.0
                linear 14 alpha 0.6
            c "When you like... go out you will see like... a ton of girls like... talking like this."
            c "It's like... just like... like something we do."
            "Like.... like... like... like... like... like... like... like..."
            "Like.... like... like... like... like... like... like... like... Like.... like... like... like... like... like... like... like... Like.... like... like... like... like... like... like... like... Like.... like... like... like... like... like... like... like... Like.... like... like..."
            hide likelikelike
            y "Okay.... New rule. You're not allowed to say {i}'like'{/i} anymore."
            c r29 "What...?"
            y "You heard me. Not more liking."
            c r16 "{b}*Scoffs*{/b} But...-"
            y "And no more scoffing either."
            c r17 "What?!"
            y "You heard me. I'm your boss and I get do that."
            c r12 "{b}*Scoffs*{/b} No you don't...."
            y "HEY! No scoffing!"
            c r10 "!!!"
            y "I'll come back next time to see how you're holding up under the new rules."
            c "{b}*Grumbles*{/b}"
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 2:
            $ cloverSocial = 3
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red at ri with d3
            y "Hey Clover."
            c r10 "Hey..."
            y "How are you today?"
            c r11 "Lik-.... I mean.... I'm doing fine."
            y "And how was your last mission?"
            c "I had to get dirty... It was lik-..."
            c ".................."
            c r12 "It was not glamorous....!"
            y "And how do you enjoy hanging out in this base?"
            c "......!"
            c "It....{w} is...{w} not...{w} as bad...{w} as I...{w} thought..."
            y "Really struggling there, aren't ya?"
            c r38 "Like... this is not what I'm used to!!!"
            c "How do you like... not use {i}'like'{/i} in every sentence you like... say!"
            y "It's quite easy actually."
            c r39 "{b}*Scoffs*{/b} For you maybe!"
            c "..................."
            c r38 "I'll... keep trying."
            y "You will?"
            c r11 "I'll be honest... like... I also sorta think a Valley Accent is like...{w} kinda annoying."
            y "See?! That's what I was saying."
            c "Ngh... okay I'll keep trying...."
            y "I'll be sure to check in on your progress later."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 3:
            $ cloverSocial = 4
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red at ri with d3
            y "Hey parsnip, how are you doing?"
            c r16 "Parsnip?"
            y "Y'know... cause you wear a red suit."
            c "...?"
            y "You know... cause parsnips are red."
            c "Parsnips aren't red."
            y "They're not...?{w} Oh God, what have {i}'I'{/i} been eating?"
            c r3 "Maybe [playerName] isn't a appropriate nickname for you either...{w} I think {i}'weirdo'{/i} would be more fitting."
            y "I can't argue with that...{w} But please don't."
            c "{b}*Smirks*{/b} We'll see..."
            c r1 "By the way, how do you like my accent? I haven't used {i}'like'{/i} once!"
            y "I'm very proud of you. I'll check in on you again later. I gotta find out what parsnips look like now."
            c "Okay..."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 4:
            $ cloverFriend = "Friend"
            $ cloverSocial = 5
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red r1 at ri with d3
            y "Time for another chat."
            c r41 "Yeah? What did you want to talk about?"
            y "Well, I'd like to know a bit more about you. How's the accent thing coming along?"
            c r11 "Take a lot of effort, but it's getting there..."
            c r23 "It only took a world-ending scenario for me to unlearn it."
            y "You mentioned wanting to get rid of the Valley girl accent. Right?"
            c r11 "Yeah~... can't say it has done me a whole lot of good in the past."
            c "With the accent comes the stereotype of being a bimbo. Plus being blonde didn't help."
            c "A lot of people just see me as the dumb blonde who's obsessed with shopping."
            y "You're telling me you're not?"
            c r20 "Er..."
            c "Well okay, shopping {i}'is'{/i} important, but there's more to me than worrying about where the latest sale is."
            y "Yeah? Like what?"
            c "Like...! {w}Er..."
            c "......................."
            c r21 "Like....."
            y "You can't think of anything, can you?"
            c r29 "Wow... I must've gone along with the stereotype for so long that I've become the very thing I didn't want to become."
            y "Think it over. We'll talk again soon."
            c "Yeah...."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 5:
            $ cloverSocial = 6
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red r10 at ri with d3
            y "Hello Clover. Have you thought about what we talked about last time?"
            c r11 "Yeah... It's a little disturbing to think about to be honest."
            c "Whenever I think 'hobbies', I keep ending up with the same three things."
            y "Which are?"
            c r12 "Fashion, beauty and boys."
            y "........................."
            y "You really are a bimbo."
            c r29 "I...!{w} I kinda am!"
            y "What did you like to do when you were a kid?"
            c r11 "Hm... I was never really into sports, but I got pretty good at taekwondo when I joined WOOHP."
            c r3 "Maybe I could practise that and become the cool kick-ass fighter who doesn't take shit from anyone!"
            y "That's as good as a place of any to start."
            y "Good chat, Clover. You focus on your training and let me know how it worked out for you next time we talk."
            "Clover gives you a determined look and nods."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 6:
            $ cloverSocial = 7
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red r11 at ri with d3
            y "Howdy Clover. Want to spar?"
            y "I used to be one pretty mean boxer in highschool. I bet I could teach you a thing or two!"
            c r30 "Oh, hey. Hmm... I've been thinking..."
            c "Maybe being the badass martial artist isn't my thing."
            y "Oh... So who do you want to be instead?"
            c r1 "Well I was thinking and I used to like interviewing people when I was little. Maybe the suave war reporter who reports from the frontline is more my style!"
            y "Okay, start with interviewing me."
            play sound "audio/voice/clover/what2.mp3"
            c r16 "Er... what?"
            y "Go on, show me how good of a reporter you are. Interview me."
            c "Er... well let's hear something interesting about you then!"
            y "You don't wanna know my real name first?"
            c "Is it a particularly interesting name?"
            y "Well no, but...."
            c r38 "Then who cares. I only want to report the interesting stuff!"
            y "All right, you seem to know... or at least pretend to know what you're doing. Go on, interview me then."
            c "Well...! I... erm... so were you... born here in the USA?"
            y "Yes."
            c r10 "Oh... that's not very interesting."
            y "Gotta say, so far you're not being a really good reporter."
            c r40 "{b}*Scoffs*{/b} Like... I just need to do some preparing and stuff!"
            c "Next time we chat, for sure. I'll ask you everything there is to know about you!"
            y "Deal."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 7:
            $ cloverSocial = 8
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red r1 at ri with d3
            y "Clover, I'm ready for my interview."
            c r18 "Oh right... about that..."
            y "Don't want to be a reporter anymore?"
            c r1 "I couldn't think of any good questions and then I realized... I should be a relationship counselor!"
            y ".........................."
            play sound "audio/voice/clover/what2.mp3"
            c "What?"
            y "Don't you have a new boyfriend every week?"
            c "Exactly! I'd be perfect for the job!"
            y "Clover... a relationship counselor makes sure people stay together in their relation. Not finding a new one every seven days."
            c r10 "But that's so boring... Who'd want to get tied down with the same person for more than a week?"
            y "You'll find that a lot of people do...."
            c r12 "Ugh whatever."
            c "........................"
            y "Clover?"
            c r14 "{b}*Sighs*{/b} Martial artist, reporter, counselor... I suck at everything I do..."
            y "Well..."
            y "Instead of trying to be something you're not. Why not try being yourself?"
            c r15 "................."
            c r18 "I don't know, [playerName]. That sounds super cheesy."
            y "You'll figure it out. You're already a superspy, you just gotta find yourself a hobby that fits you."
            y "In the meantime you just get to be a bimbo."
            c "Heh... I guess you're right.{w} Except for the bimbo part."
            y "Sure.{w} Talk to you later, bimbo."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 8:
            $ cloverFriend = "Good Friend"
            $ cloverSocial = 9
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red r1 at ri with d3
            c "I want to know a little bit more about you now, [playerName]."
            y "About me?"
            c "Yeah, you seem to have a bit more personality than your typical WOOHP agent."
            y "Oh er... yeah... about that..."
            c "Did you have a job before you joined WOOHP?"
            y "Hm? Oh yes, many actually.{w} I used to be a daycare worker."
            c r10 "........................."
            c "You? A daycare worker?"
            y "Yeah, but we don't talk about those... dark, terrible days..."
            stop music
            play sound "audio/sfx/panic2.mp3" fadein 5.0
            show black:
                xalign 0.0 yalign 0.0 alpha 0.0
                linear 8.0 alpha 0.8
            y "...............................................................................................................\n...............................................................................................................\n...................................................................................................................\n............................................................{nw}"
            hide black
            stop sound
            c r16 "Did you just have a ptsd flashba-...?"
            y "NO! It wasn't my fault!"
            c "Wh-..."
            y "Any questions should be directed towards my lawyer!"
            c "O-okay, I'm sorry I asked!"
            y "{b}*Shudders*{/b} So many icebergs...."
            c "...................................."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 9:
            $ cloverSocial = 10
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red at ri with d3
            y "So how did you join WOOHP?"
            c r12 "Same as Alex and Sam. Recruited by Jerry."
            c r11 "............................."
            c "It was... messy."
            y "Do tell."
            c r10 "Well... originally we weren't interested in becoming spies. So Jerry had to be creative."
            c "He sorta...{w} cut me off from all of my bank accounts, abducted me and locked me up in an unknown location."
            y "!!!"
            c r38 "Then he sorta blackmailed us into joining."
            y "!!!"
            c r10 "Then he forced us to undergo a 48 hour spy crash course before sending us on our first mission."
            y "!!!"
            y "Wait... 48 hours?"
            y "The leader of WOOHP sent you on a mission after two days of training...?"
            c "Yeah kinda."
            y "That's crazy!"
            y "I'm crazy, but that's a whole 'nother level of insane!"
            c r11 "I guess.. but it did introduce us to the spy life."
            y "How old were you even at that time?!"
            c "Er...{w}sixteen."
            y "................................."
            y "And you're sure WOOHP are the good guys....?"
            c r16 "I think so... but recalling the events out loud, I'm not so sure anymore."
            y "All right, thanks for sharing parsnip. Goodnight."
            c "Night."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 10:
            $ cloverSocial = 11
            $ cloverDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show red r18 at ri with d3
            c "Hey [playerName]. Remember what we were talking about last time?"
            y "How you joined WOOHP?"
            c "Yeah..."
            c "I thought it over and I realized something."
            c r11 "........................"
            c "The way we joined WOOHP was kind of fucked up!"
            y "That's what I thought!"
            c r40 "Once we rescue Jerry I'm going to give him a piece of my mind!"
            c "I could've done so much with my life if it wasn't for this spy job. I might've actually grown to appreciate other hobbies instead of shopping and boyfriend hunting!"
            c "{b}*Humpf*{/b} And I bet I'm going to get wrinkles at a young age cause of the stress!"
            y "So I read the WOOHP guidelines and it says we're not officially allowed to mess with civillians."
            c r10 "Yeah he told us something like that when we joined aswell... but remember. This is a spy organization. Everything they do is off the record."
            c "I've never even told my parents. One of these days there's going to be a ray-gun with my name on it. Not sure how they'll react to their daughter being fried by a international super villain!"
            c "{b}*Grumbles*{/b}"
            y "Sounds like you've got some things to think over. I'll talk to you later, Clover."
            hide scene_darkening
            hide red
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if cloverSocial == 11:
            if punkRank >= 2:
                $ cloverSocial = 12
                $ cloverDailyChat = 1
                pause 0.2
                show scene_darkening with d3
                pause 0.3
                show red r10 at ri with d3
                y "Clover."
                c "[playerName]."
                y "Ready to talk about it again?"
                c r11 "I guess..."
                c r2 "The way we joined WOOHP might have been a little controversial, but... I don't think I'd trade it for the world."
                c "The places we've been and seen. The people we've met and the dangers we faced. It may sound strange, but it made me who I am."
                c r12 "At the same time... I don't wish this lifestyle on any unsuspecting teenager that WOOHP has its eyes on."
                c "The girls and I have always come off unscathed, but we had some close calls. There's something telling me that WOOHP has a laundry list of spies that weren't so lucky."
                y "Once we free WOOHP, will you stay a spy?"
                c r1 "I think so, yes. As long as there are some changes in our recruitment policy."
                y "You'll have to take that up with your boss."
                c r11 "..........................."
                c r12 "I wonder how Jerry is doing... We've been going at it for a while now. I hope he's okay."
                hide scene_darkening
                hide red
                with d3
                pause 0.3
                scene bgBase with fade
                jump base
            elif True:
                "You can't think of anything to talk about."
                jump cloverCall
        if cloverSocial == 12:
            if punkRank >= 3:
                $ cloverFriend = "Best Friend"
                $ cloverSocial = 13
                $ cloverDailyChat = 1
                pause 0.2
                show scene_darkening with d3
                pause 0.3
                show red at ri with d3
                c r12 "[playerName]... I just wanted to talk for a moment..."
                y "What is it parsnip?"
                c r11 "Well I was just thinking..."
                stop music fadeout 2.0
                c "Everything we went through... all the stupid shenanigans you pulled and all the crazy missions we completed..."
                c "It's been a crazy journey... but you've always stucks with us..."
                play music "audio/music/ahsoka.mp3" fadein 3.0
                c r20 "............................................."
                c "At first I thought you were just in it for yourself. That you just wanted to see some tits. That you were outright insane, but..."
                c "You really wanted to help... You worked really hard for us..."
                "Clover turns around, facing away from you."
                hide red with d3
                c ".........................."
                c "I don't care if you're crazy. You're loyal...{w} and one of my best friends."
                y "Clover..."
                c "You talk in your sleep, y'know..."
                c "You mutter things... You talk about taking back WOOHP... Freeing Jerry... Other crazy things..."
                c "You say the stupidest shit, but it always makes me laugh. You talk about your favorite milkshakes. Your love for rhinos..."
                c "..........................."
                c "And you talk about keeping us safe..."
                c "{b}*Sniff*{/b} And you always have..."
                y "Aw Clover..."
                c "Thanks to you my two best friends are safe...! Sam and Alex trust you too..."
                c "{b}*Sniff*{/b}"
                "You walk up behind Clover..."
                c "I don't know what we would've done if you didn't come to help us..."
                "You throw your arms around her and pull her in for an embrace."
                c "{b}*Sniff*{/b} Stop that stupid... You're gonna make me cry."
                y "You want me to stop?"
                c ".................................................................................."
                c "No.."
                scene black with fade
                pause 2.0
                stop music fadeout 3.0
                scene bgBase with longFade
                jump base
            elif True:
                "You can't think of anything to talk about right now. Maybe try raising your rank with the Drift Punk first."
                jump cloverCall
        elif True:
            "You can't think of anything to talk about right now. Maybe try raising your rank with the Drift Punk first."
    elif True:
        "You already spoke with Clover today."
        jump cloverCall
    jump base

label alexSocial:
    $ yellowArms = 1
    if spy3Status == 1:
        "Alex isn't home right now."
    elif spy3Status == 2:
        "Alex isn't available right now."
    if alexDailyChat == 0:
        if yellowChest == 0 and yellowUnder == 0:
            $ yellowUnder = 1
            $ yellowArms = 1
    if alexDailyChat == 0:
        if alexSocial == 0:
            $ alexSocial = 1
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            y "So... Alex..."
            a "Hiya [playerName]!"
            y "I thought we should maybe get to know each other a little better..."
            a y18 "You want me to show my boobies again...?"
            y "What? No!{w} I mean.... unless you {i}'want'{/i} to show me your boobi-..."
            a y17 "No!"
            y "No! Of course not!"
            y "{b}*Ahem*{/b} Why not tell me about yourself a bit."
            a y42 "{b}*Inhale*{/b}...."
            y "Alex? What are you doi-....?"
            a y1 "MynameisAlexIliketoplaymusiceatingcottoncandyvisitingthemeparksandthemallIlovethecolormacaroonsinginganddancingallnightlong\nialsolovepuppiesandbabykittensandprettymucheverythingelsethatsstillababyexceptformaybehumanbabieswhichalwaysbitemyfingerandtheyalwayssmellreallybad\nbutthatsokayiknowtheyrebabiesandallalsohaveyoueverplayedgamesonyourphoneitskindafunbutIkeepspending\ntoomuchmone-..."
            y "Okay okay! Hold up! One thing at a time."
            a y15 "Oh.."
            y "Through your rambling I think I heard you liked to play music?"
            a y1 "Yeah! I play instruments!"
            y "That's pretty cool. Are you any good at it?"
            a "Yeah, WOOHP taught me for one of our missions!"
            a "We went on stage to play the opening number for Ricky Mathis."
            y ".............."
            y "Who?"
            a y41 "The pop idol? What? Have you been living underground for the past few years or something?"
            y "Er.. never mind! Let's get back to the instruments!"
            y "So what type of music do you play?"
            a y1 "Rock and roll!"
            y "Really?"
            a "Yeah, I play electric guitar, bass, drums. Perfect for playing rock."
            y "I'm surprised, I more picture you as... a nursery rhyme type."
            a y10 "I'm not eight, [playerName]!"
            y "Could've fooled me."
            a y12 "{b}*Hmpf!*{/b} I'll have you know that I can be very mature if I want to be."
            a "I just don't want to be..."
            y "Fair enough. All right, good chat. We'll talk more later."
            a y1 "{b}*Nods*{/b}"
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 1:
            $ alexSocial = 2
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a "Hello again [playerName]!"
            y "Hey Alex. Figured we'd continue our chat from last time."
            a "Sure, but want to see me do a handstand first?"
            hide yellow with d2
            $ yellowArms = 0
            show yellow:
                xalign 1.4 yalign -0.08 rotate 180 xzoom -1
            with d2
            y "................"
            y "You seem to have a lot of energy. Being locked up down here must be hard on you."
            show yellow:
                linear 2.0 xalign 1.0 yalign -0.08 rotate 180 xzoom -1
            y "I know that it's a tough situation, but we just gotta work through it."
            hide yellow
            show yellow:
                xalign 1.0 yalign -0.08 rotate 180
                linear 2.0 xalign 1.4 yalign -0.08 rotate 180
            y "It is in times like these that you have to be able to rely on your friends and allies to get through the darkest of tim-..."
            hide yellow
            show yellow:
                xalign 1.4 yalign -0.08 rotate 180 xzoom -1
                linear 2.0 xalign 1.0 yalign -0.08 rotate 180 xzoom -1
            y "Can you stop walking around on your hands please?"
            a "Oh? Sorry, I didn't realize you were talking!"
            hide yellow
            $ yellowArms = 1
            show yellow at ri with d3
            y "........................."
            y "On second thought. You seem to be doing fine."
            a y19 "Actually it's really tough being locked up in here, but if I rely on my friends and allies, I can get through the darkest of times!"
            y ".........................."
            y "{b}*Sighs*{/b} Good chat, Alex. Until next time."
            a y1 "O-oh? Leaving already? All right, [playerName]!"
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 2:
            $ alexSocial = 3
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow y1 at ri with d3
            a "Hi [playerName]."
            y "Hello Alex, not standing on your hands today?"
            a y14 "No... I tried and fell over. Hurt my butt..."
            menu:
                "Better your butt than your head" if True:
                    y "Could've been worse. Try not to hurt yourself okay? There's plenty of people who would gladly do that for you."
                    a "I know... I'm sorry..."
                    a y1 "I got something to show you though!"
                "Let me check" if True:
                    y "Drop your pants. I'll make sure it's all right."
                    a y1 "Okay!"
                    play sound "audio/sfx/cloth.mp3"
                    hide yellow with d3
                    $ yellowBottom = 0
                    if yellowUnder == 0:
                        $ yellowUnder = 1
                    pause 0.5
                    show yellow at ri with d3
                    a y10 "Waaaait a second! You're just trying to see my naked butt!"
                    y "I would never!"
                    a y11 "{b}*Hmpf*{/b} And I was gonna show you something really cool aswell...."
                    y "Your butt?"
                    a y8 "No!"
            "Alex shows you a small gold broche of a four leafed clover."
            a y1 "It's my lucky charm. The girls always say I have the worst luck, so I got this to help with that."
            a y28 "It cost me an arm and a leg to get it! Gold is so expensive!"
            y "Lemme see that..."
            y ".............................."
            y "It's not real gold."
            a y29 "W-what...?"
            y "It's fake. You've been scammed."
            a y4 "B-but....!"
            "Alex's lower lip quivers."
            y "How.... How much did you pay for it...?"
            a "{b}*Sniff*{/b} A whole month's salary..."
            y "......................."
            y "D-did I say it was fake? Oh silly me! I got it wrong!"
            a "...?"
            y "Yeah~... no this is totally real gold. That makes it extra lucky, y'know."
            a y29 "Really?!"
            y "Yup, I would't be surprised if you were the luckiest person here!"
            a y42 "I knew it! Wow, I was really worried there for a second, [playerName]."
            a "I knew it couldn't be fake. The trustworthy man in the raincoat in the dark alleyway would never have lied to me!"
            y ".............................."
            y "We'll talk more later. Later Lady Luck."
            "Alex is too busy hugging her four-leafed clover to notice you leaving."
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 3:
            $ alexSocial = 4
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a "Say [playerName]. How old are you exactly?"
            y "I don't know. It's hard to keep track of time when you've been locked up for a while."
            y "What year is it?"
            a y18 "Err.. it's [year]."
            y "Oh god, really?! Oh I'm way older than I thought I was!"
            a y16 "What did you mean with being locked u-..."
            y "All those wasted years! I could have been married by now! I could've owned a house!"
            a "[playerName]...?"
            y "I could have invested money in real estate! Trade stocks and other things that adults do! Instead I just wasted away in an underground cell surrounded by crazy people!"
            a "[playerName]... You're not a bad guy are you...?"
            y "............."
            y "No."
            a y1 "Okay! Phew~... for a second there I thought you might've not really been a WOOHP agent, but stole a suit when you broke out of prison."
            y "Yeah, but that would have been silly, right?"
            a "Yeah totally! I'm glad you're still one of the good guys, [playerName]."
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase
            hide screen nanoLevelAlex
            with fade
            pause 0.8
            y "(My entire life is a lie.)"
            "Voice" "(Now is not the time to have an existential crisis.)"
            y "(Yeah you're right, voice in my head.)"
            jump base
        if alexSocial == 4:
            $ alexFriend = "Friend"
            $ alexSocial = 5
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a "Hey [playerName] guess what!"
            y "Chicken butt!"
            a "Chicken bu-..."
            a y28 "!!!"
            a "You knew what I was going to say before I said it!"
            y "Of course I did. I'm psychic."
            a y29 "No way!"
            y "I'll proof it. Your favorite color is... macaroon."
            a y28 "{b}*Gasps*{/b} YES! It is!"
            a "Okay! What's my favorite candy?!"
            y "Cotton Candy."
            a "Aiiiii! You're right!!!"
            a y1 "You are so amazing! No wonder you're the...{w} leader....{w}...?"
            a y21 "W-wait..."
            a "Is you're psychic... does that mean you can read all my naughty thoughts aswell....?"
            y "You bet I do."
            a y42 "Oh noooo!"
            hide yellow with d3
            "Alex hops on her bed and covers her face with her pillow."
            a "This is so embarrassing!"
            y "Don't worry, I won't tell anyone."
            a "Thank you....."
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 5:
            $ alexSocial = 6
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a "Hi [playerName]. What's up?"
            y "Just checking in on you."
            y "You mentioned playing instruments, right? Is there anything else you like doing?"
            a "Hm... well I'm a big soccer fanatic."
            y "Soccer?"
            a y29 "Yeah, I play in competitions and everything. I guess I'm just really good at kicking stuff."
            y "I'm sure that'll come in useful."
            y "Sorry, not a lot of space in here to play soccer for the time being."
            a y1 "That's okay, I'll stay in shape beating up bad guys."
            a y18 "By the way, how much longer do you think until Beverly Hills is back to normal?"
            y "Erm... It will probably be a while."
            a y20 "Oh..."
            if traitorRandom == 708349:
                a "...................."
            elif True:
                a "I miss Jerry..."
            y "It'll be fine. We're making good progress, just try to keep your head in the game."
            a y1 "Of course!"
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 6:
            $ alexSocial = 7
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a y15 "..........."
            a y38 "Man I miss living a normal life..."
            y "Isolation getting to you?"
            a y20 "Maybe..."
            a "I get that we have to go undercover, but I miss being myself around others."
            a "To be honest, the undercover part was always my least favorite part of being a spy. I was never very good at it."
            y "I'm afraid it comes with the job and we really need you right now. Plus, so far you're doing great."
            a y29 "You think so?"
            a y1 "Okay well if it will help the mission then I will give it my all!"
            a "I'll even wear a fake moustache and glasses if I have to!"
            y "Yeah... somehow I don't think that will be nessecary. How about lingerie instead?"
            a y16 "What's lingerie?"
            y "................."
            y "I'll explain it some other time."
            a y1 "Okay, you can count on me!"
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 7:
            $ alexSocial = 8
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a "[playerName]!"
            y "Oh hi, Alex."
            a y14 "I looked up what lingerie is and...!"
            y "Now don't be angry, Alex. It was just a jo-..."
            a y38 "And if it will help the mission then I'll do it!"
            y "You will?"
            a y5 "It was kind of naughty, but I'll wear it... If it'll help the mission...."
            y "You don't sound very motivated."
            a y28 "I am! Really!{w} It just takes some getting used to... I'm normally not exactly seen as... 'sexy'."
            y "What do you mean?"
            a y19 "Well you know... Sam is a sexy redhead and Clover can wrap any guy around her finger."
            a "But I sorta feel like the odd one out. I don't know how to look 'hot'...."
            y "Then we'll practise it. Next time you go out, show a little more skin and see if guys notice."
            a y20 "{b}*Nods*{/b} I'll try."
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 8:
            $ alexFriend = "Good Friend"
            $ alexSocial = 9
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a y39 "{b}*Grumbles*{/b}"
            y "Uh oh... Is Alex feeling moody today~...?"
            a y12 "I tried your suggestion... Y'know, to show a little more skin."
            y "And I take it, it didn't work?"
            a y20 "No..."
            a "Noone even batted an eye..."
            y "Really? What did you show off?"
            a y1 "Oh I wore a shirt with short sleaves."
            y "................."
            y "Alex, when I said 'show off some skin' I meant cleavage."
            a y29 "O-oh...!"
            a "That makes a lot more sense....!"
            y "If you want to be sexy, try wearing a shorter skirt, change your hairstyle, show off some cleavage!"
            a y1 "O-okay...! I'll try! Thanks,[playerName], you're the best teacher!"
            y "Yes, yes I am."
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 9:
            $ alexSocial = 10
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow y1 at ri with d3
            y "And? Tried showing off a bit more today?"
            a "I did and I got loads of attention!"
            y "See? All you have to do i-..."
            a y28 "I took off my top in public!"
            y ".........................."
            y "You what?"
            a y2 "Yeah! I decided I might aswell show my dedication and I took my top off. And I got a lot of attention!"
            y "................"
            menu:
                "Encourage sluttiness" if True:
                    $ slutPublic += 1
                    y "Ah well, who am I to argue with results. Keep up the good work, Alex!"
                    a y1 "It was fun! Boys from all over the place started cheering!"
                    a "I've never had this much attention!"
                    a y4 "......................"
                    a "I feel a little guilty though. My mom always told me {i}'not'{i} to show off my nudies...."
                    y "There is a time and place for it. For now, good work Alex."
                "Discourage sluttiness " if True:
                    y "Maybe not take it {i}'that'{/i} far."
                    a y16 "What do you mean...?"
                    y "Don't get me wrong, this is 'definitely' a way to get noticed, but we're still hiding remember?"
                    y "Wearing some more sexy clothes is fine, just don't go around flashing the entire neighborhood next time."
                    a y1 "Okay!"
            "Alex smiles and nods."
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 10:
            $ alexSocial = 11
            $ alexDailyChat = 1
            pause 0.2
            show scene_darkening with d3
            pause 0.3
            show yellow at ri with d3
            a "Today I wanna learn more about you, [playerName]!"
            y "About me?"
            a "Yeah! Like where you're from, what your hobbies are, if you have a girlfriend, what your job before joining WOOHP was."
            y "Those... sure are a lot of questions."
            y "I guess I could tell you... except for the previous job..."
            a y18 "Why not?"
            y "I... I used to be a prison guard, but...."
            stop music
            play sound "audio/sfx/panic2.mp3" fadein 5.0
            show black:
                xalign 0.0 yalign 0.0 alpha 0.0
                linear 8.0 alpha 0.8
            y "...............................................................................................................\n...............................................................................................................\n...................................................................................................................\n............................................................{nw}"
            hide black
            stop sound
            y "Alex... please tell me I'm not a bad person."
            a y28 "Of course you're not! You're part of the good guys, right? And you're helping us take back WOOHP!"
            y "Yeah.... Yeah, you're right..."
            y "And will I continue being your friend even if you find out about some.... iceberg related incidents...?"
            a y42 "I will always be your friend, [playerName]! No matter what lettuce you like!"
            y "Lettuce? That's not what I-....{w} Oh... iceberg... lettuce. I get it."
            y "All right, Alex. Good chat. Now if you'll excuse me, I'm going to take a shower and wash away the sins."
            a y1 "Okay [playerName], have fun!"
            hide scene_darkening
            hide yellow
            with d3
            pause 0.3
            scene bgBase with fade
            jump base
        if alexSocial == 11:
            if outsideRank >= 2:
                $ alexSocial = 12
                $ alexDailyChat = 1
                pause 0.2
                show scene_darkening with d3
                pause 0.3
                show yellow at ri with d3
                y "All right Alex. I think you're way too innocent. Let's find out some naughty things about you."
                y "What's your favorite position?"
                a "The Sweeper!"
                y "..............."
                y "The what? I don't think I know that one."
                a y28 "Yeah, as a Sweepers you get all the attention. You're expected to be flexable and all over the place!"
                y "Oh I see...! Tell me more."
                a y1 "You're often the most important member of the group!"
                y "G-group? Wow Alex, that's kind of kinky."
                a y42 "Plus they pass you the ball more often so you can score!"
                y "Ball...?"
                y "........................."
                y "You're talking about soccer, aren't you?"
                a y41 "Yeah!{w} Wait... what are 'you' talking about?"
                y "Nothing. It seems a shame to corrupt such a sweet innocent mind of yours."
                a y1 "Awe~... thanks [playerName]!"
                hide scene_darkening
                hide yellow
                with d3
                pause 0.3
                scene bgBase with fade
                jump base
            elif True:
                "You don't have anything to talk about."
            jump alexCall
        if alexSocial == 12:
            if outsideRank >= 3:
                $ alexSocial = 13
                $ alexDailyChat = 1
                pause 0.2
                show scene_darkening with d3
                pause 0.3
                show yellow y19 at ri with d3
                $ alexFriend = "Best Friend"
                a "[playerName]..."
                y "Alex...?"
                stop music fadeout 1.0
                a "................................"
                a "I want you to have something."
                y "A gift? For me?"
                a "Yeah... I've had it for a while now, but I think I don't need it anymore..."
                play music "audio/music/ahsoka.mp3" fadein 3.0
                a "............."
                "Alex hands you her golden four leafed clover broche."
                a y20 "Remember this?"
                y "Yeah.. it's something you bought a while ago from that shady street merchant. You want me to have it...?"
                a y14 "Yes. It's suppose to bring you luck, but..."
                a y13 "I think I'm pretty lucky to you have you as a friend already."
                y "Alex..."
                a y15 "Please hold on to it, okay? It will bring you everything you ever wanted."
                y "I will treasure it forever, Alex. I promise."
                "Alex throws her arms around you and burries her face in your chest. Hugging you tightly."
                a "Once Beverly Hills is back to normal. Will we stay friends...?"
                y "Yes Alex. Yes we will."
                "You hug Alex back."
                scene black with longFade
                stop music fadeout 3.0
                scene bgBase with longFade
                jump base
            elif True:
                "You can't think of anything to talk about right now. Maybe try raising your rank with the Outsiders first."
                jump alexCall
        elif True:
            "You can't think of anything to talk about right now. Maybe try raising your rank with the Outsiders first."
    elif True:
        "You already spoke with Alex today."
        jump alexCall
    jump base





screen nanoLevelClover:
    vbox xalign 0.5 yalign 0.0:
        imagebutton:
            idle "gui/nanobotLvlBg.png"
            hover "gui/nanobotLvlBg.png" tooltip "ttNanoControl"
            action Jump("cloverCall")
    $ tooltip = GetTooltip()
    if tooltip == "ttNanoControl":
        text "{font=fonts/freshMarker.ttf}{size=-4}Nanobot Control{/size}{/font}" xpos 560 yalign 0.07
    vbox xalign 0.51 yalign 0.025:
        text "{font=fonts/freshmarker.ttf}[nanoLevelClover]/100{/font}"

label cloverCall:
    if spy2Status == 0:
        show screen nanoLevelClover
        if spyRoomRand == 1:
            call undressClover from _call_undressClover_5
            $ top11Clover = True
            $ hat11Clover = True
            $ redChest = 11
            $ redHat = 11
        if spyRoomRand == 2:
            call undressClover from _call_undressClover_6
            $ redArms = 2

        menu:
            "???" if slutLevel == 0:
                jump cloverCall
            "Nanobot control" if slutLevel >= 1:
                jump sexScenesClover
            "Chat" if tod == 2 and spy2Status == 0 and cloverSocial <= 12:
                if spyRoomRand >= 1:
                    hide screen nanoLevelClover
                    $ spyRoomRand = 0
                jump cloverSocial
            "Change naming" if True:
                menu:
                    "Call me..." if True:
                        menu:
                            "New Guy" if True:
                                $ playerName = "New Guy"
                                c "Sure, I can call you New Guy."
                            "Lowlife" if cardSWTitle == True:
                                $ playerName = "Lowlife"
                                c "That's a weird nickname... But I guess I can call you that from now on."
                                jump cloverCall
                            "Boss" if True:
                                if slutLevel <= 2:
                                    c "Let's not get carried away now..."
                                    c "I think I'll keep calling you [playerName] for now."
                                elif True:
                                    $ playerName = "Boss"
                                    c "Well you do order me around a lot..."
                                    c "I guess I might aswell call you Boss."
                            "Master" if True:
                                if slutLevel <= 3:
                                    c "I don't know... That sounds kind of wrong."
                                    c "I think I'll keep calling you [playerName] for now."
                                elif True:
                                    $ playerName = "Master"
                                    c "Master...? Oh well... I mean I guess that's okay."
                                    c "Okay fine, I'll call you my Master from now on."
                        jump cloverCall
                    "Call yourself..." if True:
                        menu:
                            "Girl" if True:
                                $ cloverNick = "Girl"
                                c "Girl? Er... sure why not."
                            "Parsnip" if True:
                                $ cloverNick = "Parsnip"
                                c "I still think this is a really stupid nickname... Fine... Parsnip it is..."
                            "Bitch" if True:
                                if slutLevel <= 2:
                                    c "B-... That's so rude! Why would you even say that?!"
                                    c "I'm not your or anyone's bitch. So you can just forget it!"
                                elif True:
                                    $ cloverNick = "Bitch"
                                    c "Bitch...? Like those girls online who wear the collars...?"
                                    c "I dunno. I guess I wouldn't mind if you called me Bitch."
                            "Whore" if True:
                                if slutLevel <= 3:
                                    c "What?! I'm only doing this to help safe WOOHP! I am 'not' a whore!"
                                    c "I can't believe you just said that to me! There's no way I'll call myself that!"
                                elif True:
                                    $ cloverNick = "Whore"
                                    c "Heh heh~... Whore, huh?"
                                    c "That seems... oddly fitting for someone like me, doesn't it~...?"
                                    c "Heh... Okay! I'll be your Whore, [playerName]!"
                            "Gang Trash" if True:
                                if slutLevel <= 4:
                                    c "Listen [playerName]... Just because I'm going undercover doesn't mean you can call me that."
                                    c "I'm still a spy and I'm still one of the good guys. So please don't call me that."
                                elif True:
                                    $ cloverNick = "Gang Trash"
                                    c "Gang Trash?! But I'm not...!"
                                    c "I'm..."
                                    c "......................"
                                    c "Man... I really have turned into that, haven't I?{w} Fine, no other way around it. I'm Gang Trash and you can call me that."
                            "Fuck Toy" if True:
                                if slutLevel <= 4:
                                    c "F-fuck toy?!"
                                    c "That is very inappropriate, [playerName]!"
                                    c "Please don't suggest that to me again!"
                                elif True:
                                    $ cloverNick = "Fuck Toy"
                                    c "Heh~... Is that how you see me? As your toy?"
                                    c "Well I do let you play with me a lot~... I guess being called a Fuck Toy isn't so bad~..."
                            "Cum Dumpster" if True:
                                if slutLevel <= 4:
                                    c "C-...! [playerName] are you feeling okay...?"
                                    c "You shouldn't call girls that! I'll pretend that I didn't hear it."
                                elif True:
                                    $ cloverNick = "Cum Dumpster"
                                    c "Cum Dumpster...? That sounds so wrong!"
                                    c "Like I'm just a deposit for your semen...."
                                    c "................."
                                    c "Well I mean... That is kinda what I'm being used for."
                                    c "Fine. I'll be your Cum Dumpster, [playerName]."
                            "Semen Demon" if True:
                                if slutLevel <= 4:
                                    c "......................."
                                    c "Is that a normal thing to say to a girl?"
                                    c "You should be ashamed of yourself! Let's not bring this up again!"
                                elif True:
                                    $ cloverNick = "Semen Demon"
                                    "{b}*Smirks*{/b} That's so wrong~..."
                                    c "But I kinda like it~... All right, [playerName]. I'll be your little Semen Demon~..."
                            "Anal Agent" if True:
                                if slutLevel <= 4:
                                    c "A-anal what?! Listen here [playerName], let's not talk about this right now!"
                                    c "Or ever! Let's drop it completely!"
                                elif True:
                                    $ cloverNick = "Anal Agent"
                                    c "Anal Agent. Literacy, I like it. Also it's weirdly appropriate~..."
                                    c "I guess I've earned that nickname by now~... Sure call me whatever you like, [playerName]."
                        jump cloverCall
                    "Back" if True:
                        jump cloverCall
            "Decorate cell" if True:
                label decorateCloverCell:
                    pass
                call screen cellCloverDeco
            "Never mind" if True:
                hide screen nanoLevelClover
                $ spyRoomRand = 0
                hide cellClover
                jump base
    elif True:
        "Clover isn't available right now."
        jump base





screen nanoLevelAlex:
    vbox xalign 0.5 yalign 0.0:
        imagebutton:
            idle "gui/nanobotLvlBg.png"
            hover "gui/nanobotLvlBg.png" tooltip "ttNanoControl"
            action Jump("alexCall")
    $ tooltip = GetTooltip()
    if tooltip == "ttNanoControl":
        text "{font=fonts/freshMarker.ttf}{size=-4}Nanobot Control{/size}{/font}" xpos 560 yalign 0.07
    vbox xalign 0.51 yalign 0.025:
        text "{font=fonts/freshmarker.ttf}[nanoLevelAlex]/100{/font}"

label alexCall:
    if spy2Status == 0:
        show screen nanoLevelAlex
        if spyRoomRand == 1:
            call undressAlex from _call_undressAlex_7
            $ top11Alex = True
            $ hat11Alex = True
            $ yellowChest = 11
            $ yellowHat = 11
        if spyRoomRand == 2:
            call undressAlex from _call_undressAlex_8
            $ yellowArms = 2

        menu:
            "???" if slutLevel == 0:
                jump alexCall
            "Nanobot control" if slutLevel >= 1:
                jump sexScenesAlex
            "Chat" if tod == 2 and spy3Status == 0 and alexSocial <= 12:
                if spyRoomRand >= 1:
                    hide screen nanoLevelAlex
                    $ spyRoomRand = 0
                jump alexSocial
            "Change naming" if True:
                menu:
                    "Call me..." if True:
                        menu:
                            "New Guy" if True:
                                $ playerName = "New Guy"
                                a "Sure, I can call you New Guy."
                            "Lowlife" if cardSWTitle == True:
                                $ playerName = "Lowlife"
                                a "That's a weird nickname... But I guess I can call you that from now on."
                                jump alexCall
                            "Boss" if True:
                                if slutLevel <= 2:
                                    a "Let's not get carried away now..."
                                    a "I think I'll keep calling you [playerName] for now."
                                elif True:
                                    $ playerName = "Boss"
                                    a "Well you do order me around a lot..."
                                    a "I guess I might aswell call you Boss."
                            "Master" if True:
                                if slutLevel <= 3:
                                    a "I don't know... That sounds kind of wrong."
                                    a "I think I'll keep calling you [playerName] for now."
                                elif True:
                                    $ playerName = "Master"
                                    a "Master...? Oh well... I mean I guess that's okay."
                                    a "Okay fine, I'll call you my Master from now on."
                        jump alexCall
                    "Call yourself..." if True:
                        menu:
                            "Girl" if True:
                                $ alexNick = "Girl"
                                a "Girl? Well obviously I'm a girl~..."
                            "Canary" if True:
                                $ alexNick = "Canary"
                                a "Tjirp tjirp...!"
                            "Banana" if True:
                                $ alexNick = "Banana"
                                a "Rich in calcium! All right, I'll be Banana from now on."
                            "Bitch" if True:
                                if slutLevel <= 2:
                                    a "{b}*Gasp*{/b} You said a naughty word....!"
                                    y "Alex... put down that bar of soap...!"
                                    a "GET OVER HERE! I need to clean your mouth!"
                                    y "AAAAAAH!"
                                elif True:
                                    $ alexNick = "Bitch"
                                    a "Yay! I'm [playerName]'s bitch!"
                                    y "You... seem excited..."
                                    a "I recently found out that {i}'bitch'{/i} is a term of endearment between people who like each other very much!"
                                    y "Well obviously. I like you a lot Alex."
                                    $ yellowBlush = 1
                                    a "D'aww.."
                            "Whore" if True:
                                if slutLevel <= 3:
                                    a "Isn't being called a whore a bad thing...?"
                                    a "I'd rather not [playerName]...."
                                elif True:
                                    $ alexNick = "Whore"
                                    a "A whore is a girl who has loads and loads of sex!"
                                    a "Are we going to have loads of sex, [playerName]?"
                                    y "As much as you like."
                            "Gang Trash" if True:
                                if slutLevel <= 4:
                                    a "I don't like being called trash..."
                                    a "But you can call me a gangster!{w} Phew! Phew!"
                                    "Alex pretends her hands are guns."
                                    y "..............."
                                elif True:
                                    $ alexNick = "Gang Trash"
                                    a "Okay."
                                    y "That was easy."
                                    a "Well I'll have you know, I am {i}'very'{/i} easy."
                                    y "(Should I tell her what that means...?)"
                                    "Inner Voice" "Don't you dare."
                            "Fuck Toy" if True:
                                if slutLevel <= 4:
                                    a "Like a dildo?"
                                    a "I am not a dildo, [playerName]!"
                                    a "Dildos are meant to bring pleasure to girls. Do you want me to make out with Clover instead?"
                                    y "................."
                                elif True:
                                    $ alexNick = "Fuck Toy"
                                    a "I like toys!"
                                    a "And I like fucking..."
                                    a "I guess I can be your fuck toy!"
                            "Cum Dumpster" if True:
                                if slutLevel <= 4:
                                    a ".............................."
                                    a "I don't get it...."
                                    y "..........."
                                elif True:
                                    $ alexNick = "Cum Dumpster"
                                    a "Oooooh I get it! Cause you dump all your cum in me!"
                                    a "All right, in that case you should cum inside me many more times, else the nickname doesn't make sense."
                                    y "Promise."
                            "Semen Demon" if True:
                                if slutLevel <= 4:
                                    a "Demons are scary!"
                                    y "Alex..."
                                    a "NOOOOOOOOOOOOO!"
                                    "Alex ran away~..."
                                elif True:
                                    $ alexNick = "Semen Demon"
                                    a "Demons are scary!"
                                    y "Alex..."
                                    a "NOOOOOOOOOOOOO!"
                                    "Alex ran away~..."
                                    y "I'M STILL GOING TO CALL YOU THAT!"
                                    "...................."
                                    "Alex is no longer in hearing range."
                            "Anal Agent" if True:
                                if slutLevel <= 4:
                                    a "That sounds so crude... Can't I be a Butt Agent instead?"
                                    y "................"
                                elif True:
                                    $ alexNick = "Anal Agent"
                                    a "Yes sir! I promise to be the best anal agent in WOOHP!"
                        $ yellowBlush = 0
                        jump alexCall
                    "Back" if True:
                        jump alexCall
            "Decorate cell" if True:
                label decorateAlexCell:
                    pass
                call screen cellAlexDeco
            "Never mind" if True:
                hide screen nanoLevelAlex
                $ spyRoomRand = 0
                hide cellAlex
                jump base
    elif True:
        "Alex isn't available right now."
        jump base

default prisonersNew = False
default maggieSocial = 0
default melodySocial = 0
default carlaSocial = 0
default taliaSocial = 0
default muffySocial = 0

label prisonersCall:
    menu:

        "{color=#EFD66D}Inspect prisons{/color}" if task3Stage >= 7 and task7Stage == 0:
            if spy1Status == 0 and spy2Status == 0 and spy3Status == 0:
                pass
            elif True:
                y "(Maybe I should wait until the girls are available before exploring around.)"
                jump base
            $ task7Stage = 1
            jump task7
        "Visit Maggie T." if specialMaggieStatus == 2:
            if maggieSocial == 0:
                jump task3
            elif maggieSocial == 1:
                "MAGGIE SOCIAL TREE NOT IN YET."
                jump prisonersCall
            elif True:
                "MAGGIE SOCIAL TREE NOT IN YET."
                jump prisonersCall

        "Visit Tim Scam" if task26Stage == 16:
            jump task26

        "Visit Carla Wong" if specialDragonStatus == 2:
            if carlaSocial == 0:
                jump task10
            elif carlaSocial == 1:
                "MAGGIE SOCIAL TREE NOT IN YET."
                jump prisonersCall
            elif True:
                "MAGGIE SOCIAL TREE NOT IN YET."
                jump prisonersCall

        "Visit Talia Hardwire" if specialTaliaStatus == 2:
            if taliaSocial == 0:
                jump task18
            elif taliaSocial == 1:
                "MAGGIE SOCIAL TREE NOT IN YET."
                jump prisonersCall
            elif True:
                "MAGGIE SOCIAL TREE NOT IN YET."
                jump prisonersCall

        "Visit Muffy Peprich" if specialMuffyStatus == 2:
            if muffySocial == 0:
                $ muffySocial = 1
                $ specialMuffyBounty = True
                $ specialMuffyStatus = 3
                show scene_darkening with d3
                y "Muffy~... Muffy Muffy Muf~..."
                muff "........................."
                y "I read your file and it says here you're a sorority girl."
                y "Not exactly what I expected from a punk rocker."
                muff "{b}*Scoffs*{/b} I was rejected from every sorority I applied to. That's why I created my own."
                y "And then mind controlled the other sororities into joining you..."
                y "Still... Why join the Outsiders? Wouldn't the Aces or Drift Punk have been a better fit for you?"
                muff "I did some thinking in prison..."
                muff "After some deep reflecting and inner soul searching...."
                y "Yes~...?"
                muff "I decided I shouldn't be held responsible for my actions! It was all society's fault!"
                y "..................."
                muff "Who cares about a stupid sorority when the {i}man{/i} is still out there keeping you down?!"
                show yellow y1 at le with d3
                a "Hey [playerName]. Any luck with Muffy?"
                muff "You...!"
                muff "I'll get you for this, Alex! Better sleep with one eye open cause I'm coming for you when you least exp-..."
                a y56 "Hey... Her eyes are red."
                y "...?"
                y "Ah damn it... she's under nanobot control aswell. All right Muffy, drop your panties."
                muff "W-what?"
                a y55 "Don't worry! He's just gonna break the nanobot control over you by putting his peepee in you!"
                muff "................."
                y ".................."
                muff "Fine... as long as the banana isn't here to watch."
                y "Deal."
                a y28 "Banana?!"
                hide yellow with d3
                "You shoo Alex out of the cell."
                scene black with fade
                pause 0.4
                muff "Yes! Yes! Rock on!"
                muff "Ahh! Ah! Ah! ♥♥"
                muff "Who cares about overthrowing the world! I wanna keep doing this forever!"
                muff "Ahhhh! ♥♥♥♥♥♥"
                y "Say cheese!"
                show white
                play sound "audio/sfx/camera.mp3"
                hide white with d2
                show picMuffy:
                    xalign 0.5 yalign 0.5
                pause
                hide picMuffy
                with d3
                "A new photo has been added to your photoalbum."
                scene bgPrison with fade
                show scene_darkening with d3
                muff "{b}*Pant* *Pant*{/b} Now that was {i}intense{/i}!"
                y "Still feeling evil?"
                muff "I'm a villain, of course I still feel evil. {w}But at least I no longer want to work for the Outsiders."
                y "Then let's talk for a bit..."
                "Muffy tells you everything she knows about WOOHP HQ and the mastermind's plans."
                $ randIntel = 300
                $ intel += 300
                call missionRewardInt from _call_missionRewardInt_22
                pause 0.4
                muff "So... seeing as I hel-..."
                y "I'm not letting you go."
                muff "Oh..."
                pause 0.7
                "Computer" "Muffy Peprich status: Captured.{w} Allocating resources..."
                $ randMoney = 500
                $ cash += 500
                call missionRewardMoney from _call_missionRewardMoney_71
                hide scene_darkening with d3
                scene bgBase with fade
                jump base
            if muffySocial == 1:
                "Not yet in"
                scene bgBase with fade
                jump base
        "Visit Melody G." if specialMelodyStatus == 2:
            if melodySocial == 0:
                jump task6
        "Visit Candy Sweet" if specialCandyStatus == 2 and task16Stage == 5:
            jump task16
        "Visit Sebastian Sage" if specialSebStatus == 2:
            jump task23
        "Visit The Great Kandinsky" if specialKandStatus == 2 or task25Stage == 10:
            jump task25
        "Visit Britney" if task26Stage == 10:
            jump task26

        "Visit Felicity Fences" if specialFelicityStatus == 2:
            jump task21
        "Back" if True:

            scene bgBase with fade
            jump base





default socialSilva = 0

label socialSilva:
    scene black with fade
    if socialSilva <= 7:
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
    elif True:
        scene bgBar with fade
    if 0 <= socialSilva <= 1:
        $ socialSilva = 2
        "The journey is made more difficult by the wild plants and trees growing everywhere now."
        stop music fadeout 1.5
        y "It's like a freakin' jungle here!"
        play music "audio/music/silva2.mp3" fadein 1.5
        sil "Ce n'était pas ma faute!"
        y "....?"
        "That sounded like Silva as you begin making your way to the noise."
        y "Sil?"
        sil "!!!"
        with hpunch
        "Suddenly you're snatched up by a gigantic carnivorous plant!"
        y "ARGH!"
        sil "Non! Non, put him down! Bad plant!"
        "A second later you're spat out again as you drop down to the pavement below."
        y "......................."
        y "Traumatizing."
        show scene_darkening
        with d3
        show silvaModel:
            xalign 0.9 yalign 0.0
        with d3
        sil "Oh! Are you okay? Sorry, he iz a bit overzealous with guarding ze garden."
        y "No kidding. Think you might've gone a bit overboard? It's like a jungle in here."
        sil "Overboard? No no, if anything I haven't done enough! So many pretty flowers!"
        sil "Ze world would be so much nicer if we replaced all these ugly concrete parking lots with colorful plants, non?"
        y "And where are us humans suppose to live then?"
        sil "Oh I have thought of zhat too! Humans can all live in these vine caves! Zhey're water tight, isolating and can grow in size to support large families!"
        y "And one may accidentally molest your girlfriend."
        sil "Tentacles have a mind of their own. Zhey can't help it!"
        y ".........."
        y "Parking lots sound pretty appealing right now..."
        sil "Oh vous of little faith. I am going to make zhis world beautiful. You'll see! As soon as ze mastermind picks me as their righthand woman, I shall take back the world that was taken from nature and return it to its original, beautiful state."
        y "Yeah... That's what I'm worried about."
        hide silvaModel
        hide scene_darkening
        with d3
        "You spend the rest of the day chatting with Silva Abegail. When it gets late, you return to the base."
        scene black with fade
        $ tod = 2
        jump jobReport
    if socialSilva == 2:
        $ socialSilva = 3
        y "(All right, to avoid that big ass plant this time, I brought some dog treats.)"
        "With dog treats in hand, you begin making your way through the jungle of Les Épines."
        y "(It's even denser than last time... Now was it left or rig-...)"
        stop music fadeout 3.0
        sil "Attention!"
        y "!!!"
        "Just in time you notice a large bed of flowers, completely covered in massive thorns."
        show scene_darkening
        with d3
        play music "audio/music/silva2.mp3" fadein 1.5
        show silvaModel:
            xalign 0.9 yalign 0.0
        with d3
        y "(That was close...)"
        sil "Welcome to my little garden, mon ami! It iz always good to see you!"
        sil "Oh and please watch out for ze thorns on those plants. They are highly acidic and will burn through human flesh with ease."
        y "Sil! Keep your weeds in check!"
        sil "Zhey are not weeds! I planted zhem there myself!"
        y "As a trap?"
        sil "No, because zhey look nice!"
        y "................"
        y "I-..."
        sil "Before you say something! Remember that nature also provides."
        "Silva hands you a pear as the two of you make your way through the bush."
        y "Your gangsters must have a hard time making their way past all the dangerous plants, right?"
        sil "............."
        sil "Oh...! No, not at all! Zhey know what to look out for."
        y "Where are they anyways?"
        sil "On a daring mission to bring me back-..."
        y "More plants?"
        sil "How did you know?!"
        hide silvaModel
        hide scene_darkening
        with d3
        "You and Silva spend the rest of the day chatting. When it turns dark, you carefully make your way back to the base."
        scene black with fade
        $ tod = 2
        jump jobReport
    if socialSilva == 3:
        $ socialSilva = 4
        y "(How upset would Abegail be with me if I brought some Weed Killer? Best not risk it.)"
        "You begin your safari through the jungle, making sure to dodge any dangerous obstacle you come across."
        stop music fadeout 1.0
        show scene_darkening
        with d3
        show silvaModel:
            xalign 0.9 yalign 0.0
        with d3
        play music "audio/music/silva2.mp3" fadein 1.5
        sil "♫♪ {i}'Alouette, gentille alouette. Allouette, je te plumerai~...'{/i} ♫♪"
        y "Are you singing to your plants?"
        sil "Oh! Hello again! Why oui, I am!"
        y "That's kinda crazy, Sil."
        sil "Takes one to know one, mon ami."
        y "......................."
        y "Touché."
        sil "Oh! Zhat was French. Very good!"
        sil "Have you come to chat?"
        "The two of you find a nice place to sit down and have some tea."
        y "I gotta say Abegail. For being a bit of a botanical fanatic, you're not a bad neighbor to have around."
        sil "Non?"
        y "I never hear of any issues caused by your gang. No gunshots, no fires in the streets."
        y "Sure, I have to sometimes dodge one of your abominations, but so far none of your plants have eaten any of my staff yet."
        sil "Staff? Oh! Wait, you mentioned opening a bar, oui?"
        sil "Please tell me more!"
        y "Er...."
        y "Well it's what you'd expect. We serve food and people come there to relax. We managed to declare neutral ground, so everyone is allowed to show up without the fear of being attacked by a rival gang."
        sil "Oh zhat sounds wonderful!{w} Can I visit sometime?"
        y "I don't see why not. Just don't bring any of your killer plants."
        y "That actually reminds me... I don't think I've seen {i}'any'{/i} gangmembers of Les Épines visit the bar before."
        sil "Oh you know. Busy, busy! We have a world to conquer, you know!"
        sil "..................."
        sil "A-anyways, I would love to visit. I'll stop by sometime soon!"
        hide silvaModel
        hide scene_darkening
        with d3
        "You and Sil spend the rest of the day chatting before you head back home."
        scene black with fade
        $ tod = 2
        jump jobReport
    if socialSilva == 4:
        $ socialSilva = 5
        y "(Maybe I should bring snacks next time.{w} What does Sil even eat...?)"
        y "(Those hippy types seem to love vegan stuff, but if I show up with a salad she might get angry at me for bringing her dead plants.)"
        y "(I'll be sure to think it ove-...)"
        y "Oh!"
        with hpunch
        stop music fadeout 1.0
        "You tripped over a pair of overgrown boots!"
        play music "audio/music/silva2.mp3" fadein 1.5
        y "Oh right... hazardous jungle. Best pay attention."
        show scene_darkening
        with d3
        show silvaModel:
            xalign 0.9 yalign 0.0
        with d3
        sil "Oh bonjour!{w} Why are you lying on the ground? Are you tired?"
        y "Tired of having to pack my safari hat everytime I want to come visit you."
        sil "Oh look like somebody has a case of the grumpies!{w} Come, I'll make tea."
        "The two of you find a nice spot to sit down for tea."
        y "So your reputation is growing."
        sil "Oui?"
        y "Yeah, I overheard some gangsters mention being too afraid to go near your jungle."
        sil "Ah... I see."
        sil "Well I'm glad zhey are clever enough not to mess with moi."
        y "I haven't seen any of your gangmembers in ages. Are they still out gathering plants?"
        sil "Indeed! A ficus to be more precise. One that grows the most delicious fruits, but spews forth chloroform gas if you get too close!"
        y "Jesus! Why can't you just plant some nice daffodils instead?!"
        sil "All plants deserve love!"
        y "Do all humans deserve love?"
        sil "Well... No I guess not."
        y "Then not all plants deserve love either. Some plants are just dickbags."
        sil "I promise that when I rule the planet, I'll make sure only nice plants grow around your house."
        y "If I survive the eucalyptus apocalypse that is."
        sil "Oh! A plant pun. Very good!"
        hide silvaModel
        hide scene_darkening
        with d3
        "You and Sil spend the rest of the day chatting before you head back home."
        scene black with fade
        $ tod = 2
        jump jobReport
    if socialSilva == 5:
        $ socialSilva = 6
        "{b}*Buzzzzzz*{/b}"
        y "Huh...?"
        "{b}*Buzzzzzz*{/b}"
        y "OW!"
        "You slap your arm and kill a mosquito that bit you."
        y "First deadly plants and now mosquitos..? I'm gonna end up getting malaria in this jungle...."
        y "Maybe next time I'll ask Silva to come meet me at my pla-....{w} Huh...?"
        "You see something shiny in the dirt. Upon closer inspect you see...."
        y "A golden watch?{w} And a golden ring?!{w} Okay I take it back. This place is awesome."
        stop music fadeout 1.0
        show scene_darkening
        with d3
        show silvaModel:
            xalign 0.9 yalign 0.0
        with d3
        play music "audio/music/silva2.mp3" fadein 1.5
        s "Oooh, what's zis little fly I spot buzzing in my garden...~?"
        y "More like mosquito. You know you're gonna get sick with these around, right?"
        s "Mosquitos?! Oh no...."
        y "Oh no...?"
        sil "I'll explain later. First, come come! I made you lunch!"
        "The two of you find a nice spot to sit as Silva hands you a salad."
        y "Not gonna lie. This tastes amazing."
        sil "See? Nature is full of surprises!"
        sil "Sorry about the mosquito earlier. They came with the ficus I had brought in last time."
        sil "They seem to be spreading quicker than my plants can eat them."
        y "You might want to go buy some malaria pills."
        sil "Oh, I sent some of my men to buy some for moi.{w} But zhey haven't returned yet."
        "The two of you happily continue chatting throughout the lunch. When you finish up you thank Sil and get up to leave."
        sil "Are you... leaving so soon?"
        y "I sorta have a business to run."
        sil "Ah oui, I understand..."
        y "I can stay a bit longer if you like...?"
        sil "Oh oui! Want to help me water my daffodils?"
        hide scene_darkening
        hide silvaModel
        with d3
        "You and Sil spend the rest of the day chatting and taking care of the garden. When it starts getting dark, you head back home."
        scene black with fade
        $ tod = 2
        jump jobReport
    if socialSilva == 6:
        $ socialSilva = 7
        y "(Sometimes I wonder why I keep coming back here...)"
        "In the distance you softly hear singing."
        stop music fadeout 1.0
        sil "♫♪ {i}'Alouette, gentille alouette. {b}*Sniff*{/b}{w} Allouette, je te plumerai~...'{/i} ♫♪"
        y "Sil?"
        play music "audio/music/silva2.mp3" fadein 1.5
        show scene_darkening
        with d3
        show silvaModel:
            xalign 0.9 yalign 0.0
            pause 0.1
            linear 0.12 yalign 0.5
            linear 0.12 yalign 0.0
        with d3
        sil "{b}*Yelps*{/b}"
        "The startled Silva jumps into the air in surprise!{w} Followed by a massive flesh-eating plant biting down on on your head."
        scene black
        hide scene_darkening
        hide silvaModel
        y "!!!"
        menu:
            "SCREAM" if True:
                y "{b}*MUFFLED SCREAM*{/b}"
            "Remain calm" if True:
                y "......................."
                y "(I'm pretty sure this is somebody's fetish.)"
            "Say something insane" if True:
                y "{b}*Muffled insanity*{/b}"
        sil "Non! Non! We do {b}not{/b} eat our friends!"
        "After some concerned shouting, the plant finally let's go of you. Leaving you soaked in its saliva."
        scene bgStreet1
        show scene_darkening
        show silvaModel:
            xalign 0.9 yalign 0.0
        with d3
        y "Again... Ew."
        sil "I'm so sorry, mon ami! Are you okay?"
        y "About as okay as I usually am walking into this place. What about you?"
        sil "Moi?"
        y "I thought I heard you crying from a distance."
        "Silva wipes her eyes and smirks at you."
        sil "Oh non silly. I was cutting onions!"
        y ".............."
        y "Onions?"
        sil "Oui, for the hamburgers we are having!"
        y "Hamburgers? Where did you find beef in this woodland of yours?"
        sil "I had it delivered!"
        y "......................"
        "Out of the corner of your eye you suddenly see the torn up hat of a delivery boy."
        y "Oh Sil you didn't!"
        sil "Don't worry, don't worry. He is fine. My plants gave him a bit of a scare, but he got out {i}'mostly'{/i} unscathed."
        sil "Now let's eat!"
        "The two of you make a little fire in the center of a clearing and enjoy a freshly made burger together."
        y "And here I thought you'd be vegan."
        sil "{b}*Scoffs*{/b} Half my plants eat meat, why shouldn't I?"
        y "Can't argue with that."
        hide scene_darkening
        hide silvaModel
        with d3
        "You and Sil spend the rest of the day chatting. When it starts getting dark, you head back home."
        scene black with fade
        $ tod = 2
        jump jobReport
    if socialSilva == 7:
        $ gang4Active = False
        $ socialSilva = 8
        y "Let's see what Silva is up to today."
        "........................."
        "The jungle is thicker than ever! There are parts where you can barely see the sunlight coming in due to the trees."
        y "SILVA! This is getting out of hand!"
        y "......................"
        y "Silva?"
        "You look around, but can't find Silva anywhere."
        y "I guess she must be out..."
        "{b}*Russle* *Russle*{/b}"
        y "...?"
        "You hear something in the bushes..."
        y "Silva...?"
        y "AHH-...!"
        stop music
        scene black
        with hpunch
        "{b}*NOM*{/b}!"
        play music "audio/music/crisis.mp3"
        "You were eaten again! By a giant plant!"
        y "This is getting ridiculous! When I find Silva I'm going t-..."
        $ silOutfit = 3
        $ silFace = 2
        $ silHair = 1
        show silvaModel at ce
        with d3
        pause 0.5
        y "Silva...? Silva!"
        "She has been eaten by the plant!"
        pause 0.5
        sil "..................."
        y "Don't worry Abegail, I'm getting you out of here!"
        $ silFace = 3
        with d3
        sil "........?"
        sil "Mon amie...?"
        y "Sil! I thought you were dead for a second. Any suggestions on how to get out of here?"
        sil "Non... Non my friend. You shouldn't be here..."
        y "I know! And neither should you!"
        "You kick the plant from the inside as it begins to growl in protest."
        y "Yiiiiha!"
        "Tired of your antics, the plant spits the two of you out!"
        stop music fadeout 5.0
        $ silFace = 2
        scene bgStreet1 with fade
        pause 0.4
        show scene_darkening with d3
        show silvaModel at ce with d3
        y "Sil..? Are you okay?"
        sil "............................"
        y "Sil?"
        sil "I'm fine..."
        sil "........."
        hide silvaModel
        with d2
        $ silCry = True
        show silvaModel at ce
        with d2
        sil "{b}*Sniff*{/b} I'm fine..."
        y "Come, let's go find a safer place to sit down."
        show black with fade
        play music "audio/music/silva.mp3" fadein 3.5
        "The two of you walk to the edge of the forest and find a tree stump to sit down on."
        $ silModel = 2
        $ silOutfit = 0
        hide black with fade
        pause 0.6
        y "Silva, what's going on...? Where are your gang members?"
        sil "{b}*Sniff*{/b} Zhey're all gone... It iz just me left..."
        y "I don't understand..."
        sil "It iz theze stupid plants... The gangsters that didn't get eaten got stung by venomous thorns or choked by vines...!"
        sil "The onez that remained just ran away..."
        y "................."
        y "That doesn't explain why you were inside that plant, Sil. Why would your own plants attack you?"
        sil ".........................."
        y "Oh no...{w} It didn't attack you, did it?"
        sil "........................."
        y "Silva... why? You could've asked me for help..."
        sil "I got my entire gang killed... I deserve it..."
        y "No you don't. You're talking crazy. How long have you been alone...?"
        sil "................................................"
        y "Long...?"
        $ silFace = 3
        sil "Pretty much since we started talking...."
        y "You've been alone all this time?"
        $ silFace = 2
        sil ".................................."
        "You carefully throw your arms around Silva and hug her close to your chest."
        y "Silva... your gang is gone... Leave this jungle and come back with me."
        y "The Milkshake Bar has plenty of room and I know the girls will welcome you..."
        $ silFace = 2
        sil "{b}*Sniff*{/b} Je suis désolé...."
        y "I know Sil. {w}I know..."
        y "Come... let's go back. Let's get you somewhere safe and warm."
        show black with longFade
        stop music fadeout 5.0
        pause 5.0
        scene bgBase with fade
        pause 0.5
        show scene_fighting with d3
        "You quickly tell the shocked Silva who you and the spies really are and find her a bed to rest."
        "Silva Abegail can now be visited during the day at the Milkshake Bar."
        play music "audio/music/nighttime.mp3" fadein 2.0
        hide scene_fighting with d3
        $ tod = 2
        jump jobReport
    if socialSilva == 8:
        if task30Stage <= 2:
            "Silva is still recovering."
            jump club
        elif True:
            $ socialSilva = 9
            $ silOutfitSet = 2
            $ silOutfit = 2
            $ silCry = False
            $ silFace = 3
            $ silModel = 1
            show scene_darkening with d3
            show silvaModel at le with d3
            y "And this is the Milkshake Bar."
            sil "It iz a little much to all take in..."
            sil "So you are not a gangster?"
            y "Nope."
            $ silFace = 4
            sil "Heh... You and the girls sure fooled me."
            $ kimFace = 6
            show kim at ri with d3
            kim "Hey boss. Who's this?"
            y "Kim, I want you to meet Silva Abegail. Silva, this is Kim."
            sil "Bonjour Kim."
            $ kimFace = 1
            kim "Oooh French! The customers will love her!"
            y "Oh, she's not working here. Sil is just taking a small break."
            sil "............"
            sil "Actually... I would love working 'ere."
            y "Sil... are you sure?"
            sil "I've been living alone for too long... I wouldn't mind spending some time amongst ze people here."
            y "Er... you know this is a tittie bar, right?"
            sil "A... what?"
            y "Erm... a place where the staff gets groped a lot and take off their tops."
            $ silFace = 1
            sil "Oooh, reminds me of my time in Paris. I think I will fit right in!"
            kim "She's French {i}'and'{/i} she's eager! C'mon boss. Let her work here."
            y ".............."
            y "Well all right. But keep an eye on her Kim."
            $ kimFace = 3
            kim "Tsk, with a body like that, I'd like to keep both eyes on her."
            "Silva smiles shyly. You've never seen her like this before. She seems less confident, but more at ease."
            hide kim
            hide silvaModel
            with d3
            hide scene_fighting with d3
            $ tod = 2
            y "Well... she looks a little better. Maybe spending some time amongst people will do her some good."
            scene bgBase with fade
            jump jobReport
    if socialSilva == 9:
        $ socialSilva = 10
        $ silOutfit = 4
        $ silHair = 2
        show scene_darkening with d3
        show silvaModel at ce
        $ kimFace = 1
        show kim at le
        with d3
        y "And? How is she doing, Kim?"
        kim "Oh she fits right in. We customized her uniform a bit. Hope you don't mind."
        sil "....."
        sil "What do you think?"
        menu:
            "I love it" if True:
                y "You look good, Silva. Welcome to the family."
                sil "Heh..."
            "It's okay" if True:
                y "The outfit is pretty good, but I think I prefer your old one."
                sil "Well I do love my old one, but it sorta got eaten up by zhat plant."
                sil "There iz not much of an outfit left of it. It shows of all my goods!"
                y "{b}*Smirks*{/b} Exactly why I love it so much."
            "I hate it" if True:
                y "You look goofy wearing that."
                sil "O-oh... you think zo? I thought I'd theme it a bit... I'm zorry for change your uniform..."
        y "Has Kim been keeping you busy?"
        sil "Oh oui! We've been working 'ard together. She is a very talented waitress!"
        sil "She really knows how to behave around the customers and how to get the biggest tip."
        y "(I bet she does.)"
        $ kimFace = 5
        kim "I've got customers to serve. Don't take too long."
        hide kim with d3
        pause 1.0
        y "You seem to fit in pretty well."
        y "Does Kim know about your little stunt?"
        $ silFace = 3
        sil "Non...{w} I am afraid it might scare her off. Or make her think I'm a nutcase."
        y "Sil, you escaped from an asylum, dress like a plant and tried to take over the world with your botanical skills."
        sil "So?"
        y "....................."
        y "Anyways, It's good to see you two getting along. If there's any trouble let me know, okay?"
        $ silFace = 1
        $ tod = 2
        "Silva nods and gets back to work."
        scene bgBase with fade
        jump jobReport
    if socialSilva == 10:
        $ socialSilva = 11
        show scene_darkening with d3
        $ kimFace = 6
        show silvaModel at ce
        show kim at le
        with d3
        kim "Silva, I need you at table 4!"
        sil "Coming!"
        hide kim with d3
        y "I see Kim is working you hard."
        sil "Oui! I'm not used to be the one taking orders."
        y "I'll tell her to lay off you for a bit."
        sil "Oh non, I didn't mean it like that! I actually like not being the one in charge for once."
        sil "It feels good to talk to anyone other than plants for a change."
        y "And you don't mind showing yourself off a bit?"
        sil "Well...."
        sil "I haven't done a lot of that yet."
        y "Shy?"
        sil "Non it's not that..."
        kim "Sil?!"
        sil "Coming!"
        sil "We'll talk more later."
        hide silvaModel with d3
        "Silva runs off to continue waiting tables."
        $ tod = 2
        scene bgBase with fade
        jump jobReport
    if socialSilva == 11:
        $ socialSilva = 12
        show scene_darkening with d3

        with d3
        kim "Silva? Where are you, we have guests waiting!"
        show silvaModel at ce with d3
        sil "Shhh mon ami, come with me quick."
        y "Er... okay...?"
        hide silvaModel at ce
        show bgBase with longFade
        pause 0.5
        show silvaModel at ce with d3
        y "So why did I have to come with y-.."
        hide silvaModel with d2
        $ silOutfit = 0
        show silvaModel at ce with d2
        y "!!!"
        sil "I didn't want to show off at the milkshake bar before I showed you~..."
        sil "You like?"
        menu:
            "I like a lot" if True:
                sil "I thought you would~..."
                sil "I bet I could think of something you'd like even more~..."
            "Eh, I've seen better" if True:
                sil "{b}*Scoffs*{/b} Yeah...! Well... Like...!"
                sil "Let's zee if I can change your mind!"
            "Say something insane" if True:
                y "I want to water you right now."
                sil "Wha-...?"
                y "Like a plant!"
                sil "Is that a double entendre or are you serious...?"
                sil "Oh! Silly moi, I forgot that you were coo-coo. How about you and I teach you about the birds and the bees~..."
                y "....."
                y "And the flowers?"
                sil "Sure mon ami~..."
        scene black with fade
        sil "Ooooh~... ♥"
        sil "Mmmm.... right there~.... ♥♥♥"
        sil "Oui! Stick it in me! Harder!"
        sil "Ah! Ah! Ah! Oh!"
        y "Say cheese~...."
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d3
        pause 0.5
        show expression "gui/photos/other/picSilva.jpg":
            xalign 0.5 yalign 0.5
        with d3
        pause
        hide expression "gui/photos/other/picSilva.jpg" with d2
        scene bgBase with fade
        show scene_darkening with d3
        show silvaModel at ce with d3
        pause 0.4
        y "Phew~....! You might be crazy, but you're a damn good lay."
        sil "Right back at you~..."
        sil "Zhank you for taking care of me, mon ami."
        hide silvaModel with d3
        $ tod = 2
        scene bgBase with fade
        jump jobReport

    jump jobReport





default socialKim = 0

label socialKim:
    if socialKim == 0:
        $ socialKim = 1
        show scene_darkening with d3
        $ kimFace = 1
        show kim at ri with d3
        y "Hi Kim. How are you enjoying the life as a waitress?"
        kim "Technically I'm still on the clock as a spy so... double pay baby!"
        $ kimFace = 5
        kim "I'm not doing it for the money of course."
        y "Of course.{w} But I bet the tips don't hurt."
        $ kimFace = 1
        kim "They are so good~...!"
        y "You don't mind being groped now and again?"
        kim "Eh, not really. It's part of the job, right?"
        kim "Plus this is not the first time I've gone deep undercover. I got used to it pretty quickly."
        y "I'm glad you're taking it so serious! Okay we'll talk more later."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 1:
        $ socialKim = 2
        show scene_darkening with d3
        kim "C'mooon~... I know you want to~...."
        "{b}*Pinch*{/b}"
        kim "Oooooh ♥"
        pause 0.4
        $ kimFace = 1
        show kim at ri with d3
        y "I saw that. Getting customers to pinch you for tips?"
        kim "Yup."
        y "Good girl. I bet the customers are happy with that aswell."
        kim "Heh, you bet! This is making more than my spy job at this rate!"
        $ kimFace = 3
        kim "I {i}'accidentally'{/i} spilled a beer on my tits today and the guys doubled the bill!"
        y "Wow.. you 'are' good at this."
        kim "I know we're suppose to be saving the world and all, but this is getting me through college so er... no rush. Okay?"
        y "........................"
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 2:
        $ socialKim = 3
        $ kimFace = 1
        show scene_darkening with d3
        show kim at ri with d3
        kim "Slap."
        with hpunch
        "Kim just slapped you in the face... with a wad of dollar bills!"
        y "Do I even want to know what you did to get those?"
        kim "Nip slips."
        y "......."
        y "Yeah okay, I expected as much."
        y "Wow Kim, you're a much bigger slut than I had given you credit for!"
        $ kimFace = 2
        kim "Don't call me a slut!"
        y "Oh! I'm sorry, I thought yo-..."
        $ kimFace = 3
        kim "Not until you've paid me two dollars first."
        y "....................."
        menu:
            "Pay Kim 2 dollars" if True:
                $ cash -= 2
                play sound "audio/sfx/cashRegister.mp3"
                y "Here you go, you slut."
                kim "Yeah~... you like calling me that. Don't you."
                y "You cheap whore. Being bend over the diner tables to be fucked for tips!"
                kim "Mmmm~.... yes please~...."
                y "Gurgling down cum as it stains your uniform and sticks in your hair. Glazing your face as it drops out of your well worn pussy!"
                y "Lying pantsless on a table as patrons whip out their dicks to cum on the worthless waitress."
                kim "Ngh~... yes~...!"
                y "................................."
                y "Damn, this is fun. I can see how you do it."
                $ kimFace = 1
                kim "See? Well worth the 2 dollars, right?"
                y "Yeah!"
                y "Okay, good chat Kim. I'm going to grab a cold shower now."
            "Don't pay" if True:
                y "I'm your boss! You should be paying me!"
                $ kimFace = 5
                kim "That's not really how it works, [playerName]."
                y "................."
                y "You're still not getting those two dollars."
                kim "Suit yourself big guy. If you change your mind, you know where to find me...~"
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 2:
        $ socialKim = 3
        show scene_darkening with d3
        $ kimFace = 4
        show kim at ri with d3
        kim "..........................."
        y "Kim? Are you okay?"
        kim "Y-yeah yeah... just a little shook up, that's all."
        kim "A customer got aggressive and actually grabbed me by the throat."
        $ kimFace = 6
        kim "Now I'm all for getting choked, but normally that costs extra."
        y ".........................."
        y "Were you hurt?"
        $ kimFace = 5
        kim "No, it just surprised me. Luckily before I could ruin my cover, a few people rushed to my help and kicked the guy out."
        $ kimFace = 3
        kim "Which was a good thing, cause I felt my nipples getting hard!"
        y "........................."
        y "Kim, stop acting. Are you okay?"
        $ kimFace = 5
        kim "What do you mean?"
        y ".........................."
        kim "It... it's nothing..."
        y "You were attacked by a customer. It's okay to be upset."
        kim "............................"
        kim "You know... it's funny."
        $ kimFace = 6
        kim "Being a spy you face danger all the time, you sorta forget how fragile you are."
        kim "I've been in much worse situations, but... just imaging going out because of a drunk in a shady bar..."
        kim "It's kind of scary."
        y "Take the rest of the day off. Next time, don't worry about your cover. I wouldn't."
        $ kimFace = 1
        kim "Thanks boss...."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 3:
        $ socialKim = 4
        $ kimFace = 1
        show scene_darkening with d3
        show kim at ri with d3
        y "Hey Kim. Customers giving you anymore trouble?"
        kim "Nah, most people like this place because there's no fighting. It being neutral ground and all."
        kim "Earlier I saw some Outsiders hang out with Drift Punks."
        kim "There's been so much fighting in the streets that people just want to come in and relax. Grab a beer and ogle the girls."
        kim "And honestly, in a world where people kill each other over a few feet of 'turf'. Ogling girls isn't so bad in comparison."
        "Customer" "HEY KIM, WHERE'S MY BURGER?!"
        $ kimFace = 2
        kim "SHUT YOUR TRAP, I'M BUSY!"
        y "......................"
        $ kimFace = 1
        kim "So yeah, it's going pretty well!"
        y "I'll... leave you to your work."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 4:
        $ socialKim = 5
        $ kimFace = 1
        show scene_darkening with d3
        show kim at ri with d3
        y "Hello Kim, how is the restau-...{b}*Splesh*{/b}"
        y "...................."
        y "What did I just step in?"
        $ kimFace = 4
        kim "Oh that's a large Number 4 I dropped earlier."
        y "Oh well it happeneds. So tell me, how is the clu-....{b}*Splesh*{/b}"
        y "...."
        y "Another Number 4?"
        kim "Number 3 I think..."
        y "Kim, why is the bar such a mess?"
        kim "Cause I keep dropping orders."
        y "And why do you keep dropping orders....?"
        $ kimFace = 1
        kim "Cause of all the saving the world I have to do!"
        y ".........................."
        $ kimFace = 5
        kim "Okay fine, I'm just a lousy waitress."
        kim "Being sexy is one thing, but being sexy {i}'and'{i} remembering people's orders? That's madness!"
        y "You're a super spy. I didn't think waiting tables would give you trouble."
        $ kimFace = 6
        kim "Hey! I can do anything!"
        y "But can you do anything well?"
        $ kimFace = 4
        kim "That...! Er..."
        kim "....................."
        kim "Well maybe not..."
        y "Though so. If you can do anything, then get busy cleaning up this mess."
        $ kimFace = 5
        kim "Yes boss...."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 5:
        $ socialKim = 6
        show scene_darkening with d3
        $ kimFace = 6
        show kim at ri with d3
        y "So Kim, I've been meaning to ask you. What's your cover story?"
        kim "Cover story?"
        y "Yeah, what did you tell your parents and your school what you were doing."
        $ kimFace = 5
        kim "Er... liberating Beverly Hills and fighting WOOHP."
        y "................"
        y "You told them that...? What about your secret identity?"
        $ kimFace = 1
        kim "I don't have a secret identity. Everyone knows that I'm a super spy."
        y "If everyone knows you're a spy... then you're not much of a spy."
        kim "Super Agent then."
        y "............................."
        $ kimFace = 5
        kim "Super Hero?"
        y "All right wonder woman, whatever you say."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 6:
        $ socialKim = 7
        show scene_darkening with d3
        $ kimFace = 1
        show kim at ri with d3
        kim "Boss I need your help. Could you drive me over to the mall? They've got a Club Banana store there that's having a sale."
        y "A club banana...? That sounds like an icecream parlor."
        $ kimFace = 4
        kim "It's a clothing shop! I can't believe you haven't heard of it!"
        y "You're starting to sound more like the spies every day...{w} Anyways, I'm busy. Drive yourself."
        $ kimFace = 6
        kim "..........................."
        y "What?"
        $ kimFace = 5
        kim "I... I don't have a driver's license."
        y "You don't have a driver's license?{w} What superspy doesn't have her license? How do you get to missions?!"
        kim "I walk."
        y "....."
        kim "Okay fine. I usually call in a favor and carpool."
        y "You carpool..."
        y "I thought you were a super hero? Where's the Possible Mobile or the Kim Jet?"
        $ kimFace = 1
        kim "I wouldn't be able to drive those without a license, now would I? C'mon boss, give me a ride~...."
        y "Say please~..."
        kim "Pleeeeease~.... I'll show you my tiiiiits~...."
        y "How can I say no to that face...{w} and those tits...."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 7:
        $ socialKim = 8
        show scene_darkening with d3
        $ kimFace = 1
        show kim at ri with d3
        y "Kim! I found a picture of you from your highschool days!"
        $ kimFace = 4
        kim "Oh no..."
        y "You were a cheerleader? Nice."
        kim "I changed a lot since then. I grew up... stopped being the naive little girl I was then... learned what the universe was all about..."
        y "You discovered boys, didn't you?"
        kim "Boss!"
        y "Trust me. Looking at these pictures, boys discovered you far before you discovered them~...."
        hide kim with d1
        $ kimEffects = 1
        show kim at ri with d1
        $ kimFace = 5
        kim "Can you stop perving over my highschool photos now...?"
        y "Oh relax. You were way too... triangley for me anyways. What did you do? Stuff your bra or something?"
        $ kimFace = 4
        kim "I was young and dumb, okay?! "
        hide kim at ri with d3
        $ kimEffects = 0
        hide scene_darkening with d3
        jump club
    if socialKim == 8:
        $ socialKim = 9
        $ kimFace = 5
        show scene_darkening with d3
        show kim at ri with d3
        kim "....................."
        kim "I'm horny."
        y "I'm not paying you to be horny. I'm paying you to {i}'pretend'{/i} to be horny to bring in more tips."
        kim "This is a problem... I've never been horny on a mission before..."
        y "I guess some of the customers are pretty good loo-..."
        $ kimFace = 6
        kim "It's not the customers. It's the staff."
        y "........................."
        y "THERE YOU ARE!"
        $ kimFace = 4
        kim "Huh...?"
        y "I've been wondering when a lesbian would show up! We got so many hot spy girls, I was beginning to worry we wouldn't get some hot girl-on-girl action!"
        kim "Boss... I'm not a lesb-..."
        y "Sure I see some of the staff girls make out from time to time for tips, but they're just faking it for money."
        $ kimFace = 6
        kim "I'm no-..."
        y "So? Which one is your favorite? I like all three of the spies, but if you had to choose. Who'd you sleep with?"
        kim "Boss, I'm not a lesbian..."
        y "You're not? But I thought-...?"
        $ kimFace = 1
        kim "Girls can be sexually attracted to each other without being gay."
        y "................."
        kim "Why do you think {i}'lesbian'{/i} is the most search term for porn by women?"
        y "I'm confused. Are you gay or not?"
        $ kimFace = 6
        kim "No, I'm not."
        y "But you have sexual fantasies about the staff."
        $ kimFace = 5
        kim "Yes, I do."
        y "......................"
        $ kimFace = 4
        kim "Look, it's complicated okay?!"
        y "You're telling me..."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 9:
        $ socialKim = 10
        $ kimFace = 4
        show scene_darkening with d3
        show kim at ri with d3
        y "Hey Kim. Still horny?"
        kim "YES!"
        kim "I figured it would just go away, but it hasn't!"
        kim "I mean look at them! Hot girls in tiny uniforms...!"
        y "Yeah you're right. Those uniforms are way too provacitive."
        y "All right, everybody listen up!"
        y "Take off your clothes, you'll be working nude today."
        kim "Wait...!"
        "The girls in the bar look at each other, shrug and begin undressing."
        kim "Wait...!"
        "Waitress" "Oh no! My breasts are so big. I need someone to help me undress~...."
        kim "This isn't helping....!"
        "Waitress" "Oh I'm so embarrassed~.... quickly someone cover my naked breasts with their hands~.... ♥"
        kim "{b}*Pant* *Pant*{/b}"
        "Waitress" "Oops, I spilled a milkshake on my hot....{w} naked...{w} voluptuous breasts~.... I need someone to lick me clean~...!"
        $ kimFace = 7
        kim "Ngh~...."
        y "Wow... what's with these girls? I feel like I'm in a bad porno movi-...."
        kim "Boss!"
        kim "You and me.{w} NOW!"
        y "I thought you were into girl-..."
        $ kimFace = 2
        kim "NOW!"
        "Kim drags you away from the crowd and begins unbuckling her shorts. Bending over to pull them down over her soft smooth buttcheeks."
        kim "I want you to use this...!"
        "Kim hands you a leah and collar."
        y "...................."
        y "You're a fucking slut."
        $ kimFace = 3
        kim "Yes I am~....."
        scene black with fade
        kim "Oh! Oh! Oh! Yes!"
        kim "H-harder...! Pull harder~.... ♥♥♥"
        kim "Call me a slut! Fuck me like one!"
        kim "Aaaaaahhh!!! ♥♥♥♥♥♥"
        y "This is going into the photobook. Say cheese~...."
        show white
        play sound "audio/sfx/camera.mp3"
        hide white with d2
        show expression "gui/photos/other/picKim.jpg":
            xalign 0.5 yalign 0.5
        pause
        hide expression "gui/photos/other/picKim.jpg"
        with d3
        "A new photo has been added to your photoalbum."
        $ kimOutfit = 0
        scene bgBar with fade
        show scene_darkening with d3
        $ kimFace = 1
        show kim at ri with d3
        kim "{b}*Pant* *Pant*{/b}"
        y "You still horny?"
        kim "I think that fixed it..."
        y "All right. Staff! Get your clothing back on!"
        "You hear the disappointed cries of the customers as the girls begin getting dressed again."
        hide kim with d2
        $ kimOutfit = 1
        show kim at ri with d2
        kim "Thanks boss."
        y "Anytime."
        hide kim at ri with d3
        hide scene_darkening with d3
        jump club
    if socialKim == 10:
        $ kimFace = 1
        y "Hey Kim."
        menu:
            "Show me your boobs" if True:
                kim "You got it boss."
                hide kim with d2
                $ kimArms = 2
                $ kimOutfit = 2
                show kim at ri with d2
                pause
                $ randBoob = renpy.random.randint(1,3)
                if randBoob == 1:
                    "{b}*Pinch*{/b}"
                    kim "Don't have too much fun there boss~... Else you gotta pay."
                    y "............."
                    hide kim
                    hide scene_darkening
                    $ kimArms = 1
                    $ kimOutfit = 1
                    with d3
                    jump club
                if randBoob == 2:
                    y "Boobies~...."
                    kim "Boss... you're drooling."
                    y "Shh, don't ruin this for me."
                    hide kim
                    hide scene_darkening
                    $ kimArms = 1
                    $ kimOutfit = 1
                    with d3
                    jump club
                if randBoob == 3:
                    kim "Want a grope? Two bucks."
                    y "Kim... I'm your boss. Lemme grope."
                    kim "That's some serious abuse of power there."
                    y ".................."
                    hide kim
                    hide scene_darkening
                    $ kimArms = 1
                    $ kimOutfit = 1
                    with d3
                    jump club
                pause
            "Never mind" if True:
                jump club
        jump club
    jump club
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
