"""
Return text based on the tab number passed
"""

def descriptions(index):
	if index == 0:
		#print('tab number {}'.format(index))
		return text_0
	elif index == 1:
		#print('tab number {}'.format(index))
		return text_1
	elif index == 2:
		#print('tab number {}'.format(index))
		return text_2
	elif index == 3:
		#print('tab number {}'.format(index))
		return text_3
	elif index == 4:
		#print('tab number {}'.format(index))
		return text_4
	elif index == 5:
		#print('tab number {}'.format(index))
		return text_5
	elif index == 6:
		#print('tab number {}'.format(index))
		return text_6
	elif index == 7:
		#print('tab number {}'.format(index))
		return text_7
	else:
		#print('tab number {}'.format(index))
		return text_no
	
text_0 = """
Help Text for Machine Tab

Configuration Name is letters, numbers, spaces (replaced by underscore)
Version = 1.0 or higher

IP Address 10.10.10.10 is recommended to avoid conficts on your LAN
	10.10.10.10 W5 Down W6 Up
	192.168.1.121 W5 Down W6 Down

Firmware
To read the current firmware select the IP Address first.
	After reading the current firmware the Copy button will place the text in the clipboard.
To flash a card select the firmware and IP Address first.
	After flashing Reload or Power Cycle the card
"""

text_1 = """
Help Text for Displa Tab
Offset and Feedback display use reletive (including offsets) or machine.
Overrides use percent of programed value.
"""

text_2 = """
Help Text for Axis Tab
"""

text_3 = """
Help Text for Spindle Tab
"""

text_4 = """
Help Text for Inputs Tab
"""

text_5 = """
Help Text for Outputs Tab
"""

text_6 = """
Help Text for Options Tab
"""

text_7 = """
Help Text for PLC Tab
"""

text_8 = """
Help Text for PinOut Tab
"""

text_no = """
No Help is found for this tab
"""

