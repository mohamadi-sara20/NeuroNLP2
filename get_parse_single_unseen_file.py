import os
import sys


print('=========================== syntax embeddings extraction ===========================')
path = sys.argv[1]
files = os.listdir(path)
for f in files:
    print('===========================' + f + '===========================')
    if f.endswith('.conll'):
        os.system(f'python3 experiments/parsing.py --word_embedding sskip --word_path data/sskip.eng.100.gz --mode parse --config configs/parsing/convbiaffine.json --num_epochs 10 --batch_size 5 --opt adam --learning_rate 0.001 --lr_decay 0.999995 --beta1 0.9 --beta2 0.9 --eps 1e-4 --grad_clip 5.0 --loss_type token --warmup_steps 40 --reset 20 --weight_decay 0.0 --unk_replace 0.5 --char_embedding random --model_path ./eng_final --test {path}{f}')