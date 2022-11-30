income=int(input('เงินเดือนของคุณคือ '))
print('เงินเดือนของคุณ ',income,'บาท')
bonus=int(input('เงินเดือนของคุณคือ '))
print('เงินเดือนของคุณ ',bonus,'บาท')
pery = ((income*12)+bonus)
#Calculate all
if pery>=5000001 :
    print((((pery-5000000)*0.35)+1265000),'บาท')
elif pery>=2000001 :
    print((((pery-2000000)*0.30)+365000),'บาท')
elif pery>=1000001 :
    print((((pery-1000000)*0.25)+115000),'บาท')
elif pery>=750001 :
    print((((pery-750000)*0.20)+65000),'บาท')
elif pery>=500001 :
    print((((pery-500000)*0.15)+27500),'บาท')
elif pery>=300001 :
    print((((pery-300000)*0.10)+7500),'บาท')
elif pery>=150001 :
    print(((pery-150000)*0.05),'บาท')
else:
    print('ไม่ต้องเสียภาษี')