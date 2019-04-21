punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    for s in string:
        if s in punctuation_chars:
            string=string.replace(s,'')
    return string
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(string):
    string = strip_punctuation(string)
    strings=string.split(" ")
    i=0
    for s in strings:
        if s in positive_words:
            i+=1
    return i

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(string):
    string = strip_punctuation(string)
    strings=string.split(" ")
    i=0
    for s in strings:
        if s in negative_words:
            i+=1
    return i
fp=open('project_twitter_data.csv','r')
lines=fp.readlines()
texts=[]
num_retweets=[]
num_replies=[]
for row in lines:
    vals=row.strip().split(',')
    texts+=[vals[0]]
    num_retweets+=[vals[1]]
    num_replies+=[vals[2]]
del texts[0]
del num_retweets[0]
del num_replies[0]
pos=[]
neg=[]
ovl=[]
for text in texts:
    pos+=[get_pos(text)]
    neg+=[get_neg(text)]
    ovl+=[get_pos(text)-get_neg(text)]
outfile=open('resulting_data.csv','w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for i in range(len(texts)):
    outfile.write('{}, {}, {}, {}, {}'.format(num_retweets[i], num_replies[i], pos[i], neg[i], ovl[i]))
    outfile.write('\n')
