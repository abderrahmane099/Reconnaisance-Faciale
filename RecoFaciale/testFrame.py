import sys
import os
import pygame
import pygame.camera
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from reconnaitre import usedVar

class RecoFaciale(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif',10))

		camBtn = QPushButton('Ouvrir Camera',self)
		camBtn.setToolTip('Ce bouton permet de vous prendre en photo')
		camBtn.clicked.connect(self.cameraCall)
		camBtn.setStyleSheet('background-color:aqua')
		camBtn.resize(camBtn.sizeHint())
		camBtn.move(30,70)
		
		recoBtn = QPushButton('Lancer script',self)
		recoBtn.setToolTip('Ce bouton permet de lancer le script de reconnaissance faciale')
		recoBtn.clicked.connect(self.runAlgo)
		recoBtn.setStyleSheet('background-color:aqua')
		recoBtn.resize(recoBtn.sizeHint())
		recoBtn.move(30,100)

		closeBtn = QPushButton('Fermer',self)
		closeBtn.clicked.connect(self.closeEvent)
		closeBtn.resize(closeBtn.sizeHint())
		closeBtn.setStyleSheet('background-color:red')
		closeBtn.move(290,220)
		
		pixmap = QPixmap('C:/Users/YASSER/Desktop/RecoFaciale/test/testCam.jpg')
		lbl = QLabel(self)
		smaller_pixmap = pixmap.scaled(200, 200)
		lbl.setPixmap(smaller_pixmap)
		lbl.resize(200,200)
		lbl.move(230,20)
		
		self.display = QLabel(self)
		self.display.setText('')
		self.display.resize(150,150)
		self.display.move(460,85)

		
#		hbox = QHBoxLayout()
#		hbox.addStretch(1)
#		hbox.addWidget(lbl)
#		hbox.addWidget(camBtn)
#		
#		vbox = QVBoxLayout()
#		vbox.addStretch(1)
#		vbox.addLayout(hbox)
#		vbox.addLayout(closeBtn)
#		
#		self.setLayout(vbox)

		self.setGeometry(610,350,650,250)
		self.setWindowTitle('Reconnaissance Faciale')
		self.show()

	def closeEvent(self,event):
		reply = QMessageBox.question(self, 'Message','Voulez-vous vraiment quitter ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	
	def cameraCall(self):
		os.system('python test_camera.py')
	@pyqtSlot()
	def runAlgo(self):
		os.system('python reconnaitre.py')
		self.display.setText(usedVar)
		
		

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = RecoFaciale()
	sys.exit(app.exec_())