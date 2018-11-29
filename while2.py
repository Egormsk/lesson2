vocabulari ={'Как дела?': 'Хорошо', 
			 'Что делаешь?': 'Програмирую', 
			 'Как настроение': 'Отличное'}
ask = input()
def ask_user (ask):
		while True :
			if ask in vocabulari:
				ans = vocabulari [ask]
				print (ans)
				break
			else :
				print ('Моя твою не понимать')
				break
ask_user(ask)