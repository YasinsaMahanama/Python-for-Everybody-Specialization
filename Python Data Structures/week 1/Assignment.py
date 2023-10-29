text = "X-DSPAM-Confidence:    0.8475"
colon_pos = text.find(':')

number_str = text[colon_pos + 1:]

number_str = number_str.strip()

number = float(number_str)

print(number)
