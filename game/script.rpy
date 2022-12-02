﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jack", color=(66, 221, 241, 255))
define m = Character("Buzz", color=(221, 15, 176, 255))
define player = Character("You", color=(222, 34, 213, 255))


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene uhm

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    """
      You and Buzz are meeting up one day before class! Buzz is a known diabetic, and but recently his mind has been occupied by school and responsibilities.
    """
    
    player "Hey Buzz! How’s it going? Are you ready for CS 2200 to steamroll us again?"
    
    m "Hey! I’m going as well as I can, didn’t get much sleep last night, but at least I managed to work out a lot today! Pretty hungry though, weird since my breakfast was kinda big."

    
    player "Let’s head down to class then!"
    
    #somehow change slides here
   # e "Well- this game will be about helping people with diabetes? When you're up for it, press start okay??"
    """
    As you walk, Buzz seems to be shaking a little bit as he talks, but you’re not sure if it’s just because it’s cold outside or because of something else.
    """
    menu:

        "Ignore it. He’s probably just tired.":
            jump outside_class

        "Ask if he’s alright.":
            jump conversation_to_class

    label conversation_to_class:

      #  $ menu_flag = True
        """
        You start walking to class, chatting aimlessly about the next impossible project that the professors have decided was an amazing idea.
        """

        player "I’m telling you, there’s no way we’ll be able to finish it "

        """
        He stops, staring at the horizon and trying to intake air, looking a little queasy.
        """

        #jump choice1_done

        menu:

            "Wait Quietly.":
                jump buzz_says_nothing

            "Ask “Are you alright?”":
                jump buzz_says_something

        label buzz_says_nothing:

        #  $ menu_flag = True
            """
            The two of you quickly walk to class.
            """
            jump outside_class

        label buzz_says_something:

        #   $ menu_flag = False

            m "Oh yeah, I’m all good. Thanks for asking. Just tired after the workout and weirdly anxious about the project"

            jump outside_class

        jump outside_class

    label outside_class:

     #   $ menu_flag = False

        m "Finally, we make it to class. 5 minutes before we’re due to start! Nice! Head hurts now, but that’s fine. Price we pay for speedwalking."

        player "{i}This is starting to be a lot of symptoms that aren’t just from a long workout or a bad night of sleep. What should I do?{/i}" 
        
        menu:

            "Usher the both of you into class. He’s probably fine.":
                jump in_class

            "Ask “Are you sure you’re okay?”":
                jump buzz_sits_down

            "Ask “Should you check your blood sugar?”":
                jump buzz_check_blood

        label buzz_check_blood:

        #  $ menu_flag = True
            m "I don’t actually know. I’m really not feeling great, so I could just be sick. But everything came pretty suddenly. I’ll check it once we’re in class, I don’t want to pull it out my pocket right now."
            """
            The two of you head inside and settle down in class.
            """
            jump in_class

        label buzz_sits_down:

        #   $ menu_flag = False

            m "Let’s just sit down in class first and I’ll solve it in there."

            jump in_class

        label in_class:

        #   $ menu_flag = False
            """
            Both of you pull out your laptops and prepare to start taking notes

            """

            m "I think I’m going to put my head down for a bit. It’s not doing to great with both the headache and the amount of trauma this room has given me from 2200 Tests."

            menu:

                "Let him rest":
                    jump class_continues

                "Ask if he can check his blood sugar.":
                    jump check_blood_sugar

            label check_blood_sugar:

            #  $ menu_flag = True
                """
                Buzz pulls out his CGM (Continuous Glucose Monitor) and notices that it’s way too low! It’s only 93 mg/dL!
                """
 
 
                "{i}This normally isn't a problem, but after eating breakfast, his average blood sugar should be closer to 140mg/dL{/i}"
                "{i}This blood sugar level is comparable to that of a non-diabetic person having not eaten for over 5 hours{/i}"

                m "Oh. That explains... This"
                "Buzz gestures towards himself"
                m "Could you run and grab me a snack?"

                player "You got it!"

                """
                You run to the vending machine
                """

                menu:

                    "Choose a pack of hard candy":
                        jump hard_candy

                    "Choose a pack of peanuts":
                        jump peanuts

                label hard_candy:

                #  $ menu_flag = True
                """
                You come back to class holding a bag of Jolly Ranchers.
                """

                m "Sweet! Pun Intended, that’s exactly what I needed! Thank you so much!"

                jump vending_machine_ending_screen
                
                label peanuts:

                """
                You come back to class holding a bag of peanuts
                """
                m "uhhhh- Not quite what I needed... but I'll take it"
                jump class_continues

            label class_continues:

            #   $ menu_flag = False
                """
                You pay attention to class for sometime, diligently taking notes and noticing that Buzz hasn’t lifted his head from the table in a while. 
                """
                menu: 
                    "Poke him to see if he wakes up":
                        jump found_sluggish

                    "Let him sleep":
                        jump found_unconcious_way_later

                label found_sluggish:
                    """
                    You decide to poke him a little bit, and find that he’s not responding at all! Not even a slap to let him sleep more!
                    """

                    y "Buzz? Buzz! Are you there, we need to learn about network hopping!"

                    m ". . . hrggg? Sup? Is something wrong? Something is probably wrong, but something is always wrong."

                    y "Uh oh, this doesn’t look to good."

                    menu:
                        "Check his CGM for his blood sugar level":
                            jump you_check_CGM

                        "Leave him alone":
                            jump found_unconcious_way_later

                    label you_check_CGM:
                        """
                        You pull out his CGM from his pocket. It’s way below 70dl/mg! That’s not good, what do you do now?!                        
                        """
                        menu:
                            "Run to the Vending Machine":
                                jump vending_machine_pt2

                            "Panic silently":
                                jump to found_unconcious_way_later

                        label vending_maching_pt2:
                            """
                            You run to the vending machine.
                            """

                            menu:
                                "Choose sweet fruit juice":
                                    jump to sweet_fruit_juice

                                "Choose beef jerky":
                                    jump to beef_jerky

                            label sweet_fruit_juice:
                                """
                                You come back to class holding a Minute Maid, and shake Buzz a little more to wake him up.
                                """

                                y "Hey, just checked your CGM it doesn’t look too good. You mind taking a couple for now to get the blood sugar up?"

                                m "Hrgg? Oh yeah sure. Thanks for watching out for me, I’ll pay you back. Hopefully after class I can go eat a meal."
                                
                                jump middle_ending_screen

                            label beef_jerky:
                                """
                                You come back to class holding a bag of beef jerky.
                                """

                                y "Hey, just checked your CGM it doesn’t look too good. You mind taking a couple for now to get the blood sugar up?"

                                m "Hrgg? Oh yeah sure. Thanks for watching out for me, I’ll pay you back. Hopefully after class I can go eat a meal."
                                
                                m "Wait a second, these are nuts I don’t know how much this will help me."

                                jump found_unconcious_way_later

                label found_unconccious_way_later:
                    """
                    It’s now the end of class! And you two need to leave soon! So you poke Buzz to see if he wakes up.
                    """

                    y "Buzz, we have to go! Wake up!"

                    m ". . ."

                    y "Buzz? Buzz! Hello?!"

                    m ". . ."

                    """
                    This doesn’t look good, what do you do??!!
                    """

                    menu:
                        "Call 911":
                            jump to er_ending_screen

                        "Try to shake him awake":
                            jump to someone_else_calls_911

                    return

                            
            #jump vending_machine_ending_screen

        label vending_machine_ending_screen:
            "You got his blood sugar to a normal range with that little sweet rush! Good job!!"
            "Buzz started feeling a bit better within the hour."
            return
        





    label choice1_done:



    label middle_ending_screen:
    
    label bad_ending_screen:
        "Buzz quietly ate some peanuts before looking dazed"
        "The person behind you gives him some fruit from their bag and worridly looks after him the rest of class"
        "You seriously didn't know what to do huh?"

    label er_ending_screen:
    label someone_else_called_911:
        # ... the game continues here.

 
    ## show buzz

    ## e ""

    # This ends the game.

    return
