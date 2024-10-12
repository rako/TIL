import datetime
import os

d_today = datetime.date.today()
year = str(d_today.year)
month = str(d_today.month)
day = str(d_today.day)

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

#カレントディレクトリのなかに年月のディレクトリがあるかと日のファイルがあるかどうかを確認
for yearname in os.scandir(path='.'):
    if yearname.is_dir(): #yearnameがディレクトリでない場合はスキップ
        if yearname == year: #年のディレクトリが一緒の場合
            yeardir = yearname
            yearflag = True
            for monthname in os.scandir(path='./yeardir'):
                if monthname.is_dir():
                    if monthname == month:
                        monthdir = monthname
                        monthflag = True
                        for dayname in os.scandir(path='./yeardir/monthdir'):
                            if dayname.is_file():
                                if dayname == day:
                                    dayflag = True

#年月のディレクトリがない場合は作成
if yearflag == False: #年のディレクトリがない場合
    if monthflag == False: #月のディレクトリもない場合
        os.mkdir(f'{year}/{month}')
    else:
        pass #年のディレクトリがなくて月のディレクトリがある場合はないとする
else: #年のディレクトリがある場合
    if monthflag == False: #月のディレクトリはない場合
        os.chdir('yeardir')
        os.mkdir('monthdir')
    else:
        pass #どちらもある場合

if dayflag == False: #日のファイルがない場合ファイルを作成
    os.chdir('yeardir/monthdir')
    with open(f'{day}.md', 'x', encoding='utf-8') as f: #そのディレクトリに移動してファイルを作成
        f.write(content)

#ここにファイルに追記する処理をchrome拡張機能で書く