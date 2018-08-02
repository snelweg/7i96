def config(parent):
	configErrors = []
	if not parent.configName.text():
		configErrors.append('A configuration name must be entered')



	if configErrors:
		config.result = '\n'.join(configErrors)
		return False
	else:
		config.result = 'Configuration checked OK'
		return True
