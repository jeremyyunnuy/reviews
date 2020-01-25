data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 10000 == 0: # %用來求餘數
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0]) #印出清單第0個位置

# 文字計數

wc ={} # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    word = input('查詢的關鍵字: ')
    if word == 'q':
    	break
    if word in wc:
    	print(word, '出現過的次數為: ', wc[word])
    else:
    	print('這個字沒有出現過!')
 print('查詢結束')


    sum_len = 0
    for d in data:
        sum_len += len(d)
    print('留言的平均長度為', sum_len/len(data))
    # 以下為篩選 小於100
    new = [] #新增新的清單  
    for d in data: # 把清單中的東西一個一個拿出來
        if len(d) < 100:
            new.append(d) # 加入到新的新單裡面
    print('一共有', len(new), '筆留言長度小於100')
    print(new[0])
    print(new[1])

    good = []
    for d in data:
        if 'good' in d:
            good.append(d)
    print('一共有', len(good), '筆留言提到good')

# 'a' in 'abc' --> True    
# 'x' in 'abc' --> False 