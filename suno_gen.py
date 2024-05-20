from suno import SongsGen
from config import SUNO_COOKIE

def suno_gen(query,callback):
    songs = []
    gen = SongsGen(SUNO_COOKIE) # Replace 'cookie'
    print(gen.get_limit_left())
    songs=gen.save_songs(query, './output',callback=callback)
    return songs