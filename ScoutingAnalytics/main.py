import schedule_norm
import oprlib
import toprlib
import asrlib
import simplejson

if __name__ == "__main__":
	event_key = raw_input("Event key, e.g. 2016njfla: ")
	try:
		schedule_norm.write_normalized_CSV(event_key)
		print "Success: normalized rankings (1/4)."

		oprlib.write_stats_CSV(event_key)
		print "Success: OPR/DRP/CCWM/MPR (2/4)."

		toprlib.write_tOPRs_CSV(event_key)
		print "Success: task OPRs (3/4)."

		asrlib.get_ASR_CSV(event_key)
		print "Success: Alliance Synergy Ratings (ASR) (4/4)."
	
	except simplejson.scanner.JSONDecodeError:
		print "Invalid event code."
	except ValueError:
		print "Not enough matches played, check back later!"