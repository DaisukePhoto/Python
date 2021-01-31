
# クライアントを作成
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバー指定
    s.connect(('127.0.0.1', 50007))
    # サーバーにメッセージを送る
    s.sendall(b'I am Daisuke Noguchi')
    # ネットワークのバッファサイズは1024、サーバーからの文字列を取得
    data = s.recv(1024)

    print(repr(data))