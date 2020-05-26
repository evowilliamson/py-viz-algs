import unittest
from pythonalgos.graph.directed_graph import DirectedGraph
from pythonalgos.graph.directed_graph import DirectedGraph
from pythonalgos.graph.algorithm_ordering import AlgorithmOrdering
from pythonvizalgos.graph.viz_scc_kosaraju_tracing\
    import VizSccsKosarajuTracing
import os
from pythonalgos.util.logging import Logging
import pythonalgos.util.path_tools as pt
from os import path
import inspect


class TestVizSccsKosarajuTracing(unittest.TestCase):

    DIGRAPH_VIZ = "digraph_viz"
    RESOURCES_PATH = "python-test-resources/scc_kosaraju"
    RESOURCES_PATH_RECYCLE = RESOURCES_PATH + "/recycle"

    @classmethod
    def setUpClass(cls):
        pt.clean_dir_in_user_home(TestVizSccsKosarajuTracing.RESOURCES_PATH)

    def setUp(self):
        self.vertices = {1: [2], 2: [3, 6], 3: [4], 4: [5], 5: [1],
                         6: [7], 7: [8], 8: [9, 12], 9: [6, 10], 10: [],
                         11: [11], 12: [13], 13: []}
        self.directed_graph = DirectedGraph(self.vertices)

    def test_VizSccTracing_nontrivial(self):
        """ Functions more as a demonstration than as a test. It will create
        the animation for an acyclic graph"""

        self.directed_graph = \
            DirectedGraph(self.vertices,
                          algorithm_ordering=AlgorithmOrdering.ASC)
        dir = TestVizSccsKosarajuTracing.RESOURCES_PATH + "/" + \
            inspect.currentframe().f_code.co_name
        VizSccsKosarajuTracing.enable(
            pt.get_dir_in_user_home(dir),
            self.directed_graph,
            vertex_states=[
                    {VizSccsKosarajuTracing.ACTIVATED:
                        {"fillcolor": "red", "style": "filled"}},
                    {VizSccsKosarajuTracing.VISITED:
                        {"fillcolor": "gray", "style": "filled"}}])
        VizSccsKosarajuTracing.execute(self.directed_graph, resource_path=dir,
                                       nontrivial=True)
        self.assertTrue(True)

    def tearDown(self):
        pt.clean_dir_in_user_home(
            TestVizSccsKosarajuTracing.RESOURCES_PATH_RECYCLE)
        self.assertFalse(os.path.exists(pt.get_dir_in_user_home(
            TestVizSccsKosarajuTracing.RESOURCES_PATH_RECYCLE)))


if __name__ == '__main__':
    unittest.main()