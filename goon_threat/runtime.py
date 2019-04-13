import pygame
import esper
from goon_threat.entities import init_entities
from goon_threat.processors import init_processors

FPS = 60
RESOLUTION = 720, 480

def run():
  pygame.init()
  window = pygame.display.set_mode(RESOLUTION)
  pygame.display.set_caption('Goon Threat')
  clock = pygame.time.Clock()
  pygame.key.set_repeat(1, 1)

  world = esper.World()

  context = {"world": world, "resolution": RESOLUTION, "fps": FPS, "window": window}
  init_entities(context)
  init_processors(context)

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    world.process()
    clock.tick(FPS)
