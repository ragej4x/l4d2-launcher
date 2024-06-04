import pygame as pg
import gif_pygame
import random
import os
import requests
import pyi_splash
import time, sys
time.sleep(5)
pyi_splash.close()

url = "https://raw.githubusercontent.com/ragej4x/text-db/main/db.txt"
response = requests.get(url)


#L4D2 LAUNCHER

window = pg.display.set_mode((820, 820/2))
pg.display.set_icon(pg.image.load("assets/ico.png"))
#pg.display.set_caption("L4D LAUNCHER                                                      @aczontongao")
clock = pg.time.Clock()

#ASSET
l4d_bg = "assets/l4d-bg.gif"
l4d_logo = "assets/l4d-gif.gif"

#LOAD
l4d_bg = gif_pygame.load(l4d_bg)
l4d_logo = gif_pygame.load(l4d_logo)
pg.init()
class button_class():
    def __init__(self, x ,y, text, text_size):
        self.x = x
        self.y = y
        self.clicked = False
        #self.width , self.height = width , height
        self.color = 255,255,255
        self.text = text
        #self.text_col = text_col
        self.size = text_size
        self.text_color = None
        self.tex_col = 200,200,200
    def render_button(self, get_event):
        #TEXT
        font = pg.font.Font("assets/BLOODY.ttf", self.size)
        text = font.render(self.text, True , self.tex_col)
        
        #BOX
        mx , my = pg.mouse.get_pos()
        #mouse = pg.mouse.get_pressed()[0]
        mouse_box = pg.Rect((mx,my ,1 ,1))
        button = pg.Rect((self.x ,self.y,  len(self.text) * self.size//1.9, self.size))
        #pg.draw.rect(window, self.color, button)

        if event in get_event:
            if mouse_box.colliderect(button) == True:
                self.tex_col = 150,0,0
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.clicked = True
                    #print("CLICKED", self.clicked)
            else:
                self.clicked = False
                self.tex_col = 200,200,200
            #print(self.clicked)
        


        window.blit(text, (self.x, self.y))


txt_msg = None
start_button = button_class(40, 50, "Start", 68)
update_button = button_class(70, 170, "Update", 38)
msg = button_class(70, 350, f"Message And Updates from =)\n Aczontongao", 18)
owner = button_class(520, 5, f"MIT LICENSE (JIMBOY TONGAO, 2024)", 18)

readmsg = False


while True:

    window.fill(0)
    get_event = pg.event.get()
    for event in get_event:
        if event.type == pg.QUIT:
            pg.quit() # quits pygame
            sys.exit()
            
    if update_button.clicked == True:
        os.startfile("update.exe")
        os._exit(os.EX_OK)
        time.sleep(1)

    if start_button.clicked == True:
        path = os.path.join('game' , 'os.exe')
        os.startfile(path)
        os._exit(os.EX_OK)
        pg.quit() # quits pygame
        sys.exit()


    if msg.clicked == True:
        readmsg = True


    window.blit(l4d_logo.blit_ready(), (190,- 50))
    #window.blit(l4d_bg.blit_ready(), (300,0))
    #BUTTONS
    start_button.render_button(get_event)
    update_button.render_button(get_event)
    msg.render_button(get_event)
    owner.render_button(get_event)


    #if readmsg == True:

    if response.status_code == 200:
        print("Contents of db.txt:")
        print(response.text)
        msg_cont = button_class(380, 250, f"{response.text}", 18)
        msg_cont.render_button(get_event)
    else:
        print(f"Error fetching data. Status code: {response.status_code}")


    pg.display.set_caption(f"L4D LAUNCHER                                                                           { random.randint(10,90) }    | ACZON TONGAO |   { random.randint(10,90) }")
    pg.display.flip()   
    clock.tick(60)
