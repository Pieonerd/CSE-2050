import unittest
import game
import maze

class TestGame(unittest.TestCase):

    def test1_example_test(self):
        '''An example test that shows all the steps to initialize and invoke the solution algorithm'''

        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
        start = (0,1)
        end = (0,3)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3)])

    #############################################
    # TODO - add the rest of your test cases here
    def test_no_solution(self):
        "Tests edge case if there is no solution to the maze"
        grid = maze.Maze(2, 2)
        grid._set_maze([[1, "*"],
                        ["*", 1] ])
        start = (0,0)
        end = (1,1)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        self.assertEqual(score, -1)
        self.assertEqual(path, [])

    def test_all_numbers(self):
        "Test case if maze is composed of all numbers"
        grid = maze.Maze(2, 3)
        grid._set_maze([[1, 2, 3],
                        [4, 5, 6]])
        start = (0,0)
        end = (1,2)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        self.assertEqual(score, 14)
        self.assertEqual(path, [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2)])
    
    def test_all_walls(self):
        "Test case if maze if composed of all walls"
        grid = maze.Maze(3, 3)
        grid._set_maze([["*", "*", "*"],
                        ['*', "*", "*"],
                        ["*", "*", "*"]])
        start = (0,0)
        end = (2,2)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        self.assertEqual(score, -1)
        self.assertEqual(path, [])
    
    def test_adjacent_start_end(self):
        "Test case when the start and end points are adjacent to each other"
        grid = maze.Maze(3, 2)
        grid._set_maze([[1, 1],
                        [2, 5],
                        [3, 4]])
        start = (0,0)
        end = (0,1)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        self.assertEqual(score, 14)
        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1)])

if __name__ == '__main__':
    unittest.main()
