
# Pong Game using PyGame Library

This is a classic Pong game implemented using Python and the Pygame library. The game features two player-controlled paddles and a bouncing ball, with increasing ball speed over time for added challenge. Players can use the keyboard to move paddles and compete for points by hitting the ball past their opponent’s paddle. The game includes a start screen, score display, and endgame logic declaring the winner or tie, with an option to replay.
## Features

- Two-player Pong gameplay with paddle movement controlled by keyboard
- Ball with increasing speed after set intervals to increase difficulty
- Scoring system tracking player points and displaying scores on screen
- Start screen prompting players to press space to begin
- Game over screen displaying winner or tie and option to replay
- Dotted center line for visual separation of playfield
- Smooth animation and collision detection using Pygame’s rendering

## Getting Started / Installation

- Make sure Python 3.x is installed on your system.
- Install Pygame via pip if not already installed:

    ```
    pip install pygame
    ```
- Download or clone this Pong game project files.
- Run the main Python script:
    ```
    python main.py
    ```
- The game window will open and be ready for play.
## Usage Instructions

- Press the **Space** key to start the game or restart after game over.
- Player 1 controls paddle movement using **W** (up) and **S** (down) keys.
- Player 2 controls paddle movement using the **Up Arrow** and **Down Arrow** keys.
- Score points by bouncing the ball past the opponent’s paddle.
- Game ends when the ball goes beyond the left or right screen edge, and the winner/tie is shown.
- Press **Space** to replay after the game over screen.
## Technologies Used

- Python 3.x
- Pygame library for game window, rendering, input handling, and fonts
## File Structure

```
/
├── main.py          # Main Python script containing game logic and rendering
└── README.md        # Project documentation (this file)

```
## Customization

- Modify variables like screen width/height or colors inside the script for different game sizes or themes.
- Adjust paddle speed, ball acceleration, and speed increase intervals to change gameplay difficulty.
- Extend the game with sound effects or multiplayer networking features.
Known Issues / Limitations
## Limitations

- No AI opponent; both paddles require human control.
- Game over condition is when the ball crosses left or right edge, with no round limits or timers.
- No pause or save functionality implemented.
- No sound effects included by default.
## Future Improvements

- Add a single-player mode with AI for paddle control.
- Implement pause, save/load game state, and round limits.
- Add sound effects and background music for enhanced experience.
- Include power-ups or special ball effects for gameplay variety.
- Improve graphics and add animations.
## Contributing

Contributions are always welcome! To contribute:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes with clear comments and testing.
- Submit a pull request describing your work.
## License


This project is open-source and available under the MIT License.
## Acknowledgements

- Pygame community and documentation for excellent game development support.
- Classic Pong game as inspiration and gameplay model.
- Online tutorials and forums for Python game programming techniques.