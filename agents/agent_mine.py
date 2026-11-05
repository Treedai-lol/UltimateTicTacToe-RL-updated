from agents.agent import Agent
from agents.common.bitboard import BitBoard,SmallBoard
from agents.common.lib import Board

class MyAgent(Agent):

    def __init__(self, player = 1):
        super().__init__(self)

    def getAction(self, env, observation):
        temp = env.pygame.board.grid.append(env.pygame.board.largeGrid)
        if(len(env.pygame.board.possible))>1:
            temp.append(9)
        else:
            temp.append(env.pygame.board.possible)
        temp.append(env.pygame.board.currentPlayer)
        b = Board(temp)
        action = 0
        return action