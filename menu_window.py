from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QHBoxLayout, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout, QSpinBox, QGroupBox, QButtonGroup, QLineEdit
menu_win = QWidget()
menu_win.setWindowTitle("Memory Card Menu")
menu_win.resize(400, 200)
menu_win.move(200,200)

lb_quest = QLabel("Введіть запитання:")
lb_right_ans = QLabel("Введіть правильну відповідь:")
lb_wrong1 = QLabel("Введіть неправильну відповідь:")
lb_wrong2 = QLabel("Введіть неправильну відповідь:")
lb_wrong3 = QLabel("Введіть неправильну відповідь:")

le_quest = QLineEdit()
le_right_ans = QLineEdit()
le_wrong1 = QLineEdit()
le_wrong2 = QLineEdit()
le_wrong3 = QLineEdit()


col1 = QVBoxLayout()
col2 = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()

col1.addWidget(lb_quest)
col1.addWidget(lb_right_ans)
col1.addWidget(lb_wrong1)
col1.addWidget(lb_wrong2)
col1.addWidget(lb_wrong3)           

col2.addWidget(le_quest)
col2.addWidget(le_right_ans)
col2.addWidget(le_wrong1)
col2.addWidget(le_wrong2)
col2.addWidget(le_wrong3)

row1.addLayout(col1)
row1.addLayout(col2)
add_btn = QPushButton("Додати запитання")
clear_btn = QPushButton("Очистити")
back_btn = QPushButton("Назад")
row2.addWidget(add_btn)
row2.addWidget(clear_btn)


stat_lb = QLabel("Статистика:")
stat_lb.setStyleSheet('font-size: 19px; font-weight: bold;')

count_ans_lb = QLabel("Кількість відповідей: 0")
count_right_lb = QLabel("Кількість правильних відповідей: 0")
success_lb = QLabel("Успішність: 0%")

vline = QVBoxLayout()
vline.addLayout(row1)
vline.addLayout(row2)
vline.addWidget(stat_lb)
vline.addWidget(count_ans_lb)
vline.addWidget(count_right_lb)
vline.addWidget(success_lb)
vline.addWidget(back_btn)


menu_win.setLayout(vline)
