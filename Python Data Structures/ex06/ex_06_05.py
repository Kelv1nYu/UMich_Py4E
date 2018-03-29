# extract the number at the end of the line below.

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('.')
st = text[pos - 1:]
ft = float(st)
print(ft)
