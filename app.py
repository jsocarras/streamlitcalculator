import streamlit as st

def calculate(n1, n2, operator):
    if operator == 'Add':
        return n1 + n2
    elif operator == 'Subtract':
        return n1 - n2
    elif operator == 'Multiply':
        return n1 * n2
    elif operator == 'Divide':
        if n2 == 0:
            return 'Error! Division by zero is not allowed.'
        else:
            return n1 / n2

st.title("Simple Calculator")

# Input fields
num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')

# Dropdown menu for operations
operation = st.selectbox(
    "Choose an operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f'The result is {result}')
