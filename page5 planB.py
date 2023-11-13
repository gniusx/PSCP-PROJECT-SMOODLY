"""สำหรับสร้าง output_dict ver.txt"""
output_dict = dict()
def randomtext(selected):
    """เสิชชื่อไฟล์ที่ตรงกับ input มาทำ list"""
    text = ('./text_output/%s.txt') %selected
    #r อ่านข้อความในไฟล์
    with open(text, 'r') as file:
        #ทำข้อความเป็นlist
        eachline = file.readlines()
    output_dict[selected] = eachline
    return
#dict จาก trans_to_eng
mood = {'เศร้า':'sad','โกรธ':'angry', 'เบื่อ':'bored', 'กังวล':'worry', 'มีความสุข':'happy'}
topic = {'ครอบครัว':'family','เพื่อน':'friends', 'ความรัก':'love', 'เรียน/งาน':'study-work', 'สุขภาพ':'health'}
for i in mood.values():
    for j in topic.values():
        filename = '%s-%s' %(i, j)
        randomtext(filename)
#ส่งdict ที่รวมข้อความ output ไป .txt
f = open('output_dict ver.txt', 'w')
f.write(str(output_dict))
f.close
