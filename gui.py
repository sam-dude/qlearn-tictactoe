import pygame
import sys
from game import TicTacToe

WIDTH  = 450
HEIGHT = 540
CELL   = WIDTH // 3
GRID_H = WIDTH


def play_with_agent(screen, ai_agent, human_symbol="X"):
    ai_symbol = "O" if human_symbol == "X" else "X"

    pygame.display.set_caption("Tic Tac Toe")

    font     = pygame.font.SysFont(None, 140)
    q_font   = pygame.font.SysFont(None, 36)
    msg_font = pygame.font.SysFont(None, 46)

    env   = TicTacToe()
    state = env.reset()

    WHITE  = (255, 255, 255)
    BLACK  = (0,   0,   0  )
    BAR_BG = (230, 230, 230)
    Q_POS  = (30,  160, 30 )
    Q_NEG  = (180, 30,  30 )
    Q_ZERO = (150, 150, 150)

    def get_message():
        if env.done:
            if env.winner == human_symbol: return "You won! Good game."
            elif env.winner == ai_symbol:  return "AI won! Try again."
            else:                          return "Draw!"
        return "Your turn" if env.current_player == human_symbol else "AI is thinking..."

    def draw():
        screen.fill(WHITE)

        for i in range(1, 3):
            pygame.draw.line(screen, BLACK, (0, i * CELL), (WIDTH, i * CELL), 5)
            pygame.draw.line(screen, BLACK, (i * CELL, 0), (i * CELL, GRID_H), 5)

        for i, v in enumerate(env.board):
            r, c   = divmod(i, 3)
            cx, cy = c * CELL, r * CELL

            if v != "-":
                sym    = font.render(v, True, BLACK)
                sw, sh = sym.get_size()
                screen.blit(sym, (cx + (CELL - sw) // 2, cy + (CELL - sh) // 2))
            else:
                q     = ai_agent.Q.get(state, {}).get(i, 0.0)
                color = Q_POS if q > 0.01 else Q_NEG if q < -0.01 else Q_ZERO
                label = q_font.render(f"{q:+.2f}", True, color)
                screen.blit(label, (cx + 10, cy + 10))

        pygame.draw.rect(screen, BAR_BG, (0, GRID_H, WIDTH, HEIGHT - GRID_H))
        pygame.draw.line(screen, BLACK, (0, GRID_H), (WIDTH, GRID_H), 3)
        msg = msg_font.render(get_message(), True, BLACK)
        screen.blit(msg, ((WIDTH - msg.get_width()) // 2,
                           GRID_H + (HEIGHT - GRID_H - msg.get_height()) // 2))
        pygame.display.flip()

    running = True

    while running:
        draw()

        if env.done:
            pygame.time.wait(2000)
            state = env.reset()
            continue

        if env.current_player == ai_symbol:
            pygame.time.wait(400)
            action = ai_agent.select_action(state, env.available_actions())
            state, _, _ = env.step(action)
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if my < GRID_H:
                    a = (my // CELL) * 3 + (mx // CELL)
                    if a in env.available_actions():
                        state, _, _ = env.step(a)

    pygame.quit()
    sys.exit()