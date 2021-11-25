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

@st.cache
def load_data_polar():
    return pd.read_csv('data/top_polar.csv.zip')

data_polar_top = load_data_polar()

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
    
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'

def music_details():
    
    st.subheader('What makes a track popular?')
    
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'

def popularity_estimator():
    
    st.subheader('Predicting if a track will be popular or not')
    
    'Explanation text'
    
    genre_list = ["Children's Music", 'Comedy', 'Soundtrack', 'Indie', 'Jazz', 'Pop', 'Electronic', 'Folk', 'Hip-Hop', 'Rock', 'Alternative', 'Classical', 'Rap', 'World', 'Soul', 'Blues', 'R&B', 'Anime', 'Reggaeton', 'Ska', 'Reggae', 'Dance', 'Country', 'Opera', 'Movie', 'A Capella']
    key_list = ['C', 'G', 'D', 'C#', 'A', 'F', 'B', 'E', 'A#', 'F#', 'G#', 'D#']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        valence = st.slider(label='Valence', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        danceability = st.slider(label='Danceability', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        loudness = st.slider(label='Loudness', min_value=-50.0, max_value=0.0, value=-25.0, step=0.1)
        duration_ms = st.slider(label='Duration in seconds', min_value=90, max_value=900, value=210, step=1)
        
    with col2:
        energy = st.slider(label='Energy', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        speechiness = st.slider(label='Speechiness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        instrumentalness = st.slider(label='Instrumentalness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        key = st.select_slider(label='Key', options=key_list)
        
    ''    
    with col3:
        liveness = st.slider(label='Liveness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        acousticness = st.slider(label='Acousticness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        genre = st.select_slider(label='Genre', options=genre_list)
        mode = st.select_slider(label='Mode', options=['Major', 'Minor'])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(" ")
        
    with col2:
        if st.button('add'):
            result = add(1, 2)
            st.write('result: %s' % result)
        
    ''    
    with col3:
        st.write(" ")

if __name__ == "__main__":
    main()