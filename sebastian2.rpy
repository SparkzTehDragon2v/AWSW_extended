label sebastianchap2:
    $ sebtour = False
    $ sebxp = 0
    $ sebPoints = 0
    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - Sebastian - 2"
    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - Sebastian - 2"
    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - Sebastian - 2"
    else:
        $ save_name = "Chapter 1 - Sebastian - 2"


scene black with dissolvemed
$ renpy.pause (0.5)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

$ renpy.pause (0.5)

# m "I was interrupted by the doorbell."

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)
c "(That must be him.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)
play music "mx/cruising.ogg" fadein 2.0

show sebastian smile b

with fade

c "Hey, Sebastian."

Sb "Howdy, [player_name]."

Sb drop b "I wanted to apologize for what you had to see on your first day here."

c "Look, Sebastian it wasn't too much for me to handle. In the mean time why don't you have a seat? You look stressed."

Sb normal b "I can agree with you on that."

m "Sebastian takes his time to pick a spot on one of the couches before placing his rump down on a cushion. Sebastian sighs gently in displeasure."

Sb disapproval b "There's a lot to see here, but a homocide was not one to even be seen."

Sb "If Bryce let you choose to not get involved, this would have been easier for all of us, including yourself [player_name]. Especially, for an ambassador such as yourself."

m "Sebastian looked a bit tense through this as well."

menu:
    "Let him speak.":



        m "I take a seat on another cushion, but close to Sebastian. Nodding and listening."

        m "Sebastian looked at me with his purple eyes and relaxed a bit."

        # Allow Sebastian to speak to the MC about his concerns with the MC being on the crime scene helping the investigation.

    "Give him a Kiss.":



        m "I took a seat next to the cushion Sebastian was sitting on, leaning over gently to give Sebastian a kiss on the cheek."

        Sb shy b "H-hey... what are you doing [player_name]?"

        c "I thought that it would make you feel better Sebastian. You look stressed out like I said before, maybe it's just time for you to relax and ease up a bit you know?"

        c "I know being a police officer is hard and I sympathy with you. Back home where I belong, there was tons of crime that was everywhere... homicides, murder, poisonings..."

        c "There's a lot of bad there at my home world, but one day it'll get better."

        m "Sebastian, eased up a bit and looked at me with his purple iris eyes that could see for miles."

        Sb disapproval b "Much more worse there than here I assume."

        m "I nodded gently."

        c "It's just how our society works, everyone is different and thinks for themselves sometimes. They can even think hard enough to actually want to kill."

        $ sebxp += 1 # 1 point.

        # Ease out of this conversation as it will allow sebastian to stop continuing on with the conversation and ease into a new topic. TOPIC WILL BE SELECTED BY OPTION!!!

    "Respectfully accept his apology.":
        c "Sebastian, I forgive you. It's fine. I've seen worse."

        Sb normal b "Have you?"

        m "I come over and take a seat on the cushion beside Sebastian and nod a bit."

        c "Well, for me at least I have seen worse, but I would rather not talk about it... it's rather disturbing if I can say so myself."

        c "Plus, didn't you want to relax anyways? You did tell me if I needed anything I could always ask you."

        Sb smile b "[player_name], I do wish to relax and I thank you for that. So, to move on from our previous topic. How do you like it here?"
        menu:
            "Good.":
                c "I love it so far, even if it is my first day here."

                Sb smile b "That's good to hear."

                $ sebxp += 1 # 1 point.

                Sb smile b "You know, there are other places that you probably haven't seen around here. You may enjoy it too if you're into learning about us dragons."

                menu:
                    Sb "So, what do you say?"
                    "Take Sebastian's Tour.":
                        $ sebtour = True
                        $ sebxp += 1 # 2 points if "Good" to this node.
                        c "I would enjoy seeing other places in town here, it'd help me get to know you guys better of your works and advancement."

                        Sb smile b "Then that's what we'll do."

                        Sb smile b "When do you want to go look around the town?"

                        menu:
                            c "(When should I go with Sebastian on his tour?)"
                            "Now.":
                                c "We could go now if you're comfortable with that."
                            
                            "After some lunch.":
                                c "We could go after some lunch, I am getting pretty hungry."

                                menu:
                                    Sb "Of course, do you want to go back to Uncle Mugen's at all? I am sure they have something that you'll like."
                                    "I'm down.":
                                        Sb smile b "Then let's make our way there in the meantime."
                                    "Somewhere else.":
                                        c "We could go somewhere else to find something to eat. Know of any other places?"

                                        Sb normal b "There is Cafe Memoria, I don't know if you've heard of it before, but it is another place to eat at."

                                        menu:
                                            "Uncle Mugen's.":
                                                c "Let's go to Uncle Mugen's. Last time you took me there it went pretty well."
                                                Sb smile b "I'm glad that it did go well for you, [player_name]."
                                                Sb "Let's go."
                                                jump SebastianLunchMugens

                                            "Cafe Memoria.":
                                                c "I wanna go to Cafe Memoria, that other place that you mentioned."
                                                Sb smile b "Alright, we'll go."
                                                jump SebastianLunchMemoria


                            "Later tonight.":
                                c "How about later this evening?"

                                Sb smile b "Sounds good, [player_name]."

                                Sb drop b "Usually later in the evening, I take a run to the bar."

                                Sb drop b "Bryce, or as you should know him the Chief of Police, normally is there. I check to make sure he isn't there or vice versa."

                                c "Why does Bryce go to the bar?"

                                Sb disapproval b "It's a long story... at some point I'll be able to tell you why he does go to the bar, but right now I can't."

                                Sb disapproval b "Until you learn of why on your own or when I can comfortably say why Bryce goes to the bar."

                                Sb smile b "Bryce is a great Chief and friend once you get to know him more."

                                c "I can already tell he's a great leader, he's quite perfectly fit for being Chief of this town. He's civil and kind as far as I have seen of him."

                                Sb smile b "That's one of the other stories you will learn soon enough about him. He's got stories too, so you should also go meet up with him sometime."

                            "Tomorrow.":
                                c "We could do the tour tomorrow later in the afternoon. Shouldn't be too bad if we aren't too busy."

                                Sb normal b "I can't guarantee that we won't be busy."

                                Sb smile b "There may be something that will let us squeeze in time."

                            "Early morning tomorrow.":
                                c "How about tomorrow morning? You could come back and rest here when you aren't on duty."

                                Sb smile b "That would work, it'd make things go easier as well just in case we do have to go back to the police station."

                                Sb smile b "Though if we need to be there quickly, I hope you can run."
                                
                                c "You seem like you can definitely run faster than I ever could."

                                Sb smile b "I'd like to at least let you try to run with me. See how long you can keep up with my speed."

            "It's ok.":
                c "It could be better."

                Sb normal b "I see, once we get around to it I could give you a more thorough tour of this small town here, how does that sound?"

                menu:
                    "Accept Sebastian's Invitation.":
                        c "Sounds like something we could do. I am up for it."

                        Sb smile b "Good! Can't wait to show you some of my favorite places I go during my freetime."

                        c "What do you do in your freetime?"

                        Sb shy b "That's... for another time [player_name]. Heh."

                        c "Alright."

                        $ sebtour = True
                        $ sebxp += 1 

                    "Decline Sebastian's Invitation.":
                        c "I am going to have to say, 'no', on that offer Sebastian."

                        Sb normal b "If you change your mind I wouldn't mind taking you around the town. There's beautiful and unique places that may catch your eye one way or another."

                        $ sebxp -= 1 # Lose a point. 
                        $ sebtour = False

                        menu:
                            "Reconsider Sebastian's Invitation.":
                                c "Alright, you got me interested."

                                Sb smile b "Glad I did peak your interest, next time we will spend the day walking around the town."

                                c "Sounds good to me."

                                $ sebtour = True
                                $ sebxp += 1

                            "Keep your answer the same.":
                                c "No thanks, Sebastian, but thank you anyways for the offer."

                                Sb disapproval b "Shame."

                                $ sebtour = False
                                $ sebxp -= 1 # Lose a Point.


            "I hate it here.":
                c "I don't really like it here in this foreign land. Just gives me a reason to want to leave sooner."

                Sb disapproval b "This place is the first place you have been to, this just brings us back to the investigation after you accepted my apology."

                Sb disapproval b "It wasn't my intention to get you involved in the investigation, I thought it was a bad idea, but Bryce saw something in you."

                Sb normal b "He saw something in you that made this investigation rather simple. Even if it was out of routine, [player_name]."

                Sb smile b "So, please give this land a chance, I can guarantee you may find something you like, whether it is the people or the significance of the land itself."

                menu:
                    "Give it a chance.":
                        c "I'll give it a chance, even if it doesn't seem too good in my current situation."

                        Sb smile b "That's what I like to hear."

                        Sb smile b "You'll find a lot of great things in this wonderful place we call home. Trust me it will only get better from here."

                        $ sebtour = True

                    "Keep your answer the same.":
                        c "I don't like it here. It's really already bad enough as it is I don't think this place deserves another chance."

                        Sb dro b "Hey... that's only your opinion. This town is normally quiet it doesn't normally have that much crime here."

                        c "You aren't changing my mind about it."

                        Sb disapproval b "Suit yourself then."

                        $ sebtour = False



c "That's just me and who I am."




# scene black with dissolvemed
# $ renpy.pause (0.5)
# scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

# $ renpy.pause (0.5)



stop music fadeout 1.0

scene black with dissolvemed
# hide sebastian
$ renpy.pause (0.5)
scene o with dissolvemed

$ renpy.pause (1.5)


# $ sebastianavailable = False
$ sebastian2available = False
$ sebastian2unplayed = False
$ sebastian2played = True
$ sebastian3unplayed = True
$ sebastian3available = True
# $ sebPoints += 3 

jump chapter2charsmodded #chapter2charmodded | Previous Jump point.


label SebastianLunchMugens:
    $ save_name = "Chapter 2 - Sebastian - Uncle Mugen's"

stop music fadeout 1.0

scene black with dissolvemed
# hide sebastian
$ renpy.pause (0.5)
scene cafe with dissolvemed

$ renpy.pause (1.5)
jump chapter2charsmodded #chapter2charmodded | Previous Jump point.


label SebastianLunchMemoria:
    $ save_name = "Chapter 2 - Sebastian - Cafe Memoria"

stop music fadeout 1.0

scene black with dissolvemed
# hide sebastian
$ renpy.pause (0.5)
scene "bg/bar.jpg" with dissolvemed

$ renpy.pause (1.5)
jump chapter2charsmodded #chapter2charmodded | Previous Jump point.

label SebastiansTour:
    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - Sebastian - Tour"
    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - Sebastian - Tour"
    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - Sebastian - Tour"
    else:
        $ save_name = "Chapter 1 - Sebastian - Tour"




