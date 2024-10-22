import os
import pygame
from pygame.locals import *

class Button:

    def __init__(self,x,y,width,height,text,button_color,text_color,font_size):
        self.rectangle=pygame.Rect(x,y,width,height)
        self.text = text
        self.button_color=button_color
        self.text_color = text_color
        self.font_size = font_size

    def draw(self,screen):
        pygame.draw.rect(screen,self.button_color,self.rectangle)
        directory = os.path.dirname(__file__)
        font_path = os.path.join(directory, 'font', "RadiantKingdom-m5LeV.ttf")
        font = pygame.font.SysFont(font_path,self.font_size)
        text = font.render(self.text, True, self.text_color) 
        text_rect = text.get_rect(center=self.rectangle.center)
        screen.blit(text, text_rect)
    
    def is_clicked(self, pos):
        return self.rectangle.collidepoint(pos)
    
class CheckBox:

    def __init__(self,x,y,width,height,checkbox_color,color_select,color_unselect,border_width):
        # Useful to draw if see it is clicked!
        self.rectangle=pygame.Rect(x+(border_width/2),y+(border_width/2),width-(border_width),height-(border_width))

        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.checkbox_color = checkbox_color
        self.color_select = color_select
        self.color_unselect = color_unselect
        self.border_width = border_width
        self.selected = False

    def draw(self,screen):
        # Draw top border
        pygame.draw.line(screen, self.checkbox_color, (self.x, self.y), (self.x + self.width, self.y), self.border_width)
        # Draw bottom border
        pygame.draw.line(screen, self.checkbox_color, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), self.border_width)
        # Draw left border
        pygame.draw.line(screen, self.checkbox_color, (self.x, self.y), (self.x, self.y + self.height), self.border_width)
        # Draw right border
        pygame.draw.line(screen, self.checkbox_color, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), self.border_width)
        pygame.display.flip()
    def is_clicked(self, screen, pos):
        if self.rectangle.collidepoint(pos) and self.selected:
            pygame.draw.rect(screen,self.color_unselect,self.rectangle)
            self.selected = False
            pygame.display.flip()
            return True
        elif self.rectangle.collidepoint(pos) and (not self.selected):
            self.selected = True
            pygame.draw.rect(screen,self.color_select,self.rectangle)
            pygame.display.flip()
            return True
        else:
            return False

class ClickableArrow:
    def __init__(self, screen, x, y, width, height, direction):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.color = (0,0, 255)
    
    def draw(self):
        if self.direction == "right":
            pygame.draw.polygon(self.screen, self.color, [
                (self.x, self.y),
                (self.x - self.width, self.y - self.height // 2),
                (self.x - self.width, self.y + self.height // 2)
            ])
        elif self.direction == "left":
            pygame.draw.polygon(self.screen, self.color, [
                (self.x, self.y),
                (self.x + self.width, self.y - self.height // 2),
                (self.x + self.width, self.y + self.height // 2)
            ])
        elif self.direction == "up":
            pygame.draw.polygon(self.screen, self.color, [
                (self.x, self.y),
                (self.x - self.width // 2, self.y + self.height),
                (self.x + self.width // 2, self.y + self.height)
            ])
        elif self.direction == "down":
            pygame.draw.polygon(self.screen, self.color, [
                (self.x, self.y),
                (self.x - self.width // 2, self.y - self.height),
                (self.x + self.width // 2, self.y - self.height)
            ])
    
    def is_clicked(self, mouse_pos):
        if self.direction in ["right", "left"]:
            if self.direction == "right":
                if self.x - self.width <= mouse_pos[0] <= self.x and self.y - self.height // 2 <= mouse_pos[1] <= self.y + self.height // 2:
                    return True
            elif self.direction == "left":
                if self.x <= mouse_pos[0] <= self.x + self.width and self.y - self.height // 2 <= mouse_pos[1] <= self.y + self.height // 2:
                    return True
        elif self.direction in ["up", "down"]:
            if self.direction == "up":
                if self.x - self.width // 2 <= mouse_pos[0] <= self.x + self.width // 2 and self.y <= mouse_pos[1] <= self.y + self.height:
                    return True
            elif self.direction == "down":
                if self.x - self.width // 2 <= mouse_pos[0] <= self.x + self.width // 2 and self.y - self.height <= mouse_pos[1] <= self.y:
                    return True
        return False


