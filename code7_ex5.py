file_r = open('diary.txt', 'r', encoding ="UTF-8")
file_w = open('copy.txt', 'w', encoding ="UTF-8")

for line in file_r:
    file_w.write(line)
file_r.close()
file_w.close()