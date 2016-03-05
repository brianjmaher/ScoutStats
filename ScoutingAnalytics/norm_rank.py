import asr
import bscout
import csv

def normalize_sheet(sheet):
	sheet[0].insert(0, "Norm Ranking")
	sheet[0].insert(1, "QA")
	for i in range(1, len(sheet)):
		sheet[i].insert(0, round(float(sheet[i][2]) / float(sheet[i][8]), 2))
	sheet = [sheet[0]] + sorted(sheet[1:], key=lambda x: x[0], reverse=True)
	for i in range(1, len(sheet)):
		sheet[i].insert(0, i)
	return sheet

def writeCSV(sheet, event_key):
	with open('%s_normalized_rankings.csv' % event_key, 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect=csv.excel)
		for row in sheet:
			writer.writerow(row)

def write_normalized_CSV(event_key):
	sheet = bscout.get_event_rankings(event_key)
	sheet = normalize_sheet(sheet)
	writeCSV(sheet, event_key)