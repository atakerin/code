tid1 = input("första tiden (tt:mm): ")
tid2 = input("andra tiden(tt:mm): ")

timme1 = int(tid1[0:2])
minute1 = int(tid1[3:5])
timme2 = int(tid2[0:2])
minute2 = int(tid2[3:5])

minute1 += timme1 * 60
minute2 += timme2 * 60
if minute2 < minute1:
    minute2 += 24 * 60
    
print(F'detr är {minute2-minute1} minuter mellan {tid1} och {tid2}')