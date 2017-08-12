import media
import fresh_tomatoes

""" Create instances of the class media to store the list of my favorite movies """

deadpool = media.Movie("Deadpool","dc comics movie",
                        "http://media.comicbook.com/2016/09/deadpool-poster-198257-1280x0.jpg",
                        "https://www.youtube.com/watch?v=ONHBaC-pfsk")

suicide_squad = media.Movie("Suicide Squad", "dc comics movie",
                     "http://www.dccomics.com/sites/default/files/GalleryMovies_1920x1080_IntlKeyArt_57a3cb0dc87909.86070665.jpg",
                     "https://www.youtube.com/watch?v=CmRih_VtVAs&t=11s")

snatched = media.Movie("Snatched", "Amy Schumer movie",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BZTI5NWY1YTQtODYxMi00M2VmLTgzNDQtMGM3NWU5YjViNDE5XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=PsBWnst8f7w&t=4s")
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://is1.mzstatic.com/image/thumb/Video69/v4/22/50/c3/2250c3e7-6b24-a0df-dd8f-dea7321b3ee4/source/1200x630bb.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "Goint to meet authors",
                                "https://natashastander.files.wordpress.com/2014/07/mip.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

                                
hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

#list of movies
movies = [deadpool, suicide_squad, snatched, ratatouille, midnight_in_paris, hunger_games]

#Call function to generate HTML file to display the list of movies  
fresh_tomatoes.open_movies_page(movies)


                            


