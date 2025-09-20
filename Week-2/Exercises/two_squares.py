from expyriment import design, control, stimuli

exp = design.Experiment(name = "Two_square")

control.initialize(exp)

red_square = stimuli.Rectangle((50,50), colour=(255,0,0), position=(-100,0))
green_square = stimuli.Rectangle((50,50), colour=(0,255,0), position=(100,0))

control.start(subject_id=1)

red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()
