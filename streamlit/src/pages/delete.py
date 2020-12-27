import requests
import json

import streamlit as st
import pandas as pd

from config import API_URL

PAGE_TITLE = 'Delete Item'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    items = read_items()
    items.set_index('id', inplace=True)
    st.write(items)

    namecol='name'
    pricecol='price'

    selected_id = st.selectbox(
        label='Choose Item to Update',
        options=list(items.index),
        format_func=lambda x: f'{x}: {items.loc[x,namecol]} (${items.loc[x,pricecol]})')

    delete = st.button(label='Delete'):

    if delete:
        deleted_item = delete_item(id=selected_id)
        if deleted_item:
            st.write(deleted_item)
            delete = False

def delete_item(id):
    url = f'{API_URL}/item/delete/{id}'
    res = requests.post(url)
    return json.loads(res.text)

def read_items():
    url = f'{API_URL}/items/'
    res = requests.get(url)
    return pd.read_json(res.text)

if __name__=='__main__':
    write()