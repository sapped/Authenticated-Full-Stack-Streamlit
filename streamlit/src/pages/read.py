import requests
import json

import streamlit as st
import pandas as pd

from config import API_URL

PAGE_TITLE = 'Read Items'

def write():
    st.markdown(f'# {PAGE_TITLE}')
    
    read_items()

def read_items():
    url = f'{API_URL}/items/'
    res = requests.get(url)
    st.write(pd.read_json(res.text))
    
    # if you just want to see the JSON, uncomment this:
    # res_json = json.loads(res.text)
    # st.write(res_json)

if __name__=='__main__':
    write()