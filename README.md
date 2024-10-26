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

微调过程中的详细命令行输出过程和GPU情况，进行了截图，放在路径Screenshot/finetuning下

### finetuning_result

> User: 写十句不同的买衣服的广告标语
>
> 1.买一件，送一件!限时特惠，抢购从速!
>
> 2.品质保证，穿上舒适，让你成为潮流焦点!
>
> 3.时尚经典，百搭实穿，让你轻松驾驭各种场合!
>
> 4.美丽冻人，美丽冷艳，让你美得冒汗!
>
> 5.美得让人心动，让你成为焦点!
>
> 6.限时抢购，错过再等一年，让你穿出个性!
>
> 7.时尚经典，穿出自己的风格，让你成为潮流的焦点!
>
> 8.穿出自信，穿出气质，让你成为别人羡慕的对象!
>
> 9.舒适时尚，穿出自己的气质，让你成为潮流的焦点!
>
> 10.品质保证，穿上舒适，让你穿出自己的个性!

让模型直接写十句不同的衣服广告语

截图记录（path: Screenshot/AdvertiseGen_result/result_1.png）

```
{"conversations": 
	[
	{"role": "user", "content": "类型#裤*风格#英伦*风格#简约"},
	{"role": "assistant", "content": "裤子是简约大方的版型设计，带来一种极简主义风格而且不乏舒适优雅感，是衣橱必不可少的一件百搭单品。标志性的logo可以体现出一股子浓郁的英伦风情，轻而易举带来独一无二的体验。"}
	]
}
```

上面是数据集中测试集中的一个数据样例，作为参照，下面是一个例子，微调后的模型生成广告语，意思明确清晰，介绍特点鲜明。

> User: 类型#裤\*风格#英伦\*风格#简约
>
> Assistant: 简约时尚的英伦风裤，整体版型简约利落，裤腿的剪裁设计，搭配上脚口的松紧带，可以随意的调整裤子的长度，穿起来舒适又方便。

这个例子是让模型生成十句不同的广告语，每一句就会相对短一些，只有两个分句。

截图记录（path: Screenshot/AdvertiseGen_result/result_2.png）

> User: 根据以下的衣服类型和风格，写十句不同的推销语句。类型#裤\*风格#英伦\*风格#简约
>
> Assistant: 1.英伦风简约裤，让你在时尚中展现自己的优雅魅力。
>
> 2.简约时尚的裤脚设计，穿起来显腿细又显腿长。
>
> 3.休闲时尚的裤脚设计，穿起来舒适又百搭。
>
> 4.简约大方的裤脚设计，穿起来显腿细又显腿长。
>
> 5.简约时尚的裤脚设计，穿起来显腿细又显腿长。
>
> 6.英伦风简约裤，让你穿出优雅的时尚感。
>
> 7.简约时尚的裤脚设计，穿起来显腿细又显腿长。
>
> 8.休闲时尚的裤脚设计，穿起来舒适又百搭。
>
> 9.简约时尚的裤脚设计，穿起来显腿细又显腿长。
>
> 10.英伦风简约裤，让你穿出优雅的时尚感。

