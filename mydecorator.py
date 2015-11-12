def logger(func):
   logger_name = logger.__name__
   def inner(*args, **kwargs): #1
      print "Arguments were: %s, %s" % (args, kwargs)
      inner_name = inner.__name__
      return func(*args, **kwargs), inner_name, logger_name #2
   return inner


@logger
def fool(x=5,y=7):
   fool_name= fool.__name__
   print fool_name
   return x*y, fool_name

print fool(2,3)