#!/bin/bash
#SBATCH -A kcis
#SBATCH -n 10
#SBATCH --gres=gpu:1
#SBATCH --partition=lovelace
#SBATCH --time=2-00:00:00

# set up the env
source ~/.bashrc
conda activate instagan

cd ~/cross-embodiment/instagan

python train.py --dataroot ~/cross-embodiment/data/jeans2skirt_ccp --model insta_gan --name jeans2skirt_cpp_scratch --loadSizeH 330 --loadSizeW 220 --fineSizeH 300 --fineSizeW 200 --display_id -1 --verbose ---ins_per 1 --batch_size 1

# NOTE: the additional arguments
# display_id -1 -> ensures no data being served to a visdom server
# ins_per 1 -> enforces a single instance being passed per forward pass
