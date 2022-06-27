from manim import *
class Vibrating(VGroup):
    CONFIG={
        'amplitude':0.5,
        'jingle_per_second':1,
    }
    def __init__(self,group,**kwargs):
        VGroup.__init__(self,**kwargs)
        for submob in group.submobjects:
            submob.jingling_direction=rotate_vector(RIGHT,np.random.random()*TAU)
            submob.jingling_amplitude=self.CONFIG['amplitude']*np.random.random()
            submob.jingling_phase=np.random.random()*TAU
            self.add(submob)
        self.add_updater(lambda m,dt:m.update(dt))
    def update(self,dt):
        for submob in self.submobjects:
            submob.jingling_phase+=np.random.random()*TAU
            submob.shift(submob.jingling_amplitude*np.sin(submob.jingling_phase))
class Proving(Scene):
    def construct(self):
        elementos=Vibrating(VGroup(*[Square() for i in range(10)]))
        elementos.arrange(RIGHT,buff=0.5)
        self.add(elementos)
        self.wait(2)