import snake
import unittest
from unittest.mock import patch, MagicMock

class SnakeTest(unittest.TestCase):
    @patch("snake.curses.initscr")
    def test_setup_pass(self, mock_curses):
        mock_curses.assert_called_with() 
        result = snake.setup()
