def setupCombo(combo):
	if combo == 'ipCombo':
		comboList = [['Select an IP Address', False],
								['10.10.10.10', '"10.10.10.10"'],
								['192.168.1.121', '"192.168.1.121"']]
		return comboList

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
		return comboList

	if combo == 'direction':
		comboList = [['None', False],
								['CW', 'cw'],
								['CCW', 'ccw'],]
		return comboList

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
		return comboList

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
		return comboList

