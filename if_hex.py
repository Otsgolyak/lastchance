import re
outputfile='../file.txt'
my_file=open(outputfile, mode='w', encoding = 'latin_1')
my_text = '0x012345,0xa1b2c3,0xdeadbeef,0x0x0x0x,0xabcdefg,0123abcd'
text_look_for = r"[0][x][0-9a-fA-F]+\,"
all_results = re.findall(text_look_for, my_text)
print(all_results)
my_file.write(str(all_results))