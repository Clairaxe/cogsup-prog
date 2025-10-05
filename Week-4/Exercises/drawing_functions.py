from expyriment import design, control, stimuli
import random

'''
1. `load`: preload the stimuli passed as input
2. `timed_draw`: draw a list of (preloaded) stimuli on-screen, return the time it took to execute the drawing
3. `present_for`: draw and keep stimuli on-screen for time *t* in ms (be mindful of edge cases!)
'''

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(stims, canvas): 
    canvas.clear_surface()
    t0 = exp.clock.time
    for stim in stims: 
        stim.plot(canvas)
    t1 = exp.clock.time
    canvas.present()
    return (t1 - t0)

def present_for(stims, canvas, t=1000):
    draw_time = timed_draw(stims, canvas)
    if t - draw_time > 0:
        exp.clock.wait(t - draw_time)

""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

width, height = exp.screen.size
canvas = stimuli.Canvas((width, height))

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, canvas, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()

''' 
Le résultat que j'obtiens:
[505, 502, 501, 502, 502, 502, 502, 502, 502, 503, 502, 502, 501, 503, 501, 503, 502, 501, 503, 501]
'''