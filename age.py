a = float(input('Сколько Вам лет? '))
age = int(a)
def get_answer(age):
	if age <7:
		print ('Вы учитесь в детском саду')
	elif 7 <= age <=18:
		print ('Вы учитесь в школе')
	elif 18 < age <=23:
		print ('Вы учитесь в ВУЗе')
	else age >23:
		print ('Вы работаете')
get_answer(age)
