from flask import render_template,request,jsonify
import os
from app.utils import gender_predict 


UPLOAD_FOLDER = './static/images/upload'

def upload():
    f = request.files['upload']  
    f.save(os.path.join(UPLOAD_FOLDER,f.filename))
    predict,correct = gender_predict(f.filename)
    data ={}
    data['img_name'] = f.filename
    data['predict'] = predict
    data['correct'] = correct
    print(correct)
    resp = jsonify(data)
    return resp
def index():
    data = {
        'HTML':'HTML  là một ngôn ngữ đánh dấu được thiết kế ra để tạo nên các trang web trên World Wide Web. HTML mô tả cấu trúc của một trang web về mặt ngữ nghĩa và các dấu hiệu ban đầu được bao gồm cho sự xuất hiện của tài liệu',
        'CSS':'CSS là ngôn ngữ tạo phong cách cho trang web, giúp điều khiển định dạng của nhiều trang web cùng lúc để tiết kiệm công sức cho người viết web. Nó phân biệt cách hiển thị của trang web với nội dung của trang bằng các bố cục, màu sắc và font chữ',
        'JavaScript':'Javascript được sử dụng rộng rãi trong các ứng dụng Website. Nhiệm vụ của Javascript là xử lý những đối tượng HTML trên trình duyệt. Javascript có thể làm việc được ở cả frontend và backend',
        'jQuery':'jQuery là một thư viện JavaScript được thiết kế đơn giản hóa thao tác HTML DOM, cũng như xử lý sự kiện, hoạt ảnh CSS, và Ajax.',    
        'Python':'Ngôn ngữ Python là một ngôn ngữ lập trình mã nguồn mở, đa nền tảng, dễ học dễ đọc. Python được dùng rộng rãi trong phát triển trí tuệ nhân tạo, và được ứng dụng trong nhiều lĩnh vực',
        'Flask':'Flask là một web framework, nó là một Python module cho phép bạn phát triển các ứng dụng web một cách dễ dàng, có tính mở rộng và là một microframework không bao gồm ORM (Object Relational Manager) hoặc các tính năng tương tự',
    }
    return render_template('index.html',data = data)

