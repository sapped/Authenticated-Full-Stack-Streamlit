import requests
import json

import streamlit as st
import pandas as pd

from config import API_URL

PAGE_TITLE = 'Test Page'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    st.write('Test Page Loads')

if __name__=='__main__':
    write()