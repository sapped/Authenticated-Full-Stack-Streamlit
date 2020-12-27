import requests
import json

import streamlit as st
import pandas as pd

from config import API_URL

PAGE_TITLE = 'Create Item'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    st.markdown('## Enter item details')
    
    data = {}

    data['item_name'] = st.text_input(
        label='Item Name',
        value='')

    data['item_price'] = st.number_input(
        label='Item Price ($USD)',
    )

    res = requests.get(f'{API_URL}/test')
    st.write(res.text)

    if st.button(label='Submit'):
        st.write('yay')
        submit_item(data)

def submit_item(data):
    url = f'{API_URL}/item'
    st.write(url)
    res = requests.post(url, data=data)
    res_json = json.loads(res.text)
    st.write(res_json)

if __name__=='__main__':
    write()