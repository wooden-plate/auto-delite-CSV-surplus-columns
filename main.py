import csv
import os
from datetime import datetime

def main():
    print("=== Order Data 整形ツール（pandasなし版） ===")

    # --- ① CSVのファイル名またはパスをユーザーに聞く ---
    user_input = input("対象CSVファイル名を入力してください（同じフォルダなら名前だけでOK）: ").strip()

    # --- ② 入力がファイル名だけの場合は同一フォルダで探す ---
    # 絶対パス or 相対パスか判定
    if os.path.isabs(user_input):
        input_file = user_input
    else:
        # カレントディレクトリにあるファイルとして扱う
        input_file = os.path.join(os.getcwd(), user_input)

    # --- ③ ファイル存在チェック ---
    if not os.path.exists(input_file):
        print(f"エラー: ファイルが見つかりません → {input_file}")
        return

    # --- ④ 出力ファイル名作成 ---
    current_ymd = datetime.now().strftime("%Y%m%d")
    output_file = f"{current_ymd}_orderData.csv"

    # --- ⑤ 抽出する列（surplus以外）---
    columns_to_extract = [
        "PRID",
        "OrderNumber",
        "ItemID",
        "ItemName",
        "Quantity",
        "DeliveryDate",
        "DeliveryPlace"
    ]

    try:
        # --- ⑥ 入力CSV読み込み ---
        with open(input_file, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            input_columns = reader.fieldnames

            # 必要な列が存在するかチェック
            missing = [c for c in columns_to_extract if c not in input_columns]
            if missing:
                print(f"エラー: 以下の必要列が CSV に存在しません → {missing}")
                return

            # --- ⑦ 出力CSV書き込み ---
            with open(output_file, "w", newline='', encoding="utf-8") as out_f:
                writer = csv.DictWriter(out_f, fieldnames=columns_to_extract)
                writer.writeheader()

                for row in reader:
                    filtered_row = {col: row[col] for col in columns_to_extract}
                    writer.writerow(filtered_row)

    except Exception as e:
        print("エラー: CSV の処理中に問題が発生しました。")
        print("詳細:", e)
        return

    print(f"\n成功！ {output_file} を作成しました。")


if __name__ == "__main__":
    main()
