#!/usr/bin/env ruby
#(.*?): This is a non-greedy capture group that
#matches any sequence of characters except newline characters.
#The ? makes it non-greedy
#meaning it will stop matching as soon as
#it finds a closing bracket ]
#.: any char
#*: 0 or more of preceding
#?: 1 or none
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
