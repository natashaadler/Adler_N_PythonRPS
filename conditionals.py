# check a temperature and output a result

temperature= int(input("input a number between 0 and 100"))

#always put : after what you are making conditional?
#looks at three conditions, remember numbers are not equal to text***

#<= less then or equal to
if temperature <= 4:
	print("water is solid. because it frozen")
# < - less then
# elif - if the previous conditions were not true, then try this condition
elif temperature < 100:
	print("water is a liquid")
# >= - greater then or equal to 
#else - if only when test condition is True . If the condition is False , body of else is executed.
else:
	print("water is gas. beacuse its boiling")