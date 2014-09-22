def joga(elemento1,elemento2):
	if ((elemento1 == "papel") and (elemento2 == 'pedra') or (elemento1 == "pedra") and (elemento2 == 'papel')):
		return 'papel'
	elif ((elemento1 == "tesoura") and (elemento2 == 'pedra') or (elemento1 == "pedra") and (elemento2 == 'tesoura')):
		return 'pedra'
	elif ((elemento1 == "tesoura") and (elemento2 == 'papel') or (elemento1 == "papel") and (elemento2 == 'tesoura')):
		return 'tesoura'