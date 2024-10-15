import datetime
import os

#classmethod datetime.date.today() 現在のローカルな日付を返す
d_today = datetime.date.today().split('-') #2020-01-01の形式で返す
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


#ディレクトリの作成を監視するフラグ, これないとfor文が回るごとにディレクトリが作成されてしまうかも？
yearflag = False
monthflag = False
dayflag = False

#カレントディレクトリのなかに年月のディレクトリがあるかと日のファイルがあるかどうかを確認。該当するディレクトリとファイルがない場合は何もしないことにする。
#match case文を使ったらいいかもしれない。
for yearname in os.scandir(path='.'):
    if yearname.is_dir() and yearname == year: #yearnameがディレクトリでない場合はスキップ #年のディレクトリが一緒の場合
        yeardir = yearname
        yearflag = True
        for monthname in os.scandir(path='./yeardir'):
            if monthname.is_dir() and monthname == month:
                monthdir = monthname
                monthflag = True
                for dayname in os.scandir(path='./yeardir/monthdir'):
                    if dayname.is_file() and dayname == day:
                        dayflag = True

#年月のディレクトリがない場合は作成
if yearflag == False: #年のディレクトリがない場合
    if monthflag == False: #月のディレクトリもない場合
        os.mkdir(f'{year}/{month}')
    else:
        pass #年のディレクトリがなくて月のディレクトリがある場合はないとする
else: #年のディレクトリがある場合
    if monthflag == False: #月のディレクトリはない場合
        os.chdir('yeardir') #ここでディレクトリ移動しないで済む方法があるかもしれない
        os.mkdir('monthdir')
    else:
        pass #どちらもある場合

if dayflag == False: #日のファイルがない場合ファイルを作成
    os.chdir('yeardir/monthdir')
    with open(f'{day}.md', 'x', encoding='utf-8') as f: #そのディレクトリに移動してファイルを作成
        f.write(content)

#ここにファイルに追記する処理をchrome拡張機能で書く