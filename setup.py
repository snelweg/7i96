def setupCombo(combo):
	comboList = []

	# might take a look at the data and see if we can simply use '10.10.10.10' format
	if combo == 'ipAddress':
		comboList = [['None', False],
								['10.10.10.10', '"10.10.10.10"'],
								['192.168.1.121', '"192.168.1.121"']]

	if combo == 'axis':
		comboList = [['None', False],
								['X', 'X'],
								['Y', 'Y'],
								['Z', 'Z'],
								['A', 'A'],
								['B', 'B'],
								['C', 'C'],
								['U', 'U'],
								['V', 'V'],
								['W', 'W']]

	if combo == 'joint':
		comboList = [['None', False],
								['Joint 0', '0'],
								['Joint 1', '1'],
								['Joint 2', '2'],
								['Joint 3', '3'],
								['Joint 4', '4']]

	if combo == 'direction':
		comboList = [['None', False],
								['CW', 'cw'],
								['CCW', 'ccw']]

	if combo == 'display':
		comboList = [['None', False],
								['Axis', 'axis'],
								['Touchy', 'touchy']]

	if combo == 'linearUnits':
		comboList = [['None', False],
								['Imperial', 'inch'],
								['Metric', 'metric']]

	if combo == 'angularUnits':
		comboList = [['Degree', 'degree'],]


	if combo == 'positionOffset':
		comboList = [['None', False],
								['Relative', 'RELATIVE'],
								['Machine', 'MACHINE'],]

	if combo == 'positionFeedback':
		comboList = [['None', False],
								['Commanded', 'COMMANDED'],
								['Actual', 'ACTUAL'],]

	if combo == 'input':
		comboList = [['None', False],
								['E-Stop In', 'E-Stop In'],
								['Home', 'Home'],
								['Both Limit', 'Both Limit'],
								['Min Limit', 'Min Limit'],
								['Max Limit', 'Max Limit'],
								['Home & Limit', 'Home & Limit'],
								['Min Limit & Home', 'Min Limit & Home'],
								['Max Limit & Home', 'Max Limit & Home'],
								['Probe', 'Probe'],
								['Digital In 0', 'Digital In 0'],
								['Digital In 1', 'Digital In 1'],
								['Digital In 2', 'Digital In 2'],
								['Digital In 3', 'Digital In 3']]

	if combo == 'output':
		comboList = [['None', False],
								['Coolant Flood', 'Coolant Flood'],
								['Coolant Mist', 'Coolant Mist'],
								['Spindle On', 'Spindle On'],
								['Spindle CW', 'Spindle CW'],
								['Spindle CCW', 'Spindle CCW'],
								['Spindle Brake', 'Spindle Brake'],
								['E-Stop Out', 'E-Stop Out'],
								['Digital Out 0', 'Digital Out 0'],
								['Digital Out 1', 'Digital Out 1'],
								['Digital Out 2', 'Digital Out 2'],
								['Digital Out 3', 'Digital Out 3']]

	if combo == 'debug':
		comboList = [['Debug Off', '0x00000000'],
								['Debug Configuration', '0x00000002'],
								['Debug Task Issues', '0x00000008'],
								['Debug NML', '0x00000010'],
								['Debug Motion Time', '0x00000040'],
								['Debug Interpreter', '0x00000080'],
								['Debug RCS', '0x00000100'],
								['Debug Interperter List', '0x00000800'],
								['Debug IO Control', '0x00001000'],
								['Debug O Word', '0x00002000'],
								['Debug Remap', '0x00004000'],
								['Debug Python', '0x00008000'],
								['Debug Named Parameters', '0x00010000'],
								['Debug Gdbon Signal', '0x00020000'],
								['Debug Python Task', '0x00040000'],
								['Debug User 1', '0x10000000'],
								['Debug User 2', '0x20000000'],
								['Debug Unconditional', '0x40000000'],
								['Debug All', '0x7FFFFFFF']]

	if combo == 'board':
		comboList = [['7i96', '7i96']]

	if combo == 'driver':
		comboList = [['HostMot2 Ethernet', 'hm2_eth']]

	if combo == 'firmware':
		comboList = [['None', False],
								['5 StepGens No PWM', '7i96d.bit'],
								['4 StepGens and PWM', '7i96d_1pwm.bit']]

	return comboList
