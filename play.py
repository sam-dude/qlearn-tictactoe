import pickle
import pygame
from gui import play_with_agent

with open("o_agent.pkl", "rb") as f:
    o_agent = pickle.load(f)

pygame.init()
screen = pygame.display.set_mode((450, 540))

o_agent.epsilon = 0.0 # agent always plays best
play_with_agent(screen, ai_agent=o_agent, human_symbol="X")
