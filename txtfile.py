def countwords():
    file=open("vaibhav.txt","r")
    count=0
    data=file.read()
    x=data.split()
    for i in x:
        if i[-1].isdigit():
            count+=1
            print(count)
    file.close()



        
def longlines():
    file=open("samplpefile","r"):
        data=file.readlines()
        for i in data:
            word=i.split()
            if len[word]>=10
            print(word)
        file.close()
        
