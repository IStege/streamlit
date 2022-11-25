import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(page_title="Test-app main app", layout="centered", page_icon="🐱")


st.markdown("""# This is a header
## This is a sub header
## etc
This is text

- this
- is
- a
- list""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

with st.echo():
    st.write("hello")



st.write(st.secrets['section']['another_key'])
