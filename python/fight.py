""" Created by Vladimir Gonchrov, 11.04.2018 
	count_attack() considers the total damage to the army / unit"""
	
def count_attack(army):	
	sum_attack = 0
	for j in army:
		for i in army[j]:
			sum_attack += i.check_attack()
	return sum_attack