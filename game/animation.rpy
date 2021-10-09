
default aniStage = 1
default aniSpySelect = 0
default finishAni = False
default sexScene = 0
default loopProtection = 0


default modelArmsMenu = False
default modelOutfitMenu = False

default sexAct1 = "???"
default sexAct2 = "???"
default sexAct3 = "???"
default sexAct4 = "???"
default sexAct5 = "???"
default sexAct6 = "???"

image blow = "animations/blow/blowjob.jpg"
image kiss1 = "animations/kissSamClover.jpg"
image kiss2 = "animations/kissCloverAlex.jpg"



screen nxtPhotoScene:
    if finishAni == True:
        vbox xalign 1.0 yalign 0.0:
            imagebutton:
                idle "animations/finAni.png"
                hover "animations/finAni-hover.png"
                action Jump("finAni")

    vbox xalign 0.05 yalign 0.05:
        imagebutton:
            idle "animations/camera.png"
            hover "animations/camera-hover.png"
            action Jump("takePic")

    vbox xalign 0.95 yalign 0.92:
        imagebutton:
            idle "animations/model/photoBut4.png"
            hover "animations/model/photoBut4-hover.png"
            action Jump("finAni")

    if aniSpySelect == 1:
        vbox xalign 0.05 yalign 0.2:
            imagebutton:
                idle "animations/model/shopButtTop.png"
                hover "animations/model/shopButtTop-hover.png"
                action ToggleVariable("modelOutfitMenu")
        vbox xalign 0.05 yalign 0.33:
            imagebutton:
                idle "animations/model/shopArm.png"
                hover "animations/model/shopArm-hover.png"
                action ToggleVariable("modelArmsMenu")

        if modelOutfitMenu:
            vbox xalign 0.11 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt1.png"
                    hover "animations/model/butt1-hover.png"
                    action SetVariable("samModelOutfit", 1)
            vbox xalign 0.16 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt2.png"
                    hover "animations/model/butt2-hover.png"
                    action SetVariable("samModelOutfit", 2)
            vbox xalign 0.21 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt3.png"
                    hover "animations/model/butt3-hover.png"
                    action SetVariable("samModelOutfit", 3)
            vbox xalign 0.26 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt4.png"
                    hover "animations/model/butt4-hover.png"
                    action SetVariable("samModelOutfit", 4)
            vbox xalign 0.31 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt0.png"
                    hover "animations/model/butt0-hover.png"
                    action SetVariable("samModelOutfit", 0)

        vbox xalign 0.47 yalign 0.28:
            imagebutton:
                idle "animations/model/hidBut1.png"
                hover "animations/model/hidBut1-hover.png"
                if samModelOutfit == 2:
                    action SetVariable("samModelOutfit", 2.1)
                if samModelOutfit == 3:
                    action SetVariable("samModelOutfit", 3.1)

        if modelArmsMenu:
            vbox xalign 0.11 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt1.png"
                    hover "animations/model/butt1-hover.png"
                    action SetVariable("samModelArms", 1)
            vbox xalign 0.16 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt2.png"
                    hover "animations/model/butt2-hover.png"
                    action SetVariable("samModelArms", 2)
            vbox xalign 0.21 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt3.png"
                    hover "animations/model/butt3-hover.png"
                    action SetVariable("samModelArms", 3)
            vbox xalign 0.26 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt4.png"
                    hover "animations/model/butt4-hover.png"
                    action SetVariable("samModelArms", 4)

        if picQuest3 >= 3:
            vbox xalign 0.735 yalign 0.23:
                imagebutton:
                    idle "animations/model/cuffsButt.png"
                    hover "animations/model/cuffsButt-hover.png"
                    action Jump("modelEquipCuffs")
        if picQuest4 >= 3:
            vbox xalign 0.83 yalign 0.23:
                imagebutton:
                    idle "animations/model/collarButt.png"
                    hover "animations/model/collarButt-hover.png"
                    action ToggleVariable("samModelCollar1")
        if picQuest5 >= 3:
            vbox xalign 0.905 yalign 0.23:
                imagebutton:
                    idle "animations/model/gagButt.png"
                    hover "animations/model/gagButt-hover.png"
                    action SetVariable("samModelFace", 7), ToggleVariable("samModelGag1")
        if picQuest2 >= 3:
            vbox xalign 0.73 yalign 0.4:
                imagebutton:
                    idle "animations/model/blindfoldButt.png"
                    hover "animations/model/blindfoldButt-hover.png"
                    action ToggleVariable("samModelBlind1")
        if picQuest9 >= 3:
            vbox xalign 0.84 yalign 0.4:
                imagebutton:
                    idle "animations/model/spreaderButt.png"
                    hover "animations/model/spreaderButt-hover.png"
                    action SetVariable("samModelFace", 4), Jump("modelEquipSpreader")
        if picQuest7 >= 3:
            vbox xalign 0.915 yalign 0.42:
                imagebutton:
                    idle "animations/model/chainsButt.png"
                    hover "animations/model/chainsButt-hover.png"
                    action SetVariable("samModelFace", 5), Jump("modelEquipChains")
        if picQuest8 >= 3:
            vbox xalign 0.92 yalign 0.61:
                imagebutton:
                    idle "animations/model/vibButt.png"
                    hover "animations/model/vibButt-hover.png"
                    action SetVariable("samModelFace", 2), Jump("modelEquipVIB")
        if picQuest6 >= 3:
            vbox xalign 0.735 yalign 0.68:
                imagebutton:
                    idle "animations/model/plugButt.png"
                    hover "animations/model/plugButt-hover.png"
                    action SetVariable("samModelFace", 8), ToggleVariable("samModelPlug")
        if task26Stage >= 23:
            vbox xalign 0.785 yalign 0.68:
                imagebutton:
                    idle "animations/model/dildoButt.png"
                    hover "animations/model/dildoButt-hover.png"
                    action SetVariable("samModelFace", 6), ToggleVariable("samModelDildo")


    if aniSpySelect == 2:
        vbox xalign 0.05 yalign 0.2:
            imagebutton:
                idle "animations/model/shopButtTop.png"
                hover "animations/model/shopButtTop-hover.png"
                action ToggleVariable("modelOutfitMenu")
        vbox xalign 0.05 yalign 0.33:
            imagebutton:
                idle "animations/model/shopArm.png"
                hover "animations/model/shopArm-hover.png"
                action ToggleVariable("modelArmsMenu")

        if modelOutfitMenu:
            vbox xalign 0.11 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt1.png"
                    hover "animations/model/butt1-hover.png"
                    action SetVariable("cloverModelOutfit", 1)
            vbox xalign 0.16 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt2.png"
                    hover "animations/model/butt2-hover.png"
                    action SetVariable("cloverModelOutfit", 2)
            vbox xalign 0.21 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt3.png"
                    hover "animations/model/butt3-hover.png"
                    action SetVariable("cloverModelOutfit", 3)
            vbox xalign 0.26 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt4.png"
                    hover "animations/model/butt4-hover.png"
                    action SetVariable("cloverModelOutfit", 4)
            vbox xalign 0.31 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt0.png"
                    hover "animations/model/butt0-hover.png"
                    action SetVariable("cloverModelOutfit", 0)

        if modelArmsMenu:
            vbox xalign 0.11 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt1.png"
                    hover "animations/model/butt1-hover.png"
                    action SetVariable("cloverModelArms", 1)
            vbox xalign 0.16 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt2.png"
                    hover "animations/model/butt2-hover.png"
                    action SetVariable("cloverModelArms", 2)
            vbox xalign 0.21 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt3.png"
                    hover "animations/model/butt3-hover.png"
                    action SetVariable("cloverModelArms", 3)
            vbox xalign 0.26 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt4.png"
                    hover "animations/model/butt4-hover.png"
                    action SetVariable("cloverModelArms", 4)

    if aniSpySelect == 3:
        vbox xalign 0.05 yalign 0.2:
            imagebutton:
                idle "animations/model/shopButtTop.png"
                hover "animations/model/shopButtTop-hover.png"
                action ToggleVariable("modelOutfitMenu")
        vbox xalign 0.05 yalign 0.33:
            imagebutton:
                idle "animations/model/shopArm.png"
                hover "animations/model/shopArm-hover.png"
                action ToggleVariable("modelArmsMenu")

        if modelOutfitMenu:
            vbox xalign 0.11 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt1.png"
                    hover "animations/model/butt1-hover.png"
                    action SetVariable("alexModelOutfit", 1)
            vbox xalign 0.16 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt2.png"
                    hover "animations/model/butt2-hover.png"
                    action SetVariable("alexModelOutfit", 2)
            vbox xalign 0.21 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt3.png"
                    hover "animations/model/butt3-hover.png"
                    action SetVariable("alexModelOutfit", 3)
            vbox xalign 0.26 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt4.png"
                    hover "animations/model/butt4-hover.png"
                    action SetVariable("alexModelOutfit", 4)
            vbox xalign 0.31 yalign 0.21:
                imagebutton:
                    idle "animations/model/butt0.png"
                    hover "animations/model/butt0-hover.png"
                    action SetVariable("alexModelOutfit", 0)

        vbox xalign 0.47 yalign 0.28:
            imagebutton:
                idle "animations/model/hidBut1.png"
                hover "animations/model/hidBut1-hover.png"
                if alexModelOutfit == 2:
                    action SetVariable("alexModelOutfit", 2.1)

        if modelArmsMenu:
            vbox xalign 0.11 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt1.png"
                    hover "animations/model/butt1-hover.png"
                    action SetVariable("alexModelArms", 1)
            vbox xalign 0.16 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt2.png"
                    hover "animations/model/butt2-hover.png"
                    action SetVariable("alexModelArms", 2)
            vbox xalign 0.21 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt3.png"
                    hover "animations/model/butt3-hover.png"
                    action SetVariable("alexModelArms", 3)
            vbox xalign 0.26 yalign 0.34:
                imagebutton:
                    idle "animations/model/butt4.png"
                    hover "animations/model/butt4-hover.png"
                    action SetVariable("alexModelArms", 4)

        if picQuest3 >= 3:
            vbox xalign 0.735 yalign 0.23:
                imagebutton:
                    idle "animations/model/cuffsButt.png"
                    hover "animations/model/cuffsButt-hover.png"
                    action Jump("modelEquipCuffs")
        if picQuest4 >= 3:
            vbox xalign 0.83 yalign 0.23:
                imagebutton:
                    idle "animations/model/collarButt.png"
                    hover "animations/model/collarButt-hover.png"
                    action ToggleVariable("alexModelCollar1")
        if picQuest5 >= 3:
            vbox xalign 0.905 yalign 0.23:
                imagebutton:
                    idle "animations/model/gagButt.png"
                    hover "animations/model/gagButt-hover.png"
                    action SetVariable("alexModelFace", 7), ToggleVariable("alexModelGag1")
        if picQuest2 >= 3:
            vbox xalign 0.73 yalign 0.4:
                imagebutton:
                    idle "animations/model/blindfoldButt.png"
                    hover "animations/model/blindfoldButt-hover.png"
                    action ToggleVariable("alexModelBlind1")
        if picQuest9 >= 3:
            vbox xalign 0.84 yalign 0.4:
                imagebutton:
                    idle "animations/model/spreaderButt.png"
                    hover "animations/model/spreaderButt-hover.png"
                    action SetVariable("alexModelFace", 4), Jump("modelEquipSpreader")
        if picQuest7 >= 3:
            vbox xalign 0.915 yalign 0.42:
                imagebutton:
                    idle "animations/model/chainsButt.png"
                    hover "animations/model/chainsButt-hover.png"
                    action SetVariable("alexModelFace", 5), Jump("modelEquipChains")
        if picQuest8 >= 3:
            vbox xalign 0.92 yalign 0.61:
                imagebutton:
                    idle "animations/model/vibButt.png"
                    hover "animations/model/vibButt-hover.png"
                    action SetVariable("alexModelFace", 2), Jump("modelEquipVIB")
        if picQuest6 >= 3:
            vbox xalign 0.775 yalign 0.68:
                imagebutton:
                    idle "animations/model/plugButt.png"
                    hover "animations/model/plugButt-hover.png"
                    action SetVariable("alexModelFace", 8), ToggleVariable("alexModelPlug")
        if task26Stage >= 23:
            vbox xalign 0.785 yalign 0.68:
                imagebutton:
                    idle "animations/model/dildoButt.png"
                    hover "animations/model/dildoButt-hover.png"
                    action SetVariable("alexModelFace", 6), ToggleVariable("alexModelDildo")

    if aniSpySelect == 2:
        if picQuest3 >= 3:
            vbox xalign 0.735 yalign 0.23:
                imagebutton:
                    idle "animations/model/cuffsButt.png"
                    hover "animations/model/cuffsButt-hover.png"
                    action Jump("modelEquipCuffs")
        if picQuest4 >= 3:
            vbox xalign 0.83 yalign 0.23:
                imagebutton:
                    idle "animations/model/collarButt.png"
                    hover "animations/model/collarButt-hover.png"
                    action ToggleVariable("cloverModelCollar1")
        if picQuest5 >= 3:
            vbox xalign 0.905 yalign 0.23:
                imagebutton:
                    idle "animations/model/gagButt.png"
                    hover "animations/model/gagButt-hover.png"
                    action SetVariable("cloverModelFace", 7), ToggleVariable("cloverModelGag1")
        if picQuest2 >= 3:
            vbox xalign 0.73 yalign 0.4:
                imagebutton:
                    idle "animations/model/blindfoldButt.png"
                    hover "animations/model/blindfoldButt-hover.png"
                    action ToggleVariable("cloverModelBlind1")
        if picQuest9 >= 3:
            vbox xalign 0.84 yalign 0.4:
                imagebutton:
                    idle "animations/model/spreaderButt.png"
                    hover "animations/model/spreaderButt-hover.png"
                    action SetVariable("cloverModelFace", 4), Jump("modelEquipSpreader")
        if picQuest7 >= 3:
            vbox xalign 0.915 yalign 0.42:
                imagebutton:
                    idle "animations/model/chainsButt.png"
                    hover "animations/model/chainsButt-hover.png"
                    action SetVariable("cloverModelFace", 5), Jump("modelEquipChains")
        if picQuest8 >= 3:
            vbox xalign 0.92 yalign 0.61:
                imagebutton:
                    idle "animations/model/vibButt.png"
                    hover "animations/model/vibButt-hover.png"
                    action SetVariable("cloverModelFace", 2), Jump("modelEquipVIB")
        if picQuest6 >= 3:
            vbox xalign 0.735 yalign 0.68:
                imagebutton:
                    idle "animations/model/plugButt.png"
                    hover "animations/model/plugButt-hover.png"
                    action SetVariable("cloverModelFace", 8), ToggleVariable("cloverModelPlug")
        if task26Stage >= 23:
            vbox xalign 0.785 yalign 0.68:
                imagebutton:
                    idle "animations/model/dildoButt.png"
                    hover "animations/model/dildoButt-hover.png"
                    action SetVariable("cloverModelFace", 6), ToggleVariable("cloverModelDildo")

    if aniSpySelect == 3:
        if picQuest3 >= 3:
            vbox xalign 0.735 yalign 0.23:
                imagebutton:
                    idle "animations/model/cuffsButt.png"
                    hover "animations/model/cuffsButt-hover.png"
                    action Jump("modelEquipCuffs")
        if picQuest4 >= 3:
            vbox xalign 0.83 yalign 0.23:
                imagebutton:
                    idle "animations/model/collarButt.png"
                    hover "animations/model/collarButt-hover.png"
                    action ToggleVariable("alexModelCollar1")
        if picQuest5 >= 3:
            vbox xalign 0.905 yalign 0.23:
                imagebutton:
                    idle "animations/model/gagButt.png"
                    hover "animations/model/gagButt-hover.png"
                    action SetVariable("alexModelFace", 7), ToggleVariable("alexModelGag1")
        if picQuest2 >= 3:
            vbox xalign 0.73 yalign 0.4:
                imagebutton:
                    idle "animations/model/blindfoldButt.png"
                    hover "animations/model/blindfoldButt-hover.png"
                    action ToggleVariable("alexModelBlind1")
        if picQuest9 >= 3:
            vbox xalign 0.84 yalign 0.4:
                imagebutton:
                    idle "animations/model/spreaderButt.png"
                    hover "animations/model/spreaderButt-hover.png"
                    action SetVariable("alexModelFace", 4), Jump("modelEquipSpreader")
        if picQuest7 >= 3:
            vbox xalign 0.915 yalign 0.42:
                imagebutton:
                    idle "animations/model/chainsButt.png"
                    hover "animations/model/chainsButt-hover.png"
                    action SetVariable("alexModelFace", 5), Jump("modelEquipChains")
        if picQuest8 >= 3:
            vbox xalign 0.92 yalign 0.61:
                imagebutton:
                    idle "animations/model/vibButt.png"
                    hover "animations/model/vibButt-hover.png"
                    action SetVariable("alexModelFace", 2), Jump("modelEquipVIB")
        if picQuest6 >= 3:
            vbox xalign 0.775 yalign 0.68:
                imagebutton:
                    idle "animations/model/plugButt.png"
                    hover "animations/model/plugButt-hover.png"
                    action SetVariable("alexModelFace", 8), ToggleVariable("alexModelPlug")



label modelEquipCuffs:
    if aniSpySelect == 1:
        if samModelArms == 4:
            play sound "audio/sfx/handcuffs.mp3"
            $ samModelArms = 1
        elif True:
            play sound "audio/sfx/handcuffs.mp3"
            $ samModelArms = 4
    elif aniSpySelect == 2:
        if cloverModelArms == 4:
            play sound "audio/sfx/handcuffs.mp3"
            $ cloverModelArms = 1
        elif True:
            play sound "audio/sfx/handcuffs.mp3"
            $ cloverModelArms = 4
    elif aniSpySelect == 3:
        if alexModelArms == 4:
            play sound "audio/sfx/handcuffs.mp3"
            $ alexModelArms = 1
        elif True:
            play sound "audio/sfx/handcuffs.mp3"
            $ alexModelArms = 4
    call screen nxtPhotoScene



label modelEquipSpreader:
    if aniSpySelect == 1:
        if samModelBody != 2:
            $ samModelSpread = True
            $ samModelBody = 2
        elif True:
            $ samModelSpread = False
            $ samModelBody = 1
    if aniSpySelect == 2:
        if cloverModelBody != 2:
            $ cloverModelSpread = True
            $ cloverModelBody = 2
        elif True:
            $ cloverModelBody = 1
    if aniSpySelect == 3:
        if alexModelBody != 2:
            $ alexModelSpread = True
            $ alexModelBody = 2
        elif True:
            $ alexModelBody = 1
    call screen nxtPhotoScene



label modelEquipVIB:
    if aniSpySelect == 1:
        if samModelBody != 3:
            $ samModelBody = 3
        elif True:
            $ samModelBody = 1
    if aniSpySelect == 2:
        if cloverModelBody != 3:
            $ cloverModelBody = 3
        elif True:
            $ cloverModelBody = 1
    if aniSpySelect == 3:
        if alexModelBody != 3:
            $ alexModelBody = 3
        elif True:
            $ alexModelBody = 1
    call screen nxtPhotoScene



label modelEquipChains:
    if aniSpySelect == 1:
        if samModelArms == 5:
            $ samModelArms = 1
        elif True:
            $ samModelArms = 5
    elif aniSpySelect == 2:
        if cloverModelArms == 5:
            $ cloverModelArms = 1
        elif True:
            $ cloverModelArms = 5
    elif aniSpySelect == 3:
        if alexModelArms == 5:
            $ alexModelArms = 1
        elif True:
            $ alexModelArms = 5
    call screen nxtPhotoScene


screen nxtScene:
    key "1" action Jump("nxtAniStage")

    text "[randVid]" xalign 0.9 yalign 0.9

    vbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "animations/aniNxt.png"
            hover "animations/aniNxt-hover.png"
            action Jump("nxtAniStage")

    if finishAni == True:
        vbox xalign 1.0 yalign 0.0:
            imagebutton:
                idle "animations/finAni.png"
                hover "animations/finAni-hover.png"
                action Jump("finAni")

    vbox xalign 0.05 yalign 0.05:
        imagebutton:
            idle "animations/camera.png"
            hover "animations/camera-hover.png"
            action Jump("takePic")

default perfectPic = False
default infiniteLoopBlock = 0
label takePic:
    hide cameraSmiley
    play sound "audio/sfx/camera.mp3"
    show screen white
    pause 0.01
    hide screen white
    if aniSpySelect == 1:

        if sexScene == 1:
            if 2 <= task5Stage <= 2.5:
                $ task5Pics = True
                call newPhoto from _call_newPhoto
            if picQuest1 == 1 and samModelOutfit == 1:
                $ picQuest1 = 2
                call newPhoto from _call_newPhoto_1
            if picQuest2 == 1 and 2 <= samModelOutfit <= 2.3:
                $ picQuest2 = 2
                call newPhoto from _call_newPhoto_2
            if picQuest3 == 1 and samModelOutfit == 2.1 and samModelArms == 3:
                $ picQuest3 = 2
                call newPhoto from _call_newPhoto_3
            if picQuest4 == 1 and samModelOutfit == 0 and samModelArms == 2:
                $ picQuest4 = 2
                call newPhoto from _call_newPhoto_12
            if picQuest5 == 1 and samModelOutfit == 0 and samModelArms == 4:
                $ picQuest5 = 2
                call newPhoto from _call_newPhoto_13
            call screen nxtPhotoScene

        if sexScene == 2:
            jump restartSamSex2

        if sexScene == 3:
            jump restartSamSex3
        if sexScene == 4:
            jump restartSamSex4
        if sexScene == 5:
            jump restartSamSex4



    if aniSpySelect == 2:

        if sexScene == 1:
            if 2 <= task5Stage <= 2.5:
                $ task5Pics = True
                call newPhoto from _call_newPhoto_4
            if picQuest1 == 1 and cloverModelOutfit == 1:
                $ picQuest1 = 2
                call newPhoto from _call_newPhoto_5
            if picQuest2 == 1 and 2 <= cloverModelOutfit <= 2.3:
                $ picQuest2 = 2
                call newPhoto from _call_newPhoto_6
            if picQuest3 == 1 and cloverModelOutfit == 2.1 and cloverModelArms == 3:
                $ picQuest3 = 2
                call newPhoto from _call_newPhoto_7
            if picQuest4 == 1 and cloverModelOutfit == 0 and cloverModelArms == 2:
                $ picQuest4 = 2
                call newPhoto from _call_newPhoto_14
            if picQuest5 == 1 and cloverModelOutfit == 0 and cloverModelArms == 4:
                $ picQuest5 = 2
                call newPhoto from _call_newPhoto_15
            call screen nxtPhotoScene

        if sexScene == 2:
            jump restartCloverSex2

        if sexScene == 3:
            jump restartCloverSex3
        if sexScene == 4:
            jump restartCloverSex4
        if sexScene == 5:
            jump restartCloverSex4



    if aniSpySelect == 3:

        if sexScene == 1:
            if 2 <= task5Stage <= 2.5:
                $ task5Pics = True
                call newPhoto from _call_newPhoto_8
            if picQuest1 == 1 and alexModelOutfit == 1:
                $ picQuest1 = 2
                call newPhoto from _call_newPhoto_9
            if picQuest2 == 1 and 2 <= alexModelOutfit <= 2.3:
                $ picQuest2 = 2
                call newPhoto from _call_newPhoto_10
            if picQuest3 == 1 and alexModelOutfit == 2.1 and alexModelArms == 3:
                $ picQuest3 = 2
                call newPhoto from _call_newPhoto_11
            if picQuest4 == 1 and alexModelOutfit == 0 and alexModelArms == 2:
                $ picQuest4 = 2
                call newPhoto from _call_newPhoto_16
            if picQuest5 == 1 and alexModelOutfit == 0 and alexModelArms == 4:
                $ picQuest5 = 2
                call newPhoto from _call_newPhoto_17
            call screen nxtPhotoScene

            call screen nxtPhotoScene

        if sexScene == 2:
            jump restartAlexSex2

        if sexScene == 3:
            jump restartAlexSex3
        if sexScene == 4:
            jump restartAlexSex4
        if sexScene == 5:
            jump restartAlexSex4



label nxtAniStage:
    $ aniStage += 1

    hide dildoAlexSce1Var1
    hide dildoAlexSce1Var2
    hide dildoAlexSce1Var3
    hide dildoAlexSce1Var4
    hide dildoSamSce1Var1
    hide dildoSamSce1Var2
    hide dildoSamSce1Var3
    hide dildoSamSce1Var4
    hide dildoCloverSce1Var1
    hide dildoCloverSce1Var2
    hide dildoCloverSce1Var3
    hide dildoCloverSce1Var4

    hide dildoAlexSce2Var1
    hide dildoAlexSce2Var2
    hide dildoAlexSce2Var3
    hide dildoAlexSce2Var4
    hide dildoSamSce2Var1
    hide dildoSamSce2Var2
    hide dildoSamSce2Var3
    hide dildoSamSce2Var4
    hide dildoCloverSce2Var1
    hide dildoCloverSce2Var2
    hide dildoCloverSce2Var3
    hide dildoCloverSce2Var4

    hide dildoAlexSce3Var1
    hide dildoAlexSce3Var2
    hide dildoAlexSce3Var3
    hide dildoAlexSce3Var4
    hide dildoSamSce3Var1
    hide dildoSamSce3Var2
    hide dildoSamSce3Var3
    hide dildoSamSce3Var4
    hide dildoCloverSce3Var1
    hide dildoCloverSce3Var2
    hide dildoCloverSce3Var3
    hide dildoCloverSce3Var4

    hide dildoAlexSce4Var1
    hide dildoAlexSce4Var2
    hide dildoAlexSce4Var3
    hide dildoAlexSce4Var4
    hide dildoSamSce4Var1
    hide dildoSamSce4Var2
    hide dildoSamSce4Var3
    hide dildoCloverSce4Var1
    hide dildoCloverSce4Var2
    hide dildoCloverSce4Var3

    hide dildoAlexSce5Var1
    hide dildoSamSce5Var1
    hide dildoCloverSce5Var1
    if aniSpySelect == 1:
        jump restartSamSex2
    if aniSpySelect == 2:
        jump restartCloverSex2
    if aniSpySelect == 3:
        jump restartAlexSex2

label finAni:
    if sexScene == 1:
        scene black
        hide samPhotoFace
        $ infiniteLoopBlock = 0
        hide modelSam
        hide modelClover
        hide modelAlex
        hide screen nxtScene
        hide screen nxtPhotoScene
        with fade
        $ finishAni = False
        $ aniStage = 1
        jump nightCycle
    if sexScene == 2:
        scene black
        hide screen nxtScene
        with fade
        $ finishAni = False
        $ aniStage = 1
        $ aniSpySelect = 0
        hide dildoAlexSce5Var1
        hide dildoCloverSce5Var1
        hide dildoSamSce5Var1
        jump nightCycle



image bgDildo1 = "animations/dildo/green/bgDildo.jpg"

image dildoSamSce1Var1 movie = Movie(play="animations/dildo/green/1-1.ogv", loop=False)
image dildoSamSce1Var2 movie = Movie(play="animations/dildo/green/1-2.ogv", loop=False)
image dildoSamSce1Var3 movie = Movie(play="animations/dildo/green/1-3.ogv", loop=False)
image dildoSamSce1Var4 movie = Movie(play="animations/dildo/green/1-4.ogv", loop=False)

image dildoSamSce2Var1 movie = Movie(play="animations/dildo/green/2-1.ogv", loop=False)
image dildoSamSce2Var2 movie = Movie(play="animations/dildo/green/2-2.ogv", loop=False)
image dildoSamSce2Var3 movie = Movie(play="animations/dildo/green/2-3.ogv", loop=False)
image dildoSamSce2Var4 movie = Movie(play="animations/dildo/green/2-4.ogv", loop=False)

image dildoSamSce3Var1 movie = Movie(play="animations/dildo/green/3-1.ogv", loop=False)
image dildoSamSce3Var2 movie = Movie(play="animations/dildo/green/3-2.ogv", loop=False)
image dildoSamSce3Var3 movie = Movie(play="animations/dildo/green/3-3.ogv", loop=False)
image dildoSamSce3Var4 movie = Movie(play="animations/dildo/green/3-4.ogv", loop=False)

image dildoSamSce4Var1 movie = Movie(play="animations/dildo/green/4-1.ogv", loop=False)
image dildoSamSce4Var2 movie = Movie(play="animations/dildo/green/4-2.ogv", loop=False)
image dildoSamSce4Var3 movie = Movie(play="animations/dildo/green/4-3.ogv", loop=False)

image dildoSamSce5Var1 movie = Movie(play="animations/dildo/green/5-1.ogv", loop=False)


image bgForplay1 = "animations/forplay/green/bgForplay.jpg"

label sexScenesSam:
    hide screen nanoLevelSam
    menu:
        "!!! Emergency suppression !!!" if nanoLevelSam == 100:
            $ nanoLevelSam = 50
            show scene_darkening with d3
            show green g100 at ri with d3
            s "{b}*Growls*{/b}"
            y "Uh oh! Looks like we need to 'seriously' have your nanobots suppressed tonight!"
            hide green
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            "You jump Sam and tie her to the bed."
            s "!!!"
            hide scene_darkening with d3
            $ spyRoomRand = 11
            with d3
            y "There we go. You stay there until you're back to your normal self."
            s "{b}*Moans*{/b}"
            jump samCall
        "[sexAct1]" if True:
            if sexAct1 == "???":
                jump sexScenesSam
            elif task5Stage >= 5 and samMood <= 25:
                show green g4 at ri with d3
                s "I'm sorry, I really don't feel like it right now..."
                y "................"
                hide green with d3
                jump samCall
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelSam -= 15
                if 2 <= slutLevel <= 3:
                    $ nanoLevelSam -= 8
                if 4 <= slutLevel <= 6:
                    $ nanoLevelSam -= 5
                elif True:
                    $ nanoLevelSam -= 2

                $ sexScene = 1
                jump samSex1
        "[sexAct2]" if True:
            if sexAct2 == "???":
                jump sexScenesSam
            elif task5Stage >= 5 and samMood <= 25:
                show green g4 at ri with d3
                s "I'm sorry, I really don't feel like it right now..."
                y "................"
                hide green with d3
                jump samCall
            elif 5 <= task5Stage <= 7 and samMood >= 26:

                if slutLevel <= 1:
                    $ nanoLevelSam -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelSam -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelSam -= 5
                elif True:
                    $ nanoLevelSam -= 2

                $ sexScene = 2
                $ samSpySex = 2
                show green g38 at ri with d3
                s "Okay... but you can't watch!"
                y "......................"
                hide green
                scene bgBase
                with fade
                jump base
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelSam -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelSam -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelSam -= 5
                elif True:
                    $ nanoLevelSam -= 2

                show green g18 at ri with d3
                s "Sure, let me get ready."
                hide green with d2
                play sound "audio/sfx/cloth.mp3"
                $ sexScene = 2
                scene black with fade
                pause 0.9
                jump samSex2
        "[sexAct3]" if True:
            if sexAct3 == "???":
                jump sexScenesSam
            elif task5Stage >= 5 and samMood <= 25:
                show green g4 at ri with d3
                s "I'm sorry, I really don't feel like it right now..."
                y "................"
                hide green with d3
                jump samCall
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelSam -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelSam -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelSam -= 5
                elif True:
                    $ nanoLevelSam -= 2

                show green g19 at ri with d3
                s "Well... okay if it helps..."
                hide green with d2
                play sound "audio/sfx/cloth.mp3"
                $ sexScene = 3
                scene black with fade
                pause 0.9
                jump samSex3
        "[sexAct4]" if True:
            if sexAct4 == "???":
                jump sexScenesSam
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelSam -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelSam -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelSam -= 5

                $ sexScene = 1
                jump samSex4
        "[sexAct5]" if True:
            if sexAct5 == "???":
                jump sexScenesSam
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelSam -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelSam -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelSam -= 15
                elif True:
                    $ nanoLevelSam -= 2

                $ sexScene = 1
                jump samSex5
        "[sexAct6]" if True:
            if sexAct6 == "???":
                jump sexScenesSam
            elif True:
                jump foursomeSex
        "Back" if True:
            jump samCall



image modelSamBG = "animations/model/bg.jpg"
default samModelArms = 1
default samModelOutfit = 0
default samModelFace = 5
default samModelBody = 1
default samModelCollar1 = False
default samModelGag1 = False
default samModelBlind1 = False
default samModelPlug = False
default samModelSpread = False
default samModelDildo = False


layeredimage modelSam:
    if samModelPlug:
        "animations/model/sam/plug.png"

    if samModelBody == 1:   
        "animations/model/sam/body1.png"
    if samModelBody == 2:   
        "animations/model/sam/body2.png"
    if samModelBody == 3:   
        "animations/model/sam/body3.png"

    if samModelOutfit == 1:
        "animations/model/sam/out1.png"
    if samModelOutfit == 2:
        "animations/model/sam/out2.png"
    if samModelOutfit == 2.1:
        "animations/model/sam/out2b.png"
    if samModelOutfit == 3:
        "animations/model/sam/out3.png"
    if samModelOutfit == 3.1:
        "animations/model/sam/out3b.png"
    if samModelOutfit == 4:
        "animations/model/sam/out4.png"


    if samModelFace == 1:
        "animations/model/sam/face1.png"
    if samModelFace == 2:
        "animations/model/sam/face2.png"
    if samModelFace == 3:
        "animations/model/sam/face3.png"
    if samModelFace == 4:
        "animations/model/sam/face4.png"
    if samModelFace == 5:
        "animations/model/sam/face5.png"
    if samModelFace == 6:
        "animations/model/sam/face6.png"
    if samModelFace == 7:
        "animations/model/sam/face7.png"
    if samModelFace == 8:
        "animations/model/sam/face8.png"


    if samModelCollar1:
        "animations/model/sam/neck1.png"
    if samModelGag1:
        "animations/model/sam/gag1.png"


    if samModelArms == 1:
        "animations/model/sam/arms1.png"
    if samModelArms == 2:
        "animations/model/sam/arms2.png"
    if samModelArms == 3:
        "animations/model/sam/arms3.png"
    if samModelArms == 4:
        "animations/model/sam/arms4.png"
    if samModelArms == 5:
        "animations/model/sam/arms5.png"

    if samModelBlind1:
        "animations/model/sam/blind.png"
    if samModelSpread and samModelBody == 2:
        "animations/model/sam/spread.png"
    if samModelDildo and samModelBody == 1:
        "animations/model/sam/dildo.png"

label samSex1:
    $ sexScene = 1
    $ aniSpySelect = 1
    $ samModelOutfit = 1
    $ samModelFace = 5
    scene modelSamBG
    with fade
    show modelSam:
        xalign 0.5 yalign 0.5


    call screen nxtPhotoScene




image bgDildoSam1 = "animations/dildo/green/bgDildo1.jpg"
image bgDildoSam2 = "animations/dildo/green/bgDildo2.jpg"
image bgDildoSam3 = "animations/dildo/green/bgDildo3.jpg"
image bgDildoSam4 = "animations/dildo/green/bgDildo4.jpg"
image bgDildoSam5 = "animations/dildo/green/bgDildo4.jpg"

screen progressSexScene2Sam:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartSamSex2")
    key "mouseup_1" action Hide("nonexistent_screen")

label samSex2:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 3

    $ randVid = renpy.random.randint(1, 4)

    show screen progressSexScene2Sam
    label restartSamSex2:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene2Sam
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump samSex2

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgDildoSam1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/green/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/green/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/green/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/green/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgDildoSam2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/green/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/green/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/green/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/green/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgDildoSam3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/green/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/green/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/green/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/green/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgDildoSam4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/green/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/green/4-2.ogv", stop_music=False)
            elif randVid >= 3:
                $ renpy.movie_cutscene("animations/dildo/green/4-3.ogv", stop_music=False)

        if aniStage == 5:
            scene bgDildoSam5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/dildo/green/5-1.ogv", stop_music=False)
                $ aniStage = 6

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 6:
            scene bgDildoSam1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/green/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/green/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/green/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/green/1-4.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene2Sam
            scene bgDildoSam1
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if picQuest6 == 1:
                $ picQuest6 = 2
                show white
                play sound "audio/sfx/camera.mp3"
                pause 0.03
                hide white
                pause 0.5
                play sound "audio/sfx/itemGot.mp3"
                "You collected a photo for the bookstore clerk!"
            jump nightCycle
        jump restartSamSex2
    jump nightCycle


image bgForplaySam1 = "animations/forplay/green/bgForplay1.jpg"
image bgForplaySam2 = "animations/forplay/green/bgForplay2.jpg"
image bgForplaySam3 = "animations/forplay/green/bgForplay3.jpg"
image bgForplaySam4 = "animations/forplay/green/bgForplay4.jpg"
image bgForplaySam5 = "animations/forplay/green/bgForplay5.jpg"
image bgForplaySam6 = "animations/forplay/green/bgForplay6.jpg"

screen progressSexScene3Sam:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartSamSex3")
    key "mouseup_1" action Hide("nonexistent_screen")

label samSex3:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 3

    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene3Sam
    label restartSamSex3:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene3Sam
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump samSex3

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgForplaySam1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/green/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/green/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/green/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/green/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgForplaySam2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/green/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/green/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/green/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/green/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgForplaySam3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/green/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/green/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/green/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/green/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgForplaySam4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/green/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/green/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/green/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/green/4-4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgForplaySam5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/forplay/green/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgForplaySam6
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/green/6-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/green/6-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/green/6-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene3Sam
            scene bgForplaySam6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if picQuest7 == 1:
                $ picQuest7 = 2
                call undressSam from _call_undressSam_13
                show white
                play sound "audio/sfx/camera.mp3"
                pause 0.03
                hide white
                pause 0.5
                play sound "audio/sfx/itemGot.mp3"
                "You collected a photo for the bookstore clerk!"
                scene bgSamCell with fade
                if slutLevel >= 4:
                    show green g1 at ce
                    with fade
                    y "I'm going to show this picture to the bookstore girl."
                    s "That's fine I guess..."
                    s g16 "Is she giving you a reward for it?"
                    y g21 "She sure is. Want to know what it is?"
                    s "Something tells me it's better if I don't know..."
                    hide green with d3
                    jump nightCycle
                elif True:
                    show green g20 at ce
                    with fade
                    s g15 "You're not sharing that with the bookstore clerk, right...?"
                    y "Sure am."
                    s "I... I don't want you."
                    y "..................."
                    s g14 "It's just a little too personal..."
                    y "Really? This is what you're insecure about?"
                    s g39 "Well it's still a very lewd scene! I don't know if I want to start sharing it around. Who knows who's watching..."
                    menu:
                        "Share the photo (-karma)" if True:
                            $ playerKarma -= 2
                            y "Don't want your nudes to leak unto the internet?"
                            s g15 "No..."
                            y "Well too bad. I'm trading this picture at the bookstore."
                            $ greenBlush = 1
                            s g28 "No! [playerName] please!"
                        "Delete the photo" if True:
                            $ picQuest7 = 1
                            y "Fine... I'll delete it..."
                            s g1 "Thanks [playerName]-..."
                    $ greenBlush = 0
                    hide green with d3

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellSam with fade
                        jump sexScenesSam
                    "No" if True:
                        pass
            jump nightCycle
        jump restartSamSex3
    jump nightCycle


image bgSexSam1 = "animations/sex/green/bgSex1.jpg"
image bgSexSam2 = "animations/sex/green/bgSex2.jpg"
image bgSexSam3 = "animations/sex/green/bgSex3.jpg"
image bgSexSam4 = "animations/sex/green/bgSex4.jpg"
image bgSexSam5 = "animations/sex/green/bgSex5.jpg"
image bgSexSam6 = "animations/sex/green/bgSex6.jpg"

screen progressSexScene4Sam:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartSamSex4")
    key "mouseup_1" action Hide("nonexistent_screen")

label samSex4:
    scene bgSexSam1
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 1
    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene4Sam
    label restartSamSex4:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene4Sam
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump samSex4

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgSexSam1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/green/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/green/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/green/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/green/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgSexSam2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/green/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/green/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/green/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/green/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgSexSam3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/green/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/green/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/green/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/green/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgSexSam4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/green/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/green/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/green/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/green/4-4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgSexSam5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/sex/green/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgSexSam6
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/green/6-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/green/6-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/green/6-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene4Sam
            scene bgSexSam6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if picQuest8 == 1:
                $ picQuest8 = 2
                call undressSam from _call_undressSam_14
                show white
                play sound "audio/sfx/camera.mp3"
                pause 0.03
                hide white
                pause 0.5
                play sound "audio/sfx/itemGot.mp3"
                "You collected a photo for the bookstore clerk!"
                scene bgSamCell with fade
                if slutLevel >= 5:
                    show green g1 at ce
                    with fade
                    y "I'm going to show this picture to the bookstore girl."
                    s "If that's what floats her boat..."
                    hide green with d3
                    jump nightCycle
                elif True:
                    show green g20 at ce
                    with fade
                    s "I'm not sure if you should share that..."
                    y "She's already seen you naked. Might aswell, right?"
                    s "There's just something really unsettling, knowing that this picture is being shown to the world!"
                    s "I mean... even if it's just shown to her, she could still lose it..."
                    menu:
                        "Share the photo (-karma)" if True:
                            $ playerKarma -= 2
                            y "I'll be sure to tell her not to lose it then."
                            s "That's not what I mean! Please [playerName]!"
                            hide green with d3
                        "Delete the photo" if True:
                            $ picQuest8 = 1
                            y "Fine... I'll delete it..."
                            s g1 "Thanks [playerName]-..."
                    $ greenBlush = 0
                    hide green with d3

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellSam with fade
                        jump sexScenesSam
                    "No" if True:
                        pass
            jump nightCycle
        jump restartSamSex4
    jump nightCycle


image bgAnalSam1 = "animations/anal/green/bgAnal1.jpg"
image bgAnalSam2 = "animations/anal/green/bgAnal2.jpg"
image bgAnalSam3 = "animations/anal/green/bgAnal3.jpg"
image bgAnalSam4 = "animations/anal/green/bgAnal4.jpg"
image bgAnalSam5 = "animations/anal/green/bgAnal5.jpg"
image bgAnalSam6 = "animations/anal/green/bgAnal6.jpg"

screen progressSexScene5Sam:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartSamSex5")
    key "mouseup_1" action Hide("nonexistent_screen")

label samSex5:
    "Progress anal scene by pressing SPACE."
    scene bgAnalSam1
    $ aniSpySelect = 1
    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene5Sam
    label restartSamSex5:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene5Sam
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump samSex5

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgAnalSam1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/anal/green/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/anal/green/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/anal/green/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/anal/green/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgAnalSam2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/anal/green/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/anal/green/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/anal/green/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/anal/green/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgAnalSam3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/anal/green/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/anal/green/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/anal/green/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/anal/green/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgAnalSam4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/anal/green/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/anal/green/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/anal/green/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/anal/green/4-4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgAnalSam5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/anal/green/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgAnalSam6
            if randVid == 1:
                $ renpy.movie_cutscene("animations/anal/green/6-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/anal/green/6-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/anal/green/6-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene5Sam
            scene bgAnalSam6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if task26Stage == 5:
                jump task26
            if picQuest9 == 1:
                $ picQuest9 = 2
                call undressSam from _call_undressSam_26
                show white
                play sound "audio/sfx/camera.mp3"
                pause 0.03
                hide white
                pause 0.5
                play sound "audio/sfx/itemGot.mp3"
                "You collected a photo for the bookstore clerk!"
                scene bgSamCell with fade
                if slutLevel >= 5:
                    show green g1 at ce
                    with fade
                    y "One more picture in the bag!"
                    s g16 "Is that girl some sort of sex freak or something...?"
                    y "No more than you, you slut."
                    s g28 "O-oh...!"
                    $ greenBlush = 1
                    s g48 "Heh~..."
                    hide green with d3
                    $ greenBlush = 0

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellSam with fade
                        jump sexScenesSam
                    "No" if True:
                        pass
            jump nightCycle
        jump restartSamSex5
    jump nightCycle





image bgDildo2 = "animations/dildo/red/bgDildo.jpg"

image dildoCloverSce1Var1 movie = Movie(play="animations/dildo/red/1-1.ogv", loop=False)
image dildoCloverSce1Var2 movie = Movie(play="animations/dildo/red/1-2.ogv", loop=False)
image dildoCloverSce1Var3 movie = Movie(play="animations/dildo/red/1-3.ogv", loop=False)
image dildoCloverSce1Var4 movie = Movie(play="animations/dildo/red/1-4.ogv", loop=False)

image dildoCloverSce2Var1 movie = Movie(play="animations/dildo/red/2-1.ogv", loop=False)
image dildoCloverSce2Var2 movie = Movie(play="animations/dildo/red/2-2.ogv", loop=False)
image dildoCloverSce2Var3 movie = Movie(play="animations/dildo/red/2-3.ogv", loop=False)
image dildoCloverSce2Var4 movie = Movie(play="animations/dildo/red/2-4.ogv", loop=False)

image dildoCloverSce3Var1 movie = Movie(play="animations/dildo/red/3-1.ogv", loop=False)
image dildoCloverSce3Var2 movie = Movie(play="animations/dildo/red/3-2.ogv", loop=False)
image dildoCloverSce3Var3 movie = Movie(play="animations/dildo/red/3-3.ogv", loop=False)
image dildoCloverSce3Var4 movie = Movie(play="animations/dildo/red/3-4.ogv", loop=False)

image dildoCloverSce4Var1 movie = Movie(play="animations/dildo/red/4-1.ogv", loop=False)
image dildoCloverSce4Var2 movie = Movie(play="animations/dildo/red/4-2.ogv", loop=False)
image dildoCloverSce4Var3 movie = Movie(play="animations/dildo/red/4-3.ogv", loop=False)

image dildoCloverSce5Var1 movie = Movie(play="animations/dildo/red/5-1.ogv", loop=False)


image bgForplay2 = "animations/forplay/red/bgForplay.jpg"

label sexScenesClover:
    hide screen nanoLevelClover
    menu:
        "!!! Emergency suppression !!!" if nanoLevelClover == 100:
            $ nanoLevelClover = 50
            show scene_darkening with d3
            show red r100 at ri with d3
            c "{b}*Growls*{/b}"
            y "Uh oh! Looks like we need to 'seriously' have your nanobots suppressed tonight!"
            hide red
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            "You jump Clover and tie her to the bed."
            c "!!!"
            hide scene_darkening with d3
            $ spyRoomRand = 11
            with d3
            y "There we go. You stay there until you're back to your normal self."
            c "{b}*Moans*{/b}"
            jump cloverCall
        "[sexAct1]" if True:
            if sexAct1 == "???":
                jump sexScenesClover
            elif True:
                $ sexScene = 1
                jump cloverSex1
        "[sexAct2]" if True:
            if sexAct2 == "???":
                jump sexScenesClover
            elif task5Stage >= 5 and cloverMood <= 25:
                show red r4 at ri with d3
                c "I'm sorry, I really don't feel like it right now..."
                y "................"
                hide red with d3
                jump cloverCall
            elif 5 <= task5Stage <= 7 and cloverMood >= 26:

                if slutLevel <= 1:
                    $ nanoLevelClover -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelClover -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelClover -= 5
                elif True:
                    $ nanoLevelClover -= 2

                $ sexScene = 2
                $ cloverSpySex = 2
                show red r38 at ri with d3
                c "Let's take this baby for a spin~....{w} Oh you're still here?"
                y "......................"
                hide red
                scene bgBase
                with fade
                jump base
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelClover -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelClover -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelClover -= 5
                elif True:
                    $ nanoLevelClover -= 2

                show red r18 at ri with d3
                c "Well don't mind if I do~..."
                hide red with d2
                play sound "audio/sfx/cloth.mp3"
                $ sexScene = 2
                scene black with fade
                pause 0.9
                jump cloverSex2
        "[sexAct3]" if True:
            if sexAct3 == "???":
                jump sexScenesClover
            elif task5Stage >= 5 and cloverMood <= 25:
                show red r4 at ri with d3
                c "I'm sorry, I really don't feel like it right now..."
                y "................"
                hide red with d3
                jump cloverCall
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelClover -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelClover -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelClover -= 5
                elif True:
                    $ nanoLevelClover -= 2

                show red r22 at ri with d3
                c "Well then, let's see if I can beat my personal record~..."
                hide red with d2
                play sound "audio/sfx/cloth.mp3"
                $ sexScene = 3
                scene black with fade
                pause 0.9
                jump cloverSex3
        "[sexAct4]" if True:
            if sexAct4 == "???":
                jump sexScenesClover
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelClover -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelClover -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelClover -= 5

                jump cloverSex4
        "[sexAct5]" if True:
            if sexAct5 == "???":
                jump sexScenesClover
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelClover -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelClover -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelClover -= 15
                elif True:
                    $ nanoLevelClover -= 2

                jump cloverSex5
        "[sexAct6]" if True:
            if sexAct6 == "???":
                jump sexScenesClover
            elif True:
                jump foursomeSex
        "Back" if True:
            jump cloverCall


image modelCloverBG = "animations/model/clover/bg.jpg"
default cloverModelArms = 1
default cloverModelOutfit = 0
default cloverModelFace = 5
default cloverModelBody = 1
default cloverModelCollar1 = False
default cloverModelGag1 = False
default cloverModelBlind1 = False
default cloverModelPlug = False
default cloverModelSpread = False
default cloverModelDildo = False


layeredimage modelClover:
    if cloverModelPlug:
        "animations/model/clover/plug.png"

    if cloverModelBody == 1:   
        "animations/model/clover/body1.png"
    if cloverModelBody == 2:   
        "animations/model/clover/body2.png"
    if cloverModelBody == 3:   
        "animations/model/clover/body3.png"

    if cloverModelOutfit == 1:
        "animations/model/clover/out1.png"
    if cloverModelOutfit == 2:
        "animations/model/clover/out2.png"
    if cloverModelOutfit == 2.1:
        "animations/model/clover/out2b.png"
    if cloverModelOutfit == 3:
        "animations/model/clover/out3.png"
    if cloverModelOutfit == 3.1:
        "animations/model/clover/out3b.png"
    if cloverModelOutfit == 4:
        "animations/model/clover/out4.png"


    if cloverModelFace == 1:
        "animations/model/clover/face1.png"
    if cloverModelFace == 2:
        "animations/model/clover/face2.png"
    if cloverModelFace == 3:
        "animations/model/clover/face3.png"
    if cloverModelFace == 4:
        "animations/model/clover/face4.png"
    if cloverModelFace == 5:
        "animations/model/clover/face5.png"
    if cloverModelFace == 6:
        "animations/model/clover/face6.png"
    if cloverModelFace == 7:
        "animations/model/clover/face7.png"
    if cloverModelFace == 8:
        "animations/model/clover/face8.png"


    if cloverModelCollar1:
        "animations/model/clover/neck1.png"
    if cloverModelGag1:
        "animations/model/clover/gag1.png"


    if cloverModelArms == 1:
        "animations/model/clover/arms1.png"
    if cloverModelArms == 2:
        "animations/model/clover/arms2.png"
    if cloverModelArms == 3:
        "animations/model/clover/arms3.png"
    if cloverModelArms == 4:
        "animations/model/clover/arms4.png"
    if cloverModelArms == 5:
        "animations/model/clover/arms5.png"

    if cloverModelBlind1:
        "animations/model/clover/blind.png"
    if cloverModelSpread and cloverModelBody == 2:
        "animations/model/clover/spread.png"
    if cloverModelDildo and cloverModelBody == 1:
        "animations/model/clover/dildo.png"

label cloverSex1:
    $ sexScene = 1
    $ aniSpySelect = 2
    $ cloverModelOutfit = 1
    $ cloverModelFace = 5
    scene modelSamBG
    with fade
    show modelClover:
        xalign 0.5 yalign 0.5
    call screen nxtPhotoScene


image bgDildoClover = "animations/dildo/red/bgDildo.jpg"

screen progressSexScene2Clover:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartCloverSex2")
    key "mouseup_1" action Hide("nonexistent_screen")

label cloverSex2:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 2
    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene2Clover
    label restartCloverSex2:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene4Clover
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump cloverSex2

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgDildoClover
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/red/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/red/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/red/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/red/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgDildoClover
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/red/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/red/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/red/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/red/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgDildoClover
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/red/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/red/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/red/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/red/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgDildoClover
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/red/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/red/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/red/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/red/4-3.ogv", stop_music=False)

        if aniStage == 5:
            scene bgDildoClover
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/dildo/red/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgDildoClover
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/red/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/red/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/red/1-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene2Clover
            scene bgDildoClover
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if picQuest6 == 1:
                $ picQuest6 = 2
                show white
                play sound "audio/sfx/camera.mp3"
                pause 0.03
                hide white
                pause 0.5
                play sound "audio/sfx/itemGot.mp3"
                "You collected a photo for the bookstore clerk!"
            jump nightCycle
        jump restartCloverSex2
    jump nightCycle


image bgForplayClover1 = "animations/forplay/red/bgForplay1.jpg"
image bgForplayClover2 = "animations/forplay/red/bgForplay2.jpg"
image bgForplayClover3 = "animations/forplay/red/bgForplay3.jpg"
image bgForplayClover4 = "animations/forplay/red/bgForplay4.jpg"
image bgForplayClover5 = "animations/forplay/red/bgForplay5.jpg"
image bgForplayClover6 = "animations/forplay/red/bgForplay6.jpg"

screen progressSexScene3Clover:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartCloverSex3")
    key "mouseup_1" action Hide("nonexistent_screen")

label cloverSex3:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 2

    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene3Clover
    label restartCloverSex3:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene3Clover
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump cloverSex3

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgForplayClover1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/red/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/red/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/red/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/red/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgForplayClover2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/red/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/red/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/red/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/red/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgForplayClover3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/red/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/red/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/red/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/red/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgForplayClover4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/red/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/red/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/red/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/red/4-4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgForplayClover5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/forplay/red/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgForplayClover6
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/red/6-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/red/6-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/red/6-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene3Clover
            scene bgForplayClover6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellClover with fade
                        jump sexScenesClover
                    "No" if True:
                        pass
            jump nightCycle
        jump restartCloverSex3
    jump nightCycle


image bgSexClover1 = "animations/sex/red/bgSex1.jpg"
image bgSexClover2 = "animations/sex/red/bgSex2.jpg"
image bgSexClover3 = "animations/sex/red/bgSex3.jpg"
image bgSexClover4 = "animations/sex/red/bgSex4.jpg"
image bgSexClover5 = "animations/sex/red/bgSex5.jpg"
image bgSexClover6 = "animations/sex/red/bgSex6.jpg"

screen progressSexScene4Clover:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartCloverSex4")
    key "mouseup_1" action Hide("nonexistent_screen")

label cloverSex4:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 1
    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene4Clover
    label restartCloverSex4:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene4Clover
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump cloverSex4

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgSexClover1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/red/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/red/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/red/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/red/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgSexClover2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/red/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/red/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/red/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/red/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgSexClover3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/red/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/red/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/red/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/red/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgSexClover4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/red/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/red/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/red/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/red/4-3.ogv", stop_music=False)

        if aniStage == 5:
            scene bgSexClover5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/sex/red/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgSexClover6
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/red/6-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/red/6-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/red/6-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene4Clover
            scene bgSexClover6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellClover with fade
                        jump sexScenesClover
                    "No" if True:
                        pass
            jump nightCycle
        jump restartCloverSex4
    jump nightCycle


image bgAnalClover1 = "animations/anal/red/bgAnal1.jpg"
image bgAnalClover2 = "animations/anal/red/bgAnal1.jpg"
image bgAnalClover3 = "animations/anal/red/bgAnal1.jpg"
image bgAnalClover4 = "animations/anal/red/bgAnal1.jpg"
image bgAnalClover5 = "animations/anal/red/bgAnal1.jpg"
image bgAnalClover6 = "animations/anal/red/bgAnal1.jpg"

screen progressSexScene5Clover:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartCloverSex5")
    key "mouseup_1" action Hide("nonexistent_screen")

label cloverSex5:
    "Progress anal scene by pressing SPACE."
    scene bgAnalClover1
    $ aniSpySelect = 1
    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene5Clover
    label restartCloverSex5:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene5Clover
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump cloverSex5

        if aniStage == 1:
            scene bgAnalClover1
            $ renpy.movie_cutscene("animations/anal/red/1.ogv", stop_music=False)

        if aniStage == 2:
            scene bgAnalClover2
            $ renpy.movie_cutscene("animations/anal/red/2.ogv", stop_music=False)

        if aniStage == 3:
            scene bgAnalClover3
            $ renpy.movie_cutscene("animations/anal/red/3.ogv", stop_music=False)

        if aniStage == 4:
            scene bgAnalClover4
            $ renpy.movie_cutscene("animations/anal/red/4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgAnalClover5
            $ renpy.movie_cutscene("animations/anal/red/5.ogv", stop_music=False)
            $ aniStage = 6

        if aniStage == 6:
            scene bgAnalClover6
            $ renpy.movie_cutscene("animations/anal/red/6.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene5Clover
            scene bgAnalClover6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if task26Stage == 5:
                jump task26

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellClover with fade
                        jump sexScenesClover
                    "No" if True:
                        pass
            jump nightCycle
        jump restartCloverSex5
    jump nightCycle






label sexScenesAlex:
    hide screen nanoLevelAlex
    menu:
        "!!! Emergency suppression !!!" if nanoLevelAlex == 100:
            $ nanoLevelAlex = 50
            show scene_darkening with d3
            show yellow y100 at ri with d3
            a "{b}*Growls*{/b}"
            y "Uh oh! Looks like we need to 'seriously' have your nanobots suppressed tonight!"
            hide yellow
            play sound "audio/sfx/punch1.mp3"
            with hpunch
            "You jump Alex and tie her to the bed."
            a "!!!"
            hide scene_darkening with d3
            $ spyRoomRand = 11
            with d3
            y "There we go. You stay there until you're back to your normal self."
            a "{b}*Moans*{/b}"
            jump alexCall
        "[sexAct1]" if True:
            if sexAct1 == "???":
                jump sexScenesAlex
            elif True:
                jump alexSex1
        "[sexAct2]" if True:
            if sexAct2 == "???":
                jump sexScenesAlex
            elif task5Stage >= 5 and alexMood <= 25:
                show yellow y4 at ri with d3
                a "I'm sorry, I really don't feel like it right now..."
                y "................"
                hide yellow with d3
                jump alexCall
            elif 5 <= task5Stage <= 7 and alexMood >= 26:

                if slutLevel <= 1:
                    $ nanoLevelAlex -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelAlex -= 10
                if 4 <= slutLevel <= 5:
                    $ nanoLevelAlex -= 5
                elif True:
                    $ nanoLevelAlex -= 2

                $ sexScene = 2
                $ alexSpySex = 2
                show yellow y38 at ri with d3
                a "Well... all right. Which side is up again...? Oh, and don't be silly, you can't stay to watch!"
                y "......................"
                hide yellow
                scene bgBase
                with fade
                jump base
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelAlex -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelAlex -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelAlex -= 5
                elif True:
                    $ nanoLevelAlex -= 2

                show yellow y18 at ri with d3
                a "It's time to get naughty!"
                hide yellow with d2
                play sound "audio/sfx/cloth.mp3"
                $ sexScene = 2
                scene black with fade
                pause 0.9
                jump alexSex2
        "[sexAct3]" if True:
            if sexAct3 == "???":
                jump sexScenesAlex
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelAlex -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelAlex -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelAlex -= 5
                elif True:
                    $ nanoLevelAlex -= 2

                show yellow y1 at ri with d3
                a "Butt time! Time to get naked!"
                stop music fadeout 3.0
                hide yellow with d2
                play sound "audio/sfx/cloth.mp3"
                $ sexScene = 3
                scene black with fade
                pause 0.9
                jump alexSex3
        "[sexAct4]" if True:
            if sexAct4 == "???":
                jump sexScenesAlex
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelAlex -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelAlex -= 10
                if 4 <= slutLevel <= 5:
                    $ nanoLevelAlex -= 5

                jump alexSex4
        "[sexAct5]" if True:
            if sexAct5 == "???":
                jump sexScenesAlex
            elif True:

                if slutLevel <= 1:
                    $ nanoLevelAlex -= 20
                if 2 <= slutLevel <= 3:
                    $ nanoLevelAlex -= 10
                if 4 <= slutLevel <= 6:
                    $ nanoLevelAlex -= 15
                elif True:
                    $ nanoLevelAlex -= 2

                jump alexSex5
        "[sexAct6]" if True:
            if sexAct6 == "???":
                jump sexScenesAlex
            elif True:
                jump foursomeSex
        "Back" if True:
            jump alexCall

image modelAlexBG = "animations/model/bg.jpg"
default alexModelArms = 1
default alexModelOutfit = 0
default alexModelFace = 5
default alexModelBody = 1
default alexModelCollar1 = False
default alexModelGag1 = False
default alexModelBlind1 = False
default alexModelPlug = False
default alexModelSpread = False
default alexModelDildo = False


layeredimage modelAlex:
    if alexModelPlug:
        "animations/model/alex/plug.png"

    if alexModelBody == 1:   
        "animations/model/alex/body1.png"
    if alexModelBody == 2:   
        "animations/model/alex/body2.png"
    if alexModelBody == 3:   
        "animations/model/alex/body3.png"

    if alexModelOutfit == 1:
        "animations/model/alex/out1.png"
    if alexModelOutfit == 2:
        "animations/model/alex/out2.png"
    if alexModelOutfit == 2.1:
        "animations/model/alex/out2b.png"
    if alexModelOutfit == 3:
        "animations/model/alex/out3.png"
    if alexModelOutfit == 3.1:
        "animations/model/alex/out3b.png"
    if alexModelOutfit == 4:
        "animations/model/alex/out4.png"


    if alexModelFace == 1:
        "animations/model/alex/face1.png"
    if alexModelFace == 2:
        "animations/model/alex/face2.png"
    if alexModelFace == 3:
        "animations/model/alex/face3.png"
    if alexModelFace == 4:
        "animations/model/alex/face4.png"
    if alexModelFace == 5:
        "animations/model/alex/face5.png"
    if alexModelFace == 6:
        "animations/model/alex/face6.png"
    if alexModelFace == 7:
        "animations/model/alex/face7.png"
    if alexModelFace == 8:
        "animations/model/alex/face8.png"


    if alexModelCollar1:
        "animations/model/alex/neck1.png"
    if alexModelGag1:
        "animations/model/alex/gag1.png"


    if alexModelArms == 1:
        "animations/model/alex/arms1.png"
    if alexModelArms == 2:
        "animations/model/alex/arms2.png"
    if alexModelArms == 3:
        "animations/model/alex/arms3.png"
    if alexModelArms == 4:
        "animations/model/alex/arms4.png"
    if alexModelArms == 5:
        "animations/model/alex/arms5.png"

    if alexModelBlind1:
        "animations/model/alex/blind.png"
    if alexModelSpread and alexModelBody == 2:
        "animations/model/alex/spread.png"
    if alexModelDildo and alexModelBody == 1:
        "animations/model/alex/dildo.png"


label alexSex1:
    $ sexScene = 1
    $ aniSpySelect = 3
    $ alexModelOutfit = 1
    $ alexModelFace = 5
    scene modelAlexBG
    with fade
    show modelAlex:
        xalign 0.44 yalign 0.5


    call screen nxtPhotoScene



screen progressSexScene2Alex:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartAlexSex2")
    key "mouseup_1" action Hide("nonexistent_screen")

image bgDildo3 = "animations/dildo/yellow/bgDildo.jpg"
image dildoAlexSce1Var1 movie = Movie(play="animations/dildo/yellow/1-1.ogv", loop=False)
image dildoAlexSce1Var2 movie = Movie(play="animations/dildo/yellow/1-2.ogv", loop=False)
image dildoAlexSce1Var3 movie = Movie(play="animations/dildo/yellow/1-3.ogv", loop=False)
image dildoAlexSce1Var4 movie = Movie(play="animations/dildo/yellow/1-4.ogv", loop=False)

image dildoAlexSce2Var1 movie = Movie(play="animations/dildo/yellow/2-1.ogv", loop=False)
image dildoAlexSce2Var2 movie = Movie(play="animations/dildo/yellow/2-2.ogv", loop=False)
image dildoAlexSce2Var3 movie = Movie(play="animations/dildo/yellow/2-3.ogv", loop=False)
image dildoAlexSce2Var4 movie = Movie(play="animations/dildo/yellow/2-4.ogv", loop=False)

image dildoAlexSce3Var1 movie = Movie(play="animations/dildo/yellow/3-1.ogv", loop=False)
image dildoAlexSce3Var2 movie = Movie(play="animations/dildo/yellow/3-2.ogv", loop=False)
image dildoAlexSce3Var3 movie = Movie(play="animations/dildo/yellow/3-3.ogv", loop=False)
image dildoAlexSce3Var4 movie = Movie(play="animations/dildo/yellow/3-4.ogv", loop=False)

image dildoAlexSce4Var1 movie = Movie(play="animations/dildo/yellow/4-1.ogv", loop=False)
image dildoAlexSce4Var2 movie = Movie(play="animations/dildo/yellow/4-2.ogv", loop=False)
image dildoAlexSce4Var3 movie = Movie(play="animations/dildo/yellow/4-3.ogv", loop=False)

image dildoAlexSce5Var1 movie = Movie(play="animations/dildo/yellow/5-1.ogv", loop=False)

label alexSex2:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 3
    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene2Alex
    label restartAlexSex2:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene2Alex
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump alexSex2

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgDildo3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/yellow/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/yellow/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/yellow/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/yellow/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgDildo3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/yellow/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/yellow/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/yellow/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/yellow/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgDildo3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/yellow/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/yellow/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/yellow/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/yellow/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgDildo3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/yellow/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/yellow/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/yellow/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/dildo/yellow/4-3.ogv", stop_music=False)

        if aniStage == 5:
            scene bgDildo3
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/dildo/yellow/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgDildo3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/dildo/yellow/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/dildo/yellow/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/dildo/yellow/1-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene2Alex
            scene bgDildo3
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if picQuest6 == 1:
                $ picQuest6 = 2
                show white
                play sound "audio/sfx/camera.mp3"
                pause 0.03
                hide white
                pause 0.5
                play sound "audio/sfx/itemGot.mp3"
                "You collected a photo for the bookstore clerk!"
            jump nightCycle
        jump restartAlexSex2
    jump nightCycle


image bgForplayAlex1 = "animations/forplay/yellow/bgForplay1.jpg"
image bgForplayAlex2 = "animations/forplay/yellow/bgForplay2.jpg"
image bgForplayAlex3 = "animations/forplay/yellow/bgForplay3.jpg"
image bgForplayAlex4 = "animations/forplay/yellow/bgForplay4.jpg"
image bgForplayAlex5 = "animations/forplay/yellow/bgForplay5.jpg"
image bgForplayAlex6 = "animations/forplay/yellow/bgForplay6.jpg"

screen progressSexScene3Alex:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartAlexSex3")
    key "mouseup_1" action Hide("nonexistent_screen")

label alexSex3:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 3

    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene3Alex
    label restartAlexSex3:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene3Alex
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump alexSex3

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgForplayAlex1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/yellow/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/yellow/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/yellow/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/yellow/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgForplayAlex2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/yellow/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/yellow/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/yellow/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/yellow/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgForplayAlex3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/yellow/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/yellow/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/yellow/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/yellow/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgForplayAlex4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/yellow/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/yellow/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/yellow/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/forplay/yellow/4-4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgForplayAlex5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/forplay/yellow/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgForplayAlex6
            if randVid == 1:
                $ renpy.movie_cutscene("animations/forplay/yellow/6-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/forplay/yellow/6-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/forplay/yellow/6-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene3Alex
            scene bgForplayAlex6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellAlex with fade
                        jump sexScenesAlex
                    "No" if True:
                        pass
            jump nightCycle
        jump restartAlexSex3
    jump nightCycle


image bgSexAlex1 = "animations/sex/yellow/bgSex1.jpg"
image bgSexAlex2 = "animations/sex/yellow/bgSex2.jpg"
image bgSexAlex3 = "animations/sex/yellow/bgSex3.jpg"
image bgSexAlex4 = "animations/sex/yellow/bgSex4.jpg"
image bgSexAlex5 = "animations/sex/yellow/bgSex5.jpg"
image bgSexAlex6 = "animations/sex/yellow/bgSex6.jpg"

screen progressSexScene4Alex:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartAlexSex4")
    key "mouseup_1" action Hide("nonexistent_screen")

label alexSex4:
    "Progress sex scene by pressing SPACE."
    $ aniSpySelect = 3

    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene4Alex
    label restartAlexSex4:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene4Alex
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump alexSex4

        $ randVid = renpy.random.randint(1, 4)
        if aniStage == 1:
            scene bgSexAlex1
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/yellow/1-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/yellow/1-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/yellow/1-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/yellow/1-4.ogv", stop_music=False)

        if aniStage == 2:
            scene bgSexAlex2
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/yellow/2-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/yellow/2-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/yellow/2-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/yellow/2-4.ogv", stop_music=False)

        if aniStage == 3:
            scene bgSexAlex3
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/yellow/3-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/yellow/3-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/yellow/3-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/yellow/3-4.ogv", stop_music=False)

        if aniStage == 4:
            scene bgSexAlex4
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/yellow/4-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/yellow/4-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/yellow/4-3.ogv", stop_music=False)
            elif randVid == 4:
                $ renpy.movie_cutscene("animations/sex/yellow/4-4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgSexAlex5
            if randVid >= 1:
                $ renpy.movie_cutscene("animations/sex/yellow/5-1.ogv", stop_music=False)
                $ aniStage = 6

        if aniStage == 6:
            scene bgSexAlex6
            if randVid == 1:
                $ renpy.movie_cutscene("animations/sex/yellow/6-1.ogv", stop_music=False)
            elif randVid == 2:
                $ renpy.movie_cutscene("animations/sex/yellow/6-2.ogv", stop_music=False)
            elif randVid == 3:
                $ renpy.movie_cutscene("animations/sex/yellow/6-3.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene4Alex
            scene bgSexAlex6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellAlex with fade
                        jump sexScenesAlex
                    "No" if True:
                        pass
            jump nightCycle
        jump restartAlexSex4
    jump nightCycle



image bgAnalAlex1 = "animations/anal/yellow/bgAnal1.jpg"
image bgAnalAlex2 = "animations/anal/yellow/bgAnal1.jpg"
image bgAnalAlex3 = "animations/anal/yellow/bgAnal1.jpg"
image bgAnalAlex4 = "animations/anal/yellow/bgAnal1.jpg"
image bgAnalAlex5 = "animations/anal/yellow/bgAnal1.jpg"
image bgAnalAlex6 = "animations/anal/yellow/bgAnal1.jpg"

screen progressSexScene5Alex:
    key "K_SPACE" action SetVariable("aniStage", aniStage + 1), Jump("restartAlexSex5")
    key "mouseup_1" action Hide("nonexistent_screen")

label alexSex5:
    "Progress anal scene by pressing SPACE."
    scene bgAnalAlex1
    $ aniSpySelect = 1
    $ randVid = renpy.random.randint(1, 4)
    show screen progressSexScene5Alex
    label restartAlexSex5:
        $ loopProtection += 1
        if loopProtection >= 200:
            hide screen progressSexScene5Alex
            $ loopProtection = 0
            $ aniStage = 1
            y "Ngh~...!"
            jump alexSex5

        if aniStage == 1:
            scene bgAnalAlex1
            $ renpy.movie_cutscene("animations/anal/yellow/1.ogv", stop_music=False)

        if aniStage == 2:
            scene bgAnalAlex2
            $ renpy.movie_cutscene("animations/anal/yellow/2.ogv", stop_music=False)

        if aniStage == 3:
            scene bgAnalAlex3
            $ renpy.movie_cutscene("animations/anal/yellow/3.ogv", stop_music=False)

        if aniStage == 4:
            scene bgAnalAlex4
            $ renpy.movie_cutscene("animations/anal/yellow/4.ogv", stop_music=False)

        if aniStage == 5:
            scene bgAnalAlex5
            $ renpy.movie_cutscene("animations/anal/yellow/5.ogv", stop_music=False)
            $ aniStage = 6

        if aniStage == 6:
            scene bgAnalAlex6
            $ renpy.movie_cutscene("animations/anal/yellow/6.ogv", stop_music=False)
        if aniStage == 7:
            hide screen progressSexScene5Alex
            scene bgAnalAlex6
            hide movie with fade
            stop movie
            $ aniStage = 1
            $ loopProtection = 0
            if task26Stage == 5:
                jump task26

            if medPills >= 1:
                scene black with fade
                "You have vigor pills. Want to use one?"
                menu:
                    "Yes (-1 Vigor Pill)" if True:
                        y "{b}*Gulp*{/b}"
                        "You feel reinvigorated!"
                        scene cellAlex with fade
                        jump sexScenesAlex
                    "No" if True:
                        pass
            jump nightCycle
        jump restartAlexSex5
    jump nightCycle



default foursomeStage = 1
default foursomePlayer = 1
default foursomeAction = ""

screen foursomeInteract:
    vbox xalign 0.04 yalign 0.1:
        imagebutton:
            idle "animations/4//foursomePlayerSam.png"
            hover "animations/4//foursomePlayerSam-hover.png"
            action SetVariable("foursomePlayer", 1), Jump("foursomeSex")
    vbox xalign 0.04 yalign 0.2:
        imagebutton:
            idle "animations/4//foursomePlayerClover.png"
            hover "animations/4//foursomePlayerClover-hover.png"
            action SetVariable("foursomePlayer", 2), Jump("foursomeSex")
    vbox xalign 0.04 yalign 0.3:
        imagebutton:
            idle "animations/4//foursomePlayerAlex.png"
            hover "animations/4//foursomePlayerAlex-hover.png"
            action SetVariable("foursomePlayer", 3), Jump("foursomeSex")

    if foursomePlayer == 1:
        vbox xalign 0.11 yalign 0.11:
            imagebutton:
                idle "animations/4/fourPussyBut.png"
                hover "animations/4/fourPussyBut-hover.png"
                action SetVariable("foursomeAction", "vag"), SetVariable("foursomeStage", 2), Jump("foursomeSex")
        vbox xalign 0.15 yalign 0.11:
            imagebutton:
                idle "animations/4/fourAnalBut.png"
                hover "animations/4/fourAnalBut-hover.png"
                action SetVariable("foursomeAction", "anal"), SetVariable("foursomeStage", 2), Jump("foursomeSex")
    if foursomePlayer == 2:
        vbox xalign 0.11 yalign 0.21:
            imagebutton:
                idle "animations/4/fourPussyBut.png"
                hover "animations/4/fourPussyBut-hover.png"
                action SetVariable("foursomeAction", "vag"), SetVariable("foursomeStage", 2), Jump("foursomeSex")
        vbox xalign 0.15 yalign 0.21:
            imagebutton:
                idle "animations/4/fourAnalBut.png"
                hover "animations/4/fourAnalBut-hover.png"
                action SetVariable("foursomeAction", "anal"), SetVariable("foursomeStage", 2), Jump("foursomeSex")
    if foursomePlayer == 3:
        vbox xalign 0.11 yalign 0.31:
            imagebutton:
                idle "animations/4/fourPussyBut.png"
                hover "animations/4/fourPussyBut-hover.png"
                action SetVariable("foursomeAction", "vag"), SetVariable("foursomeStage", 2), Jump("foursomeSex")
        vbox xalign 0.15 yalign 0.31:
            imagebutton:
                idle "animations/4/fourAnalBut.png"
                hover "animations/4/fourAnalBut-hover.png"
                action SetVariable("foursomeAction", "anal"), SetVariable("foursomeStage", 2), Jump("foursomeSex")
    vbox xalign 0.05 yalign 0.41:
        imagebutton:
            idle "animations/4/fourNutBut.png"
            hover "animations/4/fourNutBut-hover.png"
            action SetVariable("foursomeAction", "cum"), SetVariable("foursomeStage", 3),  Jump("foursomeSex")

image bg41 = "animations/4/bg41.jpg"
image bg42 = "animations/4/bg42.jpg"

image fourStage1 movie = Movie(play="animations/4/stage1.webm")


image samPusStage2 movie = Movie(play="animations/4/samPusStage2.webm")
image samAnalStage2 movie = Movie(play="animations/4/samAnalStage2.webm")


image cloverPusStage2 movie = Movie(play="animations/4/cloverPusStage2.webm")
image cloverAnalStage2 movie = Movie(play="animations/4/cloverAnalStage2.webm")


image alexPusStage2 movie = Movie(play="animations/4/alexPusStage2.webm")
image alexAnalStage2 movie = Movie(play="animations/4/alexAnalStage2.webm")


image fourClimax movie = Movie(play="animations/4/climax.webm")

label foursomeSex:
    stop music fadeout 1.0
    scene bg41
    if foursomeStage == 1:
        show fourStage1 movie
    if foursomeStage == 2:
        if foursomeAction == "vag":
            if foursomePlayer == 1:
                show samPusStage2 movie
            elif foursomePlayer == 2:
                show cloverPusStage2 movie
            elif foursomePlayer == 3:
                show alexPusStage2 movie
        if foursomeAction == "anal":
            if foursomePlayer == 1:
                show samAnalStage2 movie
            if foursomePlayer == 2:
                show cloverAnalStage2 movie
            if foursomePlayer == 3:
                show alexAnalStage2 movie
    if foursomeStage == 3:

        $ nanoLevelSam -= 14
        $ nanoLevelClover -= 14
        $ nanoLevelAlex -= 14
        hide screen foursomeInteract
        show fourClimax movie
        $ renpy.pause(9.0, hard='True')
        hide fourClimax movie
        scene bg42
        pause 0.3
        if picQuest10 == 1:
            $ picQuest10 = 2
            call undressSam from _call_undressSam_36
            show white
            play sound "audio/sfx/camera.mp3"
            pause 0.03
            hide white
            pause 0.5
            play sound "audio/sfx/itemGot.mp3"
            "You collected a photo for the bookstore clerk!"
        scene black with fade
        $ foursomeStage = 1
        jump nightCycle
    call screen foursomeInteract

label devAniTest:
    stop music
    scene black
    menu:
        "Animation Sam (DEV)" if True:
            ""
        "Animation Alex (DEV)" if True:
            ""
        "Never mind (jump nightcycle)" if True:
            jump nightCycle
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
