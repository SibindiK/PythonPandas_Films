from PyQt5 import QtCore as qtc

class DFModel(qtc.QAbstractTableModel):
	def __init__(self, df):
		super().__init__()
		self._df = df
	
	def rowCount(self, parent=None):
		return self._df.shape[0]
	
	def columnCount(self, parent=None):
		return self._df.shape[1]
	
	def data(self, index, role=qtc.Qt.DisplayRole):
		if index.isValid():
			if role == qtc.Qt.DisplayRole:
				return str(self._df.iloc[index.row(), 
						index.column()])
		return None
	
	def headerData(self, col, orientation, role):
		if (orientation == qtc.Qt.Horizontal and role == qtc.Qt.DisplayRole):
			return self._df.columns[col].upper()
		return None
	
	