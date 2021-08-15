import streamlit as st
import plotly.express as px
from sklearn.datasets import load_iris


# Get the data
df = load_iris(as_frame=True).frame
# Rename columns
df = df.rename(columns=lambda x: '_'.join(x.split()[:2]))


### Build the sidebar ###
# Class selector
iris_type = st.sidebar.radio('Choose iris type', [0, 1, 2])
# Chart type selector
chart_type = st.sidebar.radio('Choose chart type', ['scatterplot', 'boxplot'])
# Variable selector
variable = st.sidebar.radio('Choose variable', ['sepal', 'petal'])

### Add the app title
st.title('Iris Dataset Visualization')


### Visualize ###
df = df.query('target==@iris_type')

if chart_type == 'scatterplot':
    fig = px.scatter(data_frame=df, x=variable+'_length', y=variable+'_width')
else:
    fig = px.box(data_frame=df, x='target', y=variable+'_length')

st.plotly_chart(fig)
