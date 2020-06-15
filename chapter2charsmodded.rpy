
label chapter2charsmodded:

    

    # $ save_name = (_("Chapter 2"))

    # if persistent.endingsseen > 0:

    #     $ sebastianavailable = True
    #     $ sebastian2available = True
        # $ kevinunplayed = True
        # $ kevininvited = False

    # if sebastianunplayed == False:

    #     $ sebastianavailable = False
    #     $ sebastian2available = False

    # if kevinunplayed == False:
# Kevin's previous statement for Chapter 1. MC is forced to meet with Kevin on their walk, but it does not affect the other people they are going to be able to see.
        # $ kevinavailable = False 
        # $ kevininvited = False

#     if chapter2csplayed == 0:

#         menu:
#             c "(What should I do?)"
#             "Meet with Remy." if remy1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap1picka = "remy"
#                 $ chap3picksremy += 3
#                 jump remy2

#             "Meet with Anna." if anna1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap1picka = "anna"
#                 $ chap3picksanna += 3
#                 jump anna2

#             "Meet with Lorem." if lorem1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap1picka = "lorem"
#                 $ chap3pickslorem += 3
#                 jump lorem2

#             "Meet with Bryce." if bryce1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap1picka = "bryce"
#                 $ chap3picksbryce += 3
#                 jump bryce2

#             "Order some lunch." if adine1unplayed:
#                 stop music fadeout 1.0
#                 $ chap1picka = "adine"
#                 $ chap3picksadine += 3
#                 jump adine2


#             "Meet with Sebastian." if sebastianavailable:
#                 stop music fadeout 1.0
#                 $ chap1picka = "sebastian"
#                 jump sebastian2

# ##            "[Show More.]":
# ##            "Meet with Kevin." if kevinavailable:
# ##                play sound "fx/steps/clean2.wav"
# ##                stop music fadeout 1.0
# ##                $ chap1picka = "kevin"
# ##                jump 

# ##                            "[Go back.]"
# ##                                jump chapter1charsmodding
                       

#     elif chapter2csplayed == 1:

#         scene black with dissolveslow
#         $ renpy.pause (1.0)
#         scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

#         menu:
#             c "(More free time. What should I do?)"
#             "Meet with Remy." if remy1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "remy"
#                 $ chap3picksremy += 2
#                 jump remy1

#             "Meet with Remy." if remy2unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "remy"
#                 $ chap3picksremy += 2
#                 jump remy2

#             "Meet with Anna." if anna1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "anna"
#                 $ chap3picksanna += 2
#                 jump anna1
# # In case Anna has already been played it will now be displayed in chapter2charsmodded to allow any second dates with Anna.
#             "Meet with Anna." if anna2unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "anna"
#                 $ chap3picksanna += 2
#                 jump anna2

#             "Meet with Lorem." if lorem1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "lorem"
#                 $ chap3pickslorem += 2
#                 jump lorem1
# # In case Lorem has already been played it will now be displayed in chapter2charsmodded to allow any second dates with Lorem.
#             "Meet with Lorem." if lorem2unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "lorem"
#                 $ chap3pickslorem += 2
#                 jump lorem2

#             "Meet with Bryce." if bryce1unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "bryce"
#                 $ chap3picksbryce += 2
#                 jump bryce1

# # In case Bryce has already been played it will now be displayed in chapter2charsmodded to allow any second dates with Bryce.
#             "Meet with Bryce." if bryce2unplayed:
#                 play sound "fx/steps/clean2.wav"
#                 stop music fadeout 1.0
#                 $ chap2pickb = "bryce"
#                 $ chap3picksbryce += 2
#                 jump bryce2
#             "Order some lunch." if adine1unplayed:
#                 stop music fadeout 1.0
#                 $ chap2pickb = "adine"
#                 $ chap3picksadine += 2
#                 jump adine1
# # In case Adine has already been played it will now be displayed in chapter2charsmodded to allow any second dates with Adine.
#             "Meet with Adine." if adine2unplayed:
#                 stop music fadeout 1.0
#                 $ chap2pickb = "adine"
#                 $ chap3picksadine += 2
#                 jump adine2
# # In case Sebastian has already been played it will now be displayed in chapter2charsmodded to allow any second dates with Sebastian.
#             "Meet with Sebastian." if sebastian2available:
#                 stop music fadeout 1.0
#                 $ chap2pickb = "sebastian"
#                 jump sebastian2
            
#            "Take a walk." if kevinunplayed:
#                play sound "fx/steps/clean2.wav"
#                stop music fadeout 1.0
#                $ chap2pickb = "kevin"
#                jump KevinExtended
# # In case Kevin has already been played it will now be displayed in chapter2charsmodded to allow any second dates with Kevin.
#            "Meet with Kevin." if kevin2available:
#                play sound "fx/steps/clean2.wav"
#                stop music fadeout 1.0
#                $ chap2pickb = "kevin"
#                jump k2chap2
                
#             "Get some well deserved rest.":
#                 $ chap2pickb = "none"
#                 m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
#                 jump chapter3
#     else:

#         jump chapter3

# return
