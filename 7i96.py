#!/usr/bin/python3
# -*- coding: utf-8 -*-

version = 0.8

import sys, os, configparser
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QLineEdit)
import setup, loadini

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi("7i96.ui", self)
		self.config = configparser.ConfigParser(strict=False)
		self.linuxcncDir = os.path.expanduser('~/linuxcnc')
		self.configsDir = os.path.expanduser('~/linuxcnc/configs')

		self.buildWidgets()

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
		pass

	@pyqtSlot()
	def on_actionBuild_triggered(self):
		pass

	@pyqtSlot()
	def on_actionSaveAs_triggered(self):
		 print('File Save As')

	@pyqtSlot()
	def on_actionExit_triggered(self):
		exit()

	def buildWidgets(self):
		for item in setup.setupCombo('ipCombo'):
			self.ipCombo.addItem(item[0], item[1])
		#print(setup.setupCombo('ipCombo'))
		for i in range(5):
			for item in setup.setupCombo('axis'):
				eval('self.axis_' + str(i)).addItem(item[0], item[1])
		for i in range(5):
			for item in setup.setupCombo('direction'):
				eval('self.stepDir_' + str(i)).addItem(item[0], item[1])
		for i in range(11):
			for item in setup.setupCombo('input'):
				eval('self.input_' + str(i)).addItem(item[0], item[1])
		for i in range(5):
			for item in setup.setupCombo('output'):
				eval('self.output_' + str(i)).addItem(item[0], item[1])
		for i in range(11):
			for item in setup.setupCombo('axis'):
				eval('self.inputaxis_' + str(i)).addItem(item[0], item[1])

	def iniLoad(self):
		# iniList section, item, value
		for item in loadini.iniList():
			if self.config.has_option(item[0], item[1]):
				if isinstance(eval('self.' + item[2]), QLineEdit):
					eval('self.' + item[2]).setText(self.config[item[0]][item[1]])

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())
