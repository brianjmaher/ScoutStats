import oprlib
import toprlib
import simplejson

if __name__ == "__main__":
	event_key = raw_input("Event key, e.g. 2016njfla: ")
	try:
		toprlib.write_tOPRs_CSV(event_key)
		print "Succees (1/2)."
		oprlib.write_stats_CSV(event_key)
		print "Success (2/2)."
	except simplejson.scanner.JSONDecodeError:
		print "Invalid event code."
	except ValueError:
		print "Not enough matches played, check back later!"