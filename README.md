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


## Problem 2 (numerical): Moment of Inertia for a non-trivial symmetrical object
