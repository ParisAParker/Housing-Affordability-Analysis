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

def n_interactive_metric_over_time(metric):

    # Create the interactive plot
    fig = px.line(national_df, 
                  x = 'month_date_yyyymm', 
                  y = f'{metric}', 
                  title = f'{metric} for the Country', 
                  labels = {'month_date_yyyymm': 'Month', f'{metric}': f'{metric}'},
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

def pct_change_metric(metric, state):

    # Sort values by state and date for percent change calculation
    percent_change = state_df.sort_values(by = ['state', 'month_date_yyyymm'])

    percent_change = percent_change.groupby('state').agg(earliest_price = (f'{metric}','first'),
                                    latest_price = (f'{metric}','last'))\
                                    .reset_index()

    percent_change['percent_increase'] = ((percent_change['latest_price'] - percent_change['earliest_price']) / percent_change['earliest_price']) * 100

    percent_change = percent_change.sort_values('percent_increase', ascending = False).reset_index(drop = True)

    # Create column for rank of state for that metric
    percent_change = percent_change.reset_index()\
    .rename(columns = {'index': 'rank'})

    percent_change['rank'] = percent_change['rank'] + 1

    pct_increase = percent_change[percent_change['state'] == state]['percent_increase'].iloc[0]
    pct_increase = int(round(pct_increase,0))

    rank = percent_change[percent_change['state'] == state]['rank'].iloc[0]
    rank = int(rank)

    return pct_increase, rank

###Content of the actual page
###
###


# Create tabs
tab1, tab2 = st.tabs(["National View","State View"])

# Create tab for national view
with tab1:

    st.header("National View")

    # Create national tabs
    n_tab1, n_tab2 = st.tabs(["Seasonality View", "National Metrics"])

    with n_tab1:
        # Create columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.pyplot(best_time_buy('Median Listing Price', -10, 10))
            st.pyplot(home_size_variability('Median Square Feet', -10, 10))

        with col2:
            st.pyplot(most_listing_options('active_listing_count', -10, 10))

        st.write("# <span style='color: red;'>Note: The Median Days on Market plot has a different scale for the x-axis</span>", unsafe_allow_html=True)    
        st.pyplot(median_days_on_market('median_days_on_market', -45, 45))
    
    with n_tab2:
        # Create columns
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(n_interactive_metric_over_time("Median Listing Price"))
            st.plotly_chart(n_interactive_metric_over_time("Median Square Feet"))
            st.plotly_chart(n_interactive_metric_over_time("Income to Home Price Ratio"))

        with col2:
            st.plotly_chart(n_interactive_metric_over_time("Median Listing Price per Square Foot"))
            st.plotly_chart(n_interactive_metric_over_time("active_listing_count"))
            st.plotly_chart(n_interactive_metric_over_time("median_days_on_market"))      

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
        m_col1, m_col2, m_col3 = st.columns(3)
        st.write("")
        m_col4, m_col5, m_col6 = st.columns(3)
        
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

        def styled_metric(metric_label,rank_value,percent_value,background_color='#EEEEEE',text_align='center'):
            if percent_value >= 0:
                direction = 'increase'
            else:
                direction = 'decrease'

            metric_html = f""" 
            <div style="background-color: {background_color};
              padding: 0px;
                border-radius: 5px;
                  text-align: {text_align};
                  ">

            <div style="margin: 10 px auto;">
                <p style="margin: 0;">{metric_label}</p>
                    <h3 <span style="margin: 0; font-size: 26px; color:green">{percent_value}%</span> {direction} since July 2016</h3>
                        <p style="margin: 0; font-size: 20px;">Rank {rank_value} out of 51</p> 
                        </div> </div>
                            """ 
            return metric_html 
        
        with m_col1:
            metric = 'Median Listing Price'
            percent_increase = pct_change_metric(f"{metric}",state)[0]
            rank = pct_change_metric(f"{metric}",state)[1]

            metric_html = styled_metric(
                metric_label=f"{metric}",
                rank_value=rank,
                percent_value = percent_increase
            )

            st.markdown(metric_html, unsafe_allow_html=True)


        with m_col2:
            metric = 'Median Square Feet'
            percent_increase = pct_change_metric(f"{metric}",state)[0]
            rank = pct_change_metric(f"{metric}",state)[1]

            metric_html = styled_metric(
                metric_label=f"{metric}",
                rank_value=rank,
                percent_value = percent_increase
            )

            st.markdown(metric_html, unsafe_allow_html=True)
            
        with m_col3:
            metric = 'Median Listing Price per Square Foot'
            percent_increase = pct_change_metric(f"{metric}",state)[0]
            rank = pct_change_metric(f"{metric}",state)[1]

            metric_html = styled_metric(
                metric_label=f"{metric}",
                rank_value=rank,
                percent_value = percent_increase
            )

            st.markdown(metric_html, unsafe_allow_html=True)
            
        with m_col4:
            metric = 'Income to Home Price Ratio'
            percent_increase = pct_change_metric(f"{metric}",state)[0]
            rank = pct_change_metric(f"{metric}",state)[1]

            metric_html = styled_metric(
                metric_label=f"{metric}",
                rank_value=rank,
                percent_value = percent_increase
            )

            st.markdown(metric_html, unsafe_allow_html=True)
            
        with m_col5:
            metric = 'active_listing_count'
            percent_increase = pct_change_metric(f"{metric}",state)[0]
            rank = pct_change_metric(f"{metric}",state)[1]

            metric_html = styled_metric(
                metric_label=f"{metric}",
                rank_value=rank,
                percent_value = percent_increase
            )

            st.markdown(metric_html, unsafe_allow_html=True)
            
        with m_col6:
            metric = 'median_days_on_market'
            percent_increase = pct_change_metric(f"{metric}",state)[0]
            rank = pct_change_metric(f"{metric}",state)[1]

            metric_html = styled_metric(
                metric_label=f"{metric}",
                rank_value=rank,
                percent_value = percent_increase
            )

            st.markdown(metric_html, unsafe_allow_html=True)
        
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
