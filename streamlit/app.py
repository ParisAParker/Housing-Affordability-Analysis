import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read csv, convert datetime column & create affordability index column
national_housing_df = pd.read_csv("../data/national_housing.csv")
national_housing_df['month_date_yyyymm'] = pd.to_datetime(national_housing_df['month_date_yyyymm'])
national_housing_df['affordability_index'] = national_housing_df['median_income'] / national_housing_df['median_listing_price']

state_housing_df = pd.read_csv("../data/state_housing.csv")
state_housing_df['month_date_yyyymm'] = pd.to_datetime(state_housing_df['month_date_yyyymm'])
state_housing_df['affordability_index'] = state_housing_df['Households'] / state_housing_df['median_listing_price']

# Select the year
selected_year = st.selectbox('Select Year', national_housing_df['year'].unique())

# Create dataframe filtered for selected year
filtered_df = national_housing_df.query(f'year == {selected_year}')

# Define x and y
x = filtered_df['affordability_index']
y = filtered_df['month']

# Create horizontal bar chart for national affordability index by month
fig, ax = plt.subplots()
bars = ax.barh(y, x)

# Set the title and axes
ax.set_xlabel('Income to Home Price Ratio')
ax.set_ylabel('Month')
ax.set_title(f'Income to Home Price Ratio by Month for {selected_year}')

ax.bar_label(bars)
ax.set_xlim(0,0.35)

st.pyplot(fig)

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

states = st.multiselect('Select States:', state_housing_df['state'].unique(), default = state_housing_df['state'].unique())

show_national = st.checkbox('Show national line', value = True)

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
ax1.set_xlabel('Year')
ax1.set_ylabel(f'{metric}')
ax1.set_title(f'{metric} Over Time')

# Remove the spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Define y range
ax1.set_ylim(bottom = 0)

st.pyplot(fig)