from expyriment import design, control, stimuli

control.set_develop_mode()
exp = design.Experiment(name = "Kanizsa-square",background_colour=(119,136,153))
control.initialize(exp)

screen_width, screen_heigth = exp.screen.size
square_size = int(screen_width/5)
circle_radius = int(screen_width/20)

circle_1 = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position= (square_size/2,square_size/2))
circle_2 = stimuli.Circle(radius=circle_radius,colour=(255,255,255),position= (-square_size/2,-square_size/2))
circle_3 = stimuli.Circle(radius=circle_radius, colour=(255,255,255),position= (square_size/2,-square_size/2))
circle_4 = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position= (-square_size/2,square_size/2))
square = stimuli.Rectangle(size=(square_size,square_size), colour=(119,136,153))

control.start(subject_id=1)

circle_1.present(clear=True, update=False)
circle_2.present(clear=False, update=False)
circle_3.present(clear=False, update=False)
circle_4.present(clear=False, update=False)
square.present(clear=False,update=True)


exp.keyboard.wait()

control.end()
