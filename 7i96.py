#!/usr/bin/python3
# -*- coding: utf-8 -*-

version = 0.8

import sys, os, configparser
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QLineEdit,
	QSpinBox, QCheckBox, QComboBox, QLabel)
import setup, loadini, checkit, buildini, buildhal
from dialog import Ui_Dialog as errorDialog

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi("7i96.ui", self)
		self.config = configparser.ConfigParser(strict=False)
		self.linuxcncDir = os.path.expanduser('~/linuxcnc')
		self.configsDir = os.path.expanduser('~/linuxcnc/configs')
		self.configNameUnderscored = ''
		self.checkConfig = checkit.config
		self.buildini = buildini.buildini
		self.buildhal = buildhal.buildhal
		self.buildCB()
		self.setupConnections()
		self.axisList = ['axisCB_0', 'axisCB_1', 'axisCB_2', 'axisCB_3', 'axisCB_4']
		self.show()


	# Auto connected menu action callbacks
	@pyqtSlot()
	def on_actionFileNew_triggered(self):
		print('File New')

	@pyqtSlot()
	def on_actionOpen_triggered(self):
		if not os.path.isdir(self.configsDir):
			self.configsDir = os.path.expanduser('~/')
		fileName = QFileDialog.getOpenFileName(self,
		caption="Select Configuration INI File", directory=self.configsDir,
		filter='*.ini', options=QFileDialog.DontUseNativeDialog,)
		if fileName:
			iniFile = (fileName[0])
			if self.config.read(iniFile):
				self.iniLoad()

	@pyqtSlot()
	def on_actionSave_triggered(self):
		pass

	@pyqtSlot()
	def on_actionAbout_triggered(self):
		pass

	@pyqtSlot()
	def on_actionCheck_triggered(self):
		if self.checkConfig(self):
			print('OkDokey')
		else:
			self.dialog(self.checkConfig.result)

	@pyqtSlot()
	def on_actionBuild_triggered(self):
		self.buildini(self)
		self.buildhal(self)

	@pyqtSlot()
	def on_actionSaveAs_triggered(self):
		 print('File Save As')

	@pyqtSlot()
	def on_actionExit_triggered(self):
		exit()

	def setupConnections(self):
		self.configName.textChanged[str].connect(self.onConfigNameChanged)
		self.axisCB_0.currentIndexChanged.connect(self.onAxisChanged)
		self.axisCB_1.currentIndexChanged.connect(self.onAxisChanged)
		self.axisCB_2.currentIndexChanged.connect(self.onAxisChanged)
		self.axisCB_3.currentIndexChanged.connect(self.onAxisChanged)
		self.axisCB_4.currentIndexChanged.connect(self.onAxisChanged)

	def onConfigNameChanged(self, text):
		# update the iniDictionary when text is changed
		if text:
			self.configNameUnderscored = text.replace(' ','_')
			self.configPath = self.configsDir + '/' + self.configNameUnderscored
			self.pathLabel.setText(self.configPath)
		else:
			self.pathLabel.setText('')

	def onAxisChanged(self):
		coordList = []
		for item in self.axisList:
			if getattr(self,item).itemData(getattr(self,item).currentIndex()):
				jointTab = getattr(self,item).objectName()[7]
				axisLetter = getattr(self,item).itemData(getattr(self,item).currentIndex())
				coordList.append(axisLetter)
				if axisLetter in ['X', 'Y', 'Z']:
					getattr(self, 'axisType_' + jointTab).setText('LINEAR')
				else:
					getattr(self, 'axisType_' + jointTab).setText('ANGULAR')
		self.coordinatesL.setText(''.join(coordList))


	def buildCB(self):
		for item in setup.setupCombo('ipAddress'):
			self.ipAddressCB.addItem(item[0], item[1])
		for item in setup.setupCombo('board'):
			self.boardCB.addItem(item[0], item[1])
		for item in setup.setupCombo('driver'):
			self.driverCB.addItem(item[0], item[1])
		for item in setup.setupCombo('display'):
			self.guiCB.addItem(item[0], item[1])
		for item in setup.setupCombo('linearUnits'):
			self.linearUnitsCB.addItem(item[0], item[1])
		for item in setup.setupCombo('angularUnits'):
			self.angularUnitsCB.addItem(item[0], item[1])
		for item in setup.setupCombo('positionOffset'):
			self.positionOffsetCB.addItem(item[0], item[1])
		for item in setup.setupCombo('positionFeedback'):
			self.positionFeedbackCB.addItem(item[0], item[1])


		for i in range(5):
			for item in setup.setupCombo('axis'):
				getattr(self, 'axisCB_' + str(i)).addItem(item[0], item[1])
		for i in range(5):
			for item in setup.setupCombo('direction'):
				getattr(self, 'stepDir_' + str(i)).addItem(item[0], item[1])
		for i in range(11):
			for item in setup.setupCombo('input'):
				getattr(self, 'input_' + str(i)).addItem(item[0], item[1])
		for i in range(5):
			for item in setup.setupCombo('output'):
				getattr(self, 'output_' + str(i)).addItem(item[0], item[1])
		for i in range(11):
			for item in setup.setupCombo('axis'):
				getattr(self, 'inputaxis_' + str(i)).addItem(item[0], item[1])
		for item in setup.setupCombo('debug'):
			self.debugCombo.addItem(item[0], item[1])

	def iniLoad(self):
		# iniList section, item, value
		for item in loadini.iniList():
			if self.config.has_option(item[0], item[1]):
				if isinstance(getattr(self, item[2]), QLabel):
					getattr(self, item[2]).setText(self.config[item[0]][item[1]])
				if isinstance(getattr(self, item[2]), QLineEdit):
					getattr(self, item[2]).setText(self.config[item[0]][item[1]])
				if isinstance(getattr(self, item[2]), QSpinBox):
					getattr(self, item[2]).setValue(int(self.config[item[0]][item[1]]))
				if isinstance(getattr(self, item[2]), QCheckBox):
					#print(self.config[item[0]][item[1]])
					if self.config[item[0]][item[1]] in ['YES', 'yes']:
						getattr(self, item[2]).setChecked(True)
					else:
						getattr(self, item[2]).setChecked(False)
				if isinstance(getattr(self, item[2]), QComboBox):
					index = getattr(self, item[2]).findData(self.config[item[0]][item[1]])
					getattr(self, item[2]).setCurrentIndex(index)

	def dialog(self, text):
		dialog = QtWidgets.QDialog()
		dialog.ui = errorDialog()
		dialog.ui.setupUi(dialog)
		#dialog.ui.windowTitle('Configuration Errors')
		dialog.ui.label.setText(text)
		dialog.exec_()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())
