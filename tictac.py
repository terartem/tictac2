from pygame import *
window = display.set_mode((600,600))
display.set_caption('Крестики-нолики')
fon = transform.scale(image.load("fon_tictac.png"),(600,600))


clock = time.Clock()
FPS = 60




class Wall(sprite.Sprite):
    def __init__(self,color,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))




wall1 = Wall((0, 0, 0),0,0,30,600)
wall2 = Wall((0, 0, 0),570,0,30,600)
wall3 = Wall((0, 0, 0),0,0,600,30)
wall5 = Wall((0, 0, 0),190,0,30,600)
wall6 = Wall((0, 0, 0),390,0,30,600)
wall7 = Wall((0, 0, 0),0,200,600,30)
wall8 = Wall((0, 0, 0),0,400,600,30)






window.blit(fon,(0,0))


finish = False
game = True
while game:
    if finish != True:
        

    











        
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
    






    for e in event.get():
        if e.type == QUIT:
            game =  False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            window.blit(image.load('krestik.png'),(x,y))
        if e.type == MOUSEBUTTONDOWN and e.button == 3:
            x, y = e.pos
            window.blit(image.load('nolik.png'),(x,y))



    clock.tick(FPS)
    display.update()