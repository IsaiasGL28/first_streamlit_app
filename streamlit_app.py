import snowflake.connector as snf_con
import streamlit as st
import pandas as pd
import requests

st.title('My Mom\'s New Healthy Diner')

# ----------------- BREAKFAST FAVORITES -----------
st.header('Breakfast Favorites')
st.write(':bowl_with_spoon: Omega 3 & Blueberry Oatmeal')
st.write(':green_salad: Kale, Spinach & Rocket Smoothie')
st.write(':chicken: Hard-Boiled Free-Range Egg')
st.write(':avocado::bread: Avocado Toast')

# ----------------- FRUIT PICKER -------------------------------
st.header(':banana::mango: Build Your Own Fruit Smoothie :kiwifruit::grapes:')
fruits_df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits_df = fruits_df.set_index('Fruit')
fruits_list = list(fruits_df.index)
fruits_selected = st.multiselect('Pick some fruits: ', fruits_list, fruits_list[:2])
df_to_show = fruits_df.loc[fruits_selected]
st.dataframe(df_to_show)

#-------------------- FRUITYVICE API ---------------------
st.header('Fruityvice Fruit Advice!')
api_url = 'https://fruityvice.com/api/fruit/'
sel_fruit = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', sel_fruit)
json_response = requests.get(api_url+sel_fruit).json()
fruityvice_df = pd.json_normalize(json_response)
st.dataframe(fruityvice_df)


# ----------------- SNOWFLAKE CONNECTION -----------------
my_cnx = snf_con.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
