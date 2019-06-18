import re
# For dealing with Contents from:
# https://book.douban.com/subject/30157181/
# Book from:
# http://www.xz577.com/e/691.html
f1 = open('spark.txt', 'r')
f2 = open('spark2.txt', 'w')

for line in f1.readlines():
    after = re.sub(r'\·\·+', '@', line)
    pos = after.find('@')
    if pos != -1:
        print(after[pos+1:])
        if after[-1] == '\n':
            page_num = int(after[pos+1:-1]) + 14
        else:
            page_num = int(after[pos+1:]) + 14
        after = re.sub(r'\@[0-9]+', '@'+ str(page_num), after)

    f2.write(after)

f1.close()
f2.close()