def a(txt):
  def binadd(arr,count):
    if arr[count] == 0:
      arr[count] = 1
      return arr
    else:
      arr[count] = 0
      return binadd(arr,count+1)
  
  qry = [0]*len(txt)
  comb = [0]*(2**len(txt)-1)
  
  for i, iitem in enumerate(comb[:-1]):
  #is the first combination there?
    for j, jitem in enumerate(qry):
      if qry[j]:
        if txt[j]:
          comb[i] = 1
        else:
          comb[i] = 0
          break
    qry = binadd(qry,0)
  else:
    for k, kitem in enumerate(qry):
      if kitem:
        if txt[k]:
          comb[-1] = 1
        else:
          comb[-1] = 0
          break

  return comb

if __name__ == "__main__":
  text = [1]
  print(text)
  comb = a(text)
  print(comb)

'''
lcount = 0
for l in text:
  if l == 1:
    lcount += 1

mcount = 0
for m in comb:
  if m == 1:
    mcount += 1

lpercent = (float(lcount)/float(len(text)))*100
mpercent = (float(mcount)/float((len(comb)-1)))*100

print ("text active nodes percent")
print (lpercent)
print ("combinations active nodes percent")
print (mpercent)
'''