import pygame
from goon_threat.components import Renderable, Velocity

class Character:
  def __init__(self, x, y, image_path):
    self.components = [Renderable(image=pygame.image.load(image_path), posx=x, posy=y), Velocity(x=0, y=0)]

def init_entities(context):
  def load_entity(entity):
    world = context.get('world')
    world_entity = world.create_entity()
    for component in entity.components:
      world.add_component(world_entity, component)
    return world_entity

  return list(map(load_entity, [Character(100, 100, '/Users/konapun/Documents/Projects/goon-threat/goon_threat/resource/spritesheet/bluesquare.png')]))
