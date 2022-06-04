import pandas as pd

class Films():
    def __init__(self, _imdb_path:str):
        self.imdb_path = _imdb_path 
#load films         
    def load_films(self):
        self.films_df = pd.read_csv(self.imdb_path)

#blank dataframe to clear the table view     
    def set_dummy_df(self):
        self.dummy_df = pd.DataFrame()

#filter the films df based on user choice of genre, content_rating or actor name    
    def filter_df(self, genre, content_rating, actor):
        if ((genre == 'ALL') & (content_rating == 'ANY') & (actor == '')):
            _df = self.films_df
        elif((genre == 'ALL') & (content_rating != 'ANY') & (actor == '')):    
            _df = self.films_df.loc[self.films_df['content_rating'] == content_rating]    
        elif ((genre != 'ALL') & (content_rating == 'ANY') & (actor == '')):
            _df = self.films_df.loc[(self.films_df['genre'] == genre)]
        elif ((genre != 'ALL') & (content_rating != 'ANY') & (actor == '')):
            _df = self.films_df.loc[(self.films_df['genre'] == genre) &
                 (self.films_df['content_rating'] == content_rating)]
        elif ((genre == 'ALL') & (content_rating == 'ANY') & (actor != '')):
            _df = self.films_df.loc[self.films_df['actors_list'].str.contains(actor, case=False)]
        elif ((genre != 'ALL') & (content_rating == 'ANY') & (actor != '')):
            _df = self.films_df.loc[(self.films_df['genre'] == genre) & 
                    (self.films_df['actors_list'].str.contains(actor, case=False))]
        elif ((genre == 'ALL') & (content_rating != 'ANY') & (actor != '')):
            _df = self.films_df.loc[(self.films_df['content_rating'] == content_rating) & 
                    (self.films_df['actors_list'].str.contains(actor, case=False))]
        elif ((genre != 'ALL') & (content_rating != 'ANY') & (actor != '')):
            _df = self.films_df.loc[(self.films_df['genre'] == genre) & 
                    (self.films_df['content_rating'] == content_rating) & 
                    (self.films_df['actors_list'].str.contains(actor, case=False))]
       
        return _df