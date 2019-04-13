import pygame

class Controller:
  def __init__(self, entity, bindings):
    self.entity = entity
    self.bindings = bindings

  def process_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        pass
      if event.key == pygame.K_a:
        pass
      if event.key == pygame.K_s:
        pass
      if event.key == pygame.K_d:
        pass
