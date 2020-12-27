import streamlit as st
import pandas as pd
import requests

PAGE_TITLE = 'Create Item'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    st.markdown('## Enter item details')
    item_name = st.text_input(
        label='Item Name',
        value='')

    item_price = st.number_input(
        label='Item Price ($USD)',
    )

if __name__=='__main__':
    write()