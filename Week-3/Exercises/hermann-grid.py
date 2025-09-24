from expyriment import design, control, stimuli
control.set_develop_mode()

def hermann_grid(size, colour_square, space, nb_row, nb_col, colour_screen):
    exp = design.Experiment(name="Hermann Grid", background_colour=colour_screen)
    control.initialize(exp)

    total_width = nb_col * size + (nb_col - 1) * space
    total_height = nb_row * size + (nb_row - 1) * space

    squares = []

    for i in range(nb_row):
        for j in range(nb_col):
            #compute center positions
            x = j * (size + space) - total_width // 2 + size // 2
            y = i * (size + space) - total_height // 2 + size // 2
            rect = stimuli.Rectangle(size=(size, size), colour=colour_square, position=(x, y))
            squares.append(rect)

    control.start(subject_id=1)

    for k, sq in enumerate(squares):
        sq.present(clear=(k == 0), update=(k == len(squares) - 1))
        #that way we have the first (clear=True,update=False) and the last (clear=False,update=True)

    exp.keyboard.wait()
    control.end()


size = 100
colour_square = (0, 0, 0)
space = 20
nb_row = 5
nb_col = 5
colour_screen = (255, 255, 255)

hermann_grid(size=size, colour_square=colour_square, space=space, nb_row=nb_row, nb_col=nb_col, colour_screen=colour_screen)
