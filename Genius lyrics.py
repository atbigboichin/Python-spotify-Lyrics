import time
import requests
from tkinter import Tk, BOTH, Label

from musixmatch import Musixmatch
from lyricsgenius import Genius
from pprint import pprint
from googletrans import Translator

from track import Track
from tokens import SPOTIFY_ACCESS_TOKEN, GENIUS_TOKEN

#OBVIOUSLY dont try to use this for the under:night ost THIS WILL NOT WORK there is no artist out there name "ratio"
#this is a very specific to me problem
#if you want all the lyrics you can like go through musixmatches process
#'TypeError: 'NoneType' object is not subscriptable' means you are listening to an ad
#if you get an error around lines 204-213 then the song you are playing does not have lyrics
#i think you have to reset the token every day
#https://www.youtube.com/watch?v=l4WOgef0pDU&list=PL0MxHK9qnVo4koZLFrOsNuEEZixV1_JAu&index=2 Thanks

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

root = Tk()
genius = Genius(GENIUS_TOKEN) #THIS IS NEEDED FOR GENIUS THOUGH, AND USE YOUR OWN API KEY STOP USING MINE
musixmatch = Musixmatch('<Use your own>') #this is not needed for genius
translator = Translator()




# Thank you Ian Annase

# musixmatch api base url
base_url = "https://api.musixmatch.com/ws/1.1/"

# your api key and I MEAN YOUR API KEY|| this is not needed for genius
api_key = "&apikey=:)"

# api methods

# This all should be reworked
a1 = lyrics_matcher = "matcher.lyrics.get"
a2 = lyrics_track_matcher = "track.lyrics.get"
a3 = track_matcher = "matcher.track.get"
a4 = subtitle_matcher = "matcher.subtitle.get"
a5 = track_search = "track.search"
a6 = artist_search = "artists.search"
a7 = album_tracks = "album.tracks.get"
a8 = track_charts = "chart.tracks.get"
a9 = artist_charts = "chart.artists.get"
a10 = related_artists = "artist.related.get"
a11 = artist_album_getter = "artist.albums.get"
a12 = track_getter = "track.get"
a13 = artist_getter = "artist.get"
a14 = album_getter = "album.get"
a15 = subtitle_getter = "track.subtitle.get"
a16 = snippet_getter = "track.snippet.get"
api_methods = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16]

# format url
format_url = "?format=json&callback=callback"

# parameters
p1 = artist_search_parameter = "&q_artist="
p2 = track_search_parameter = "&q_track="
p3 = track_id_parameter = "&track_id="
p4 = artist_id_parameter = "&artist_id="
p5 = album_id_parameter = "&album_id="
p6 = has_lyrics_parameter = "&f_has_lyrics="
p7 = has_subtitle_parameter = "&f_has_subtitle="
p8 = page_parameter = "&page="
p9 = page_size_parameter = "&page_size="
p10 = word_in_lyrics_parameter = "&q_lyrics="
p11 = music_genre_parameter = "&f_music_genre_id="
p12 = music_language_parameter = "&f_lyrics_language="
p13 = artist_rating_parameter = "&s_artist_rating="
p14 = track_rating_parameter= "&s_track_rating="
p15 = quorum_factor_parameter = "&quorum_factor="
p16 = artists_id_filter_parameter = "&f_artist_id="
p17 = country_parameter = "&country="
p18 = release_date_parameter = "&s_release_date="
p19 = album_name_parameter = "&g_album_name="
paramaters = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19]

# arrays with paramaters for each method
x1 = lyrics_matcher_parameters = [p1,p2]
x2 = lyrics_track_matcher_parameters = [p3]
x3 = track_matcher_parameters = [p1,p2,p6,p7]
x4 = subtitle_matcher_parameters = [p1,p2]
x5 = track_search_paramaters = [p1,p2,p10,p4,p11,p12,p12,p14,p15,p8,p9]
x6 = artist_search_parameters = [p1,p16,p8,p9]
x7 = album_tracks_parameters = [p5,p6,p8,p9]
x8 = track_charts_paramaters = [p8,p9,p17,p6]
x9 = artist_charts_parameters = [p8,p9,p17]
x10 = related_artists_parameters = [p4,p8,p9]
x11 = artists_album_getter_paramaters = [p4,p18,p19,p8,p9]
x12 = track_getter_parameters = [p3]
x13 = artist_getter_parameters = [p4]
x14 = album_getter_parameters = [p5]
x15 = subtitle_getter_parameters = [p3]
x16 = snippet_getter_parameters = [p3]
paramater_lists = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16]

# get the paramaters for the correct api method
def get_parameters(choice):
    if choice == a1:
        return x1
    if choice == a2:
        return x2
    if choice == a3:
        return x3
    if choice == a4:
        return x4
    if choice == a5:
        return x5
    if choice == a6:
        return x6
    if choice == a7:
        return x7
    if choice == a8:
        return x8
    if choice == a9:
        return x9
    if choice == a10:
        return x10
    if choice == a11:
        return x11
    if choice == a12:
        return x12
    if choice == a13:
        return x13
    if choice == a14:
        return x14
    if choice == a15:
        return x15
#https://www.youtube.com/watch?v=yKz38ThJWqE Thanks bro


def get_current_track():
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
        }
    )
    song_data = response.json()["item"]
    return Track(**song_data)

#
#    global artists_names
#    global track_name
#
#    track_id = resp_json['item']['id']
#    track_name = resp_json['item']['name']
#    artists = [artist for artist in resp_json['item']['artists']]
#
#    link = resp_json['item']['external_urls']['spotify']
#
#    artists_names = ', '.join([artist['name'] for artist in artists])
#
#    global tpt
#    global namept
#    tpt = track_name
#    namept = artists_names
#
#    current_track_info = {
#        "id": track_id,
#        "name": track_name,
#        "artists": artists_names,
#        "link": link
#    }


def breakwindow():
    for widgets in root.winfo_children():
        widgets.destroy()


def get_lyrics(track: Track):
    artists_names = ",".join(a for a in track.artists)
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artists_names + track_search_parameter + track.name + api_key
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    genius.excluded_terms = ["(Remix)", "(Live)"]
    # Does not work, you should figure out why
    # translated_names = (translator.translate(artists_names, dest="en")).text
    song = genius.search_song(track.name, artists_names)
    try:
        lyrics = song.lyrics
    except AttributeError:
        lyrics = ""

    # Should have
    # return lyrics

    # Should be in separate update_window(current_track) function called from main
    root.title(F"PLAYING: {track.name}")
    root.geometry("400x500")
    root.configure(bg="#00ff08")
    ratioL = (F"""
{track.name}
{track.artists}

{lyrics}""")
    lyricswindow = Label(root,text=ratioL,width=50,height=50, bg="#00ff08", font=("Arial",8))
    lyricswindow.pack(expand=True,fill=BOTH)
    root.wm_attributes("-topmost", 1)

    # Replaced mainloop() because it was blocking the entire program
    root.update()
    if "normal" == root.state():
        breakwindow()
        song = genius.search_song(F"{track.name}", artists_names)
        try:
            lyrics = song.lyrics
        except AttributeError:
            lyrics = ""
        ratioL = (F"""
    {track.name}
    {track.artists}

    {lyrics}""")
    root.title(F"PLAYING: {track.name}")
    lyricswindow = Label(
                    root,
                    text=ratioL,
                    width=50,
                    height=50,
                    bg="#00ff08",
                    font=("Arial", 8)
                )
    lyricswindow.pack(expand=True, fill=BOTH)
    # Replaced mainloop() because it was blocking the entire program
    root.update()


def main():
    current_track_id = None
    while True:
        time.sleep(1)
        current_track = get_current_track()

        if current_track.song_id == current_track_id:
            continue

        pprint(current_track, indent=4)
        current_track_id = current_track.song_id

        get_lyrics(current_track)
        # current_track.lyrics = get_lyrics(current_track)
        # update_window(current_track)


if __name__ == "__main__":
    main()
