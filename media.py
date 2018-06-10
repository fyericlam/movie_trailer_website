import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # Class constructor
    def __init__(self, movie_title, movie_storyline, movie_duration, poster_image, trailer_youtube):
        """
        Attributes:
            movie_title (str): Name of movie
            movie_storyline (str): Outline of story
            movie_duration (int): Length of movie in minutes
            poster_image (str): url of movie's poster in wikimedia
            trailer_youtube (str): url of movie's trailer at YouTube
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.duration = movie_duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Class method: open youtube trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
