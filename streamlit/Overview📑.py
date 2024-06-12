import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Housing Affordability Analysis",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Title of the dashboard
st.title("Housing Affordability Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")

section = st.sidebar.selectbox("Go to section:", 
                               ["🏠 Executive Summary", 
                                "📄 Motivation & Data Questions", 
                                "📊 Data Sources",  
                                "📈 Results",
                                "🛑 Limitations", 
                                "📄 Conclusion",
                                "🛠 Future Directions"])

# Define the content for each section
def show_executive_summary():
    st.header("Executive Summary")
    st.write("""
    This project explores how housing affordability has changed over the years. 
    Using data from median income statistics, Realtor housing metrics, and potentially other sources, 
    the project aims to provide insights into housing affordability trends. 
    The primary motivation for this research is to assist prospective homebuyers, like myself, 
    in understanding the evolving landscape of housing affordability.
    """)

def show_motivation_and_data_questions():
    st.header("Motivation & Data Questions")
    st.write("""
    As I prepare to purchase my first home or apartment, I want to understand the changes in housing affordability. 
    This project seeks to answer questions such as:
    
    - How has housing affordability changed over the years?
    - Which areas have had the highest/lowest percentage increases in housing prices?
    - Are there specific times when buying a house is easier?
    """)

def show_data_sources():
    st.header("Data Sources")
    st.write("""
    The data for this project comes from various sources, including:
    
    - Median income data from Census Bureau
    - Housing metrics from Realtor.com
    """)

def show_results():
    st.header("Results")
    st.write("""
    ### Key Findings

    **1. Median Income to Median Home Price Ratio Trends:**
    - The Median Income to Median Home Price Ratio has been decreasing over the years.
    - Ohio has the highest ratio, indicating better affordability.
    - Montana has the lowest ratio, indicating lower affordability.

    **2. Seasonality in Home Pricing:**
    - Home prices exhibit seasonality with January historically having the lowest prices.
    - Summer months, particularly June through August, tend to have the highest home prices.

    **3. Housing Options Availability:**
    - There are fewer housing options available in January.
    - The number of available housing options increases during the summer months, peaking until September.

    **4. Median Listing Price Changes:**
    - New York has experienced the greatest percent increase of 125% since July 2016.
    - Hawaii has experienced the smallest percent change in median listing price of 28%.

    These insights can help prospective homebuyers to better understand market trends and make informed decisions about when and where to buy a home.
    """)

def show_limitations():
    st.header("Limitations")
    st.write("""
    While median income and median housing metrics provide valuable insights into housing affordability trends, they come with certain limitations:

    **1. Lack of Granularity:**
    - Median income and median housing metrics provide an average value, which may not capture variations within different segments of the population or housing market. For example, they may not reflect disparities in income distribution or variations in housing quality.

    **2. Ignoring Socioeconomic Factors:**
    - Median income alone may not fully represent the socioeconomic status of individuals or households. Factors such as employment stability, debt-to-income ratio, and access to credit also play a crucial role in determining housing affordability.

    **3. Omitting Local Factors:**
    - Median income and housing metrics may not account for localized factors such as zoning regulations, land availability, and regional economic conditions. These factors can significantly influence housing affordability at the local level.

    **4. Limited Scope:**
    - Using only median income and median housing metrics may overlook other dimensions of affordability, such as utility costs
    """)

def show_conclusion():
    st.header("Conclusion")
    st.write("""
    **Housing Affordability Decline:**
    Housing affordability has steadily decreased over the years, evident from the declining median income to median home price ratio annually.

    **Regional Price Trends:**

    **New York:**
    New York has witnessed the most significant increase in housing prices, with prices more than doubling (125%) over the past 8 years.

    **Hawaii:**
    In contrast, Hawaii has experienced the lowest percent increase at 28%.

    **Timing for Home Purchase:**
    Depending on your goals, it's crucial to consider the timing for purchasing a home:

    **Summer Months:**
    More housing options are typically available during the summer months, but at higher prices.
    **Off-season Months (e.g., January):**
    If you're seeking lower home prices, consider the off-season months like January, which tend to offer the lowest prices.
    """)

def show_future_directions():
    st.header("Future Directions")
    st.write("""
    In I had additional time, the following enhancements would be considered:

    **1. Incorporating Mortgage Rates Data:**
    Including mortgage rates data can provide insights into the financing aspect of home purchases and how changes in interest rates may impact housing affordability.

    **2. Integrating Population Data:**
    Population data can offer valuable demographic insights, such as population growth or decline trends, which may influence housing demand and pricing dynamics.

    **3. Adding Other Economic Indicators:**
    Exploring additional economic indicators, such as unemployment rates, GDP growth, or inflation rates, can provide a more comprehensive understanding of the macroeconomic factors influencing housing affordability.

    **4. Developing a Home Affordability Calculator:**
    Building a calculator tool where users can input their income, debt, interest rate, down payment, and type of mortgage to estimate the affordability of a home. This calculator can also provide insights into how many states an individual would be able to purchase a median priced home
             """)

# Display the selected section content
if section == "🏠 Executive Summary":
    show_executive_summary()
elif section == "📄 Motivation & Data Questions":
    show_motivation_and_data_questions()
elif section == "📊 Data Sources":
    show_data_sources()
elif section == "📈 Results":
    show_results()
elif section == "🛑 Limitations":
    show_limitations()
elif section == "📄 Conclusion":
    show_conclusion()
elif section == "🛠 Future Directions":
    show_future_directions()
