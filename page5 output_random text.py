"""for testing randoming text from file"""

def trans_to_eng(thai_selected):
    """เปลี่ยนค่าที่ดึงจากไทยเป็นอังกฤษ"""
    thai_selected = thai_selected.split('เรื่อง')
    mood = {'เศร้า':'sad','โกรธ':'angry', 'น่าเบื่อ':'bored', 'กังวล':'worry', 'มีความสุข':'happy'}
    topic = {'ครอบครัว':'family','เพื่อน':'friends', 'ความรัก':'love', 'เรียน/งาน':'study-work', 'สุขภาพ':'health'}
    eng_selected = '%s-%s' %(mood[thai_selected[0]], topic[thai_selected[1]])
    return eng_selected

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

    #ใส่ข้อความที่สุ่มได้ลงใน html
    #ขอปิดไว้ก่อนน้า ถ้ากดไฟล์มันจะเปลี่ยนแล้วเปลี่ยนเลยอยู่น่ะ
    
    #with open('page5 output.html', 'r') as show_output:
        #html_page5 = show_output.read()
    #html_page5 = html_page5.replace("loading for random text...", random_t)

    #with open('page5 output.html', 'w') as output_file:
        #output_file.write(html_page5)
randomtext(trans_to_eng('น่าเบื่อเรื่องสุขภาพ'))
#เวอร์ชั่นmanual ตรงด้านในวงเล็บของจริงจะเป็นค่าที่เราดึงมาจากเว็บ

