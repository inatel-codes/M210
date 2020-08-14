import math 
import numpy as np

def simplex(table, lines, columns, decisions_variables, constraints):
  columns = columns-1
  pivotColumnIndex = lowerValueCalculate(table, columns)
  variables = np.zeros(lines)
  print("\n"+ str(table))
  while pivotColumnIndex != -1:
    pivotRowIndex = rowPivotCalculate(table, lines, columns, pivotColumnIndex)
    variables[pivotRowIndex] = pivotColumnIndex
    table = createNewTable(table, lines, columns, pivotRowIndex, pivotColumnIndex)
    print("\n"+ str(table))
    pivotColumnIndex = lowerValueCalculate(table, columns)

  
  #print("\nSolução Ótima: ")
  #for i in range(1, lines):
  #  print("X"+ str(int(variables[i]+1)) + " = " + str(table[i][columns]))
  
  greatProfit = table[0][columns]
  print("\nLucro Ótimo: " + str(greatProfit))

  print("\nPreço Sombra:")
  for i in range(0, constraints):
    print("X" + str(i+1) + " = " + str(table[0][i+decisions_variables]))

# Função que retorna o menor valor negativo da função objetivo
def lowerValueCalculate(table, columns):
  pivotColumn = -1
  lowerValue = 0

  for i in range(0, columns):
    if table[0][i] < lowerValue:
      lowerValue = table[0][i]
      pivotColumn = i

  return pivotColumn

def rowPivotCalculate(table, lines, columns, pivotColumnIndex):
  lowerValue = math.inf
  lowerValueIndex = -1

  for i in range(0, lines):
    if table[i][pivotColumnIndex] != 0:
      division = table[i][columns]/table[i][pivotColumnIndex]
    else:
      division = math.inf

    if(division > 0 and division < lowerValue):
      lowerValue = division
      lowerValueIndex = i

  return lowerValueIndex

def createNewTable(table, lines, columns, pivotRowIndex, pivotColumnIndex):
  pivot = table[pivotRowIndex][pivotColumnIndex]
  newTable = np.zeros((lines, columns+1))

  for i in range(0, columns+1):
    newTable[pivotRowIndex][i] = np.around(table[pivotRowIndex][i]/pivot, 2)

  for i in range(0, lines):
    for j in range(0, columns+1):
      if i != pivotRowIndex:
        parameter = table[i][pivotColumnIndex]*-1
        newTable[i][j] = np.around(table[i][j]+(parameter*newTable[pivotRowIndex][j]), 2)

  return newTable
