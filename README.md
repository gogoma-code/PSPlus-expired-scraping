# PS Plus 게임 카탈로그 만료 예정인 게임 찾기 프로그램
This program extracts the expiry date and list of the game catalog of PS Plus

## 목적

PS Plus 게임 카탈로그는 영구적으로 등록되는 게임이 아니다.
만료일이 정해져 있는데, 만료일이 3개월 이내가 되면 사이트에 노출되어 확인할 수 있다.
그러나 만료일이 노출된 것만 따로 찾아볼 수 없으며, 직접 하나씩 눌러서 확인해야 하기 때문에 어떤게 만료되는지 확인하기 매우매우매우 귀찮다.
그래서 웹스크래핑으로 모든 게임들의 목록과 PS4/PS5 지원 여부도 추출하고, 그 중에서 만료 예정일도 함께 추출하는 것이 목적이다.

## 기획

1. 웹 스크래핑으로 PS Store 게임 카탈로그([https://store.playstation.com/ko-kr/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/1](https://store.playstation.com/ko-kr/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/1))의 정보를 수집해 모든 게임 카탈로그를 찾고, 그 중 만료 예정일을 찾는 것이 핵심이다.
2. 수집한 정보를 웹페이지에서 쉽게 확인할 수 있도록 만든다.

