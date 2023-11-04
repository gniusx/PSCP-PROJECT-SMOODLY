"""for testing randoming text from file"""
from pyscript import document

import random
angry_txt = 'text_output/Text_output_Angry (โกรธ).txt'
#r อ่านข้อความในไฟล์
with open(angry_txt, 'r') as file:
    #ทำข้อความเป็นlist
    eachline = file.readlines()
#สุ่มจากlist
random_t = random.choice(eachline)
print(random_t)

with open('page5 output.html', 'r') as show_output:
    html_page5 = show_output.read()
html_page5 = html_page5.replace("loading for random text...", random_t)

with open('page5 output.html', 'w') as output_file:
    output_file.write(html_page5)

#แต่ต้องมากด run ก่อนอ่ะตอนนี้ ถึงจะขึ้นบนเว็บ