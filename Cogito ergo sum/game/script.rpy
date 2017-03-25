# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image bg bedroom = "bedroom.jpg"
image bg livingroom = "living_room.jpg"
image bg bedroom_c = "bedroom_ceiling.jpg"
image bg hospital = "hospital.jpg"
image bg hospital_c = "hospital_ceiling"
image bg tornado = "tornado.jpg"

define g = Character('Gerald', color = "#c8ffc8")
define t = Character('Thia', color = "#c8ffc8")
define

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
