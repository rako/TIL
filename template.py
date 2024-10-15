import datetime
import os

#classmethod datetime.date.today() 現在のローカルな日付を返す
d_today = str(datetime.date.today()).split('-') #2020-01-01の形式で返す
year = str(d_today[0])
month = str(d_today[1])
day = str(d_today[2])
#本当はd_today.dayでいいけど、日のファイル名が一桁の場合は0がつかないので10以降のファイルの後にソートされてしまうため、'-'で分けている。
#dayのみ一桁の場合は0をつける条件にしても良いかもしれない。monthも同様になるので、これでいいかもしれない。

#mdファイルのテンプレートの中身
content = """
# Today I Learned

## Done

## Todo

## 読みたい本リスト

## 参考文献リスト
"""


#これ一行でディレクトリが存在してもエラーが出なくて、ディレクトリがない場合はディレクトリを作成してくれる
os.makedirs(f'{year}/{month}', exist_ok=True)

with open(f'{year}/{month}/{day}.md', 'x', encoding='utf-8') as f: #そのディレクトリに移動してファイルを作成
    f.write(content)

#ここにファイルに追記する処理をchrome拡張機能で書く