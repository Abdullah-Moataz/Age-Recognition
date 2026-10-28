import streamlit as st
import importlib.util
import sys

st.title("Dependency Check")

st.write("Python version:", sys.version)
st.write("TensorFlow installed:", importlib.util.find_spec("tensorflow") is not None)
st.write("Keras installed:", importlib.util.find_spec("keras") is not None)
