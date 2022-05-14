

class Track:
    def __init__(self, **kwargs):
        self.song_id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.artists = (a["name"] for a in kwargs.get("artists"))
        self.link = kwargs.get("external_urls")["spotify"]
