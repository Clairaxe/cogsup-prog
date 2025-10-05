from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE

# ---------- Fonctions ----------

def load(stims):
    for stim in stims:
        stim.preload()


def timed_draw(stims, canvas): # retour de timed_draw pour bien reprendre la logique de temps exact
    canvas.clear_surface()
    t0 = exp.clock.time
    for stim in stims:
        stim.plot(canvas)
    t1 = exp.clock.time
    canvas.present()
    return t1 - t0


def present_for(stims, canvas, n_frames=5):
    target_time = n_frames * (1000/60.0) # convertir en ms
    dt = timed_draw(stims, canvas)
    remaining = target_time - dt
    if remaining > 0:
        exp.clock.wait(remaining)


def make_circles(radius=50, preload=True):
    """Créer les cercles A et B (jaune se déplace, rouge et bleu restent fixes)"""
    pos_yel_A = -225
    pos_yel_B = 225
    pos_red = -75
    pos_blue = 75

    yel_A = stimuli.Circle(radius=radius, position=(pos_yel_A, 0), colour=(0, 0, 0))
    yel_B = stimuli.Circle(radius=radius, position=(pos_yel_B, 0), colour=(0, 0, 0))
    red = stimuli.Circle(radius=radius, position=(pos_red, 0), colour=(0, 0, 0))
    blue  = stimuli.Circle(radius=radius, position=(pos_blue, 0),  colour=(0, 0, 0))

    if preload:
        load([yel_A, yel_B, red, blue])

    frame_A = [yel_A, red, blue]
    frame_B = [yel_B, red, blue]

    return frame_A, frame_B


def add_tags(frameA, frameB, tag_radius):
    colours = [(225, 225, 0), (255, 0, 0), (0, 0, 255)]

    # jaune dans A et B
    tag_yel = stimuli.Circle(radius=tag_radius, colour=colours[0], position=(0, 0))
    tag_yel.plot(frameA[0]); frameA[0].preload()
    tag_yel.plot(frameB[0]); frameB[0].preload()

    # rouge (toujours frameA[1] == frameB[1])
    tag_red = stimuli.Circle(radius=tag_radius, colour=colours[1], position=(0, 0))
    tag_red.plot(frameA[1]); frameA[1].preload()

    # bleu (toujours frameA[2] == frameB[2])
    tag_blue = stimuli.Circle(radius=tag_radius, colour=colours[2], position=(0, 0))
    tag_blue.plot(frameA[2]); frameA[2].preload()

    return frameA, frameB


# ---------- Ternus trial ----------
# je ne suis pas certaine d'avoir compris la différence entre: 
# - ISI currently controls is how long the circles are shown on-screen
# - ISI should control the amount of blank frames in-between.
# je vais donc rajouter un canvas blanc qui va apparaître pendant un certain nb de frames (ISI)

def run_trial(radius=50, isi_frames=3, color_tag=False, n_cycles=10):
    A, B = make_circles(radius, preload=not color_tag)
    if color_tag:
        A, B = add_tags(A, B, radius//5)

    #ajout du dit blank frame
    blank = stimuli.BlankScreen(colour=(255,255,255))
    blank.preload()

    while True:
        present_for(A, canvas, 9)   # ~150 ms
        if isi_frames > 0: present_for([], blank, isi_frames) #présente le blank frame pendant isi_frame
        present_for(B, canvas, 9)
        if isi_frames > 0: present_for([], blank, isi_frames)
        if exp.keyboard.check(K_SPACE):
            return


# ---------- Main ----------

exp = design.Experiment(name="Ternus Illusion")
control.set_develop_mode()
control.initialize(exp)

canvas = stimuli.Canvas(exp.screen.size, colour=(255,255,255 ))

# 1. Element motion (low ISI, pas de tags)
run_trial(radius=50, isi_frames=0, color_tag=False)

# 2. Group motion (high ISI, pas de tags)
run_trial(radius=50, isi_frames=18, color_tag=False)

# 3. Element motion (high ISI + tags)  
run_trial(radius=50, isi_frames=18, color_tag=True)

control.end()