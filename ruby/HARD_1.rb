def g b=-1,t=101
  puts (a=rand(b+1...t)),' high/low/right?'
  (o=STDIN.gets)[/\Ah/] ? g(b,a) : o[/\Al/] ? g(a,t) : (puts "yay!")
end;g


# ALT SOLUTION
# def main

#   lower_bound = 1
#   upper_bound = 100

#   rand = Random.new
#   current = rand.rand(lower_bound..upper_bound)
#   previous_choices = []

#   while true

#     previous_choices.push(current)

#     print "Is #{current} your number? [yes/no]: "

#     break if gets =~ /^yes/

#     print "Is it high or low? [high/low]: "

#     answer = gets.strip

#     if answer =~ /^high/
#       upper_bound = current
#     elsif answer =~ /^low/
#       lower_bound = current
#     end

#     while previous_choices.include? current
#       current = rand.rand(lower_bound..upper_bound)
#     end

#   end

#   puts "Sweet!!!"

# end

# main()
