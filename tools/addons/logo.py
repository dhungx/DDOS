import os
from colorama import Fore as F

def show_logo(color: str = 'red') -> None:
    """In logo ứng dụng với thông điệp cảnh báo.

    Tham số:
        color (str): Màu của văn bản logo. Mặc định là 'red'.

    Trả về:
        None
    """
    logo = r"""
     __   _____ ___  ___  ___ ___   ___ _____ _   _ ___ ___ ___  
 \ \ / /_ _| _ )/ _ \/ __/ __| / __|_   _| | | |   \_ _/ _ \ 
  \ V / | || _ \ (_) \__ \__ \ \__ \ | | | |_| | |) | | (_) |
   \_/ |___|___/\___/|___/___/ |___/ |_|  \___/|___/___\___/ 
                                                             
HÃY CẨN THẬN TRƯỚC KHI SỬ DỤNG VÌ VIỆC BẠN SẮP LÀM CÓ THỂ LÀ ĐIỀU PHẠM PHÁP
ĐỪNG TẤN CÔNG TRANG WEB CHÍNH PHỦ (NHÀ NƯỚC).

PHẢI ĐẲNG CẤP THÌ MỚI TỒN TẠI ĐƯỢC!

AuThor: ViBoss Studio
Github: https://github.com/dhungx/
  """

    # Đặt màu dựa trên tùy chọn của người dùng
    color_map = {
        'red': F.RED,
        'green': F.GREEN,
        'yellow': F.YELLOW,
        'blue': F.BLUE,
        'magenta': F.MAGENTA,
        'cyan': F.CYAN,
        'white': F.WHITE,
    }

    selected_color = color_map.get(color, F.RED)  # mặc định là đỏ nếu không tìm thấy màu

    print(f"{selected_color}{logo}")
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    
    if os.name != "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├─── LAYER 2: ARP-SPOOF | DISCONNECT")
    
    print("├───┐")
    print(f"{F.YELLOW}Hãy chắc chắn rằng bạn hiểu những gì bạn đang làm!{F.RESET}")
