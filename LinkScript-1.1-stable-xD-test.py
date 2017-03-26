import datetime

now = datetime.datetime.now()
start = True

while(start == True):
	link = input("Bitte füge den Link hier ein! Zum Beenden exit eingeben:	")
	if(link == "exit"):
		start = False

	else:
		text_file = open("links.txt","a")
		zeit = now.strftime ("%Y-%m-%d %H:%M")
		text_file.write(link+"		Zeit: "+ zeit +"\n")
		text_file.close()
		print(link + "wurde geaddet in der Datei links.txt!	")
	



