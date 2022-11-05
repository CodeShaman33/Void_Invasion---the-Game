import pygame.font

class Button:

    def __init__(self, game, msg, position):

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.position = position
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 5)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        #self.rect.center = self.screen_rect.center



        self._msg(msg)

    def _msg(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)