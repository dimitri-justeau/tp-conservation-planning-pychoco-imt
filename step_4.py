"""
STEP 4 - Same as STEP 3, but we want at least two occurrences of each species
"""
from conservation_planning_model import ConservationPlanningModel

if __name__ == "__main__":

    TP4 = ConservationPlanningModel()
    s4 = TP4.solve_step_4()
    TP4.validate_base_model(s4)
    TP4.validate_covering_set_plants(s4, 1)
    TP4.validate_covering_set_animals(s4, 2)
    if s4.get_int_val(TP4.nb_pus) > 4:
        raise AssertionError("The solution is not optimal");
    TP4.print_solution(s4)
