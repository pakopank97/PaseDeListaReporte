from os import sep
import pandas as pd
import openpyxl
from pandas.core.indexes.base import Index   

'''CON CSV donde sacare los datos par amandar el valor 1'''
#Lectura del archivo CSV
arch_csv = pd.read_csv('1.csv', sep =',')
#jsCSV = arch_csv[['Participants']]
datosCVS = arch_csv[['Participants']]
datosCVS.to_excel('1.xlsx')
'''esta lines convierte la consulta del CVS a json'''
#jsCSV.to_json('jsCSV.json')
#listaCSV = []
#listaCSV.append(arch_csv[['Participants']])
#print(listaCSV)
#print(arch_csv[['Participants']])

#print(arch_csv[['Participants']]

'''CON XLSX es a donde voy a mandar el 1 cuando Participants sea igual entre B19;B66'''
arch_excel = pd.read_excel('2.xlsx')

'''en esta linea se solicitam los datos que se requieren para validar los datos del CVS con el XLSX'''
jsXLSX = arch_excel[['CONTROL DE ASISTENCIA']].iloc[17:66]
print(jsXLSX)