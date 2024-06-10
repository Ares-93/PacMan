import turtle
import time
import random


# Step 1: Setting Up the Game Environment
screen = turtle.Screen()
screen.title("Pac-Man Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off the screen updates

# Step 2: Creating Pac-Man
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.goto(0, 0)
pacman.direction = "stop"

# Step 3: Control Pac-Man's Direction


def go_up():
    pacman.direction = "up"


def go_down():
    pacman.direction = "down"


def go_left():
    pacman.direction = "left"


def go_right():
    pacman.direction = "right"

# Move Pac-Man


def move():
    if pacman.direction == "up":
        y = pacman.ycor()
        pacman.sety(y + 20)
    elif pacman.direction == "down":
        y = pacman.ycor()
        pacman.sety(y - 20)
    elif pacman.direction == "left":
        x = pacman.xcor()
        pacman.setx(x - 20)
    elif pacman.direction == "right":
        x = pacman.xcor()
        pacman.setx(x + 20)


# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# # Step 5 create Ghosts with Custom Shape
# custom_ghost_shape = [(0, 0), (10, -5), (12, -10), (10, -15),
#                       (0, -20), (-10, -15), (-12, -10), (-10, -5)]

# screen.register_shape("ghost", custom_ghost_shape)

ghosts = []
colors = ["purple", "cyan", "orange", "green"]
start_pos = [(100, 0), (-100, 0), (0, 100), (0, -100)]

for color, position in zip(colors, start_pos):
    ghost = turtle.Turtle()
    ghost.shape("square")
    ghost.color(color)
    ghost.penup()
    ghost.goto(position)
    ghosts.append(ghost)

# random ghost directions


def move_ghosts():
    for ghost in ghosts:
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            y = ghost.ycor()
            ghost.sety(y + 20)
        elif direction == "down":
            y = ghost.ycor()
            ghost.sety(y - 20)
        elif direction == "left":
            x = ghost.xcor()
            ghost.setx(x - 20)
        elif direction == "right":
            x = ghost.xcor()
            ghost.setx(x + 20)


# create the maze:
maze_layout = [
    "WWWWWWWWWWWWWW",
    "W            W",
    "W WWW WW WWW W",
    "W            W",
    "W WWW WW WWW W",
    "W            W",
    "WWWWWWWWWWWWWW",
]

block_size = 40  # Change this to a larger number to scale up the maze

# Adjust the draw_maze function


def draw_maze(maze):
    num_blocks_width = len(maze[0])
    num_blocks_height = len(maze)

    # Calculate the block size based on the screen dimensions and number of blocks
    block_size_width = screen.window_width() / num_blocks_width
    block_size_height = screen.window_height() / num_blocks_height

    # The smallest of the two will ensure that the maze does not stretch disproportionately
    block_size = min(block_size_width, block_size_height)

    wall = turtle.Turtle()
    wall.shape("square")
    wall.color("red")
    wall.penup()
    wall.speed(0)

    # Calculate the starting positions based on block size
    start_x = -((num_blocks_width / 2) * block_size)
    start_y = ((num_blocks_height / 2) * block_size)

    # Loop through the maze list and create walls where "W" appears
    for y in range(num_blocks_height):
        for x in range(num_blocks_width):
            character = maze[y][x]  # get the character at the current position
            # calculate the x pos on the screen
            screen_x = start_x + (x * block_size)
            # calculate the y pos on the screen
            screen_y = start_y - (y * block_size)
            if character == "W":
                wall.goto(screen_x, screen_y)
                # move the turtle across the x and y pos and stretch the maze to fit the screen.
                wall.shapesize(stretch_wid=block_size / 20,
                               stretch_len=block_size / 20)
                wall.stamp()  # stamps a square shape to draw the wall.


draw_maze(maze_layout)

# Main Game Loop
while True:
    screen.update()
    move()
    move_ghosts()
    time.sleep(0.1)  # Control the speed of Pac-Man's movement
