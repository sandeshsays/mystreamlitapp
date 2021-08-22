import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

plt.style.use("dark_background")
st.set_page_config(layout = "wide")

# @st.cache
def get_data():
    path = 'data/15.json'
    return pd.read_json(path)
    
df = get_data()

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

# with header:
st.title('Welcome to My First App!')

# Using the "with" syntax
with st.form(key='my_form'):
    province = df['province'].drop_duplicates()
    province_choice = st.selectbox('Select Province:', province)
    district = df['district'].drop_duplicates()
    district_choice = st.selectbox('Select District:', district)
    localbody = df['localbody'].drop_duplicates()
    localbody_choice = st.selectbox('Select Local Body:', localbody)
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # st.dataframe(df)
    st.dataframe(df[['full_name_np','father','mother','province','district','ward','house_no','plus_code','_geolocation']])


# with dataset:
#     st.header('LGP Dataset')
#     df = pd.read_json('data/15.json')



#     makes = df['make'].drop_duplicates()
#     make_choice = st.selectbox('Select Region:', makes)

# with features:
#     st.header('The features I created')

# with model_training:
#     st.header('time to train')

