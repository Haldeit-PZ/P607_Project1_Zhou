# Project 1 Overview

## Problem 1 (ODE): Radioactive Compound-Decay
We know that radioactive decay of  substance A-B follows the simple ODE:

## $\frac{dN_A}{dt} = -\lambda_A N_A(t)$

Solving the ODE, one yields:
## $N_A(t) = N_A(0)e^{-\lambda_A t}$

In this problem, one shall consider an element decaying into other elements in series in the form of A-B-C. In the above single case, the $N$ describes $N_A$ to be specifically, where nothing is decaying into sustance A. In the new case, if one were to consider the rate of change of substance B, there are two factors, where A decays into B, increasing number of B; On the other hand, B is decreasing as it decays to C. More specifically:

## $\frac{dN_B}{dt} = \lambda_A N_A(t) - \lambda_B N_B(t)$

The setup of this problem begins with certain mass of substance A, B, the amount of substance A decreases as it decays into B; B gains mass from decayed A, and losses mass from decaying into C; C only gains mass. In the long run, C will dominate to be the majority. The function will perform a fixed amount of iterations using a for-loop, as substance mass of A will asymptomatically approach zero, quicker than mass B.

Here're some helpful (methods) functions:
### 1. Update the next set of mass A, B, and C. This method takes in the current set of A, B, C, change the substance with the decay rate (gammas are global variables) and return them.


## Problem 2 (numerical): Moment of Inertia for a non-trivial, not so symmetrical object (tetrahedron)

More specifically, the moment of inertia has its axis defined going through one of its vertex, exiting at the center of the equilatteral trangle on the other side. One might define the pointing direction of vertex with the spinning axis going through as positive Z axis. The I solution follows:

## $I_{ij} = \int \rho(q_i,q_j,q_k) (r^2 \delta_{ij} - q_i q_j)d\tau$
In the case if Z is spining axis:
## $I_zz = \int\int\int \rho(x,y,z)(x^2+y^2+z^2 - z^2) dx dy dz = \int\int\int \rho(x,y,z)(x^2+y^2)dx dy dz $

