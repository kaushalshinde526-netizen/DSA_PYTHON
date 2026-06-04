from collections import defaultdict
n=int(input("Enter number of strings : "))
strs=[]
for i in  range(n):
    word=input("Enter string{i+1}: ")
    strs.append(word)
    groups = defaultdict(list)
    for word in strs:
        key="".join(sorted(word))
        groups[key].append(word)
        result=list(groups.values())
print("Grouped Anagrams : ",result)