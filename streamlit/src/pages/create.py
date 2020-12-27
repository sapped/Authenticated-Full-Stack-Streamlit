import requests
import json

import streamlit as st
import pandas as pd

from config import API_URL

PAGE_TITLE = 'Create Item'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    st.markdown('## Enter item details')
    
    item = {}

    item['name'] = st.text_input(
        label='Item Name',
        value='')

    item['price'] = st.number_input(
        label='Item Price ($USD)',
    )

    if st.button(label='Submit'):
        submit_item(item)

def submit_item(item):
    url = f'{API_URL}/item/'
    res = requests.post(url, json=item)
    res_json = json.loads(res.text)
    st.write(res_json)

if __name__=='__main__':
    write()