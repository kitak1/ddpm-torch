#!/bin/bash

#SBATCH -p h100          # パーティション（キュー）を指定
#SBATCH -w h100-01       # 実行するノードを指定 (特定のノードを使いたい場合)
#SBATCH --gres=shard:1   # GRES (Generic Resource) を指定

#SBATCH -o slurm_logs/copy.out
#SBATCH -e slurm_logs/copy.err
# ログファイル用のディレクトリを作成

mkdir -p slurm_logs
uv run copy_img.py