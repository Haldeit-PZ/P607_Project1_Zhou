import numpy as np
import matplotlib.pyplot as plt
from integrals import update_mass_euler, update_mass_RK4, a_rate, b_rate

##############################
###### global variables ##### 
##############################

    # decay rate can be changed under integrals.py

a_mass = 100                     # starting mass of A (changeable)
b_mass = 0                       # starting mass of B (changeable)
c_mass = 0                       # starting mass of C (changeable, although not significant to result)

mass_max = np.array([a_mass, b_mass, c_mass]).max() # for purpose of plotting vertical line siz


##############################
######### main method ########
##############################

if __name__ == "__main__":
    """
    Main Method
    """
    
    a_mass_list_euler = []
    b_mass_list_euler = []
    c_mass_list_euler = []

    a_mass_list_RK4 = []
    b_mass_list_RK4 = []
    c_mass_list_RK4 = []    

    a_mass_euler, a_mass_RK4 = a_mass, a_mass
    b_mass_euler, b_mass_RK4 = b_mass, b_mass
    c_mass_euler, c_mass_RK4 = c_mass, c_mass

    t = np.arange(0, 100)

    for i in range (t.size):
        a_mass_list_euler.append(a_mass_euler)
        b_mass_list_euler.append(b_mass_euler)
        c_mass_list_euler.append(c_mass_euler)
        a_mass_euler, b_mass_euler, c_mass_euler = update_mass_euler(a_mass_euler, b_mass_euler, c_mass_euler)

        a_mass_list_RK4.append(a_mass_RK4)
        b_mass_list_RK4.append(b_mass_RK4)
        c_mass_list_RK4.append(c_mass_RK4)
        a_mass_RK4, b_mass_RK4, c_mass_RK4 = update_mass_RK4(i, a_mass_RK4, b_mass_RK4, c_mass_RK4)


    b_max_t = np.array(b_mass_list_euler).argmax()

    plt.plot(t, a_mass_list_euler,
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = ":",
            markersize = 3,
            label = f"Substance A (Euler), rate: {a_rate}")
    
    
    plt.plot(t, b_mass_list_euler,
            color = '#f6adc6', # Nadeshiko pink
            marker = "None",
            linestyle = ":",
            markersize = 3,
            label = f"Substance B (Euler), rate: {b_rate}")
    
    plt.plot(t, c_mass_list_euler,
            color = '#00ced1', # Dark turquoise
            marker = "None",
            linestyle = ":",
            markersize = 3,
            label = f"Substance C (Euler), rate: stable")
    
    
    plt.plot(t, a_mass_list_RK4,
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = "--",
            markersize = 3,
            label = f"Substance A (RK4), rate: {a_rate}")
    
    plt.plot(t, b_mass_list_RK4,
            color = '#f6adc6', # Nadeshiko pink
            marker = "None",
            linestyle = "--",
            markersize = 3,
            label = f"Substance B (RK4), rate: {b_rate}")
    
    plt.plot(t, c_mass_list_RK4,
            color = '#00ced1', # Dark turquoise
            marker = "None",
            linestyle = "--",
            markersize = 3,
            label = f"Substance C (RK4), rate: stable")
    
    
    plt.vlines(b_max_t, 0, mass_max,
          color = '#343837', # charcoal
          linewidth = 1,
          linestyle = '-',
          label = f"B Max, at t = {b_max_t} [unit time]")
    
    
    plt.title('Compound Decay - A->B->C')
    plt.xlabel('Time [unit time]')
    plt.ylabel('Mass [unit mass]')
    plt.legend()

    plot_destination = "figures/euler-RK4_overlapped.png"
    plt.savefig(plot_destination)

    