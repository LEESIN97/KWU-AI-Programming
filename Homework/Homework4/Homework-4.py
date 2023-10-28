import matplotlib.pyplot as plt
import pandas as pd

# read data
df = pd.read_csv('./hw2.csv', encoding='utf-8-sig')

# 원하는 기록을 내림차순 출력후 파일에 저장
column_titles_list = df.columns.tolist()
column_titles_list.remove('선수명')
column_titles_list.remove('팀명')

for title in column_titles_list:
    if(title == 'SF'): print(title)
    else: print(title, end=', ')
print ('위의 목록중 원하는 데이터를 입력하시오 : ')
picked_data = input(' : ')

if(picked_data in column_titles_list):
    sorted_by_stat_df = df.sort_values(by=picked_data, ascending=False)
    print(sorted_by_stat_df[['선수명', '팀명', picked_data]].to_string(index=False))
    sorted_by_stat_df[['선수명', '팀명', picked_data]].to_csv('player_stat.csv', encoding='utf-8-sig',index=False)
    

# 자료를 팀별로 그룹지어서 화면에 출력 및 저장
sorted_by_team_df = df.groupby('팀명')
print(sorted_by_team_df)

team_dfs = {}

for team_name, group in sorted_by_team_df:
    team_dfs[team_name] = group.reset_index(drop=True)

kia_df = team_dfs['KIA']
kt_df = team_dfs['KT']
lg_df = team_dfs['LG']
nc_df = team_dfs['NC']
ssg_df = team_dfs['SSG']
doosan_df = team_dfs['두산']
lotte_df = team_dfs['롯데']
samsung_df = team_dfs['삼성']
kium_df = team_dfs['키움']
hanhwa_df = team_dfs['한화']

team_df_list = [kia_df, kt_df, nc_df, ssg_df, doosan_df, lotte_df, samsung_df, kium_df, hanhwa_df]
for df_x in team_df_list:
    team_name = df_x.iloc[0, 1]
    print('-'*37, team_name, '-'*37)
    print(df_x)
    df_x.to_csv('./team_stat/' + team_name +'.csv', index=False, encoding='utf-8-sig')
    

#선수명과 특정항목을 입력하면 해당 값을 화면에 출력
player_name = input('선수명을 입력하시오 : ')
stat = input('원하는 항목을 입력하시오 : ')

for i in range(len(df)):
    if(df.loc[i, '선수명'] == player_name):
        print('선수명 : ', df.loc[i, '선수명'])
        print(stat, ': ', df.loc[i, stat])

# 팀별로 HR값 더해서 pie 차트에 그리기(범례 표시)
hr_dict = {}

for team_df in team_df_list:
    sum = 0
    sum = team_df['HR'].sum()
    hr_dict[team_df.loc[0, '팀명']] = sum
values_team_HR = list(hr_dict.values())
team_label = list(hr_dict.keys())
print(values_team_HR)
team_label[4] = 'DOOSAN'
team_label[5] = 'LOTTE'
team_label[6] = 'SAMSUNG'
team_label[7] = 'KIUM'
team_label[8] = 'HANHWA'
print(team_label)


plt.pie(values_team_HR, labels=team_label, autopct='%.2f')
plt.show()


