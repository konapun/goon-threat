import pygame
from esper import Processor
from goon_threat.components import Velocity, Renderable

class MovementProcessor(Processor):
  def __init__(self, minx, maxx, miny, maxy):
    super().__init__()
    self.minx = minx
    self.maxx = maxx
    self.miny = miny
    self.maxy = maxy

  def process(self):
    for ent, (vel, rend) in self.world.get_components(Velocity, Renderable):
        # Update the Renderable Component's position by its Velocity:
        rend.x += vel.x
        rend.y += vel.y

        # Adjust the position back inside screen boundaries if the entity tries to go outside:
        rend.x = max(self.minx, rend.x)
        rend.y = max(self.miny, rend.y)
        rend.x = min(self.maxx - rend.w, rend.x)
        rend.y = min(self.maxy - rend.h, rend.y)

class ControllerProcessor(Processor):
  def __init__(self):
    pass

  def process(self):
    pass

class RenderProcessor(Processor):
  def __init__(self, window, clear_color=(0, 0, 0)):
    super().__init__()
    self.window = window
    self.clear_color = clear_color

  def process(self):
    self.window.fill(self.clear_color) # clear the window

    # This will iterate over every Entity that has this Component, and blit it:
    for ent, rend in self.world.get_component(Renderable):
      print("RENDERING RENDERABLE!" + str(rend.x) + ", " + str(rend.y))
      self.window.blit(rend.image, (rend.x, rend.y))
    pygame.display.flip() # flip the framebuffers

def init_processors(context):
  world = context['world']
  resolution_x, resolution_y = context['resolution']

  render_processor = RenderProcessor(window=context['window'])
  movement_processor = MovementProcessor(minx=0, maxx=resolution_x, miny=0, maxy=resolution_y)
  world.add_processor(render_processor)
  world.add_processor(movement_processor)
