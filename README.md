sc_sent_tagger
==============

Tagger for manually adding sentiment labels to tweets

Usage:

`python sent_tagger.py <input_file> <output_file>`

Upon running the program it will ask you for your name. Input your first name. This is simply so we can see who labelled the sentiment for a given tweet, we may not even need/use this data.

The program will then present you with a tweet and ask you to enter a value from 0 - 3.

+ 0 = don't know
+ 1 = negative
+ 2 = neutral
+ 3 = positive

The program will exit when all the lines in the input file have been processed. You may exit early with Ctrl-c and your results will still be written to the output file.

As of now there is no way to start tagging at an intermediate location in the input file. I would suggeset suspending the process (Ctrl-z) if you would like to stop tagging and start again later. You could also just stop with Ctrl-c and then edit your input file to begin where you left off.
