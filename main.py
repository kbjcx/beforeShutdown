import sys
from actions import actionOnShutdown, actionOnRecover
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Shutdown")

# 设置窗口的大小
window.resize(400, 200)

# 设置窗口的几何形状，使其居中显示
screen = app.primaryScreen()
geometry = screen.geometry()
x = (geometry.width() - window.width()) // 2
y = (geometry.height() - window.height()) // 2
window.setGeometry(x, y, window.width(), window.height())

buttonS = QPushButton("关机")
buttonS.setFixedHeight(50)
buttonS.clicked.connect(actionOnShutdown)

buttonR = QPushButton("重启")
buttonR.setFixedHeight(50)
buttonR.clicked.connect(actionOnRecover)
# 将按钮添加到窗口中
layout = QVBoxLayout()  # 创建一个垂直布局
layout.addWidget(buttonS)
layout.addWidget(buttonR) # 将第一个按钮添加到布局中

window.setLayout(layout)  # 将布局设置为窗口的布局

window.show()

sys.exit(app.exec_())


    
