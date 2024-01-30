import pandas as pd


data_SpineSurgeryList =  pd.read_csv("./csv/SpineSurgeryList.csv")  # csv 읽기
df_SpineSurgeryList = pd.DataFrame(data_SpineSurgeryList)           # csv파일을 dataframe화
df_SpineSurgeryList.info()                                          # df 정보 읽기
df_SpineSurgeryList[["체중","신장"]]                                 # df 내 해당 컬럼 확인

def BMI(params):                                                    # BMI 구하기 function
    weight = params.loc["체중"]
    tall = params.loc["신장"]*0.01		
    result = weight/tall**2
    return result
df_SpineSurgeryList["BMI"] = df_SpineSurgeryList[["체중", "신장"]].apply(BMI, axis=1)   # df안에 BMI 컬럼 생성

df_SpineSurgeryList.info()                                          # BMI 컬럼 생성 확인
print(df_SpineSurgeryList["BMI"])

# BMI
# 0       22.695623
# 1       24.520365
# 2       24.334049
# 3       24.507861
# 4       24.097465
#           ...
# 1889    25.964542
# 1890    23.936062
# 1891    25.099502
# 1892    24.577867
# 1893    17.361111
