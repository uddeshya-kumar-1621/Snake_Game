# backend.py
# This file contains the logic for snake movement (Backend)

def go_up(head):
    if head.direction != "down":
        head.direction = "up"

def go_down(head):
    if head.direction != "up":
        head.direction = "down"

def go_left(head):
    if head.direction != "right":
        head.direction = "left"

def go_right(head):
    if head.direction != "left":
        head.direction = "right"

def move(head):
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)