# socket server作成
import socket

# AF = IPv4 という意味
# TCP/IPの場合は、SOCK_STREAMを使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポート指定
    s.bind(('127.0.0.1', 50007))
    # 1 接続
    s.listen(1)
    # connectionするまで待つ
    while True:
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn, addr = s.accept()
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print('data: {}, addr: {}'.format(data, addr))
                # クライアントにデータを返す(b -> byteでないといけない)
                conn.sendall(b'Received: ' + data)