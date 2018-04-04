"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)


    def test_example(self):
        # TODO: All methods must start with "test_"
        # self.fail("Hello, World!")
        agent1 = game_agent.MinimaxPlayer()
        agent2 = game_agent.MinimaxPlayer()

        game = isolation.Board(agent1, agent2)

        game.apply_move((2, 3))
        game.apply_move((0, 5))

        winner, history, outcome = game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))

if __name__ == '__main__':
    unittest.main()
