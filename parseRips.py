# A utility to parse National Weather Service Alerts
# and write to a csv file

#import libraries
import sys, csv, argparse, re, time

start = 0
end = 0

# main parser function
def parseNWS(file):

	#open a new csv using the entered file name
	writer = csv.writer(open('rip_risk.csv', 'wb'))
	writer.writerow(['pil_code','geo_code','geo_desc','datetime','daypart','error_check','beach_spec','rip_current_risk'])
	print('New file created...')

	print('Opening source data file...')
	# now we need to split each forecast into its constituent parts
	# get the first date for reach discrete forecast
	date_pattern = '((?:TTTTTTTTT|\d{3,4}) \SM E\ST (?:\S{3} ){2}(?: \d|\d{1,2}) \d{4})'
	# here's our best try so far at extracting the rip risk forecast
	# this only captures the first instance
	rip_pattern = '.*?\n([Rr][Ii][Pp].*?[Rr][Ii][Ss][Kk](?: (.*?)\.+|\.*?|: *)(\w.*?)\.)'
	rip_pattern_p2 = '.*?\n([Rr][Ii][Pp].{1,9}[Rr][Ii][Ss][Kk](?: (?:\w.*?)\.+|: *)(?:\w.*?)\..*?[Rr][Ii][Pp].{1,9}[Rr][Ii][Ss][Kk](?: (\w.*?)\.+|: *)(\w.*?)\.)'
	# and for our geo codes
	geo_start = '(\SCZ\d{3}).*?-\n(.*?)-.*?'
	geo_end = '\n.*?\n\.(TOMORROW|REST OF TODAY|TODAY)\.\.\.'
	geo_pattern = '\n(\SCZ\d{3}).*?-\n(.*?)-\n.*?\n\.(TOMORROW|REST OF TODAY|TODAY)\.\.\.'
	pil_code = 'SRFILM'
	with open(file) as f:
		# read in our context as one text blob
		blob = f.read()
		# parse individual forecasts bounded on each side by
		# the \x01 and \x03 characters, using inclusive newline
		# flag and the minimal capture qualifier
		forecasts = re.findall('\x01\n(.*?)\x03', blob, re.DOTALL)
		print('Captured {} forecasts...').format(len(forecasts))
		# initialize a variable to store our bad dates for later error checking
		bad_dates = []
		# loop through each of our forecasts
		counter = 0
		for forecast in forecasts:
			stations = forecast.split('\n$$\n')
			for station in stations:
				# pull out the first instance of date with our date pattern
				date = re.search(date_pattern,station)
				# if our search pattern doesn't match anything...
				if date != None:
					#store the text of the bad station in a list for later error checking
					rip_forecasts = re.findall(geo_start + date_pattern + geo_end + rip_pattern, station, re.DOTALL)
					rip_p2_forecasts = re.findall(geo_start + date_pattern + geo_end + rip_pattern_p2, station, re.DOTALL)
					for rcf in rip_forecasts:
						#clean up our input of extra spaces and linebreaks
						rcf = map(lambda x: ' '.join((x.replace('\n',' ')).split()),rcf)
						counter += 1
						rcf.insert(0,pil_code)
						writer.writerow(rcf)
						print('Writing row: {}').format(rcf)
					for rcf2 in rip_p2_forecasts:
						#clean up our input of extra spaces and linebreaks
						rcf2 = map(lambda x: ' '.join((x.replace('\n',' ')).split()),rcf2)
						counter += 1
						rcf2.insert(0,pil_code)
						writer.writerow(rcf2)
						print('Writing row: {}').format(rcf2)
				else:
					bad_dates.append(station)
		print('Logged {} discrete forecasts...').format(counter)

if __name__ == '__main__':
	start = time.time()
	parser = argparse.ArgumentParser(description='Parse NWS alerts')
	parser.add_argument('path',help='Enter the file location')
	args = parser.parse_args()
	
	parseNWS(args.path)
	end
	end = time.time()
	print('...finished in {} seconds').format(end - start)