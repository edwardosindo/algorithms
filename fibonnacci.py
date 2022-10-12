# How to find Fibonacci numbers using Recusrsion

def fibonacci(n):
    assert n>=0 and int(n)==n, 'The number has to be positive number'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


- Table Name :Employees 
-- empID, name, managerID 
-- 1234, Tom, 4567 
-- 2345, Bob, 1356 
-- 4567, Henry, null 
-- 1356, Julia, null 
-- 4826, Jane, 1356 
-- 7890,Janet,1234
-- 9009,Peter,6789
-- write the query to fetch Name of employees that are managed byTOM 

-- select name == Tom from Employees;

-- A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning true if the integer is pandigital, and false otherwise.
-- Sample input : 1234567890
-- Output : True

-- Sample input : 1123456890
-- Output : False
-- # list of numbers
-- # sort 
-- #loop through the list

def is_pandigital_num(num): 
    assert int(num) == num, 'Not integer'
    if x in [num]:
        return True
    else:
        return False