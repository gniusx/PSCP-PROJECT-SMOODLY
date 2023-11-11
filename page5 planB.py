"""แผนสำรองเพราะเหมือนpyscriptจะเปิดไฟล์ไม่ได้"""
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
randomtext("angry-family")
randomtext("angry-friends")
randomtext("angry-health")
randomtext("angry-love")
randomtext("angry-study-work")

randomtext("bored-family")
randomtext("bored-friends")
randomtext("bored-health")
randomtext("bored-love")
randomtext("bored-study-work")

randomtext("happy-family")
randomtext("happy-friends")
randomtext("happy-health")
randomtext("happy-love")
randomtext("happy-study-work")

randomtext("sad-family")
randomtext("sad-friends")
randomtext("sad-health")
randomtext("sad-love")
randomtext("sad-study-work")

randomtext("worry-family")
randomtext("worry-friends")
randomtext("worry-health")
randomtext("worry-love")
randomtext("worry-study-work")
f = open('output_dict ver.txt', 'w')
f.write(str(output_dict))
f.close
