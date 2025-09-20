from expyriment import design, control, stimuli


def launching(temporal_gap=0, spatial_gap=0, green_speed=1):

    control.set_develop_mode()
    exp = design.Experiment(name="Launching")
    control.initialize(exp)

    # Create two squares:
    # Red starts 400 px left from center, green at center + possible spatial gap
    red_square = stimuli.Rectangle((50, 50), colour=(255, 0, 0), position=(-400, 0))
    green_square = stimuli.Rectangle((50, 50), colour=(0, 255, 0), position=(0, 0))

    control.start()

    # Animate red square moving right until it reaches green square
    while red_square.position[0] + 50 < green_square.position[0]:
        red_square.move((5, 0))
        red_square.present(clear=True)
        green_square.present(clear=False)
        exp.clock.wait(10)

    # Collision moment
    red_square.present(clear=True)
    green_square.present(clear=False)
    exp.clock.wait(temporal_gap)

    # Animate green square moving right
    steps = int((400) / (5 * green_speed))
    for _ in range(steps):
        green_square.move((5 * green_speed, 0))
        red_square.present(clear=True)
        green_square.present(clear=False)
        exp.clock.wait(10)

    # Hold final display for 1 second
    red_square.present(clear=True)
    green_square.present(clear=False)
    exp.clock.wait(1000)

    control.end()


# Michottean launching
launching(temporal_gap=0, spatial_gap=0, green_speed=1)

# Temporal gap
launching(temporal_gap=1000, spatial_gap=0, green_speed=1)

# Spatial gap
launching(temporal_gap=0, spatial_gap=20, green_speed=1)

# Triggering
launching(temporal_gap=0, spatial_gap=0, green_speed=3)

"""
Displays a launching event with configurable parameters.

temporal_gap : int
    Time in ms between collision and green square movement.
spatial_gap : int
    Extra distance in pixels between red and green square at the start.
green_speed : float
    Relative speed of the green square (1 = same as red, >1 = faster).
"""