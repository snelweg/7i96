import os, sys, subprocess
from PyQt5.QtWidgets import QInputDialog, QLineEdit

def check(parent):

	if parent.ipAddressCB.currentText() == 'None':
		parent.testConnectionLB.setText('An IP address must be selected')
		return 'An IP address must be selected'
	ipAddress = parent.ipAddressCB.currentText()

	if sys.maxsize > 2**32:
		mesaflash = "./mesaflash64"
	else:
		mesaflash = "./mesaflash32"
	command = [mesaflash, "--device", "7i96", "--addr", ipAddress, "--readhmid"]

	try:
		output = subprocess.check_output(command, stderr=subprocess.PIPE)
		parent.testConnectionLB.setText(output.decode(sys.getfilesystemencoding()))
		return output.decode(sys.getfilesystemencoding())
	except subprocess.CalledProcessError as e:
		#print('exit code: {}'.format(e.returncode))
		#print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
		parent.testConnectionLB.setText(e.output.decode(sys.getfilesystemencoding()))
		return e.output.decode(sys.getfilesystemencoding())

def flashCard(parent):
	if not parent.firmwareCB.currentData():
		parent.testConnectionLB.setText('A firmware must be selected')
		return

	if parent.is64bit:
		command = os.path.join(parent.cwd, 'mesaflash64')
	else:
		command = os.path.join(parent.cwd, 'mesaflash32')
	proc = subprocess.Popen(['/usr/bin/pkexec', command])


	#text, ok = QInputDialog.getText(None, "Flash", "User Password Needed!")
	#if ok and text:
	#	print("password={}".format(text))


def reloadCard(parent):
	print('reloading')
