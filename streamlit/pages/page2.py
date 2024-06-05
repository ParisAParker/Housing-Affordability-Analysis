import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Setting up streamlit page configuration
st.set_page_config(layout = 'wide')

# Read csv, convert datetime column & create affordability index column
national_df = pd.read_csv("../data/national_housing.csv")
national_df['month_date_yyyymm'] = pd.to_datetime(national_df['month_date_yyyymm'])

state_df = pd.read_csv("../data/state_housing.csv")
state_df['month_date_yyyymm'] = pd.to_datetime(state_df['month_date_yyyymm'])

def best_time_buy(metric):
    
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
    ax.set_xlim(-(lim), lim)

    return fig

def most_listing_options(metric):
    
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
    ax.set_xlim(-(lim), lim)

    return fig

def home_size_variability(metric):
    
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
    ax.set_xlim(-(lim), lim)

    return fig

def state_best_time_buy(metric, state):
    
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
    ax.set_title(f'{best_month} is the Best Time to Buy A House')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()


    # Set the x range
    ax.set_xlim(min_value, max_value)

    return fig

# Create tabs
tab1, tab2 = st.tabs(["National View","State View"])

# Create tab for national view
with tab1:

    # Create columns
    col1, col2 = st.columns(2)

    st.header("National View")
    with col1:
        st.pyplot(best_time_buy('Median Listing Price'))
        st.pyplot(home_size_variability('Median Square Feet'))

    with col2:
        st.pyplot(most_listing_options('total_listing_count'))

with tab2:
    st.header("State View")
    state = st.selectbox('Select State:', state_df['state'].unique())
    st.pyplot(state_best_time_buy("Median Listing Price", state))
