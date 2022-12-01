Income = int(input('เงินเดือน(เงินเดือนทั้งปี)ของคุณคือ '))
Income2 = int(input('เงินได้ประเภทที่สองของคุณคือ'))
tax = ((Income+Income2)*0.5)
if tax <= 100000 :
    print('เสียภาษี',tax,'บาท')
else :
    print('เสียภาษี 100,000 บาท')