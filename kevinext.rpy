
label KevinExtended:
    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - KevinExtended - Start"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - KevinExtended - Start"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - KevinExtended - Start"

    else:
        $ save_name = "Chapter 1 - KevinExtended - Start"

$ kvextpoints = 0

play music "mx/dash.ogg" fadein 2.0

scene town2 with dissolveslow

m "I was on my way to the hatchery when I heard a voice call out to me."

"???" "Hello there!"

m "I turned around to see an unfamiliar face before me."

show meetingkevin at Pan ( (400, 327), (300, 0), 8.0) with fade

$ renpy.pause (6.5)

hide meetingkevin

show kevin normal

with fade

Kv "Hey. I'm Kevin."

c "[player_name]. Nice to meet you."

Kv ramble "Could I perhaps interest you in our Midwest Institution?"

c "Is this some kind of religious thing?"

Kv "Not at all! It's a college."

c "Sorry, but I already got my degrees."

Kv face "Yeah, I know. It was just a joke."

c "Oh, so me going to college is a joke now. I'm not good enough, is that it?"

Kv normal "Not at all! Even if you wanted to study there, I don't think you'll be with us long enough to make use of it."

Kv face "I think that came out wrong."

c "You're lucky I won't take this the wrong way."

Kv normal "Phew."

c "So, you're a recruiter for this college?"

Kv ramble "No, this is just my summer job. Once the semester starts up again, I'll actually be attending to get my degree in psychology."

c "College. Wonderful times."

Kv brow "Is that sarcasm?"

c "Maybe. I didn't even know you had colleges here, though."

Kv ramble "Well, you do now."

c "Why'd you even approach me if you know I'm not going to go to college here? Don't tell me it's just because I'm human."

Kv normal "I was actually trying to talk to that old lady who walked by, but once you turned around there was no going back."

c "Oh. Well, thanks for not making things awkward."

Kv ramble "Hey, I treat everyone nicely until I have reason not to."

c "That's good customer service."

Kv normal "Sure, but it's not just for the job, you know. That's just me."

menu:
    "Invite him.":


        c "Why don't you come over to my place later? I'd love to hear more about what college is all about in this world."

        Kv ramble "Then you found the right person for the job."

        c "I can't promise anything right now, but maybe I'll see you another time."

        Kv normal "For sure. I also have to finish this up here, but after that I'm free."

        c "Alright, I'll let you know."

        Kv ramble "I'm here all day today and tomorrow, so it shouldn't be hard to find me."

        c "Great. I have to get going now, but I'll be sure to let you know if anything's up."

        Kv normal "Sure. See ya!"

        $ kevinavailable = True
    "Excuse yourself.":


        c "Oh, I should really be going. I have some things to take care of."

        Kv ramble "Alright, no problem. See ya!"


# scene black with dissolvemed

$ renpy.pause (0.5)

scene town2 at Pan ((0, 0), (0, 180), 3.0) with dissolveslow

stop music fadeout 1.0

scene black with dissolvemed

$ renpy.pause (1.0)

jump chapter1charsmodded
