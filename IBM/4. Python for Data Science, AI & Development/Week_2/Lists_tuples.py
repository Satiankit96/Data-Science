#1. Tuples 
#This is an ordered sequence 
#Tupples are immutable
#Nested tuples are supported tupple1[outer][inner]
ratings = (10,9,8,7,6,5,4,3)
print(ratings)
tuple1 = ("name",1,2)
print(tuple1[2])
print(tuple1[0:5])

#2. Lists 
#These are mutable 
# They are ordered as well[]
#Extend adds the elements to the list. Append adds the entire list
list1 = [1,2,3,4,1]
# Cheat sheet
# https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstUFkwMTAxRU4tU2tpbGxzTmV0d29yay9sYWJzL2hhbmRvdXRzL0NoZWF0X1NoZWV0X1dlZWstMi5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE2OTcxMjk1NTB9.xNRTFFzY9COyLCPBuSKyLwcwqX9J2NUEeBCA349Zq2w

#3. Dictionaries - Key value pairs 
dict1 = {"a":1,"b":2}

#Sets 
#These are unordered
#Set1 = {''} - They do not have duplicates.
print(set(list1))