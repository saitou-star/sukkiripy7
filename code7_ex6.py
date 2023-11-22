from random import randint as r

print('数当てゲームを始めます。３桁の数を当ててください！')



answer = list()
for n in range(3):
    answer.append(r(0, 9))
# answer = [r(0, 9) for n in range(3)]  上の三行をこの一文で出来る。　内包表記



is_continue = True
while is_continue == True:

    prediction = []
    for n in range(3):
        data = int(input(f'{n + 1}桁目の予想を入力(0~9) >>'))
        prediction.append(data)

    hit = 0
    blow = 0
    for n in range(3):
        if prediction[n] == answer[n]:
            hit += 1
        else:
            for y in range(3):
                if prediction[n] == answer[y]:
                    blow += 1
                    break

    print(f'{hit}ヒット、{blow}ボール！')
    if hit == 3:
        print('正解です！')
        is_continue = False
    else:
        if int(input('続けますか？ 1:続ける  2:終了  >>')) == 2:
            print(f'正解は{answer[0]}{answer[1]}{answer[2]}')
            is_continue = False



