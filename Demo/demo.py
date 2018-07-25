# print("hello python")


# # 数据类型
# a = 1
# # 变量类型为数字int 
# b = "1"
# # 当带了引号的时候，变量类型为字符串，str
# c = [1, 2, 3, "汉字", [1, 2, 3], {' a ': 1}]
# # 数组，数组可以放任何东西进去。 
# d = {' a ': 111} 
# # 字典，在其他语言里面叫对象,key:value，d={'a':{'b':111}} f = () #元祖，和数组很像，但是不可以修改
# print(c[4][1]) 
# print(d["a"]) 
# print(d.get("a"))

# 九九乘法表
# for循环：for属于一种遍历，
# a = [1,2,3,4]
# for i int a:
# 	print(i)

# range函数,
# c = range(1,5) #1,2,3,4
# c = range(5)  #0,1,2,3,4

# python中以空格来区分代码块。
# """
# num = input("请输入你要的值：")
# print(type(num))

# cfb = ""
# for i in range(1,int(num)):
# 	for j in range(1,int(num)):
# 		if i >= j
# 			cfb += "%dX%d=%d"%(i,j,i*j)
# 	cfb +="\n"
# print(cfb)
# """


# 外边一层循环控制行数
# i是行数
i = 1
while i <= 9:
     # 里面一层循环控制每一行中的列数
     j = 1
     while j <= i:
          mut = j*i
          print("%d*%d=%d"%(j, i, mut), end="  ")
          j += 1
     print("")
     i += 1



# python 冒泡排序

def paixu(li) :
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                max = li[x]
                li[x] = li[x + 1]
                li[x + 1] = max
            else:
                max = li[x + 1]
    print(li)
paixu([41,23344,9353,5554,44,7557,6434,500,2000])



import random
while 1:
    s=int(random.randint(1,3))
    if s==1:
        ind="石头"
    elif s==2:
        ind="剪刀"
    elif s==3:
        ind="布" 
    m=input('输入石头，剪刀，布，输入end结束游戏：')
    
    blist=['石头','剪刀','布']
    
    if(m not in blist) and (m!='end'):
        print("输入错误，重试：")
    elif(m=='end')and(m not in blist):
        print(ind)
        print("\n游戏退出")
        break
    elif m==ind:
        print("平")
    elif (m == '石头' and ind =='剪子') or (m == '剪子' and ind =='布') or (m == '布' and ind =='石头'):
        print ("电脑出了： " + ind +"，你赢了！")
    else:
        print ("电脑出了： " + ind +"，你输了！")




# if True:
#     print ("True")
# else:
#     print ("False")

# input("\n\n按下 enter 键后退出。")

# a = 888
# print(isinstance(a, int))
# # del a
# print(isinstance(a, int))

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print("对应人类年龄: ", human)
 
# # 退出提示
# input("点击 enter 键退出")


print('----欢迎使用BMI计算程序----')
name = input('请键入您的姓名:')
height = eval(input('请键入您的身高(m):'))
weight = eval(input('请键入您的体重(kg):'))
gender = input('请键入你的性别(F/M)')
BMI = float(float(weight)/(float(height)**2))
# 公式
if BMI <= 18.4:
    print('姓名:', name, '身体状态:偏瘦')
elif BMI <= 23.9:
    print('姓名:', name, '身体状态:正常')
elif BMI <= 27.9:
    print('姓名:', name, '身体状态:超重')
elif BMI >= 28:
    print('姓名:', name, '身体状态:肥胖')