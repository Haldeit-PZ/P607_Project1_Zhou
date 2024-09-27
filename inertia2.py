import numpy as np
from integrals import riemann_rule, trapezoidal_rule
from scipy.integrate import simpson
import time

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

    num_divisions = 100             # of integration steps per dimension

    x_vals = np.linspace(-1, 1, num_divisions)          # integration meshing for x, y, z
    y_vals = np.linspace(- side_length / np.sqrt(3) / 2, side_length / np.sqrt(3), num_divisions)
    z_vals = np.linspace(0, h, num_divisions)

    dx = x_vals[1] - x_vals[0]                  # small chunks of x, y, z
    dy = y_vals[1] - y_vals[0]
    dz = z_vals[1] - z_vals[0]
    dV = dx * dy * dz

    # --------------------------------------- Solution Evaluation --------------------------------------- #

    time_riem_start = time.time()
    I_riemann = riemann_rule(x_vals, y_vals, z_vals, dV, rho)
    time_riem_end = time.time()
    time_riem = time_riem_end - time_riem_start

    time_trap_start = time.time()
    I_trapezoidal = trapezoidal_rule(x_vals, y_vals, z_vals, dV, rho)
    time_trap_end = time.time()
    time_trap = time_trap_end - time_trap_start

    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals, indexing='ij')
    integrant = X ** 2 + Y ** 2

    time_simp_start = time.time()
    I_simpson_z = simpson(integrant, z_vals, axis=-1)  # integrate over z first
    I_simpson_yz = simpson(I_simpson_z, y_vals, axis=-1)  # over y
    I_simpson_xyz = simpson(I_simpson_yz, x_vals, axis=-1)  # finallly over x
    time_simp_end = time.time()
    time_simp = time_simp_end - time_simp_start

    I_simpson = I_simpson_xyz * rho
    
    # Print the results
    print(f"Moment of Inertia using Riemann Sum: {I_riemann}, time used: {time_riem:.3} seconds")
    print(f"Moment of Inertia using Trapezoidal Rule: {I_trapezoidal}, time used: {time_trap:.3} seconds")
    print(f"Moment of Inertia using Simpson's Rule: {I_simpson}, time used: {time_simp:.3} seconds")

