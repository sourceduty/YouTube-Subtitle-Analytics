from collections import Counter
# function to sort and count words in the fileS
def sorting(filename):
  infile = open(filename)
  words = []
  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i.split('.')[0])
  infile.close()
  numberofwords=len(words)
  res2 = sorted(words, key = lambda s: s.casefold())
###################################
  print("Extracted sorted word list ")
  for i in res2:
    print(i)
###########################################
# open file in write mode
  with open(r'analytics.txt', 'w') as fp:
    for item in res2:
            # write each item on a new line
        fp.write("%s\n" % item)
  fp.close()
  return res2,numberofwords

# function to word frequency
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())   

def writefreq(noWords,add):
    indexes=[]
    valuess=[]
    for i in add.keys():
        indexes.append(i)
        #print(i)

    for i in add.values():
        valuess.append(i)
        #print(i)

    diction=dict(add)
    with open('analytics.txt', 'a') as fp:
        fp.write("word count in file is %s\n" %noWords)   
        fp.write("WORD FREQUENCY\n")   
        for i in range(len(indexes)):
                # write each item on a new line
            fp.write("%s\t-> %s\n" %(indexes[i],valuess[i]))  

    

    sorted_dic = dict(sorted(diction.items(), key=lambda x:x[1]))
    indexes_sort=[]
    valuess_sort=[]
    for i in sorted_dic.keys():
        indexes_sort.append(i)
        #print(i)

    for i in sorted_dic.values():
        valuess_sort.append(i)

    valuess_sort.reverse()
    indexes_sort.reverse()
    with open('popular.txt', 'w') as fp:  
        for i in range(10):
                # write each item on a new line
            fp.write("%s\t-> %s\n" %(indexes_sort[i],valuess_sort[i]))  

#main driver code

sortedlist,noWords=sorting("subtitles.txt")
add=word_count("analytics.txt")
writefreq(noWords,add)
 

   



