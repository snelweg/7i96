import os
from datetime import datetime

def buildio(parent):
	configPath = os.path.join(parent.configsDir, parent.configName.text())
	ioFilePath = os.path.join(configPath, 'io.hal')
	ioContents = []
	ioContents = ['# This file was created with the 7i96 Wizard on ']
	ioContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	ioContents.append('# If you make changes to this file your screwed\n\n')

	# build the inputs
	for index in range(11):
		inputText = getattr(parent, 'input_' + str(index)).currentText()
		inputJoint = getattr(parent, 'inputJoint_' + str(index)).currentData()
		if inputText == 'Home':
			ioContents.append('net home-joint-{0} joint.{0}.home-sw-in <= hm2_7i96.0.gpio.00{1}.in\n'.format(inputJoint, index))
		elif inputText == 'Both Limit':
			ioContents.append('net limits-joint-{0} joint.{0}.neg-lim-sw-in <= hm2_7i96.0.gpio.00{1}.in\n'.format(inputJoint, index))
			ioContents.append('net limits-joint-{0} joint.{0}.pos-lim-sw-in\n'.format(inputJoint))
		elif inputText == 'Min Limit':
			ioContents.append('net min-limit-joint-{0} joint.{0}.neg-lim-sw-in <= hm2_7i96.0.gpio.00{1}.in\n'.format(inputJoint, index))
		elif inputText == 'Max Limit':
			ioContents.append('net max-limit-joint-{0} joint.{0}.pos-lim-sw-in <= hm2_7i96.0.gpio.00{1}.in\n'.format(inputJoint, index))
		elif inputText == 'Home & Limit':
			ioContents.append('net home-limit-joint-{0} joint.{0}.home-sw-in <= hm2_7i96.0.gpio.00{1}.in\n'.format(inputJoint, index))
			ioContents.append('net home-limit-joint-{0} joint.{0}.neg-lim-sw-in\n'.format(inputJoint))
			ioContents.append('net home-limit-joint-{0} joint.{0}.pos-lim-sw-in\n'.format(inputJoint))
		elif inputText == 'Min Limit & Home':
			ioContents.append('net min-limit-home-joint-{0} joint.{0}.neg-lim-sw-in <= hm2_7i96.0.gpio.00{1}.in\n'.format(inputJoint, index))
			ioContents.append('net min-limit-home-limit-joint-{0} joint.{0}.neg-lim-sw-in\n'.format(inputJoint))
		elif inputText == 'Max Limit & Home':
			ioContents.append('net max-limit-home-joint-{0} joint.{0}.pos-lim-sw-in <= hm2_7i96.0.gpio.00{1}.in\n'.format(inputJoint, index))
			ioContents.append('net max-limit-home-limit-joint-{0} joint.{0}.neg-lim-sw-in\n'.format(inputJoint))
		elif inputText == 'Probe':
			ioContents.append('net probe-input motion.probe-input <= hm2_7i96.0.gpio.00{}.in\n'.format(index))
		elif inputText == 'Digital In 0':
			ioContents.append('net digital-input-0 motion.digital-in-00 <= hm2_7i96.0.gpio.00{}.in\n'.format(index))
		elif inputText == 'Digital In 1':
			ioContents.append('net digital-input-1 motion.digital-in-01 <= hm2_7i96.0.gpio.00{}.in\n'.format(index))
		elif inputText == 'Digital In 2':
			ioContents.append('net digital-input-2 motion.digital-in-02 <= hm2_7i96.0.gpio.00{}.in\n'.format(index))
		elif inputText == 'Digital In 3':
			ioContents.append('net digital-input-3 motion.digital-in-03 <= hm2_7i96.0.gpio.00{}.in\n'.format(index))

	# build the outputs
	for index in range(5):
		outputText = getattr(parent, 'output_' + str(index)).currentText()
		if outputText == 'Coolant Flood':
			ioContents.append('net flood-output iocontrol.0.coolant-flood => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
			print('here')
		if outputText == 'Coolant Mist':
			ioContents.append('net flood-output iocontrol.0.coolant-mist => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle On':
			ioContents.append('net spindle-on motion.spindle-on => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle CW':
			ioContents.append('net spindle-cw motion.spindle-forward => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle CCW':
			ioContents.append('net spindle-ccw motion.spindle-reverse => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle Brake':
			ioContents.append('net spindle-brake motion.spindle-brake => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'E-Stop Out':
			ioContents.append('net estop-loop hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 0':
			ioContents.append('net digital-out-0 motion.digital-out-00 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 1':
			ioContents.append('net digital-out-2 motion.digital-out-01 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 2':
			ioContents.append('net digital-out-2 motion.digital-out-02 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 3':
			ioContents.append('net digital-out-3 motion.digital-out-03 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))

	with open(ioFilePath, 'w') as ioFile:
		ioFile.writelines(ioContents)
	return True

