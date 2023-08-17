from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool
import sys
import time

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
    
    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)
        # time.sleep(5)
    
    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)



class Worker(QRunnable):
    '''
    Worker thread
    '''

    @Slot() # QtCore.Slot
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Thread start")
        time.sleep(5)
        print("Thread complete")

app = QApplication(sys.argv)
window = MainWindow()
app.exec()