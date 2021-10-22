import pandas as pd
import openpyxl
from pandas.core.indexes.base import Index   

'''CON CSV donde sacare los datos par amandar el valor 1'''
arch_csv = pd.read_csv('1.csv')
print(arch_csv[['Participants']])

'''CON XLSX es a donde voy a mandar el 1 cuando Participants sea igual entre B19;B66'''
arch_excel = pd.read_excel('2.xlsx')
print(arch_excel[['CONTROL DE ASISTENCIA']].iloc[17:66])