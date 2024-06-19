import turtle
import pandas
import turtle

# Read data from csv file and store in us_states_data variable
us_states_data = pandas.read_csv("./day025/day25_project_USStatesGames/50_states.csv")
us_states_list = us_states_data.state.to_list()


# Create to game screen by turtle
screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("./day025/day25_project_USStatesGames/blank_states_img.gif")
turtle.shape("./day025/day25_project_USStatesGames/blank_states_img.gif")

continue_game = True
answer_list = []
while continue_game:

    # Ask the state
    answer_state = screen.textinput(
        title="Guess the State: ",
        prompt=f"{len(answer_list)}/50 States Correct, What's another state's name? ",
    ).title()

    # Check correct answer
    if answer_state in us_states_list and answer_state not in answer_list:
        answer_list.append(answer_state)
        x_pos = us_states_data[us_states_data.state == answer_state].x.to_list()[0]
        y_pos = us_states_data[us_states_data.state == answer_state].y.to_list()[0]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=x_pos, y=y_pos)
        # t.write(answer_state)
        t.write(us_states_data[us_states_data.state == answer_state].state.item())
    if len(answer_list) == 50:
        continue_game = False
    if answer_state == "Exit":
        break

# Save the missing states to csv.
print(answer_list)
set1 = set(answer_list)
set2 = set(us_states_list)
missing_states = list(set2 - set1)
missing_states_dict = {"Learning": missing_states}
df = pandas.DataFrame(missing_states_dict)
df.to_csv("./day025/day25_project_USStatesGames/learning_states.csv")
