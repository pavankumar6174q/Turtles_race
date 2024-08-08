import turtle as t
import random
screen = t.Screen()


game_started = False

screen.setup(width= 1000, height= 700)
user_guess = screen.textinput(title="Turtle Race Make a bet", prompt= "Who's gonna win pick a color :  ")
print(user_guess)

colors = ['red','green','blue', 'purple','yellow', 'orange', 'pink']

y_positions = [-300 , -200, -100, 0, 100, 200, 300]

turtles = []
for turtle_index in range(0, 7):

    tim = t.Turtle(shape= "turtle")
    tim.speed(100)
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x= -450 , y = y_positions[turtle_index])
    turtles.append(tim)


if user_guess:
    game_started = True

while game_started:
    for tim in turtles:
        if tim.xcor()> 430:
            game_started = False
            winning_color = tim.pencolor()
            if winning_color == user_guess :
                print(f"You've won the winning turtle is {winning_color} ")
                

            else:
                print(f"You've lost the winning turtle is {winning_color} ")
        rand_distance = random.randint(0,10)
        tim.forward(rand_distance)

















screen.exitonclick()