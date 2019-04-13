class Renderable:
  def __init__(self, image, posx, posy, depth=0):
    self.image = image
    self.depth = depth
    self.x = posx
    self.y = posy
    self.w = image.get_width()
    self.h = image.get_height()

class Velocity:
  def __init__(self, x=0.0, y=0.0):
    self.x = x
    self.y = y

class Animated:
  def __init__(self, spritesheet):
    pass

class Controlled:
  def __init__(self, ):
    pass

class Collidable:
  def __init__(self, ):
    pass
