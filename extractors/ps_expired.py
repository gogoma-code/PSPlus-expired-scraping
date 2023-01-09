import requests
from bs4 import BeautifulSoup

# 전체 페이징 순환
def extract_ps_expired_paging():
    ps_url = "https://store.playstation.com"
    url = f"{ps_url}/ko-kr/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/1"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15"})

    games = []
    
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        page_button_list = soup.find_all("button", {"class": "psw-page-button"})

        # 전체 페이지 수 추출
        last_page_value = int(page_button_list[len(page_button_list) - 1]["value"])
        
        for i in range(last_page_value):
            games = extract_ps_expired(games, i+1)

        # 게임 이름으로 정렬
        games =  sorted(games, key=lambda d: d['game_name'])
    return games

def extract_ps_expired(games, page):
    ps_url = "https://store.playstation.com"
    url = f"{ps_url}/ko-kr/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/{page}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15"})

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        
        psw_grid_list = soup.find("ul", {"class": "psw-grid-list"})
        
        psw_content_link_list = psw_grid_list.find_all("a", {"class": "psw-content-link"})
        for psw_content_link in psw_content_link_list:
            psw_cover_list = psw_content_link.find_all("img", {"class": "psw-l-fit-cover"})
            psw_cover = psw_cover_list[0]["src"]

            href = psw_content_link["href"]
            href = href.replace("/en-us", "/ko-kr")
            sub_url = ps_url + href
        
            res_detail = requests.get(sub_url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15"})
            if res_detail.status_code == 200:
                soup_detail = BeautifulSoup(res_detail.text, "html.parser")
                
                game_title = soup_detail.find("div", {"class": "pdp-game-title"})
                area_game_name = game_title.find("h1")
                area_game_tag_list = game_title.findAll("span", {"class": "psw-t-tag"})
                area_cta = soup_detail.find("div", {"class": "pdp-cta"})
                area_ps_plus = area_cta.find("span", {"class": "psw-c-t-ps-plus"})
                if area_ps_plus is not None:
                    area_ps_plus_parent = area_ps_plus.find_parent("span", {"class": "psw-l-line-wrap"})
                    area_ps_expired = area_ps_plus_parent.find("span", {"class": "psw-c-t-2"})
                else:
                    area_ps_expired = None
                
                game_name = area_game_name.get_text()
                
                game_tags = []
                for area_game_tag in area_game_tag_list:
                    game_tags.append(area_game_tag.get_text())
                
                ps_expired_flag = False
                ps_expired = "종료 예정 없음"
                if area_ps_expired is not None:
                    ps_expired_flag = True
                    ps_expired = area_ps_expired.get_text()

                game = {
                    "game_name": game_name,
                    "game_tags": game_tags,
                    "ps_expired_flag": ps_expired_flag,
                    "ps_expired": ps_expired,
                    "psw_cover": psw_cover,
                    "sub_url": sub_url
                }
                games.append(game)
        
    return games