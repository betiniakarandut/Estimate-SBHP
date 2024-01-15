"""
Module for automate_integral_df2.py
This module is for pressure less than 2000psia
or ppr less than 2.0
"""
import os
import pandas as pd
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path2 = os.path.join(script_dir, 'sukkarcornellintegral2.csv')
df2 = pd.read_csv(csv_file_path2)


def truncate_to_one_dp(digit_to_truncate):
    """Truncates a real number to 1 decimal place

    Args:
        digit_to_truncate[real number]

    Returns:
        the truncated digit
    """
    number_string = str(digit_to_truncate)
    decimal_index = number_string.find(".")
    if decimal_index != -1:
        truncated_number_string = number_string[:decimal_index + 2]
        return float(truncated_number_string)
    else:
        return digit_to_truncate


def print_target_pseudoreduced_pressure(reduced_pressure):
    """Truncates pseudoreduced pressure to 1 dp
    
    Args:
        reduced_pressure[float]-> input from user

    Return:
        truncated ppr
    """
    return truncate_to_one_dp(reduced_pressure)


def locate_cell_with_ppr(reduced_pressure):
    """Locates the cell containing ppr in the csv file
    
    Arg:
        reduced_pressure[float]-> input from user

    Returns:
        the found ppr
    """
    target_ppr = truncate_to_one_dp(reduced_pressure)
    find_ppr = df2["pseudoreduced_pressures"].searchsorted(target_ppr)
    return find_ppr


def value_of_cell_above_ppr(reduced_pressure):
    """Locates the value of the cell above ppr in the csv file
    
    Args:
        reduced_pressure[float]-> input from user

    Returns:
        ppr if cell_above_ppr > 0
        otherwise None
    """
    cell_above_ppr = locate_cell_with_ppr(reduced_pressure) - 1

    if cell_above_ppr > 0:
        return df2['pseudoreduced_pressures'][cell_above_ppr]
    # Handle the case where cell_above_ppr is 0 or negative
    else:
        return None


def locate_and_get_cell_values(reduced_pressure):
    """Locates the cell with ppr and retrieves the values of the cell above and below
    
    Args:
        reduced_pressure[float]-> input from user

    Returns:
        A tuple(ppr_cell_index, value_above, value_below)
    """
    ppr_cell_index = locate_cell_with_ppr(reduced_pressure)
    value_above = df2['pseudoreduced_pressures'][ppr_cell_index - 1]
    value_below = df2['pseudoreduced_pressures'][ppr_cell_index + 1]

    return ppr_cell_index, value_above, value_below


def sciv_for_cell_above_ppr(reduced_temp, reduced_pressure):
    """Locates the sciv cell above corresponding to ppr in the csv file
    
    Args:
        reduced_temp[float]-> input from user
        reduced_pressure[float]-> input from user
    
    Returns:
        Raise ValueError if reduced_temp is out of or below range.
        otherwise return sukkar&cornell integral value (sciv) corresponding
        to  cell above the ppr (pseudoreduced pressure)
    """
    try:
        target_ppr_index = locate_cell_with_ppr(reduced_pressure) - 1
        if not 1.5 <= reduced_temp <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            target_tpr_index = {1.5: 1, 1.6: 2, 1.7: 3}[reduced_temp]
            return df2.iloc[target_ppr_index, target_tpr_index]
    except Exception as e:
        print(f"Error: Index out of bound ==> {e}")


def sciv_for_cell_below_ppr(reduced_temp, reduced_pressure):
    """Locates the sciv cell above corresponding to ppr in the csv file
    
    Args:
        reduced_temp[float]-> input from user
        reduced_pressure[float]-> input from user
    
    Returns:
        Raise ValueError if reduced_temp is out of or below range.
        otherwise return sukkar&cornell integral value (sciv) corresponding
        to  cell below the ppr (pseudoreduced pressure)
    """
    try:
        target_ppr_index = locate_cell_with_ppr(reduced_pressure) + 1
        if not 1.5 <= reduced_temp <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            target_tpr_index = {1.5: 1, 1.6: 2, 1.7: 3}[reduced_temp]
            return df2.iloc[target_ppr_index, target_tpr_index]
    except Exception as e:
        print(f"Error: Index out of bound ==> {e}")


def sciv_for_ppr_cell(reduced_temp, reduced_pressure):
    """Locates the sciv cell above corresponding to ppr in the csv file
    
    Args:
        reduced_temp[float]-> input from user
        reduced_pressure[float]-> input from user
    
    Returns:
        Raise ValueError if reduced_temp is out of or below range.
        otherwise return sukkar&cornell integral value (sciv) corresponding
        to the ppr (pseudoreduced pressure)
    """
    try:
        target_ppr_index = locate_cell_with_ppr(reduced_pressure)
        if not 1.5 <= reduced_temp <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            target_tpr_index = {1.5: 1, 1.6: 2, 1.7: 3}[reduced_temp]
            return df2.iloc[target_ppr_index, target_tpr_index]
    except Exception as e:
        print(f"Error: Index out of bound ==> {e}")


def compute_denominator_sciv(reduced_temp, reduced_pressure):
    """Computes denominator side for the second linear interpolation
    
    Args:
        reduced_temp[float]-> input from user
        reduced_pressure[float]-> input from user

    Returns:
        difference between the above and below sciv
    """
    above = sciv_for_cell_above_ppr(reduced_temp, reduced_pressure)
    below = sciv_for_cell_below_ppr(reduced_temp, reduced_pressure)
    return above - below


def compute_the_value_of_unknown_sciv(reduced_temp, reduced_pressure):
    """Computes the unknown value of the sciv in the second linear interpolation
    Locates the cell with ppr and retrieves the values of the cell above and below
    Handles linear interpolation without recursion

    Args:
        reduced_temp[float]-> input from user
        reduced_pressure[float]-> input from user

    Returns:
        The computed value of the unknown sciv(sukkar&cornel integral value)
    """
    # Locates the cell with ppr and retrieves the values of the cell above and below
    ppr_cell_index = locate_cell_with_ppr(reduced_pressure)
    value_above = df2['pseudoreduced_pressures'][ppr_cell_index - 1]
    value_below = df2['pseudoreduced_pressures'][ppr_cell_index + 1]

    #Computes the LHS of the linear interpolation without recursion
    value_2 = value_above - value_below
    if value_2 == 0:
        return 0

    res = (value_above - reduced_pressure) / value_2
    above = sciv_for_cell_above_ppr(reduced_temp, reduced_pressure)
    deno_sciv = compute_denominator_sciv(reduced_temp, reduced_pressure)
    return above - (deno_sciv * res)


def pivot_sciv(reduced_temp, reduced_pressure, scrhs):
    """Determines the pivot sciv value
    
    Args:
        reduced_temp[float]-> input from user
        reduced_pressure[float]-> input from user
        scrhs[float] -> input from user

    Returns:
        Difference btw computed sciv and the scrhs
        [pivot_integral used to obtain the unknown ppr]
    """
    computed = compute_the_value_of_unknown_sciv(reduced_temp, reduced_pressure)
    return round(computed - scrhs, 4)


def pseudo_reduced_bhp2(reduced_temp, reduced_pressure, scrhs):
    """Function to compute reduced bottom hole pressure
    
    Args:
        reduced_temp[float]-> input from user
        reduced_pressure[float]-> input from user
        scrhs[float] -> input from user

    Returns:
        reduced bottom hole pressure rounded to one decimal place
    """
    try:
        # Checks for the column containing the Tpr
        target_column = f'pseudoreduced_temp{reduced_temp}'
        abs_diffs = np.abs(df2[target_column] - pivot_sciv(reduced_temp, reduced_pressure, scrhs))
        closest_index = abs_diffs.idxmin()
        closest_value = df2[target_column][closest_index]

        ppr = df2['pseudoreduced_pressures'][closest_index]
        cell_value_1_level_below_ppr = df2['pseudoreduced_pressures'][closest_index + 1]

        # Dictionary to store Tpr and its associated column
        tpr_to_column = {1.5: 1, 1.6: 2, 1.7: 3}

        # Gets the value of the intersect (the value of sciv above and below pivot sciv)
        target_tpr_index = tpr_to_column[reduced_temp]
        cell_value_above_pivot_sciv = df2.iloc[closest_index, target_tpr_index]
        cell_value_below_pivot_sciv = df2.iloc[closest_index + 1, target_tpr_index]

        numerator = cell_value_above_pivot_sciv - pivot_sciv(reduced_temp, reduced_pressure, scrhs)
        denominator = cell_value_above_pivot_sciv - cell_value_below_pivot_sciv
        LHS = numerator / denominator
        RHS_denominator = ppr - cell_value_1_level_below_ppr

        reduced_bhp = ppr - (LHS * RHS_denominator)
        return round(reduced_bhp, 1)
    except Exception as e:
        print(f"""
            Error: The result is not visible.
            Ensure that the input fields have met all the requirements.
            See error for details ==> {e}
        """)


print('<-------------------------------------->')
