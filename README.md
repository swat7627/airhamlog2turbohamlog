# airhamlog2turbohamlog
AirHamLogからエクスポートしたCSVファイルを、TurboHAMLOGのインポート用CSVに変換するツール。

## 必要環境
- pythonスクリプトです。python実行環境が必要です。

## できること
- AirHamlog( https://air-hamlog.com/ )からCSV出力したファイルを使って、turboHAMLOGのCSV登録用CSVを作成します。

### CSV項目対応表

|TurboHamLog項目名|対応するだれでもQSLのCSV項目名|備考|
|---|---|---|
|Call|callsign||
|Date|qso_at|yy/mm/dd形式に変換します。|
|Time|qso_at|hh:mmJ形式に変換します。|
|His|sent_rst||
|My|received_rst||
|Freq|frequency|数字部分のみを抜き出しています。430Mhz→430|
|Mode|mode||
|Code|received_qth|received_qthに数値が含まれる場合のみ数値を抜き出します。|
|GL|-||
|QSL|-||
|HisName|received_qra||
|QTH|received_qth||
|Remarks1|card_remarks||
|Remarks2|-||

## 使い方

```shell
$python airhamlog2daredemoqsl.py airhamlog_csv_file 
```
- コマンド例
```shell
$python airhamlog2daredemoqsl.py airhamlog_20230212105022.csv 
```
