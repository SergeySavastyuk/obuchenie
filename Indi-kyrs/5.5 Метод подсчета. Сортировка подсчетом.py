'''На вход вашей программе поступает положительное целое число n, а ваша задача вывести в порядке возрастания все цифры,
которые встречались в этом числе, и напротив каждого также необходимо вывести сколько раз данная цифра встречалась в
числе n'''
s = input() # 45654
b = [0]*10
for i in s:
    b[int(i)]+=1
for i in range(10):
    if b[i]>0:
        print(i,b[i])











