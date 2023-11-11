from pyscript import Element

#def send_to_py(): 
    #Element("random_show").write("ทดสอบทดสอบ")

def send_to_py(): 
    
    Element("random_show").write(f"{selected}")
#กะว่าจะแยกกัน คือตรงbuttonส่ง selected เข้ามาให้ได้ 
#แล้วปล่อยให้pyรัน ที่แปล สุ่ม นู่นนี่นั่น
#ค่อยส่งกลับตอนสุ่มเสร็จ
