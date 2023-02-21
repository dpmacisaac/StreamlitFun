import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# My first Streamlit Webpage

And then here is some more text. Here is a live update
""")

df = pd.read_csv('./data.csv')
st.dataframe(df)

options  = st.selectbox("Which options:", ["shhow plotting feature", "show slider"])
if options == 'shhow plotting feature':
    if st.checkbox('Show plotting feature:'):

        sample_df = pd.DataFrame(
            np.random.randn(50,3),
            columns=['a','b','c']
        )
        sample_df
        st.line_chart(sample_df)
elif options == "show slider":
    bonks = st.slider("bonks")
    st.write("bonks = " + str(bonks * 2))