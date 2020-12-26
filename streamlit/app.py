import streamlit as st
import pandas as pd

def helloworld():
    st.header('Sapp Family Rankings of Christmas Gifts')
    
    data = {
        'Slaughters Greek Yogurt': [6,5,5,3,5,6],
        'Perkins Chex Mix': [1,3,6,4,2,4],
        'Austins Amaretto Cookies': [5,4,4,1,6,2],
        'Supples Peanut Clusters': [3,2,3,6,3,3],
        'Heckmans Chocolate Cookies': [4,6,2,5,4,5],
        'Pats Fudge Sauce': [2,1,1,2,1,1],
    }

    # df = pd.DataFrame(data=data)
    df = pd.DataFrame(data=data, index=['Edward','Mom','Baxter','MK','Hannah','Dad'])
    df.loc['mean'] = df.mean()
    
    df = df.T
    df = df[['mean','Edward','Mom','Baxter','MK','Hannah','Dad']]

    df = df.sort_values(by=['mean'])

    st.write(df)
    st.bar_chart(df['mean'])

    df = df.T
    for col in df.columns:
        with st.beta_expander(f'{col}'):
            st.bar_chart(df[col])

if __name__=='__main__':
    helloworld()