import sys
sys.path.append(".")

from PyQt5 import QtWidgets as qtw
import model.constants as cc
from model.dataframe_model import DFModel
from model.films import Films
from view.main_view_ui import Ui_MainWindow

class MainViewController(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.myfilms = Films(cc.IMDB_RATINGS_SOURCE)
        self.setupUi(self)
        self.main_controller()
    
    def main_controller(self):
        self.loadFilmsButton.clicked.connect(self.load_df_btn_clicked)
        self.loadSelectionButton.clicked.connect(self.set_selection)
        self.clearSelectionButton.clicked.connect(self.clear_selection_clicked)

#filters data according to user's selection    
    def set_selection(self):
        pass

#loads films dataset and displays data on table view     
    def load_df_btn_clicked(self):
        self.myfilms.load_films()
        self.df_model = DFModel(self.myfilms.films_df)
        self.mainTableView.setModel(self.df_model)

#clears the table view by loading the df model with an empty dataframe     
    def clear_selection_clicked(self):
        self.myfilms.set_dummy_df()
        self.df_model = DFModel(self.myfilms.dummy_df)
        self.mainTableView.setModel(self.df_model)