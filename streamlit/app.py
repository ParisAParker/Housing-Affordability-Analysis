import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read csv, convert datetime column & create affordability index column
national_housing_df = pd.read_csv("../data/national_housing.csv")
national_housing_df['month_date_yyyymm'] = pd.to_datetime(national_housing_df['month_date_yyyymm'])
national_housing_df['affordability_index'] = national_housing_df['median_income'] / national_housing_df['median_listing_price']

state_housing_df = pd.read_csv("../data/state_housing.csv")
state_housing_df['month_date_yyyymm'] = pd.to_datetime(state_housing_df['month_date_yyyymm'])
state_housing_df['affordability_index'] = state_housing_df['Households'] / state_housing_df['median_listing_price']

mlp_increase = pd.read_csv('../data/mlp_percent_increase.csv')

# Setting up page configuration
st.set_page_config(layout = 'wide')

# Defining functions
# This function takes in the selected states and show national argument & returns a line plot of the states median listing price over the years
# & the united states line if checked true
def mlp_pricing_trend(states, show_national):
    
    # Define the metric used
    metric = 'median_listing_price'
    year = 2022
    month = 'December'

    # Defining top 10 states and bottom 10 states
    top_10_states = state_housing_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()\
    [['month_date_yyyymm','state',f'{metric}']].head(10)

    top_10_states = top_10_states['state'].unique()

    bottom_10_states = state_housing_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()\
    [['month_date_yyyymm','state',f'{metric}']].tail(10)

    bottom_10_states = bottom_10_states['state'].unique()

    # Subsetting dataframe for selected states
    housing_for_state = state_housing_df[state_housing_df['state'].isin(states)]

    # Create line graph for median listing price over several years
    fig, ax1 = plt.subplots()

    for state in states:
        # Subset dataset for that state
        state_data = housing_for_state.query(f"state == '{state}'")
        
        if state in top_10_states:
            # Plot line graph 
            ax1.plot(state_data['month_date_yyyymm'], state_data[f'{metric}'], color = 'blue')
            
            # Label the end of each line
            ax1.text(state_data['month_date_yyyymm'].iloc[0],
                state_data[f'{metric}'].iloc[0],
                state,
                fontsize = 9,
                ha = 'left',
                color = 'blue',
                fontweight = 'bold')
        
        elif state in bottom_10_states:
            # Plot line graph 
            ax1.plot(state_data['month_date_yyyymm'], state_data[f'{metric}'], color = 'red')

            # Label the end of each line
            ax1.text(state_data['month_date_yyyymm'].iloc[0],
            state_data[f'{metric}'].iloc[0],
            state,
            fontsize = 9,
            ha = 'left',
            color = 'red',
            fontweight = 'bold')
        
        else:
            # Plot line graph 
            ax1.plot(state_data['month_date_yyyymm'], state_data[f'{metric}'], color = 'grey')

            # Label the end of each line
            ax1.text(state_data['month_date_yyyymm'].iloc[0],
            state_data[f'{metric}'].iloc[0],
            state,
            fontsize = 9,
            ha = 'left',
            color = 'grey',
            fontweight = 'bold')   
        
    # Add a line for the entire united states
    if show_national == True:
        ax1.plot(national_housing_df['month_date_yyyymm'], national_housing_df[f'{metric}'], color = 'black')
        
        ax1.text(national_housing_df['month_date_yyyymm'].iloc[0],
                national_housing_df[f'{metric}'].iloc[0],
                'United States',
                fontsize = 9,
                ha = 'left',
                color = 'black',
                fontweight = 'bold')
        
    # Set the title and axes
    ax1.set_ylabel(f'{metric}')
    ax1.set_title(f'{metric} Over Time', loc = 'left')

    # Remove the spines
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Define y range
    ax1.set_ylim(bottom = 0)

    # Return the figure
    return(fig)

# Function that takes in metric, month, and year and returns the top 10 states for that specific metric in the given timeframe
def top_10_mlp(metric,month,year):

    filtered_df = state_housing_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()

    filtered_df = filtered_df[['month_date_yyyymm','state',f'{metric}']]
    top_10_states = filtered_df.head(10)
    top_10_states = top_10_states.sort_values(by = f"{metric}", ascending = True)

    # Define x and y
    x = top_10_states[f'{metric}']
    y = top_10_states['state']

    # Create horizontal bar chart for national affordability index by month
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, state in zip(bars, y):
        if state in states:
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'Top 10 States by {metric} ')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Set the x range
    ax.set_xlim((0,900000))

    return fig

# Function that takes in metric, month, and year and returns the bottom 10 states for that specific metric in the given timeframe
def bottom_10_mlp(metric,month,year):

    filtered_df = state_housing_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()

    filtered_df = filtered_df[['month_date_yyyymm','state',f'{metric}']]
    bottom_10_states = filtered_df.tail(10)
    bottom_10_states = bottom_10_states.sort_values(by = f"{metric}", ascending = True)

    # Define x and y
    x = bottom_10_states[f'{metric}']
    y = bottom_10_states['state']

    # Create horizontal bar chart for national affordability index by month
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, state in zip(bars, y):
        if state in states:
            bar.set_color('red')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'Bottom 10 States by {metric} ')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Set x range
    ax.set_xlim((0,900000))

    return fig

# Function that takes in states and returns plot of their percentage increase in median listing price
def percentage_increase_plot(states):   
    # Subset data for the selected states
    filtered_df = mlp_increase[mlp_increase['state'].isin(states)]\
    .sort_values(by = 'percentage_increase', ascending = True)

    # Define x and y for the plot
    x = filtered_df['percentage_increase']
    y = filtered_df['state']

    # Create horizontal bar chart for national affordability index by month
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    return fig

# Create cols
top_left_column, top_right_column = st.columns((2,1))
bottom_left_column, bottom_right_column = st.columns(2)

with top_left_column:

    states = st.multiselect('Select States:', state_housing_df['state'].unique(), default = 'Tennessee')
    show_national = st.checkbox('Show United States', value = True)

    st.pyplot(mlp_pricing_trend(states,show_national))

with top_right_column:

    metric = 'median_listing_price'
    month = 'December'
    year = 2022

    with st.container():
        st.pyplot(top_10_mlp(metric,month,year))
    
    with st.container():
       st.pyplot(bottom_10_mlp(metric,month,year))

# Subset dataframe to only show selected states
mlp_increase = mlp_increase[mlp_increase['state'].isin(states)]

st.dataframe(mlp_increase)
