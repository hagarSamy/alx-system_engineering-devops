#!/usr/bin/env ruby

matches = ARGV[0].scan(/\bhbtn\b|\bhtn\b/)
puts matches.join

#puts ARGV[0].scan(/hb?tn/).join
