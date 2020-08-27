from calculator import add
from calculator import factorial
from calculator import sin
from calculator import divide
from calculator import less_than
from calculator import innerprod
from math import pi
import math
import pytest


def test_add_exercise_1():
    x = 1
    y = 2
    expected_sum = 3
    computed = add(x,y)
    assert computed == expected_sum 

def test_add_floats_exercise_2():
    tol = 1e-10
    x = 0.1
    y = 0.2
    expected_sum = 0.3
    computed = add(x,y)
    assert abs(computed - expected_sum) < tol

def test_add_strings_exercise_3():
    x = "Hello "
    y = "World"
    expected = "Hello World"
    computed = add(x,y)
    assert expected == computed
  
def test_factorial_exercise_4():
    n = 3
    expected = math.factorial(n)
    computed = factorial(n)
    assert expected == computed

def test_sin_exercise_4():
    tol = 1e-6
    x = pi
    N = 10
    expected = math.sin(x)
    computed = sin(x,N)
    assert abs(expected - computed) < tol

def test_divide_exercise_4():
    tol = 1e-10
    x = 1
    y = 2
    expected = 0.5
    computed = divide(x,y)
    assert abs(expected - computed) < tol


def test_less_than_exercise_4():
    input_list = [1,3,5]
    n = 4
    expected = [1,3]
    computed = less_than(input_list,n)
    for a,b in zip(expected,computed):
        assert a == b

def test_innerprod_exercise_4():
    x = [1,2,3]
    y = [0,1,2]
    expected = 8
    computed = innerprod(x,y)
    assert expected == computed

def test_add_raises_TypeError_for_string_added_with_number_exercise_5():
    with pytest.raises(TypeError):
        add("Hello",2)

def test_divide_raises_ZeroDivisionError_when_dividing_by_zero_exercise_5():
    with pytest.raises(ZeroDivisionError):
        divide(2,0)


@pytest.mark.parametrize("arg, expected_output", [[(-1, -1), -2], [(0.1, 0.1), 0.2], [("Hello ", "World"), "Hello World"]])
def test_add_parametrized_exersice_6(arg,expected_output):
    assert add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[0, 1], [1, 1], [3,6]])
def test_factorial_parametrized_exersice_6(arg,expected_output):
    assert factorial(arg) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(pi, 10), 0], [(pi/2,10), 1], [(3*pi/2,10), -1]])
def test_sin_parametrized_exersice_6(arg,expected_output):
    tol = 1e-6
    assert abs(sin(arg[0], arg[1]) - expected_output) < tol

@pytest.mark.parametrize("arg, expected_output", [[(1, 2), 0.5], [(10, 2), 5], [(0.2, 10), 0.02]])
def test_divide_parametrized_exersice_6(arg,expected_output):
    assert divide(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[([1,2,3], 3), [1,2]], [([5,8,10], 6), [5]], [([9,4,7], 8), [4,7]]])
def test_less_than_parametrized_exersice_6(arg,expected_output):
    assert less_than(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[([1,2,3], [1,2,3]), 14], [([5,8], [1,2]), 21], [([3,1], [1,1]), 4]])
def test_innerprod_parametrized_exersice_6(arg,expected_output):
    assert innerprod(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("string, x", [["Hello",1], ["Name",2], ["Test",3]])
def test_add_raises_TypeError_for_string_added_with_number_exercise_5(string, x):
    with pytest.raises(TypeError):
        add(string,x) 

@pytest.mark.parametrize("x", range(10))
def test_divide_raises_ZeroDivisionError_when_dividing_by_zero_exercise_5(x):
    with pytest.raises(ZeroDivisionError):
        divide(x,0) 