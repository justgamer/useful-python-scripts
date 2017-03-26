import datetime

now = datetime.datetime.now()

while(True):
	link = input("Bitte füge den Link hier ein! Zum Beenden exit eingeben:  ")
	if(link == "exit"):
		break;

	else:
		text_file = open("links.txt","a")
		zeit = now.strftime ("%Y-%m-%d %H:%M")
		text_file.write(link+"		Zeit: "+ zeit +"\n")
		text_file.close()
		print(link + " wurde geaddet in der Datei links.txt!	")
	



