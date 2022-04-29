import curses
import random
import start_game

def main(stdscr):
    def game_over():
        nonlocal temp,x,y,score
        temp = None
        x,y = 1,1
        win.clear()
        win.border()
        win.addstr((curses.LINES//2)-7,(curses.COLS//2)-7,'GAME OVER')
        win.addstr((curses.LINES//2)-6,(curses.COLS//2)-7,f'SCORE:{score}')
        start_game.Options.new_game(win,score)
        score = 0

    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_RED,curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(3)
    RED_AND_BLACK = curses.color_pair(4)

    stdscr.nodelay(True)
    curses.curs_set(0)

    is_paused = False
    win = curses.newwin((curses.LINES-6),(curses.COLS-6),3,3) #mesa se auto to window tha paizei o paiktis
    temp = '' #krataei to teleuteo pliktro pou patithike
    x,y = 1,1
    score = 0
    temp_x = [] #krataei tin teleftea thesi toy kefalioy
    temp_y = []
    ran_x = random.randint(1,curses.COLS-8) #sintetagmenes frouton
    ran_y = random.randint(1,curses.LINES-8)
    while True: #to loop diarkei oso paizei o paiktis

        temp_x.append(x) #krataei tin teleftea thesi toy kefalioy
        temp_y.append(y)
        try:
            key = stdscr.getkey()
        except:
            if not temp:            
                key = None
            else:
                key = temp

        if key == 'p' or key == 'P':
            if is_paused == False:
                is_paused = True
            elif is_paused == True:
                is_paused = False

        if is_paused == True:
            stdscr.addstr(12,((curses.COLS//2)-6),'GAME IS PAUSED')
            stdscr.addstr(13,((curses.COLS//2)-9),'(PRESS P TO CONTINUE)')
            continue

        if key == 'KEY_LEFT':
            if temp == 'KEY_RIGHT': continue #gia na min ginete to kefali oura
            x -= 1
        elif key == 'KEY_RIGHT':
            if temp == 'KEY_LEFT': continue #gia na min ginete to kefali oura
            x += 1
        elif key == 'KEY_UP':
            if temp == 'KEY_DOWN': continue #gia na min ginete to kefali oura
            y -= 1
        elif key == 'KEY_DOWN':
            if temp == 'KEY_UP': continue #gia na min ginete to kefali oura
            y += 1
        else:
            key = temp
        temp = key
        stdscr.clear()
        win.clear()

        if x == ran_x and y == ran_y:
            score += 1
            ran_x = random.randint(1,curses.COLS-8) #nees sintetagmenes frouton
            ran_y = random.randint(1,curses.LINES-8)

        stdscr.border()
        stdscr.addstr((curses.LINES-2),(curses.COLS-20),'Project 53') #titloi kai score
        stdscr.addstr(2,((curses.COLS//2)-2),'SNAKE')
        stdscr.addstr(2,curses.COLS-15,f'Score: {score}')

        win.border()
        win.addstr(ran_y,ran_x,'@',RED_AND_BLACK) #frouto

        try:
            win.addstr(y, x, '0') #kefali fidiou
        except:
            game_over()
            break

        if x == 0 or x==curses.COLS-7 or y == curses.LINES-7 or y == 0:
            game_over()
            break

        for i in range(1,score+1): #gia to soma tou fidiou
            win.addstr(temp_y[-i],temp_x[-i],'0',GREEN_AND_BLACK)

            if x == temp_x[-i] and y == temp_y[-i]: #gia na pethainei otan akoumpaei to soma to kefali
                game_over()
                break
        win.refresh()
        curses.napms(150)
        stdscr.refresh()