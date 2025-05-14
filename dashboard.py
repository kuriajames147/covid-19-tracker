import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page config
st.set_page_config(page_title="COVID-19 Global Tracker", layout="wide")
st.title("🌍 COVID-19 Global Data Tracker")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('owid-covid-data.csv', parse_dates=['date'])
    df = df[['date', 'location', 'total_cases', 'new_cases', 'total_deaths',
             'new_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']]
    df.dropna(subset=['location', 'date'], inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df

df = load_data()

# Sidebar - Country selector
st.sidebar.header("Filter")
countries = ['Kenya', 'India', 'United States']
selected_country = st.sidebar.selectbox("Select a Country", countries)

# Filter data by country
country_df = df[df['location'] == selected_country]

# Death rate calculation
country_df['death_rate'] = country_df['total_deaths'] / country_df['total_cases']

# ------------------ Layout ------------------ #
col1, col2 = st.columns(2)

# Total Cases Over Time
with col1:
    st.subheader(f"📈 Total COVID-19 Cases in {selected_country}")
    fig, ax = plt.subplots()
    sns.lineplot(data=country_df, x='date', y='total_cases', ax=ax)
    ax.set_ylabel("Total Cases")
    st.pyplot(fig)

# Total Deaths Over Time
with col2:
    st.subheader(f"☠️ Total COVID-19 Deaths in {selected_country}")
    fig, ax = plt.subplots()
    sns.lineplot(data=country_df, x='date', y='total_deaths', ax=ax, color='red')
    ax.set_ylabel("Total Deaths")
    st.pyplot(fig)

# Vaccination Progress
st.subheader(f"💉 Vaccination Progress in {selected_country}")
fig, ax = plt.subplots()
sns.lineplot(data=country_df, x='date', y='total_vaccinations', ax=ax, color='green')
ax.set_ylabel("Total Vaccinations")
st.pyplot(fig)

# Death Rate
st.subheader(f"⚰️ Death Rate in {selected_country}")
fig, ax = plt.subplots()
sns.lineplot(data=country_df, x='date', y='death_rate', ax=ax, color='black')
ax.set_ylabel("Death Rate")
st.pyplot(fig)

# Summary Insights
st.markdown("### 🧠 Key Insights")
if selected_country == "United States":
    st.markdown("- 🇺🇸 USA had the highest total cases and deaths throughout the pandemic.")
elif selected_country == "India":
    st.markdown("- 🇮🇳 India experienced sharp waves in 2021 with a fast vaccination rollout.")
elif selected_country == "Kenya":
    st.markdown("- 🇰🇪 Kenya had relatively lower cases and deaths, but slow vaccination progress.")

# Footer
st.markdown("---")
st.markdown("🔬 Data source: [Our World in Data](https://ourworldindata.org/coronavirus)")
