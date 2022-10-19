


## 3교시: 하나의  변수를 사용한 회귀분석

https://youtu.be/O-VkVrmUPkY

### 데이터 로드 방법

- 파일 위치: [week6 - car.csv](https://github.com/hrbae/DRB_ML_Training/blob/main/2022/week6/car.csv)

```
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/hrbae/DRB_ML_Training/main/2022/week6/car.csv')
```


## 4교시: 전진선택법을 활용한 회귀분석

https://youtu.be/8MNwdsl3AlU

### 데이터 로드 방법

- 파일 위치: [week6 - car.csv](https://github.com/hrbae/DRB_ML_Training/blob/main/2022/week6/car.csv)

```
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/hrbae/DRB_ML_Training/main/2022/week6/car.csv')
```


## 6교시: 로지스틱 회귀분석

https://youtu.be/t67FoibFA6Y

### 데이터 로드 방법

- 파일 위치: [week6 - loan.csv](https://github.com/hrbae/DRB_ML_Training/blob/main/2022/week6/Loans.csv)

```
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/hrbae/DRB_ML_Training/main/2022/week6/Loans.csv')
```



## 8교시: 의사결정나무

https://youtu.be/4ZSGv9DJFy0

### 데이터 로드 방법

- 파일 위치: [week6 - cars_part_quality.csv](https://github.com/hrbae/DRB_ML_Training/blob/main/2022/week6/cars_part_quality.csv)

```
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/hrbae/DRB_ML_Training/main/2022/week6/cars_part_quality.csv')
```


## 추가 잠고자료: 더미변수를 활용한 회귀분석

https://youtu.be/MENL8w0at6A

### 데이터 로드 방법

- 파일 위치: [week6 - car.csv](https://github.com/hrbae/DRB_ML_Training/blob/main/2022/week6/car.csv)

```
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/hrbae/DRB_ML_Training/main/2022/week6/car.csv')
```




6교시 로지스틱 회귀 시작부분 라이브러리 실행 코드(복사하셔서 사용하시면 됩니다.)
```
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rc('font', familt = 'Malgul Gothic')
```




8교시 의사결정나무 시작부분 라이브러리 실행 코드(복사하셔서 사용하시면 됩니다.)
```
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
```
