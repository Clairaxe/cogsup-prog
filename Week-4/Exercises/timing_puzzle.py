from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

t0 = exp.clock.time 
fixation.present() 
dt = exp.clock.time - t0 
exp.clock.wait(1000 - dt) 

t1 = exp.clock.time 
text.present() 
fix_duration = (t1 - t0)/1000

exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()

from expyriment import design, control, stimuli
import random

'''
1. `load`: preload the stimuli passed as input
2. `timed_draw`: draw a list of (preloaded) stimuli on-screen, return the time it took to execute the drawing
3. `present_for`: draw and keep stimuli on-screen for time *t* in ms (be mindful of edge cases!)
'''

def load(stims):
    for stim in stims :
        stim.preload()

def timed_draw(stims):
    t0 = exp.clock.time
    for stim in stims :
        stim.draw()
    t1 = exp.clock.time
    return (t1-t0)

def present_for(stims, t=1000):
    for stim in stims:
        stim.present()
        exp.clock.wait(t)

""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 10
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()