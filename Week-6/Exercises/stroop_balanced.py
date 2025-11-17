from playsound3 import playsound
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_r, K_b, K_g, K_o
import random

""" Constants """
KEYS = [K_r, K_b, K_g, K_o]
TRIAL_TYPES = ["match", "mismatch"] 
COLORS = [(255,0,0), (0,0,255), (0,255,0), (255,165,0)]
WORDS = ["red", "blue", "green", "orange"]

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 8

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do, F if they don't.\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """Good Answer !"""
FEEDBACK_INCORRECT = """Bad Answer ..."""

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in WORDS}
load([stims[w][c] for w in WORDS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    correct = (key == K_r and color == (255,0,0)) or ( key == K_b and color == (0,0,255)) or (key == K_g and color == (0,255,0)) or (key == K_o and color == (255,165,0))
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    feedback.present()
    feedback_sound = "/home/clairaxe/Cours/Master/CORE1/cogsup-prog/Week-6/OK.mp3" if correct else "/home/clairaxe/Cours/Master/CORE1/cogsup-prog/Week-6/LOSE.mp3"
    playsound(feedback_sound)
    
control.start(subject_id=1)

present_instructions(INSTR_START)
for block_id in range(1, N_BLOCKS + 1):
    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):

        trial_type = random.choice(TRIAL_TYPES)
        r1 = random.randint(0, 3)

        if trial_type == "match":
            color = COLORS[r1]
            word = WORDS[r1]
        else:
            r2 = random.randint(0, 3)
            while r2 == r1:
                r2 = random.randint(0, 3)
            color = COLORS[r1]
            word = WORDS[r2]
             
        run_trial(block_id, trial_id, trial_type, word, color)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)

control.end()