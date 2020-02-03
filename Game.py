import time
from threading import Thread

import Enemy
from Me import Me
from Enemy import *
class Game:

    @staticmethod
    def play():



        print("     ___       __   _______   ___       ________  ________  _____ ______   _______")
        print("    |\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\   _ \  _   \|\  ___ \ ")
        print("     \ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/| ")
        print("      \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \_|/__ ")
        print("       \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \\\  \ \  \    \ \  \ \  \_|\ \ ")
        print("        \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\ ")
        print("         \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______| ")

        answer = input("want to play a game?")
        if answer == ("no"):
                print("you're annoying")


        elif answer.lower().strip()== ("yes"):
            print("Cool let's play")
         #   print("type /exit to quit the game or /restart to restart the game")
            #i want a quick escape or a restart method
            print("Enter your name:")
            name = input()
            print("Hello," + name )
            print("You are in a cavern and there are two exits, one to the right and one to the left." )
            left_right = input("Which way do you choose? (left/right)")
            if left_right == ("left"):
                print("you go through this exit and see a crazy big statue that resembles a demon. How do you procede?  (touch/ move on) " )
                touch_move_on = input()
                if touch_move_on == ("touch"):
                    print("you get burned to ashes due to it's inmense power")
                    Game.death()

                if touch_move_on == ("move on"):
                    print("you decide to keep walking and find yourself facing a bigger section of the cavern. ""There is a rope bridge and a path leading down a canyon")
                    print("cross/go down")
                    cross_go_down = input()

                    if cross_go_down == ("cross"):
                        print("you cross the wiggly and unstable rope bridge safely and see something in the corner of your eye. ")
                        print("You reach out to grab the shiny object in the ground but it jumps out and reveals itself. ")
                        print("It is a goblin with a chain mail armor. How do you procede? (run/confront)")
                        run_confront = input()
                        if run_confront ==("run"):
                            print(" you run past the goblin and activate a trip wire. A giant boulder crushes the goblin behind you and starts rolling towards you.")
                            print("How do you procede? (run/accept your death)")
                        elif run_confront ==("confront"):
                            print("the goblin stabs you, spits in your face and whispers in your ear: You are a fool for trying to face me. ")
                            Game.death()

                    if cross_go_down == ("go down"):
                        print("You follow the path downwards until you reach the bottom of the chasm. It is very dark yet you are able to see the way and start walking forward. ")
                        time.sleep(2)
                        print("After many hours of walking you see a bright orb of light descend from the above you approaching you and stopping suddenly. It seems as if it ")
                        print(" is trying to communicate with you. How do you procede? (touch/nothing)")
                        touch_nothing = input()
                        if touch_nothing == ("touch"):
                            print("The orbs seems to want you to touch it so you put your hand on the orb. It is warm but suddenly gets really hot.")
                            print("A bright orange power seems to course through your hand and you feel amazing. You feel better than you have in years.")
                            time.sleep(2)

                            print('''                            )`·.            )\                                                                                )`·.                                                '       
       )`·.             .·´   ..:).·´(_ .·´   `·.’'                                                               /(      .·´    (                      (`·.                )\       '    
        \::’·._)'·.  (::::....   .. .:\(      .:::)                   /(      .·´( )`·.                   )\      )  `·._):::.    )        ’'             )  `·.   .·´( .·´  (     /(   ' 
  .·´(   )::. ..:::).·´;·::  ´ ´\::.    ::....:·´            )\      )  `·._):::.....::)'’          )\ .·´ .:`·.(:;;  --  ' '\:. :(.·´)    )\      .·´( .·´:..::(,(::--  ' '\::.`·._) `·.’ 
  ):..\(;;::--  ´ ´               \:::::::..::)        )\ .·´ .:`·.(:;;  --  ' '\:. :(.·´)    )\ .·´  (,): --  ' '              \....:::`·.(  (     );; :--  ' '               \::....:::::)'
 (::...:/\                          ¯¯¯¯¯¯ /·.'.·´  (,): --  ' '              \....:::`·.(  ():.::/\                        ¯¯¯` · ::·´’  .·´/\                ,... ·::´’:::/¯  - :;
   `·:/::::\...:’/        ___________/..::)):.::/\                 ,..::´/:::......:::·´`·:/::::\...:´/       ____          \       )/:::'\...:´/       /:::::::::::/        / 
      \::::/::::/        /::::::::::::·-  ´ ´\/    `·:/::::\...:´/       /:::::'/`·:'/¯¯¯ /   ’   \::::/::::/      /::::::::/\         I"      \:::/::::/       /;;::;;´-··´´        /  '
        \/;::-'/        /;;::·-  ’ ´         _\       \::::/::::/      /;::::-'   '/       /          \/;::-'/’     /::::::::/:::I       /         '\/;::-'/               __,...::::´/    
             /                      .,.,·:::::/         \/;::-'/      /          /       /    '            /’     /¯¯¯¯¯\::'/..-::::/               /        ,,           ` -:::;/  '   
   )`·.   '’/         _ .,., ·:::::::::::::::/               /      /          /       /                ’/     /__.·´(    I:/::::::/          .·´( '/       /:::::·-..,          /       
 (::..:(.·/         /::::::::::::::::--  ´ ´               '/      /          /       /     '       .·´/I'       I `·::__)  /;;::- '´         _) ::/       ’/:::::::::://        /        
  `·:...'/         /:::::::: · ´                   '       /I      'I         /       /              )/::I,       ` · .                       ’')..::/       /``··::::;;//        /     '    
     ):/         /··  ´                                 /::/`· ,    ` ·,_’/       /        '       I:::::::.,         ¯¯¯.·´/              `·:/____ /           /        /       '   
     '/         /                                  '    I:/::::::::` · , ___,.·:/                 I::::::::::::.. __.·´:::/               ’ /::::::::/           /        '/            
   '/,...:::· ´/                    '                    `·:;::::::::::/:::::/:::/                   ' ·:::;:::::::/::/::::·´                 '/::::::::/          '/,....·::´/             
  /::::::::::/                                               ` ·:;:::/:::::/;·´                          ' ·::::'/::/::·´                     ¯¯¯¯¯          /:::::::::/    ’          
'/;:: ·   ´                  '                                       ¯¯¯                      ’                  ¯                        ’'                 '/;;::: · ´´                ''')
                            print('''                 /(      .·´    (                                                            ’                                                                                            '
         )\      )  `·._):::.    )        ’'     (`·.                    )`·._.·´(        )`·.                                                                                            '
   )\ .·´ .:`·.(:;;  --  ' '\:. :(                  \::`·._)`·.     )\.·´::...  .::)   .·´   ./                  )\       )\                             (`·.                )\            '
.·´ (,): --  ' '              \:·´    )`·.     .·´(   )::. ..:::).·´;· --  ´ ´\::.`·.(::...:(’                .·´  /  .·´.:/           .·´(                 )  `·.   .·´( .·´  (     /(     '
):::/\                ,..::´/    .·´:...:)    ):..\(;;::--  ´ ´               ’\:::::::...::)       .·´(     ):.::`·.)::::)    )\     )   `·.      .·´( .·´:..::(,(::--  ’ \::.`·._) `·.   
`·/::::\...:´/       /:::::/     ):::...:`·.(::...:/\                          ’¯¯¯¯¯¯/'      (  .:::`·./::;,  --  ' '\/(.·´.::).·´:   .::)     );; :--  ' '             _\::....:::::)’(
  \::::/::::/      /;:::-'      (:/¯¯¯¯/'   `·:/::::\...:´/        ___________'/     .·´.;);;--  ' '               '\:::::.    .:::·´'  .·´/\                ,..:´:::::'/ `  · :/;·´
    \/;::-'/      /             '/       '/ '      \::::/::::/        /:::::::::;; --  ´ ´\     ’I:::/\                         `` ··:::::·´   ’'  )/:::'\...:´/       /::::::::::/        /   
      )/::I,       ` · .       /       ’/   '       \/;::-'/        /;;::·-  ´ ´         _\    ')/::::'\..:´/       /`::-..,         `./      '    \:::/::::/       /;;:::·  ´ /        '/    
      I:::::::.,         ¯¯¯       '/    '             /                      .,.,·:::::'/   ’''\:::'/::::/       /,::-·· ' '         /             '\/;::-'/       /,  -·· ' '          /     '
      I::::::::::::.. ___         /         )`·.    '/         _ ,.,.,·:::::::::::::::/     '  \/;::-'/       ,...-:::' '/        /         '          /        ,...-:::: ´'/       '/   '   
       ' ·:::;:::::::/::::::/      /    '    (::..:(.·/         /:::::::::::::::::::--  ´      ’       /       /:::::::::/        /              .·´( '/       /::::::::::::/       '/   '    
            ' ·::::'/::::: /      /           `·::..'/          `·__:::::· ’\:   .·´                '/       /;::: ·- '/        '/           '  _) ::/____/;;::::: - ´ /        /      ’  
            .. - ··  ´´       .·/                )/`·.                        \(              ’    /____/.·´)    (/        '/            '  `·:::/:::::::/.  - ··  ´´       .·´/    '     
   ,, -  '        ..-:::::'/::::/                /::::::`·._____ ...·::::::/                  /::::::::/;;  --  ´´      .·´/                  )/::; - '          ..-:::::'/:::/       '   
  /::`*..¸..-::::::::::::/:::·´            ’    `·:::::::/::::::::/:::::::::/                 ’/::::::::/':-.., .,..-:::'/::::/                    ¯/::`*..¸..-::::::::::::/:·´            '
/::::::::/::::::::::-·· ´´                          `·::/::::::::/::::: ·´´                   ’ ¯¯¯¯/::::::/:::::::/:::·´                      /:::::::/::::::::::-·· ´´               ' 
`*-::;/::::-·· ´´                          ’            ¯¯¯¯¯                                     '` ·::;/::;::-·· ´´                   '      `*-::;/::::-·· '’                         ''')
                            time.sleep(2)
                            print("You look at your hand and you notice it is all charred and burnt and try to pull away but cannot. You start to panick and try to get away from the orb.")
                            time.sleep(1)
                            print("But there is nothing you can do except watch as the rest of yuor arm is consumed along with the rest of you. Your head is last to burn but")
                            time.sleep(1)
                            print("the feeling of power is long gone by now and all you feel is a burning sensation as you are consumed by the orb. ")
                            print("Everything goes black")
                            Game.death()
                        elif touch_nothing == ("nothing"):
                            print("You stare at the orb and start to enter a trance")
                            x = ''''|| '||'  '|' '||                .       ||                             ||                                       
 '|. '|.  .'   || ..    ....   .||.     ...   ....       ... .   ...   ...  .. ...     ... .      ...   .. ...   
  ||  ||  |    ||' ||  '' .||   ||       ||  ||. '      || ||  .|  '|.  ||   ||  ||   || ||     .|  '|.  ||  ||  
   ||| |||     ||  ||  .|' ||   ||       ||  . '|..      |''   ||   ||  ||   ||  ||    |''      ||   ||  ||  ||  
    |   |     .||. ||. '|..'|'  '|.'    .||. |'..|'     '||||.  '|..|' .||. .||. ||.  '||||.     '|..|' .||. ||. 
                                                       .|....'                       .|....'                     
                                                                                                                 '''
                            print(x)
                            print("You wake up looking upwards, head on the ground,slowlybeing dragged. You look and see a shadowy figure dragging you to a bright light.")
                            print("How do you procede? (run away/nothing")
                            run_away_nothing = input()
                            if run_away_nothing == ("run away"):
                                print("you kick the figure and scramble away running into the darkness far away from the light.You hear the figures footsteps but keep runnign until you lose  the figure.")
                                print("After you  are sure you are not being tailed then you walk and find yourself a nice cavern and decide to camp there. It seems cozy enough.")
                                time.sleep(2)
                                print("Lots of time passes but you are unsure of how much because there is no sun to tell you of the days or a clock for the hours.")
                                print("You do not leave the cave for it has become your home. You have not eaten or drunk anything at all but that doesn't worry you at all because the cave is all you need.")
                                print("How do you procede? (leave/stay)")
                                eh = input()
                                if eh == ("The cave does not provide"):
                                    print("Thats not true, the cave is all. The cave provides all I need. The cave is all,the cave is benevolent")
                                    print("If you cannot accept the caves benevolance then...")
                                    time.sleep(1)
                                    print("There is no point in you playing this game to continue. Come back when you have appreciated how the Cave is benevolent.")
                                    Game.death()

                                else:
                                    print("You do not move from the cave. You stay there and sit, admiring the  benevolence of it. This is all you could ever want.")
                                    print("How do you procede?")

                            elif  run_away_nothing == ("nothing"):
                                print("gay  pt2")


                            # function(player, enemy)
    #     while enemyHealth > 0
    #         player.attack()
    #         enemyhealth - player.dmg

    @staticmethod
    #this is the death function that prints a message and then restarts the game
    def death():
       print(" ▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄")
       print(" ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌")
       print(" ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌")
       print(" ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌")
       print(" ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓")
       print(" ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒")
       print(" ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒")
       print(" ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░")
       print(" ░ ░         ░ ░     ░           ░     ░     ░  ░   ░")
       print(" ░ ░                           ░                  ░ ")
       go_leave = input("You see the light. How do you you procede? (go to it/leave it alone")
       if go_leave == ("go to it"):
           #i want to implement a screen clear on the console so that if replaying the game that you don't cheat and remember you past decisions
           Game.play()
       elif go_leave == ("leave it alone"):
           print("bye bye")
           #exit code somehow

