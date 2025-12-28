import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="ENTER_CLIENT_ID",
        client_secret="ENTER_SECRET_ID",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-modify-playback-state user-read-playback-state"
    )
)

def play_top_song(query):
    results = sp.search(q=query, type="track", limit=1)
    tracks = results["tracks"]["items"]

    if not tracks:
        print(f"No song found for '{query}'")
        return

    track_uri = tracks[0]["uri"]
    track_name = tracks[0]["name"]
    track_artist = tracks[0]["artists"][0]["name"]

    devices = sp.devices()
    if not devices['devices']:
        print("No active Spotify device found. Open Spotify and play a song first!")
        return

    device_id = devices['devices'][0]['id']

    sp.start_playback(device_id=device_id, uris=[track_uri])
    print(f"Now playing: {track_name} by {track_artist} on {devices['devices'][0]['name']}")


r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False

def record_text():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, phrase_time_limit=5)
            text = r.recognize_google(audio, language="en-GB")
            print("Recognised:", text)
            return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
    return None

with sr.Microphone() as source:
    print("Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Calibration complete.\n")


while True:
    text = record_text()
    if text is None:
        continue

    text_lower = text.lower()
    print("Heard:", text_lower)

    if "WORD" in text_lower.split():
        play_top_song("SONG_NAME")
        
    if "WORD" in text_lower.split():
        play_top_song("SONG_NAME")
        
    if "WORD" in text_lower.split():
        play_top_song("SONG_NAME")
    
    if "WORD" in text_lower.split():
        play_top_song("SONG_NAME")