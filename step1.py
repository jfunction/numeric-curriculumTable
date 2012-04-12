#!/usr/python2.7

#	TODO:
#1. Clean exercise names (truncate after max chars)
#2. Section headers
#3. Get playlists from file...
#4. Dropdown playlist menu
#5. Export to PDF



from urllib import urlopen
from re import split
import json# was jolly annoyed/relieved to find this 5 hours into making my own json parser :(

########################
#1.	Khan API -> XML file
#	I'll get the XML file containing {video name, time, exercise name}
#	
#2. JSON file -> javascript
#	Print a pretty table and allow the user to click which video they want in "My Curriculum"
#
#3. form -> php -> pdf
#	Allow the user to save the data to a pdf document
############################
#Step 1:			 # # # #
############################
#Original List:
#
#Addition and subtraction
#Multiplication and division
#Negative numbers
#Number properties
#Order of operations
#Factors and multiples
#Fractions
#Decimals
#Percents
#Ratios and proportions (basic)
#Exponents (basic)

#playlists for arithmetic
playlists = [
"addition-subtraction",
"multiplication-division",
"negative-numbers",
"number-properties",
"order-of-operations",
"factors-multiples",
"fractions",
"decimals",
"percents",
"ratios-proportions",
"basic-exponents"
]
#obviously one can customize this easily. Looking at api, can look for "arithmetic" in topic_page_url of playlists...
#get the playlists with "/math/arithmetic" and pop them on the page...

def main():#later extend this to take in lists containing the info in playlists above...
	print "writing xml file"
	f=open("list.xml",'w')
	f.write("<?xml version=\"1.0\"?>\n");
	f.write("<!--Step2, xml file for parsing into javascript-->\n");
	f.write("<node>");
	for playlist in playlists:

		print "--generating list of triples for playlist..."
		triplesList = getTriples(playlist)

		print "\n--writing data for playlist: ",playlist
		f.write("<playlist ptitle = \""+str(playlist)+"\">\n")#write the playlist tag
		for triple in triplesList:#returns a list of triples [(..,..,..),(...),(...)]
			print triple
			video = triple[0]
			time = triple[1]
			exercises = triple[2]
			
			#write data to xml file
			videoTag = "\t\t<title>"+video+"</title>\n"
			timeTag = "\t\t<time>"+time+"</time>\n"
			exerciseTags = ["\t\t<exercise>"+exercise+"</exercise>\n" for exercise in exercises]
			
			f.write("\t<video>\n")
			f.write(videoTag)
			f.write(timeTag)
			for exerciseTag in exerciseTags:
				f.write(exerciseTag)
			f.write("\t</video>\n")

		f.write("</playlist>\n")#close playlist tag
	f.write("</node>");

def getTriples(playlist):
	print "---opening site..."
	jsons = urlopen("http://www.khanacademy.org/api/v1/playlists/"+str(playlist)+"/videos")
	print "----reading JSON text..."
	import json
	text = jsons.read()
	jsons.close()
	print "---parsing text..." 
	
	triplesList = []
	videoList = json.loads(text)
	
	for video in videoList:
		youtubeId = video["youtube_id"]
		title = video["title"]
		time = str(video["duration"])
		print "\tTitle: ",title,"\n\tDuration: ",time," sec\n\tYouTube ID: ",youtubeId
		exercises = getExercises(youtubeId)
		print "----writing triple to xml"
		triple = (title, time, exercises)
		triplesList.append(triple)
		
	return triplesList
		
def getExercises(youtubeId): #fetches a list of exercise names
	print "---opening site..."
	jsonpage = urlopen("http://www.khanacademy.org/api/v1/videos/"+str(youtubeId)+"/exercises")

	print "----reading JSON text..."
	text = jsonpage.read()
	jsonpage.close()

	print "---parsing text..."
	exercise_data = json.loads(text)
	short_names = []

	for exercise in exercise_data:
		short_names.append(str(exercise["short_display_name"]))
	return short_names

if __name__ == "__main__":
	main()
