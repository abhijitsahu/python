import media
import fresh_tomatoes


'''
Pass below args to Movie class.
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube
'''
# Create an object for "Luka Chuppi" class movie
luka_huppi = media.Movie(
    "Luka Chuppi",
    "The story of Guddu a television reporter in Mathura,"
    "who falls in love with a headstrong woman Rashmi.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcSHDq0RNEZ1"
    "od03cG7XEA0-LVXBPwZKMWrzHBgSbfE0HQ0rFarR",
    "https://www.youtube.com/watch?v=-JLewvWBkCw"
    )
# Create an object for "Aladdin" class movie
aladdin = media.Movie(
    "Aladdin",
    "It's an upcoming American musical fantasy film"
    "directed by Guy Ritchie, from the screenplay "
    "co-written with John August,"
    "and produced by Walt Disney Pictures.",
    "https://upload.wikimedia.org/wikipedia/en/9/9a/"
    "Aladdin_%28Official_2019_Film_Poster%29.png",
    "https://www.youtube.com/watch?v=foyufD52aog")
# Create an object for "Kalanak" class movie
kalank = media.Movie(
    "Kalanak",
    "The upcoming Indian Hindi-language period drama film "
    "directed by Abhishek Varman and produced by Karan Johar,"
    "Sajid Nadiadwala and Fox Star Studios.",
    "https://upload.wikimedia.org/wikipedia/en/8/80/"
    "Kalank_Poster.jpg",
    "https://www.youtube.com/watch?v=UmhXhTmP0a0")
# Create an object for "Kesari" class movie
kesari = media.Movie(
    "Kesari",
    "Kesari is an upcoming Indian action-war film starring "
    "Akshay Kumar and Parineeti Chopra in the lead roles and"
    "directed by Anurag Singh.",
    "https://upload.wikimedia.org/wikipedia/en/c/c4/"
    "Kesari_poster.jpg",
    "https://www.youtube.com/watch?v=JFP24D15_XM")
# Create an object for "Avenger" class movie
avenger = media.Movie(
    "Avenger",
    "upcoming American superhero film based on the Marvel"
    "Comics superhero team the Avengers, produced by Marvel"
    "Studios.",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/"
    "Avengers_Endgame_poster.jpg",
    "https://www.youtube.com/watch?v=TcMBFSGVi1c")
# Create an object for "Warriors" class movie
warriors_of_future = media.Movie(
    "Warriors of Future",
    "The upcoming Hong Kong science fiction"
    "action film directed by visual effects"
    "artist Ng Yuen-fai in his directorial"
    "debut and starring Louis Koo, Sean Lau"
    "and Carina Lau.",
    "https://upload.wikimedia.org/wikipedia/"
    "en/7/7b/WarriorsofFuture.jpg",
    "https://www.youtube.com/watch?v=0PDhuy6ovc0")

# making a list of movies obj for passing arg
movies = [kalank, kesari, luka_huppi, avenger, aladdin, warriors_of_future]
# passing arg to open_movies_page() of fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
