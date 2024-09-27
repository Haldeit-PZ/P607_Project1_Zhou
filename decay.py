import numpy as np
import matplotlib.pyplot as plt
from integrals import update_mass_euler, update_mass_RK4, f, f_total, a_rate, b_rate
from scipy.integrate import solve_ivp

import time

##############################
###### global variables ##### 
##############################

    # decay rate can be changed under integrals.py

a_mass = 100                     # starting mass of A (changeable)
b_mass = 0                       # starting mass of B (changeable)
c_mass = 0                       # starting mass of C (changeable, although not significant to result)

time_start = 1
time_end = 100
time_number = 100

mass_max = np.array([a_mass, b_mass, c_mass]).max() # acquiring the height for a vertical line, marking turning point for substance B

##############################
######### main method ########
##############################

if __name__ == "__main__":
    """
    Main Method
    """
    
    a_mass_list_euler = []                              # initializing arrays for plots
    b_mass_list_euler = []
    c_mass_list_euler = []

    a_mass_list_RK4 = []
    b_mass_list_RK4 = []
    c_mass_list_RK4 = []    

    a_mass_euler, a_mass_RK4 = a_mass, a_mass           # assign variables for iterations for various integral methods
    b_mass_euler, b_mass_RK4 = b_mass, b_mass
    c_mass_euler, c_mass_RK4 = c_mass, c_mass

    t = np.linspace(time_start, time_end, time_number)  # initialize time array

    for i in range (t.size):                            # iterations via for-loop
        a_mass_list_euler.append(a_mass_euler)
        b_mass_list_euler.append(b_mass_euler)
        c_mass_list_euler.append(c_mass_euler)
        a_mass_euler, b_mass_euler, c_mass_euler = update_mass_euler(a_mass_euler, b_mass_euler, c_mass_euler)

        a_mass_list_RK4.append(a_mass_RK4)
        b_mass_list_RK4.append(b_mass_RK4)
        c_mass_list_RK4.append(c_mass_RK4)
        a_mass_RK4, b_mass_RK4, c_mass_RK4 = update_mass_RK4(i, a_mass_RK4, b_mass_RK4, c_mass_RK4)

    # solution using Scipy (BDF)

    mass_list_scipy = solve_ivp(f_total, [t[0], t[-1]], [a_mass, b_mass, c_mass], method='BDF', t_eval=t).y
    a_mass_list_scipy = mass_list_scipy[0, :]           # unpacks the a, b, c mass
    b_mass_list_scipy = mass_list_scipy[1, :]
    c_mass_list_scipy = mass_list_scipy[2, :]

    b_max_t = np.array(b_mass_list_scipy).argmax()    # acquiring the 'x' position of a vertical line for turning point in substance B

    # --------------------------------------- Euler Plots --------------------------------------- #

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
    
    # --------------------------------------- RK4 Plots --------------------------------------- #

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
    
    # --------------------------------------- scipy (BDF) Plots --------------------------------------- #
    
    plt.plot(t, a_mass_list_scipy,
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Substance A (Scipy), rate: {a_rate}")
    
    plt.plot(t, b_mass_list_scipy,
            color = '#f6adc6', # Nadeshiko pink
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Substance B (Scipy), rate: {b_rate}")
    
    plt.plot(t, c_mass_list_scipy,
            color = '#00ced1', # Dark turquoise
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Substance C (Scipy), rate: stable")
    
    
    plt.title('Compound Decay - A->B->C')
    plt.xlabel('Time [unit time]')
    plt.ylabel('Mass [unit mass]')
    plt.legend(loc=5, prop={'size': 6})

    plot_destination = "figures/euler-RK4_overlapped.png"
    plt.savefig(plot_destination, dpi=500)

    