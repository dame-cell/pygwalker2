import pandas as pd
import streamlit as st
import pygwalker as pyg

# Set page configuration
st.set_page_config(
    page_title="PyGWalker Demo",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load Data
@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.xlsx') or file.name.endswith('.xls'):
        df = pd.read_excel(file)
    else:
        raise ValueError("Invalid file format. Please upload a CSV or Excel file.")
    return df

# Set title and subtitle
st.title('PyGWalker Demo App 🦉 ')


# File Uploader
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    # Process the uploaded file
    try:
        df = load_data(uploaded_file)
        pyg.walk(df , env="Streamlit" , dark="light")  # Display the dataframe
    except Exception as e:
        st.error(str(e))