def setupCombo(combo):
	if combo == 'ipCombo':
		comboList = [['Select an IP Address', False],
								['10.10.10.10', '"10.10.10.10"'],
								['192.168.1.121', '"192.168.1.121"']]

	if combo == 'axis':
		comboList = [['None', False],
								['X', 'x'],
								['Y', 'y'],
								['Z', 'z'],
								['A', 'a'],
								['B', 'b'],
								['C', 'c'],
								['U', 'u'],
								['V', 'v'],
								['W', 'w'],]

	if combo == 'direction':
		comboList = [['None', False],
								['CW', 'cw'],
								['CCW', 'ccw'],]

	if combo == 'input':
		comboList = [['None', False],
								['E-Stop In', 'estopin'],
								['Home', 'home'],
								['Both Limit', 'bothlimit'],
								['Min Limit', 'minlimit'],
								['Max Limit', 'maxlimit'],
								['Home & Limit', 'homelimit'],
								['Min Limit & Home', 'minlimithome'],
								['Max Limit & Home', 'maxlimithome'],
								['Probe', 'probe'],
								['Digital 0', 'digitalin0'],
								['Digital 1', 'digitalin1'],
								['Digital 2', 'digitalin2'],
								['Digital 3', 'digitalin3']]

	if combo == 'output':
		comboList = [['None', False],
								['Coolant Flood', 'coolantflood'],
								['Coolant Mist', 'coolantmist'],
								['Spindle On', 'spindleon'],
								['Spindle CW', 'spindlecw'],
								['Spindle CCW', 'spindleccw'],
								['Spindle PWM', 'spindlepwm'],
								['Spindle Brake', 'spindlebrake'],
								['E-Stop Out', 'estopout'],
								['Digital Out 0', 'digitalout0'],
								['Digital Out 1', 'digitalout1'],
								['Digital Out 2', 'digitalout2'],
								['Digital Out 3', 'digitalout3']]

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

	return comboList
