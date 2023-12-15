import time

def wait_seconds(x):
  time.sleep(x)
def question_add(x, y):
  question_a = x + " + " + y + " is? "
  return question_a
def calculateQuizPercent():
  #here, the quiz percentage is defined as a function so that i can get the percent. if you get all of them right, you pass. if you fail one, you fail.
  score = 0
  for x in questionsC:
    score += 1
  print('Your score is ' + str(score))
  wait_seconds(2)
  if score <= 2:
    print('You failed.')
  if score == 3:
    print('You passed! ')

print('Welcome to my quiz')
wait_seconds(2)
print('You will do an easy addition quiz because I feel like it')
wait_seconds(2)
print('There will be 3 questions of easy stuff')
wait_seconds(2)

questionsC = []
#these are the lists, questionsC stands for the correct answers and questionsIc stands for the incorrect answers
questionsIc = []

q1 = input(question_add(str(13), str(42)))
#here is the first question, q1. notice how there is an input() surrounding the question_add function.
#inside of the function, there is a str(13), which is x, and a str(42), which is y. the numbers have str() surrounding them so that they can be used in the input.
q1Answer = q1
if q1Answer == '55':
  questionsC.append(q1)
  print('Correct!')
else:
  questionsIc.append(q1)
  print('Incorrect.')

q2 = input(question_add(str(39), str(54)))
q2Answer = q2
if q2Answer == '93':
  questionsC.append(q2)
  print('Correct!')
else:
  questionsIc.append(q2)
  print('Incorrect.')

q3 = input(question_add(str(153), str(92)))
q3Answer = q3
if q3Answer == '245':
  questionsC.append(q3)
  print('Correct!')
else:
  questionsIc.append(q3)
  print('Incorrect.')

calculateQuizPercent()