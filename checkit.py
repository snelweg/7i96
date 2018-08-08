from PyQt5 import QtWidgets

def config(parent):
	configErrors = []
	qclip = QtWidgets.QApplication.clipboard()
	tabError = False
	nextHeader = 0

	# check the Machine Tab for errors
	if not parent.configName.text():
		tabError = True
		configErrors.append('\tA configuration name must be entered')
	if not parent.versionLE.text():
		tabError = True
		configErrors.append('\tA version must be entered, use 1.0')
	if parent.linearUnitsCB.currentText() == 'None':
		tabError = True
		configErrors.append('\tLinear Units must be selected')
	if parent.ipAddressCB.currentText() == 'None':
		tabError = True
		configErrors.append('\tAn IP address must be selected, 10.10.10.10 is recommended')

	if tabError:
		configErrors.insert(nextHeader, 'Machine Tab":')
		nextHeader = len(configErrors)
		print(nextHeader)
		tabError = False
	# end of Machine Tab

	# check the Display Tab for errors
	if parent.guiCB.currentText() == 'None':
		tabError = True
		configErrors.append('\tA GUI must be selected')
	if parent.positionOffsetCB.currentText() == 'None':
		tabError = True
		configErrors.append('\tA Position Offset must be selected')
	if parent.positionFeedbackCB.currentText() == 'None':
		tabError = True
		configErrors.append('\tA Position Feedback must be selected')
	if parent.maxFeedOverrideSB.value() == 0.0:
		tabError = True
		configErrors.append('\tThe Max Feed Override must be greater than zero, 1.2 is suggested')

	if tabError:
		configErrors.insert(nextHeader, 'Display Tab:')
		nextHeader = len(configErrors)
		print(nextHeader)
		tabError = False
	# end of Display Tab

	# check the Axis Tab for errors
	if len(parent.coordinatesLB.text()) == 0:
		tabError = True
		configErrors.append('\tAt least one Joint must be configured starting with Joint 0')

	if tabError:
		configErrors.insert(nextHeader, 'Axis Tab:')
		nextHeader = len(configErrors)
		print(nextHeader)
		tabError = False
	# end of Axis Tab


	if configErrors:
		config.result = '\n'.join(configErrors)
		#print(config.result)
		qclip.setText(config.result)
		return False
	else:
		config.result = 'Configuration checked OK'
		return True
