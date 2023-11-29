import streamlit as st
st.title("calculate x * y")

form=st.form(key="test")

X=form.number_input("enter the value of x ", value=1, key = "x")
Y=form.number_input("enter the value of y ", value=1, key = "y")

if form.form_submit_button("x * y"):
    form.write(f" x * y = {X*Y}")
