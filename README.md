# midterm_LLM

## Base Information

Chosen base model: ChatGLM3-6B

Training Method: LoRA

Finetuning Dataset: AdvertiseGen Dataset

## Dataset Preprocessing

Code: data_preprocessing.py

Origin Dataset: data/AdvertiseGen; Processed Dataset: data/AdvertiseGen_fix

validation/test dataset: dev.json

training dataset: train.json

## Model Information

ChatGLM3-6B：checkpoints

path: THUDM/chatglm3-6b

## Running Basic Demo

## Finetuning

通过下面的命令行

>  python finetune_hf.py data/AdvertiseGen_fix/ ..THUDM/chatglm3-6b configs/lora.yaml

来使用AdvertiseGen_fix数据集进行chatglm3-6b的微调，令其获取优秀的服饰广告能力

微调过程中的详细命令行输出过程和GPU情况，进行了截图，放在文件夹Screenshot_finetuning_process下
