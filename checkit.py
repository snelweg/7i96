def config(parent):
	configErrors = []
	print(parent.configName)
	"""
	if not parent.configName.text():
		configErrors.append('A configuration name must be entered')
	else:
		print(parent.configName.text())

"""

	if configErrors:
		config.result = '\n'.join(configErrors)
		return False
	else:
		config.result = 'Configuration checked OK'
		return True
