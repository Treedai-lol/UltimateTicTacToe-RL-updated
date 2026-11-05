from agents.agent import Agent
from agents.common.lib import Board
import math
from agents.common.MCTS import mcts_search

class MyAgent(Agent):

    def __init__(self, player = 1):
        super().__init__(self)

    def getAction(self, env, observation):
        temp = list(env.pygame.board.grid)
        temp.extend(env.pygame.board.largeGrid)
        if(len(env.pygame.board.possible))>1:
            temp.append(9)
        else:
            temp.append(int(env.pygame.board.possible[0]))
        temp.append(env.pygame.board.currentPlayer)
        #print(env.pygame.board.grid)
        #print(len(env.pygame.board.largeGrid))
        #print(len(env.pygame.board.possible))
        #print(env.pygame.board.currentPlayer)
        #print(temp)
        b = Board(temp)
        #b.PrintBoard()
        move = mcts_search(b,1.024)
        action = move.bit_length()-1
        return action