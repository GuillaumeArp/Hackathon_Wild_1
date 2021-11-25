import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import math

def popularity_score(popularity):
  popularity = popularity / 20
  popularity = math.ceil(popularity)
  return popularity

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/spotify.zip')

df.drop('time_signature', axis = 1, inplace = True)
df = df[(df['genre'] != 'Soundtrack') & (df['genre'] != 'Movie')]
df = df[(df['duration_ms'] > 90000) & (df['duration_ms'] < 900000)]
df['genre'].replace("Children's Music", "Children’s Music", inplace = True)

top_songs = df[df['popularity'] >= 80]
top_scaled = top_songs.copy()

scaler = MinMaxScaler()
top_scaled['loudness_scaled'] = scaler.fit_transform(top_songs['loudness'].values.reshape(-1, 1))


df_music_dummies = pd.concat([df , df['genre'].str.get_dummies()], axis = 1)
df_music_dummies['mode'] = df_music_dummies['mode'].factorize()[0]
df_music_dummies_keys = pd.concat([df_music_dummies , df_music_dummies['key'].str.get_dummies()], axis = 1)

df_music_dummies_keys["popularity_score"] = df["popularity"].apply(popularity_score)
cols = ['genre', 'artist_name', 'track_name', 'track_id', 'key']
df_music_dummies_keys.drop(cols, axis=1, inplace=True)
df_music_without_0_pop = df_music_dummies_keys[df_music_dummies_keys['popularity_score'] != 0]

df_final = df_music_without_0_pop.copy()
df_final['duration'] = round(df_music_without_0_pop['duration_ms'] / 1000)
df_final = df_final.astype({'duration': 'int32'})

df_final.to_csv('data/music_ml.csv.zip', compression='zip')
top_scaled.to_csv('data/top_polar.csv.zip', compression='zip')
