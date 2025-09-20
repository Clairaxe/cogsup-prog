'''## Exercise 4: Labeled shapes
3. Add 50px-long and 3px-wide white vertical lines going upwards from the top of each shape. 
4. Add shape labels on top of the line segments ("triangle" and, respectively, "hexagon"), 20px away from the upper end of the segments. 
The color of the font should be white.

Hints:
- To find out how to present polygons, lines, and text of various kinds, check out expyriment's documentation:
    - ```Shape``` [documentation](https://docs.expyriment.org/expyriment.stimuli.Shape.html), in particular the **Notes** under ```__init__```
    - ```Line``` [documentation](https://docs.expyriment.org/expyriment.stimuli.Line.html)
    - ```TextLine``` [documentation](https://docs.expyriment.org/expyriment.stimuli.TextLine.html)
'''

from expyriment import design, control, stimuli
from expyriment.misc import geometry

control.set_develop_mode()

exp = design.Experiment(name = "Shapes")

control.initialize(exp)

purple_triangle = stimuli.Shape(vertex_list = geometry.vertices_triangle(60,50,50), colour=(255,0,255), position=(-100,0))
yellow_hex = stimuli.Shape(vertex_list = geometry.vertices_regular_polygon(6,28.9), colour=(255,255,0), position=(100,0))
line_tri = stimuli.Line(start_point=(-100, 25), end_point=(-100, 75),line_width=3, colour=(255,255,255))
line_hex = stimuli.Line(start_point=(100,25), end_point=(100, 75),line_width=3, colour=(255,255,255))
text_tri = stimuli.TextLine(text="triangle", position=(-100, 95), text_colour=(255,255,255))
text_hex = stimuli.TextLine(text="hexagon", position=(100,95), text_colour=(255,255,255))

control.start(subject_id=1)

purple_triangle.rotate(180,True)
purple_triangle.present(clear=True, update=False)
yellow_hex.present(clear=False, update=False)
line_hex.present(clear=False, update=False)
line_tri.present(clear=False, update=False)
text_hex.present(clear=False, update=False)
text_tri.present(clear=False, update=True)


exp.keyboard.wait()

control.end()
