"""
STEP 2 - Identify a protected area covering all the species
"""
from conservation_planning_model import ConservationPlanningModel

if __name__ == "__main__":

    TP2 = ConservationPlanningModel()
    s2 = TP2.solve_step_2()
    TP2.validate_base_model(s2)
    TP2.validate_covering_set(s2, 1)
    TP2.print_solution(s2)
