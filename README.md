# PS Plus 게임 카탈로그 만료 예정인 게임 찾기 프로그램

This program extracts the expiry date and list of the game catalog of PS Plus

# 목적

PS Plus 게임 카탈로그는 영구적으로 등록되는 게임이 아니다.
![image](https://user-images.githubusercontent.com/61766907/211231468-e86beb68-f852-47ec-8588-0be051ae7be1.png)
위 이미지에 `‘2023/2/22 오후…’` 처럼 만료일이 정해져 있는데, 만료일은 3개월 이내가 되면 사이트에 노출되어 확인할 수 있다.
그러나 만료일이 예정된 것만 따로 찾아볼 수 없으며, 리스트에서 직접 하나씩 눌러서 확인해야 하기 때문에 어떤 게임이 만료되는지 확인하기 매우매우매우 귀찮다. (약 250~300개의 게임을 모두 눌러서 확인해야 한다…)
그래서 웹스크래핑으로 모든 게임들의 목록과 PS4/PS5 지원 여부도 추출하고, 그 중에서 만료 예정일도 함께 추출하는 것이 목적이다.

---

# 기획

- 웹 스크래핑으로 PS Store 게임 카탈로그([https://store.playstation.com/ko-kr/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/1](https://store.playstation.com/ko-kr/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/1))의 정보를 수집해 모든 게임 카탈로그를 찾고, 그 중 만료 예정일을 찾는 것이 핵심이다.
- 수집할 정보
    - 커버 이미지+게임 이름, 태그(PS4/PS5 구분 또는 에디션), 만료예정일, 게임 상세정보 링크
- 정보를 추출해 웹페이지에 보기 쉽게 게임 이름 순으로 정렬 (만료일 순으로 정렬할까 하다가 만료되는 게임이 무조건 10개 미만인 것 같아 게임 이름 순으로 결정)
- 추후 필요하다면 excel로 추출하는 것도 고려

---

# 화면

![image](https://user-images.githubusercontent.com/61766907/210938004-f3727b08-2577-4d10-b97f-f101d382e316.png)