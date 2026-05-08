import random


class QAgent:
    def __init__(self, alpha, gamma, epsilon):
        self.Q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def ensure_state(self, state, actions):
        if state not in self.Q:
            self.Q[state] = {a: 0.0 for a in actions}

    def select_action(self, state, actions):
        self.ensure_state(state, actions)

        if random.random() < self.epsilon:
            return random.choice(actions)

        values = self.Q[state]
        max_v = max(values[a] for a in actions)
        best = [a for a in actions if values[a] == max_v]
        return random.choice(best)

    def update(self, state, action, reward, next_state, next_actions):
        self.ensure_state(state, [action])
        self.ensure_state(next_state, next_actions)

        best_next = max([self.Q[next_state][a] for a in next_actions], default=0.0)

        target = reward + self.gamma * best_next
        self.Q[state][action] += self.alpha * (target - self.Q[state][action])
        
        
