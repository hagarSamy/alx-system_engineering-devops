#!/usr/bin/env ruby
#program executed using Ruby interpreter

#puts: outputs the string passed\n
#ARGV = array containing cmnd-line arguments passed to script
#scan = searches the string for matches (regular expression) returns an array of matches
#.join = to put them ALL in 1 string

puts ARGV[0].scan(\bSchool\b).join
