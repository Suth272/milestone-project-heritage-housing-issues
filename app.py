import streamlit as st
from app_pages.multi_page import MultiPage

# Load page scripts
from app_pages.quick_project_summary import quick_project_summary_page
from app_pages.sale_price_study import sale_price_study_page
from app_pages.house_sale_price_ui import house_sale_price_ui_page
from app_pages.ml_house_sale_price import ml_house_sale_price_page

app = MultiPage(app_name="Ames Housing Price Prediction App")

# Add pages
app.add_page("Quick Project Summary", quick_project_summary_page)
app.add_page("Sale Price Study", sale_price_study_page)
app.add_page("House Sale Price UI", house_sale_price_ui_page)
app.add_page("ML: House Sale Price", ml_house_sale_price_page)

# Run the app
app.run()
