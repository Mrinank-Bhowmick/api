import random
#from flask import jsonify
def life_quote():
    fin=open('lifequotes.txt','r')
    for count, line in enumerate(fin):
        pass
    fin.seek(0)
    data=(fin.readlines()[random.randint(1,count)]).split('-')
    q=data[0]  #quote
    a=data[1].replace('\n','')  #author
    result={
        "a": a,
        "q": q
    }
    return result

def business_quote():
    fin=open('business_quotes.txt','r')
    for count, line in enumerate(fin):
        pass
    fin.seek(0)
    data=(fin.readlines()[random.randint(1,count)]).split('-')
    q=data[0]  #quote
    a=data[1].replace('\n','')  #author
    result={
        "a": a,
        "q": q
    }
    return result

def friendship_quote():
    fin=open('business_quotes.txt','r')
    for count, line in enumerate(fin):
        pass
    fin.seek(0)
    data=(fin.readlines()[random.randint(1,count)]).split('-')
    q=data[0]  #quote
    a=data[1].replace('\n','')  #author
    result={
        "a": a,
        "q": q
    }
    return result