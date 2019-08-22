from PySide2.QtWidgets import *
app = QApplication([])
layout = QVBoxLayout()
te = QTextEdit()
le = QLineEdit()
le2 = QLineEdit()
btn = QPushButton("&클릭")

te.setText("한글")
le.setText("한글도 들어갑니다")


layout.addWidget(te)
layout.addWidget(le)
layout.addWidget(btn)
layout.addWidget(le2)

window = QWidget()
window.setLayout(layout)


window.show()

print("te ::")
print(te.toPlainText())
print("*"*50)
print("le ::")
print(le.text())
print("*"*50)
print("btn ::")
print(btn)
print("*"*50)

def callBtn():
    print("callbtn")

btn.clicked.connect(callBtn())

app.exec_()