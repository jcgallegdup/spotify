"""
Showcases how the Spotify client retrieves data about arbitary artists.
"""

import pprint
import sys

from spotify_client import SpotifyClient


pp = pprint.PrettyPrinter(
    indent=2,
    depth=4,
    compact=True,
)

def _get_artist_data(spotify, artists):
    """
    Params:
        spotify (SpotifyClient): for making requests to Spotify web API.
        artists (iterable): each element is an artist name.
            (e.g. list of strings, file with artist names on each line)

    Returns:
        artist_data (dict): key is artist name, value is a dict containing artist metadata.
            e.g. {
                "Justin Bieber": {
                    id=1uNFoZAHBGtllmzznpCI3s,
                    num_followers=25683438,
                    genres=["canadian pop", "dance pop", "pop", "post-teen pop"]
                }
                ...
            }
    """
    artist_data = dict()
    for tmp_artist_name in artists:
        tmp_artist_name = tmp_artist_name.strip()
        data = spotify.get_artist_data(tmp_artist_name)
        if data is not None:
            artist_data[tmp_artist_name] = data
    return artist_data


def _get_artist_metadata(spotify, artist_names):
    """Fetches metadata for each artist specified in stdin.

    Returns:
        full_artist_metadata (dict): key is artist name, val is dict with:
            Spotify ID, genres, number of Spotify followers, related artists, and songs.

    e.g. {
        "Raveena": {
            'ID': '2kQnsbKnIiMahOetwlfcaS',
            'genres': ['indie r&b'],
            'num_followers': 19191,
            'related_artists': {
                'Alextbh': {
                    'ID': '0kXDB5aeESWj5BD9TCLkMu',
                    'genres': ['indie r&b', 'malaysian indie'],
                    'num_followers': 19517
                },
                ...
            },
            'songs': {
                'Honey': {
                    'duration_ms': 272331,
                    'id': '6ohzjop0VYBRZ12ichlwg5',
                    'popularity': 60,
                    'uri': 'spotify:track:6ohzjop0VYBRZ12ichlwg5'
                },
                ...
            }
        }
        ...

    """
    artist_summaries = _get_artist_data(spotify, artist_names)
    full_artist_metadata = dict()
    for artist, artist_summary in artist_summaries.items():
        full_artist_metadata[artist] = dict(
            ID=artist_summary["id"],
            num_followers=artist_summary["num_followers"],
            genres=artist_summary["genres"],
            related_artists=spotify.get_related_artists(artist_summary["id"]),
            songs=spotify.get_top_songs(artist_summary["id"], "CA")
        )
    return full_artist_metadata


def get_spotify_data(spotify_client_id, spotify_secret_key, artists, path=None):
    kb_api = KnowledgeBaseAPI(path_to_db)
    return artist_metadata

def main():
    print("Enter Spotify client ID:")
    spotify_client_id = sys.stdin.readline().split(" ")[-1].strip("\n")
    print("Enter Spotify secret key:")
    spotify_secret_key = sys.stdin.readline().split(" ")[-1].strip("\n")

    print("Enter names of artists, separated by new-lines:")
    artist_metadata = _get_artist_metadata(SpotifyClient(spotify_client_id, spotify_secret_key), sys.stdin)

    print("Fetched info: ")
    pp.pprint(artist_metadata)


if __name__ == "__main__":
    main()