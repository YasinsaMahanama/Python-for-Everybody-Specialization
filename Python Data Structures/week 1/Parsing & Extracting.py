data = 'From stephen.marquard@uct.ac.za sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)                                         # 21

sppos = data.find(' ', atpos)
print(sppos)                                 # 31

host = data[atpos+1 : sppos]
print(host)                           # uct.ac.za
