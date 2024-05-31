import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Setting up streamlit page configuration
st.set_page_config(layout = 'centered')

# Read csv, convert datetime column & create affordability index column
national_df = pd.read_csv("../data/national_housing.csv")
national_df['month_date_yyyymm'] = pd.to_datetime(national_df['month_date_yyyymm'])

state_df = pd.read_csv("../data/state_housing.csv")
state_df['month_date_yyyymm'] = pd.to_datetime(state_df['month_date_yyyymm'])

# Function that displays a plot showing the best month to buy a house
def best_time_buy(metric):
    
    local_filtered_df = national_df.query('year != 2024')

    local_filtered_df['Median Listing Price Yearly Average'] = local_filtered_df.groupby('year')['Median Listing Price'].transform('mean')

    local_filtered_df['Median Listing Price Percentage of Average'] = (local_filtered_df['Median Listing Price'] / local_filtered_df['Median Listing Price Yearly Average']) * 100

    # Make months a categorical variable with an order
    month_order = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    local_filtered_df['month'] = pd.Categorical(local_filtered_df['month'], categories = month_order, ordered = True)

    agg_value = local_filtered_df.groupby('month')['Median Listing Price Percentage of Average'].mean().reset_index()

    agg_value = agg_value.sort_values('month', ascending = False)

    metric = 'Median Listing Price Percentage of Average'

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
            bar.set_color('blue')

    # Set the title and axes
    ax.set_xlabel(f'{metric}')
    ax.set_title('January is the Best Time to Buy A House')

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Label the bar numbers
    ax.bar_label(bars, color = 'white', padding = -50)

    # Calculate the max of the metric and round
    min_value = x.min()

    max_value = x.max()


    # Set the x range
    ax.set_xlim(min_value - 10, max_value + 10)

    return fig

st.pyplot(best_time_buy('Median Listing Price'))
