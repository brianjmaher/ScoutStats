import norm_rank
import oprlib
import toprlib
import asr
import simplejson

if __name__ == "__main__":
	event_key = raw_input("Event key, e.g. 2016njfla: ")
	while True:
		try:
			norm_rank.write_normalized_CSV(event_key)
			print "Success: normalized rankings (1/4)."

			oprlib.write_stats_CSV(event_key)
			print "Success: OPR/DRP/CCWM/MPR (2/4)."

			toprlib.write_tOPRs_CSV(event_key)
			print "Success: task OPRs (3/4)."

			asr.get_ASR_CSV(event_key)
			print "Success: Alliance Synergy Ratings (ASR) (4/4)."
			break

		except simplejson.scanner.JSONDecodeError:
			print "Invalid event code."
			break
		
		except ValueError:
			print "Not enough matches played, check back later."
			break
		
		except IOError:
			command = raw_input("ERROR: file is open, please close it before writing. Try again? (Y or N)")
			if command == "Y":
				continue
			elif command == "N":
				break
			else: 
				print "Invalid command. Trying anyway."
