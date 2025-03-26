import pywhatkit as pwk

phone_number = '+919876543210'
message = 'this is a automation message'

time_hour = 11  #hours
time_min = 31   #minutes

pwk.sendwhatmsg(phone_number,message,time_hour,time_min)
