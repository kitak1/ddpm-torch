#!/bin/bash

#SBATCH -p h100          # パーティション（キュー）を指定
#SBATCH -w h100-01       # 実行するノードを指定 (特定のノードを使いたい場合)
#SBATCH --gres=shard:1   # GRES (Generic Resource) を指定

#SBATCH -o slurm_logs/train.out
#SBATCH -e slurm_logs/train.err
# ログファイル用のディレクトリを作成

apptainer exec ../pytorch-2506-fixed.sif 

mkdir -p slurm_logs
uv run train.py --dataset celeba_hq --batch-size 32 --num-accum 2 --train-device cuda:0 --epochs 10 --image-intv 1