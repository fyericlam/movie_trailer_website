import media
import fresh_tomatoes

# Instantiate objects/instances from Movie class in media.py
# Provide values to five class variables:
# movie_title, movie_storyline, movie_duration, poster_image and trailer_youtube
cloverfield = media.Movie('Cloverfield',
                          'Six young New York City residents flee from a gigantic monster and various other smaller creatures that attack the city while they are having a farewell party.',
                          85,
                          'https://upload.wikimedia.org/wikipedia/en/f/f1/Cloverfield_theatrical_poster.jpg',
                          'https://www.youtube.com/watch?v=M1XEriXzNik')

ten_cloverfield_lane = media.Movie('10 Cloverfield Lane',
                                   'A young woman who, after a car crash, wakes up in an underground bunker with two men who insist that an event has left the surface of Earth uninhabitable.',
                                   104,
                                   'https://upload.wikimedia.org/wikipedia/en/0/0e/10_Cloverfield_Lane.png',
                                   'https://www.youtube.com/watch?v=1WQfDnj_e2I')

super_8 = media.Movie('Super 8',
                      'A group of young teenagers who are filming their own Super 8 movie when a train derails, releases a dangerous presence into their town.',
                      112,
                      'https://upload.wikimedia.org/wikipedia/en/7/74/Super_8_Poster.jpg',
                      'https://www.youtube.com/watch?v=t-0XuYxh67w')

the_cloverfield_paradox = media.Movie('The Cloverfield Paradox',
                                      "An international group of astronauts aboard a space station who, after using a particle accelerator to try to solve Earth's energy crisis, must find a way home after accidentally traveling to an alternate dimension",
                                      102,
                                      'https://upload.wikimedia.org/wikipedia/en/e/e5/Cloverfield_paradox_poster.jpg',
                                      'https://www.youtube.com/watch?v=8brYvhEg5Aw')

# Put Movie objects into a list
movies = [cloverfield, ten_cloverfield_lane, super_8, the_cloverfield_paradox]

# Call open_movies_page() function in fresh_tomatoes.py to build HTML file with movies list
fresh_tomatoes.open_movies_page(movies)
