#coding: utf-8


constants = {0:'zero',1:"un",2:"deux",3:"trois",4:"quatre",5:"cinq",6:"six",7:"sept"
,8:"huit",9:"neuf",10:"dix",11:"onze",12:"douze",13:"treize",14:"quatorze",15:"quinze",16:"seize",
20:"vingt",30:"trente",40:"quarante",50:"cinquante",60:"soixante",100:"cent"}

def n2l(nbre) :
	"""
	la fonction n2l prend en argument un nbre compris entre 0 et 999 et retourne son equivalent en lettre
	"""
	#verifier si cest le bon nombre
	if not isinstance(nbre,int):
		raise TypeError("you must enter an integer value ")

	#le mot en lettre qu'il faut retourner 
	letterToReturn = ""
	
	
	# On verifier si le parametre <nbre> n'est pas dans notre dictionnaire des constantes
	
	if nbre not in constants :


		modCentaine = nbre % 100
		nbreCentaine = (nbre - (modCentaine))/100
		nbreDizaine  = (modCentaine - (modCentaine % 10))/10
		nbreUnite    = nbre % 10

		#formuler
		#letterToReturn = "je suis pas dans le tableau" + " CENTAINE "+ str(nbreCentaine) + " DIZAINE "+ str(nbreDizaine) +" UNITE "+ str(nbreUnite) + "\n \n"

		#formulation centaine
		if nbreCentaine > 0  :
			if nbreCentaine == 1  :
				""" traitement des centaine  les 100"""
				
				if nbreDizaine not in [7,8,9,0,1]:
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[nbreDizaine*10]
					elif nbreUnite == 1:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[nbreDizaine*10]+" et "+constants[nbreUnite]
					else:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[nbreDizaine*10]+"-"+constants[nbreUnite]

				if nbreDizaine == 1 :
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[nbreDizaine*10]
					elif nbreUnite not in [7,8,9]:
						indice = int("1"+str(nbreUnite) )
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[indice]
					else:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[10]+"-"+constants[nbreUnite]
					
				if nbreDizaine == 7:
					if nbreUnite ==0:
						letterToReturn += constants[nbreCentaine*100]+"-"+ constants[60]+"-"+constants[10]
					elif nbreUnite not in [7,8,9]:
						letterToReturn += constants[nbreCentaine*100] + "-"+ constants[60]+"-"+constants[int("1"+str(nbreUnite))]
					else:
						letterToReturn += constants[nbreCentaine*100]+ "-"+ constants[60]+"-"+constants[10]+"-"+constants[nbreUnite]					
				if nbreDizaine == 8:	
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[4]+"-"+constants[20]+"s"
					elif nbreUnite == 1:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[4]+"-"+constants[20]+" et "+constants[nbreUnite]
					else:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[nbreUnite]
						
				if nbreDizaine == 9:
					if nbreUnite ==0:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[10]
					elif nbreUnite not in [7,8,9] :
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[int("1"+str(nbreUnite))]
					else:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[10]+"-"+constants[nbreUnite]
				
				if nbreDizaine == 0:
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine*100]
					else:
						letterToReturn += constants[nbreCentaine*100]+"-"+constants[nbreUnite]
			else :
				""" traitement des centaines  les 200, 300, 400, 500, 600, 700, 800, 900 """
				
				if nbreDizaine not in [7,8,9,0,1]:
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[nbreDizaine*10]
					elif nbreUnite == 1:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[nbreDizaine*10]+" et "+constants[nbreUnite]
					else:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[nbreDizaine*10]+"-"+constants[nbreUnite]
				
				if nbreDizaine == 1 :
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[nbreDizaine*10]
					elif nbreUnite not in [7,8,9]:
						indice = int("1"+str(nbreUnite) )
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[indice]
					else:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[10]+"-"+constants[nbreUnite]
							

				if nbreDizaine == 7:
					if nbreUnite ==0:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+ constants[60]+"-"+constants[10]
					elif nbreUnite not in [7,8,9]:
						indice = int("1"+str(nbreUnite))
						letterToReturn += constants[nbreCentaine]+"-"+constants[100] + "-"+ constants[60]+"-"+constants[indice]
					else:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+ "-"+ constants[60]+"-"+constants[10]+"-"+constants[nbreUnite]					
				if nbreDizaine == 8:	
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[4]+"-"+constants[20]+"s"
					elif nbreUnite == 1:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[4]+"-"+constants[20]+" et "+constants[nbreUnite]
					else:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[nbreUnite]
						
				if nbreDizaine == 9:
					if nbreUnite ==0:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[10]
					elif nbreUnite not in [7,8,9] :
						indice = int("1"+str(nbreUnite))
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[indice]
					else:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[4]+"-"+constants[20]+"-"+constants[10]+"-"+constants[nbreUnite]
				
				if nbreDizaine == 0:
					if nbreUnite == 0:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"s"
					else:
						letterToReturn += constants[nbreCentaine]+"-"+constants[100]+"-"+constants[nbreUnite]				
			
				    
				    
		else : #formulatio dizaine et unité

			if nbreDizaine > 0 :
				if nbreDizaine == 1:
					if nbreUnite not in [7,8,9]:
						letterToReturn +=  constants[int(str(nbreDizaine)+str(nbreUnite))]
					else:
						letterToReturn += constants[10] +"-"+ constants[nbreUnite]
		
				elif nbreDizaine not in [7,8,9]:
					if nbreUnite == 0 :
						letterToReturn += constants[nbreDizaine*10]
					if nbreUnite ==1 :
						letterToReturn += constants[nbreDizaine*10]+" et "+constants[nbreUnite]
					else:
						letterToReturn += constants[nbreDizaine*10]+"-"+constants[nbreUnite]
				else:
					if nbreDizaine == 7:
						if nbreUnite ==0:
							letterToReturn += constants[60]+"-"+constants[10]
						elif nbreUnite not in [7,8,9]:
							indice = int("1"+str(nbreUnite))
							letterToReturn += constants[60]+"-"+constants[indice]
						else:
							letterToReturn += constants[60]+"-"+constants[10]+"-"+constants[nbreUnite]
		
					if nbreDizaine == 8:
						if nbreUnite ==0:
							letterToReturn += constants[4]+"-"+constants[20]+"s"
						else:
							letterToReturn += constants[4]+"-"+constants[20]+"-"+constants[nbreUnite]
		
					if nbreDizaine ==9 :
							if nbreUnite == 0:
								letterToReturn += constants[4]+"-"+constants[20]+"-"+constants[10]
							elif nbreUnite not in [7,8,9]:
								indice = int("1"+str(nbreUnite))
								letterToReturn +=  constants[4]+"-"+constants[20]+"-"+constants[indice]
							else:
								letterToReturn += constants[4]+"-"+constants[20]+"-"+constants[10]+"-"+constants[nbreUnite]

	else:
		letterToReturn =constants[nbre]

	return letterToReturn




