def count_words(str2):
    count =dict()
    w=str2.split()

    for a in w:
        if a in count:
            count[a]+=1
        else :
            count[a]=1

    return count


str1=input("Enter The String: ")
c=count_words(str1)
print(c)
