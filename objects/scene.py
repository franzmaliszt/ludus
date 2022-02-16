class Scene:
    def __init__(self):
        self.director = None
        self.size = None

    def process_input(self):
        raise NotImplementedError("Need overriding in subclass.")
   
    def update(self):
        raise NotImplementedError("Need overriding in subclass.")

    def render(self):
        raise NotImplementedError("Need overriding in subclass.")
