k1=[31.0, 72, 105.0, 581.5, 0, 0, 0]
newk1= k1[::-1]
for i in range(len(newk1)):
    if newk1[i]>0:
        newk1[i] += 100
        break
print("Newk1", newk1 )