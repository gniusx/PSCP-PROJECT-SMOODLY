"""for testing randoming text from file"""
import random
angry_txt = 'text_output/Text_output_Angry (โกรธ).txt'
#r อ่านข้อความในไฟล์
with open(angry_txt, 'r') as file:
    #ทำข้อความเป็นlist
    eachline = file.readlines()
#สุ่มจากlist
random_t = random.choice(eachline)
print(random_t)