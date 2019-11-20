from Enemy import Enemy
from Me import Me

class Game:

    @staticmethod
    def play():

        goblin = Enemy(3, 33, 'black', 'nicholas')
        player = Me(100, 40, 15, 10)



        yes_no = input("want to play a game?")
        if yes_no == ("no"):
                print("stop being gay")

        elif yes_no == ("yes"):
            print("Cool let's play")
            print("Enter your name:")
            name = input()
            print("Hello," + name )
            print("You are in a cavern and there are two exits, one to the right and one to the left." )
            left_right = input("Which way do you choose? (left/right)")
            if left_right == ("left") :
                print("you go through this exit and see a crazy big statue that resembles a demon. How do you procede?  (touch/ move on) " )
                touch_move_on = input()
                if touch_move_on == ("touch"):
                    print("you get burned to ashes due to it's inmense power")
                    print('fdecr3grh5')
                    print(player.HP)

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
                            #print("the goblin stabs you, spits in your face and whispers in your ear: You are a fool for trying to face me. ")
                            print()


                    if cross_go_down == ("go down"):
                        print("A booming voice shakes the ground saying 'WHOOOO GOOES THERE!'")
                        print("How do you procede? (respond/keep going")
                        respond_keep_going = input()
                        if respond_keep_going == ("respond"):
                            print("How do you respond? (none of your business/Who's asking?)")
                            lost_idc_ignore = input()
                            if lost_idc_ignore == ("none of your business"):
                                print("The voice implodes exclaiming: SPEAK NOW OR FOREVER HOLD YOUR PEACE")
                                print("(I don't know/ oooh how scary)")
                                scary_idk = input()
                                if scary_idk == ("I don't know"):
                                    print("THEN I WILL SMITE YOU!")
                                    print("A giant arm extends out of the darkness under the bridge and smashes you to bits")
                                    print("GAME OVER")
                                if scary_idk == ("ooh how scary"):
                                    print("SILENCE I AM SCARY! YOU WILL SEE MY POWER")
                                    print("A shadow ascends from the darkness, a very small person, a midget or maybe a gnome? if they wear a hat does that make them a gnome or a dwarf.")
                                    print("Huh its questions like these that keep me going")
                                    print(" How do you procede? (laugh/laugh")
                                    input("laugh")
                                    print("I hate you")
                            if lost_idc_ignore == ("ignore"):
                                print("The booming voice explodes and says: I SAID WHOO GOEES THERE")
                                print("(answer/run downwards")
                                if input() == ("answer"):
                                    print("My name is"+ name + "I am lost and don't know which way is out? Can you help me?")

                                elif input() == ("run downwards"):
                                    print("You run down the path which leads to the bottom of the canyon. you observe lots of bodies lying about.")
                        if respond_keep_going ==("keep going"):
                            print("you run downwards to the bottom of the canyon and see a dark figure approaching you. It has dark purple eyes that glow.")
                            print(name + "I know who you are, this is not how we meet, We shal meet again when you are ready. ")
                            print(" The figure disapears and you are left alone facing the darkness. You are drawn to the darkness and walk into it. ")
                            print("You walk through the darkness, strangely enough not bumoing to anything, as if the darkness was leading you somewhere. ")
                            print("An bright orange orb descends from the darkness and approaches you. How do you procede? (touch/ ignore)")
                            touch_keep_going =input()
                            if touch_keep_going == ("touch"):
                                print("You feel a surge of energy coursing through your fingers. You look at the darkness and the orb turns red, consuming your hand, taking your entire arm. ")
                                print("You drop toy your knees from the pain. Your vision blurs and you lose conciousness. ")
                                print("A sharp pain awakens you and you find yourself being dragged by your feet by a strange creature with weirdly long fingers. ")
                                print("How do you proced? (fight/ fake being asleep)")
                if left_right == ("right"):
                    print("you touch the door on the right and feel a cold chill down your spine, you enter anyways.")
                    print("The walls are iced over and you hear a humming noise, wondering what it is you move closer to the source")
                    print("you find a big red button on the wall behind some wooden crates, (press/keep exploring/go back")
                    if input() == (" press"):
                        print("the room is lit and you are burnt to crisp")
                        print("GAME OVER")
                    elif input() == ("keep exploring"):
                        print("You find a cool looking statue and store it in your bag")
                        print("The door starts to glow and your bag coombust into flames. The bag turns to ash and a mark on your arm.")
                        print("      /\ ")
                        print("     /  \ ")
                        print("     /\/\ ")
                        print("     \  /")
                        print("      \/")
                        print(" The mark of dahl: you whisper. Confused to where the words came from a hatch from the roof opens. you decide to go through it.")
                        print(" You jump and go through the hatch revealing a grey sky, the air smells of ash and all that surrounds you is a barren terrain.")
                        print("How do you procede? (go explore/admire the view)")
                        explore_admire = input()
                        if explore_admire == ("go explore"):
                            print(" You jump off the roof and start walking through the wasteland. Hours pass and you see an abandoned building in the distamce.")
                            print(" You hurry towards the building and observe a pack in front of the entrance. ")
                            print("How do you procede? (go through pack/go in building)")
                            pack_go_in = input()
                            if pack_go_in == ("go through pack"):
                                pack = [" a waterbottle", "a key", "a book", "5 gummy worms"]
                                print("You look in the pack and you see" + pack[0])
                                print("Oooh gummies")
                                print("How do you procede? (take/leave it")
                            if pack_go_in == ("go in building"):
                                print("lrl")
                        if explore_admire == ("admire the view"):
                            view = [" dead trees", "buildings in ruins", "a figure in the distance", "rocks, wait hold up a figure in the distance?"]
                            print("you analyze your surroundings and see:" + view[0])
                            print("how do you procede? (hide/wave")
                    else:
                            print("you go through this exit and see a crazy big statue that resembles a demon. How do you procede?  (touch/ move on) ")
                            if input() == ("touch"):
                                print("the room gets lit on fire and you are burned alive")

                            else:
                                print("you decide to keep walking and find yourself facing a bigger section of the cavern ""There is a rope bridge and a path leading down a canyon")
                                print("cross/go down path")

    # function(player, enemy)
    #     while enemyHealth > 0
    #         player.attack()
    #         enemyhealth - player.dmg