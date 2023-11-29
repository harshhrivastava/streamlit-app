import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# The steps for creating the visualization website is as follows:


# 1. Configure the project
# The following will set the page configurations
st.set_page_config(
    page_title = "Data Visualization App",
    page_icon = "⚗️",
    layout = "wide",
)



# 2. Load the data
# Read data from the analysis.ipynb file
@st.cache_data()

def load_data():
    url = "data/data.csv"
    data = pd.read_csv(url, parse_dates=['release_date'])
    data.drop(columns=['id'], inplace=True)
    return data



# 3. Build the interface

# The following is used to create a title which will be displayed
st.title("Data Science App")

# The following will load the data as well as
# show a spinner until the data has been loaded
with st.spinner("Loading Data..."):
    data = load_data()

# If we want to show the data, we can use the dataframe function of streamlit
st.header("Dataset")
st.info("Raw Data in DataFrame")
st.dataframe(data, use_container_width=True)

# Here we list the columns of the dataset
st.success("Column information of the dataset.")
columns = data.columns.tolist()
st.write(f"Columns of the above dataset are {', '.join(columns)}.")

# If we want, we can uncomment the following to hide the header and the footer
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden; display:none;}
#             footer {visibility: hidden; display:none;}
#             header {visibility: hidden; display:none;}
#             .block-container {padding:8rem 8rem;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



# 4. Add Graphs and Widgets

st.header("Data Visualization")
graph_options = ['Bar Chart', 'Line Chart', 'Area Chart']
subset = data.sort_values(by='popularity', ascending=False).head(10)
column1, column2 = st.columns(2)

selected_option1 = column1.selectbox("Select Chart Type For Popularity", graph_options)
if selected_option1 == graph_options[0]:
    fig = px.bar(data_frame=subset, x='title', y='popularity')
elif selected_option1 == graph_options[1]:
    fig = px.line(data_frame=subset, x='title', y='popularity')
else:
    fig = px.area(data_frame=subset, x='title', y='popularity')
column1.plotly_chart(figure_or_data=fig)

selected_option2 = column2.selectbox("Select Chart Type For Vote Count", graph_options)
if selected_option2 == graph_options[0]:
    fig = px.bar(data_frame=subset, x='title', y='vote_count')
elif selected_option2 == graph_options[1]:
    fig = px.line(data_frame=subset, x='title', y='vote_count')
else:
    fig = px.area(data_frame=subset, x='title', y='vote_count')
column2.plotly_chart(figure_or_data=fig)

tab1, tab2 = st.tabs(['Bivariate', 'Trivariate'])
num_cols = data.select_dtypes(include='number').columns.tolist()
    
with tab1:
    c1, c2 = tab1.columns(2)
    col1 = c1.radio("1st Column", num_cols)
    col2 = c2.radio("2nd Column", num_cols)
    fig = px.scatter(data, x=col1, y=col2, title=f'{col1} vs {col2}')
    st.plotly_chart(fig, use_container_width=True)
    
with tab2:
    c1, c2, c3 = tab2.columns(3)
    col1 = c1.radio("1st Column for 3d Plot", num_cols)
    col2 = c2.radio("2nd Column for 3d Plot", num_cols)
    col3 = c3.radio("3rd Column for 3d Plot", num_cols)
    fig = px.scatter_3d(data, x=col1, y=col2, z=col3, title=f'{col1} vs {col2} vs {col3}', height=1000)
    st.plotly_chart(fig, use_container_width=True)



# 5. Adjust the layouts



# To run the app, open terminal and run: streamlit run main.py