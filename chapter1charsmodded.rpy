
label chapter1charsmodded:

    $ save_name = (_("Chapter 1"))

    if persistent.endingsseen > 0:

        $ sebastianavailable = True
        $ kevinunplayed = True
        $ kevininvited = False
        

    if sebastianunplayed == False:

        $ sebastianavailable = False

    if kevinunplayed == False:
        $ kevinavailable = False
        $ kevininvited = False

    if chapter1csplayed == 0:

        menu:
            c "(What should I do?)"
            "Meet with Remy." if remy1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "remy"
                $ chap3picksremy += 3
                jump remy1

            "Meet with Anna." if anna1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "anna"
                $ chap3picksanna += 3
                jump anna1

            "Meet with Lorem." if lorem1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "lorem"
                $ chap3pickslorem += 3
                jump lorem1

            "Meet with Bryce." if bryce1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "bryce"
                $ chap3picksbryce += 3
                jump bryce1

            "Order some lunch." if adine1unplayed:
                stop music fadeout 1.0
                $ chap1picka = "adine"
                $ chap3picksadine += 3
                jump adine1


            "Meet with Sebastian." if sebastianavailable:
                stop music fadeout 1.0
                $ chap1picka = "sebastian"
                jump sebastian

##            "[Show More.]":
            "Take a walk." if kevinavailable:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "kevin"
                jump KevinExtended

##                            "[Go back.]"
##                                jump chapter1charsmodding
                       

    elif chapter1csplayed == 1:

        scene black with dissolveslow
        $ renpy.pause (1.0)
        scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

        menu:
            c "(More free time. What should I do?)"
            "Meet with Remy." if remy1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "remy"
                $ chap3picksremy += 2
                jump remy1

            "Meet with Anna." if anna1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "anna"
                $ chap3picksanna += 2
                jump anna1

            "Meet with Lorem." if lorem1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "lorem"
                $ chap3pickslorem += 2
                jump lorem1

            "Meet with Bryce." if bryce1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "bryce"
                $ chap3picksbryce += 2
                jump bryce1

            "Order some lunch." if adine1unplayed:
                stop music fadeout 1.0
                $ chap1pickb = "adine"
                $ chap3picksadine += 2
                jump adine1

            "Meet with Sebastian." if sebastianavailable:
                stop music fadeout 1.0
                $ chap1pickb = "sebastian"
                jump sebastian

            "Take a walk." if kevinunplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "kevin"
                jump KevinExtended
                
            "Meet with Kevin." if kevininvited:
                play sound "fx/steps/cean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "kevin"
                jump k1chap1
                
            "Get some well deserved rest.":
                $ chap1pickb = "none"
                m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
                jump chapter2
    else:

        jump chapter2

return
