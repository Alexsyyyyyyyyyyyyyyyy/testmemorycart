from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle
class Question():
    def __init__(self,question,right_answer,wrong_1,wrong_2,wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
question_list = []
question_list.append(Question('Сколько ног у паука','8','5','6','4'))
question_list.append(Question('Как называется электро кар','тесла','жига','тойота','маздам'))        
question_list.append(Question('Кто есть жираф','животное','живот','хывотное','ивотное'))
shuffle(question_list)
app = QApplication([])

 
window = QWidget()
window.setWindowTitle('Memo Card')
 
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('В каком году была основана Москва?') # текст вопроса
 
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

AnswerButtonGroup = QButtonGroup()
AnswerButtonGroup.addButton(rbtn_1)
AnswerButtonGroup.addButton(rbtn_2)
AnswerButtonGroup.addButton(rbtn_3)
AnswerButtonGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


#Группа результат-теста
AnswerGroup = QGroupBox('Результат теста')
lb_result = QLabel('правильно/неправильно') #переменная результата
lb_current = QLabel('Правильный ответ') #переменная ответа
answer_line = QVBoxLayout() #вертикальная линия

#Привязка виджетов к линии
answer_line.addWidget(lb_result) 
answer_line.addWidget(lb_current) 

AnswerGroup.setLayout(answer_line)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addWidget(lb_Question)
layout_card.addWidget(RadioGroupBox)
layout_card.addWidget(AnswerGroup)
layout_card.addWidget(btn_OK)
AnswerGroup.hide()

def show_result():
    RadioGroupBox.hide()
    AnswerGroup.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnswerButtonGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    AnswerButtonGroup.setExclusive(True)  
    AnswerGroup.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    
def start():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    lb_Question.setText(q.question)
    lb_current.setText(q.right_answer)
    show_question()
    
def check_answer():
    if answers[0].isChecked():
        lb_result.setText('Правильно!')
        window.total += 1
    else:
        lb_result.setText('Неверно!')
    show_result()
def next_question():
    window.num_of_question +=1
    if window.num_of_question == len(question_list):
        result()
        window.num_of_question = 0
    q = question_list[window.num_of_question]
    ask(q)
def result():
    result_win = QMessageBox()
    percent=window.total/len(question_list) * 100
    if percent >80:
        rs = 'Хорощо'
    elif  percent <=80 and perecent>60:
        rs = 'Гуд'
    else:
        rs = 'Могло быть хуже'
    result_win.setText('Ваш результат:\n' + str(window.total) + '/' + str(len(question_list)))
    result_win.exec_()
window.total = 0
window.num_of_question = -1
btn_OK.clicked.connect(start)
window.setLayout(layout_card)
window.show()
app.exec()
