
##############################
###### global variables ##### 
##############################

h = 1                            # integral weight

a_rate = 0.073                    # rate at which A decays into B (changeable)
b_rate = 0.025                    # rate at which B decays into C (changeable)

##############################
###### helper methods #######
##############################

def f(t, mass, rate):
    """
    This method is the function of decay, no minus sign
        't' - time, although not depended here
        'mass' - the dependent variable, or the mass
    """
    return mass * rate


def f_total(t, masses):
    """
    This method is the function of decay of all
        't' - time, although not depended here
        'masses' - the dependent variable, unpacks into mass A, B, C
    """
    a_mass, b_mass, c_mass = masses
    dadt = - a_mass * a_rate
    dbdt = - b_mass * b_rate + a_mass * a_rate
    dcdt = b_mass * b_rate
    return  dadt, dbdt, dcdt

'''

def f_c(t, mass):
    """
    This method is the function of decay of C only
        't' - time, although not depended here
        'mass' - the dependent variable, or the mass
    """
    return mass * b_rate

'''


def update_mass_euler(a_mass, b_mass, c_mass):
    """
    This method takes current mass of three substance, update them and return using Euler's method
        'i_mass' -- current mass of substance I
    """
    a_mass = a_mass - h * a_mass * a_rate
    b_mass = b_mass + h * (a_mass * a_rate - b_mass * b_rate)
    c_mass = c_mass + h * (b_mass * b_rate)

    return (a_mass, b_mass, c_mass)

def update_mass_RK4(t, a_mass, b_mass, c_mass):
    """
    This method takes current mass of three substance, update them and return using 4th order Runge Kutta's method
        't' -- current iteration
        'i_mass' -- current mass of substance I
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


def riemann_rule(x_vals, y_vals, z_vals, dV, rho):
        """
        Calculate inertia of shape using Riemann Sum
            'qi_vals' -- variable range of axis qi
            'dv' -- small chunk of volume
            'rho' -- shape density
        """
        I_riem = 0
        for x in x_vals:
            for y in y_vals:
                for z in z_vals:
                    r_sq = x ** 2 + y ** 2
                    I_riem += r_sq * dV
        return I_riem * rho


def trapezoidal_rule(x_vals, y_vals, z_vals, dV, rho):
        """
        Calculate inertia of shape using trapezoidal rule
            'qi_vals' -- variable range of axis qi
            'dv' -- small chunk of volume
            'rho' -- shape density
        """
        I_trap = 0
        for i in range(len(x_vals) - 1):
            for j in range(len(y_vals) - 1):
                for k in range(len(z_vals) - 1):
                    x = (x_vals[i] + x_vals[i+1]) / 2
                    y = (y_vals[j] + y_vals[j+1]) / 2
                    z = (z_vals[k] + z_vals[k+1]) / 2
                    r_sq = x ** 2 + y ** 2
                    I_trap += r_sq * dV
        return I_trap * rho
     