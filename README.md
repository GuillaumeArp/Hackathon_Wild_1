# Music Popularity Predictor

This is a project done during a 29 hours hackathon, which subject was music.

Our team Data Yoyo decided to create a project to predict the popularity of a song based on its characteristics. To do that, we used a dataset from Spotify containing about 250k songs, and the calculated characteristics of those tracks, as well as the genre, the key, the mode, and the actual popularity of the track on Spotify.

The app can be found on [this page](https://data-yoyo.herokuapp.com/) (it may take few seconds for the server to wape up at first).

To summarize the scenario in few words, we wanted to create a tool that a music producer could use to create a band that would produce songs designed to be as profitable as possible. We added few plots to determine which characteristics were the most important to the success of a track, and then we added the tool itself, predicting the popularity of the song on a scale of 1 to 5, 5 being a probable huge hit.

To help get a feel of the different characteristics, it is possible to select a band or artist name, and then one of its songs, to automatically populate its data into the sliders, and start from that. After clicking on the button, the algorithm (a Random Forest Classifier) will predict the popularity of the song after few seconds, and show the results in the form of bank notes.

If you would like to clone or fork this project, and run it locally, please install the requirements from the dedicated requirements.txt file, and the run at the root of the folder the command:
`streamlit run app.py`
