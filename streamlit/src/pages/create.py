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

    create = st.button(label='Create')

    if create:
        item = submit_item(item)
        if item:
            st.write(item)
            create = False

def submit_item(item):
    url = f'{API_URL}/item/'
    res = requests.post(url, json=item)
    return json.loads(res.text)

if __name__=='__main__':
    write()