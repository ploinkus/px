import time

def wait_seconds(x):
  time.sleep(x)
#this makes the time.sleep method into a function that is easier to read.

#ex:
  print('waiting 2 seconds with the normal time.sleep() function:')
  time.sleep(2)
  print('done')
#the time.sleep is less readable than the wait_seconds() function
  print('waiting 2 seconds with the normal time.sleep() function:')
  wait_seconds(2)
  print('done')

#things i programmed in mobile github
name = input("What is your name? ")
print("Your name is " + name + ", correct?")