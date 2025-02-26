text = "X-DSPAM-Confidence:    0.8475"

stpos = text.find('0')

num = text[stpos:].strip()
#note: strip is unnecessary but probably good practice to ensure we don't have hidden whitespace

print(float(num))