txt = """https://www.atfx.com/gm/ph/new-instruments-online-notice/?s=
https://www.atfx.com/gm/ko/중국-휴일-거래-일정-안내/?s=
https://www.atfx.com/gm/ko/중국-및-독일-휴일-거래-일정-안내/?s=
https://www.atfx.com/gm/ko/새-금융상품-온라인-공지/?s=
https://www.atfx.com/gm/ar/جدول-التداول-بالعطلات-الصينية/?s=
https://www.atfx.com/gm/ms/jadual-holiday-trading-uk/?s=
https://www.atfx.com/gm/id/jadwal-trading-pada-libur-di-inggris-raya/?s=
https://www.atfx.com/gm/ph/us-uk-holidays-trading-schedules/?s=
https://www.atfx.com/gm/ms/jadual-dagangan-cuti-chinese-holiday/?s=
https://www.atfx.com/gm/zh-hant/美國假期及英國假期交易通告/?s=
https://www.atfx.com/gm/id/jadwal-trading-pada-hari-libur-china/?s=
https://www.atfx.com/gm/ar/جدول-توقيتات-عمل-الأسواق-خلال-عطلات-ال/?s=
https://www.atfx.com/gm/ms/jadual-dagangan-cuti-china-dan-germany-holiday/?s=
https://www.atfx.com/gm/ar/إشعار-بإضافة-أدوات-مالية-جديدة/?s=
https://www.atfx.com/gm/id/jadwal-trading-selama-libur-china-dan-jerman/?s=
https://www.atfx.com/gm/hi/notice-atfx-2019-daylight-saving-time/
https://www.atfx.com/gm/ms/notis-online-instrumen-baru/?s=
https://www.atfx.com/gm/id/35462/?s=
https://www.atfx.com/gm/th/ตารางการซื้อขายช่วงวัน-2/?s=
https://www.atfx.com/gm/th/ตารางวันหยุดการซื้อขาย/?s=
https://www.atfx.com/gm/th/atfx-debuts-exhibitor-vietnams-traders-fair-gala-night/?s=
https://www.atfx.com/gm/zh-hant/歡迎登陸atfxgm平台通知/?s=
https://www.atfx.com/gm/ph/united-kingdom-parliament-vote-notice-2019/
https://www.atfx.com/gm/ph/us-australian-holidays-trading-schedules/
https://www.atfx.com/gm/th/ตารางวันหยุดการซื้อขาย-2/?s=
https://www.atfx.com/gm/id/atfx-participate-traders-fair-gala-night-thailand/?s=
https://www.atfx.com/gm/th/ประกาศเกี่ยวกับตราสารต/?s=
https://www.atfx.com/gm/ar/جداول-التداول-أثناء-العطلات-في-الولاي/?s=
https://www.atfx.com/gm/ms/jadual-dagangan-us-dan-uk-holiday/?s=
https://www.atfx.com/gm/id/atfx-debuts-exhibitor-vietnams-traders-fair-gala-night/?s=
https://www.atfx.com/gm/ur/atfx-participate-traders-fair-gala-night-thailand/?s=
https://www.atfx.com/gm/ur/مصنوعہ-تصریحات-میں-تبدیلی-کا-نوٹس-اور-ن/?s=
https://www.atfx.com/gm/vi/atfx-participate-international-financeword-forum-taipei/?s=
https://www.atfx.com/gm/ar/أوقات-التداول-خلال-عطلة-استرالية/?s=
https://www.atfx.com/gm/th/ตารางการซื้อขายในช่วงว/?s=
https://www.atfx.com/gm/ph/china-germany-holidays-trading-schedules/?s=
https://www.atfx.com/gm/ph/christmas-new-year-holiday-trading-schedules/
https://www.atfx.com/gm/ph/notice-adjustment-swap-policy/
https://www.atfx.com/gm/ph/uk-parliament-vote-notice/"""

urls = txt.splitlines()
#print(urls)
count=0
total=0
useful_urls=[]
for url in urls:
    total+=1
    x = url.split('/')
    #print(x)
    if x[4]!='ug' and x[4]!='zh-hans':
        useful_urls.append(url)
        count+=1

for i in useful_urls:
    if(i[-1]=='/'):
        print(i)
    else:
        print(i[0:len(i)-4])

print(count,' useful URLs out of ',total)
