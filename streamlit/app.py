import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Setting up streamlit page configuration
st.set_page_config(layout = 'wide')

# Read csv, convert datetime column & create affordability index column
national_housing_df = pd.read_csv("../data/national_housing.csv")
national_housing_df['month_date_yyyymm'] = pd.to_datetime(national_housing_df['month_date_yyyymm'])

state_housing_df = pd.read_csv("../data/state_housing.csv")
state_housing_df['month_date_yyyymm'] = pd.to_datetime(state_housing_df['month_date_yyyymm'])

mlp_increase = pd.read_csv('../data/mlp_percent_increase.csv')

# Add metric option to sidebar
metric_options = ['Median Listing Price','Median Square Feet','Median Listing Price per Square Foot','Median Income','Income to Home Price Ratio']
metric = st.sidebar.selectbox("Select Metric", metric_options)

# Remove all null values for the specific metric
state_housing_df = state_housing_df.dropna(subset = f"{metric}")

# Grab the earliest and latest date of the dataframe
start_date = state_housing_df['month_date_yyyymm'].min().to_pydatetime()
end_date = state_housing_df['month_date_yyyymm'].max().to_pydatetime()

# Making sure slider only uses first day of the month
date_range = pd.date_range(start = start_date,
                           end = end_date,
                           freq = 'MS').to_list()

# Create a date slider for the page
date_slider = st.sidebar.select_slider(
    "Select date range",
    options = date_range,
    value = (date_range[0], date_range[-1]),
    format_func = lambda x: x.strftime("%b %Y"))

# Filter data based on date metrics
filtered_df = state_housing_df[(state_housing_df['month_date_yyyymm'] >= date_slider[0]) & (state_housing_df['month_date_yyyymm'] <= date_slider[1])]
latest_year = date_slider[1].to_pydatetime().year
latest_month = date_slider[1].to_pydatetime().strftime('%B')

filtered_national_df = national_housing_df[(national_housing_df['month_date_yyyymm'] >= date_slider[0]) & (national_housing_df['month_date_yyyymm'] <= date_slider[1])]

# Defining functions
# This function takes in the selected states and show national argument & returns a line plot of the states median listing price over the years
# & the united states line if checked true
def mlp_pricing_trend(metric, year, month, states, show_national):

    # Defining top 10 states and bottom 10 states
    top_10_states = filtered_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()\
    [['month_date_yyyymm','state',f'{metric}']].head(10)

    top_10_states = top_10_states['state'].unique()

    bottom_10_states = filtered_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()\
    [['month_date_yyyymm','state',f'{metric}']].tail(10)

    bottom_10_states = bottom_10_states['state'].unique()

    # Subsetting dataframe for selected states
    housing_for_state = filtered_df[filtered_df['state'].isin(states)]

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
        ax1.plot(filtered_national_df['month_date_yyyymm'], filtered_national_df[f'{metric}'], color = 'black')
        
        ax1.text(filtered_national_df['month_date_yyyymm'].iloc[0],
                filtered_national_df[f'{metric}'].iloc[0],
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

    local_filtered_df = filtered_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()

    local_filtered_df = local_filtered_df[['month_date_yyyymm','state',f'{metric}']]
    top_10_states = local_filtered_df.head(10)
    top_10_states = top_10_states.sort_values(by = f"{metric}", ascending = True)

    # Define x and y
    x = top_10_states[f'{metric}']
    y = top_10_states['state']

    # Create horizontal bar chart for top 10 states
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, state in zip(bars, y):
        if state in states:
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'{latest_month} {latest_year}: Top 10 States by {metric}')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric
    max_value = filtered_df[f"{metric}"].max()

    # Set the x range
    ax.set_xlim(0,(max_value))

    return fig

# Function that takes in metric, month, and year and returns the bottom 10 states for that specific metric in the given timeframe
def bottom_10_mlp(metric,month,year):

    local_filtered_df = filtered_df.query(f"year == {year} and month == '{month}'")\
    .sort_values(f"{metric}", ascending = False).reset_index()

    local_filtered_df = local_filtered_df[['month_date_yyyymm','state',f'{metric}']]
    bottom_10_states = local_filtered_df.tail(10)
    bottom_10_states = bottom_10_states.sort_values(by = f"{metric}", ascending = True)

    # Define x and y
    x = bottom_10_states[f'{metric}']
    y = bottom_10_states['state']

    # Create horizontal bar chart
    fig, ax = plt.subplots()
    bars = ax.barh(y, x, color = 'grey')

    # Highlight a specific state
    for bar, state in zip(bars, y):
        if state in states:
            bar.set_color('red')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title(f'{latest_month} {latest_year}: Lowest 10 States by {metric}')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric
    max_value = filtered_df[f"{metric}"].max()

    # Set the x range
    ax.set_xlim(0,(max_value))

    return fig

# Function that shows how much higher (in %) the max value is than the national value
def percent_higher_lower(metric, month, year, method):
    # Filter data for the specific month and year
    local_filtered_df = filtered_df.query(f"month == '{month}' and year =={year}")
    
    # Are we comparing the highest or lowest state?
    if method == 'highest':
        
        # Find the row that has the highest value for the specific metric
        metric_row = local_filtered_df.sort_values(by = f'{metric}', ascending = False).iloc[0]
    elif method == 'lowest':
        
        
        # Find the row that has the lowest value for the specific metric
        metric_row = local_filtered_df.sort_values(by = f'{metric}', ascending = True).iloc[0]
    
    else:
        raise ValueError("No correct method type highest or lowest")
        
    # Find the state and metric value of the row
    metric_value = metric_row[f"{metric}"]
    state = metric_row['state']

    # Filter data for national dataframe
    national_local_filtered_df = filtered_national_df.query(f"month == '{month}' and year =={year}")

    # Find the metric value at the national level
    national_metric_value = national_local_filtered_df.iloc[0][f'{metric}']

    # Find how much higher/lower the metric value is than the national value
    percent_change = round(((metric_value - national_metric_value) / national_metric_value) * 100,0).astype(int)

    # If the value is a decimal round to 2 places if not round and make an integer
    if metric_value < 1:
        metric_value = round(metric_value,2)
        metric_value = f"{metric_value:.2f}"

    else:
        metric_value = int(round(metric_value,0))

    return metric_value, state, int(percent_change)

def national_comparison(metric, month, year):
    # Find the national value of the metric
    national_value = filtered_national_df.query(f"year == {year} and month == '{month}'").iloc[0][f"{metric}"]

    # Filter the dataframe for the month and year
    local_filtered_df = filtered_df.query(f"year == {year} and month == '{month}'")

    # Find how many states are above the national value
    states_num_above = len(local_filtered_df[local_filtered_df[f'{metric}'] >= national_value])

    # Find what percentage of all states are above the national value
    percent_states_above = (states_num_above / len(local_filtered_df)) * 100
    percent_states_above = int(round(percent_states_above,0))

    # If the value is a decimal round to 2 places if not round and make an integer
    if national_value < 1:
        national_value = round(national_value,2)
        national_value = f"{national_value:.2f}"

    else:
        national_value = int(round(national_value,0))

    return states_num_above, percent_states_above, national_value

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

month = latest_month
year = latest_year

# Create cols
left_column, right_column = st.columns((2,1))

with left_column:
    #st.markdown

    # Create 4 equal columns withing the left section
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        national_value = national_comparison(metric, month, year)[2]

        st.metric(label = "National Value",
                  value = national_value)

    with col2:
        percent_metric_list = percent_higher_lower(metric, month, year, 'highest')
        metric_value = percent_metric_list[0]
        metric_state = percent_metric_list[1]
        metric_percent = percent_metric_list[2]

        st.metric(label = f'{metric_state}',
              value = metric_value,
              delta=int(metric_percent))

    with col3:
        percent_metric_list = percent_higher_lower(metric, month, year, 'lowest')
        metric_value = percent_metric_list[0]
        metric_state = percent_metric_list[1]
        metric_percent = percent_metric_list[2]

        st.metric(label = f'{metric_state}',
              value = metric_value,
              delta=int(metric_percent))
    
    with col4:
        national_comparison_list = national_comparison(metric, month, year)
        num_states = national_comparison_list[0]
        percent_states = national_comparison_list[1]

        st.metric(label = "Number of States Above National Value",
                  value = num_states,
                  delta = percent_states)
    

    states = st.multiselect('Select States:', filtered_df['state'].unique(), default = ['Tennessee', 'Hawaii','Ohio'])
    show_national = st.checkbox('Show United States', value = False)

    st.pyplot(mlp_pricing_trend(metric, year, month, states, show_national))

with right_column:

    with st.container():
        st.pyplot(top_10_mlp(metric,month,year))
    
    with st.container():
        st.pyplot(bottom_10_mlp(metric,month,year))