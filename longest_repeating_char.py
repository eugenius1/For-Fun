# Eusebius N.

import time

def longest_repeat_char(string):
	''' 
	Return the (first) longest repeating character in a sorted string
	Naive approach that iterates each character
	
	O(1) space
	O(n) time: best, worst and average
	'''

	if string:
		# initialise
		last_char = ''
		last_count = 0
		longest_count = 0

		for char in string:
			# last sequence continues
			if char == last_char:
				last_count += 1
			
			# end of last sequence
			else:
				# if new longest repeating character
				if last_count > longest_count:
					longest_char = last_char
					longest_count = last_count
				
				# reset for current character
				last_char = char
				last_count = 1

		return longest_char

def longest_repeat_char2(string):
	'''
	Uses the sortedness to look ahead and see if current character can form the longest sequence

	O(1) space

	O(1) best time
	O(n/L) average time where L is the size of the longest sequence
	O(n) worst time
	'''
	if string:
		if len(string) <= 1:
			return string[0]
		longest_char = string[0]
		longest_count = 1

		i = 1
		while i < (len(string[1:]) - longest_count):
			char = string[i]
			
			# if current character repeats longer than current longest_count
			if char == string[i+longest_count]:
				longest_char = char
				# repeat_end is the index immediately after sequence
				repeat_end = i+longest_count +1
				
				# find end of repeating sequence
				try:
					while string[repeat_end] == char:
						repeat_end += 1
				# if we reach the end of string
				except IndexError:
					return (len(string) - i)
				
				# repeat_end still lands on the character immediately after sequence
				longest_count = repeat_end - i
			else:
			# iterate until a character is found with a longer sequence
				i += 1

		return longest_char	


######### testing #############
s = 'the quick brown fox jumped over the lazy dog'.replace(' ', '')
s = ''.join(sorted(s))

f = [longest_repeat_char, longest_repeat_char2]
for func in f:
	start_time = time.time()
	print func(s)
	print '----%f usec----' % ((time.time()-start_time) * 1e6)
