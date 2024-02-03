#!/usr/bin/env ruby
#^: Asserts the position at the start of the string
#$: for the end
puts ARGV[0].scan(/^[0-9]{10}$/).join
