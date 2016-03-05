import bscout
import oprlib
import csv

def get_schedule_sheet(event_key):
	sheet = []
	top_row = [["Match #", "Red 1", "Red 2", "Red 3", "Blue 1", "Blue 2", "Blue 3", "Red Score", "Blue Score"]]
	matches = bscout.get_event_matches(event_key)
	for match in matches:
		if match["comp_level"] == "qm" and match["alliances"]["red"]["teams"] > -1:
			row = [match["match_number"]]
			colors = ("red", "blue")
			for color in colors:
				for team in match["alliances"][color]["teams"]:
					row.append(int(team[3:]))
			for color in colors:
				row.append(match["alliances"][color]["score"])
			sheet.append(row)
	sheet.sort(key=lambda x: x[0])
	return top_row + sheet

def add_asr_to_sheet(event_key, sheet):
	oprs = [opr[0] for opr in oprlib.compute_OPR(event_key)]
	teams = bscout.get_event_teams_list(event_key)
	sheet[0].extend(["Red Total OPR", "Blue Total OPR", "Red ASR", "Blue ASR"])
	for i in range(1, len(sheet)):
		red_total_opr = 0
		blue_total_opr = 0
		for j in range(1, 4):
			red_total_opr += oprs[teams.index(sheet[i][j])]
		for j in range(4, 7):
			blue_total_opr += oprs[teams.index(sheet[i][j])]
		red_asr = sheet[i][7] - red_total_opr
		blue_asr = sheet[i][8] - blue_total_opr 
		row_ext = [red_total_opr, blue_total_opr, red_asr, blue_asr]
		sheet[i].extend([round(x,2) for x in row_ext])

def writeCSV(sheet, event_key):
	with open('%s_asr.csv' % event_key, 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect=csv.excel)
		for row in sheet:
			writer.writerow(row)

def get_ASR_CSV(event_key):
	sheet = get_schedule_sheet(event_key)
	add_asr_to_sheet(event_key, sheet)
	writeCSV(sheet, event_key)