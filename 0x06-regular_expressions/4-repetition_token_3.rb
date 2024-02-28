#!/usr/bin/env ruby
puts ARGV[0].scan(/^.[^o]{3,}$/).join
