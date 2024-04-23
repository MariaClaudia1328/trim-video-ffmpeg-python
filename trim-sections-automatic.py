import os
import sys 

marcacoes_csv = sys.argv[1]
nome_filme = sys.argv[2]

inicio = []
final = []
label = []
with open(marcacoes_csv) as f:
    for row in f:
        actual_row = row.split(',')
        inicio.append(actual_row[0])
        final.append(actual_row[1])
        label.append(actual_row[2].strip())

command = "ffmpeg -i " + nome_filme 

for i in range(1,len(inicio)):
    output_name = str(i) + "_output_" + label[i] +".mp4"
    command +=" -ss " + inicio[i] + " -to " + final[i] + " -c:v copy -c:a " + output_name
    
os.system(command)