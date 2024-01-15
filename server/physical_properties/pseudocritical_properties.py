def natural_gas_systems(gas_specific_gravity):
    """Function to calculate pseudocritical
    temperature of gas

    Return
        floats: pseudocritical temperature
    """
    tpc_natural_gas_systems = 170.491 + (307.344 * gas_specific_gravity) + (10.54 * gas_specific_gravity**2)
    return tpc_natural_gas_systems


def natural_gas_systems2(gas_specific_gravity):
    """Function to calculate pseudocritical
    pressure of gas

    Return:
        floats: pseudocritical pressure
    """
    ppc_natural_gas_systems = 709.604 - (58.718 * gas_specific_gravity) + (3.015*gas_specific_gravity**2)
    return ppc_natural_gas_systems


def gas_condensate_systems(gas_specific_gravity):
    """Function to calculate pseudocritical
    temperature in gas condensate systems

    Return:
        floats: pseudocritical temperature
    """
    tpc_gas_condensate_systems = 149.18 + 358.14 * gas_specific_gravity - 66.976 * gas_specific_gravity ** 2
    return tpc_gas_condensate_systems


def gas_condensate_systems2(gas_specific_gravity):
    """Function to compute pseudocritical
    pressure in gas condensate systems

    Return:
        floats: pseudocritical pressure
    """
    ppc_gas_condensate_systems = 787.06 - 147.34 * gas_specific_gravity - 7.916 * gas_specific_gravity ** 2
    return ppc_gas_condensate_systems
