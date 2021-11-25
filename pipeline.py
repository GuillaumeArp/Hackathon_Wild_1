import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/spotify.zip')

df.drop('time_signature', axis = 1, inplace = True)
df = df[(df['genre'] != 'Soundtrack') & (df['genre'] != 'Movie')]
df = df[(df['duration_ms'] > 90000) & (df['duration_ms'] < 900000)]
df['genre'].replace("Children's Music", "Children’s Music", inplace = True)

top_songs = df[df['popularity'] > 80]