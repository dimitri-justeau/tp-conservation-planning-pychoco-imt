"""
STEP 1 - Build the base model
"""
from conservation_planning_model import ConservationPlanningModel

if __name__ == "__main__":

    TP1 = ConservationPlanningModel()
    s1 = TP1.solve_step_1()
    TP1.validate_base_model(s1)
    TP1.print_solution(s1)
