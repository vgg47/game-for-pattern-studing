""" Created by Vladimir Gonchrov, 11.04.2018 
	count_attack() considers the total damage to the army / unit"""

from army import Army
	
def count_attack(real_army):	
	sum_attack = 0
	for j in real_army.army:
		for i in real_army.army[j]:
			sum_attack += i.check_attack()
	return sum_attack