import Running_Through_Space as Run
import unittest

class TestTodoList(unittest.TestCase):
    def test_build_deck(self):
        deck = Run.deck()
        self.assertEqual(len(deck), 100)

    def test_board(self):
        board = Run.build_board()
        self.assertEqual(len(board), 50)
        self.assertEqual(board[0][0]['space_name'], 'Start')
        self.assertEqual(board[49][0]['space_name'], 'End')

    def test_turn(self):
        pos = Run.player1_pos
        self.assertEqual(pos, False)

    def test_save_scores(self):
        scores = Run.save_scores(3, 4)
        self.assertEqual(scores, 7)

    def test_load_scores(self):
        scores_frm_func = Run.load_scores()
        with open('Game_Counter.txt', 'r') as file:
            scores = file.readline().split()
            p1_score = int(scores[0])
            p2_score = int(scores[1])
        self.assertEqual(scores_frm_func[0], p1_score)
        self.assertEqual(scores_frm_func[1], p2_score)

if __name__ == '__main__':
    unittest.main()