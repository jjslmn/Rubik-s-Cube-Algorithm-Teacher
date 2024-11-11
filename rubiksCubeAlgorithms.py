import time
import sys
import graphics as g
win = g.GraphWin("Rubiks Cubes", 550, 900 )
#global variables
choice = ''
cycle = ''
key = ''
x = 0
textBox4= g.Text(g.Point(0, 0), '')
text = g.Text(g.Point(0,0), '')
#putting the algorithms into a dictionary
AlgorithmsOLL = {'Line':'FRUrufz' , 'Lshape': 'FRUrufz', 'Dot': 'FRUruRUrufz', 'Sune': 'RUruRkrz', 'Antisune': 'luLulkLz', 'H': 'FRUruRUruRUrufz', 'Pi': 'RkRktututkRz', 'L': 'rFRbruRBz', 'T': 'LFrflFRfz', 'U': 'tDrkRdrkrz'}
algNameList = list(AlgorithmsOLL.keys())
algList = list(AlgorithmsOLL.values())
#F = F
#f = F'
#R = R
#r = R'
#t = R2
#L = L
#l = L'
#U = U
#u = U'
#k = U2
#D = D
#d = D'
#b = B' Move the back side(oppisite face) to the right
#B = B Move the back side(oppisite face) to the left
#z = random character to end the loop

def Menu():
    global choice, textBox4, cycle, key
    textBox1 = g.Text(g.Point(196, 60), "*****2-Look OLL Rubiks Cube Algorithms*****")
    textBox1.draw(win)
    y = 95
    i = 1
#cycles throught the dictionary and prints out all of the Keys
    for x in AlgorithmsOLL:
        textBox = g.Text(g.Point(170, y), str(i) + ". " + str(x) + "\n")
        textBox.draw(win)
        y = y + 20
        i = i + 1
    textBox2 = g.Text(g.Point(170, y-10), str(i) + ". Quit")
    y = y + 20
    textBox3 = g.Text(g.Point(260, y), "Please enter in your choice as a number and left click using your mouse")
    y = y + 25
    entryBox = g.Entry(g.Point(170,y),5)
    y = y + 30
    textBox2.draw(win)
    textBox3.draw(win)
    entryBox.draw(win)
    win.getMouse()
    textBox4.move(2000,0)
    choice = entryBox.getText()
#error trapping the choice making sure that the answer is an integer
    try:
        answer = int(choice)-1
        if answer == i-1:
            #to quit function
            sys.exit()
        elif answer < i:
            textBox4 = g.Text(g.Point(130, y+10), 'You chose: ' + algNameList[answer])
            textBox4.draw(win)
            cycle = algList[answer]
            key = algNameList[answer]
            Cube()
        elif answer >= i:
            textBox4 = g.Text(g.Point(220, y), "'" + str(choice) + "' is not an acceptable choice. Try again.")
            textBox4.draw(win)
            Menu()
    except ValueError:
        textBox4 = g.Text(g.Point(220, y), "'" + str(choice) + "' is not an acceptable choice. Try again.")
        textBox4.draw(win)
        Menu()



    # Handle user input
    choice = entryBox.getText()
    try:
        answer = int(choice) - 1
        if answer == i - 1:
            # Quit the program
            sys.exit()
        elif answer < i:
            key = algNameList[answer]
            cycle = AlgorithmsOLL[key]
            Cube()
        else:
            raise ValueError
    except ValueError:
        error_text = g.Text(g.Point(220, y), f"'{choice}' is not an acceptable choice. Try again.")
        error_text.draw(win)
        Menu()

#Draws out the cube
def Cube():
    #left side
    topLleft = g.Rectangle(g.Point(50,500), g.Point(100,550))
    topLright = g.Rectangle(g.Point(150,500), g.Point(200,550))
    ltr = g.Rectangle(g.Point(50,500), g.Point(200,550))
    lmr = g.Rectangle(g.Point(50,550), g.Point(200,600))
    lm = g.Rectangle(g.Point(100,500), g.Point(150,650))
    lbr = g.Rectangle(g.Point(50,600), g.Point(200,650))
    #middle face
    Mleft = g.Rectangle(g.Point(200,500), g.Point(250,550))
    Mright = g.Rectangle(g.Point(300,500), g.Point(350,550))
    tr = g.Rectangle(g.Point(200,500), g.Point(350,550))
    mr = g.Rectangle(g.Point(200,550), g.Point(350,600))
    m = g.Rectangle(g.Point(250,500), g.Point(300,650))
    br = g.Rectangle(g.Point(200,600), g.Point(350,650))
    #top face
    ttlcorner = g.Rectangle(g.Point(200,350), g.Point(250,400))
    ttmcorner = g.Rectangle(g.Point(250,350), g.Point(300,400))
    ttrcorner = g.Rectangle(g.Point(300,350), g.Point(350,400))
    tmlcorner = g.Rectangle(g.Point(200,400), g.Point(250,450))
    tmmcorner = g.Rectangle(g.Point(250,400), g.Point(300,450))
    tmrcorner = g.Rectangle(g.Point(300,400), g.Point(350,450))
    tblcorner = g.Rectangle(g.Point(200,450), g.Point(250,500))
    tbmcorner = g.Rectangle(g.Point(250,450), g.Point(300,500))
    tbrcorner = g.Rectangle(g.Point(300,450), g.Point(350,500))
    #right face
    topRleft = g.Rectangle(g.Point(350,500), g.Point(400,550))
    topRright = g.Rectangle(g.Point(450,500), g.Point(500,550))
    rtr = g.Rectangle(g.Point(350,500), g.Point(500,550))
    rmr = g.Rectangle(g.Point(350,550), g.Point(500,600))
    rmm = g.Rectangle(g.Point(400,500), g.Point(450,650))
    rbr = g.Rectangle(g.Point(350,600), g.Point(500,650))
    
#drawing them out
    #middle
    Mleft.draw(win)
    Mright.draw(win)
    tr.draw(win)
    mr.draw(win)
    m.draw(win)
    br.draw(win)
    #right
    topRright.draw(win)
    topRleft.draw(win)
    rtr.draw(win)
    rmr.draw(win)
    rmm.draw(win)
    rbr.draw(win)
    #top
    ttlcorner.draw(win)
    ttmcorner.draw(win)
    ttrcorner.draw(win)
    tmlcorner.draw(win)
    tmmcorner.draw(win)
    tmrcorner.draw(win)
    tblcorner.draw(win)
    tbmcorner.draw(win)
    tbrcorner.draw(win)
    #left
    topLleft.draw(win)
    topLright.draw(win)
    ltr.draw(win)
    lmr.draw(win)
    lm.draw(win)
    lbr.draw(win)
    
#plotting key reference points    
    textBox = g.Text(g.Point(100, 420), 'Your reference points are\nin yellow')
    textBox.draw(win)
    if key == algNameList[0]:
        tmlcorner.setFill('yellow')
        tmmcorner.setFill('yellow')
        tmrcorner.setFill('yellow')
    elif key == algNameList[1]:
        tbmcorner.setFill('yellow')
        tmmcorner.setFill('yellow')
        tmrcorner.setFill('yellow')
    elif key == algNameList[2]:
        tmmcorner.setFill('yellow')
    elif key == algNameList[4]:
        Mleft.setFill('yellow')
        tbrcorner.setFill('yellow')
    elif key == algNameList[3]:
        tblcorner.setFill('yellow')
        Mright.setFill('yellow')
    elif key == algNameList[5]:
        Mleft.setFill('yellow')
        Mright.setFill('yellow')
    elif key == algNameList[6]:
        Mright.setFill('yellow')
        topLleft.setFill('yellow')
        topLright.setFill('yellow')
    elif key == algNameList[7]:
        ttlcorner.setFill('yellow')
        tbrcorner.setFill('yellow')
        Mleft.setFill('yellow')
        topRright.setFill('yellow')
    elif key == algNameList[8]:
        ttrcorner.setFill('yellow')
        ttlcorner.setFill('yellow')
        Mleft.setFill('yellow')
    elif key == algNameList[9]:
        ttlcorner.setFill('yellow')
        ttrcorner.setFill('yellow')
        Mleft.setFill('yellow')
        Mright.setFill('yellow')
        
    time.sleep(4)
#moving everything unneeded out of the window
    textBox.move(2000, 0)
    Mleft.move(2000, 0)
    Mright.move(2000, 0)
    textBox.move(2000, 0)
    topRright.move(2000, 0)
    topRleft.move(2000, 0)
    rtr.move(2000, 0)
    rmr.move(2000, 0)
    rmm.move(2000, 0)
    rbr.move(2000, 0)
    ttlcorner.move(2000, 0)
    ttmcorner.move(2000, 0)
    ttrcorner.move(2000, 0)
    tmlcorner.move(2000, 0)
    tmmcorner.move(2000, 0)
    tmrcorner.move(2000, 0)
    tblcorner.move(2000, 0)
    tbmcorner.move(2000, 0)
    tbrcorner.move(2000, 0)
    ltr.move(2000, 0)
    lmr.move(2000, 0)
    lm.move(2000, 0)
    lbr.move(2000, 0)
    topLleft.move(2000, 0)
    topLright.move(2000, 0)
    Letters()

def Letters():
#Goes through each position in the list made from the dictionaries values
#It prints out the Letter and the arrow which indicate what side on the rubix cube you move when holding the the correst side facing you
    global x
    letterTextBox = g.Text(g.Point(0, 0), '')
    Arrow = g.Circle(g.Point(0,0), 0)   
    tmArrow = g.Line(g.Point(0,0), g.Point(0,0))
    bmArrow = g.Line(g.Point(0,0), g.Point(0,0))
    tlArrow = g.Line(g.Point(0,0), g.Point(0,0))
    blArrow = g.Line(g.Point(0,0), g.Point(0,0))   
    trArrow = g.Line(g.Point(0,0), g.Point(0,0))
    brArrow = g.Line(g.Point(0,0), g.Point(0,0))  
    btmArrow = g.Line(g.Point(0,0), g.Point(0,0))
    bbmArrow = g.Line(g.Point(0,0), g.Point(0,0))
    tArrow = g.Line(g.Point(0,0), g.Point(0,0))
    bArrow = g.Line(g.Point(0,0), g.Point(0,0))
    v = cycle
    if ('F' in cycle[x]) or ('b' in cycle[x]):
        if 'b' == cycle[x]:
            letterTextBox = g.Text(g.Point(290, 450), 'B\' Move the back-side(oppisite face) to the right')
        else:
            letterTextBox = g.Text(g.Point(275, 450), 'F')
        letterTextBox.draw(win)  
        Arrow = g.Circle(g.Point(275,575), 60)   
        tmArrow = g.Line(g.Point(260,505), g.Point(280,515))
        bmArrow = g.Line(g.Point(260,525), g.Point(280,515))
        tlArrow = g.Line(g.Point(215,565), g.Point(205,585))
        blArrow = g.Line(g.Point(215,565), g.Point(225,585))  
        trArrow = g.Line(g.Point(335,585), g.Point(325,565))
        brArrow = g.Line(g.Point(335,585), g.Point(345,565))  
        btmArrow = g.Line(g.Point(280,625), g.Point(265,635))
        bbmArrow = g.Line(g.Point(280,645), g.Point(265,635))  
        tmArrow.draw(win)
        bmArrow.draw(win)
        trArrow.draw(win)
        brArrow.draw(win)
        tlArrow.draw(win)
        blArrow.draw(win)
        btmArrow.draw(win)
        bbmArrow.draw(win)
        Arrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    elif 'f' in cycle[x]:
        if 'B' == cycle[x]:
            letterTextBox = g.Text(g.Point(290, 450), 'B Move the back side(oppisite face) to the left')
        else:
            letterTextBox = g.Text(g.Point(275, 450), 'F')
        letterTextBox.draw(win)  
        Arrow = g.Circle(g.Point(275,575), 60)
        tmArrow = g.Line(g.Point(280,505), g.Point(260,515))
        bmArrow = g.Line(g.Point(280,525), g.Point(260,515))
        tlArrow = g.Line(g.Point(215,585), g.Point(205,565))
        blArrow = g.Line(g.Point(215,585), g.Point(225,565))
        trArrow = g.Line(g.Point(335,565), g.Point(325,585))
        brArrow = g.Line(g.Point(335,565), g.Point(345,585))
        btmArrow = g.Line(g.Point(265,625), g.Point(280,635))
        bbmArrow = g.Line(g.Point(265,645), g.Point(280,635))
        tmArrow.draw(win)
        bmArrow.draw(win)
        trArrow.draw(win)
        brArrow.draw(win)
        tlArrow.draw(win)
        blArrow.draw(win)
        btmArrow.draw(win)
        bbmArrow.draw(win)
        Arrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    elif 'u' in cycle[x]:
        Arrow = g.Line(g.Point(225,525), g.Point(325,525))
        tArrow = g.Line(g.Point(305,510), g.Point(325,525))
        bArrow = g.Line(g.Point(305,540), g.Point(325,525))
        letterTextBox = g.Text(g.Point(275, 450), 'U\'')
        letterTextBox.draw(win) 
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)    
    elif ('U' in cycle[x]) or ('k' in cycle[x]):
        if 'k' == cycle[x]:
            letterTextBox = g.Text(g.Point(275, 450), 'U2')
        else:
            letterTextBox = g.Text(g.Point(275, 450), 'U')
        letterTextBox.draw(win) 
        Arrow = g.Line(g.Point(225,525), g.Point(325,525))
        tArrow = g.Line(g.Point(225,525), g.Point(245,510))
        bArrow = g.Line(g.Point(225,525), g.Point(245,540))
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    elif 'D' in cycle[x]:
        Arrow = g.Line(g.Point(225,625), g.Point(325,625))
        tArrow = g.Line(g.Point(305,610), g.Point(325,625))
        bArrow = g.Line(g.Point(305,640), g.Point(325,625))
        letterTextBox = g.Text(g.Point(275, 450), 'D')
        letterTextBox.draw(win) 
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    elif 'd' in cycle[x]:
        Arrow = g.Line(g.Point(225,625), g.Point(325,625))
        tArrow = g.Line(g.Point(225,625), g.Point(245,610))
        bArrow = g.Line(g.Point(225,625), g.Point(245,640))
        letterTextBox = g.Text(g.Point(275, 450), 'D\'')
        letterTextBox.draw(win) 
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)   
    elif ('R' in cycle[x]) or ('t' in cycle[x]):
        if 't' == cycle[x]:
            letterTextBox = g.Text(g.Point(275, 450), 'R2')
        else:
            letterTextBox = g.Text(g.Point(275, 450), 'R')
        letterTextBox.draw(win) 
        Arrow = g.Line(g.Point(325,625), g.Point(325,525))
        tArrow = g.Line(g.Point(315,545), g.Point(325,525))
        bArrow = g.Line(g.Point(335,545), g.Point(325,525))
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    elif 'r' in cycle[x]:
        Arrow = g.Line(g.Point(325,625), g.Point(325,525))
        tArrow = g.Line(g.Point(315,605), g.Point(325,625))
        bArrow = g.Line(g.Point(335,605), g.Point(325,625))
        letterTextBox = g.Text(g.Point(275, 450), 'R\'')
        letterTextBox.draw(win) 
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)       
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    elif 'l' in cycle[x]:
        Arrow = g.Line(g.Point(225,625), g.Point(225,525))
        tArrow = g.Line(g.Point(215,545), g.Point(225,525))
        bArrow = g.Line(g.Point(235,545), g.Point(225,525))
        letterTextBox = g.Text(g.Point(275, 450), 'L\'')
        letterTextBox.draw(win) 
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    elif 'L' in cycle[x]:
        Arrow = g.Line(g.Point(225,625), g.Point(225,525))
        tArrow = g.Line(g.Point(215,605), g.Point(225,625))
        bArrow = g.Line(g.Point(235,605), g.Point(225,625))
        letterTextBox = g.Text(g.Point(275, 450), 'L')
        letterTextBox.draw(win) 
        Arrow.draw(win)
        tArrow.draw(win)
        bArrow.draw(win)
        x = x + 1
        Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox)
    else:  
        End()
        
def End():
#After the algorithm is ran the program goes here where the user will either continue the program or end the program
    global x, text
    textBox = g.Text(g.Point(300, 430), "Do you want to continue? (y/n)")
    textBox.draw(win)
    entryBox = g.Entry(g.Point(300, 450), 5)  
    entryBox.draw(win)
    win.getMouse()
    text.move(2000,0)
    answer = entryBox.getText()
    if answer == 'y':
        textBox.move(2000,0)
        entryBox.move(2000,0)
        x = 0
        Menu()
    elif answer == 'n':
        sys.exit()
    else:
       text = g.Text(g.Point(300, 480), "'" + str(answer) + "' is not an acceptable choice\n")
       text.draw(win)
       textBox.move(2000,0)
       entryBox.move(2000,0)
       End()
       
def Clear(Arrow, tArrow, bArrow, tmArrow, bmArrow, tlArrow, blArrow, trArrow, brArrow, btmArrow, bbmArrow, letterTextBox):
    time.sleep(2)
    Arrow.move(2000, 0)
    tArrow.move(2000, 0)
    bArrow.move(2000, 0)
    tmArrow.move(2000, 0)
    bmArrow.move(2000, 0)
    tlArrow.move(2000, 0)
    blArrow.move(2000, 0)
    trArrow.move(2000, 0)
    brArrow.move(2000, 0)
    btmArrow.move(2000, 0)
    bbmArrow.move(2000, 0)
    letterTextBox.move(2000, 0) 
    Letters()
#calling the funtion    
Menu()