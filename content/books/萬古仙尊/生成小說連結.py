def to_chinese_num(n):
    units = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
    if n < 10:
        return units[n]
    elif n == 10:
        return "十"
    elif n < 20:
        return "十" + units[n % 10]
    elif n < 100:
        return units[n // 10] + "十" + units[n % 10]
    else:
        # 支援 100 ~ 999 回
        hundreds = units[n // 100] + "百"
        remainder = n % 100
        if remainder == 0:
            return hundreds
        elif remainder < 10:
            return hundreds + "零" + units[remainder]
        elif remainder == 10:
            return hundreds + "一十"
        elif remainder < 20:
            return hundreds + "一" + ("十" + units[remainder % 10])
        else:
            return hundreds + (units[remainder // 10] + "十" + units[remainder % 10])

# 修改這個數字，看您的小說目前寫到第幾回
total_chapters = 100 

with open("novel_links.txt", "w", encoding="utf-8") as f:
    for i in range(1, total_chapters + 1):
        ch_num = to_chinese_num(i)
        file_num = f"{i:02d}"  # 自動補零，如 01, 09, 10, 100
        f.write(f"* [第{ch_num}回]({file_num})\n")

print(f"成功！請打開 novel_links.txt 複製您的清單。")
