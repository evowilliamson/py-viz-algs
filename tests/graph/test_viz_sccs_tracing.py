import unittest
from pythonalgos.graph.directed_graph import DirectedGraph
from pythonalgos.graph.directed_graph import DirectedGraph
from pythonalgos.graph.algorithm_ordering import AlgorithmOrdering
from pythonvizalgos.graph.viz_cyclic_tracing import VizCyclicTracing
import os
from pythonalgos.util.logging import Logging
import pythonalgos.util.path_tools as pt
from os import path
import inspect


class TestVizCyclicTracing(unittest.TestCase):

    DIGRAPH_VIZ = "digraph_viz"
    RESOURCES_PATH = "python-test-resources"
    RESOURCES_PATH_RECYCLE = RESOURCES_PATH + "/recycle"

    @classmethod
    def setUpClass(cls):
        pt.clean_dir_in_user_home(TestVizCyclicTracing.RESOURCES_PATH)

    def setUp(self):
        self.vertices = {0: [1], 1: [2, 3], 2: [3],
                         3: [4, 6], 4: [5, 6], 5: [5], 6: [6]}
        self.directed_graph = DirectedGraph(self.vertices)

    def test_VizSccTracing_nontrivial(self):
        """ Functions more as a demonstration than as a test. It will create
        the animation for an acyclic graph"""

        Logging.enable()
        self.vertices = {0: [1], 1: [2, 3], 2: [3],
                         3: [4, 6], 4: [5, 6], 5: [7, 8], 6: [7, 8],
                         7: [9, 10, 11], 8: [11, 12], 9: [],
                         10: [11], 11: [12], 12: []}
        self.directed_graph = \
            DirectedGraph(self.vertices,
                          algorithm_ordering=AlgorithmOrdering.ASC)
        dir = TestVizCyclicTracing.RESOURCES_PATH + "/" + \
            inspect.currentframe().f_code.co_name
        VizCyclicTracing.enable(
            pt.get_dir_in_user_home(dir),
            self.directed_graph,
            vertex_states=[
                    {VizCyclicTracing.ACTIVATED:
                        {"fillcolor": "red", "style": "filled"}},
                    {VizCyclicTracing.IN_CYCLE:
                        {"fillcolor": "blue", "style": "filled"}},
                    {VizCyclicTracing.VISISTED:
                        {"fillcolor": "gray", "style": "filled"}}])
        VizCyclicTracing.execute(self.directed_graph, resource_path=dir)
        self.assertTrue(True)

    def test_VizCyclicTracing_cyclic(self):
        """ Functions more as a demonstration than as a test. It will create
        the animation for a cyclic graph"""

        Logging.enable()
        self.vertices = {0: [1], 1: [2, 3], 2: [3],
                         3: [4, 6], 4: [5, 6], 5: [7, 8], 6: [7, 8],
                         7: [9, 10, 11], 8: [3], 9: [],
                         10: [11], 11: [12], 12: []}
        self.directed_graph = \
            DirectedGraph(self.vertices,
                          algorithm_ordering=AlgorithmOrdering.ASC)
        dir = TestVizCyclicTracing.RESOURCES_PATH + "/" + \
            inspect.currentframe().f_code.co_name
        VizCyclicTracing.enable(
            pt.get_dir_in_user_home(dir),
            self.directed_graph,
            vertex_states=[
                    {VizCyclicTracing.ACTIVATED:
                        {"fillcolor": "red", "style": "filled"}},
                    {VizCyclicTracing.IN_CYCLE:
                        {"fillcolor": "blue", "style": "filled"}},
                    {VizCyclicTracing.VISISTED:
                        {"fillcolor": "gray", "style": "filled"}}])
        VizCyclicTracing.execute(self.directed_graph, resource_path=dir)
        self.assertTrue(True)

    def tearDown(self):
        pt.clean_dir_in_user_home(TestVizCyclicTracing.RESOURCES_PATH_RECYCLE)
        self.assertFalse(os.path.exists(pt.get_dir_in_user_home(
            TestVizCyclicTracing.RESOURCES_PATH_RECYCLE)))


if __name__ == '__main__':
    unittest.main()
