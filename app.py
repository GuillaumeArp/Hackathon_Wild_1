import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_icon=':musical_note:')

st.markdown("<h1 style='text-align: center;'>Music Popularity Analysis</h1>", unsafe_allow_html=True)

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
def load_data_pop_genre():
    return pd.read_csv('data/pop_genre.csv.zip')

data_polar_top = load_data_polar()
data_ml = load_data_ml()
popularity_genre = load_data_pop_genre()


st.title(' ')

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
        st.image('assets/logo_data_yoyo.png', width=300)
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
        st.image('assets/nizar.png')
        
    with col3:
        st.markdown('[Alexandra Houssin](hhttps://github.com/alexandrahoussin)')
        st.image('assets/alex.png')    
    
    ''    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown('[Catherine Le Calve](https://github.com/CathieLC)')
        st.image('assets/cath.png')
        
    with col5:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.image('assets/logo_data_yoyo.png', width=400)
        
    with col6:
        st.markdown('[Bérenger Queune](https://github.com/BerengerQueune)')
        st.image('assets/berenger.png')
        
def scenario():
    
    st.subheader('The story')

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('assets/the-osmonds-musical.jpg')
    
    'It all started in the 60s with the arrival of the first boy bands.'
    'This successful term was originally family-run with The Osmonds, made up of 5 brothers, who produced cheerful and romantic songs.'
    'Others have started to ride the wave, and in particular The Jackson five, which will form the basis of this new musical approach that will be the boys band.'

    'Finally definition is simple : Omnipresence of voices sung in chorus, synchronized attitude and songs that could seduce young girls.'
    'Yes yes, only young girls ...'

    'Music is like fashion, it\'s cyclical. With the popularity running out of control, the record companies started to get ideas.'
    '30 years later, the same excitement with the new boys bands, this time with young girls who are part of the game (the spice girls not to mention them).'

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('assets/Past_time.gif')

    'A global success with these groups, such a dazzling disappearance you could say? But what financial success!'
    'It is then without counting on our 5 super brains able to predict you which best combinations of musical data can bring you to the artistic and financial recognition !'

    " "
    st.subheader('Who are we?')

    'Alexandra, Catherine, Bérenger, Guillaume and Nizar.'
    'We all come from the wild code school with different backgrounds but one point brought us together:'
    st.markdown("<h6 style = 'text-align : center'> We miss the boys bands (and the money too)! </h6>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('assets/brain.png', width = 300)

    'After a big brainstorming session, our ideas rocketed faster than the latest one from space X (and we didn\'t explode!)'
    'We defined together that the death of the boy bands were unfair and that thanks to the compilation of our ideas, we could dust them off to make the tickets trickle.'

    col1, col2, col3, col4, col5 = st.columns(5)
    with col2:
        st.image('assets/money_rain.gif', width = 280)   
    with col4:
        st.image('assets/picsou.gif')   

    'So yes ! It\'s a pure commercial product, but it works!'
    'For your information, The beatles have also been categorized as a boy band!'

    " "
    st.subheader('Keep a cool head, Data Yoyo is here')

    'We have understood that if it is in our head, it is achievable, so we did it !'

    'From the spotify database, we asked ourselves with what parameters we could predict the popularity of a title.'
    'These parameters, we would like to modify them in real time and this is what we managed to do with the sliders that you can see on the popularity_estimator page.'
    'To show you our demo, you can select any title and we can show you what our app is capable of!'
    'These are automatically matched with the corresponding sliders and you can see that if we change a parameter, we can influence its popularity.'


    " "
    st.subheader('Beware the fall !')

    'Obviously what we do not yet know how to do is influence the human parameter to ensure our commercial success for sure!'
    'But we are working on it for the next datathon'

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('assets/logo_data_yoyo.png')

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
    
    "The most popular genres have high danceability. But we can see that it's not the only characteristic to do a hit song. Let's go further and and study all the features that make a hit!"
    
    "Let's see if the hit songs have common features. We sorted the data to keep only songs with popularity over 80 to see that."
      
    carac = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness',  'valence', 'loudness_scaled']
    
    fig = px.line_polar(data_polar_top, theta=carac, r= data_polar_top[carac].mean(), line_close=True, template="plotly_dark", 
                        color_discrete_sequence=['rgb(195,38,135)'], title="Common characteristics of hit songs")
    fig.update_traces(fill='toself')
    fig.update_layout(width=1000, 
                      height=600, 
                      title= {'x' : 0.5})
    
    st.plotly_chart(fig, use_container_width=True)
    
    "This polar chart shows us that a popular song is a song on which we can easily dance and with high energy. The valence is one of hit songs characteristics too, listeners prefer positive songs. We've scaled the loudness and show the absolute value. Here we can see that Hit songs have a high intensity."

def popularity_estimator():
    
    st.subheader('Predicting if a track will be popular or not')
    
    col1, col2, col3 = st.columns([3, 1, 3])
    
    with col1:
        artist_name = st.selectbox('Select an artist or band', data_ml['artist_name'].unique())
    
    with col3:
        df_temp = data_ml[data_ml['artist_name'] == artist_name]
        track_name = st.selectbox('Select a track name', df_temp['track_name'])
    
    track_id = df_temp[df_temp['track_name'] == track_name]['track_id'].values[0]
    
    selected_track_df = data_ml[data_ml['track_id'] == track_id]

    genre_list = ["Children's Music", 'Comedy', 'Indie', 'Jazz', 'Pop', 'Electronic', 'Folk', 'Hip-Hop', 'Rock', 'Alternative', 'Classical', 'Rap', 'World', 'Soul', 'Blues', 'R&B', 'Anime', 'Reggaeton', 'Ska', 'Reggae', 'Dance', 'Country', 'Opera', 'A Capella']
    
    selected_genre = ''
    for i in genre_list:
        if selected_track_df[i].values[0] == 1:
            selected_genre = i
  
    selected_mode = ''
    if selected_track_df['mode'].values[0] == 1:
        selected_mode = 'Major'
    else:
        selected_mode = 'Minor'
        
        
    
    col1, col2, col3, col4, col5= st.columns([3,1,3,1,3])
    
    with col1:
        valence = st.slider(label='Valence', min_value=0.0, max_value=1.0, value=float(selected_track_df['valence'].iloc[0]), step=0.01)
        danceability = st.slider(label='Danceability', min_value=0.0, max_value=1.0, value=float(selected_track_df['danceability'].iloc[0]), step=0.01)
        loudness = st.slider(label='Loudness', min_value=-50.0, max_value=0.0, value=float(selected_track_df['loudness'].iloc[0]), step=0.1)
        tempo = st.slider(label='Tempo', min_value=32, max_value=242, value=int(selected_track_df['tempo'].iloc[0]), step=1)
        
    with col3:
        energy = st.slider(label='Energy', min_value=0.0, max_value=1.0, value=float(selected_track_df['energy'].iloc[0]), step=0.01)
        speechiness = st.slider(label='Speechiness', min_value=0.0, max_value=1.0, value=float(selected_track_df['speechiness'].iloc[0]), step=0.01)
        instrumentalness = st.slider(label='Instrumentalness', min_value=0.0, max_value=1.0, value=float(selected_track_df['instrumentalness'].iloc[0]), step=0.01)
        duration_ms = st.slider(label='Duration', min_value=90, max_value=900, value=int(selected_track_df['duration_ms'].iloc[0]), step=1)
        
    with col5:
        liveness = st.slider(label='Liveness', min_value=0.0, max_value=1.0, value=float(selected_track_df['liveness'].iloc[0]), step=0.01)
        acousticness = st.slider(label='Acousticness', min_value=0.0, max_value=1.0, value=float(selected_track_df['acousticness'].iloc[0]), step=0.01)
        genre = st.select_slider(label='Genre', options=genre_list, value=selected_genre)
        mode = st.select_slider(label='Mode', options=['Major', 'Minor'], value=selected_mode)
        
        if mode == 'Minor':
            mode = 0
        else:
            mode = 1
        
    def algo_popularity():

        df_popular = pd.DataFrame()

        cols = ['acousticness', 'danceability', 'duration_ms', 'energy',
       'instrumentalness', 'liveness', 'loudness', 'mode',
       'speechiness', 'tempo', 'valence', 'A Capella',
       'Alternative', 'Anime', 'Blues', "Children's Music",
       'Classical', 'Comedy', 'Country', 'Dance', 'Electronic', 'Folk',
       'Hip-Hop', 'Indie', 'Jazz', 'Opera', 'Pop', 'R&B', 'Rap',
       'Reggae', 'Reggaeton', 'Rock', 'Ska', 'Soul', 'World']

        X = data_ml[cols]
        y = data_ml['popularity_score']
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75)

      
        # Random Forest
        rfc = RandomForestClassifier(n_estimators=8)
        rfc.fit(X_train, y_train)

        dataset_columns = ['artist_name', 'track_name', 'track_id']

        df_popular = pd.DataFrame(columns=dataset_columns)

        genres = ['A Capella',
            'Alternative', 'Anime', 'Blues', "Children's Music",
            'Classical', 'Comedy', 'Country', 'Dance', 'Electronic', 'Folk',
            'Hip-Hop', 'Indie', 'Jazz', 'Opera', 'Pop', 'R&B', 'Rap',
            'Reggae', 'Reggaeton', 'Rock', 'Ska', 'Soul', 'World']

        genres = sorted(genres, reverse=True)



        for i in genres:
            if genre == i:
                df_popular.insert(1, i, [1])
            else:
                df_popular.insert(1, i, [0])
                
        df_popular.insert(1, "valence", [valence])
        df_popular.insert(1, "tempo", [tempo])
        df_popular.insert(1, "speechiness", [speechiness])
        df_popular.insert(1, "mode", [mode])
        df_popular.insert(1, "loudness", [loudness])
        df_popular.insert(1, "liveness", [liveness])
        df_popular.insert(1, "instrumentalness", [instrumentalness])
        df_popular.insert(1, "energy", [energy])
        df_popular.insert(1, "duration_ms", [duration_ms])
        df_popular.insert(1, "danceability", [danceability])
        df_popular.insert(1, "acousticness", [acousticness])

        df_popular["popularity_score"] = rfc.predict(df_popular[cols])

        resultat = df_popular["popularity_score"].iloc[0]

        return resultat

    col1, col2, col3, col4, col5= st.columns([3,5,1,5,3])

    with col1:
        st.write(" ")
        
    with col3:
        if st.button('Click Here'):
            #########
            resultat = algo_popularity()
            if resultat == 1:
                st.write("bravo c'est 1 lol")
            elif resultat == 2:
                st.write("bravo c'est 2 lol")
            elif resultat == 3:
                st.write("bravo c'est 3 lol")
            elif resultat == 4:
                st.write("bravo c'est 4 lol")
            elif resultat == 5:
                st.write("bravo c'est 5 lol")
            #########

        
    ''    
    with col3:
        st.write(" ")
    
if __name__ == "__main__":
    main()