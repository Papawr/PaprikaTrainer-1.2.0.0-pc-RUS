













define config.name = _("Paprika Trainer")





define gui.show_name = True




define config.version = "1.2.0.0"





define gui.about = _p("""
""")






define build.name = "PaprikaTrainer"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True






























define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "hide"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.0001)







default preferences.text_cps = 45





default preferences.afm_time = 15
















define config.save_directory = "PaprikaTrainer2-1545125197"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)





    build.classify('game/bgs/**.png', 'archive')
    build.classify('game/gui/**.png', 'archive')
    build.classify('game/mission/**.png', 'archive')
    build.classify('game/models/**.png', 'archive')
    build.classify('game/bgs/**.jpg', 'archive')
    build.classify('game/gui/**.jpg', 'archive')
    build.classify('game/mission/**.jpg', 'archive')
    build.classify('game/models/**.jpg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpt', 'archive')
    build.classify('game/**.ogv', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')



















define config.layers = [ 'master', 'transient', 'decor', 'screens', 'minigame', 'overlay' ]

init -1:
    python hide:
        config.developer = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
