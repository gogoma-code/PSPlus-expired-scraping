def save_to_file(file_name, games):
    file = open(f"{file_name}.csv", "w", encoding="utf8")

    file.write("game_name,game_tags,ps_expired,sub_url\n")
    for game in games:
        if type(game['game_tags']) is list:
            game_tags = ':'.join(game['game_tags'])
        
        file.write(f"{game['game_name']},{game_tags},{game['ps_expired']},{game['sub_url']}\n")

    file.close()
