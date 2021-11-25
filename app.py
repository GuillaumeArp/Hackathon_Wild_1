import streamlit as st
import pandas as pd

st.set_page_config(page_title='Music Popularity Analysis', page_icon=':musical_note:')

def _max_width_():
    max_width_str = "max-width: 1300px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

st.title('Music Track Analysis Project')

def main():

    pages = {
        'Home': home,
        'Scenario': scenario,
        'Best Parameters': music_details,
        'Popularity Estimator': popularity_estimator
        }

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Home'
        })

    with st.sidebar:
        page = st.selectbox("Choose a page", tuple(pages.keys()))

    pages[page]()


def home():

    st.subheader('About this project')

    'This project was completed during a 33 hours hackathon, and the subject is music.'
    'We tried to determine what makes a music track popular, and to estimate the popularity of a track by tweaking its characteristics.'
    'This app is brought to you by the awesome Data Yoyo Team:'
    ''
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('[Guillaume Arp](https://github.com/GuillaumeArp)')
        st.image('assets/guillaume.png')
        
    with col2:
        st.markdown('[Nizar Ben Slama](https://github.com/bennizar87)')
        #st.image('')
        
    with col3:
        st.markdown('[Alexandra Houssin](hhttps://github.com/alexandrahoussin)')
        #st.image('')    
    
    ''    
    col4, col5 = st.columns(2)
    
    with col4:
        st.markdown('[Catherine Le Calve](https://github.com/CathieLC)')
        st.image('assets/cath.png')
        
    with col5:
        st.markdown('[Bérenger Queune](https://github.com/BerengerQueune)')
        #st.image('')
        
def scenario():
    
    st.subheader('Scenario')

def music_details():
    pass

def popularity_estimator():
    pass