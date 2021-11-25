import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title='Music Popularity Analysis', page_icon=':musical_note:')
df = pd.read_csv('..\data\dataset_algo.csv.zip', index_col=0)


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

data_polar_top = load_data_polar()
data_ml = load_data_ml()


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
        st.image('assets/logo_data_yoyo.png', width=200)
        page = st.selectbox("Choose a page", tuple(pages.keys()))

    pages[page]()


def home():

    st.image('assets/logo_data_yoyo.png', width=400)
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
    
    'Polar chart showing top music characteristics.'
    
    carac = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness',  'valence', 'loudness_scaled']
    fig = px.line_polar(data_polar_top, theta=carac, r= data_polar_top[carac].mean(), line_close=True, template="plotly_dark", 
                        color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig.update_traces(fill='toself')
    
    fig.update_layout(height=900)
    st.plotly_chart(fig, use_container_width=True)

def popularity_estimator():
    
    st.subheader('Predicting if a track will be popular or not')
    
    'Explanation text'
    
    genre_list = ["Children's Music", 'Comedy', 'Soundtrack', 'Indie', 'Jazz', 'Pop', 'Electronic', 'Folk', 'Hip-Hop', 'Rock', 'Alternative', 'Classical', 'Rap', 'World', 'Soul', 'Blues', 'R&B', 'Anime', 'Reggaeton', 'Ska', 'Reggae', 'Dance', 'Country', 'Opera', 'Movie', 'A Capella']
    
    col1, col2, col3, col4, col5= st.columns([3,1,3,1,3])
    
    with col1:
        valence = st.slider(label='Valence', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        danceability = st.slider(label='Danceability', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        loudness = st.slider(label='Loudness', min_value=-50.0, max_value=0.0, value=-25.0, step=0.1)
        tempo = st.slider(label='Tempo', min_value=32, max_value=242, value=120, step=1)
        
    with col3:
        energy = st.slider(label='Energy', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        speechiness = st.slider(label='Speechiness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        instrumentalness = st.slider(label='Instrumentalness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        duration_ms = st.slider(label='Duration', min_value=90, max_value=900, value=210, step=1)
        
    with col5:
        liveness = st.slider(label='Liveness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        acousticness = st.slider(label='Acousticness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        genre = st.select_slider(label='Genre', options=genre_list, value='Pop')
        mode = st.select_slider(label='Mode', options=['Major', 'Minor'])


    def algo_popularity():

        df_popular = pd.DataFrame()

        cols = ['acousticness', 'danceability', 'duration_ms', 'energy',
       'instrumentalness', 'liveness', 'loudness', 'mode',
       'speechiness', 'tempo', 'valence', 'A Capella',
       'Alternative', 'Anime', 'Blues', "Children's Music",
       'Classical', 'Comedy', 'Country', 'Dance', 'Electronic', 'Folk',
       'Hip-Hop', 'Indie', 'Jazz', 'Opera', 'Pop', 'R&B', 'Rap',
       'Reggae', 'Reggaeton', 'Rock', 'Ska', 'Soul', 'World']

        X = df[cols]
        y = df['popularity_score']
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75)


        scaler = StandardScaler().fit(X_train)

        # Your scaler model can now transform your data
        X_train_scaled = scaler.transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        model = LogisticRegression(max_iter=20).fit(X_train_scaled,y_train)

        dataset_columns = ['track_name']

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
        df_popular.insert(1, "tempo", [temp])
        df_popular.insert(1, "speechiness", [speechiness])
        df_popular.insert(1, "mode", [mode])
        df_popular.insert(1, "loudness", [loudness])
        df_popular.insert(1, "liveness", [liveness])
        df_popular.insert(1, "instrumentalness", [instrumentalness])
        df_popular.insert(1, "energy", [energy])
        df_popular.insert(1, "duration_ms", [duration_ms])
        df_popular.insert(1, "danceability", [danceability])
        df_popular.insert(1, "acousticness", [acousticness])

        df_popular["popularity_score"] = model.predict(df_popular[cols])

        resultat = df_popular["popularity_score"].iloc[0]

        return resultat

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(" ")
        
    with col2:
        if st.button('add'):
            #########
            algo_popularity()
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
        
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'
    
if __name__ == "__main__":
    main()