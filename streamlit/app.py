import streamlit as st
import pandas as pd

# ast credit to https://github.com/MarcSkovMadsen/awesome-streamlit
import awesome_streamlit as ast
import src.pages.create
import src.pages.read
import src.pages.update
import src.pages.delete

ast.core.services.other.set_logging_format()

PAGES = {
    'Create': src.pages.create,
    'Read': src.pages.read,
    'Update': src.pages.update,
    'Delete': src.pages.delete
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    
    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

if __name__=='__main__':
    main()