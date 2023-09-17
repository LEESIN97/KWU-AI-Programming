import turtle as t

#그림 그리기
t.penup()
t.goto(-75,-200)

for n in range(9, 3, -1):
    t.penup()
    if n == 4:
        t.fillcolor('lawngreen')
        t.begin_fill()
    elif n == 5:
        t.fillcolor('blue')
        t.begin_fill()
    elif n == 6:
        t.fillcolor('yellow')
        t.begin_fill()
    elif n == 7:
        t.fillcolor('orange')
        t.begin_fill()
    elif n == 8:
        t.fillcolor('pink')
        t.begin_fill()
    elif n == 9:
        t.fillcolor('DarkSeaGreen1')
        t.begin_fill()
    t.goto(-5*n-75, -200)
    forward_length = 100 + 10*n
    for i in range(n):
        t.pendown()
        t.forward(forward_length/2)
        t.stamp()
        t.forward(forward_length/2)
        t.left(360/n)    
    t.end_fill()
# 이름 쓰기
t.penup()
t.goto(-20, 250)
t.hideturtle()
t.write("이 신", move=False, align='center', font=('Arial', 24, 'normal'))
t.done()