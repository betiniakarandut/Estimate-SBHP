from .conversions import temp_avg_in_rankine
from .pseudocritical_properties import natural_gas_systems, natural_gas_systems2


def pseudo_reduced_temp(temp_avg_sys, gas_specific_gravity):
    """Function to compute reduced temperature

    Return
        floats: reduced temperature rounded to one
        decimal place
    """
    tpr_pseudo_reduced_temp = float(temp_avg_in_rankine(temp_avg_sys)) / natural_gas_systems(gas_specific_gravity)
    return round(tpr_pseudo_reduced_temp, 1)

def pseudo_reduced_wellhead_pressure(static_wellhead_pressure, gas_specific_gravity):
    """Function to compute reduced pressure
    at wellhead pressure

    Return:
        floats: reduced pressure at wellhead rounded
        to three decimal places
    """
    try:
        if static_wellhead_pressure <= 0:
            raise ValueError("Static wellhead pressure is not valid")
        else:
            ppr1_wellhead = static_wellhead_pressure / natural_gas_systems2(gas_specific_gravity)
            return round(ppr1_wellhead, 3)
    except Exception as e:
        print(f"Error: Enter a valid wellhead pressure ==> {e}")
