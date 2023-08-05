from app import app
import pytest

def test_addition():
    response = app.test_client().post("/calculate", data={"number_one": "5", "number_two": "3", "operation": "add"})
    assert b"8.0" in response.data

def test_subtraction():
    response = app.test_client().post("/calculate", data={"number_one": "10", "number_two": "7", "operation": "subtract"})
    assert b"3.0" in response.data

def test_multiplication():
    response = app.test_client().post("/calculate", data={"number_one": "4", "number_two": "5", "operation": "multiply"})
    assert b"20.0" in response.data

def test_division():
    response = app.test_client().post("/calculate", data={"number_one": "12", "number_two": "3", "operation": "divide"})
    assert b"4.0" in response.data

def test_invalid_operation():
    response = app.test_client().post("/calculate", data={"number_one": "5", "number_two": "3", "operation": "invalid"})
    assert b"Error: Invalid operation" in response.data

def test_divide_by_zero():
    response = app.test_client().post("/calculate", data={"number_one": "10", "number_two": "0", "operation": "divide"})
    assert b"Error: Cannot divide by zero" in response.data
