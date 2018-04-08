from Gondor_pers import Soldier

a = Soldier(gondor_characteristics = {'magic_spell' : 1}, \
		damage_dealer_characteristics = {'attack' : 2, 'attack_range' : 3, \
	 	'attack_speed' : 4, 'attack_type' : 5}, characteristics = \
	 	{'cost' : 6, 'health' : 7, 'speed' : 8, 'defence' : 9, \
	 	'magic_resistance' : 10, 'phys_resistance' : 11})

print(a.characteristics)