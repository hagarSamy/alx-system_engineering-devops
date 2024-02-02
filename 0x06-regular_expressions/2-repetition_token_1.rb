#!/usr/bin/env ruby

matches = ARGV[0].scan(/\bhbtn\b|\bhtn\b/)
puts matches.join
