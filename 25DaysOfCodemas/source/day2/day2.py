import pandas as pd
import re   

file_name = "game_data_file.txt"
result_list = []

with open(file_name, 'r') as file:
    for line in file:
        game, results = line.strip().split(':')
        game_number = int(game.split(' ')[-1])
        results = results.split(';')
        for r in results:
            green_match = re.search(r'(\d+)\s+green', r)
            red_match = re.search(r'(\d+)\s+red', r)
            blue_match = re.search(r'(\d+)\s+blue', r)

            result = {"game_number": game_number, "green": -1, "blue": -1, "red": -1 }
            if green_match:
                result['green'] = int(green_match.group(1))
            if red_match:
                result['red'] = int(red_match.group(1))
            if blue_match:
                result['blue'] = int(blue_match.group(1))
            result_list.append(result)






df = pd.DataFrame(result_list)
df['passed_game'] = ((df['red'] <= 12) & (df['blue'] <= 13) & (df['green'] <= 14))

print(df.columns)
print(df['game_number'].dtype)
df['game_number'] = df['game_number'].astype(int)

df_pct = df.groupby('game_number')['passed_game'].mean().reset_index()
total_passed_games = df_pct.query("passed_game == 1")["game_number"].sum()

print(total_passed_games)
