# Snake

A small Snake game built with Python and Pygame. Guide the snake around the
grid, eat the shrimp to grow, and avoid the walls and your own tail. The cat is my own cat, Olivia :)
<img src="https://github.com/user-attachments/assets/ca686c04-e6c4-40e3-9e67-4f0ec483d038" width="500" />



## Features

- Keyboard-controlled movement on a 20 × 20 grid
- A score that increases as the snake grows
- Sound and custom graphics loaded from local asset files

## Requirements

- Python 3
- Pygame
- The game assets listed below

Install Pygame with:

```bash
python -m pip install pygame
```

The script loads these files by name from its working directory:

- `shrimp.png`
- `head_up.png`, `head_right.png`, `head_down.png`, `head_left.png`
- `tail_up.png`, `tail_right.png`, `tail_down.png`, `tail_left.png`
- `body_vertical.png`, `body_horizontal.png`
- `body_tr.png`, `body_tl.png`, `body_br.png`, `body_bl.png`
- `cat_meow.MP3`
- `Carnevalee Freakshow.ttf`

These assets are not included in this project folder. Place the files alongside
`ar.py` before launching the game.

## Run the game

From the directory containing `ar.py` and the required assets, run:

```bash
python ar.py
```

Use the **arrow keys** to steer. Eating the shrimp grows the snake and increases
the score. Hitting a wall or the snake's own body resets the game.

## Help

For help, contact the project maintainer through the repository where you
obtained this code. No separate documentation or support channel is included.

## Maintainers and contributing

The maintainer is the owner of this project repository. Contributions can be
submitted as pull requests through the repository hosting service. Please
describe the change and verify that the game still launches and plays with its
required assets. No separate contribution guide is currently included.
