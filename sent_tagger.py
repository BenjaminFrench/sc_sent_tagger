import json
import sys

name = ''

def process_tweet(input_tweet):
	tweet_json = json.loads(input_tweet)

	# get tweet text
	tweet_text = tweet_json['text']

	# Display text to user and ask for response
	print tweet_text
	print

	print 'Classify tweet (0 = Don\'t know, 1 = negative, 2 = neutral, 3 = positve: ',

	while True:
		sentiment = raw_input()
		if sentiment in ('0','1','2','3'):
			break
		print 'Please enter a value between 0 and 3: ',

	print '--------------------------------------------------------------------------------'
	print



	# add tagged parts of speech to JSON
	output_tweet = {'id': tweet_json['id'], 'text': tweet_text, 'sentiment': sentiment, 'tagged_by': name}

	return output_tweet

def process_file(input_filename, output_filename):
	"""
	Process the file one input at a time and write the given output file
	"""
	# Create output file
	outfile = open(output_filename, 'w')

	# Process one line of the file
	with open(input_filename, 'r') as infile:
		for line in infile:
			tweet_output = process_tweet(line)
			if tweet_output is not None:
				json.dump(tweet_output, outfile)
				outfile.write('\n')

		infile.close()

	outfile.close()

if __name__ == '__main__':

	# Get arguments
	arguments = sys.argv
	arguments_len = len(arguments)

	# Data set name 
	input_filename = arguments[1]
	output_filename = arguments[2]

	print 'Please enter your first name only: ',
	name = raw_input()
	print
	print

	process_file(input_filename, output_filename)
