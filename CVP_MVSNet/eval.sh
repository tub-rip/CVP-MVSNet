# Shell script for evaluating the CVP-MVSNet
# by: Jiayu Yang
# date: 2019-08-29

# Dataset
DATASET_ROOT="./dataset/dtu-test-1200/"

# Checkpoint
LOAD_CKPT_DIR="./checkpoints/pretrained/model_000027.ckpt"

# Logging
LOG_DIR="./logs/"

# Output dir
OUT_DIR="./outputs_pretrained/"

python3 eval.py \
\
--info="eval_pretrained_e27" \
--mode="test" \
\
--dataset_root=$DATASET_ROOT \
--imgsize=128 \
--nsrc=3 \
--nscale=5 \
\
--batch_size=1 \
\
--loadckpt=$LOAD_CKPT_DIR \
--logckptdir=$CKPT_DIR \
--loggingdir=$LOG_DIR \
\
--outdir=$OUT_DIR