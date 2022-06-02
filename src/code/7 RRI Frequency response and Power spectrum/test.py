from matplotlib import pyplot as plt
from scipy.fftpack import fft, fftfreq
from RR_Class import RRClass

# open the folder
rrDataCenter = RRClass()
rrDataBase = rrDataCenter.get_data_base()
taNames = rrDataCenter.get_ta_name()
typeFiles = rrDataCenter.get_state_menu()
# print(typeFiles)

# Check is it ok
# pprint(RRDataBase['CW']['baseline'])

testData = rrDataBase['CW']['baseline']
data = list(testData)
y = fft(data)
print(y)
