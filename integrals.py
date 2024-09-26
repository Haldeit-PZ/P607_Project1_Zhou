##############################
###### global variables ##### 
##############################

h = 2                            # integral weight

a_rate = 0.073                    # rate at which A decays into B (changeable)
b_rate = 0.025                    # rate at which B decays into C (changeable)

##############################
###### helper methods #######
##############################

def f(t, mass, rate):
    """
    This method is the function of decay
        't' - time, although not depended here
        'mass' - the dependent variable, or the mass
    """
    return mass * rate

def update_mass_euler(a_mass, b_mass, c_mass):
    """
    This method takes current mass of three substance, update them and return using Euler's method
        'a_mass' -- current mass of substance A
        'b_mass' -- current mass of substance B
        'c_mass' -- current mass of substance C
    """
    a_mass = a_mass - h * a_mass * a_rate
    b_mass = b_mass + h * (a_mass * a_rate - b_mass * b_rate)
    c_mass = c_mass + h * (b_mass * b_rate)

    return (a_mass, b_mass, c_mass)

def update_mass_RK4(t, a_mass, b_mass, c_mass):
    """
    This method takes current mass of three substance, update them and return using 4th order Runge Kutta's method
        'a_mass' -- current mass of substance A
        'b_mass' -- current mass of substance B
        'c_mass' -- current mass of substance C
    """

    k1_a_mass = f(t, a_mass, a_rate)
    k2_a_mass = f(t + h / 2, a_mass + h * k1_a_mass / 2, a_rate)
    k3_a_mass = f(t + h / 2, a_mass + h * k2_a_mass / 2, a_rate)
    k4_a_mass = f(t + h, a_mass + h * k3_a_mass, a_rate)
    a_update = h / 6 * (k1_a_mass + 2 * k2_a_mass + 2 * k3_a_mass + k4_a_mass)
    a_mass = a_mass - a_update

    k1_b_mass = f(t, b_mass, b_rate)
    k2_b_mass = f(t + h / 2, b_mass + h * k1_b_mass / 2, b_rate)
    k3_b_mass = f(t + h / 2, b_mass + h * k2_b_mass / 2, b_rate)
    k4_b_mass = f(t + h, b_mass + h * k3_b_mass, b_rate)
    b_update = h / 6 * (k1_b_mass + 2 * k2_b_mass + 2 * k3_b_mass + k4_b_mass)
    b_mass = b_mass + a_update - b_update

    c_mass = c_mass + b_update

    return (a_mass, b_mass, c_mass)