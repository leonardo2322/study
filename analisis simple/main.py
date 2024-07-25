from banner import bannerPaper
from funcionalidades import saveInExcel
import pandas as pd

bannerPaper()

bd = pd.read_excel(".\\ResetasPrueba.xlsx", sheet_name=hoja, header=None,engine='openpyxl')