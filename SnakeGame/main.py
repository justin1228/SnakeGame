import curses
import random
from snake import Snake
from prey import Prey


curses.initscr()
y_size = 9
x_size = 27
win = curses.newwin(y_size + 2, x_size + 2, 0, 0)
curses.noecho()
curses.cbreak()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
win.keypad(True)
win.nodelay(1)
win.border('x', 'x', 'x', 'x')
score = 0
keys = [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]
ESC = 27

key = keys[0] #첫 시작은 오른쪽
s1 = Snake()
p1 = Prey()
p1.addData(y_size, x_size)

while(key != ESC):
    win.addstr(0,0, f"xxx SCORE = {score} xxxxxxxxxxxxxxx")
    for i in range(0, y_size + 2):
        win.addstr(i,0, 'x')
    head = s1.get_body()[0]
    try:
        if head[0] < 0 or head[0] > (y_size):
            break
        elif head[1] < 0 or head[1] > (x_size):
            break
    except curses.error:
        pass
    
    if key in [keys[0], keys[1]]:
        win.timeout(45 + (150 - s1.length) // 5 + s1.length // 10 % 120)
    elif key in [keys[2], keys[3]]:
        win.timeout(117 + (150 - s1.length) // 5 + s1.length // 10 % 120)
    
    


    try:
        for c in s1.get_body():
            win.addch(c[0], c[1], "+", curses.color_pair(1))
    except curses.error:
        pass
    if head == p1.getData()[0]:
        score += 1
        if key == keys[0]:
            last = s1.get_last_element()
            last[1] -= 1
            if last[1] < 1:
                last[1] = x_size - 1
            s1.append(tuple(last))
            p1.popData()
            p1.addData(y_size, x_size)
        elif key == keys[1]:
            last = s1.get_last_element()
            last[1] += 1
            if last[1] > x_size - 1:
                last[1] = 1
            s1.append(tuple(last))
            p1.popData()
            p1.addData(y_size, x_size)
        elif key == keys[2]:
            last = s1.get_last_element()
            last[0] -= 1
            if last[0] < 1:
                last[0] = y_size - 1
            s1.append(tuple(last))
            p1.popData()
            p1.addData(y_size, x_size)
        elif key == keys[3]:
            last = s1.get_last_element()
            last[0] += 1
            if last[0] > y_size - 1:
                last[0] = 1
            s1.append(tuple(last))
            p1.popData()
            p1.addData(y_size, x_size)

    for p in p1.getData():
        win.addch(p[0], p[1], "*")
    event = win.getch() #입력받기
    prev_key = key

    key = event if event != -1 else prev_key #입력이 없으면 전의 키 유지 입력하면 키 입력을 Key에 저장

    if key not in keys: #방향키가 아니면 전의 키 유지
        key = prev_key
    
    if key == keys[0]:
        s1.move_right()
        last = s1.pop()
        win.addch(last[0],last[1], " ")
    elif key == keys[1]:
        s1.move_left()
        last = s1.pop()
        win.addch(last[0],last[1], " ")
    elif key == keys[2]:
        s1.move_up()
        last = s1.pop()
        win.addch(last[0],last[1], " ")
    elif key == keys[3]:
        s1.move_down()
        last = s1.pop()
        win.addch(last[0],last[1], " ")

    

    if s1.get_body()[0] in s1.get_body()[1:]:
        break
    

    


curses.endwin()   

