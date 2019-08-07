import turtle
import random
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 4
TIME_STEP = 200
turtle.bgcolor("orchid")

bin1pos_list=[] # the list of the bin's pos
stamp_list=[]
plas_pos=[]
plas_stamps=[]
paper_pos = []
paper_stamps = []

turtle.register_shape("paper.gif")
paper = turtle.clone()
paper.shape("paper.gif")
turtle.register_shape("paper_basket.gif")
paper.hideturtle()


turtle.register_shape("plastic_basket.gif")


bin1= turtle.clone()
bin1.shape("plastic_basket.gif")
bin1.hideturtle()
def new_stamp():
    bin1_pos=bin1.pos()
    #bin1pos_list.append(plas_pos)
    bin1pos_list.append(bin1_pos)
    #plas_stamp=bin1.stamp()
    #stamp_list.append(plas_stamp)
    bin1_stamp=bin1.stamp()
    stamp_list.append(bin1_stamp)
for i in range(START_LENGTH):
    x_pos=bin1.xcor()
    y_pos=bin1.ycor()
    x_pos+=SQUARE_SIZE
    bin1.goto(x_pos,y_pos)
    new_stamp()


def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    bin1.clearstamp(old_stamp) # erase last piece of tail
    bin1pos_list.pop(0) # remove last piece of tail's position
bin1.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def up():
    bin1.direction="Up" #Change direction to up
    print("You pressed the up key!")
#snake.direction = "Up"

def down():
    bin1.direction="Down" #Change direction to up
    print("You pressed the down key!")
#snake.direction = "down"

def right():
    bin1.direction="Right" #Change direction to up
    print("You pressed the right key!")
#snake.direction = "right"

def left():
    bin1.direction="Left" #Change direction to up 
    print("You pressed the left key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.listen()
turtle.register_shape("plas.gif")
plas=turtle.clone()
plas.shape("plas.gif")
## locations of plastic
plas_pos=[]
'''
for this_plas_pos in plas_pos :
    plas.goto(this_plas_pos)
    plas_stamps.append(plas.stamp())
'''
def make_plastic():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    plas_x = random.randint(min_x,max_x)*SQUARE_SIZE
    plas_y = random.randint(min_y,max_y)*SQUARE_SIZE
    plas.goto(plas_x,plas_y)
    plas_pos.append(plas.pos())
    plas_stamps.append(plas.stamp())
    

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

for k in range (1):
    make_plastic()
    plas.hideturtle()


def move_bin():
    my_pos = bin1.pos()
    global paper_pos

    #bin1pos_list.append(my_pos)


    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = bin1.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    if new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    if new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    if new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()

        


   


    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if bin1.direction == "Up":
        bin1.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif bin1.direction=="Down":
        bin1.goto(x_pos, y_pos - SQUARE_SIZE)
    
    elif bin1.direction=="Right":
        bin1.goto(x_pos +SQUARE_SIZE, y_pos)
    elif bin1.direction=="Left":
        bin1.goto(x_pos-SQUARE_SIZE,y_pos)

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5
    if bin1.pos() in plas_pos:
        plas_index=plas_pos.index(bin1.pos()) #What does this do?
        plas.clearstamp(plas_stamps[plas_index]) #Remove eaten food stamp
        plas_pos.pop(plas_index) #Remove eaten food position
        plas_stamps.pop(plas_index) #Remove eaten food stamp
        
        print(plas_pos)
        print(plas_stamps)
        print("You have eaten the plastic!")
    else:
        remove_tail()
    

        

    #remove the last piece of the snake (Hint Functions are FUN!)
    '''
    if len(plas_stamps)<3:
        make_plastic()
        
    '''
    x = 1
    
    if (len(plas_pos)) == 0 and x == 1:
        make_plastic()
        bin1.shape("paper_basket.gif")
        paper_pos = [(200,-100), (-200,100), (-100,300), (100,-100), (-100, 500), (-140, 220)]
        print (bin1.pos())
        print("%%%%%%%%%")
    
        for this_paper_pos in paper_pos :
            paper.goto(this_paper_pos)
            paper_stamp=paper.stamp()
            paper_stamps.append(paper_stamp)
            print(paper_stamps)
            paper.hideturtle()
        x = 2
    if bin1.pos() in paper_pos:
        print("**&&&&%%%$$$$$") 
        print('condition satisfied')
        paper_index=paper_pos.index(bin1.pos()) #What does this do?
        paper.clearstamp(paper_stamps[paper_index]) #Remove eaten food stamp
        paper_pos.pop(paper_index) #Remove eaten food position
        paper_stamps.pop(paper_index) #Remove eaten food stamp
        print('you have touched the paper')
        print(paper_stamps)
        print(paper_pos)
    if len((paper_pos)) > 0 and bin1.pos() in plas_pos:
            print("you can't put plastic in the paper bin!!")
            quit()
            
        #x += 1
    turtle.ontimer(move_bin,TIME_STEP)



move_bin()

turtle.mainloop()
    

    
    

