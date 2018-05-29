import rake
import io

stoppath = "Stop_Word_Lib/stopWordLib.txt"
rake_object = rake.Rake(stoppath)

sample_file = io.open("asr-result/aliasr-result/14_20180514_1600_channel_0.txt",'r',encoding="UTF-8")
text = sample_file.read()

keywords = rake_object.run(text)
print("Keywords:", keywords[:10])