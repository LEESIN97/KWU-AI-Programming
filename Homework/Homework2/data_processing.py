# csv파일을 불러와 야구선스들의 data(각 categroy를 key로 가지고 있는 dictionary)를 list로 저장
def read_and_transform_data(file_path='./hw2.csv'):
    with open(file_path, 'r', encoding='utf-8-sig') as f: 
        category = f.readline()
        data = f.readlines()

    player_data = dict.fromkeys(category.strip().split(','))
    list_of_player_data = [dict.fromkeys(player_data) for _ in range(30)]

    for i in range(len(data)):
        list_of_data = data[i].strip().split(',')
        j = 0
        for key in list_of_player_data[i].keys():
            list_of_player_data[i][key] = list_of_data[j]
            j += 1
    return list_of_player_data

# User가 원하는 정보가 Category안에 있는지 확인
def get_wanted_stat_from_user():
    while True:
        wanted_stat = input('원하는 정보를 입력하시오 : ')
        if wanted_stat in ['AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SAC', 'SF']:
            return wanted_stat
        else:
            print('있는 정보에 대해서만 입력해주세요')

# Mode1 User가 특정 기록을 선택하면 선수 30명의 자료를 내림차순 후 화면에 출력 및 txt파일에 저장
def sort_and_save_stat(list_of_player_data, wanted_stat):
    wanted_stat_list = [(player['선수명'], player['팀명'], player[wanted_stat]) for player in list_of_player_data]
    sorted_wanted_stat_list = sorted(wanted_stat_list, key=lambda x: float(x[2]), reverse=True)

    with open('./wanted_stat.txt', 'w') as f: 
        for i in range(len(sorted_wanted_stat_list)):
            s = ' '.join(sorted_wanted_stat_list[i]) + '\n'
            print(s)
            f.write(s)

# Mode2 팀별로 그룹지어 화면에 출력 및 txt 파일에 저장
def group_and_save_by_team(list_of_player_data):
    team_dict = {}
    for player in list_of_player_data:
        team_name = player['팀명']
        if team_name not in team_dict:
            team_dict[team_name] = []
        team_dict[team_name].append(player)

    with open('./wanted_team.txt', 'w') as f:
        for team, players in team_dict.items():
            if team == list(team_dict.keys())[0]:
                headers = ' '.join(players[0].keys()) + '\n'
                print(headers)
                f.write(headers)
            for player in players:
                line = ' '.join(player.values()) + '\n'
                print(line)
                f.write(line)

# Mode3 선수명과 특정항목의 해당값을 화면에 출력
def find_player_stat(list_of_player_data, wanted_player, wanted_stat):
    player_found = False
    stat_found = False

    for player in list_of_player_data:
        if player['선수명'] == wanted_player:
            player_found = True
            if wanted_stat in player:
                print('선수명 :', player['선수명'])
                print(wanted_stat, ':', player[wanted_stat])
                stat_found = True
                break

    if not player_found:
        print("해당 선수를 찾을 수 없습니다.")
    elif not stat_found:
        print(f"{wanted_player}의 {wanted_stat} 정보를 찾을 수 없습니다.")
