#from subprocess import PIPE, run
#import sys, subprocess
#from subprocess import check_output, CalledProcessError, STDOUT
import sys, subprocess

def check(parent):

	if parent.ipAddressCB.currentText() == 'None':
		parent.testConnectionLB.setText('An IP address must be selected')
		return
	ipAddress = parent.ipAddressCB.currentText()

	if sys.maxsize > 2**32:
		mesaflash = "./mesaflash64"
	else:
		mesaflash = "./mesaflash32"
	command = [mesaflash, "--device", "7i96", "--addr", ipAddress, "--readhmid"]

	try:
		output = subprocess.check_output(command, stderr=subprocess.PIPE)
		parent.testConnectionLB.setText(output.decode(sys.getfilesystemencoding()))
	except subprocess.CalledProcessError as e:
		#print('exit code: {}'.format(e.returncode))
		#print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
		parent.testConnectionLB.setText(e.output.decode(sys.getfilesystemencoding()))


