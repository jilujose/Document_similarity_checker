from nltk.corpus import stopwords  #you can either use nltk or define your own stop words
import difflib as dl #for checking similarity between words
sim = dl.get_close_matches #similarity function
count = 0
#---------------------------------------------------Processing Document 1-----------------------------------------------------------
sent1 = open("doc_1.txt") 
lines1 = sent1.read()
stop_words = set(stopwords.words('english'))
word_tokens = lines1.split()	#spliting into words
filtered_sentence1 = [w for w in word_tokens if not w in stop_words]
filtered_sentence1 = []		# for saving filtered sentence after removing stop words

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence1.append(w)

newlines = []
for item in filtered_sentence1:  #removing punctuations
   newlines.append(item.strip(',''.''-'))
lines1 = newlines

#----------------------------------------------------End Processing Document 1----------------------------------------------------

#----------------------------------------------------Processing Document 2--------------------------------------------------------
sent2 = open("doc_2.txt")
lines2 = sent2.read()
stop_words = set(stopwords.words('english'))
word_tokens = lines2.split()
filtered_sentence2 = [w for w in word_tokens if not w in stop_words]
filtered_sentence2 = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence2.append(w)
newlines = []
for item in filtered_sentence2:  #removing punctuations
   newlines.append(item.strip(',''.'))
lines2 = newlines       
#-------------------------------------------------------End Processing Document 2--------------------------------------------------

#----------------------------------------------------------------Compare-----------------------------------------------------------   
#calculating similarity         
for j in lines1:
    if sim(j, lines2):
        count += 1
n = float(count) / float(len(lines1))
print "The Document is"
print '%d%% Similar' % int(n * 100)

#----------------------------------------------------------------End Compare-------------------------------------------------------