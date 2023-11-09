"""ขอร้อง ขึ้นไฟล์ไว้ก่อน เดี๋ยวกลับมาทำ"""
#ว่าจะลองตามนี้ https://youtu.be/AEM8_4NBU04?si=cZLOxpig6s30LwvC
from flask import Flask, request
app = Flask(__name__)

@app.route('/send_selected', methods=['POST'])
def receive_selected():
    html_selected = request.get.data(as_text=True)
    #ลองทำตามตัวอย่างอ่ะ แสดงค่าไปไฟล์text
    with open('output.txt', 'w') as file:
        file.write(html_selected)
    return 'ส่งข้อมูลสำเร็จ'
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)