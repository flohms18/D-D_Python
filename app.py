import streamlit as st
import pandas as pd
import os

st.title("Pandry")




df = pd.read_csv("test_data.csv")
st.header("What to do with CSV file?")
st.write(df)

RemoveNan = st.checkbox("Remove the NaN values?")
RemoveDuplicates = st.checkbox("Remove Duplicates?")

if RemoveNan:
    new_df = df.dropna()
    st.write(new_df)
    st.download_button(
        label="Download New CSV File",
        data = new_df.to_csv(index=False),
        mime="text/csv",
        icon=":material/download:",
    )
