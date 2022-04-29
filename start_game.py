import curses
from curses.textpad import Textbox, rectangle
import os
import snake_movement

class Score():

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def __str__(self):
        s = f'{self.name} {self.score}' + '\n'
        return s 
    

class Options():

    def new_game(stdscr,score_1):

        h, w = stdscr.getmaxyx()
        x = w//2
        y = h//2
        
        stdscr.addstr(y,x-(len('Enter player name (10 characters max):')//2),'Enter player name (10 characters max):')
        text_win = curses.newwin(1,11,y+5,x-2)
        box = Textbox(text_win)
        rectangle(stdscr,y+1,x-6,y+3,x+6)
        stdscr.refresh()
        box.edit()
        name_1 = box.gather().replace(' ','-')
        if not name_1: name_1 = 'Anon'

        player = Score(name_1,score_1) # απο το game tha pernei to score
        with open ('scoreboard.txt', 'a', encoding='utf-8') as f :
            f.write(str(player))

    def scoreboard(stdscr):
        if 'scoreboard.txt' in os.listdir(os.getcwd()):
            with open ('scoreboard.txt', 'r', encoding='utf-8') as f :
                all = f.read()
                line = all.split('\n')
                line.pop()
                scoreboard = [x.split() for x in line]
                scoreboard.sort(key=lambda score: int(score[1]),reverse=True)
            
            stdscr.clear()
            stdscr.addstr(1,(curses.COLS//2)-(len('Scoreboard')//2),'Scoreboard')
            for i in scoreboard:
                stdscr.addstr(scoreboard.index(i)+3,(curses.COLS//2)-(len(str(i))//2),i[0])
                stdscr.addstr(scoreboard.index(i)+3,(curses.COLS//2)-(len(str(scoreboard[0]))//2)+10,i[1])

            stdscr.refresh()
            stdscr.getch()

        else:
            Curses_class.print_center(stdscr,'Not any scores yet (Press any key to exit to menu)')
            stdscr.getch()


class Curses_class():

    menu = [ 'Play', 'Scoreboard', 'Exit']

    def print_menu(stdscr, selected_row_idx):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(Curses_class.menu):
            x = w//2 - len(row)//2
            y = h//2 - len(Curses_class.menu)//2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    def print_center(stdscr, text):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        x = w//2 - len(text)//2
        y = h//2
        stdscr.addstr(y, x, text)
        stdscr.refresh()

    def menu_control(stdscr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        current_row = 0 
        Curses_class.print_menu(stdscr, current_row)

        while True:
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(Curses_class.menu)-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:
                    snake_movement.main(stdscr)
                if current_row == 1:
                    Options.scoreboard(stdscr)
                if current_row == len(Curses_class.menu)-1:
                    break
            Curses_class.print_menu(stdscr, current_row)

if __name__ == '__main__':
    curses.wrapper(Curses_class.menu_control)