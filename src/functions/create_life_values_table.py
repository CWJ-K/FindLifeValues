from typing import List

def create_life_values_table() -> List:
    LIFE_VALUES = [
        '公平', '敏感', '公正', '務實', '耐心', '專業', '獨立', '信任',
        '自律', '志願', '溫暖', '堅持', '能量', '誠實', '流行', '教育',
        '利他', '名氣', '安全', '穩定', '友誼', '強烈', '希望', '無懼',
        '健康', '力量', '忠誠', '啟發', '毅力', '靈活', '守諾', '控制',
        '魅力', '長壽', '透明', '智慧', '探索', '細心', '奇蹟', '自由',
        '平衡', '意義', '和諧', '多元', '負責', '善良', '快樂', '權威',
        '團隊', '競爭', '努力', '直覺', '熱情', '真理', '敏銳', '冒險',
        '美德', '效率', '開放', '美麗', '同理', '獨特', '活力', '和平',
        '樂觀', '權力', '溫柔', '創造', '家庭', '忠貞', '性感', '挑戰',
        '平安', '滿足', '愛', '創新', '同情', '速度', '高貴', '影響力',
    ]
    
    life_values_table = []
    break_ = 1
    for value in LIFE_VALUES:

        if break_ == 8:
            if len(value) == 3:
                row =  value + '| \n'
            else:
                row = '  ' + value + '| \n' 
            break_ = 1
        else:
            if len(value) == 1:
                row = '    '+ value + '|'
                
            else:
                row = '  ' + value + '|'
            break_ += 1
        life_values_table.append(row)


    life_values_table = ('').join(life_values_table)

    print(life_values_table)
    
    return LIFE_VALUES