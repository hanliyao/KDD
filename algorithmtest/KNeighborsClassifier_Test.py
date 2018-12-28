from sklearn.neighbors import KNeighborsClassifier
from time  import time
from preprocess import dataRead
from preprocess import digital
from sklearn.metrics import accuracy_score

def TrainKNeighbors(data):
    """
    
    :param data: 
    :return: 
    """
    types = data['types'].copy()
    types[types != 'normal.'] = 'attack.'
    features = digital.contious_features(data)
    clf = KNeighborsClassifier(n_neighbors=5, algorithm='ball_tree', leaf_size=500)
    t0 = time()
    clf.fit(features, types)
    tt = time() - t0
    print("Classifier trained in {} seconds".format(round(tt, 3)))
    return clf

def TestKNeighbors(data,model):
    types = data['types'].copy()
    types[types != 'normal.'] = 'attack.'
    features = digital.contious_features(data)
    t0 = time()
    predict = model.predict(features)
    tt = time() - t0
    print("Predicted in {} seconds".format(round(tt, 3)))
    ## 检查测试精度
    acc = accuracy_score(predict, types)
    print("R squared is {}.".format(round(acc, 4)))

if __name__ == "__main__":
    Traindata = dataRead.corrected()
    model = TrainKNeighbors(Traindata)
    TestData = dataRead.full_data()
    TestKNeighbors(TestData,model=model)