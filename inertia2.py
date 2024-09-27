import numpy as np
from integrals import riemann_rule, trapezoidal_rule
from scipy.integrate import simpson
import time
import matplotlib.pyplot as plt

##############################
###### global variables ##### 
##############################

side_length = 2                     # side length of the tetrahedron
h = side_length * np.sqrt(6) / 3    # height of the tetrahedron

M = 1.0                             # mass of the tetrahedron
V = (1/6) * np.sqrt(2) * h          # volume of the tetrahedron
rho = M / V                         # density of tetrahedron, linear


##############################
######### main method ########
##############################

if __name__ == "__main__":
    """
    Main Method
    """
    # --------------------------------------- Geometry Setup --------------------------------------- #

    vertices = np.array([                     # vertices of the tetrahedron, array of lists
    [0, 0, h],                                # top vertex
    [0, side_length / np.sqrt(3), 0],         # base vertex, on y
    [-1, - side_length / np.sqrt(3) / 2, 0],  # base vertex 2, on third quadrant of x-y plane
    [1, side_length / np.sqrt(3), 0]          # base vertex 3, on forth quadrant of x-y plane
    ])

    axis_point1 = np.array([0, 0, 0])                           # center of base, rotation axis bottom
    axis_point2 = np.array([0, side_length / np.sqrt(3), 0])    # top vertex, rotation axis top, rotation around z axis

    riem_int_list = []
    trap_int_list = []
    simp_int_list = []

    riem_tim_list = []
    trap_tim_list = []
    simp_tim_list = []

    for i in range (10, 101, 10): # loop over the # of divisions, from 10 to 100, increment of 10

        num_divisions = i             # of integration steps per dimension

        x_vals = np.linspace(-1, 1, num_divisions)          # integration meshing for x, y, z
        y_vals = np.linspace(- side_length / np.sqrt(3) / 2, side_length / np.sqrt(3), num_divisions)
        z_vals = np.linspace(0, h, num_divisions)

        dx = x_vals[1] - x_vals[0]                  # small chunks of x, y, z
        dy = y_vals[1] - y_vals[0]
        dz = z_vals[1] - z_vals[0]
        dV = dx * dy * dz

        # --------------------------------------- Solution Evaluation --------------------------------------- #

        time_riem_start = time.time()                                  # record time start
        I_riemann = riemann_rule(x_vals, y_vals, z_vals, dV, rho)      # evaluate integral
        time_riem_end = time.time()                                    # record time stop
        time_riem = time_riem_end - time_riem_start                    # get time diff
        riem_int_list.append(I_riemann)                                # append integral to list
        riem_tim_list.append(time_riem)                                # append time to list

        time_trap_start = time.time()
        I_trapezoidal = trapezoidal_rule(x_vals, y_vals, z_vals, dV, rho)
        time_trap_end = time.time()
        time_trap = time_trap_end - time_trap_start
        trap_int_list.append(I_trapezoidal)
        trap_tim_list.append(time_trap)

        X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals, indexing='ij')
        integrant = X ** 2 + Y ** 2

        time_simp_start = time.time()
        I_simpson_z = simpson(integrant, z_vals, axis=-1)  # integrate over z first
        I_simpson_yz = simpson(I_simpson_z, y_vals, axis=-1)  # over y
        I_simpson_xyz = simpson(I_simpson_yz, x_vals, axis=-1)  # finallly over x
        I_simpson = I_simpson_xyz * rho

        time_simp_end = time.time()
        time_simp = time_simp_end - time_simp_start
        simp_int_list.append(I_simpson)
        simp_tim_list.append(time_simp)
        
        print(f"{i} pieces per dimension of integration:")
        print(f"Moment of Inertia using Riemann Sum: {I_riemann}, time used: {time_riem:.3} seconds")
        print(f"Moment of Inertia using Trapezoidal Rule: {I_trapezoidal}, time used: {time_trap:.3} seconds")
        print(f"Moment of Inertia using Simpson's Rule: {I_simpson}, time used: {time_simp:.3} seconds")
        print(f"")

    # --------------------------------------- Plot Error and Time --------------------------------------- #
    
    mesh_steps = np.arange(10, 101, 10)

    plt.plot(mesh_steps, np.absolute(np.array(riem_int_list) - np.array(simp_int_list)),
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Riemann Sum, to Simpson Scipy")
    
    plt.plot(mesh_steps, np.absolute(np.array(trap_int_list) - np.array(simp_int_list)),
            color = '#f6adc6', # Nadeshiko pink
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Trapezoidal Rule, to Simpson Scipy")
    
    plt.plot(mesh_steps, np.absolute(np.array(simp_int_list) - np.array(simp_int_list)), # will give zero of course
            color = '#00ced1', # Dark turquoise
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Simpson's Rule, to Simpson Scipy")
    
    plt.title('Tetrahedron Inertia Integration Methods Error Comparison to Scipy')
    plt.xlabel('Integration Meshes per Dimension [steps]')
    plt.ylabel('Difference of Moment of Inertia')
    plt.legend(loc=5, prop={'size': 6})

    plot_destination = "figures/inertia_comparison.png"
    plt.savefig(plot_destination, dpi=500)

    plt.clf()

    plt.plot(mesh_steps, riem_tim_list,
            color = '#007ba7', # cerulean
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Riemann Sum")
    
    plt.plot(mesh_steps, trap_tim_list,
            color = '#f6adc6', # Nadeshiko pink
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Trapezoidal Rule")
    
    plt.plot(mesh_steps, simp_tim_list, # will give zero of course
            color = '#00ced1', # Dark turquoise
            marker = "None",
            linestyle = "solid",
            markersize = 3,
            label = f"Simpson's Rule")
    
    plt.title('Tetrahedron Inertia Integration Methods - Time Comparison')
    plt.xlabel('Integration Meshes per Dimension [steps]')
    plt.ylabel('Time Taken [seconds]')
    plt.legend(loc=5, prop={'size': 6})

    plot_destination = "figures/inertia_time_comparison.png"
    plt.savefig(plot_destination, dpi=500)


