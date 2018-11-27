class_journal = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
				 {'school_class': '3a', 'scores': [3,5,2,5,2]}, 
				 {'school_class': '2a', 'scores': [3,5,4,5,3]}, 
				 {'school_class': '1a', 'scores': [5,4,4,5,4]}]
number_of_students = 0
total_scores = 0
class_average = 0
for sch_cls in class_journal:
	 for score in sch_cls:
	 	  score = sch_cls['scores']
	 	  scor = sum(score)
	 total_scores += scor                      #сумма всех оценок
	 students_in_clas = len(score)             #студентов в классе
	 number_of_students += students_in_clas    #студентов в школе
	 print ('Средняя оценка в классе:', sch_cls ['school_class'], ' : ', (scor/students_in_clas)) 
print('Средний бал по всей школе: ', (total_scores/number_of_students))