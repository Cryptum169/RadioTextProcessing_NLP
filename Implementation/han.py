from pyhanlp import *
import src.readFile as rf

with open("data/5.txt") as fp:
    text = fp.read()

print(HanLP.extractSummary(text, 5))