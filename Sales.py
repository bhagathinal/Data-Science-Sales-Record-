import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/HINAL/Internship/Sales Record/Sales.csv")

# Sidebar for filtering options
st.sidebar.title("Filter Data")
selected_region = st.sidebar.selectbox("Select Region", df['Region'].unique())
selected_country = st.sidebar.selectbox("Select Country", df[df['Region'] == selected_region]['Country'].unique())
selected_item_type = st.sidebar.selectbox("Select Item Type", df['Item Type'].unique())

# Filter data based on user selections
filtered_data = df[(df['Region'] == selected_region) & (df['Country'] == selected_country) & (df['Item Type'] == selected_item_type)]


# Distribution of numerical columns
st.write("## Numerical Column Distributions")
numeric_columns = ['Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']
selected_numeric_column = st.selectbox("Select Numeric Column", numeric_columns)
st.bar_chart(filtered_data[selected_numeric_column])

# Explore relationships between columns
st.write("## Relationships Between Columns")
selected_x_column = st.selectbox("Select X Column", df.columns)
selected_y_column = st.selectbox("Select Y Column", df.columns)
st.scatter_chart(filtered_data, x=selected_x_column, y=selected_y_column)

# Geographical analysis using a map
if 'Country' in df.columns:
    st.write("## Geographic Analysis - Sales by Country")
    country_sales = df.groupby('Country').agg({'Total Revenue': 'sum'}).reset_index()
    fig = px.choropleth(country_sales, locations='Country', locationmode='country names', color='Total Revenue',
                        title='Sales by Country', color_continuous_scale='Viridis')
    st.plotly_chart(fig)
else:
    st.warning("Geographic information not available in the dataset.")
