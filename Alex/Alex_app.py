import streamlit as st
import pandas as pd
import plotly.express as px

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

@st.cache
def load_data_ml():
    return pd.read_csv('data/music_ml.csv.zip')

@st.cache
def load_data_popu_genre():
    return pd.read_csv('data/pop_genre.csv.zip')

data_polar_top = load_data_polar()
data_ml = load_data_ml()
popularity_genre = load_data_popu_genre()

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
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown('[Catherine Le Calve](https://github.com/CathieLC)')
        st.image('assets/cath.png')
        
    with col6:
        st.markdown('[Bérenger Queune](https://github.com/BerengerQueune)')
        #st.image('')
        
def scenario():
    
    st.subheader('Scenario')
    
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'

def music_details():
    
    st.subheader('What makes a track popular?')
    
    "We wanted to know if hit songs have any characteristics in common."
    " First of all what are the most popular genres of music? "
    
    fig = px.scatter_polar(popularity_genre, r="popularity", theta="genre",
                       color="popularity", size="popularity",
                       color_continuous_scale=px.colors.diverging.Tealrose, title='Popularity rate for each musical genre',
                       template="plotly_dark")
    fig.update_layout(
                    title= {'x' : 0.5},                    
                    width=1000,
                    height=600,                    
                    template='plotly_dark',
                    font_size=13
                    )
    st.plotly_chart(fig, use_container_width=True)
    "As we can see, the most popular genre is Pop with a mean popularity rate of 66.59. "
    
    "In our exploratory data analysis we've seen that the popularity is highly correlated with the danceability. So, do the most popular genres have the higher danceability?"
    fig = px.bar_polar(popularity_genre, r=popularity_genre['danceability'],
    theta = popularity_genre['genre'], template="plotly_dark", color= 'popularity', 
    color_continuous_scale=px.colors.diverging.Temps,
    title = "Danceability by genre")
    fig.update_layout(width=1000, 
                      height=600, 
                      title= {'x' : 0.5})
    st.plotly_chart(fig, use_container_width=True)
    "The most popular genres have high danceability. But we can see that it's not the only characteristic to do a hit song. Let's go further and and study all the features that make a hit !"
    
    "Let's see if the hit songs have common features. We sorted the data to keep only songs with popularity over 80 to see that."
      
    carac = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness',  'valence', 'loudness_scaled']
    fig = px.line_polar(data_polar_top, theta=carac, r= data_polar_top[carac].mean(), line_close=True, template="plotly_dark", 
                        color_discrete_sequence=['rgb(195,38,135)'], title="Common characteristics of hit songs")
    fig.update_traces(fill='toself')
    fig.update_layout(width=1000, 
                      height=600, 
                      title= {'x' : 0.5})
    st.plotly_chart(fig, use_container_width=True)
    "This polar chart shows us that a popular song is a song on which we can easily dance and with high energy. The valence is one of hit songs characteristics too, listeners prefer positive songs. We've scaled the loudness and show the absolute value. Here we can see that Hit songs have a high intensity "
    
    
def popularity_estimator():
    
    st.subheader('Predicting if a track will be popular or not')
    
    'Explanation text'
    
    genre_list = ["Children's Music", 'Comedy', 'Soundtrack', 'Indie', 'Jazz', 'Pop', 'Electronic', 'Folk', 'Hip-Hop', 'Rock', 'Alternative', 'Classical', 'Rap', 'World', 'Soul', 'Blues', 'R&B', 'Anime', 'Reggaeton', 'Ska', 'Reggae', 'Dance', 'Country', 'Opera', 'Movie', 'A Capella']
    key_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
    col1, col2, col3, col4, col5= st.columns([3,1,3,1,3])
    
    with col1:
        valence = st.slider(label='Valence', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        danceability = st.slider(label='Danceability', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        loudness = st.slider(label='Loudness', min_value=-50.0, max_value=0.0, value=-25.0, step=0.1)
        duration_ms = st.slider(label='Duration in seconds', min_value=90, max_value=900, value=210, step=1)
        
    with col3:
        energy = st.slider(label='Energy', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        speechiness = st.slider(label='Speechiness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        instrumentalness = st.slider(label='Instrumentalness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        key = st.select_slider(label='Key', options=key_list)
        
    with col5:
        liveness = st.slider(label='Liveness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        acousticness = st.slider(label='Acousticness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        genre = st.select_slider(label='Genre', options=genre_list, value='Pop')
        mode = st.select_slider(label='Mode', options=['Major', 'Minor'])
        
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'
    
if __name__ == "__main__":
    main()