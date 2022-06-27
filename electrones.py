from manim import *
import itertools as it
class Vibrating(VGroup):
    CONFIG={
        'amplitude':0.5,
        'jingle_per_second':1,
        'colors':[RED,YELLOW,GREEN,BLUE,PURPLE,ORANGE]
    }
    def __init__(self,group,**kwargs):
        VGroup.__init__(self,**kwargs)
        colors=it.cycle(self.CONFIG['colors'])
        for submob in group.submobjects:
            submob.jingling_direction=rotate_vector(RIGHT,np.random.random()*TAU)
            submob.jingling_amplitude=self.CONFIG['amplitude']*np.random.random()
            submob.jingling_phase=np.random.random()*TAU
            submob.set_color(next(colors))
            self.add(submob)
        self.add_updater(lambda m,dt:m.update(dt))
    def update(self,dt):
        for submob in self.submobjects:
            submob.jingling_phase+=np.random.random()*TAU
            submob.shift(submob.jingling_amplitude*np.sin(submob.jingling_phase))
            submob.rotate(submob.jingling_phase)
class Proving(Scene):
    def construct(self):
        elementos=Vibrating(VGroup(*[Square() for i in range(10)]))
        elementos.arrange(RIGHT,buff=0.5)
        elementos_con_numeros=self.number_of_elements(elementos)
        self.add(elementos_con_numeros)
        self.wait(3)
    def number_of_elements(self,mobs):
        for i in range(len(mobs)):
            texto=Integer(i)
            texto.set_color(WHITE)
            texto.move_to(mobs[i].get_center())
            mobs[i].add(texto)
        return mobs