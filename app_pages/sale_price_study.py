import streamlit as st

# def sale_price_study_page():
#     st.title("Sale Price Study")

#     st.markdown("""
#     """)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def sale_price_study_page():
    st.title("Sale Price Study")

    st.markdown("""
    ## Business Requirement 1

    Lydia needs to understand which house features are most correlated with sale prices in Ames, Iowa. This is important because her experience in the Belgian housing market might not reflect the factors that drive value in Iowa.
    
    This page displays the most correlated house features with `SalePrice`, helping Lydia make sense of what attributes matter most.
    
    The house features that have the strongest correlation with the sale price are: ['1stFlrSF', '2ndFlrSF', 'GarageArea', 'GarageYrBlt', 'OverallQual'].
    """)

    st.info(
        f"The correlation indicates that: \n"
        f"* The overall quality and condition of the house will increase the sale price of the house, and is the biggest factor. \n"
        f"* A bigger above ground living area will increase the sale price of the house. \n"
        f"* A bigger garage area will increase the sale price of the house. \n"
        f"* A bigger total basement area will increase the sale price of the house. \n"
        f"* A bigger first floor will increase the sale price of the house. \n"
    )

    # Load data
    df = pd.read_csv("outputs/datasets/collection/house_prices_records.csv")

    # Calculate correlations
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlations = numeric_df.corr()['SalePrice'].sort_values(ascending=False)

    top_corr_features = correlations.drop('SalePrice').head(5).index.tolist()

    # Plotting
    if st.checkbox("Churn Levels per Variable"):
        for feature in top_corr_features:
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x=feature, y='SalePrice', ax=ax)
            ax.set_title(f"{feature} vs SalePrice")
            st.pyplot(fig)