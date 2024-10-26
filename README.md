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

![image-result_1](F:\midterm_LLM\Screenshot\AdvertiseGen_result\result_1.png)

上面的图片（path: Screenshot/AdvertiseGen_result/result_1.png）是令模型直接写十句不同的衣服广告语。

```
{"conversations": 
	[
	{"role": "user", "content": "类型#裤*风格#英伦*风格#简约"},
	{"role": "assistant", "content": "裤子是简约大方的版型设计，带来一种极简主义风格而且不乏舒适优雅感，是衣橱必不可少的一件百搭单品。标志性的logo可以体现出一股子浓郁的英伦风情，轻而易举带来独一无二的体验。"}
	]
}
```

上面是数据集中测试集中的一个数据样例，作为参照，下图中第一个例子给出的生成的广告语，意思明确清晰，介绍特点鲜明。

下图中（path: Screenshot/AdvertiseGen_result/result_2.png）第二个例子是让模型生成十句不同的广告语，每一句就会段一些，只有两个分句了。

![image-result_2](F:\midterm_LLM\Screenshot\AdvertiseGen_result\result_2.png)
