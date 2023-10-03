import data_processing

list_of_player_data = data_processing.read_and_transform_data()

while True:
    print("\n모드를 선택하세요:")
    print("1: 원하는 정보를 내림차순으로 출력")
    print("2: 팀별로 그룹지어서 출력")
    print("3: 선수명과 특정항목을 입력하여 해당 값을 출력")
    print("q: 종료")
    
    mode = input("> ")

    if mode == '1':
        wanted_stat = data_processing.get_wanted_stat_from_user()
        data_processing.sort_and_save_stat(list_of_player_data, wanted_stat)
    elif mode == '2':
        data_processing.group_and_save_by_team(list_of_player_data)
        pass
    elif mode == '3':
        wanted_player = input('원하는 선수명을 입력하시오 : ')
        wanted_stat = input('원하는 특정항목을 입력하시오 : ')
        data_processing.find_player_stat(list_of_player_data, wanted_player, wanted_stat)
    elif mode == 'q':
        break
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.")