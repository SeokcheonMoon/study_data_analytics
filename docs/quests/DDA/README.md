|No.|Variable|Definition|Key|분석가의견|
|--|--|--|--|--|
|1|PassengerId|탑승객 번호||번호는 unique value이기 때문에 분석에는 애매함|
|2|Pclass|등급|1,2,3|등급 수치를 이용하여 해당 등급에 있는 탑승객 분석 가능|
|3|Name|성명||특정 성씨나 이름을 가진 탑승객 분석 가능- 같은 성씨를 가진 사람들을 구한다던지 등|
|4|Sex|성별|male,female||
|5|Age|나이|||
|6|SibSp|동승한 형제 또는 배우자 수|NaN or number|동승한 형제 또는 배우자의 수, 즉 number만큼  |
|7|Parch|동승한 부모 또는 아이 수|NaN or number||
|8|Ticket|티켓 번호|||
|9|Fare|비용|number|비용값에 각각 기준을 0,10,20,30으로 정한 후 0~10 가격에 해당하는 탑승객은 몇명이 존재하는지 등 비용 간격별로 탑승객의 수 파악 가능 |
|10|Cabin|짐칸 번호|spelling + number,NaN|앞의 영어 spelling을 통해 몇번칸에 위치해있는지 파악이 가능. number를 통해 화물칸 내 번호가 몇번까지 부여되어 있는지 분석 가능. NaN을 통하여 짐칸을 사용하거나 사용하지 않는 탑승객 분석 가능|
|11|Embarked|탑승 장소|Q,S,C||