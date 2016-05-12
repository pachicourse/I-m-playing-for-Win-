#I'm playing!(for Win).

tasklistさんにお願いしてその結果をチェック、task.txtにあらかじめ登録してあるプロセスのイメージ名(以下タスク名)と同じものがあれば、
それを1時間周期で呟きます。twitterのアクセストークンとかはsecret.jsonに入れておく。
使用言語はpython3で、外部のライブラリはtwitter( https://github.com/sixohsix/twitter )を使用。

task.txtに検出したいタスク名、name.txtに呟きたい内容を入れておきます。

task.txtに入れるタスク名は、xx.exeだったらxxの部分です。タスクマネージャからプロセスのプロパティを見て確認してください。
(ex:Grand Theft Auto Vだったら、GTA5.exeとなるので、task.txtにはGTA5と書き込む)

name.txtに入れる内容は、task.txtに入力したタスク名と順序が対応づけられるようにしてください。
私がアップロードしたtask.txtとname.txtを見るのが手っ取り早いでしょう。
(検出したいタスク名はplaySNOW、それに対応して呟きたいのは"I'm playing SNOW(n時間)" なので、name.txtにはSNOWと登録してあります。特にタスク名から呟く内容を変える必要のないものでも入力しておかなければなりません。)

"タスク名"という言い方は良くないかもしれません。浅学故失礼いたします。
