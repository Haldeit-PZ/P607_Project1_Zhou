import numpy as np
import matplotlib as plt

##############################
###### global variables #####
##############################

a_rate = 0.2                    # rate at which A decays into B
b_rate = 0.1                    # rate at which B decays into C

a_mass = 100
b_mass = 0
c_mass = 0

##############################
###### helper functions #####
##############################

def update_mass(a_mass, b_mass, c_mass):
    """
    This method takes current mass of three substance, update them and return.
        'a_mass' -- current mass of substance A
        'b_mass' -- current mass of substance B
        'c_mass' -- current mass of substance C
    """
    a_mass = a_mass - a_mass * a_rate
    b_mass = b_mass + a_mass * a_rate - b_mass * b_rate
    c_mass = c_mass + b_mass * b_rate

    return (a_mass, b_mass, c_mass)


if __name__ == "__main__":
    """
    Main Method
    """

    a_mass_list = []
    b_mass_list = []
    c_mass_list = []

    a_mass_list.append(a_mass)
    b_mass_list.append(b_mass)
    c_mass_list.append(c_mass)

    t = np.arange(0, 1000)

    for i in range (t.size - 1):
        a_mass, b_mass, c_mass = update_mass(a_mass, b_mass, c_mass)
        a_mass_list.append(a_mass)
        b_mass_list.append(b_mass)
        c_mass_list.append(c_mass)

    plt.plot(t, a_mass_list,
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = "-.",
            markersize = 3,
            label = "Substance A")
    
    plt.plot(t, b_mass_list,
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = "-.",
            markersize = 3,
            label = "Substance B")
    
    plt.plot(t, c_mass_list,
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = "-.",
            markersize = 3,
            label = "Substance C")
    
    plt.title('Compound Decay - A->B->C')
    plt.xlabel('Time')
    plt.ylabel('Mass')
    plt.legend()

    plot_destination = "figures/decay_overlapped.png"
    plt.savefig(plot_destination)

    