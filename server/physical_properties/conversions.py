def temp_avg_in_rankine(temp_avg_sys):
    """Function to calculate temperature in degrees rankine

    Return:
        floats: Temperature in degrees rankine

    """
    value = 460 + float(temp_avg_sys)
    return value

def evaluate_scrhs(gas_specific_gravity, well_depth, temp_avg_sys):
    """Function to evaluate the sukkar and cornell
    integral right hand side

    Return:
        floats: sukkar and cornell integral-RHS
    """
    scrhs = (0.01875 * float(gas_specific_gravity * well_depth)) / float(temp_avg_in_rankine(temp_avg_sys))
    return round(scrhs, 4)
