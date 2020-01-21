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