# Tree-CSP-solver.
These programs implement the tree-csp-solver algorithm, for my assignment in artificial intelligence course at University of Florence.

## What is inside this repository?
A program called **tree_CSP_solver.py** implemented in python that implements this algorithm. This program already has an example with a simple scenario.
This scenario is graphically represented and solved in the image that is also in the repository called **figure**.

## Problem:
The algorithm is implemented in a general way to solve trees with no loops. In this case we consider this exercise:
*Scatter n points on the unit square; select a point X at random, connect X by a straight line to the nearest point Y such that X is not already connected to Y and the line crosses no other line; repeat the previous step until no more connections are possible.*

## How to use the code?
First of all, it will be necessary to study the problem, interpreting which are the nodes or variables, construct the arcs between them and see the constraints. The variables are represented as a vector; the domains are represented as a python dictionary in which each word (key) of the dictionary corresponds to a variable and its value will be a vector with the variables of the domain that it could take. In the same way, the constraints are a python dictionary each word is a variable and in the value the variables with which it has an arc (with which they are connected).