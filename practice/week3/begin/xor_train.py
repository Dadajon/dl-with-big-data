from sklearn import svm
from icecream import ic

xor_data = [
    #A, B, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# data preprocessing
data = []  # list => []
label = []  # list => []
for row in xor_data:
    first_element = row[0]
    second_element = row[1]
    third_element = row[2]
    data.append([first_element, second_element])
    label.append(third_element)

# model training
clf = svm.SVC()
clf.fit(data, label)

# model prediction
test_data = [[0, 1], [0, 1], [0, 0], [1, 1], [0, 1], [0, 1]]
test_label = [1, 1, 0, 0, 1, 1]

prediction = clf.predict(test_data)
print('예측결과:', prediction)

# 분류기 성능 평가 결과 확인하기
ok = 0
total = 0

# model evaluation
for idx, answer in enumerate(label):
    p = prediction[idx]
    if p == answer:
        ok += 1
    total += 1

print('정답률:', ok, '/', total, '=', ok/total)
