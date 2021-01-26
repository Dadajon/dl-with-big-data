from sklearn import model_selection, svm, metrics

def load_csv(fname):
    labels = []
    images = []

    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2:
                # 28x28 
                continue
            # a = [0, 1, 1] -> a[0] -> ctrl+c ctrl+v
            # a = [0, 1, 1] -> a.pop(0) -> a = [1, 1] -> ctrl+x ctrl+v
            labels.append(int(cols.pop(0)))
            # white and black image pixel values [0, 255]
            # normalization
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)

    return {"labels": labels, "images": images}

data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

clf = svm.SVC()
# train
clf.fit(data["images"], data["labels"])

# evaluation
predict = clf.predict(test["images"])

ac_score = metrics.accuracy_score(test["labels"], predict)
# classification report 
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 = ", ac_score)
print("리포트 =")
print(cl_report)