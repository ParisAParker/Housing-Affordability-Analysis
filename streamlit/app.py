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

# Shows the affordability index over the years for the selected state
metric = st.selectbox('Select Metric', ['median_listing_price',
'active_listing_count',
'median_days_on_market',
'new_listing_count',
'price_increased_count',
'price_reduced_count',
'pending_listing_count',
'median_listing_price_per_square_foot',
'median_square_feet',
'average_listing_price',
'total_listing_count',
'affordability_index'])

states = st.multiselect('Select States:', state_housing_df['state'].unique(), default = 'Tennessee')

show_national = st.checkbox('Show United States', value = True)

# Subsetting dataframe for selected states
housing_for_state = state_housing_df[state_housing_df['state'].isin(states)]

# Create line graph for national affordability index over several years
fig, ax1 = plt.subplots()

for state in states:
    # Subset dataset for that state
    state_data = housing_for_state.query(f"state == '{state}'")
    
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

st.pyplot(fig)

st.header('Column 2')

metric = 'median_listing_price'
month = 'December'
year = 2021

filtered_df = state_housing_df.query(f"year == {year} and month == '{month}'")\
.sort_values(f"{metric}", ascending = False).reset_index()

filtered_df = filtered_df[['month_date_yyyymm','state',f'{metric}']]
top_10_states = filtered_df.head(10)
top_10_states = top_10_states.sort_values(by = f"{metric}", ascending = True)

bottom_10_states = filtered_df.tail(10)

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

ax.bar_label(bars, color = 'white', padding = -50)

st.pyplot(fig)