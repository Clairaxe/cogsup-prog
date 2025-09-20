from expyriment import design, control, stimuli

exp = design.Experiment(name="Launching")
control.initialize(exp)

# creating the 2 squares
red_square = stimuli.Rectangle((50, 50), colour=(255, 0, 0), position=(-400, 0))
green_square = stimuli.Rectangle((50, 50), colour=(0, 255, 0), position=(0, 0))

control.start()             

# Animate the red square moving right until it reaches the green square
for frame in range(71):
    # Draw both squares at each frame
    red_square.present(clear=True)
    green_square.present(clear=False)
    exp.clock.wait(10)

    # Move red 4 pixels to the right
    red_square.move((5, 0))

# Animate the green square moving right
for frame in range(71):
    # Draw both squares at each frame
    red_square.present(clear=True)
    green_square.present(clear=False)
    exp.clock.wait(10)

    # Move green 4 pixels to the right
    green_square.move((5, 0))

# Final display for 1 second
red_square.present(clear=True)
green_square.present(clear=False)
exp.clock.wait(1000)

control.end()

# with this gap it feels natural.
# however, it's not very modelable 
# (it would be better to do a "while they are not touching: move")