file1 = open("/file/path.txt","r")
#Better to use it with with 
with open ("example1.txt","r") as File1:
    file_stuff = File1.read()
    print(file_stuff)

print(File1.closed)
print(file_stuff)

#Read Operations
# https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstUFkwMTAxRU4tU2tpbGxzTmV0d29yay9sYWJzL2xhYi9Nb2R1bGVfNC9SZWFkX2ZpbGVfd2l0aF9vcGVuX1JlYWRpbmcubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNjk1ODA0NjEwfQ.AciUjYuCKFvYwc_l-dU83hkDV-qJBoSm0Ds2W-HUYd8

with open ("example1.txt","w") as File1:
    File1.write("Count this as a new file")
    pass

#Write Operations
#https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstUFkwMTAxRU4tU2tpbGxzTmV0d29yay9sYWJzL2xhYi9tb2R1bGVfNC93cml0ZV9maWxlX3dpdGhfb3Blbl9yZWFkaW5nLm1kIiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTY5Njk3NDcxOH0.pAbY0tXv6dgSlWceY5r3HKXG_AMos8CWeYWfmCZ_CzA
