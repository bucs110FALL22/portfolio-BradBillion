from Rectangle import Rectangle

class Surface():

    def __init__(self, filename, x, y, h, w):
        for n in x, y, h, w:
            if n < 0:
                n = 0
        self.rect = Rectangle(x,y,w,h)
        self.image = str(filename)

    def getRect(self):
      # returns the rectangle object
      return self.rect
