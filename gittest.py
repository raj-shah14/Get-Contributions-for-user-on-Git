import xml.etree.ElementTree as ET
import urllib2

username="GrahamCampbell"
contents=urllib2.urlopen("https://github.com/users/"+username+"/contributions").read()
#print contents
contri=[]
date=[]

root=ET.fromstring(contents)

for g in root:
    for g1 in g:
        for rect in g1:
            contri.append(rect.get('data-count'))
            date.append(rect.get('data-date'))

print "Date with corresponding Contribution"

for i,j in map(None,contri,date):
    print j+"-->"+i
    
print "Day-->Contributions"
for i in range (len(date),0,-1):
    print i,"-->",contri[len(contri)-i]
   
