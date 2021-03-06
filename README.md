みんなのPython Webアプリ編 HTML版
=====================================
このリポジトリには，拙著「みんなのPython Webアプリ編」をHTML化したファイルが含まれています。書籍の本文だけでなく，サンプルコードや図も含まれています。
サンプルコードはPython 2.5をターゲットとしており，Python 2.7で動かなかったものがありました。初期コミット時に，2.7で動くように修正してあります。
また，書籍のAppendixに収録されていた，Webアプリケーションフレームワークについての解説は，情報として古くなってしまったので削除しました。
## 今後の予定
2014年度(2015年4月まで)を目処に，以下の改修を行う予定です。
+ Python 3.xに対応するよう，本文とコードを書き換え，追記
+ 古くなった部分を書き換える
+ wsgiについての解説を追加
+ サンプルコードのRSSリーダーをwsgi対応に
+ 完成したら，どこかで電子書籍として公開

### コードを3.x対応にする際の目標
+ 2から3で置き場所の変わった/名称変更されたライブラリの追従
+ ％フォーマットをformat()関数に書き換える
+ 必要十分なコメントの拡充
+ PEP8への準拠

### 本文部分の変更
+ 古くなった記述を書き換える
+ Python 2固有の解説を3向きに書き換える
+ wsgiの解説部分を追加
+ サンプルアプリのwsgi版の追加

## 協力者募集
Python3.x対応に向けて，協力者を募集します。アイデアや意見のある方(たとえば認証のハッシュがmd5じゃダメでしょ，とか)は，ぜひお寄せください。
## Licence
[MIT](http://opensource.org/licenses/mit-license.php)
## Author
[shibats](https://github.com/shibats)
