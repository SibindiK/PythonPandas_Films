import pandas as pd

class Films():
    def __init__(self, _imdb_path:str):
        self.imdb_path = _imdb_path 
        
    def load_films(self):
        self.films_df = pd.read_csv(self.imdb_path)
    
    def set_dummy_df(self):
        self.dummy_df = pd.DataFrame()