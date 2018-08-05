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

	# build the [JOINT_0] section
	if parent.axisCB_0.itemData(parent.axisCB_0.currentIndex()):
		iniContents.append('\n[JOINT_0]\n')
		iniContents.append('TYPE = {}\n'.format(parent.axisType_0.text()))
		iniContents.append('SCALE = {}\n'.format(str(parent.scale_0.value())))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(int(parent.maxVelocity_0.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(int(parent.maxAccel_0.text()) * 1.2)))
		iniContents.append('FERROR = {}\n'.format('0.0002'))
		iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_0.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_0.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_0.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_0.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_0.text()))
		iniContents.append('P = {}\n'.format(parent.p_0.text()))
		iniContents.append('I = {}\n'.format(parent.i_0.text()))
		iniContents.append('D = {}\n'.format(parent.d_0.text()))
		iniContents.append('FF0 = {}\n'.format(parent.ff0_0.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_0.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_0.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_0.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_0.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_0.text()))

	# build the [JOINT_1] section
	if parent.axisCB_1.itemData(parent.axisCB_1.currentIndex()):
		iniContents.append('\n[JOINT_1]\n')
		iniContents.append('TYPE = {}\n'.format(parent.axisType_1.text()))
		iniContents.append('SCALE = {}\n'.format(str(parent.scale_1.value())))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(int(parent.maxVelocity_1.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(int(parent.maxAccel_1.text()) * 1.2)))
		iniContents.append('FERROR = {}\n'.format('0.0002'))
		iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_1.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_1.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_1.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_1.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_1.text()))
		iniContents.append('P = {}\n'.format(parent.p_1.text()))
		iniContents.append('I = {}\n'.format(parent.i_1.text()))
		iniContents.append('D = {}\n'.format(parent.d_1.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff0_1.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_1.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_1.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_1.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_1.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_1.text()))

	# build the [JOINT_2] section
	if parent.axisCB_2.itemData(parent.axisCB_2.currentIndex()):
		iniContents.append('\n[JOINT_2]\n')
		iniContents.append('TYPE = {}\n'.format(parent.axisType_2.text()))
		iniContents.append('SCALE = {}\n'.format(str(parent.scale_2.value())))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(int(parent.maxVelocity_2.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(int(parent.maxAccel_2.text()) * 1.2)))
		iniContents.append('FERROR = {}\n'.format('0.0002'))
		iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_2.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_2.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_2.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_2.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_2.text()))
		iniContents.append('P = {}\n'.format(parent.p_2.text()))
		iniContents.append('I = {}\n'.format(parent.i_2.text()))
		iniContents.append('D = {}\n'.format(parent.d_2.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff0_2.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_2.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_2.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_2.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_2.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_2.text()))

	# build the [JOINT_3] section
	if parent.axisCB_3.itemData(parent.axisCB_3.currentIndex()):
		iniContents.append('\n[JOINT_3]\n')
		iniContents.append('TYPE = {}\n'.format(parent.axisType_3.text()))
		iniContents.append('SCALE = {}\n'.format(str(parent.scale_3.value())))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(int(parent.maxVelocity_3.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(int(parent.maxAccel_3.text()) * 1.2)))
		iniContents.append('FERROR = {}\n'.format('0.0002'))
		iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_3.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_3.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_3.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_3.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_3.text()))
		iniContents.append('P = {}\n'.format(parent.p_3.text()))
		iniContents.append('I = {}\n'.format(parent.i_3.text()))
		iniContents.append('D = {}\n'.format(parent.d_3.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff0_3.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_3.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_3.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_3.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_3.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_3.text()))

	# build the [JOINT_4] section
	if parent.axisCB_4.itemData(parent.axisCB_4.currentIndex()):
		iniContents.append('\n[JOINT_4]\n')
		iniContents.append('TYPE = {}\n'.format(parent.axisType_4.text()))
		iniContents.append('SCALE = {}\n'.format(str(parent.scale_4.value())))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(int(parent.maxVelocity_4.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(int(parent.maxAccel_4.text()) * 1.2)))
		iniContents.append('FERROR = {}\n'.format('0.0002'))
		iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_4.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_4.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_4.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_4.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_4.text()))
		iniContents.append('P = {}\n'.format(parent.p_4.text()))
		iniContents.append('I = {}\n'.format(parent.i_4.text()))
		iniContents.append('D = {}\n'.format(parent.d_4.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff0_4.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_4.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_4.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_4.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_4.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_4.text()))

	with open(iniFilePath, 'w') as iniFile:
		iniFile.writelines(iniContents)
	buildini.result = 'Sucess {} file was created'.format(iniFilePath)
	return True

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
