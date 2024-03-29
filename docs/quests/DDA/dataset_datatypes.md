### TitanicFromDisaster

<details>
<summary>List</summary>

|No.|Variable|Definition|Key|분석가의견|
|--|--|--|--|--|
|1|PassengerId|탑승객 번호|Number|번호를 이용하여 해당 목록에 있는 인원 수 분석 가능|
|2|Pclass|등급|1,2,3|등급 수치를 이용하여 해당 등급에 있는 탑승객 분석 가능|
|3|Name|성명|String|특정 성씨나 이름을 가진 탑승객 분석 가능-같은 성씨를 가진 사람들을 구하여 가족관계 등을 파악가능|
|4|Sex|성별|male,female|성별에 따른 인원수 분석 가능-male은 m명,female은 n명|
|5|Age|나이|number|탑승객의 나이 평균 등을 분석 가능, 나이 구간별로 인원수 분석 가능|
|6|SibSp|동승한 형제 또는 배우자 수|NaN or number|몇 명의 형제나 배우자와 탑승하였는지에 해당하는 인원수를 기준으로 1명과 탑승한 인원은 m명, 2명과 탑승한 인원은 n명 등으로 분석 가능|
|7|Parch|동승한 부모 또는 아이 수|NaN or number|몇 명의 부모나 아이와 탑승하였는지에 해당하는 인원수를 기준으로 1명과 탑승한 인원은 m명, 2명과 탑승한 인원은 n명 등으로 분석 가능|
|8|Ticket|티켓 번호|String|String을 통해 어느 지역으로 가는 티켓인지 분석 가능, string 이 없는 티켓은 잘 모르겠음.|
|9|Fare|비용|number|비용값에 각각 기준을 0,10,20,30으로 정한 후 0~10 가격에 해당하는 탑승객은 몇명이 존재하는지 등 비용 간격별로 탑승객의 수 파악 가능 |
|10|Cabin|짐칸 번호|spelling + number or NaN|앞의 영어 spelling을 통해 몇번칸에 위치해있는지 파악이 가능. number를 통해 화물칸 내 번호가 몇번까지 부여되어 있는지 분석 가능. NaN을 통하여 짐칸을 사용하거나 사용하지 않는 탑승객 분석 가능|
|11|Embarked|탑승 장소|Q,S,C|도착하는 탑승 장소 별 탑승객의 인원 수, 인원 성별, 티켓 비용 평균 통계 등 분석 가능|
</details>




### SpineSurgeryList

<details>
<summary>List</summary>

|No.|Variable|Definition|Key|분석가의견|
|--|--|--|--|--|
|1|Unnamed: 0|?||환자 수 이외에는 정보 x|
|2|환자ID|환자를 식별하는 고유한 ID||환자 수 이외에는 정보 x|
|3|Large Lymphocyte|혈액 내 큰 림프구 수치를 나타내는 지표|숫자형|환자의 연령,흡연여부,고혈압여부 등에 따른 혈액내 림프구 수치의 분포를 분석|
|4|Location of herniation|탈출한 디스크의 위치|숫자형|ODI와의 상관관계를 분석|
|5|ODI|척추 통증 장애 지수로, 일상 생활에서 발생하는 제한 정도를 평가하는 지표|숫자형 or nan|탈출 디스크와의 상관관계를 분석|
|6|가족력|질병이나 유전적 소인이 부모나 가족 선조에 보이는 경우|범주형 : 0.,  1., nan|가족력에 따라 고혈압,당뇨,빈혈,신부전,암발병여부 등 질병과의 상관관계를 분석|
|7|간질성폐질환|폐 건강 상태를 나타내는 지표|범주형 : 0, 1||
|8|고혈압여부|고혈압 유무를 나타내는 지표|범주형 : 0, 1|고혈압 유무에 따라 값이 달라지는 헤모글로빈수치 등의 상관관계를 분석|
|9|과거수술횟수|과거 수술을 받은 횟수를 나타내는 지표|범주형:0, 1, 2, 3|각 횟수에 해당하는 환자를 관리|
|10|당뇨여부|당뇨병 유무를 나타내는 지표|범주형 : 0, 1|당뇨병 여부에 따른 헤모글로빈수치,혈전합병증 등의 상관관계를 분석|
|11|말초동맥질환여부|말초 동맥 질환 유무를 나타내는 지표|범주형||
|12|빈혈여부|빈혈 유무를 나타내는 지표|범주형 : 0, 1|빈혈 여부에 따른 헤모글로빈수치 등 분석|
|13|성별|남성 또는 여성 성별을 나타내는 지표|범주형 : 2, 1||
|14|스테로이드치료|스테로이드 치료 여부를 나타내는 지표|범주형 : 1, 0||
|15|신부전여부|신장 건강 상태를 나타내는 지표|범주형 : 0, 1||
|16|신장|체내 물질의 정상적인 배설을 도와주는 신장 기능을 나타내는 지표|||
|17|심혈관질환|심혈관 건강 상태를 나타내는 지표|||
|18|암발병여부|암 발생 여부를 나타내는 지표|범주형 : 0, 1||
|19|연령|나이를 나타내는 지표|숫자형|연령대 별로 구분하여 어느 질환의 분포가 많고 어느 증상을 나타내는지 통계 분석|
|20|우울증여부|우울증 유무를 나타내는 지표|범주형 : 0, 1, 2||
|21|입원기간|입원한 기간을 나타내는 지표|||
|22|입원일자|입원일을 나타내는 지표|||
|23|종양진행여부|종양의 진행 상태를 나타내는 지표|범주형 : 0, 1||
|24|직업|환자의 직업을 나타내는 지표|범주형 : '자영업', '운동선수', '특수전문직', '주부', '사업가', nan, '건설업', '운수업', '사무직','공무원', '농업', '의료직', '학생', '군인', '노동직', '교사', '예술가', '무직'|환자의 각 직업마다 걸리는 질환의 분포도를 통계 및 분석|
|25|체중|체중을 나타내는 지표|숫자형|체중과 질환의 발병 여부의 상관관계를 분석|
|26|퇴원일자|퇴원일을 나타내는 지표|||
|27|헤모글로빈수치|혈중 헤모글로빈 농도를 나타내는 지표|숫자형|헤모글로빈수치 값들 내에 여러 기준값을 정하고 질병과 헤모글로빈수치의 상관관계 분석|
|28|혈전합병증여부|혈전 합병증 유무를 나타내는 지표|범주형 : 0, 1||
|29|환자통증정도|환자의 통증 정도를 평가하는 지표|범주형 : 10,  7,  8,  9,  2,  1,  6,  5,  3,  4|환자가 갖고 있는 질환의 수와 환자의 통증 정도의 상관관계 분석|
|30|흡연여부|흡연 여부를 나타내는 지표|범주형 : 0, 1|흡연여부에 따른 암발병여부,간질성폐질환과의 상관관계를 분석|
|31|통증기간(월)|통증이 시작된 지난 기간을 나타내는 지표|||
|32|수술기법|수술 시 사용된 기술을 나타내는 지표|범주형 : 'TELD', 'IELD', nan||
|33|수술시간|수술 소요 시간을 나타내는 지표|||
|34|수술실패여부|수술 실패 여부를 나타내는 지표|범주형 : 0, 1||
|35|수술일자|수술을 받은 날짜를 나타내는 지표|||
|36|재발여부|척추 통증이 재발되었는지 여부를 나타내는 지표|범주형 : 0, 1||
|37|혈액형|환자의 혈액형을 나타내는 지표|범주형 : 'RH+A', 'RH+B', 'RH+O', 'RH+AB'||
|38|전방디스크높이(mm)|전방 디스크의 높이를 나타내는 지표|||
|39|후방디스크높이(mm)|후방 디스크의 높이를 나타내는 지표|||
|40|지방축적도|지방 축적 정도를 나타내는 지표|||
|41|Instability|척추 안정성을 나타내는 지표|||
|42|MF + ES|혼합 신경병증 및 대량 열 치료(미세파 관리 및 전기 자극)로 수행된 치료법|||
|43|Modic change|검은색과 밝은색의 조합으로 척추의 변형을 표시하는 방법으로, 척추 통증과 관련이 있을 수 있다.|범주형 : 3, 0, 2, 1||
|44|PI|척추 곡률을 나타내는 지표|||
|45|PT|척추 곡률을 나타내는 지표|||
|46|Seg Angle(raw)|	척추 각도를 나타내는 지표|||
|47|Vaccum disc|Vaccum disk는 디스크의 최종 단계로, 이 상태에서 쉽게 부러져 다른 퇴행성 디스크 질환을 유발한다.|||
|48|골밀도|골의 밀도를 나타내는 지표|||
|49|디스크단면적|디스크 단면적을 나타내는 지표|||
|50|디스크위치|디스크의 위치를 나타내는 지표|||
|51|척추이동척도|척추 이동 범위를 나타내는 지표|범주형 : 'Down', 'Up', 'Middle', 'Extremely down', 'Extremely up'||
|52|척추전방위증|척추의 사진에서 전방위증을 발견한 경우의 수준을 나타내는 지표|||
</details>