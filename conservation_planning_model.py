from pychoco import Model, create_undirected_graph
from pychoco.solution import Solution

from data import *


class ConservationPlanningModel:

    def __init__(self):
        self.model = Model("Conservation planning")

        # TODO
        # -- Init variables here -- #
        self.selected = None
        self.nb_pus = None
        self.occ_tree_A = None
        self.occ_tree_B = None
        self.occ_tree_C = None
        self.occ_tree_D = None
        self.occ_fern = None
        self.occ_bird = None
        self.occ_gecko = None
        # -- End init variables -- #
        # TODO

        self.plant_species = [self.occ_tree_A, self.occ_tree_B, self.occ_tree_C, self.occ_tree_D, self.occ_fern]
        self.animal_species = [self.occ_bird, self.occ_gecko]
        self.species = self.plant_species + self.animal_species
        self.post_base_model_constraints()
        self.model.get_solver().show_short_statistics()

    def post_base_model_constraints(self):
        # TODO
        pass

    def solve_step_1(self) -> Solution:
        # TODO
        pass

    def solve_step_2(self) -> Solution:
        # TODO
        pass

    def solve_step_3(self) -> Solution:
        # TODO
        pass

    def solve_step_4(self) -> Solution:
        # TODO
        pass

    def solve_step_5(self) -> Solution:
        # TODO
        pass

    def print_solution(self, solution: Solution):
        print("Conservation planning solution:")
        print("  Nb PUs: {}".format(solution.get_int_val(self.nb_pus)))
        print("  Occurrences: ")
        print("    Tree A: {}".format(solution.get_int_val(self.occ_tree_A)))
        print("    Tree B: {}".format(solution.get_int_val(self.occ_tree_B)))
        print("    Tree C: {}".format(solution.get_int_val(self.occ_tree_C)))
        print("    Tree D: {}".format(solution.get_int_val(self.occ_tree_D)))
        print("    Fern: {}".format(solution.get_int_val(self.occ_fern)))
        print("    Bird: {}".format(solution.get_int_val(self.occ_bird)))
        print("    Gecko: {}".format(solution.get_int_val(self.occ_gecko)))
        print("  - - - - - - - - - -")
        for row in range(0, HEIGHT):
            line = "| "
            for col in range(0, WIDTH):
                v = solution.get_int_val(self.selected[get_index_from_row_col(row, col)])
                line += "{} ".format(v)
            print(line + "|")
        print("  - - - - - - - - - -")

    def validate_base_model(self, solution: Solution):
        count_occ_tree_a = sum([solution.get_int_val(self.selected[i]) * OCC_TREE_A[i] for i in range(0, N)])
        if count_occ_tree_a != solution.get_int_val(self.occ_tree_A):
            raise AssertionError("The number of occurrences of tree A is not correct")
        count_occ_tree_b = sum([solution.get_int_val(self.selected[i]) * OCC_TREE_B[i] for i in range(0, N)])
        if count_occ_tree_b != solution.get_int_val(self.occ_tree_B):
            raise AssertionError("The number of occurrences of tree B is not correct")
        count_occ_tree_c = sum([solution.get_int_val(self.selected[i]) * OCC_TREE_C[i] for i in range(0, N)])
        if count_occ_tree_c != solution.get_int_val(self.occ_tree_C):
            raise AssertionError("The number of occurrences of tree C is not correct")
        count_occ_tree_d = sum([solution.get_int_val(self.selected[i]) * OCC_TREE_D[i] for i in range(0, N)])
        if count_occ_tree_d != solution.get_int_val(self.occ_tree_D):
            raise AssertionError("The number of occurrences of tree D is not correct")
        count_occ_fern = sum([solution.get_int_val(self.selected[i]) * OCC_FERN[i] for i in range(0, N)])
        if count_occ_fern != solution.get_int_val(self.occ_fern):
            raise AssertionError("The number of occurrences of fern is not correct")
        count_occ_bird = sum([solution.get_int_val(self.selected[i]) * OCC_BIRD[i] for i in range(0, N)])
        if count_occ_bird != solution.get_int_val(self.occ_bird):
            raise AssertionError("The number of occurrences of bird is not correct")
        count_occ_gecko = sum([solution.get_int_val(self.selected[i]) * OCC_GECKO[i] for i in range(0, N)])
        if count_occ_gecko != solution.get_int_val(self.occ_gecko):
            raise AssertionError("The number of occurrences of gecko is not correct")

    def validate_covering_set_plants(self, solution: Solution, min_occ):
        if solution.get_int_val(self.occ_tree_A) < min_occ:
            raise AssertionError("Not enough occurrences of Tree A")
        if solution.get_int_val(self.occ_tree_B) < min_occ:
            raise AssertionError("Not enough occurrences of Tree B")
        if solution.get_int_val(self.occ_tree_C) < min_occ:
            raise AssertionError("Not enough occurrences of Tree C")
        if solution.get_int_val(self.occ_tree_D) < min_occ:
            raise AssertionError("Not enough occurrences of Tree D")
        if solution.get_int_val(self.occ_fern) < min_occ:
            raise AssertionError("Not enough occurrences of Fern")

    def validate_covering_set_animals(self, solution: Solution, min_occ):
        if solution.get_int_val(self.occ_bird) < min_occ:
            raise AssertionError("Not enough occurrences of Bird")
        if solution.get_int_val(self.occ_gecko) <  min_occ:
            raise AssertionError("Not enough occurrences of Gecko")

    def validate_covering_set(self, solution: Solution, min_occ):
        self.validate_covering_set_plants(solution, min_occ)
        self.validate_covering_set_animals(solution, min_occ)

    def make_graph_var(self):
        lb = create_undirected_graph(self.model, N)
        ub = create_undirected_graph(self.model, N)
        for i in range(0, N):
            for j in get_neighbors(i):
                ub.addEdge(i, j)
        g = self.model.node_induced_graphvar(lb, ub, "G")
        self.model.graph_nodes_channeling(g, self.selected).post()
        return g


def get_index_from_row_col(row, col):
    return row * WIDTH + col


def get_neighbors(cell_index):
    left = cell_index - 1 if cell_index % WIDTH != 0 else -1
    right = cell_index + 1 if (cell_index + 1) % WIDTH != 0 else -1
    top = cell_index - WIDTH if cell_index >= WIDTH else -1
    bottom = cell_index + WIDTH if cell_index < WIDTH * (HEIGHT - 1) else -1
    return [x for x in [left, right, top, bottom] if x >= 0]
