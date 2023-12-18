"""
STEP 5 - Same as STEP 4, but we want the protected area to be connected
"""
from conservation_planning_model import ConservationPlanningModel

if __name__ == "__main__":

    TP5 = ConservationPlanningModel()
    s5 = TP5.solve_step_5()
    TP5.validate_base_model(s5)
    TP5.validate_covering_set_plants(s5, 1)
    TP5.validate_covering_set_animals(s5, 2)
    if s5.get_int_val(TP5.nb_pus) > 9:
        raise AssertionError("The solution is not optimal")
    TP5.print_solution(s5)
