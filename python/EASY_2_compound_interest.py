from sys import argv, exit

types = {
  'simple': lambda capital, rate, time: capital * (1 + (rate * time)),
  'compound': lambda capital, rate, time: capital * ((1 + rate) ** time)
}

if len(argv) != 5 or argv[1] not in types:
  print "usage: %s <%s> capital rate time" % (argv[0], '|'.join(types))
  exit(1)

capital, rate, time = map(float, argv[2:])
print types[argv[1]](capital, rate, time)


# Use it like:
# python EASY_2_compound_interest.py compound 2500 .40 18
