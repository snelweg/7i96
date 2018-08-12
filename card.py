import subprocess

def check(parent):
	print('checking the card')
	result = subprocess.call(["./mesaflash", "--device", "7i96", "--addr", "10.10.10.10", "--readhmid"])
	print(result)


"""
try:
    subprocess.check_output("dir /f",shell=True,stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

subprocess.CalledProcessError returned non-zero exit status

"""
