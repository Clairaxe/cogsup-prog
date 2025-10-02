from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

t0 = exp.clock.time

square.present(clear=True, update=True)

dt = exp.clock.time - t0 
exp.clock.wait(1000 - dt)

fixation.present(clear=False, update=True)
exp.keyboard.wait()

control.end()

# I wasn't sure what was the problem... I changed the code with the clock gestion from your slide and the square appearing first and then the fixation at it's center...
# "The script should plot a fixation inside an empty square but it does something differently", I am not sure I really understood the exercice.