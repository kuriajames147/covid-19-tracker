#  COVID-19 Global Data Tracker

This project analyzes and visualizes global COVID-19 data using Python. It provides both:

1.  A **Jupyter Notebook** for in-depth step-by-step data analysis, exploration, and insights.
2. A **Streamlit Web App** for interactive data visualization and user-friendly exploration.

---

## Project Structure

covid_global_tracker/
│
├── covid_global_tracker.ipynb # Jupyter Notebook - detailed analysis & visualizations
├── covid_dashboard_app.py # Streamlit App - interactive COVID-19 dashboard
├── owid-covid-data.csv # Source dataset from Our World in Data
└── README.md # Project description and usage guide

yaml
Copy
Edit

---

## Jupyter Notebook: `covid_global_tracker.ipynb`

This file walks through:

- Data loading and cleaning
- Data exploration and column selection
-  Visual analysis of total cases, deaths, and vaccinations
-  Death rate computation
-  Key insights and commentary

Use this notebook for **understanding the data, methodology, and analysis process**.

---

## Streamlit Dashboard: `covid_dashboard_app.py`

This script creates an **interactive dashboard** using [Streamlit](https://streamlit.io/). Key features include:

- Country selector (Kenya, India, United States)
-  Total cases, deaths, and vaccinations visualized over time
- Death rate trends
-  Summary insights per country
-  Easy-to-use interface for non-technical users

### To run the app:

```bash
streamlit run covid_dashboard_app.py
Make sure owid-covid-data.csv is in the same directory.

Data Source
Our World in Data - COVID-19 Dataset

Requirements
Install dependencies using:

bash
Copy
Edit
pip install pandas matplotlib seaborn streamlit
 Author
james Harrison Kuria

Feel free to reach out or contribute!
