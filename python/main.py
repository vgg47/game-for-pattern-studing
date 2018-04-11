""" Created by Vladimir Gonchrov, 11.04.2018 
	Army is dictionary where key is type of unit and value is list units this type."""

from collections import defaultdict
import gondorpersfactory as gdf
import fight as ft

myArmy = defaultdict(list)
for i in range(20):
	myArmy['soldier'].append(gdf.create_soldier())
	print("attack force your army:", ft.count_attack(myArmy))
	myArmy['archer'].append(gdf.create_archer())
	print("attack force your army:", ft.count_attack(myArmy))
