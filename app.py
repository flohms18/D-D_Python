import streamlit as st
import pandas as pd
import os

st.title("Pandry")


'''
upload_file = st.file_uploader("Pick a CSV file", type=["csv"])

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)
'''

df = pd.read_csv("test_data.csv")
st.header("What to do with CSV file?")

RemoveNan = st.checkbox("Remove the NaN values?")

if RemoveNan:
    new_df = df.dropna()
    st.write(new_df)
    st.download_button(
        label="Download New CSV File",
        data = new_df.to_csv(index=False),
        mime="text/csv",
        icon=":material/download:",
    )
