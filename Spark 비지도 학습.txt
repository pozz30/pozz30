# Spark를 이용한 비지도 학습 - 군집화


## Spark 내려 받기

- windows terminal or mac terminal을 연다. 
- 소스 코드를 다운 받을 적당한 디렉토리로 이동한다.  
- git 명령어를 이용해 Spark를 내려 받는다. 


```
git clone https://github.com/CUKykkim/data_preprocessing.git
```


 + 주의!!! 이전의 spark 컨테이너와 동일한 컨테이너를 사용하므로, 이전의 컨테이너를 종료 시키지 않았다면, 본 과정이 제대로 진행이 되지 않음
 + 이전에 소스코드를 이미 받았다면, 소스코드를 추가로 받지 말고, 받은 소스 코드의 디렉토리로 들어가서 바로 `docker-compose` 명령어를 수행
 + 이전의 컨테이너를 제대로 종료 시키지 않았다면, 다음 명령어를 사용하여 모든 컨테이너를 강제 종료

```
docker stop $(sudo docker ps -aq)
docker container prune

```



## Spark 수행하기

- git을 통해 다운 받은 디렉토리 안으로 들어간다. 

```
cd data_preprocessing
```

- `docker-compose` 명령어를 이용해 스파크 컨테이너를 띄운다. 
  
```
docker-compose up
```

- 컨테이너가 모두 수행이 되면 컨테이너는 다음과 같은 상태가 됨

```
docker ps
```

```
CONTAINER ID   IMAGE                    COMMAND                  CREATED              STATUS          PORTS
                   NAMES
edb3f8d728c9   ykkim77/spark-worker-1   "/bin/bash /worker.sh"   42 seconds ago       Up 36 seconds   0.0.0.0:8081->8081/tcp, :::8081->8081/tcp
                   spark-worker-1
349f58d01f67   ykkim77/spark-master     "/bin/bash /master.sh"   About a minute ago   Up 39 seconds   0.0.0.0:7077->7077/tcp, :::7077->7077/tcp, 6066/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   spark-master
```


- terminal 탭을 하나 더 열어, spark-master 컨테이너로 진입

```
docker exec -it spark-master /bin/bash
```

- spark가 설치된 경로의 디렉토리로 이동

```
cd  ~/../spark/bin/
```




##  spark 쉘로 수행하기


- python으로 spark을 연산을 수행할 수 있는 스파크쉘 수행

```
./pyspark
```





```
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.1.1
      /_/

Using Python version 3.7.10 (default, Mar  2 2021 09:06:08)
Spark context Web UI available at http://349f58d01f67:4040
Spark context available as 'sc' (master = local[*], app id = local-1632992284633).
SparkSession available as 'spark'.
```




## iris 데이터 로드



- iris 데이터셋
```
 caseno	        일련번호
 Sepal Length	꽃받침의 길이 정보
 Sepal Width	꽃받침의 너비 정보
 Petal Length	꽃잎의 길이 정보
 Petal Width	꽃잎의 너비 정보  
 Species	    꽃의 종류 정보  setosa / versicolor / virginica 3종류
```

![1_Qt_pYlwBeHtTewnEdksYKQ](./images/1_Qt_pYlwBeHtTewnEdksYKQ.png)

![Large53](./images/Large53.jpg)

## 군집 알고리즘의 평가 방법

- silhouette score 

![silhouette](./images/silhouette.jpg)


```
from pyspark.ml.feature import VectorAssembler


// 파일 읽기
iris = spark.read.csv('iris.csv', header = True, inferSchema = True)

// 피쳐 벡터 어셈블
assembler = VectorAssembler(
    inputCols = ["sepal_length","sepal_width","petal_length","petal_width"], outputCol = 'features')


dataset = assembler.transform(iris)

dataset.printSchema()
dataset.show()


```

## Kmenas 수행하기

```
from pyspark.ml.clustering import KMeans
kmeans = KMeans().setK(3)
model = kmeans.fit(dataset.select('features'))    // kmeans 학습
transformed = model.transform(dataset)            // 학습된 모델을 dataframe 형태로 변환
transformed.show()                                // 군집화 결과 보기
```


## Kmenas 모델 평가하기

```
from pyspark.ml.evaluation import ClusteringEvaluator
predictions = model.transform(dataset)   // 학습된 모델을 dataframe 형태로 변환
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)

print("Silhouette with squared euclidean distance = " + str(silhouette))

```

## Bisecting Kmenas 수행하기

```
from pyspark.ml.clustering import BisectingKMeans
bkm = BisectingKMeans().setK(2).setSeed(1)
model = bkm.fit(dataset.select('features'))    // bisecting kmeans 학습
transformed = model.transform(dataset)            // 학습된 모델을 dataframe 형태로 변환
transformed.show()                                // 군집화 결과 보기
```


## Bisecting Kmenas 모델 평가하기

```
from pyspark.ml.evaluation import ClusteringEvaluator
predictions = model.transform(dataset)   // 학습된 모델을 dataframe 형태로 변환
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)

print("Silhouette with squared euclidean distance = " + str(silhouette))

```

## GaussianMixture 수행하기

```
from pyspark.ml.clustering import GaussianMixture
gmm = GaussianMixture().setK(3)
model = gmm.fit(dataset.select('features'))    // kmeans 학습
transformed = model.transform(dataset)            // 학습된 모델을 dataframe 형태로 변환
transformed.show()                                // 군집화 결과 보기
```


## GaussianMixture 모델 평가하기

```
from pyspark.ml.evaluation import ClusteringEvaluator
predictions = model.transform(dataset)   // 학습된 모델을 dataframe 형태로 변환
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)

print("Silhouette with squared euclidean distance = " + str(silhouette))

```



## spark 컨테이너 종료

```
docker-compose down
```

