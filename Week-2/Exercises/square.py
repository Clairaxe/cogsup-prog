from expyriment import design, control, stimuli

exp = design.Experiment(name = "Square")

control.initialize(exp)

fixation = stimuli.FixCross()

square = stimuli.Rectangle((50,50), colour=(0,191,255))

control.start(subject_id=1)

fixation.present(clear=True, update=True)

exp.clock.wait(500)

square.present(clear=True, update=True)

exp.keyboard.wait()

control.end()
