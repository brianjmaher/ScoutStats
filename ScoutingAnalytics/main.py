import oprlib
import toprlib
import asrlib
import simplejson

if __name__ == "__main__":
	event_key = raw_input("Event key, e.g. 2016njfla: ")
	try:
		toprlib.write_tOPRs_CSV(event_key)
		print "Succees (1/3)."
		
		oprlib.write_stats_CSV(event_key)
		print "Success (2/3)."

		asrlib.get_ASR_CSV(event_key)
		print "Success (3/3)."
	
	except simplejson.scanner.JSONDecodeError:
		print "Invalid event code."
	#except ValueError:
	#	print "Not enough matches played, check back later!"