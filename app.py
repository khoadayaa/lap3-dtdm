# Import các thư viện cần thiết
from flask import Flask, render_template

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Route chính - Trang chủ
@app.route('/')
def home():
    """
    Render trang chủ với template index.html
    Truyền các biến vào template nếu cần
    """
    return render_template(
        'index.html',
        page_title="Lap3 của Khoa",
        welcome_message="Chào mừng bạn đến với trang web đẹp mắt này!"
    )

# Route động ví dụ
@app.route('/user/<username>')
def user_profile(username):
    """Hiển thị trang profile với username động"""
    return render_template(
        'index.html',
        page_title=f"Profile {username}",
        welcome_message=f"Xin chào {username}!"
    )

# Xử lý lỗi 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Khởi chạy server
if __name__ == '__main__':
    # Bật chế độ debug để tự động reload khi code thay đổi
    # Thêm host='0.0.0.0' nếu muốn truy cập từ các thiết bị khác trong mạng
    app.run(debug=True, port=5000)
