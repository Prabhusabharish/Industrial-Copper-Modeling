import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from PIL import Image



# - - - - - - - - - - - - - - -set st addbar page - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

icon = Image.open("C:/Users/prabh/Downloads/Datascience/Project/Copper/1.png")
st.set_page_config(page_title= "BizCardX: Extracting Business Card Data with OCR",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded")

# - - - - - - - - - - - - - - -set bg image - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background: url("https://cutewallpaper.org/28/copper-hd-wallpaper/16624879.jpg");
                        background-size: cover}}
                     </style>""",unsafe_allow_html=True) 
setting_bg()



# - - - - - - - - - - - - - - -sidebar - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

st.sidebar.title("Navigation")
select_page = st.sidebar.radio("", ["Home", "Application"])

# - - - - - - - - - - - - - - -Home page - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Home page creation
if select_page == "Home":
    st.title("Home Page")

    st.markdown("""
            Technologies Used:
            - Python
            - Pandas
            - Numpy
            - Seaborn
            - sklearn
            - Pickle
            - Regression or Classification
            - Streamlit
            
            Features:
            - xxx
            """)


# ------------------------------ Application Page ----------------------#
elif select_page == "Application":
    st.title("Industrial Copper Modeling Application")




    # Dealing with data in wrong format
    copper[ "item_date"] = pd.to_datetime(copper["item_date"], format="%Y%m%d", errors = "coerce").dt.date
    copper[ "quantity tons"] = pd.to_numeric(copper["quantity tons"], errors = "coerce")
    copper["customer"] = pd.to_numeric(copper["customer"], errors = "coerce")
    copper["country"] = pd.to_numeric(copper["country"], errors = "coerce")
    copper["application"] = pd.to_numeric(copper["application"], errors = "coerce")
    copper["thickness"] = pd.to_numeric(copper["thickness"], errors = "coerce")
    copper["width"] = pd.to_numeric(copper["width"], errors = "coerce")
    copper["material_ref"] = copper["material_ref"].str. lstrip("0")
    copper[ "product_ref"] = pd.to_numeric (copper [ "product_ref"], errors = "coerce")
    copper["delivery date"] = pd.to_datetime(copper["delivery date"], format = "%Y%m%d", errors="coerce").dt.date
    copper["selling_price"] = pd.to_numeric (copper["selling_price"], errors = "coerce")


