from nltk.corpus import stopwords
import pandas as pd
import math
stop_words = set(stopwords.words('english')) - set(['in', 'to','where'])

print("this is the final list")
def getInputFiles(filelist):#the funcation that reed all paths in the file
    with open(filelist) as f:
        return [a for a in f.read().split()]
def preprocess(data):#the funcation that remove punc
    for p in "!.,:@#$%^&?<>*()[}{]-=;/\"\\\t\n":
        if p in '\n;?:!.,.':
            data = data.replace(p,' ')
        else: data = data.replace(p,'')
    return data.lower()
def computeIDF(docList):#the funcation that compute idf
    N =10#the number of doc
    for word, val in docList.items():
        if N==val:#check if num of doc =number of tf
            docList[word]=1
        else:
             docList[word] =format(float(math.log10(N / float(val))), ".2f")

    return docList
def computeTFW(wordDict):
    tfDict = {}
    for word, count in wordDict.items():
        if count>0:
            tfDict[word] =1+math.log10(float(count))
        else:
            tfDict[word]=0
    return tfDict
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        # j=float(idfs[word])
       # tfBow[word] = float(val)
        tfidf[word] = val*float(idfs[word])
    return tfidf
def computeTf(dicnumber):
    dicf = {}
    for l,k in sorted(index.items()):
                dicf[l]=0
                for j, n in k[0].items():
                    if j == dicnumber:
                       dicf[l]=len(n)
    return dicf

def computeNormlizaton(tf_idf):
    SUM = 0
    for word in tf_idf.values():
        SUM = SUM + word ** 2
    tfidf = {}
    for word, val in tf_idf.items():
        tfidf[word] = float(tf_idf[word])/math.sqrt(SUM)
    return tfidf

def computecosineSimliarty(NormlizatonQuery, Normlizatondictf_id):
    result = {key: NormlizatonQuery[key] * Normlizatondictf_id[key] for key in NormlizatonQuery}
    print(result)
    score=sum(result.values())

    return score

print('-----------------------------------------------------part1-----------------------------------------------')
files = getInputFiles("input.txt")#get list of all paths
filenumber = 1#intialize the file number=1
index = {}#the dectionary than
for i in range(len(files)):
    with open(files[i]) as f:
        l=f.read()#read all things in the doc
        doc = [a for a in preprocess(l).split()]#remove the punc and split the doc and put the token in list
        f1 = [w for w in doc if not w.lower() in stop_words]#change all item to lower and remove the stopwords
        for idx, word in enumerate(f1):#use to get the postion of the all items in list
            if word in index:#check if the token is in the index
                if filenumber in index[word][0]:#check if the file number in the index
                    index[word][0][filenumber].append(idx+1)#insert the postion in the file number of token

                else:
                    index[word][0][filenumber] = [idx+1]#insert the file numer and the first postion

            else:
                index[word] = [] # initialize the list.
                index[word].append({})# initialize the dic that contain The postings list is initially empty.
                index[word][0][filenumber] = [idx+1]# Add doc number and postion .
        filenumber += 1 # Increment the file number
print("the token after remove stop words")
for l in index.keys():
 print(l)
print("-----------------------------------------------------part2-----------------------------------------------")
diction={}#the dic that contain every token and the number doc that contain the token
for l,k in sorted(index.items()):#using to print every token and his postion
     s=len(k[0])
     print(l,":",k)
     diction[l]=int(s)#add token and the number doc that contain the token
#print (diction)
x=input("enter query phase")
doc = [a for a in preprocess(x).split()]#remove the punc and split the doc and put the token in list
query = [w for w in doc if not w.lower() in stop_words]#change all item to lower and remove the stopwords
print(query)
h=[]
for l,k in sorted(index.items()):
    for i in range (len(sorted(query))):
        if l==query[i]:
            o=[]
            for j,n in k[0].items():
              o.append(j)

            h.append(o)
print(h)
p=list(set.intersection(*map(set,h)))

print(p)

for k in p:
    print("the matched files is ")
    print(files[k-1])
print('-----------------------------------------------------part3-----------------------------------------------')
print("the df of all token", diction)
idf=computeIDF(diction)
print("the idf is",idf)
dic={}
for l,k in sorted(index.items()):
    dic[l]="|"


dic1=computeTf(1)
dic2=computeTf(2)
dic3=computeTf(3)
dic4=computeTf(4)
dic5=computeTf(5)
dic6=computeTf(6)
dic7=computeTf(7)
dic8=computeTf(8)
dic9=computeTf(9)
dic10=computeTf(10)



print("\n                                     the term Frequency for each term in each document                        \n")
df1=pd.DataFrame.from_dict([dic1,dic2,dic3,dic4,dic5,dic6,dic7,dic8,dic9,dic10]).T
df1.columns = ["doc1","doc2","doc3","doc4","doc5","doc6","doc7","doc8","doc9","doc10"]
print(df1,"\n --------------------------------------")

dictfw1=computeTFW(dic1)
dictfw2=computeTFW(dic2)
dictfw3=computeTFW(dic3)
dictfw4=computeTFW(dic4)
dictfw5=computeTFW(dic5)
dictfw6=computeTFW(dic6)
dictfw7=computeTFW(dic7)
dictfw8=computeTFW(dic8)
dictfw9=computeTFW(dic9)
dictfw10=computeTFW(dic10)

print("\n                                     theterm Frequency weight for each term in each document                        \n")
df2=pd.DataFrame.from_dict([dictfw1,dictfw2,dictfw3,dictfw4,dictfw5,dictfw6,dictfw7,dictfw8,dictfw9,dictfw10]).T
df2.columns = ["doc1","doc2","doc3","doc4","doc5","doc6","doc7","doc8","doc9","doc10"]
print(df2,"\n --------------------------------------")
dictf_idf1=computeTFIDF(dictfw1,idf)
dictf_idf2=computeTFIDF(dictfw2,idf)
dictf_idf3=computeTFIDF(dictfw3,idf)
dictf_idf4=computeTFIDF(dictfw4,idf)
dictf_idf5=computeTFIDF(dictfw5,idf)
dictf_idf6=computeTFIDF(dictfw6,idf)
dictf_idf7=computeTFIDF(dictfw7,idf)
dictf_idf8=computeTFIDF(dictfw8,idf)
dictf_idf9=computeTFIDF(dictfw9,idf)
dictf_idf10=computeTFIDF(dictfw10,idf)


print("\n                                     the tf.idf for each term in each document                        \n")
df2=pd.DataFrame.from_dict([dictf_idf1,dictf_idf2,dictf_idf3,dictf_idf4,dictf_idf5,dictf_idf6,dictf_idf7,dictf_idf8,dictf_idf9,dictf_idf10]).T
df2.columns = ["doc1","doc2","doc3","doc4","doc5","doc6","doc7","doc8","doc9","doc10"]
print(df2,"\n --------------------------------------")
query_tf = {}
for l, k in sorted(index.items()):#using to put all token =0
    query_tf[l] = 0
for o in query:#using to make for loop in the query
   for l, k in sorted(query_tf.items()):#using for loop in the query_tf
        if o == l:#check if the item in the query=item in query_tf
            query_tf[l] =k+1#add 1 to the value in the query_tf
        else:
            query_tf[l] = k
print("the tf of query", query_tf)
query_tfw=computeTFW(query_tf)
print("the tfw of query", query_tfw)
tf_idf_query=computeTFIDF(query_tfw,idf)
#print("idf", a)
print("the tf.idf of query", tf_idf_query)

NormlizatonQuery=computeNormlizaton(tf_idf_query)
print("the Normlizaton of query", NormlizatonQuery)

"""   rankscore for each document """

tf_idfdictinory={ 1:dictf_idf1,2:dictf_idf2,3:dictf_idf3,4:dictf_idf4,5:dictf_idf5,6:dictf_idf6,7:dictf_idf7,8:dictf_idf8,9:dictf_idf9,10:dictf_idf10}
rankscore={}

for key in tf_idfdictinory:
    if key in p:
        Normlizatondictf_idf = computeNormlizaton(tf_idfdictinory[key])
        print("cosineSimilarity for doc ",key)
        score = computecosineSimliarty(NormlizatonQuery, Normlizatondictf_idf)
        rankscore[key] = score

print("rankscore for each document",rankscore)

