from .pseudocritical_properties import natural_gas_systems2
from .automate_integral_df import pseudo_reduced_bhp
from .automate_integral_df2 import pseudo_reduced_bhp2

class StaticBHP:
    @staticmethod
    def staticbhp_for_ppr_gt_2(reduced_temp, reduced_pressure, scrhs, gas_specific_gravity):
        """Function to compute the Static Bottom Hole Pressure
        when pseudo_reduced_wellhead_pressure is greater than or equal to 2.0

        Return:
            pws(floats): The static BHP rounded to 3 decimal places
        """
        pws = pseudo_reduced_bhp(reduced_temp, reduced_pressure, scrhs) * natural_gas_systems2(gas_specific_gravity)
        return f"The static BHP is: {round(pws, 3)} psia"

    @staticmethod
    def staticbhp_for_ppr_lt_2(reduced_temp, reduced_pressure, scrhs, gas_specific_gravity):
        """Function to compute the Static Bottom Hole Pressure
        when pseudo_reduced_wellhead_pressure is less than 2.0

        Return:
            pws(floats): The static BHP rounded to 3 decimal places
        """
        pws = pseudo_reduced_bhp2(reduced_temp, reduced_pressure, scrhs) * natural_gas_systems2(gas_specific_gravity)
        return f"The static BHP is: {round(pws, 3)} psia"

    @staticmethod
    def print_staticbhp(reduced_temp, reduced_pressure, scrhs, gas_specific_gravity):
        try:
            if reduced_pressure >= 2.0:
                return StaticBHP.staticbhp_for_ppr_gt_2(reduced_temp, reduced_pressure, scrhs, gas_specific_gravity)
            elif reduced_pressure < 2.0:
                return StaticBHP.staticbhp_for_ppr_lt_2(reduced_temp, reduced_pressure, scrhs, gas_specific_gravity)
        except Exception as e:
            return f'Error: {e}'
