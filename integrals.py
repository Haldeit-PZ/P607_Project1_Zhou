##############################
###### global variables ##### 
##############################

h = 1                            # integral weight

a_rate = 0.13                    # rate at which A decays into B (changeable)
b_rate = 0.05                    # rate at which B decays into C (changeable)

##############################
###### helper methods #######
##############################

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

def update_mass_RK4(a_mass, b_mass, c_mass):
    """
    This method takes current mass of three substance, update them and return using 4th order Runge Kutta's method
        'a_mass' -- current mass of substance A
        'b_mass' -- current mass of substance B
        'c_mass' -- current mass of substance C
    """

    


    return (a_mass, b_mass, c_mass)