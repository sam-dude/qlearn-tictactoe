import argparse
import pickle
from train import train

parser = argparse.ArgumentParser(description="Tic Tac Toe RL")
parser.add_argument("--episodes", type=int, default=10000)
parser.add_argument("--log",      type=int, default=500)
parser.add_argument("--alpha",    type=float, default=0.1)
parser.add_argument("--gamma",    type=float, default=0.8)
parser.add_argument("--epsilon",  type=float, default=0.1)
args = parser.parse_args()

x_agent, o_agent = train(
    episodes     = args.episodes,
    alpha        = args.alpha,
    gamma        = args.gamma,
    epsilon      = args.epsilon,
    log_interval = args.log,
)

with open("x_agent.pkl", "wb") as f:
    pickle.dump(x_agent, f)
with open("o_agent.pkl", "wb") as f:
    pickle.dump(o_agent, f)

print("\nAgents saved to x_agent.pkl and o_agent.pkl")