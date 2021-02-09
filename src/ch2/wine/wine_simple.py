# 今回用いるcsvは全てのラベルにデータが分類されていない
# これは、qualityの定義が0~10にも関わらず
# 0,1,2,10のラベルのデータが存在しないということで，
# データが欠損しているという意味ではない

# また全てのラベルにデータが分類されていないとは別の意味を指すことがある。
# 予測により推定したラベルが、トレーニングデータに存在するラベル
# を充足しない状態を指す

# 
# このcsvには、データ数の分布に偏りがある
# このようなデータを不均衡データという
# これにより、実行結果がUndefinedMetricWarningとなることがある
# データが存在しないラベルがあることで、正解ラベルには存在するのに、テストラベル
# にはそのデータが存在しないなどの問題が発生し、0/0が発生しているからだ
# https://datalove.hatenadiary.jp/entry/how-to-resolve-f-score-ill-defined-error

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# データを読み込む
wine = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8")

# データをラベルとデータに分離 ---(*1)
y = wine["quality"]
x = wine.drop("quality", axis=1)

# 学習用とテスト用に分割する ---(*2)
x_train, x_test, y_train, y_test = train_test_split(
  x, y, test_size=0.2)

# 学習する ---(*3)
model = RandomForestClassifier()
model.fit(x_train, y_train)

# 評価する ---(*4)
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
print("正解率=", accuracy_score(y_test, y_pred))
