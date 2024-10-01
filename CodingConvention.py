def    calc(a, b): # Tên hàm không mô tả rõ chức năng và thụt lề sai cách
    # Tính tổng => Không mô tả rõ ràng chức năng cụ thể của mã bên dưới
    c=a+b # Không có khoảng trắng khiến code khó đọc và tên biến không rõ ràng
    return
    c; # Kết thúc bằng dấu chấm phẩy không cần thiết


def CALCULATEtotalprice(itemlist): # Tên hàm không tuân theo quy tắc đặt tên thống nhất
    total = 0
    for i in itemlist:
                total+=i.price # thụt lề quá sâu
    return total
