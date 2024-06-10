import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

# Setting up streamlit page configuration
st.set_page_config(page_title="Housing Affordability Analysis",
    page_icon="🏠",
    layout = 'wide')

# Read csv, convert datetime column & create affordability index column
national_df = pd.read_csv("../data/national_housing.csv")
national_df['month_date_yyyymm'] = pd.to_datetime(national_df['month_date_yyyymm'])

state_df = pd.read_csv("../data/state_housing.csv")
state_df['month_date_yyyymm'] = pd.to_datetime(state_df['month_date_yyyymm'])

def best_time_buy(metric, min, max):
    
    local_filtered_df = national_df.query('year != 2024')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f"{metric} Yearly Average"]) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.min():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'{best_month} has the Lowest Housing Prices')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -20)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()

    if abs(min_value) > abs(max_value):
        lim = abs(min_value)
    else:
        lim = abs(max_value)

    # Set the x range
    ax.set_xlim(min, max)

    return fig

def most_listing_options(metric, min, max):
    
    local_filtered_df = national_df.query('year != 2024')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f"{metric} Yearly Average"]) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.max():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'{best_month} has the Most Housing Options')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -20)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()

    if abs(min_value) > abs(max_value):
        lim = abs(min_value)
    else:
        lim = abs(max_value)

    # Set the x range
    ax.set_xlim(min, max)

    return fig

def home_size_variability(metric, min, max):
    
    local_filtered_df = national_df.query('year != 2024')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f"{metric} Yearly Average"]) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.max():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'Home size is consistent')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -20)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()

    if abs(min_value) > abs(max_value):
        lim = abs(min_value)
    else:
        lim = abs(max_value)

    # Set the x range
    ax.set_xlim(min, max)

    return fig

def median_days_on_market(metric, min, max):
    
    local_filtered_df = state_df.query('year != 2024')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f'{metric} Yearly Average']) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.max():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'Highest Median Days on Market: {best_month} at Peak')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()


    # Set the x range
    ax.set_xlim(min, max)

    return fig

def state_best_time_buy(metric, state, min, max):
    
    local_filtered_df = state_df.query('year != 2024')
    
    local_filtered_df = local_filtered_df.query(f'state == "{state}"')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f'{metric} Yearly Average']) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.min():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'{best_month} has the Lowest Housing Prices')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()


    # Set the x range
    ax.set_xlim(min, max)

    return fig

def state_most_listing_options(metric, state, min, max):
    
    local_filtered_df = state_df.query('year != 2024')
    
    local_filtered_df = local_filtered_df.query(f'state == "{state}"')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f'{metric} Yearly Average']) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.max():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'{best_month} has the Most Housing Options')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()


    # Set the x range
    ax.set_xlim(min, max)

    return fig

def state_home_size_variability(metric, state, min, max):
    
    local_filtered_df = state_df.query('year != 2024')
    
    local_filtered_df = local_filtered_df.query(f'state == "{state}"')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f'{metric} Yearly Average']) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.max():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'Home sizes are consistent year round')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()


    # Set the x range
    ax.set_xlim(min, max)

    return fig


def state_median_days_on_market(metric, state, min, max):
    
    local_filtered_df = state_df.query('year != 2024')
    
    local_filtered_df = local_filtered_df.query(f'state == "{state}"')

    local_filtered_df[f'{metric} Yearly Average'] = local_filtered_df.groupby('year')[f'{metric}'].transform('mean')

    local_filtered_df[f'{metric} Deviation'] = ((local_filtered_df[f'{metric}'] - local_filtered_df[f'{metric} Yearly Average']) / local_filtered_df[f'{metric} Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')[f'{metric} Deviation'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = f'{metric} Deviation'

    # Define x and y
    x = agg_value[f'{metric}']
    y = agg_value['month']

    # Round x values
    x = round(x,1)

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, month, value in zip(bars, y, x):
        if value == x.max():
            best_month = month
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'Highest Median Days on Market: {best_month} at Peak')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()


    # Set the x range
    ax.set_xlim(min, max)

    return fig


def interactive_metric_over_time(metric, state):
    local_filtered_df = state_df.query(f"state == '{state}'")

    # Create the interactive plot
    fig = px.line(local_filtered_df, 
                  x='month_date_yyyymm', 
                  y=f'{metric}', 
                  title=f'{metric} Over Time in {state}', 
                  labels={'month_date_yyyymm': 'Month', f'{metric}': f'{metric}'},
                  line_shape='linear')

    # Update line color
    fig.update_traces(line=dict(color='grey'))

    # Customize layout
    fig.update_layout(
        plot_bgcolor='white',  # Set background color to white
        xaxis=dict(
            showgrid=False,  # Remove x-axis gridlines
            showline=True,  # Show x-axis line
            linecolor='grey'  # Set x-axis line color to black
        ),
        yaxis=dict(
            showgrid=False,  # Remove y-axis gridlines
            showline=True,  # Show y-axis line
            linecolor='grey',  # Set y-axis line color to black
        ),
        hoverlabel = dict(
            bgcolor = 'white', # Set background color for hover box
            font_size = 12, # Set font size for hover box
            font_family = "Arial" # Set font family
        )
    )

    # Show the plot
    return fig

###Content of the actual page
###
###


# Create tabs
tab1, tab2 = st.tabs(["National View","State View"])

# Create tab for national view
with tab1:
    st.header("National View")
    # Create columns
    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(best_time_buy('Median Listing Price', -10, 10))
        st.pyplot(home_size_variability('Median Square Feet', -10, 10))

    with col2:
        st.pyplot(most_listing_options('active_listing_count', -10, 10))

    st.write("# <span style='color: red;'>Note: The Median Days on Market plot has a different scale for the x-axis</span>", unsafe_allow_html=True)    
    st.pyplot(median_days_on_market('median_days_on_market', -45, 45))

with tab2:
    st.header("State View")
    state = st.selectbox('Select State:', state_df['state'].unique())

    # Create tabs within the State View Tab
    s_tab1, s_tab2 = st.tabs(["Seasonality View","State Metrics"])

    # State Seasonality Tab
    with s_tab1:

        # Create columns
        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(state_best_time_buy("Median Listing Price", state, -20, 20))
            st.pyplot(state_home_size_variability("Median Square Feet", state, -20, 20))
        
        with col2:
            st.pyplot(state_most_listing_options("active_listing_count", state, -20, 20))

        st.write("# <span style='color: red;'>Note: The Median Days on Market plot has a different scale for the x-axis</span>", unsafe_allow_html=True)
        st.pyplot(state_median_days_on_market("median_days_on_market", state, -45, 45))


    with s_tab2:

        # Create columns
        col1, col2 = st.columns(2)

        with col1:
            
            st.plotly_chart(interactive_metric_over_time("Median Listing Price", state))
            st.plotly_chart(interactive_metric_over_time("Median Square Feet", state))
            st.plotly_chart(interactive_metric_over_time("Income to Home Price Ratio", state))
        
        with col2:

            st.plotly_chart(interactive_metric_over_time("Median Listing Price per Square Foot", state))
            st.plotly_chart(interactive_metric_over_time("active_listing_count", state))
            st.plotly_chart(interactive_metric_over_time("median_days_on_market", state))            
