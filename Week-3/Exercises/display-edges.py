from expyriment import design, control, stimuli
from expyriment.misc import geometry
control.set_develop_mode()
exp = design.Experiment(name = "Display Edges")
control.initialize(exp)

screen_width, screen_heigth = exp.screen.size
square_size = int(screen_width/20)

# idée: faire un frame (comme ça je peux avoir un contour rouge qui n'existe pas dans la classe Rectangle)
square_1 = stimuli.Shape(vertex_list= geometry.vertices_frame(size=[square_size,square_size], frame_thickness=1), debug_contour_colour=(255,0,0),position=(-screen_width/2+square_size/2,screen_heigth/2-square_size/2))
square_2 = stimuli.Shape(vertex_list= geometry.vertices_frame(size=[square_size,square_size], frame_thickness=1), debug_contour_colour=(255,0,0),position=(-screen_width/2+square_size/2,-screen_heigth/2+square_size/2))
square_3 = stimuli.Shape(vertex_list= geometry.vertices_frame(size=[square_size,square_size], frame_thickness=1), debug_contour_colour=(255,0,0),position=(screen_width/2-square_size/2,screen_heigth/2-square_size/2))
square_4 = stimuli.Shape(vertex_list= geometry.vertices_frame(size=[square_size,square_size], frame_thickness=1), debug_contour_colour=(255,0,0),position=(screen_width/2-square_size/2,-screen_heigth/2+square_size/2))

# en fait on peut juste changer la taille de line_width et assigner une couleur et ce sera uniquement les contours et pas le contenu qui sera de cette couleur
# je me suis donc pris la tête et je n'ai pas assez bien lu la documentation

control.start(subject_id=1)

square_1.present(clear=True, update=False)
square_2.present(clear=False, update=False)
square_3.present(clear=False, update=False)
square_4.present(clear=False, update=True)


exp.keyboard.wait()

control.end()
