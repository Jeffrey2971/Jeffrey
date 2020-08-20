import tushare

dataNow = tushare.get_realtime_quotes('000591')

print(dataNow)