#from subprocess import PIPE, run
#import sys, subprocess
#from subprocess import check_output, CalledProcessError, STDOUT
import sys, subprocess

def check(parent):

	if parent.ipAddressCB.currentText() == 'None':
		parent.testConnectionLB.setText('An IP address must be selected')


	if sys.maxsize > 2**32:
		command = ["./mesaflash64", "--device", "7i96", "--addr", "10.10.10.10", "--readhmid"]
	else:
		command = ["./mesaflash32", "--device", "7i96", "--addr", "10.10.10.10", "--readhmid"]

	try:
		output = subprocess.check_output(command, stderr=subprocess.PIPE)
		parent.testConnectionLB.setText(output)
	except subprocess.CalledProcessError as e:
		print('exit code: {}'.format(e.returncode))
		print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
		parent.testConnectionLB.setText(e.output.decode(sys.getfilesystemencoding()))


