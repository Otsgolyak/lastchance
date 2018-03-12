import re
my_text = 'mfn-fulfillable-quantity, afn-fulfillable-quantity, afn-total-quantity, afn-inbound-receiving-quantity, per-unit-volume, mfn-listing-exists, afn-listing-exists'
text_look_for = r'[a|mfn]+[\-+[\w+\-+\w]+\-+r[quantity]+'
all_results = re.findall(text_look_for, my_text)
print(all_results)
