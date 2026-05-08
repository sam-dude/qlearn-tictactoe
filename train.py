from game import TicTacToe
from agent import QAgent


def train(episodes=5000, alpha=0.1, gamma=0.8, epsilon=0.1, log_interval=500):
    env     = TicTacToe()
    x_agent = QAgent(alpha, gamma, epsilon)
    o_agent = QAgent(alpha, gamma, epsilon)

    wins = losses = draws = 0

    for episode in range(1, episodes + 1):
        state = env.reset()

        while True:
            # X move
            x_state  = state
            x_action = x_agent.select_action(state, env.available_actions())
            state, reward, done = env.step(x_action)

            if done:
                x_agent.update(x_state, x_action, reward, state, [])
                if reward == 1: wins += 1
                else: draws += 1
                break

            # O move
            o_state  = state
            o_action = o_agent.select_action(state, env.available_actions())
            state, reward, done = env.step(o_action)

            x_agent.update(x_state, x_action,  reward, state, env.available_actions())
            o_agent.update(o_state, o_action,  -reward, state, env.available_actions())

            if done:
                if reward == -1: losses += 1
                else: draws += 1
                break

        if episode % log_interval == 0:
            total = wins + losses + draws
            print(f"\nEpisode {episode}")
            print(f"Wins:   {wins} ({wins/total:.2f})")
            print(f"Losses: {losses} ({losses/total:.2f})")
            print(f"Draws:  {draws} ({draws/total:.2f})")
            print(f"Epsilon (X): {x_agent.epsilon:.4f}")
            print(f"Epsilon (O): {o_agent.epsilon:.4f}")
            wins = losses = draws = 0

            x_agent.epsilon *= 0.99
            o_agent.epsilon *= 0.99

    return x_agent, o_agent