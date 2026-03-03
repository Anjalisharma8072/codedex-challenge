# Day-2

from datetime import datetime, timedelta

def blood_moon(time):
  # Write code below 💖
  format_string = '%H:%M'

  datetime_object = datetime.strptime(time,format_string)
  arr = []

  for i in range(3):
    datetime_object = datetime_object + timedelta(hours=2, minutes=48)
    arr.append(datetime_object.time().strftime("%H:%M"))

  return arr

blood_moon('1:00')