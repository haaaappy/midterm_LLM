# midterm_LLM

## Base Information

**Chosen base model:** ChatGLM3-6B （unzip the THUDM.rar, and the base model's path: THUDM/chatglm3-6b）

**Training Method:** LoRA （choose the config file lora.yaml when finetuning）

## Running Basic Demo

```
cd basic_demo
python cli_demo.py
```

## Finetuning_1——Advertisement

### Dataset

**Finetuning Dataset:** AdvertiseGen Dataset（must be fixed to fit the model input shape）

**processing_code:** 处理原始数据集的代码，处理成微调数据集的格式：data_preprocessing.py

**Origin Dataset:** ./finetune_demo/data/AdvertiseGen;

**Processed Dataset:** ./finetune_demo/data/AdvertiseGen_fix

### filename

validation/test dataset: dev.json

training dataset: train.json

### Implement

通过下面的命令行，运行finetune_hf.py文件，“..THUDM/chatglm3-6b”是需要被微调的模型的路径，输出文件的位置在lora.yaml文件中设置，默认为/output

```python
cd finetune_demo
python finetune_hf.py data/AdvertiseGen_ fix/ ..THUDM/chatglm3-6b configs/lora.yaml
```

来使用AdvertiseGen_fix数据集进行chatglm3-6b的微调，令其获取优秀的服饰广告语生成能力

微调过程中的详细命令行输出过程和GPU情况，进行了截图，放在路径Screenshot/finetuning_1下

### finetuning_result

Finetuning output file at output.rar. Use it when testing the finetuned model.

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

## Finetuning_2——Story Continuation

### Dataset

**Original datasets:** Harry Potter Series, 7 books, in the path: "./HarryPotterEnglish/origin_books"

只用了前六本，因为第七本书的文件数据杂乱，数据无法清洗以获取想要的内容，所以舍弃了第七本

**Processed (Available) datasets:**  path: "./HarryPotterEnglish/datasets&processing_code"

这个路径下面还有处理原始数据用到的代码，生成可用数据集的代码，以及生成训练集测试集的代码

**File format:** TXT, after processed, turned into JSON format

#### Dataset Statistics

| Book | 1    | 2    | 3    | 4    | 5    | 6    | total |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- |
| Size | 2973 | 3244 | 4040 | 6684 | 9109 | 5633 | 31683 |

train_dataset: 30000

test_dataset: 1683

### filename

validation/test dataset: dev.json

training dataset: train.json

### Implement

通过下面的命令行，运行finetune_hf.py文件，“..THUDM/chatglm3-6b”是需要被微调的模型的路径，输出文件的位置在lora.yaml文件中设置，设置为./output_StoryContinuation_HP

```python
cd finetune_demo
python finetune_hf.py ../HarryPotterEnglish/datasets&processing_code ..THUDM/chatglm3-6b configs/lora.yaml
```

来使用自己获取并且生成的StoryContinuation_HP数据集进行大模型chatglm3-6b的微调，令其获取哈利波特世界下的故事续写能力。

微调过程中的详细命令行输出过程和GPU情况，进行了截图，放在路径Screenshot/finetuning_2下
