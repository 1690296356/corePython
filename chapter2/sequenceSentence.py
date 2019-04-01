#以正确的宽度在居中的“盒子”内打印一个句子
#注意，整数除法运算符（//）只能用在python2.2以及后续版本在之前的版本中，只使用普通除法（/）

sentence = input("sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width +6
left_margin = (screen_width - box_width) //2

print()
print(''*left_margin+'+'+'-'*(box_width-4)+ ' +')
print(''*left_margin+'|'+' '*text_width+ ' |')
print(''*left_margin+'|'+sentence+ ' |')
print(''*left_margin+'|'+' '*text_width+ ' |')
print(''*left_margin+'+'+'-'*(box_width-2)+ ' +')
print()

