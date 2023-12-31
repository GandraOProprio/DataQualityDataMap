import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
DETA_KEY = 'VprRGKpS_6M1PSsShZJZMj8FZRg167giyFNQTvVs7'
# DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("monthly_reports")


def insert_period(Campaign_name, campaign_id, d, selected_instrument):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": Campaign_name, "id": campaign_id, "period": d, "instruments": selected_instrument})



def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)