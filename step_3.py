"""
STEP 3 - Same as STEP 2, but find a minimal-cost protected area
"""
from conservation_planning_model import ConservationPlanningModel

if __name__ == "__main__":

    TP3 = ConservationPlanningModel()
    s3 = TP3.solve_step_3()
    TP3.validate_base_model(s3)
    TP3.validate_covering_set(s3, 1)
    if s3.get_int_val(TP3.nb_pus) > 3:
        raise AssertionError("The solution is not optimal")
    TP3.print_solution(s3)
