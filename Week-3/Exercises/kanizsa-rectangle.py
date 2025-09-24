from expyriment import design, control, stimuli

def kanizsa_rectangle(rec_ratio, rad_scale,rec_scale):
    control.set_develop_mode()
    exp = design.Experiment(name = "Kanizsa-rectangle",background_colour=(119,136,153))
    control.initialize(exp)
    screen_width, screen_heigth = exp.screen.size

    square_width = int(rec_ratio[0]*screen_width*rec_scale/100)
    square_heigth = int(rec_ratio[1]*screen_heigth*rec_scale/100)
    circle_radius = int(screen_width*rad_scale/100)

    circle_1 = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position= (square_width/2,square_heigth/2))
    circle_2 = stimuli.Circle(radius=circle_radius,colour=(255,255,255),position= (-square_width/2,-square_heigth/2))
    circle_3 = stimuli.Circle(radius=circle_radius, colour=(255,255,255),position= (square_width/2,-square_heigth/2))
    circle_4 = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position= (-square_width/2,square_heigth/2))
    square = stimuli.Rectangle(size=(square_width,square_heigth), colour=(119,136,153))

    control.start(subject_id=1)

    circle_1.present(clear=True, update=False)
    circle_2.present(clear=False, update=False)
    circle_3.present(clear=False, update=False)
    circle_4.present(clear=False, update=False)
    square.present(clear=False,update=True)


    exp.keyboard.wait()

    control.end()

# rec_ratio is an array with in position 0 the ratio od the width and in position 1 the ratio of the heigth
rec_ratio = [1.5,1]
# scale are giver in percentages
rad_scale = 5
rec_scale = 20

kanizsa_rectangle(rec_ratio=rec_ratio, rad_scale=rad_scale,rec_scale=rec_scale)