from datetime import datetime
from datetime import timezone
import csv
import sys
import argparse
import re

def main(config):
    # airhamlogのCSVファイル
    csv_file = open(config['csv_filepath'], encoding="utf_8")
    f = csv.DictReader(csv_file,
                       delimiter=",",
                       doublequote=True,
                       lineterminator="\r\n",
                       quotechar='"',
                       skipinitialspace=True)
    #出力ファイルを開く
    with open(f"export2turboHamLog.csv",
                'w', newline='', encoding="shift_jis") as expFile:
        writer = csv.DictWriter(expFile, 
            fieldnames=[
                'Call',
                'Date',
                'Time',
                'His',
                'My',
                'Freq',
                'Mode',
                'Code',
                'GL',
                'QSL',
                'HisName',
                'QTH',
                'Remarks1',
                'Remarks2',
                'END'
            ], quoting=csv.QUOTE_ALL)
        #1行分の処理
        for row in f:
            # JCC/JCGが抽出できるならとる。
            codes = re.findall(r'\d+', row['received_qth'])
            code = ''
            if len(codes) > 0:
                code = codes[0]
            #行オブジェクト
            writeRowObj = {
                'Call': row['callsign'],
                'Date': datetime.strptime(
                    row['qso_at'],
                    '%Y-%m-%d %H:%M:%S %z').strftime('%y/%m/%d'),
                'Time': datetime.strptime(
                    row['qso_at'],
                    '%Y-%m-%d %H:%M:%S %z').strftime('%H:%MJ'),
                'His': row['sent_rst'],
                'My': row['received_rst'],
                'Freq': re.findall(r'\d+', row['frequency'])[0],
                'Mode': row['mode'],
                'Code': code,
                'GL': '',
                'QSL': '',
                'HisName': row['received_qra'],
                'QTH' :row['received_qth'],
                'Remarks1': row['card_remarks'],
                'Remarks2': '',
                'END': '0',
            }
            writer.writerow(writeRowObj)

    return 0


def cli():
    parser = argparse.ArgumentParser(
        description='Airhamlog CSV to TurboHAMLOG CSV Converter')
    # CSVファイルパス
    parser.add_argument('csv_filepath')
    args = parser.parse_args()
    return main(vars(args))


if __name__ == '__main__':
    sys.exit(cli())
