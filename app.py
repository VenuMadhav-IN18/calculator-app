import streamlit as st

st.title('Calculator App')

number1 = st.number_input('Enter first number:')
number2 = st.number_input('Enter second number:')

operation = st.selectbox('Select operation:', ['Addition', 'Subtraction','Multiplication', 'Division'])

ret = st.button('Calculate')

if ret:
    if operation == 'Addition':
        result = number1 + number2
    elif operation == 'Subtraction':
        result = number1 - number2
    elif operation == 'Multiplication':
        result = number1 * number2  
    elif operation == 'Division':
        result = number1 / number2
    
    st.write('Result:', result)