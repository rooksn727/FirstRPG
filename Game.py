import time
from threading import Thread

import Enemy
import Me
from Me import *
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
        if answer.lower().strip() == ("no"):
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
            if left_right.lower().strip() == ("left"):
                print("you go through this exit and see a crazy big statue that resembles a demon. How do you procede?  (touch/ move on) " )
                touch_move_on = input()
                if touch_move_on.lower().strip() == ("touch"):
                    print("you get burned to ashes due to it's inmense power")
                    Game.death()

                if touch_move_on.lower().strip() == ("move on"):
                    print("you decide to keep walking and find yourself facing a bigger section of the cavern. ""There is a rope bridge and a path leading down a canyon")
                    print("cross/go down")
                    cross_go_down = input()

                    if cross_go_down.lower().strip() == ("cross"):
                        print("you cross the wiggly and unstable rope bridge safely and see something in the corner of your eye. ")
                        print("You reach out to grab the shiny object in the ground but it jumps out and reveals itself. ")
                        print("It is a goblin with a chain mail armor. How do you procede? (run/confront)")
                        run_confront = input()
                        if run_confront.lower().strip() ==("run"):
                            print(" you run past the goblin and activate a trip wire. A giant boulder crushes the goblin behind you and starts rolling towards you.")
                            print("How do you procede? (run/accept your death)")
                        if run_confront.lower().strip() ==("confront"):
                            print("the goblin stabs you, spits in your face and whispers in your ear: You are a fool for trying to face me. ")
                            Game.death()

                    if cross_go_down.lower().strip() == ("go down"):
                        print("You follow the path downwards until you reach the bottom of the chasm. It is very dark yet you are able to see the way and start walking forward. ")
                        time.sleep(2)
                        print("After many hours of walking you see a bright orb of light descend from the above you approaching you and stopping suddenly. It seems as if it ")
                        print(" is trying to communicate with you. How do you procede? (touch/nothing)")
                        touch_nothing = input()
                        if touch_nothing.lower().strip() == ("touch"):
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
                        elif touch_nothing.lower().strip() == ("nothing"):
                            print("You stare at the orb and start to enter a trance")
                            x = ''''|| '||'  '|' '||                .       ||                             ||                                       
 '|. '|.  .'   || ..    ....   .||.     ...   ....       ... .   ...   ...  .. ...     ... .      ...   .. ...   
  ||  ||  |    ||' ||  '' .||   ||       ||  ||. '      || ||  .|  '|.  ||   ||  ||   || ||     .|  '|.  ||  ||  
   ||| |||     ||  ||  .|' ||   ||       ||  . '|..      |''   ||   ||  ||   ||  ||    |''      ||   ||  ||  ||  
    |   |     .||. ||. '|..'|'  '|.'    .||. |'..|'     '||||.  '|..|' .||. .||. ||.  '||||.     '|..|' .||. ||. 
                                                       .|....'                       .|....'                     
                                                                                                                 '''
                            print(x)
                            time.sleep(1)
                            print("You wake up looking upwards, head on the ground,slowly  being dragged. You look and see a shadowy figure dragging you to a bright light.")
                            print("How do you procede? (run away/nothing")
                            run_away_nothing = input()
                            if run_away_nothing.lower().strip() == ("run away"):
                                print("you kick the figure and scramble away running into the darkness far away from the light.You hear the figures footsteps but keep running until you lose the figure.")
                                print("After you  are sure you are not being tailed then you walk and find yourself a nice cavern and decide to camp there. It seems cozy enough.")
                                time.sleep(2)
                                print("Lots of time passes but you are unsure of how much because there is no sun to tell you of the days or a clock for the hours.")
                                print("You do not leave the cave for it has become your home. You have not eaten or drunk anything at all but that doesn't worry you at all because the cave is all you need.")
                                print("How do you procede? (leave/stay)")
                                eh = input()
                                if eh.lower().strip() == ("The cave does not provide"):
                                    print("Thats not true, the cave is all. The cave provides all I need. The cave is all,the cave is benevolent")
                                    print("If you cannot accept the caves benevolance then...")
                                    time.sleep(1)
                                    print("There is no point in you playing this game to continue. Come back when you have appreciated how the Cave is benevolent.")
                                    Game.death()

                                else:
                                    print("You do not move from the cave. You stay there and sit, admiring the  benevolence of it. This is all you could ever want.")
                                    print("How do you procede?")
                                    eh2= input()
                                    if eh2.lower().strip() == ("Is it tho?"):
                                        print("STOP QUESTIONING THE CAVE! IT IS ALL I NEED")
                                        print("Thats it I'm done")
                                        Game.death()
                                    else:
                                        print("You keep still in the cave for longer,never moving, just admiring.")
                                        print("This")
                                        time.sleep(1)
                                        print("This is perfection")
                                        Game.death()

                            elif  run_away_nothing.lower().strip() == ("nothing"):
                                print("You lie still, letting the figure drag you to where ever it is taking you.")
                                print("It's quite a bumpy ride, the figure keeps dragging you over rocks which hurt your head and make the ride quite unpleasant.")
                                print("Eventually it drags you over a small ledge and you lose conciousness")
                                time.sleep(2)
                                print("You wake up in a metal cage, It resembles those in which you would keep a parakeet except it's bigger and it is housing you a human.")
                                print("There is a huge bonfire but no one is around. You try to pry the cage open but it is too heavy and the lock is heavy")
                                time.sleep(4)
                                print("Figures start to emerge, you noticed only a couple but there could be easily be a dozen or two. The creatures have a scale like skin, lizard people  but with milky white eyes")
                                print("They start chanting an ominous language, which started as a whisper but before you know it they're roaring it at a deafining volume.")
                                time.sleep(4)
                                print("A taller figure, emerges and the chanting stops. The figure appears to be the leader.")
                                print("The figure approaches you and starts to hiss but soon realizes you do not understand, it hisses at one of the figures wearing a red garb")
                                time.sleep(4)
                                print("The red garbed reptilian comes forth and starts to speak to you")
                                print("-Hellooo therrrreeee humaaahhn, we've been exxxxpecting you")
                                print("The leader reptilian hisses at the red garbed reptilian, which im going to call dave.")
                                time.sleep(4)
                                print("Dave says: I am Dyroman, the high priest of the Nytseny, my people. I am sure you have heard of us ")
                                print("-We are planning to ssssacrificssse you to the allmighty cave god Ghynera. He issss also known as the god of the underworld and cavessss.")
                                time.sleep(4)
                                print("-Take of your clothes so we can better inspect what we are going to deal with")
                                print("How do you procede? (refuse/do it")
                                refuse_do_it = input()
                                if refuse_do_it.lower().strip() == ("refuse"):
                                    print("You tell Dave that you refuse and he administers the message to Dyroman")
                                    print("Dyroman starts hissing furiously and puts his claws on his sword")
                                    time.sleep(3)
                                    print("Dave then looks at you and says")
                                    print("-You are ruining the ruitual by refussssing to do sssooo. The high priesssst hassss challengesssss you to a duel. if you beat him, you can earn your freedom")
                                    print("-However if the highpriessst beatsss you then you will be sssssacrificsssed.")
                                    time.sleep(3)
                                    print("-Fighting on behalfff of the High Priessssst is the Champion of the Nytsenty")
                                    print("Dave opens the cage and hands you a crooked dagger. You take the dagger and step out of the cage.")
                                    print("The Nytsenty form a ring around you and their Champion. The fight has started.")
                                    Me.Champion()
                                    print("-Thissss isss not possssibleee")
                                    print("Dyroman looks at you in awe, you don't know how you can tell but his(or rather its) eyes are wide open")
                                    print("-Fine you are allowed to leave the cage and wander on adventurer")
                                    print("A random lizard man approaches the cage with a set of keys and opens the cage. You exit the cage and start to head out")
                                    print("Dyroman then hisses at Dave. Dave nods and starts to speak")
                                    print("-The high priest of the Nytseny, Dyroman has made an offer I think that you might want to hear wanderer")
                                    print("-He is offering his hand, not in marriage but in brotherhood. You will be welcome to be one of us.")
                                    print("-That means you will dine with us, sleep with us and be one of us. We can fully transform you into one of us, magically of course")
                                    print("-You woul dbe identical to us other than the fact that you would be the new champion of the Nytseny")
                                    print("-So what do you say wanderer? Will you join us? (join/no thanks")
                                    join_go_on = input()
                                    if join_go_on.lower().strip() == ("join"):
                                        print("")

                                    if join_go_on == ("no thanks"):
                                        print("")
                                if refuse_do_it.lower().strip() == ("do it"):
                                    print("You start to take off your shirt but you hear a gasp, or at least the closest thing to it. Hissing goes around ")
                                    print("Dyroman has a panicked look on his 'face' and starts hissing at dave")
                                    print("Dave then says -You have the mark of the Traveler, it was foretold that a Travelor sent by Gyhnera would come to our village")
                                    print("-asking for safe passage. you are allowed to leave o Traveler")
                                    print("The Nytseny all bow down and let you out of your cage, hissing in harmony a chant. You leave the cage and head out into the darkness opposite from where you came from.")
                                    print("You wander")








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

