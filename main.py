# prerequisite: to install pygame 
# to change the speed of the spirit, change the variable initvel

import random
import os
import pygame
import sys
pygame.init()


# os.chdir(r"/Users/admin/Desktop/coding/projects/gdev/snake game/data")




#colors-name=(r,g,b)
#r=red,g=green,b=blue       -take values from 0 to 255
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
g_blue=(0,200,200)
r_green=(255,50,0)





#size
width=1350
height=600


clock=pygame.time.Clock() #for fps



# Creating Window
gamewindow = pygame.display.set_mode((width,height))
#gamewindow=pygame.display.set_mode((0, 0), pygame.FULLSCREEN,pygame.RESIZABLE)
pygame.display.set_caption("Snake Game")




#background songs list
songs=["m1.mp3","m2.mp3","m3.mp3","m4.mp3","m5.mp3"]


#playing music
def playmusic(music_name,volume):
    
    pygame.mixer.init()
    pygame.mixer.music.load(music_name)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()




#Displaying font on screen
def screen_text(text,color,x,y,size):
    font=pygame.font.SysFont('calibri',size)#arg1-name of var arg2-size arg2,3=>bold=,italic=   True or False
    disple=font.render(text,True,color)#render:args-(text to be displayed,antialiance,font color)
    gamewindow.blit(disple,[x,y])#arg1-font,list[x-coordinate,y-coordinate]





#displaying image function
def dimg(image,x,y,width,height):
    bgimg = pygame.image.load(image)
    bgimg = pygame.transform.scale(bgimg, (width,height)).convert_alpha()
    gamewindow.blit(bgimg,(x,y))





#main coding part-gameloop
def gameloop():
    playmusic(random.choice(songs),10)

    

    # plotting snake and increasing its length
    def plot(window,color,lst,s_size):
        for x,y in lst:
            pygame.draw.rect(window,color,[x,y,s_size,s_size])


    #beautify:window
    gamewindow.fill(black) #it will change the background color to the given attribute
    pygame.display.update() #color of window will not change until updated



    
    # Game Specific Variables
    xcord=50 #pos-x
    ycord=200 #pos-y
    s_size=25 #size of snake
    vx=0 #velocity -x comp
    vy=0 #velocity -y comp
    exit_game = False #quit by player
    game_over = False #over and out
    food_x=random.randint(30,int(width-100)) #food x pos
    food_y=random.randint(30,int(height-100)) #food y pos
    score=0 #score
    snk_list=[] #for increasing length
    snk_length=1
    initvel=10
    no_use=0
    # head=[]
    fps=150 #frames changing per second
    #high score
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open('highscore.txt','r') as h:
        hiscr=int(h.read())





    
    # Creating A Game Loop
    while exit_game==False:
        



        
        #gamewindow updation in loop
        

        if exit_game == False:
            dimg("bgimage.jpg",0,0,width,height)




        
        
        
        '''making snake and and its head '''
        #making snake head:shape-rectangle---draw.shape(window name,color of shape,list[x coord,y coord,size of shape])
        #size varies from shape to shape for rectangle breadth and length are required        
        head=[]
        head.append(xcord)
        head.append(ycord)
        snk_list.append(head)
        if len(snk_list)>snk_length:
            del snk_list[0]
        plot(gamewindow,white,snk_list,s_size)




        
        
        #Game over and continue--displaying
        '''colliding with wall'''
        if (xcord<0) or (xcord>width) or (ycord<0) or (ycord>height):
            game_over=True
            
            
        
        '''collapsing with its own head'''
        if head in snk_list[:-1]:
            game_over=True
            
            

        if game_over==True:
            gamewindow.fill(black)
            # bgimg = pygame.image.load("gameover.jpg")
            # bgimg = pygame.transform.scale(bgimg, (width,height)).convert_alpha()
            # gamewindow.blit(bgimg,(0,0))
            dimg('gameover.jpg',0,0,width,height)

            
            screen_text(f'You scored :{score} points',g_blue,450,540,60)
            screen_text('Press Enter to continue or q to quit',white,50,20,70)
            pygame.display.update()
            with open('highscore.txt','w') as f:
                f.write(str(hiscr))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        
                    exit_game=True
                    # pygame.quit()
                    sys.exit()
                    break
                    
                if event.type==pygame.KEYDOWN:

                    #play again
                    
                    if event.key==13:
                        gameloop()
                        break
                    elif event.key==pygame.K_q:
                        
                        exit_game=True
                        sys.exit()
                    elif (no_use<1) and (event.key==pygame.K_q) :
                        pygame.display.update()
                        no_use+=1








        if game_over==False:
            
            #Event loop
            for event in pygame.event.get():
                    
                #event handling
                '''Quit:exit game event'''
                if event.type==pygame.QUIT:
                    exit_game=True
                    pygame.quit()
                    sys.exit()
                    
                    


                '''velocity:for moving the snake and cheat codes'''
                if event.type==pygame.KEYDOWN:#if any key is pressed then head will be executed
                        
                    # #cheatcodes
                    # if event.key==pygame.K_s:# s for increasing score by 10
                    #     score+=10

                    # if event.key==pygame.K_f: # f for getting food at required coordinate
                        
                    #     food_x=xcord +50
                    #     food_y=ycord    
        
                    #moving snake    
                    if event.key == pygame.K_RIGHT:  #moving snake right key
                        vx=initvel
                        vy=0
                    elif event.key == pygame.K_LEFT:#moving snake left key
                        vx=-initvel
                        vy=0
                    elif event.key == pygame.K_UP:#moving snake up arrow key
                        vy=-initvel
                        vx=0
                    elif event.key == pygame.K_DOWN:#moving snake down arrow key
                        vy=+initvel
                        vx=0


                




                
            
                        


            #Drawing random food
            pygame.draw.rect(gamewindow,red,[food_x,food_y,s_size,s_size])




                
            #velocity
            xcord+=vx
            ycord+=vy





            #score and food
            if abs(xcord-food_x)<10 and abs(ycord-food_y)<10:
                score+=10
                food_x=random.randint(30,int(width//3))
                food_y=random.randint(90,int(height//3))
                snk_length+=2
                if score>hiscr:
                    hiscr=score

            screen_text('Score:'+str(score)+'                                 '+'High score:'+str(hiscr),g_blue,25,25,55)




            


                
            

            if game_over==False:
                #updating window frame
                pygame.display.update()
                


                

            #updating frame:window wont update until update() command is run
            #updating window frame at regular interval clock.tick()[clock is in game specific variable]
            clock.tick(fps)#fps-frames per second:frames updated per second         
                    

import sys
#Displaying a welcome screen
def welcome():
    exit_game2 = False
    if exit_game2 == False:
        playmusic(random.choice(songs),10)

    while  exit_game2==False:
        gamewindow.fill((1,1,50))
        screen_text("Welcome",g_blue , 450, 250,80)
        screen_text("Press Space Bar To Play", g_blue, 400, 350,75)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game2 = True
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                    exit_game2 = True
                
        if exit_game2 == True:
            break        
        pygame.display.update()
        clock.tick(60)
        
welcome()                    
pygame.quit()
quit()









