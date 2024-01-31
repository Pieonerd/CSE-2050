from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    """
            2025 miles          894 miles
Los Angeles ---------- Chicago ----------- Hartford
       \                 /                    |
        \               /                     |
         \ 1377 miles  / 1163 miles           | 1393 miles
          \           /                       |
           \         /                        |
              Austin ---------------------- Miami
                            1351 miles
"""
    def setUp(self):
        """Set up Graph with sample data"""
        V = {"Los Angeles", "Chicago", "Hartford", "Miami", "Austin"}
        E = {("Los Angeles", "Chicago", 2025), ("Chicago", "Hartford", 894), ("Hartford", "Miami", 1393), ("Miami", "Austin", 1351), ("Austin", "Los Angeles", 1377), ("Austin", "Chicago", 1163)}
        self.g = Graph(V, E)

    # TODO: Add unittests for public interface of Graph class (except traversal algs)
    def test_add_vertex(self):
        """Test add vertex"""
        self.g.addvertex("Washington D.C")
        self.assertEqual(len(self.g), 6)

    def test_remove_vertex(self):
        """Test remove vertex"""
        self.g.removevertex("Hartford")
        self.assertEqual(len(self.g), 4)

    def test_add_edge(self):
        """Test add edge"""
        self.g.addedge("Los Angeles", "Miami", 2734)
        self.assertEqual(self.g.wt("Los Angeles", "Miami"), 2734)

    def test_remove_edge(self):
        """Test remove edge"""
        self.g.removeedge("Hartford", "Miami")
        self.assertNotIn("Hartford", self.g.nbrs("Miami"))
        self.assertNotIn("Miami", self.g.nbrs("Hartford"))

    def test_nbrs(self):
        """Test neighbors"""
        neighbors = set()
        for nbr in self.g.nbrs("Austin"):
            neighbors.add(nbr)
        self.assertSetEqual(neighbors, {"Los Angeles", "Chicago", "Miami"})
    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    """
            2025 miles          894 miles
Los Angeles ---------- Chicago ----------- Hartford
       \                 /                    |
        \               /                     |
         \ 1377 miles  / 1163 miles           | 1393 miles
          \           /                       |
           \         /                        |
              Austin ---------------------- Miami
                            1351 miles
"""
    def setUp(self):
        """Set up GraphTraversal with sample data"""
        V = {"Los Angeles", "Chicago", "Hartford", "Miami", "Austin"}
        E = {("Los Angeles", "Chicago", 2025), ("Chicago", "Hartford", 894), ("Hartford", "Miami", 1393), ("Miami", "Austin", 1351), ("Austin", "Los Angeles", 1377), ("Austin", "Chicago", 1163)}
        self.g = Graph(V, E)

    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra
    # Why: Dijkstra's algorithm is an algorithm for finding the shortest amount of paths between nodes in a weighted graph
    def test_fewest_flights(self):
        """Test fewest flights"""
        path_tree, num_flights = self.g.fewest_flights("Hartford")
        self.assertDictEqual(num_flights, {'Hartford': 0, 'Miami': 1, 'Austin': 2, 'Los Angeles': 2, 'Chicago': 1})
        path_tree, num_flights = self.g.fewest_flights("Los Angeles")
        self.assertDictEqual(num_flights, {'Miami': 2, 'Hartford': 2, 'Los Angeles': 0, 'Austin': 1, 'Chicago': 1})
        path_tree, num_flights = self.g.fewest_flights("Chicago")
        self.assertDictEqual(num_flights, {'Hartford': 1, 'Los Angeles': 1, 'Austin': 1, 'Miami': 2, 'Chicago': 0})
        path_tree, num_flights = self.g.fewest_flights("Miami")
        self.assertDictEqual(num_flights, {'Chicago': 2, 'Los Angeles': 2, 'Hartford': 1, 'Austin': 1, 'Miami': 0})
        path_tree, num_flights = self.g.fewest_flights("Austin")
        self.assertDictEqual(num_flights, {'Hartford': 2, 'Austin': 0, 'Miami': 1, 'Los Angeles': 1, 'Chicago': 1})

    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra
    # Why: Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a weighted graph
    def test_shortest_path(self):
        """Test shortest path"""
        path_tree, optimized_param = self.g.shortest_path("Hartford")
        self.assertDictEqual(optimized_param, {'Austin': 2057, 'Miami': 1393, 'Hartford': 0, 'Chicago': 894, 'Los Angeles': 2919})
        path_tree, optimized_param = self.g.shortest_path("Los Angeles")
        self.assertDictEqual(optimized_param, {'Chicago': 2025, 'Austin': 1377, 'Los Angeles': 0, 'Hartford': 2919, 'Miami': 2728})
        path_tree, optimized_param = self.g.shortest_path("Chicago")
        self.assertDictEqual(optimized_param, {'Los Angeles': 2025, 'Hartford': 894, 'Miami': 2287, 'Austin': 1163, 'Chicago': 0})
        path_tree, optimized_param = self.g.shortest_path("Miami")
        self.assertDictEqual(optimized_param, {'Hartford': 1393, 'Miami': 0, 'Los Angeles': 2728, 'Chicago': 2287, 'Austin': 1351})
        path_tree, optimized_param = self.g.shortest_path("Austin")
        self.assertDictEqual(optimized_param, {'Hartford': 2057, 'Los Angeles': 1377, 'Austin': 0, 'Miami': 1351, 'Chicago': 1163})

    # TODO: Which alg do you use here, and why?
    # Alg: Prim
    # Why:  Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
    def test_minimum_salt(self):
        """Test minimum salt"""
        path_tree, vertex_weights = self.g.minimum_salt()
        total = 0
        for distance in vertex_weights.values():
            total += distance
        self.assertEqual(total, 4785)

unittest.main()