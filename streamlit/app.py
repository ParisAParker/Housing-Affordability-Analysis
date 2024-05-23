import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read csv, convert datetime column & create affordability index column
national_housing_df = pd.read_csv("../data/national_housing.csv")
national_housing_df['month_date_yyyymm'] = pd.to_datetime(national_housing_df['month_date_yyyymm'])
national_housing_df['affordability_index'] = national_housing_df['median_income'] / national_housing_df['median_listing_price']

housing_df = pd.read_csv("../data/state_housing.csv")
housing_df['month_date_yyyymm'] = pd.to_datetime(housing_df['month_date_yyyymm'])
housing_df['affordability_index'] = housing_df['Households'] / housing_df['median_listing_price']

# Create line graph for national affordability index over several years
fig, ax = plt.subplots()
ax.plot(national_housing_df['month_date_yyyymm'], national_housing_df['affordability_index'])

# Set the title and axes
ax.set_xlabel('Year')
ax.set_ylabel('Income to Home Price Ratio')
ax.set_title('Income to Home Price Ratio Over Time (National Level)')


st.pyplot(fig)

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
selected_metric = st.selectbox('Select Metric', ['median_listing_price',
 'active_listing_count',
 'median_days_on_market',
 'new_listing_count',
 'price_increased_count',
 'price_reduced_count',
 'pending_listing_count',
 'median_listing_price_per_square_foot',
 'median_square_feet',
 'average_listing_price',
 'total_listing_count'])

selected_state = st.selectbox('Select State', housing_df['state'].unique())

housing_for_state = housing_df.query(f"state == '{selected_state}'")

# Create line graph for national affordability index over several years
fig, ax = plt.subplots()
ax.plot(housing_for_state['month_date_yyyymm'], housing_for_state[f'{selected_metric}'])

# Set the title and axes
ax.set_xlabel('Year')
ax.set_ylabel('Income to Home Price Ratio')
ax.set_title(f'Income to Home Price Ratio Over Time for {selected_state}')

st.pyplot(fig)