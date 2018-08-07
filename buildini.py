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
	iniContents.append('# Changes to most things are ok and will be read by the wizard\n')

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
	iniContents.append('MAX_LINEAR_VELOCITY = {}\n'.format(parent.maxLinearVelocity.text()))

	# build the [HAL] section
	iniContents.append('\n[HAL]\n')
	iniContents.append('HALFILE = {}.hal\n'.format(parent.configNameUnderscored))
	iniContents.append('HALFILE = io.hal\n')
	iniContents.append('HALFILE = custom.hal\n')
	iniContents.append('HALFILE = postgui.hal\n')

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
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_0.itemData(parent.axisCB_0.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_0.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_0.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_0.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_0.text()))
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
		iniContents.append('HOME = {}\n'.format(parent.home_0.text()))
		iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_0.text()))
		iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_0.text()))
		iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_0.text()))
		iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_0.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_0.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_0.isChecked()))


	# build the [JOINT_1] section
	if parent.axisCB_1.itemData(parent.axisCB_1.currentIndex()):
		iniContents.append('\n[JOINT_1]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_1.itemData(parent.axisCB_1.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_1.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_1.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_1.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_1.text()))
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
		iniContents.append('FF0 = {}\n'.format(parent.ff0_1.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_1.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_1.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_1.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_1.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_1.text()))
		iniContents.append('HOME = {}\n'.format(parent.home_1.text()))
		iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_1.text()))
		iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_1.text()))
		iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_1.text()))
		iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_1.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_1.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_1.isChecked()))

	# build the [JOINT_2] section
	if parent.axisCB_2.itemData(parent.axisCB_2.currentIndex()):
		iniContents.append('\n[JOINT_2]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_2.itemData(parent.axisCB_2.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_2.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_2.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_2.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_2.text()))
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
		iniContents.append('FF0 = {}\n'.format(parent.ff0_2.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_2.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_2.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_2.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_2.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_2.text()))
		iniContents.append('HOME = {}\n'.format(parent.home_2.text()))
		iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_2.text()))
		iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_2.text()))
		iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_2.text()))
		iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_2.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_2.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_2.isChecked()))

	# build the [JOINT_3] section
	if parent.axisCB_3.itemData(parent.axisCB_3.currentIndex()):
		iniContents.append('\n[JOINT_3]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_3.itemData(parent.axisCB_3.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_3.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_3.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_3.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_3.text()))
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
		iniContents.append('FF0 = {}\n'.format(parent.ff0_3.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_3.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_3.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_3.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_3.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_3.text()))
		iniContents.append('HOME = {}\n'.format(parent.home_3.text()))
		iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_3.text()))
		iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_3.text()))
		iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_3.text()))
		iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_3.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_3.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_3.isChecked()))

	# build the [JOINT_4] section
	if parent.axisCB_4.itemData(parent.axisCB_4.currentIndex()):
		iniContents.append('\n[JOINT_4]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_4.itemData(parent.axisCB_4.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_4.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_4.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_4.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_4.text()))
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
		iniContents.append('FF0 = {}\n'.format(parent.ff0_4.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_4.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_4.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_4.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_4.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_4.text()))
		iniContents.append('HOME = {}\n'.format(parent.home_4.text()))
		iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_4.text()))
		iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_4.text()))
		iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_4.text()))
		iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_4.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_4.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_4.isChecked()))

	# build the [INPUTS] section
	iniContents.append('\n[INPUTS]\n')
	iniContents.append('# DO NOT change the input text\n')
	iniContents.append('INPUT_0 = {}\n'.format(parent.input_0.currentText()))
	iniContents.append('INPUT_JOINT_0 = {}\n'.format(parent.inputJoint_0.currentText()))
	iniContents.append('INPUT_1 = {}\n'.format(parent.input_1.currentText()))
	iniContents.append('INPUT_JOINT_1 = {}\n'.format(parent.inputJoint_1.currentText()))
	iniContents.append('INPUT_2 = {}\n'.format(parent.input_2.currentText()))
	iniContents.append('INPUT_JOINT_2 = {}\n'.format(parent.inputJoint_2.currentText()))
	iniContents.append('INPUT_3 = {}\n'.format(parent.input_3.currentText()))
	iniContents.append('INPUT_JOINT_3 = {}\n'.format(parent.inputJoint_3.currentText()))
	iniContents.append('INPUT_4 = {}\n'.format(parent.input_4.currentText()))
	iniContents.append('INPUT_JOINT_4 = {}\n'.format(parent.inputJoint_4.currentText()))
	iniContents.append('INPUT_5 = {}\n'.format(parent.input_5.currentText()))
	iniContents.append('INPUT_JOINT_5 = {}\n'.format(parent.inputJoint_5.currentText()))
	iniContents.append('INPUT_6 = {}\n'.format(parent.input_6.currentText()))
	iniContents.append('INPUT_JOINT_6 = {}\n'.format(parent.inputJoint_6.currentText()))
	iniContents.append('INPUT_7 = {}\n'.format(parent.input_7.currentText()))
	iniContents.append('INPUT_JOINT_7 = {}\n'.format(parent.inputJoint_7.currentText()))
	iniContents.append('INPUT_8 = {}\n'.format(parent.input_8.currentText()))
	iniContents.append('INPUT_JOINT_8 = {}\n'.format(parent.inputJoint_8.currentText()))
	iniContents.append('INPUT_9 = {}\n'.format(parent.input_9.currentText()))
	iniContents.append('INPUT_JOINT_9 = {}\n'.format(parent.inputJoint_9.currentText()))
	iniContents.append('INPUT_10 = {}\n'.format(parent.input_10.currentText()))
	iniContents.append('INPUT_JOINT_10 = {}\n'.format(parent.inputJoint_10.currentText()))


	# build the [OUTPUTS] section
	iniContents.append('\n[OUTPUTS]\n')
	iniContents.append('# DO NOT change the output text\n')
	iniContents.append('OUTPUT_0 = {}\n'.format(parent.output_0.currentText()))
	iniContents.append('OUTPUT_1 = {}\n'.format(parent.output_1.currentText()))
	iniContents.append('OUTPUT_2 = {}\n'.format(parent.output_2.currentText()))
	iniContents.append('OUTPUT_3 = {}\n'.format(parent.output_3.currentText()))
	iniContents.append('OUTPUT_4 = {}\n'.format(parent.output_4.currentText()))


	with open(iniFilePath, 'w') as iniFile:
		iniFile.writelines(iniContents)
	buildini.result = 'Sucess {} file was created'.format(iniFilePath)
	return True
