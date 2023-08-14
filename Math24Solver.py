# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:15:40 2023

@author: arnav
"""

import itertools

def solve_24(nums):
    if len(nums) == 1:
        if abs(nums[0] - 24) < 1e-6:
            return [str(nums[0])]
        else:
            return []
    
    solutions = []
    for perm in itertools.permutations(nums):
        for ops in itertools.product('+-*/', repeat=3):
            expression = f'(({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}){ops[2]}{perm[3]}'
            try:
                result = eval(expression)
                if abs(result - 24) < 1e-6:
                    solutions.append(expression)
            except ZeroDivisionError:
                pass
    
    return solutions

def find_24_solutions(nums):
    solutions = solve_24(nums)
    return solutions

# Example usage
input_numbers = [1, 2, 3, 4]
solutions = find_24_solutions(input_numbers)

if solutions:
    for idx, sol in enumerate(solutions):
        print(f"Solution {idx + 1}: {sol} = 24")
else:
    print("No solutions found.")
