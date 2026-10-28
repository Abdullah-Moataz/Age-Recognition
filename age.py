import streamlit as st
import importlib.util

st.write("Humanize installed:", importlib.util.find_spec("humanize") is not None)
st.write("TensorFlow installed:", importlib.util.find_spec("tensorflow") is not None)
