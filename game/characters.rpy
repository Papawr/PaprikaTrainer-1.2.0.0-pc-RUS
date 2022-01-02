




define greenName = _("Sam")
define greenLocation = "Library"


define redName = "Clover"
define redLocation = "Showers"


define yellowName = "Alex"
define yellowLocation = "Cafetaria"


define kimName = "Kim"


define playerName = _("New Guy")



transform le:
    xalign 0.0 yalign 0.0 xzoom -1
transform ce:
    xalign 0.5 yalign 0.0
transform ri:
    xalign 1.0 yalign 0.0



define y = Character(_("You"), color="#fff", what_color="#fff", image="player", window_style="windowBlue", what_style="say_dialogueRight", who_style="say_labelRight")
define yInmate = Character(_("You"), color="#fff", what_color="#fff", image="playerInmate", window_style="windowBlue", what_style="say_dialogueRight", who_style="say_labelRight")
define s = Character(_("[greenName]"), color="#fff", what_color="#fff", image="green", window_style="windowGreen", namebox_style="nameboxGreen", what_style="say_dialogueRight", who_style="say_labelRight")
define sM = Character(_("Sam[#dsM]"), color="#fff", what_color="#fff", image="miniGreen", window_style="windowGreen", namebox_style="nameboxGreen", what_style="say_dialogueRight", who_style="say_labelRight")
define cM = Character(_("Clover[#dsM]"), color="#fff", what_color="#fff", image="miniRed", window_style="windowRed", namebox_style="nameboxRed", what_style="say_dialogueRight", who_style="say_labelRight")
define aM = Character(_("Alex[#dsM]"), color="#fff", what_color="#fff", image="miniYellow", window_style="windowYellow", namebox_style="nameboxYellow", what_style="say_dialogueRight", who_style="say_labelRight")
define c = Character(_("[redName]"), color="#fff", what_color="#fff", image="red", window_style="windowRed", namebox_style="nameboxRed", what_style="say_dialogueRight", who_style="say_labelRight")
define a = Character(_("[yellowName]"), image="yellow", window_style="windowYellow", namebox_style="nameboxYellow", what_style="say_dialogueRight", who_style="say_labelRight")
define kim = Character(_("[kimName]"), color="#fff", what_color="#fff", window_style="windowOrange", namebox_style="nameboxOrange", what_style="say_dialogueRight", who_style="say_labelRight")
define brit = Character(_("Britney"), color="#fff", what_color="#fff", image="britney", window_style="windowCyan", namebox_style="nameboxCyan", what_style="say_dialogueRight", who_style="say_labelRight")
define bw = Character(_(" "), color="#fff", what_color="#fff", namebox_style="nameboxBW",  window_style="windowBW")


define O5O = Character(_("Agent O5O"), color="#fff", what_color="#fff",  namebox_style="nameboxBlue")
define GLA = Character(_("G.L.A.D.I.S."), color="#fff", what_color="#fff",  namebox_style="nameboxBlue")
define mat = Character(_("Mathias"), color="#fff", what_color="#fff",  namebox_style="nameboxBlue")
define jerry = Character(_("Jerry"), color="#fff", what_color="#fff",  namebox_style="nameboxBlue")


define sil = Character(_("Silva"), color="#fff", what_color="#fff",  namebox_style="nameboxBlue")
define santa = Character(_("{color=#e01a1a}S{color=#22b613}l{color=#e01a1a}u{color=#22b613}t {color=#e01a1a}S{color=#22b613}h{color=#e01a1a}a{color=#22b613}m{color=#e01a1a}i{color=#22b613}n{color=#e01a1a}g S{color=#22b613}a{color=#e01a1a}n{color=#22b613}t{color=#e01a1a}a{/color}"),  namebox_style="nameboxWhite")
define tim = Character(_("Tim"), color="#fff", what_color="#fff",  namebox_style="nameboxBlue")
define seb = Character(_("Sebastian"), color="#fff", what_color="#fff",  namebox_style="nameboxBlue")


image side miniMaggie = "gui/portraits/miniMaggie.png"
define mag = Character(_("Maggie T."), color="#fff", what_color="#fff", image="miniMaggie", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniMelody = "gui/portraits/miniMelody.png"
define mel = Character(_("Melody"), color="#fff", what_color="#fff", image="miniMelody", what_style="say_dialogueRight", who_style="say_labelRight")


image side miniDragon = "gui/portraits/miniDragon.png"
define drag = Character(_("Clara Wong"), color="#fff", what_color="#fff", image="miniDragon", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniTalia = "gui/portraits/miniTalia.png"
define tali = Character(_("Talia"), color="#fff", what_color="#fff", image="miniTalia", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniCandy = "gui/portraits/miniDragon.png"
define candy = Character(_("Margaret"), color="#fff", what_color="#fff", what_style="say_dialogueRight", who_style="say_labelRight")


image side miniMuffy = "gui/portraits/miniMuffy.png"
define muff = Character(_("Muffy P."), color="#fff", what_color="#fff", image="miniMuffy", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniFeli = "gui/portraits/miniFeli.png"
define feli = Character(_("Felicity"), color="#fff", what_color="#fff", image="miniFeli", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniKand = "gui/portraits/miniDragon.png"
define kand = Character(_("The Great Kandinsky"), color="#fff", what_color="#fff", what_style="say_dialogueRight", who_style="say_labelRight")


define INTERFACE = Character(what_color = "#f7c64f",  what_font="fonts/BigSquareDots.ttf", what_size=25)
define LOCATION = Character(window_style="windowEmpty", what_style="say_dialogueLOCATION", what_color = "#f7c64f",  what_font="fonts/BigSquareDots.ttf", what_size=25)

image side miniNiece = "gui/portraits/niece.png"
define niece = Character(_("Barber's niece"), color="#fff", what_color="#fff", image="miniNiece", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniShopOwner = "gui/portraits/shopOwner.png"
define shopOwner = Character(_("Shop Owner"), color="#fff", what_color="#fff", image="miniShopOwner", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniModel = "gui/portraits/model.png"
define model = Character(_("Handsome Model"), color="#fff", what_color="#fff", image="miniModel", what_style="say_dialogueRight", who_style="say_labelRight")

image side miniNerd = "gui/portraits/nerd.png"
define nerd = Character(_("Nerd"), image="miniNerd", color="#fff", what_color="#fff", what_style="say_dialogueRight", who_style="say_labelRight")





default playerName = _("New Guy")
default playerKarma = 50
default karmaCash = 0
default playerOutfit = 10
default cooking = 0


image side player = "gui/portraits/miniPlrNeutral.png"
image side player 1 = "gui/portraits/miniPlrNeutral.png"
image side player 2 = "gui/portraits/miniPlrSad.png"
image side player 3 = "gui/portraits/miniPlrHappy.png"

image side playerInmate = "gui/portraits/miniPlrNeutralTut.png"

default greenF = "g1"
label callGreen:
    show green [greenF]:
        xalign 1.0 yalign 0.0
    with d3
    pause
    return
label callRed:
    show red:
        xalign 1.0 yalign 0.0
    with d3
    return


default slutPublic = 0
default slutLevel = 0






image side miniGreen = "gui/portraits/miniGreenSerious.png"


default greenArms = 1
default greenFace = 1
default greenPubic = 0
default greenHair = 1
default greenBlush = 0
default greenCum = 0
default greenHood = False

default greenUnder = 1
default greenHat = 0
default greenGlasses = 0
default greenAcces1 = 0
default greenPierc1 = 0
default greenNeck = 0
default greenChest = 0
default greenPierc2 = 0
default greenAcces2 = 0
default greenBottom = 0
default greenAcces3 = 0
default greenShoes = 0
default greenOutfit = 1
default greenOutfitArms = 1


default greenTatHead = 0
default greenTatChest = 0
default greenTatArm = 0
default greenTatBelly = 0
default greenTatPuss = 0

default greenTatFoot = 0


default samNick = _("Cucumber {#dsn}")
default samHealth = 3
default samMood = 100
default samSocial = 0
default samSlut = 0
default samDailyChat = 0
default nanoLevelSam = 10
default samSupLvl = 0
default samFriend = _("Acquaintance {#dsf}")
default samHPTimer = 0
default samTitSize = 1


default samMiniQ1 = 0


default outfitSamUniformActive = False


default greenHatSet = 0
default greenAcc1Set = 0
default greenNeckSet = 0
default greenChestSet = 0
default greenAcc2Set = 0
default greenBottomSet = 0
default greenAcc3Set = 0
default greenShoesSet = 0
default greenUnderSet = 0
default greenOutfitSet = 0


default greenTatHeadSet = 0
default greenTatChestSet = 0
default greenTatArmSet = 0
default greenTatBellySet = 0
default greenTatPussSet = 0
default greenTatFootSet = 0


default greenPubicSet = 0


default greenHairSet = 1

layeredimage greenBondage:
    always:
        "models/green/bondage.png"
    if greenCum == 1:
        "models/green/eff/cum1.png"
    if greenCum >= 2:
        "models/green/eff/cum2.png"

layeredimage redBondage:
    always:
        "models/red/bondage.png"
    if redCum == 1:
        "models/red/eff/cum1.png"
    if redCum == 2:
        "models/red/eff/cum2.png"
    if redCum == 3:
        "models/red/eff/cum3.png"

layeredimage yellowBondage:
    always:
        "models/yellow/bondage.png"
    if redCum == 1:
        "models/yellow/eff/cum1.png"
    if redCum == 2:
        "models/yellow/eff/cum2.png"
    if redCum == 3:
        "models/yellow/eff/cum3.png"

layeredimage green:
    xalign 1.25 yalign 0.1
    if greenUnder == 0 and greenChest == 0 or greenUnder == 0 and greenOutfit == 0 and greenChest == 0:
        "models/green/greenBody1.png"
    else:
        "models/green/greenBody2.png"


    if greenAcces2 == 14:
        "models/green/outfit/acc2/acc14.png"



    if greenPubic == 1:
        "models/green/pubic/pub1.png"
    if greenPubic == 2:
        "models/green/pubic/pub2.png"
    if greenPubic == 3:
        "models/green/pubic/pub3.png"
    if greenPubic == 4:
        "models/green/pubic/pub4.png"
    if greenPubic == 5:
        "models/green/pubic/pub5.png"
    if greenPubic == 6:
        "models/green/pubic/pub6.png"
    if greenPubic == 7:
        "models/green/pubic/pub7.png"



    if greenTatPuss == 1:
        "models/green/tat/puss1.png"
    if greenTatPuss == 2:
        "models/green/tat/puss2.png"
    if greenTatPuss == 3:
        "models/green/tat/puss3.png"
    if greenTatPuss == 4:
        "models/green/tat/puss4.png"
    if greenTatPuss == 5:
        "models/green/tat/puss5.png"
    if greenTatPuss == 6:
        "models/green/tat/puss6.png"



    if greenArms == 1 and greenUnder != 0 or greenArms == 1 and greenChest != 0 or greenArms == 1 and greenOutfit != 0:
        "models/green/greenArms1a.png"
    elif greenArms == 1 and greenUnder == 0 or greenArms == 1 and greenChest == 0 or greenArms == 1 and greenOutfit == 0:
        "models/green/greenArms1b.png"
    elif greenArms == 2:
        "models/green/greenArms2.png"
    elif greenArms == 3:
        "models/green/greenArms3.png"
    elif greenArms == 4:
        "models/green/greenArms4.png"
    elif greenArms == 5:
        "models/green/greenArms5.png"
    elif greenArms == 6:
        "models/green/greenArms6.png"



    if greenTatHead == 1:
        "models/green/tat/face1.png"
    if greenTatHead == 2:
        "models/green/tat/face2.png"
    if greenTatHead == 3:
        "models/green/tat/face3.png"
    if greenTatHead == 4:
        "models/green/tat/face4.png"
    if greenTatHead == 5:
        "models/green/tat/face5.png"
    if greenTatHead == 6:
        "models/green/tat/face6.png"

    if greenTatChest == 1:
        "models/green/tat/breast1.png"
    if greenTatChest == 2:
        "models/green/tat/breast2.png"
    if greenTatChest == 3:
        "models/green/tat/breast3.png"
    if greenTatChest == 4:
        "models/green/tat/breast4.png"
    if greenTatChest == 5:
        "models/green/tat/breast5.png"
    if greenTatChest == 6:
        "models/green/tat/breast6.png"

    if greenTatArm == 1 and greenArms == 1:
        "models/green/tat/arm1.png"
    if greenTatArm == 2 and greenArms == 1:
        "models/green/tat/arm2.png"
    if greenTatArm == 3 and greenArms == 1:
        "models/green/tat/arm3.png"
    if greenTatArm == 4 and greenArms == 1:
        "models/green/tat/arm4.png"
    if greenTatArm == 5 and greenArms == 1:
        "models/green/tat/arm5.png"
    if greenTatArm == 6 and greenArms == 1:
        "models/green/tat/arm6.png"

    if greenTatBelly == 1:
        "models/green/tat/belly1.png"
    if greenTatBelly == 2:
        "models/green/tat/belly2.png"
    if greenTatBelly == 3:
        "models/green/tat/belly3.png"
    if greenTatBelly == 4:
        "models/green/tat/belly4.png"
    if greenTatBelly == 5:
        "models/green/tat/belly5.png"
    if greenTatBelly == 6:
        "models/green/tat/belly6.png"

    if greenTatFoot == 1:
        "models/green/tat/lowLeg1.png"
    if greenTatFoot == 2:
        "models/green/tat/lowLeg2.png"
    if greenTatFoot == 3:
        "models/green/tat/lowLeg3.png"
    if greenTatFoot == 4:
        "models/green/tat/lowLeg4.png"
    if greenTatFoot == 5:
        "models/green/tat/lowLeg5.png"
    if greenTatFoot == 6:
        "models/green/tat/lowLeg6.png"


    if samTitSize == 2 and greenChest == 0 and greenUnder == 0 and greenOutfit == 0 and greenArms == 1:
        "models/green/tits/titsMedium.png"
    if samTitSize == 3 and greenChest == 0 and greenUnder == 0 and greenOutfit == 0 and greenArms == 1:
        "models/green/tits/titsLarge.png"



    if greenUnder == 1:
        "models/green/outfit/under/under1.png"
    if greenUnder == 1.1:
        "models/green/outfit/under/under1a.png"
    if greenUnder == 2:
        "models/green/outfit/under/under2.png"
    if greenUnder == 3:
        "models/green/outfit/under/under3a.png"
    if greenUnder == 3.1:
        "models/green/outfit/under/under3.png"
    if greenUnder == 4:
        "models/green/outfit/under/under4.png"
    if greenUnder == 5:
        "models/green/outfit/under/under5.png"
    if greenUnder == 6:
        "models/green/outfit/under/under6.png"
    if greenUnder == 7:
        "models/green/outfit/under/under7.png"
    if greenUnder == 8:
        "models/green/outfit/under/under8.png"
    if greenUnder == 9:
        "models/green/outfit/under/under9.png"
    if greenUnder == 9.1:
        "models/green/outfit/under/under9a.png"
    if greenUnder == 10:
        "models/green/outfit/under/under10.png"
    if greenUnder == 11:
        "models/green/outfit/under/under11.png"


    if greenOutfit == 1:
        "models/green/outfit/greenSuit1.png"
    if greenOutfit == 2:
        "models/green/outfit/greenSuit2.png"
    if greenOutfit == 3:
        "models/green/outfit/greenSuit3.png"
    if greenOutfitArms == 1:
        "models/green/outfit/greenSuitArms1.png"
    if greenOutfitArms == 2:
        "models/green/outfit/greenSuitArms2.png"
    if greenOutfitArms == 3:
        "models/green/outfit/greenSuitArms3.png"
    if greenOutfitArms == 4:
        "models/green/outfit/greenSuitArms4.png"

    if greenOutfit == 4:
        "models/green/outfit/greenSuit4.png"


    group faces:
        attribute gDef default:
            "models/green/face/serious4.png"
        attribute g1:
            "models/green/face/greenHappy1.png"
        attribute g2:
            "models/green/face/happy2.png"
        attribute g3:
            "models/green/face/happy3.png"
        attribute g4:
            "models/green/face/sad1.png"
        attribute g5:
            "models/green/face/sad2.png"
        attribute g6:
            "models/green/face/sad3.png"
        attribute g7:
            "models/green/face/angry1.png"
        attribute g8:
            "models/green/face/angry2.png"
        attribute g9:
            "models/green/face/angry3.png"
        attribute g10:
            "models/green/face/annoyed1.png"
        attribute g11:
            "models/green/face/annoyed2.png"
        attribute g12:
            "models/green/face/annoyed3.png"
        attribute g13:
            "models/green/face/closed1.png"
        attribute g14:
            "models/green/face/closed2.png"
        attribute g15:
            "models/green/face/closed3.png"
        attribute g16:
            "models/green/face/confused1.png"
        attribute g17:
            "models/green/face/confused2.png"
        attribute g18:
            "models/green/face/confused3.png"
        attribute g19:
            "models/green/face/shy1.png"
        attribute g20:
            "models/green/face/shy2.png"
        attribute g21:
            "models/green/face/shy3.png"
        attribute g22:
            "models/green/face/naughty1.png"
        attribute g23:
            "models/green/face/naughty2.png"
        attribute g24:
            "models/green/face/naughty3.png"
        attribute g25:
            "models/green/face/pleasure1.png"
        attribute g26:
            "models/green/face/pleasure2.png"
        attribute g27:
            "models/green/face/pleasure3.png"
        attribute g28:
            "models/green/face/shock1.png"
        attribute g29:
            "models/green/face/shock2.png"
        attribute g30:
            "models/green/face/shock3.png"
        attribute g31:
            "models/green/face/serious1.png"
        attribute g32:
            "models/green/face/serious2.png"
        attribute g33:
            "models/green/face/serious3.png"
        attribute g34:
            "models/green/face/serious4.png"
        attribute g35:
            "models/green/face/reluctant1.png"
        attribute g36:
            "models/green/face/reluctant2.png"
        attribute g37:
            "models/green/face/reluctant3.png"
        attribute g38:
            "models/green/face/closed4.png"
        attribute g39:
            "models/green/face/closed5.png"
        attribute g40:
            "models/green/face/angry4.png"
        attribute g41:
            "models/green/face/confused4.png"
        attribute g42:
            "models/green/face/closed6.png"
        attribute g43:
            "models/green/face/down1.png"
        attribute g44:
            "models/green/face/down2.png"
        attribute g45:
            "models/green/face/down3.png"
        attribute g46:
            "models/green/face/down4.png"
        attribute g47:
            "models/green/face/down5.png"
        attribute g48:
            "models/green/face/down6.png"
        attribute g49:
            "models/green/face/down7.png"
        attribute g50:
            "models/green/face/down8.png"
        attribute g51:
            "models/green/face/down9.png"
        attribute g52:
            "models/green/face/side1.png"
        attribute g53:
            "models/green/face/side2.png"
        attribute g54:
            "models/green/face/side3.png"
        attribute g55:
            "models/green/face/side4.png"
        attribute g56:
            "models/green/face/side5.png"
        attribute g57:
            "models/green/face/side6.png"

        attribute g100:
            "models/green/face/redAngry1.png"


    if greenBlush == 1:
        "models/green/eff/blush.png"

    if greenCum == 1:
        "models/green/eff/cum1.png"
    if greenCum == 2:
        "models/green/eff/cum2.png"
    if greenCum == 3:
        "models/green/eff/cum3.png"

    if spyGreenActive == False and wardrobeCurrentSpy == 1 and tutorialActive == False:
        "models/green/lockedSam.png"
    if spyGreenActive == False and shopCurrentSpy == 1 and tutorialActive == False:
        "models/green/lockedSam.png"
    if spyGreenActive == False and shopCurrentSpy == 1 and tutorialActive == False:
        "models/green/lockedSam.png"








    if greenAcces1 == 4:
        "models/green/outfit/acc1/acc4.png"
    if greenAcces1 == 11:
        "models/green/outfit/acc1/acc11.png"
    if greenAcces1 == 14:
        "models/green/outfit/acc1/acc14.png"
    if greenAcces1 == 15:
        "models/green/outfit/acc1/acc15.png"





    if greenNeck == 1:
        "models/green/outfit/neck/neck1.png"
    if greenNeck == 2:
        "models/green/outfit/neck/neck2.png"
    if greenNeck == 3:
        "models/green/outfit/neck/neck3.png"
    if greenNeck == 7:
        "models/green/outfit/neck/neck7.png"
    if greenNeck == 10:
        "models/green/outfit/neck/neck10.png"
    if greenNeck == 14:
        "models/green/outfit/neck/neck14.png"


    if greenShoes == 2:
        "models/green/outfit/shoes/shoes2.png"
    if greenShoes == 5:
        "models/green/outfit/shoes/shoes5.png"
    if greenShoes == 6:
        "models/green/outfit/shoes/shoes6.png"
    if greenShoes == 7:
        "models/green/outfit/shoes/shoes7.png"
    if greenShoes == 7.1:
        "models/green/outfit/shoes/shoes7a.png"
    if greenShoes == 7.3:
        "models/green/outfit/shoes/var/shoes7Var1.png"
    if greenShoes == 7.4:
        "models/green/outfit/shoes/var/shoes7Var2.png"
    if greenShoes == 7.5:
        "models/green/outfit/shoes/var/shoes7Var3.png"
    if greenShoes == 7.6:
        "models/green/outfit/shoes/var/shoes7Var4.png"
    if greenShoes == 8:
        "models/green/outfit/shoes/shoes8.png"
    if greenShoes == 10:
        "models/green/outfit/shoes/shoes10.png"
    if greenShoes == 11:
        "models/green/outfit/shoes/shoes11.png"
    if greenShoes == 12:
        "models/green/outfit/shoes/shoes12.png"
    if greenShoes == 12.1:
        "models/green/outfit/shoes/shoes12a.png"
    if greenShoes == 14:
        "models/green/outfit/shoes/shoes14.png"
    if greenShoes == 15:
        "models/green/outfit/shoes/shoes15a.png"
    if greenShoes == 15.1:
        "models/green/outfit/shoes/shoes15b.png"


    if greenBottom == 1:
        "models/green/outfit/bott/bott1.png"
    if greenBottom == 2:
        "models/green/outfit/bott/bott2.png"
    if greenBottom == 2.1:
        "models/green/outfit/bott/bott2a.png"
    if greenBottom == 3:
        "models/green/outfit/bott/bott3.png"
    if greenBottom == 4:
        "models/green/outfit/bott/bott4.png"
    if greenBottom == 5:
        "models/green/outfit/bott/bott5.png"
    if greenBottom == 6:
        "models/green/outfit/bott/bott6.png"
    if greenBottom == 7:
        "models/green/outfit/bott/bott7.png"
    if greenBottom == 7.1:
        "models/green/outfit/bott/bott7a.png"
    if greenBottom == 7.3:
        "models/green/outfit/bott/var/bott7Var1.png"
    if greenBottom == 7.4:
        "models/green/outfit/bott/var/bott7Var2.png"
    if greenBottom == 7.5:
        "models/green/outfit/bott/var/bott7Var3.png"
    if greenBottom == 7.6:
        "models/green/outfit/bott/var/bott7Var4.png"
    if greenBottom == 8:
        "models/green/outfit/bott/bott8.png"
    if greenBottom == 9:
        "models/green/outfit/bott/bott9.png"
    if greenBottom == 9.3:
        "models/green/outfit/bott/var/bott9Var1.png"
    if greenBottom == 9.4:
        "models/green/outfit/bott/var/bott9Var2.png"
    if greenBottom == 9.5:
        "models/green/outfit/bott/var/bott9Var3.png"
    if greenBottom == 9.6:
        "models/green/outfit/bott/var/bott9Var4.png"
    if greenBottom == 10:
        "models/green/outfit/bott/bott10.png"
    if greenBottom == 12:
        "models/green/outfit/bott/bott12.png"
    if greenBottom == 14:
        "models/green/outfit/bott/bott14.png"
    if greenBottom == 15:
        "models/green/outfit/bott/bott15.png"


    if greenShoes == 1:
        "models/green/outfit/shoes/shoes1.png"
    if greenShoes == 9:
        "models/green/outfit/shoes/shoes9.png"


    if greenAcces2 == 11:
        "models/green/outfit/acc2/acc11.png"


    if greenChest == 1:
        "models/green/outfit/chest/top1.png"
    if greenChest == 1.3:
        "models/green/outfit/chest/var/top1Var1.png"
    if greenChest == 1.4:
        "models/green/outfit/chest/var/top1Var2.png"
    if greenChest == 1.5:
        "models/green/outfit/chest/var/top1Var3.png"
    if greenChest == 1.6:
        "models/green/outfit/chest/var/top1Var4.png"
    if greenChest == 2:
        "models/green/outfit/chest/top2.png"
    if greenChest == 2.1:
        "models/green/outfit/chest/top2a.png"
    if greenChest == 2.2:
        "models/green/outfit/chest/top2b.png"
    if greenChest == 2.3:
        "models/green/outfit/chest/top2c.png"
    if greenChest == 3:
        "models/green/outfit/chest/top3.png"
    if greenChest == 3.1:
        "models/green/outfit/chest/top3a.png"
    if greenChest == 3.3:
        "models/green/outfit/chest/var/top3Var1.png"
    if greenChest == 3.4:
        "models/green/outfit/chest/var/top3Var2.png"
    if greenChest == 3.5:
        "models/green/outfit/chest/var/top3Var3.png"
    if greenChest == 3.6:
        "models/green/outfit/chest/var/top3Var4.png"
    if greenChest == 4:
        "models/green/outfit/chest/top4.png"
    if greenChest == 4.1:
        "models/green/outfit/chest/top4a.png"
    if greenChest == 4.3:
        "models/green/outfit/chest/var/top4Var1.png"
    if greenChest == 4.4:
        "models/green/outfit/chest/var/top4Var2.png"
    if greenChest == 4.5:
        "models/green/outfit/chest/var/top4Var3.png"
    if greenChest == 4.6:
        "models/green/outfit/chest/var/top4Var4.png"
    if greenChest == 5:
        "models/green/outfit/chest/top5.png"
    if greenChest == 6:
        "models/green/outfit/chest/top6.png"
    if greenChest == 7:
        "models/green/outfit/chest/top7.png"
    if greenChest == 7.1:
        "models/green/outfit/chest/top7a.png"
    if greenChest == 7.3:
        "models/green/outfit/chest/var/top7Var1.png"
    if greenChest == 7.4:
        "models/green/outfit/chest/var/top7Var2.png"
    if greenChest == 7.5:
        "models/green/outfit/chest/var/top7Var3.png"
    if greenChest == 7.6:
        "models/green/outfit/chest/var/top7Var4.png"
    if greenChest == 8:
        "models/green/outfit/chest/top8.png"
    if greenChest == 9:
        "models/green/outfit/chest/top9.png"
    if greenChest == 9.3:
        "models/green/outfit/chest/var/top9Var1.png"
    if greenChest == 9.4:
        "models/green/outfit/chest/var/top9Var2.png"
    if greenChest == 9.5:
        "models/green/outfit/chest/var/top9Var3.png"
    if greenChest == 9.6:
        "models/green/outfit/chest/var/top9Var4.png"
    if greenChest == 9.3:
        "models/green/outfit/chest/var/top9Var1.png"
    if greenChest == 11:
        "models/green/outfit/chest/top11.png"
    if greenChest == 12:
        "models/green/outfit/chest/top12.png"
    if greenChest == 12.1:
        "models/green/outfit/chest/top12a.png"
    if greenChest == 12.3:
        "models/green/outfit/chest/var/top12Var1.png"
    if greenChest == 12.4:
        "models/green/outfit/chest/var/top12Var2.png"
    if greenChest == 12.5:
        "models/green/outfit/chest/var/top12Var3.png"
    if greenChest == 12.6:
        "models/green/outfit/chest/var/top12Var4.png"
    if greenChest == 14:
        "models/green/outfit/chest/top14.png"
    if greenChest == 15.1:
        "models/green/outfit/chest/top15a.png"
    if greenChest == 15.2:
        "models/green/outfit/chest/top15b.png"
    if greenChest == 15.3:
        "models/green/outfit/chest/top15c.png"
    if greenChest == 15.4:
        "models/green/outfit/chest/top15d.png"
    if greenChest == 99:
        "models/green/outfit/chest/wetT.png"


    if greenHat == 9 or greenHat == 11 or greenHat == 12:
        "models/green/hair/noHair.png"
    elif greenHair == 1 and greenChest == 12:
        "models/green/hair/greenHair1Back.png"
    elif greenHair == 1 and greenArms == 1:
        "models/green/hair/greenHair1.png"
    elif greenHair == 1 and greenArms != 1:
        "models/green/hair/greenHair1Back.png"
    elif greenHair == 2:
        "models/green/hair/greenHair2.png"
    elif greenHair == 3:
        "models/green/hair/greenHair3.png"
    elif greenHair == 4:
        "models/green/hair/greenHair4.png"
    elif greenHair == 5:
        "models/green/hair/greenHair5.png"
    elif greenHair == 6:
        "models/green/hair/greenHair6.png"
    elif greenHair == 8:
        "models/green/hair/greenHair8.png"




    if greenHat == 1:
        "models/green/outfit/hat/hat1.png"
    if greenHat == 2:
        "models/green/outfit/hat/hat2.png"
    if greenHat == 6:
        "models/green/outfit/hat/hat6.png"
    if greenHat == 9:
        "models/green/outfit/hat/hat9.png"
    if greenHat == 10:
        "models/green/outfit/hat/hat10.png"
    if greenHat == 11:
        "models/green/outfit/hat/hat11.png"
    if greenHat == 12:
        "models/green/outfit/hat/hat12.png"




    if greenChest == 10:
        "models/green/outfit/chest/top10a.png"
    if greenChest == 10.1:
        "models/green/outfit/chest/top10b.png"
    if greenChest == 10.3:
        "models/green/outfit/chest/var/top10Var1.png"
    if greenChest == 10.4:
        "models/green/outfit/chest/var/top10Var2.png"
    if greenChest == 10.5:
        "models/green/outfit/chest/var/top10Var3.png"
    if greenChest == 10.6:
        "models/green/outfit/chest/var/top10Var4.png"




image side green 1:
    xalign 1.0 yalign 1.0
    "gui/portraits/miniGreenHappy.png"
image side green 2:
    xalign 1.0 yalign 1.0
    "gui/portraits/miniGreenSad.png"



default greenEyesScreen = 1
screen eyesChange:
    if greenEyesScreen == 1:
        add "models/green/face/greenHappy1.png" xalign 1.25 yalign 0.1
    if greenEyesScreen == 2:
        add "models/green/face/redHappy1.png" xalign 1.25 yalign 0.1




default cloverNick = _("Girl{#dcn}")
default cloverHealth = 3
default cloverSlut = 0
default cloverMood = 100
default cloverSocial = 0
default cloverDailyChat = 0
default nanoLevelClover = 10
default cloverSupLvl = 0
default cloverFriend = _("Acquaintance{#dcf}")
default cloverHPTimer = 0
default cloverTitSize = 1


default outfitCloverUniformActive = False

default redArms = 1
default redFace = 1
default redPubic = 0
default redHair = 1
default redBlush = 0
default redCum = 0
default redHood = False

default redUnder = 1
default redHat = 0
default redGlasses = 0
default redAcces1 = 0
default redPierc1 = 0
default redNeck = 0
default redChest = 0
default redPierc2 = 0
default redAcces2 = 0
default redBottom = 0
default redAcces3 = 0
default redShoes = 0
default redOutfit = 1
default redOutfitArms = 1


default redTatHead = 0
default redTatChest = 0
default redTatArm = 0
default redTatBelly = 0
default redTatPuss = 0

default redTatFoot = 0


default redPubicSet = 0


default redHairSet = 1


default redHatSet = 0
default redAcc1Set = 0
default redNeckSet = 0
default redChestSet = 0
default redAcc2Set = 0
default redBottomSet = 0
default redAcc3Set = 0
default redShoesSet = 0
default redUnderSet = 0
default redOutfitSet = 0


default redTatHeadSet = 0
default redTatChestSet = 0
default redTatArmSet = 0
default redTatBellySet = 0
default redTatPussSet = 0
default redTatFootSet = 0



image side miniRed = "gui/portraits/miniRedSerious.png"


layeredimage red:
    xalign 1.25 yalign 0.1
    if  redUnder == 0 and redOutfit == 0 and redChest == 0:
        "models/red/redBody1.png"
    else:
        "models/red/redBody2.png"



    if redAcces2 == 14:
        "models/red/outfit/acc2/acc14.png"


    if redHat == 11 or redHat == 5 or redHat == 7:
        "models/red/hair/noHair.png"
    elif redHair == 1:
        "models/red/hair/hair1.png"
    elif redHair == 2:
        "models/red/hair/hair2.png"
    elif redHair == 3:
        "models/red/hair/hair3.png"
    elif redHair == 4:
        "models/red/hair/hair4.png"
    elif redHair == 5:
        "models/red/hair/hair5.png"
    elif redHair == 6:
        "models/red/hair/hair6.png"




    if redPubic == 1:
        "models/red/pubic/pub1.png"
    if redPubic == 2:
        "models/red/pubic/pub2.png"
    if redPubic == 3:
        "models/red/pubic/pub3.png"
    if redPubic == 4:
        "models/red/pubic/pub4.png"
    if redPubic == 5:
        "models/red/pubic/pub5.png"
    if redPubic == 6:
        "models/red/pubic/pub6.png"
    if redPubic == 7:
        "models/red/pubic/pub7.png"



    if redTatPuss == 1:
        "models/red/tat/puss1.png"
    if redTatPuss == 2:
        "models/red/tat/puss2.png"
    if redTatPuss == 3:
        "models/red/tat/puss3.png"
    if redTatPuss == 4:
        "models/red/tat/puss4.png"
    if redTatPuss == 5:
        "models/red/tat/puss5.png"
    if redTatPuss == 6:
        "models/red/tat/puss6.png"


    if redArms == 1:
        "models/red/arms1.png"
    if redArms == 2:
        "models/red/arms2.png"
    if redArms == 3:
        "models/red/arms3.png"
    if redArms == 4:
        "models/red/arms4.png"
    if redArms == 5:
        "models/red/arms5.png"



    if redTatHead == 1:
        "models/red/tat/face1.png"
    if redTatHead == 2:
        "models/red/tat/face2.png"
    if redTatHead == 3:
        "models/red/tat/face3.png"
    if redTatHead == 4:
        "models/red/tat/face4.png"
    if redTatHead == 5:
        "models/red/tat/face5.png"
    if redTatHead == 6:
        "models/red/tat/face6.png"

    if redTatChest == 1:
        "models/red/tat/breast1.png"
    if redTatChest == 2:
        "models/red/tat/breast2.png"
    if redTatChest == 3:
        "models/red/tat/breast3.png"
    if redTatChest == 4:
        "models/red/tat/breast4.png"
    if redTatChest == 5:
        "models/red/tat/breast5.png"
    if redTatChest == 6:
        "models/red/tat/breast6.png"

    if redTatArm == 1 and redArms == 1:
        "models/red/tat/arm1.png"
    if redTatArm == 2 and redArms == 1:
        "models/red/tat/arm2.png"
    if redTatArm == 3 and redArms == 1:
        "models/red/tat/arm3.png"
    if redTatArm == 4 and redArms == 1:
        "models/red/tat/arm4.png"
    if redTatArm == 5 and redArms == 1:
        "models/red/tat/arm5.png"
    if redTatArm == 6 and redArms == 1:
        "models/red/tat/arm6.png"

    if redTatBelly == 1:
        "models/red/tat/belly1.png"
    if redTatBelly == 2:
        "models/red/tat/belly2.png"
    if redTatBelly == 3:
        "models/red/tat/belly3.png"
    if redTatBelly == 4:
        "models/red/tat/belly4.png"
    if redTatBelly == 5:
        "models/red/tat/belly5.png"
    if redTatBelly == 6:
        "models/red/tat/belly6.png"

    if redTatFoot == 1:
        "models/red/tat/lowLeg1.png"
    if redTatFoot == 2:
        "models/red/tat/lowLeg2.png"
    if redTatFoot == 3:
        "models/red/tat/lowLeg3.png"
    if redTatFoot == 4:
        "models/red/tat/lowLeg4.png"
    if redTatFoot == 5:
        "models/red/tat/lowLeg5.png"
    if redTatFoot == 6:
        "models/red/tat/lowLeg6.png"


    if cloverTitSize == 2 and redChest == 0 and redUnder == 0 and redOutfit == 0 and redArms == 1:
        "models/red/tits/titsMedium.png"
    if cloverTitSize == 3 and redChest == 0 and redUnder == 0 and redOutfit == 0 and redArms == 1:
        "models/red/tits/titsLarge.png"




    if redUnder == 1:
        "models/red/outfit/under/under1.png"
    if redUnder == 2:
        "models/red/outfit/under/under2.png"
    if redUnder == 3:
        "models/red/outfit/under/under3.png"
    if redUnder == 4:
        "models/red/outfit/under/under4.png"
    if redUnder == 5:
        "models/red/outfit/under/under5.png"
    if redUnder == 6:
        "models/red/outfit/under/under6.png"
    if redUnder == 7:
        "models/red/outfit/under/under7.png"
    if redUnder == 7.1:
        "models/red/outfit/under/under7b.png"
    if redUnder == 8 and redChest == 0:
        "models/red/outfit/under/under8.png"
    if redUnder == 8 and redChest >= 1:
        "models/red/outfit/under/under8Card.png"
    if redUnder == 9:
        "models/red/outfit/under/under9.png"
    if redUnder == 9.1:
        "models/red/outfit/under/under9a.png"
    if redUnder == 9.2:
        "models/red/outfit/under/under9b.png"
    if redUnder == 10:
        "models/red/outfit/under/under10.png"
    if redUnder == 11:
        "models/red/outfit/under/under11.png"
    if redUnder == 11.1:
        "models/red/outfit/under/under11a.png"
    if redUnder == 11.2:
        "models/red/outfit/under/under11b.png"




    if redOutfit == 1:
        "models/red/outfit/suit1.png"
    if redOutfit == 2:
        "models/red/outfit/suit2.png"
    if redOutfit == 3:
        "models/red/outfit/suit3.png"
    if redOutfitArms == 1:
        "models/red/outfit/suitArms1.png"
    if redOutfitArms == 2:
        "models/red/outfit/suitArms2.png"
    if redOutfitArms == 3:
        "models/red/outfit/suitArms3.png"
    if redOutfitArms == 4:
        "models/red/outfit/suitArms4.png"

    if redOutfit == 4:
        "models/green/outfit/greenSuit4.png"


    if redShoes == 1:
        "models/red/outfit/shoes/shoes1.png"
    if redShoes == 3:
        "models/red/outfit/shoes/shoes3.png"
    if redShoes == 4:
        "models/red/outfit/shoes/shoes4.png"
    if redShoes == 5:
        "models/red/outfit/shoes/shoes5.png"
    if redShoes == 6:
        "models/red/outfit/shoes/shoes6.png"
    if redShoes == 8:
        "models/red/outfit/shoes/shoes8.png"
    if redShoes == 11:
        "models/red/outfit/shoes/shoes11.png"
    if redShoes == 14:
        "models/red/outfit/shoes/shoes14.png"



    if redShoes == 15:
        "models/red/outfit/shoes/shoes15a.png"
    if redShoes == 15.1:
        "models/red/outfit/shoes/shoes15b.png"
    if redShoes == 16:
        "models/red/outfit/shoes/shoes16.png"



    if redBottom == 1:
        "models/red/outfit/bott/bott1.png"
    if redBottom == 2:
        "models/red/outfit/bott/bott2.png"
    if redBottom == 3:
        "models/red/outfit/bott/bott3.png"
    if redBottom == 4:
        "models/red/outfit/bott/bott4.png"
    if redBottom == 5:
        "models/red/outfit/bott/bott5.png"
    if redBottom == 8:
        "models/red/outfit/bott/bott8.png"
    if redBottom == 15:
        "models/red/outfit/bott/bott15.png"
    if redBottom == 16:
        "models/red/outfit/bott/bott16.png"




    if redNeck == 2:
        "models/red/outfit/neck/neck2.png"
    if redNeck == 7:
        "models/red/outfit/neck/neck7.png"
    if redNeck == 8:
        "models/red/outfit/neck/neck8.png"
    if redNeck == 9:
        "models/red/outfit/neck/neck9.png"
    if redNeck == 14:
        "models/red/outfit/neck/neck14.png"



    if redAcces2 == 8:
        "models/red/outfit/acc2/acc8.png"
    if redAcces2 == 11:
        "models/red/outfit/acc2/acc11.png"



    if redChest == 1:
        "models/red/outfit/chest/top1.png"
    if redChest == 2:
        "models/red/outfit/chest/top2.png"
    if redChest == 2.1:
        "models/red/outfit/chest/top2a.png"
    if redChest == 2.2:
        "models/red/outfit/chest/top2b.png"
    if redChest == 3:
        "models/red/outfit/chest/top3.png"
    if redChest == 4:
        "models/red/outfit/chest/top4.png"
    if redChest == 4.1:
        "models/red/outfit/chest/top4a.png"
    if redChest == 5:
        "top5Clover"
    if redChest == 6:
        "models/red/outfit/chest/top6.png"
    if redChest == 6.1:
        "models/red/outfit/chest/top6a.png"
    if redChest == 6.2:
        "models/red/outfit/chest/top6b.png"
    if redChest == 7:
        "models/red/outfit/chest/top7.png"
    if redChest == 8 and redUnder == 0:
        "models/red/outfit/chest/top8.png"
    if redChest == 8 and redUnder >= 1:
        "models/red/outfit/chest/top8.1.png"
    if redChest == 9:
        "models/red/outfit/chest/top9.png"
    if redChest == 11:
        "models/red/outfit/chest/top11.png"
    if redChest == 14:
        "models/red/outfit/chest/top14.png"
    if redChest == 15:
        "models/red/outfit/chest/top15a.png"
    if redChest == 15.1:
        "models/red/outfit/chest/top15b.png"
    if redChest == 16:
        "models/red/outfit/chest/top16.png"
    if redChest == 99:
        "models/red/outfit/chest/wetT.png"




    if redNeck == 8:
        "models/red/outfit/neck/neck8.png"
    if redNeck == 15:
        "models/red/outfit/neck/neck15.png"
    if redNeck == 16:
        "models/red/outfit/neck/neck15.png"


    if redBottom == 6:
        "models/red/outfit/bott/bott6.png"
    if redBottom == 6.1:
        "models/red/outfit/bott/bott6a.png"
    if redBottom == 6.2:
        "models/red/outfit/bott/bott6b.png"
    if redBottom == 7:
        "models/red/outfit/bott/bott7.png"
    if redBottom == 7.1:
        "models/red/outfit/bott/bott7a.png"
    if redBottom == 8:
        "models/red/outfit/bott/bott8.png"
    if redBottom == 9:
        "models/red/outfit/bott/bott9.png"
    if redBottom == 14:
        "models/red/outfit/bott/bott14.png"


    if redNeck == 4:
        "models/red/outfit/neck/neck4.png"




    if redShoes == 2:
        "models/red/outfit/shoes/shoes2.png"
    if redShoes == 5:
        "models/red/outfit/shoes/shoes5.png"
    if redShoes == 6:
        "models/red/outfit/shoes/shoes6.png"
    if redShoes == 7:
        "models/red/outfit/shoes/shoes7.png"
    if redShoes == 9:
        "models/red/outfit/shoes/shoes9.png"


    group faces:
        attribute rDef default:
            "models/red/face/Happy1.png"
        attribute r1:
            "models/red/face/Happy1.png"
        attribute r2:
            "models/red/face/happy2.png"
        attribute r3:
            "models/red/face/happy3.png"
        attribute r4:
            "models/red/face/sad1.png"
        attribute r5:
            "models/red/face/sad2.png"
        attribute r6:
            "models/red/face/sad3.png"
        attribute r7:
            "models/red/face/angry1.png"
        attribute r8:
            "models/red/face/angry2.png"
        attribute r9:
            "models/red/face/angry3.png"
        attribute r10:
            "models/red/face/annoyed1.png"
        attribute r11:
            "models/red/face/annoyed2.png"
        attribute r12:
            "models/red/face/annoyed3.png"
        attribute r13:
            "models/red/face/closed1.png"
        attribute r14:
            "models/red/face/closed2.png"
        attribute r15:
            "models/red/face/closed3.png"
        attribute r16:
            "models/red/face/confused1.png"
        attribute r17:
            "models/red/face/confused2.png"
        attribute r18:
            "models/red/face/confused3.png"
        attribute r19:
            "models/red/face/shy1.png"
        attribute r20:
            "models/red/face/shy2.png"
        attribute r21:
            "models/red/face/shy3.png"
        attribute r22:
            "models/red/face/naughty1.png"
        attribute r23:
            "models/red/face/naughty2.png"
        attribute r24:
            "models/red/face/naughty3.png"
        attribute r25:
            "models/red/face/pleasure1.png"
        attribute r26:
            "models/red/face/pleasure2.png"
        attribute r27:
            "models/red/face/pleasure3.png"
        attribute r28:
            "models/red/face/shock1.png"
        attribute r29:
            "models/red/face/shock2.png"
        attribute r30:
            "models/red/face/shock3.png"
        attribute r31:
            "models/red/face/serious1.png"
        attribute r32:
            "models/red/face/serious2.png"
        attribute r33:
            "models/red/face/serious3.png"
        attribute r34:
            "models/red/face/serious4.png"
        attribute r35:
            "models/red/face/reluctant1.png"
        attribute r36:
            "models/red/face/reluctant2.png"
        attribute r37:
            "models/red/face/reluctant3.png"
        attribute r38:
            "models/red/face/closed4.png"
        attribute r39:
            "models/red/face/closed5.png"
        attribute r40:
            "models/red/face/angry4.png"
        attribute r41:
            "models/red/face/confused4.png"
        attribute r42:
            "models/red/face/closed6.png"
        attribute r43:
            "models/red/face/down1.png"
        attribute r44:
            "models/red/face/down2.png"
        attribute r45:
            "models/red/face/down3.png"
        attribute r46:
            "models/red/face/down4.png"
        attribute r47:
            "models/red/face/down5.png"
        attribute r48:
            "models/red/face/down6.png"
        attribute r49:
            "models/red/face/down7.png"
        attribute r50:
            "models/red/face/down8.png"
        attribute r51:
            "models/red/face/down9.png"
        attribute r52:
            "models/red/face/side1.png"
        attribute r53:
            "models/red/face/side2.png"
        attribute r54:
            "models/red/face/side3.png"
        attribute r55:
            "models/red/face/side4.png"
        attribute r56:
            "models/red/face/side5.png"
        attribute r57:
            "models/red/face/side6.png"

        attribute r100:
            "models/red/face/redAngry1.png"


    if redHat == 2:
        "models/red/outfit/hat/hat2.png"
    if redHat == 5:
        "hat5Clover"
    if redHat == 7:
        "models/red/outfit/hat/hat7.png"
    if redHat == 8:
        "models/red/outfit/hat/hat8.png"
    if redHat == 11:
        "models/red/outfit/hat/hat11.png"
    if redHat == 14:
        "models/red/outfit/hat/hat14.png"
    if redHat == 15:
        "models/red/outfit/hat/hat15.png"
    if redHat == 16:
        "models/red/outfit/hat/hat16.png"


    if redAcces1 == 4:
        "models/red/outfit/acc1/acc4.png"
    if redAcces1 == 11:
        "models/red/outfit/acc1/acc11.png"
    if redAcces1 == 14:
        "models/red/outfit/acc1/acc14.png"
    if redAcces1 == 15.1:
        "models/red/outfit/acc1/acc15a.png"
    if redAcces1 == 15.2:
        "models/red/outfit/acc1/acc15b.png"
    if redAcces1 == 15.3:
        "models/red/outfit/acc1/acc15c.png"
    if redAcces1 == 16:
        "models/red/outfit/acc1/acc16.png"


    if redAcces2 == 6:
        "models/red/outfit/acc2/acc6.png"
    if redAcces2 == 7:
        "models/red/outfit/acc2/acc7.png"
    if redAcces2 == 15:
        "models/red/outfit/acc2/acc15.png"


    if redBlush == 1:
        "models/red/eff/blush.png"

    if redCum == 1:
        "models/red/eff/cum1.png"
    if redCum == 2:
        "models/red/eff/cum2.png"
    if redCum == 3:
        "models/red/eff/cum3.png"



    if spyRedActive == False and wardrobeCurrentSpy == 2:
        "models/red/lockedClover.png"
    if spyRedActive == False and shopCurrentSpy == 2:
        "models/red/lockedClover.png"
    if spyRedActive == False and shopCurrentSpy == 2:
        "models/red/lockedClover.png"


image side red 1:
    xalign 1.0 yalign 1.0
    "gui/portraits/miniRedHappy.png"
image side red 2:
    xalign 1.0 yalign 1.0
    "gui/portraits/miniRedSad.png"


image testOutfit:
    "models/red/outfit/chest/testShirtA.png"
    pause 1.0
    "models/red/outfit/chest/testShirtB.png"
    pause 1.0
    repeat

image hat5Clover:
    "models/red/outfit/hat/hat5a.png"
    pause 0.3
    "models/red/outfit/hat/hat5b.png"
    pause 0.3
    "models/red/outfit/hat/hat5c.png"
    pause 0.3
    repeat

image top5Clover:
    "models/red/outfit/chest/top5a.png"
    pause 0.3
    "models/red/outfit/chest/top5b.png"
    pause 0.3
    "models/red/outfit/chest/top5c.png"
    pause 0.3
    repeat




default alexNick = _("Girl{#dan}")
default alexHealth = 3
default alexSlut = 0
default alexMood = 100
default alexSocial = 0
default alexDailyChat = 0
default nanoLevelAlex = 10
default alexSupLvl = 0
default alexFriend = _("Acquaintance{#daf}")
default alexHPTimer = 0
default alexTitSize = 1


default outfitAlexUniformActive = False

default yelArms = 1
default yelFace = 1
default yelHair = 1
default yelBlush = 0
default yellowHood = False


default yellowTatHead = 0
default yellowTatChest = 0
default yellowTatArm = 0
default yellowTatBelly = 0
default yellowTatPuss = 0

default yellowTatFoot = 0


default yellowPubicSet = 0


default yellowHairSet = 1


default yellowNipple = 0
default yellowArms = 1
default yellowOutfit = 1
default yellowOutfitArms = 1
default yellowFace = 1
default yellowPubic = 0
default yellowHair = 1
default yellowBlush = 0
default yellowCum = 0

default yellowUnder = 1
default yellowHat = 0
default yellowAcces1 = 0
default yellowPierc1 = 0
default yellowNeck = 0
default yellowChest = 0
default yellowPierc2 = 0
default yellowAcces2 = 0
default yellowBottom = 0
default yellowShoes = 0

default yellowHatSet = 0
default yellowAcc1Set = 0
default yellowNeckSet = 0
default yellowChestSet = 0
default yellowAcc2Set = 0
default yellowBottomSet = 0
default yellowAcc3Set = 0
default yellowShoesSet = 0
default yellowUnderSet = 0
default yellowOutfitSet = 0


default yellowTatHeadSet = 0
default yellowTatChestSet = 0
default yellowTatArmSet = 0
default yellowTatBellySet = 0
default yellowTatPussSet = 0
default yellowTatFootSet = 0



image side miniYellow = "gui/portraits/miniYellowSerious.png"

layeredimage yellow:
    xalign 1.25 yalign 0.1
    if  yellowUnder == 0 and yellowOutfit == 0 and yellowChest == 0:
        "models/yellow/yellowBody1.png"
    elif yellowUnder == 0 and yellowChest == 7.1:
        "models/yellow/yellowBody1.png"
    else:
        "models/yellow/yellowBody2.png"

    if yellowAcces2 == 14:
        "models/yellow/outfit/acc2/acc14.png"


    if yellowChest == 14 or yellowHat == 11 or yellowHat == 5:
        "models/yellow/hair/noHair.png"
    elif yellowHair == 1:
        "models/yellow/hair/hair1.png"
    elif yellowHair == 2:
        "models/yellow/hair/hair2.png"
    elif yellowHair == 3:
        "models/yellow/hair/hair3.png"
    elif yellowHair == 4:
        "models/yellow/hair/hair4.png"
    elif yellowHair == 6:
        "models/yellow/hair/hair6.png"




    if yellowPubic == 1:
        "models/yellow/pubic/pub1.png"
    if yellowPubic == 2:
        "models/yellow/pubic/pub2.png"
    if yellowPubic == 3:
        "models/yellow/pubic/pub3.png"
    if yellowPubic == 4:
        "models/yellow/pubic/pub4.png"
    if yellowPubic == 5:
        "models/yellow/pubic/pub5.png"
    if yellowPubic == 6:
        "models/yellow/pubic/pub6.png"
    if yellowPubic == 7:
        "models/yellow/pubic/pub7.png"



    if yellowTatPuss == 1:
        "models/yellow/tat/puss1.png"
    if yellowTatPuss == 2:
        "models/yellow/tat/puss2.png"
    if yellowTatPuss == 3:
        "models/yellow/tat/puss3.png"
    if yellowTatPuss == 4:
        "models/yellow/tat/puss4.png"
    if yellowTatPuss == 5:
        "models/yellow/tat/puss5.png"
    if yellowTatPuss == 6:
        "models/yellow/tat/puss6.png"


    if yellowArms == 1:
        "models/yellow/arms1.png"
    if yellowArms == 2:
        "models/yellow/arms2.png"
    if yellowArms == 3:
        "models/yellow/arms3.png"
    if yellowArms == 4:
        "models/yellow/arms4.png"



    if yellowTatHead == 1:
        "models/yellow/tat/face1.png"
    if yellowTatHead == 2:
        "models/yellow/tat/face2.png"
    if yellowTatHead == 3:
        "models/yellow/tat/face3.png"
    if yellowTatHead == 4:
        "models/yellow/tat/face4.png"
    if yellowTatHead == 5:
        "models/yellow/tat/face5.png"
    if yellowTatHead == 6:
        "models/yellow/tat/face6.png"

    if yellowTatChest == 1:
        "models/yellow/tat/breast1.png"
    if yellowTatChest == 2:
        "models/yellow/tat/breast2.png"
    if yellowTatChest == 3:
        "models/yellow/tat/breast3.png"
    if yellowTatChest == 4:
        "models/yellow/tat/breast4.png"
    if yellowTatChest == 5:
        "models/yellow/tat/breast5.png"
    if yellowTatChest == 6:
        "models/yellow/tat/breast6.png"

    if yellowTatArm == 1 and yellowArms == 1:
        "models/yellow/tat/arm1.png"
    if yellowTatArm == 2 and yellowArms == 1:
        "models/yellow/tat/arm2.png"
    if yellowTatArm == 3 and yellowArms == 1:
        "models/yellow/tat/arm3.png"
    if yellowTatArm == 4 and yellowArms == 1:
        "models/yellow/tat/arm4.png"
    if yellowTatArm == 5 and yellowArms == 1:
        "models/yellow/tat/arm5.png"
    if yellowTatArm == 6 and yellowArms == 1:
        "models/yellow/tat/arm6.png"

    if yellowTatBelly == 1:
        "models/yellow/tat/belly1.png"
    if yellowTatBelly == 2:
        "models/yellow/tat/belly2.png"
    if yellowTatBelly == 3:
        "models/yellow/tat/belly3.png"
    if yellowTatBelly == 4:
        "models/yellow/tat/belly4.png"
    if yellowTatBelly == 5:
        "models/yellow/tat/belly5.png"
    if yellowTatBelly == 6:
        "models/yellow/tat/belly6.png"

    if yellowTatFoot == 1:
        "models/yellow/tat/lowLeg1.png"
    if yellowTatFoot == 2:
        "models/yellow/tat/lowLeg2.png"
    if yellowTatFoot == 3:
        "models/yellow/tat/lowLeg3.png"
    if yellowTatFoot == 4:
        "models/yellow/tat/lowLeg4.png"
    if yellowTatFoot == 5:
        "models/yellow/tat/lowLeg5.png"
    if yellowTatFoot == 6:
        "models/yellow/tat/lowLeg6.png"


    if alexTitSize == 2 and yellowChest == 0 and yellowUnder == 0 and yellowOutfit == 0 and yellowArms == 1:
        "models/yellow/tits/titsMedium.png"
    if alexTitSize == 3 and yellowChest == 0 and yellowUnder == 0 and yellowOutfit == 0 and yellowArms == 1:
        "models/yellow/tits/titsLarge.png"



    if yellowUnder == 1:
        "models/yellow/outfit/under/under1.png"
    if yellowUnder == 1.1:
        "models/yellow/outfit/under/under1a.png"

    if yellowUnder == 4:
        "models/yellow/outfit/under/under4.png"
    if yellowUnder == 5:
        "models/yellow/outfit/under/under5.png"
    if yellowUnder == 6:
        "models/yellow/outfit/under/under6.png"
    if yellowUnder == 7:
        "models/yellow/outfit/under/under7.png"
    if yellowUnder == 7.1:
        "models/yellow/outfit/under/under7b.png"
    if yellowUnder == 8:
        "models/yellow/outfit/under/under8.png"
    if yellowUnder == 8.1:
        "models/yellow/outfit/under/under8a.png"
    if yellowUnder == 9 and yellowChest != 0:
        "models/yellow/outfit/under/under9Card.png"
    if yellowUnder == 9 and yellowChest == 0:
        "models/yellow/outfit/under/under9.png"
    if yellowUnder == 10:
        "models/yellow/outfit/under/under10.png"
    if yellowUnder == 10.1:
        "models/yellow/outfit/under/under10a.png"



    if yellowNeck == 1:
        "models/yellow/outfit/neck/neck1.png"
    if yellowNeck == 2:
        "models/yellow/outfit/neck/neck2.png"
    if yellowNeck == 7:
        "models/yellow/outfit/neck/neck7.png"
    if yellowNeck == 8:
        "models/yellow/outfit/neck/neck8.png"
    if yellowNeck == 14:
        "models/yellow/outfit/neck/neck14.png"


    if yellowShoes == 1:
        "models/yellow/outfit/shoes/shoes1.png"
    if yellowShoes == 2:
        "models/yellow/outfit/shoes/shoes2.png"
    if yellowShoes == 3:
        "models/yellow/outfit/shoes/shoes3.png"
    if yellowShoes == 4:
        "models/yellow/outfit/shoes/shoes4.png"
    if yellowShoes == 5:
        "models/yellow/outfit/shoes/shoes5.png"
    if yellowShoes == 6.1:
        "models/yellow/outfit/shoes/shoes6a.png"
    if yellowShoes == 6.2:
        "models/yellow/outfit/shoes/shoes6b.png"
    if yellowShoes == 7:
        "models/yellow/outfit/shoes/shoes7.png"
    if yellowShoes == 8:
        "models/yellow/outfit/shoes/shoes8.png"
    if yellowShoes == 9:
        "models/yellow/outfit/shoes/shoes9.png"
    if yellowShoes == 10:
        "models/yellow/outfit/shoes/shoes10.png"
    if yellowShoes == 11:
        "models/yellow/outfit/shoes/shoes11.png"


    if yellowAcces2 == 8:
        "models/yellow/outfit/acc2/acc8.png"
    if yellowAcces2 == 9:
        "models/yellow/outfit/acc2/acc9.png"
    if yellowAcces2 == 10:
        "models/yellow/outfit/acc2/acc10.png"
    if yellowAcces2 == 11:
        "models/yellow/outfit/acc2/acc11.png"

    if yellowCum == 1:
        "models/yellow/eff/cum1.png"
    if yellowCum == 2:
        "models/yellow/eff/cum2.png"
    if yellowCum == 3:
        "models/yellow/eff/cum3.png"


    if yellowChest == 14 or yellowChest == 14.1 or yellowChest == 5:
        "models/yellow/hair/noHair.png"
    elif yellowBottom == 1:
        "models/yellow/outfit/bott/bott1.png"
    elif yellowBottom == 2:
        "models/yellow/outfit/bott/bott2.png"
    elif yellowBottom == 3:
        "models/yellow/outfit/bott/bott3.png"
    elif yellowBottom == 4:
        "models/yellow/outfit/bott/bott4.png"
    elif yellowBottom == 6:
        "models/yellow/outfit/bott/bott6.png"
    elif yellowBottom == 7:
        "models/yellow/outfit/bott/bott7.png"
    elif yellowBottom == 8:
        "models/yellow/outfit/bott/bott8.png"
    elif yellowBottom == 10:
        "models/yellow/outfit/bott/bott10.png"
    elif yellowBottom == 15:
        "models/yellow/outfit/bott/bott15a.png"
    elif yellowBottom == 15.1:
        "models/yellow/outfit/bott/bott15b.png"
    if yellowBottom == 99:
        "models/yellow/outfit/cocktail2.png"



    if yellowChest == 1:
        "models/yellow/outfit/chest/top1.png"
    if yellowChest == 2:
        "models/yellow/outfit/chest/top2a.png"
    if yellowChest == 2.1:
        "models/yellow/outfit/chest/top2b.png"
    if yellowChest == 2.2:
        "models/yellow/outfit/chest/top2c.png"
    if yellowChest == 3:
        "models/yellow/outfit/chest/top3.png"
    if yellowChest == 4:
        "models/yellow/outfit/chest/top4.png"
    if yellowChest == 5:
        "models/yellow/outfit/chest/top5.png"
    if yellowChest == 6:
        "models/yellow/outfit/chest/top6.png"
    if yellowChest == 8:
        "models/yellow/outfit/chest/top8.png"
    if yellowChest == 10:
        "models/yellow/outfit/chest/top10.png"
    if yellowChest == 11:
        "models/yellow/outfit/chest/top11.png"
    if yellowChest == 14:
        "models/yellow/outfit/chest/top14a.png"
    if yellowChest == 14.1:
        "models/yellow/outfit/chest/top14b.png"
    if yellowChest == 15:
        "models/yellow/outfit/chest/top15a.png"
    if yellowChest == 15.1:
        "models/yellow/outfit/chest/top15b.png"
    if yellowChest == 7:
        "models/yellow/outfit/chest/top7a.png"
    if yellowChest == 7.1:
        "models/yellow/outfit/chest/top7b.png"



    if yellowHat == 2:
        "models/yellow/outfit/hat/hat2.png"
    if yellowHat == 5:
        "models/yellow/outfit/hat/hat5.png"
    if yellowHat == 11:
        "models/yellow/outfit/hat/hat11.png"
    if yellowHat == 15:
        "models/yellow/outfit/hat/hat15.png"





    if yellowShoes == 14:
        "models/yellow/outfit/shoes/shoes14.png"
    if yellowShoes == 15:
        "models/yellow/outfit/shoes/shoes15.png"








    if yellowOutfit == 1:
        "models/yellow/outfit/suit1.png"
    if yellowOutfit == 2:
        "models/yellow/outfit/suit2.png"
    if yellowOutfitArms == 1:
        "models/yellow/outfit/suitArms1.png"
    if yellowOutfitArms == 2:
        "models/yellow/outfit/suitArms2.png"
    if yellowOutfitArms == 3:
        "models/yellow/outfit/suitArms3.png"
    if yellowOutfitArms == 4:
        "models/yellow/outfit/suitArms4.png"


    group faces:
        attribute yDef default:
            "models/yellow/face/happy1.png"
        attribute y1:
            "models/yellow/face/happy1.png"
        attribute y2:
            "models/yellow/face/happy2.png"
        attribute y3:
            "models/yellow/face/happy3.png"
        attribute y4:
            "models/yellow/face/sad1.png"
        attribute y5:
            "models/yellow/face/sad2.png"
        attribute y6:
            "models/yellow/face/sad3.png"
        attribute y7:
            "models/yellow/face/angry1.png"
        attribute y8:
            "models/yellow/face/angry2.png"
        attribute y9:
            "models/yellow/face/angry3.png"
        attribute y10:
            "models/yellow/face/annoyed1.png"
        attribute y11:
            "models/yellow/face/annoyed2.png"
        attribute y12:
            "models/yellow/face/annoyed3.png"
        attribute y13:
            "models/yellow/face/closed1.png"
        attribute y14:
            "models/yellow/face/closed2.png"
        attribute y15:
            "models/yellow/face/closed3.png"
        attribute y16:
            "models/yellow/face/confused1.png"
        attribute y17:
            "models/yellow/face/confused2.png"
        attribute y18:
            "models/yellow/face/confused3.png"
        attribute y19:
            "models/yellow/face/shy1.png"
        attribute y20:
            "models/yellow/face/shy2.png"
        attribute y21:
            "models/yellow/face/shy3.png"
        attribute y22:
            "models/yellow/face/naughty1.png"
        attribute y23:
            "models/yellow/face/naughty2.png"
        attribute y24:
            "models/yellow/face/naughty3.png"
        attribute y25:
            "models/yellow/face/pleasure1.png"
        attribute y26:
            "models/yellow/face/pleasure2.png"
        attribute y27:
            "models/yellow/face/pleasure3.png"
        attribute y28:
            "models/yellow/face/shock1.png"
        attribute y29:
            "models/yellow/face/shock2.png"
        attribute y30:
            "models/yellow/face/shock3.png"
        attribute y31:
            "models/yellow/face/serious1.png"
        attribute y32:
            "models/yellow/face/serious2.png"
        attribute y33:
            "models/yellow/face/serious3.png"
        attribute y34:
            "models/yellow/face/serious4.png"
        attribute y35:
            "models/yellow/face/reluctant1.png"
        attribute y36:
            "models/yellow/face/reluctant2.png"
        attribute y37:
            "models/yellow/face/reluctant3.png"
        attribute y38:
            "models/yellow/face/closed4.png"
        attribute y39:
            "models/yellow/face/closed5.png"
        attribute y40:
            "models/yellow/face/angry4.png"
        attribute y41:
            "models/yellow/face/confused4.png"
        attribute y42:
            "models/yellow/face/closed6.png"
        attribute y43:
            "models/yellow/face/down1.png"
        attribute y44:
            "models/yellow/face/down2.png"
        attribute y45:
            "models/yellow/face/down3.png"
        attribute y46:
            "models/yellow/face/down4.png"
        attribute y47:
            "models/yellow/face/down5.png"
        attribute y48:
            "models/yellow/face/down6.png"
        attribute y49:
            "models/yellow/face/down7.png"
        attribute y50:
            "models/yellow/face/down8.png"
        attribute y51:
            "models/yellow/face/down9.png"
        attribute y52:
            "models/yellow/face/side1.png"
        attribute y53:
            "models/yellow/face/side2.png"
        attribute y54:
            "models/yellow/face/side3.png"
        attribute y55:
            "models/yellow/face/side4.png"
        attribute y56:
            "models/yellow/face/side5.png"
        attribute y57:
            "models/yellow/face/side6.png"

        attribute y100:
            "models/yellow/face/redAngry1.png"



    if yellowAcces1 == 4:
        "models/yellow/outfit/acc1/acc4.png"
    if yellowAcces1 == 11:
        "models/yellow/outfit/acc1/acc11.png"
    if yellowAcces1 == 14:
        "models/yellow/outfit/acc1/acc14.png"


    if yellowHair == 5 and yellowHat != 5 and yellowHat != 11:
        "models/yellow/hair/hair5.png"


    if yellowBlush == 1:
        "models/yellow/eff/blush.png"

    if spyYellowActive == False and wardrobeCurrentSpy == 3:
        "models/yellow/lockedAlex.png"
    if spyYellowActive == False and shopCurrentSpy == 3:
        "models/yellow/lockedAlex.png"
    if spyYellowActive == False and shopCurrentSpy == 3:
        "models/yellow/lockedAlex.png"


image side yellow 1:
    xalign 1.0 yalign 1.0
    "gui/portraits/miniYellowHappy.png"
image side yellow 2:
    xalign 1.0 yalign 1.0
    "gui/portraits/miniYellowSad.png"
image side yellow 3:
    xalign 1.0 yalign 1.0
    "gui/portraits/miniYellowShock.png"





default kimOutfit = 1
default kimHair = 1
default kimFace = 1
default kimArms = 1
default kimTits = 1
default kimEffects = 0

image side miniKim = "gui/portraits/miniKim.png"

layeredimage kim:
    xalign 1.25 yalign 0.1
    if kimOutfit >= 0:
        "models/kim/kimBody1.png"
    if kimHair == 1:
        "models/kim/hair1.png"

    if kimArms == 1:
        "models/kim/arms1.png"
    if kimArms == 2:
        "models/kim/arms2.png"

    if kimTits == 1:
        "models/kim/tits1.png"
    if kimTits == 2:
        "models/kim/tits2.png"
    if kimTits == 3:
        "models/kim/tits3.png"

    if kimOutfit == 1:
        "models/kim/outfit1.png"
    if kimOutfit == 2:
        "models/kim/outfit2.png"

    if kimFace == 1:
        "models/kim/face1.png"
    if kimFace == 2:
        "models/kim/face2.png"
    if kimFace == 3:
        "models/kim/face3.png"
    if kimFace == 4:
        "models/kim/face4.png"
    if kimFace == 5:
        "models/kim/face5.png"
    if kimFace == 6:
        "models/kim/face6.png"
    if kimFace == 7:
        "models/kim/face7.png"

    if kimEffects == 1:
        "models/kim/blush.png"




default dummyOutfit = 0

layeredimage dummy:
    always:
        "models/dummy/dummy1.png"
    if dummyOutfit == 1:
        "models/dummy/dummyOutfit1.png"



image GLA = "gui/portraits/gladis.png"

default jerryFace = 1
default jerryArms = 2

layeredimage jerryModel:
    always:
        "models/jerry/jerry.png"
    if jerryFace == 1:
        "models/jerry/face1.png"
    if jerryFace == 2:
        "models/jerry/face2.png"
    if jerryFace == 3:
        "models/jerry/face3.png"
    if jerryFace == 4:
        "models/jerry/face4.png"
    if jerryFace == 5:
        "models/jerry/face5.png"
    if jerryFace == 6:
        "models/jerry/face6.png"

    if jerryArms == 1:
        "models/jerry/arms1.png"
    if jerryArms == 2:
        "models/jerry/arms2.png"

default mathFace = 1

layeredimage matModel:
    always:
        "models/mathias/mathiasModel1.png"
    if mathFace == 1:
        "models/mathias/face1.png"

layeredimage spirit:
    always:
        "models/spirit/spirit.png"


default clerkFace = 1
default clerkGlasses = 1
default clerkBlush = 0

layeredimage clerk:
    always:
        "models/clerk/clerkBody.png"
    if clerkFace == 1:
        "models/clerk/face1.png"
    if clerkFace == 2:
        "models/clerk/face2.png"
    if clerkFace == 3:
        "models/clerk/face3.png"
    if clerkBlush == 1:
        "models/clerk/clerkBlush.png"
    if month == 10 and 14 <= day <= 31:
        "models/clerk/mask.png"
    if clerkGlasses == 1 and month != 10:
        "models/clerk/glasses.png"




image O5O = "models/O5O/agento5o.png"
image agentModel = "models/agent/agent1.png"
image agentModel2 = "models/agent/agent2.png"
image agentModel3 = "models/agent/agent3.png"
image agentModel4 = "models/agent/agent4.png"
image agentModel5 = "models/agent/agent5.png"
image agentModel6 = "models/agent/agent6.png"



default silFace = 1
default silHair = 1
default silOutfit = 1
default silOutfitSet = 2
default silCry = False
default silModel = 1

layeredimage silvaModel:
    if silModel == 1:
        "models/silva/silvaModel1.png"
    elif silModel == 2:
        "models/silva/silvaModel2.png"
    if silFace == 1:
        "models/silva/face/sly1.png"
    if silFace == 2:
        "models/silva/face/closed.png"
    if silFace == 3:
        "models/silva/face/sad.png"
    if silFace == 4:
        "models/silva/face/smile.png"
    if silFace == 5:
        "models/silva/face/angry.png"

    if silCry == True:
        "models/silva/face/cry.png"

    if silHair == 1:
        "models/silva/hair1.png"
    if silHair == 2:
        "models/silva/hair2.png"

    if silOutfit == 1:
        "models/silva/outfit1.png"
    if silOutfit == 2:
        "models/silva/outfit2.png"
    if silOutfit == 3:
        "models/silva/outfit3.png"
    if silOutfit == 4:
        "models/silva/outfit4.png"



default britneyFace = 1
default britneyHidden = True
default britBlush = 0
default britCaptured = False
default britSuit = 1
default britHair = 1
default britGag = False

layeredimage britney:
    always:
        "models/britney/body.png"
    if britSuit == 1:
        "models/britney/suit.png"
    if britSuit == 2:
        "models/britney/suit2.png"
    if britHair == 1:
        "models/britney/hair.png"


    group faces:
        attribute bDef default:
            "models/britney/face/serious4.png"
        attribute b1:
            "models/britney/face/britneyHappy1.png"
        attribute b2:
            "models/britney/face/happy2.png"
        attribute b3:
            "models/britney/face/happy3.png"
        attribute b4:
            "models/britney/face/sad1.png"
        attribute b5:
            "models/britney/face/sad2.png"
        attribute b6:
            "models/britney/face/sad3.png"
        attribute b7:
            "models/britney/face/angry1.png"
        attribute b8:
            "models/britney/face/angry2.png"
        attribute b9:
            "models/britney/face/angry3.png"
        attribute b10:
            "models/britney/face/annoyed1.png"
        attribute b11:
            "models/britney/face/annoyed2.png"
        attribute b12:
            "models/britney/face/annoyed3.png"
        attribute b13:
            "models/britney/face/closed1.png"
        attribute b14:
            "models/britney/face/closed2.png"
        attribute b15:
            "models/britney/face/closed3.png"
        attribute b16:
            "models/britney/face/confused1.png"
        attribute b17:
            "models/britney/face/confused2.png"
        attribute b18:
            "models/britney/face/confused3.png"
        attribute b19:
            "models/britney/face/shy1.png"
        attribute b20:
            "models/britney/face/shy2.png"
        attribute b21:
            "models/britney/face/shy3.png"
        attribute b22:
            "models/britney/face/naughty1.png"
        attribute b23:
            "models/britney/face/naughty2.png"
        attribute b24:
            "models/britney/face/naughty3.png"
        attribute b25:
            "models/britney/face/pleasure1.png"
        attribute b26:
            "models/britney/face/pleasure2.png"
        attribute b27:
            "models/britney/face/pleasure3.png"
        attribute b28:
            "models/britney/face/shock1.png"
        attribute b29:
            "models/britney/face/shock2.png"
        attribute b30:
            "models/britney/face/shock3.png"
        attribute b31:
            "models/britney/face/serious1.png"
        attribute b32:
            "models/britney/face/serious2.png"
        attribute b33:
            "models/britney/face/serious3.png"
        attribute b34:
            "models/britney/face/serious4.png"
        attribute b35:
            "models/britney/face/reluctant1.png"
        attribute b36:
            "models/britney/face/reluctant2.png"
        attribute b37:
            "models/britney/face/reluctant3.png"
        attribute b38:
            "models/britney/face/closed4.png"
        attribute b39:
            "models/britney/face/closed5.png"
        attribute b40:
            "models/britney/face/angry4.png"
        attribute b41:
            "models/britney/face/confused4.png"
        attribute b42:
            "models/britney/face/closed6.png"
        attribute b43:
            "models/britney/face/down1.png"
        attribute b44:
            "models/britney/face/down2.png"
        attribute b45:
            "models/britney/face/down3.png"
        attribute b46:
            "models/britney/face/down4.png"
        attribute b47:
            "models/britney/face/down5.png"
        attribute b48:
            "models/britney/face/down6.png"
        attribute b49:
            "models/britney/face/down7.png"
        attribute b50:
            "models/britney/face/down8.png"
        attribute b51:
            "models/britney/face/down9.png"
        attribute b52:
            "models/britney/face/side1.png"
        attribute b53:
            "models/britney/face/side2.png"
        attribute b54:
            "models/britney/face/side3.png"
        attribute b55:
            "models/britney/face/side4.png"
        attribute b56:
            "models/britney/face/side5.png"
        attribute b57:
            "models/britney/face/side6.png"

    if britGag == True:
        "models/britney/gag.png"
    if britneyHidden == True:
        "models/britney/hidden.png"


    if britBlush == 1:
        "models/britney/blush.png"



default gladisFace = 1
default gladisHidden = True

layeredimage gladis:
    always:
        "models/gladis/gladis.png"
    if gladisHidden == True:
        "models/gladis/gladisHidden.png"

image gladis2 = "models/gladis/gladisHidden.png"
image gladis3 = "models/gladis/gladisArmed.png"



default timFace = 1
default timHidden = True

layeredimage timModel:
    always:
        "models/tim/timBody1.png"
    if timFace == 1:
        "models/tim/face/neutral1.png"
    if timHidden == True:
        "models/tim/timHidden.png"



default sebFace = 1

layeredimage sebModel1:
    always:
        "models/seb/seb1.png"

layeredimage sebModel2:
    always:
        "models/seb/seb2.png"
    if sebFace == 1:
        "models/seb/sebFace1.png"
    if sebFace == 2:
        "models/seb/sebFace2.png"
    if sebFace == 3:
        "models/seb/sebFace3.png"



default candyFace = 1
default candyHidden = True

layeredimage candyModel:
    always:
        "models/candy/candyBody1.png"
    if candyFace == 1:
        "models/candy/face1.png"
    if candyFace == 2:
        "models/candy/face2.png"
    if candyFace == 3:
        "models/candy/face3.png"
    if candyFace == 4:
        "models/candy/face4.png"
    if candyFace == 5:
        "models/candy/face5.png"
    if candyFace == 6:
        "models/candy/face6.png"
    if candyHidden == True:
        "models/candy/candyHidden.png"



default kandFace = 1
default kandHidden = True

layeredimage kandModel:
    always:
        "models/kand/kandBody1.png"
    if kandFace == 1:
        "models/kand/face1.png"
    if kandHidden == True:
        "models/kand/kandHidden.png"




default melodyFace = 1

layeredimage melodyModel:
    always:
        "models/melody/melodyBody.png"





default taliaFace = 1

layeredimage taliaModel:
    always:
        "models/talia/taliaBody.png"




default gangster1Face = 1
default gangster1Outfit = 1

layeredimage gangster1:
    always:
        "models/gangster1/gangsterBody1.png"
    if gangster1Face == 1:
        "models/gangster1/gangsterFace1.png"
    if gangster1Face == 2:
        "models/gangster1/gangsterFace2.png"
    if gangster1Face == 3:
        "models/gangster1/gangsterFace3.png"

    if gangster1Outfit == 1:
        "models/gangster1/gangsterOutfit1.png"
    if gangster1Outfit == 2:
        "models/gangster1/gangsterOutfit2.png"



image zukker = "models/zukker/zukker.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
