import datetime
time_str = datetime.datetime.now().isoformat()
print(time_str)

starttime = datetime.datetime.now()

#long running

endtime = datetime.datetime.now()

print ((endtime - starttime).seconds)