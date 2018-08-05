import os
from datetime import datetime

def buildini(parent):
	buildErrors = []
	buildini.result = ''
	configPath = os.path.join(parent.configsDir, parent.configName.text())
	iniFilePath = os.path.join(configPath, parent.configName.text() + '.ini')
	if not os.path.exists(configPath):
		os.mkdir(configPath)

	iniContents = ['# This file was created with the 7i96 Wizard on ']
	iniContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	iniContents.append('# If you make changes to this file your screwed\n')

	# build the [EMC] section
	iniContents.append('\n[EMC]\n')
	iniContents.append('VERSION = {}\n'.format(parent.version.text()))
	iniContents.append('MACHINE = {}\n'.format(parent.configName.text()))
	iniContents.append('DEBUG = {}\n'.format(parent.debugCombo.itemData(parent.debugCombo.currentIndex())))

	# build the [HOSTMOT2] section
	iniContents.append('\n[HOSTMOT2]\n')
	iniContents.append('DRIVER = {}\n'.format('hm2_eth'))
	iniContents.append('IPADDRESS = {}\n'.format(parent.ipAddressCB.itemData(parent.ipAddressCB.currentIndex())))
	iniContents.append('BOARD = {}\n'.format(parent.boardCB.itemData(parent.boardCB.currentIndex())))
	iniContents.append('STEPGENS = {}\n'.format(str(parent.stepgensSB.value())))
	iniContents.append('ENCODERS = {}\n'.format(str(parent.encodersSB.value())))
	iniContents.append('SSERIAL_PORT = {}\n'.format(str(parent.sserialSB.value())))

	# build the [DISPLAY] section maxFeedOverrideLE
	iniContents.append('\n[DISPLAY]\n')
	iniContents.append('DISPLAY = {}\n'.format(parent.guiCB.itemData(parent.guiCB.currentIndex())))
	iniContents.append('POSITION_OFFSET = {}\n'.format(parent.positionOffsetCB.itemData(parent.positionOffsetCB.currentIndex())))
	iniContents.append('POSITION_FEEDBACK = {}\n'.format(parent.positionFeedbackCB.itemData(parent.positionFeedbackCB.currentIndex())))
	iniContents.append('CYCLE_TIME = {}\n'.format('0.1'))
	iniContents.append('INTRO_GRAPHIC = {}\n'.format('emc2.gif'))
	iniContents.append('INTRO_TIME = {}\n'.format('0'))
	iniContents.append('OPEN_FILE = "{}"\n'.format(''))

	# build the [KINS] section
	iniContents.append('\n[KINS]\n')
	iniContents.append('KINEMATICS = {}\n'.format('trivkins'))
	iniContents.append('JOINTS = {}\n'.format(len(parent.coordinatesL.text())))

	# build the [EMCIO] section
	iniContents.append('\n[EMCIO]\n')
	iniContents.append('EMCIO = {}\n'.format('io'))
	iniContents.append('CYCLE_TIME = {}\n'.format('0.100'))
	iniContents.append('TOOL_TABLE = {}.tbl\n'.format(parent.configNameUnderscored))

	# build the [RS274NGC] section
	iniContents.append('\n[RS274NGC]\n')
	iniContents.append('PARAMETER_FILE = {}.var\n'.format(parent.configNameUnderscored))

	# build the [EMCMOT] section
	iniContents.append('\n[EMCMOT]\n')
	iniContents.append('EMCMOT = {}\n'.format('motmod'))
	iniContents.append('SERVO_PERIOD = {}\n'.format('1000000'))

	# build the [TASK] section
	iniContents.append('\n[TASK]\n')
	iniContents.append('TASK = {}\n'.format('milltask'))
	iniContents.append('CYCLE_TIME = {}\n'.format('0.010'))

	# build the [TRAJ] section
	iniContents.append('\n[TRAJ]\n')
	iniContents.append('COORDINATES = {}\n'.format(parent.coordinatesL.text()))
	iniContents.append('LINEAR_UNITS = {}\n'.format(parent.linearUnitsCB.itemData(parent.linearUnitsCB.currentIndex())))
	iniContents.append('ANGULAR_UNITS = {}\n'.format(parent.angularUnitsCB.itemData(parent.angularUnitsCB.currentIndex())))

	# build the [HAL] section
	iniContents.append('\n[HAL]\n')
	iniContents.append('HALFILE = {}.hal\n'.format(parent.configNameUnderscored))

	# build the [HALUI] section
	iniContents.append('\n[HALUI]\n')

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'X':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_X]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'Y':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_Y]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'Z':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_Z]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'A':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_A]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'B':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_B]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'C':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_C]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'U':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_U]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'V':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_V]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'W':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_W]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	with open(iniFilePath, 'w') as iniFile:
		iniFile.writelines(iniContents)
	buildini.result = 'Sucess {} file was created'.format(iniFilePath)
	return True
	"""


	if data['RS274NGC']['RS274NGC_STARTUP_CODE']:
		iniContents.append('RS274NGC_STARTUP_CODE = {}\n'.format(data['RS274NGC']['RS274NGC_STARTUP_CODE']))
	if data['RS274NGC']['SUBROUTINE_PATH']:
		iniContents.append('SUBROUTINE_PATH = {}\n'.format(data['RS274NGC']['SUBROUTINE_PATH']))
	if data['RS274NGC']['USER_M_PATH']:
		iniContents.append('USER_M_PATH = {}\n'.format(data['RS274NGC']['USER_M_PATH']))

	# build the [TRAJ] section
	iniContents.append('\n[TRAJ]\n')
	iniContents.append('COORDINATES = {}\n'.format(data['TRAJ']['COORDINATES']))
	iniContents.append('LINEAR_UNITS = {}\n'.format(data['TRAJ']['LINEAR_UNITS']))
	iniContents.append('ANGULAR_UNITS = {}\n'.format(data['TRAJ']['ANGULAR_UNITS']))

	if data['HAL']['HALUI']:
		iniContents.append('HALUI = {}\n'.format(data['HAL']['HALUI']))
	if data['HAL']['POSTGUI_HALFILE']:
		iniContents.append('POSTGUI_HALFILE = {}\n'.format(data['HAL']['POSTGUI_HALFILE']))
	if data['HAL']['SHUTDOWN']:
		iniContents.append('SHUTDOWN = {}\n'.format(data['HAL']['SHUTDOWN']))


	if data['HALUI']['MDI_COMMAND']:
		iniContents.append('MDI_COMMAND = {}\n'.format(data['HALUI']['MDI_COMMAND']))

	# build the [JOINT_0] section
	if data['JOINT_0']['ENABLED']:
		iniContents.append('\n[JOINT_0]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_0']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_0']['SCALE']))

	# build the [JOINT_1] section
	if data['JOINT_1']['ENABLED']:
		iniContents.append('\n[JOINT_1]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_1']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_1']['SCALE']))

	# build the [JOINT_2] section
	if data['JOINT_2']['ENABLED']:
		iniContents.append('\n[JOINT_2]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_2']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_2']['SCALE']))

	# build the [JOINT_3] section
	if data['JOINT_3']['ENABLED']:
		iniContents.append('\n[JOINT_3]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_3']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_3']['SCALE']))

	# build the [JOINT_4] section
	if data['JOINT_4']['ENABLED']:
		iniContents.append('\n[JOINT_4]\n')
		iniContents.append('AXIS = {}\n'.format(data['JOINT_4']['AXIS']))
		iniContents.append('SCALE = {}\n'.format(data['JOINT_4']['SCALE']))

	# build the [AXIS_X] section
	if data['AXIS_X']['ENABLED']:
		iniContents.append('\n[AXIS_X]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_X']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_X']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_X']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_X']['MAX_ACCELERATION']))

	# build the [AXIS_Y] section
	if data['AXIS_Y']['ENABLED']:
		iniContents.append('\n[AXIS_Y]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_Y']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_Y']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_Y']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_Y']['MAX_ACCELERATION']))

	# build the [AXIS_Z] section
	if data['AXIS_Z']['ENABLED']:
		iniContents.append('\n[AXIS_Z]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_Z']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_Z']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_Z']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_Z']['MAX_ACCELERATION']))

	# build the [AXIS_A] section
	if data['AXIS_A']['ENABLED']:
		iniContents.append('\n[AXIS_A]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_A']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_A']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_A']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_A']['MAX_ACCELERATION']))

	# build the [AXIS_B] section
	if data['AXIS_B']['ENABLED']:
		iniContents.append('\n[AXIS_B]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_B']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_B']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_B']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_B']['MAX_ACCELERATION']))

	# build the [AXIS_C] section
	if data['AXIS_C']['ENABLED']:
		iniContents.append('\n[AXIS_C]\n')
		iniContents.append('MIN_LIMIT = {}\n'.format(data['AXIS_C']['MIN_LIMIT']))
		iniContents.append('MAX_LIMIT = {}\n'.format(data['AXIS_C']['MAX_LIMIT']))
		iniContents.append('MAX_VELOCITY = {}\n'.format(data['AXIS_C']['MAX_VELOCITY']))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(data['AXIS_C']['MAX_ACCELERATION']))

	# build the [AXIS_U] section

	# build the [AXIS_V] section

	# build the [AXIS_W] section
"""


	#print(iniFileName)
	# for now just write over the file if it exists.
	# fuck the configparser just fucking write the file...
	
	#config = configparser.ConfigParser(strict=False, allow_no_value=True)
	#config.optionxform = str
	#config.sections()
	#config['INFORMATION'] = '# This file was created by the 7i96 Wizard'
	#config['EMC'] = {'MACHINE' : data['EMC']['MACHINE'],
	#								'DEBUG' : '0x00000000'}

	#with open(iniFileName, 'w') as configfile:
	#	config.write(configfile)

	#print(data['EMC']['MACHINE'])
	
	



	"""
	if data['EMC']['MACHINE']: # might just check this before calling buildini
	
	iniContents.append('\n[]\n')
	iniContents.append(' = \n'.format(data['']['']))

"""

def buildHal(data, path, name):
	halFileName = os.path.join(path, name + '.hal')
	halContents = []
	halContents.append('# kinematics\n')
	halContents.append('loadrt [KINS]KINEMATICS\n')
	halContents.append('\n')
	halContents.append('# motion controller\n')
	halContents.append('loadrt [EMCMOT]EMCMOT ')
	halContents.append('servo_period_nsec=[EMCMOT]SERVO_PERIOD ')
	halContents.append('num_joints=[KINS]JOINTS\n')
	halContents.append('\n')
	halContents.append('# standard components\n')
	# this needs to be calculated by how many axies are enabled
	halContents.append('loadrt pid num_chan=4 \n')
	halContents.append('\n')
	halContents.append('# hostmot2 driver\n')
	halContents.append('loadrt hostmot2\n')
	halContents.append('\n')
	halContents.append('# load low-level driver\n')
	halContents.append('loadrt [HOSTMOT2](DRIVER) ')
	halContents.append('board_ip=[HOSTMOT2](IP) ')
	halContents.append('config=[HOSTMOT2](CONFIG)\n')
	halContents.append('\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.watchdog.timeout_ns 25000000\n')
	halContents.append('\n')
	halContents.append('# THREADS\n')
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.read servo-thread\n')
	halContents.append('addf motion-command-handler servo-thread\n')
	halContents.append('addf motion-controller servo-thread\n')
	halContents.append('addf pid.0.do-pid-calcs servo-thread\n')
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.write servo-thread\n')

	with open(halFileName, 'w') as iniFile:
		iniFile.writelines(halContents)

	buildHal.result = ''	
	return True
