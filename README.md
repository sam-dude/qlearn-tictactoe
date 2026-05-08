Hey 👋🏽,

Sam-dude here.

This is a simple Reinforcement Learning agent that learns to play Tic Tac Toe through self-play. I built and trained this entirely on my Android phone, using Pydroid3.

You can run it on yours too.

## What's here
- game.py — the Tic Tac Toe environment
- agent.py — Q-Learning agent
- train.py — self-play training loop (X agent vs O agent)
- main.py — CLI entry point for training
- play.py — launch the GUI to play against the agent
- gui.py — pygame interface with Q-value visualization


## How to run
Train from terminal:
```python main.py --episodes 10000```

Then open play.py in your IDE and run it to play against the trained agent.

## Dependencies
`pygame`

## Why
I've done RL projects before but there were quite a few dots that weren't connected. I've been reading Sutton's RL book and wanted to actually understand what's happening underneath, not just copy patterns.
And to show that you don't need a laptop to learn the basics. Any device works.
