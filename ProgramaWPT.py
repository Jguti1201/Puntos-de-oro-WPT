# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 14:36:38 2021

@author: jaime
"""
#Los datos tienen este orden por columnas
"""Torneo;Cuadro (M/F);Pareja;Break Points;Winners;Smashes;Errores no forzados;
Puntos de oro;Tiempo;Tiempo (min);Resultado;Caracteres Resultado;Nº de sets;
Pareja Contrincante;Instancia;Break Poits (hechos);Break Points (generados);
Smashes con éxito;Smashes intentados;Año"""
""
#Los datos de los partidos con WO han sido descartados en el archivo de texto ya
# que no influían en las estadísticas que quería conseguir
import pandas as pd
import pandas
from math import *
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import os
ano='2021'
infile = open('Estadisticas_generales.txt','r')
PDO_PaqDin=0
PDO_LebGal=0
PDO_StuRui=0
PDO_ChiTel=0
PDO_Bela=0
PDO_Tapia=0
PDO_Sanyo=0
PDOC_PaqDin=0
PDOC_LebGal=0
PDOC_StuRui=0
PDOC_ChiTel=0
PDOC_Bela=0
PDOC_Tapia=0
PDOC_Sanyo=0    
for line in infile:
    lineList=line[:-1].split(';')
    Torneo=lineList[0]
    Genero=lineList[1]
    pareja=lineList[2]
    Winners=int(lineList[4].replace(',', ''))
    Erroresnoforzados=int(lineList[6].replace(',', ''))
    Puntosdeoro=int(lineList[7].replace(',', ''))
    tiempo_min=int(lineList[9].replace(',', ''))
    Resultado=lineList[10]
    numero_sets=int(lineList[12].replace(',', ''))
    pareja_contrincante=lineList[13]
    Instancia=lineList[14]
    Breakpoints_hechos=int(lineList[15].replace(',', ''))
    Breakpoints_generados=int(lineList[16].replace(',', ''))
    Smashes_exitosos=int(lineList[17].replace(',', ''))
    Smashes_intentados=int(lineList[18].replace(',', ''))
    año=lineList[19]
    """Vamos a hacer el análisis del año 2021 por lo que los demás datos no nos sirven"""
    if año==ano:
      """Análisis de los puntos de oro de las principales parejas del 2021"""    
      if pareja == 'Paquito Navarro / Martin Di Nenno':
          PDO_PaqDin=PDO_PaqDin+Puntosdeoro
      if pareja == 'Juan Lebron/ Ale Galan':
          PDO_LebGal=PDO_LebGal+Puntosdeoro
      if pareja == 'Alex Ruiz/ Franco Stupa':
          PDO_StuRui=PDO_StuRui+Puntosdeoro
      if pareja =='Fede Chingotto / Juan Tello':
          PDO_ChiTel=PDO_ChiTel+Puntosdeoro
      if pareja =='Fernando Belasteguin/ Sanyo Gutierrez':
          PDO_Bela=PDO_Bela+Puntosdeoro
          PDO_Sanyo=PDO_Sanyo+Puntosdeoro
      if pareja=='Fernando Belasteguin/ Arturo Coello':
          PDO_Bela=PDO_Bela+Puntosdeoro
      if pareja == 'Pablo Lima / Agustin Tapia':
          PDO_Tapia=PDO_Tapia+Puntosdeoro
      if pareja=='Agustin Tapia / Sanyo Gutierrez':
          PDO_Tapia=PDO_Tapia+Puntosdeoro
          PDO_Sanyo=PDO_Sanyo+Puntosdeoro
      if pareja_contrincante == 'Paquito Navarro / Martin Di Nenno':
          PDOC_PaqDin=PDOC_PaqDin+Puntosdeoro
      if pareja_contrincante == 'Juan Lebron/ Ale Galan':
          PDOC_LebGal=PDOC_LebGal+Puntosdeoro
      if pareja_contrincante == 'Alex Ruiz/ Franco Stupa':
          PDOC_StuRui=PDOC_StuRui+Puntosdeoro
      if pareja_contrincante =='Fede Chingotto / Juan Tello':
          PDOC_ChiTel=PDOC_ChiTel+Puntosdeoro
      if pareja_contrincante =='Fernando Belasteguin/ Sanyo Gutierrez':
          PDOC_Bela=PDOC_Bela+Puntosdeoro
          PDOC_Sanyo=PDOC_Sanyo+Puntosdeoro
      if pareja_contrincante=='Fernando Belasteguin/ Arturo Coello':
          PDOC_Bela=PDOC_Bela+Puntosdeoro
      if pareja_contrincante == 'Pablo Lima / Agustin Tapia':
          PDOC_Tapia=PDOC_Tapia+Puntosdeoro
      if pareja_contrincante=='Agustin Tapia / Sanyo Gutierrez':
          PDOC_Tapia=PDOC_Tapia+Puntosdeoro
          PDOC_Sanyo=PDOC_Sanyo+Puntosdeoro    

PorcenatajePDO_Bela= round((PDO_Bela / (PDO_Bela+PDOC_Bela))*100,2)
PorcentajePDO_PaqDin=round((PDO_PaqDin/(PDO_PaqDin+PDOC_PaqDin))*100,2)
PorcentajePDO_LebGal=round((PDO_LebGal/(PDO_LebGal+PDOC_LebGal))*100,2)
PorcentajePDO_StuRui=round((PDO_StuRui/(PDO_StuRui+PDOC_StuRui))*100,2)
PorcentajePDO_ChiTel=round((PDO_ChiTel/(PDO_ChiTel+PDOC_ChiTel))*100,2)
PorcentajePDO_Sanyo=round((PDO_Sanyo/ (PDO_Sanyo+PDOC_Sanyo))*100,2)
PorcentajePDO_Tapia=round((PDO_Tapia/(PDOC_Tapia+PDO_Tapia))*100,2)

x=['Bela','Paq-Din','Leb-Gal','Stu-Rui','Chi-Tel','Sanyo','Tapia']
y=[PorcenatajePDO_Bela,PorcentajePDO_PaqDin,PorcentajePDO_LebGal,PorcentajePDO_StuRui,PorcentajePDO_ChiTel,PorcentajePDO_Sanyo,PorcentajePDO_Tapia] 
plt.barh(x, y, color=("green","blue","black","yellow","grey","orange","red")) 
  
for index, value in enumerate(y): 
    plt.text(value, index, str(value)) 
plt.title("% éxito Puntos de oro")
 
plt.show()

     
          