#!/usr/bin/env ruby
puts ARGV[0].scan(/\b.[^o]{3,}\b/).join
