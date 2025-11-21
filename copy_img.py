import os
import shutil
from tqdm import tqdm
import glob
import random

# コピー元のフォルダパス
source_dir = '../.cache/kagglehub/datasets/badasstechie/celebahq-resized-256x256/versions/1/celeba_hq_256'

# コピー先のフォルダパス
destination_dir = '../datasets/celeba_hq/img_celeba_hq'

# 訓練データ用のコピー先フォルダ
train_dir = '../datasets/celeba_hq/img_celeba_hq/train'

# 検証データ用のコピー先フォルダ
val_dir = '../datasets/celeba_hq/img_celeba_hq/val'

# 訓練データの割合 (80%)
train_ratio = 0.8

# 分割のランダム性を固定するためのシード値（毎回同じように分割されます）
random_seed = 42

# ----------------------------------------------------

# --- 1. ディレクトリの準備 ---
# コピー先のフォルダが存在しない場合は作成する
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# コピー元のフォルダが存在するかチェック
if not os.path.isdir(source_dir):
    print(f"エラー: コピー元のフォルダ '{source_dir}' が見つかりません。")
else:
    # --- 2. ファイルリストの取得 ---
    # コピー対象の.pngファイルリストを取得（大文字小文字を区別しないように）
    png_files = glob.glob(os.path.join(source_dir, '*.jpg'))
    # png_files.extend(glob.glob(os.path.join(source_dir, '*.PNG')))
    
    if not png_files:
        print(f"'{source_dir}' 内に.pngファイルが見つかりませんでした。")
    else:
        # --- 3. ファイルリストのシャッフル ---
        # 偏りがないように、ファイルリストをランダムにシャッフルする
        random.seed(random_seed)
        random.shuffle(png_files)

        # --- 4. 分割数の計算 ---
        total_files = len(png_files)
        split_index = int(total_files * train_ratio)

        train_files = png_files[:split_index]
        val_files = png_files[split_index:]

        print(f"合計 {total_files} 個の.pngファイルを検出しました。")
        print(f" -> 訓練用 (train): {len(train_files)} 個")
        print(f" -> 検証用 (val): {len(val_files)} 個")
        print("-" * 30)

        # --- 5. 訓練データ(train)のコピー ---
        if train_files:
            print(f"'{train_dir}' フォルダへ訓練用データをコピーしています...")
            for source_path in tqdm(train_files, desc=f"To {train_dir}", unit="file"):
                filename = os.path.basename(source_path)
                destination_path = os.path.join(train_dir, filename)
                shutil.copy2(source_path, destination_path)
        
        # --- 6. 検証データ(val)のコピー ---
        if val_files:
            print(f"\n'{val_dir}' フォルダへ検証用データをコピーしています...")
            for source_path in tqdm(val_files, desc=f"To {val_dir}", unit="file"):
                filename = os.path.basename(source_path)
                destination_path = os.path.join(val_dir, filename)
                shutil.copy2(source_path, destination_path)

        print("\n\n処理が完了しました。")