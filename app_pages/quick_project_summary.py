import streamlit as st


def quick_project_summary_page():
    st.title("Quick Project Summary")

    st.markdown("""
    ## Project Overview

    Lydia Doe has inherited four properties in Ames, Iowa, but is unfamiliar with the local housing market. To avoid undervaluing or overpricing these properties, she seeks insights and predictions based on historical house sale data in Ames.

    This project utilizes a public dataset to:
    - Explore what features impact house prices in Ames.
    - Predict sale prices for the inherited houses and any new house.

    ---

    ## Dataset Description

    The dataset contains housing information from Ames, Iowa, including:
    - 79 explanatory variables (house features)
    - Target variable: `SalePrice`

    The data is split into:
    - `house_prices_records.csv` — historical sale data for modeling
    - `inherited_houses.csv` — attributes for the four inherited houses

    ---

    ## Business Requirements

    **Requirement 1:** Identify which house features are most correlated with sale price.

    **Requirement 2:** Build a prediction model to estimate the sale price of:
    - The four inherited houses
    - Any new house in Ames, based on user input
    """)
