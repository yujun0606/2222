# while문 별 그리기
# 144

import turtle as t
t.shape('turtle')
t.pensize(5)
t.color('red')
t.fillcolor('yellow')
t.begin_fill()
i = 0
while i < 5:
    t.forward(80)
    t.right(144)
    i = i + 1
t.end_fill()
