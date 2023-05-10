#IMPORTANTE _____ Leer directorio donde está este archivo
import os
#Hacer una variable con el archivo a leer en la carpeta de este archivo
target_path_1 = os.path.join(os.path.dirname(__file__), 'Database.xlsx')

#IMPORT DATABASE
import pandas as pd
df = pd.read_excel(target_path_1, header =0, dtype = 'str')
Data_m = df.to_numpy().tolist()

#MAKE QUESTIONS AND INPUT
#Inicialize value to loop
QuestionNumber = 0
    
#inicialize Score
Score = 0

print('**************************************************')
print('你好！ CHOOSE WHAT IS THE CORRECT PINYIN')

#Number of questions the user wants
QuizzQN = input('How many questions do you want? ')
QuizzQN = int(QuizzQN)

for QuestionNumber in range(QuizzQN):

    Question = Data_m[QuestionNumber][0]
    Aoption = Data_m[QuestionNumber][1]
    Boption = Data_m[QuestionNumber][2]
    Coption = Data_m[QuestionNumber][3]
    Doption = Data_m[QuestionNumber][4]

    CorrectAnswer = Data_m[QuestionNumber][5]

    #SHOW RESULTS

    print('**************************************************')
    print('Question: ' + str(QuestionNumber + 1))

    print(Question)
    print('A)' + Aoption)
    print('B)' + Boption)
    print('C)' + Coption)
    print('D)' + Doption)
    Answer = input('Answer (CAPS): ')


    if Answer == CorrectAnswer:
        print('Correct')
        Score = Score + 1
    else:
        print('Incorrect ')

    print("Current Score: " + str(Score) + ' points')
#Data to show
print('****************************************************')
print("TOTAL Score: " + str(Score) + ' points')
print("PROGRAMED BY: ALEJANDRO 阿里山 Jimenez")
