"""for testing randoming text from file"""

def receive_selected():
    html_selected = request.get.data(as_text=True)
    #ลองทำตามตัวอย่างอ่ะ แสดงค่าไปไฟล์text
    with open('output.txt', 'w') as file:
        file.write(html_selected)
    return 'ส่งข้อมูลสำเร็จ'

def randomtext(selected):
    """เสิชชื่อไฟล์ที่ตรงกับ input มาทำ list"""
    import random
    text = ('text_output/text set_new/%s.txt') %selected
    #r อ่านข้อความในไฟล์
    with open(text, 'r') as file:
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
randomtext("angry-family")
#แต่ต้องมากด run ก่อนอ่ะตอนนี้ ถึงจะขึ้นบนเว็บ

