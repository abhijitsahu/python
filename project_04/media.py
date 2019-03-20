import webbrowser


class Movie():
    """A movie class for showcase movie trailers youtube.

    Movie class is to generate a website that displays movies.It also contains
    information about movie title, movie story line, url to poster of movie,
    url to movie trailer.

    Parameters
    ----------
    movie_title : str
        Movie title name 
    movie_storyline : str
        brief story for the same movie
    poster_image : str
        URL of poster image for the same movie
    trailer_youtube : str
        URL of youtube video for the same movie

    Attributes
    ----------
    title : str
        Movie title name 
    storyline : str
        brief story for the same movie
    poster_image_url : str
        URL of poster image for the same movie
    trailer_youtube_url : str
        URL of youtube video for the same movie

    """
    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube
    ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
    """
    Show trailer youtube link to opens up.

    It open a page in the browser, use the open() function.The URL is opened in
    a browser window, and that window is raised to the top of the window stack.

    Parameters
    ----------
    trailer_youtube_url : str
        URL to open in a browser window

    Returns
    -------
    None
    """
    webbrowser.open(self.trailer_youtube_url)

