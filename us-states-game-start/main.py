import turtle
import pandas

screen =  turtle.Screen()

screen.title("US States Game")

## -- Loading Image on the turtle screen -- ##
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#get x and y coordinates
#def get_mouse_click_coor(x,y):
#    print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()




data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title =f"{len(guessed_state)}/50 States Guessed Correctly",
                                    prompt="What's another state's name").title()
    print(answer_state)

    if answer_state == "Exit":

        with open ("Result.txt", 'w') as file:
            file.write("The states you should remember are:\n")
        for i in all_state:
            with open("Result.txt", 'a') as file:
                file.write((f"{i}\n"))
        break

    if answer_state in all_state:

        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #comparing with input
        t.goto(int(state_data.x), int(state_data.y)) # turtle uses int values for goto
        t.write(state_data.state.item()) ## item picks up the first value from the row selected
        all_state.remove(answer_state)
screen.exitonclick()







