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

#### Dataset Construction

##### An example of dataset

```json
{
	"conversation": [
		{
			"role": "user",
			"content": "I request that you craft a continuous, logical narrative following this sentence in English. 'Harry waited for the blow to fall.'"
            #一句说明续写任务的话＋需要进行续写的句子
		},
		{
			"role": "assistant",
			"content": "Harry waited for the blow to fall. 'So...' said Snape softly. 'We'll see about this....' He strode across to his fire, seized a fistful of glittering powder from a jar on the fireplace, and threw it into the flames. 'Lupin!' Snape called into the fire. 'I want a word!' Utterly bewildered, Harry stared at the fire. A large shape had appeared in it, revolving very fast. Seconds later, Professor Lupin was clambering out of the fireplace, brushing ash off his shabby robes. 'You called, Severus?' said Lupin mildly. 'I certainly did,' said Snape, his face contorted with fury as he strode back to his desk. 'I have just asked Potter to empty his pockets. He was carrying this.' Snape pointed at the parchment, on which the words of Messrs. Moony, Wormtail, Padfoot, and Prongs were still shining. An odd, closed expression appeared on Lupin's face. 'Well?' said Snape. Lupin continued to stare at the map. Harry had the impression that Lupin was doing some very quick thinking. 'Well?' said Snape again. 'This parchment is plainly full of Dark Magic. This is supposed to be your area of expertise, Lupin. Where do you imagine Potter got such a thing?' Lupin looked up and, by the merest half-glance in Harry's direction, warned him not to interrupt. 'Full of Dark Magic?' he repeated mildly. 'Do you really think so, Severus? It looks to me as though it is merely a piece of parchment that insults anybody who reads it. Childish, but surely not dangerous? I imagine Harry got it from a joke shop --' 'Indeed?' said Snape. His jaw had gone rigid with anger. 'You think a joke shop could supply him with such a thing? You don't think it more likely that he got it directly from the manufacturers?' Harry didn't understand what Snape was talking about. Nor, apparently, did Lupin." 
            #原来的这个句子及其后面的故事
		}
	]
}
```

##### Random Prompt

利用GPT-4生成了十句表述不同意思相同的提示性语句，告诉模型下面需要根据给出的句子进行续写。在构建数据集时，随机挑选一句作为提供给模型的提示性语句，告诉模型要完成续写任务。

##### Constructing Method

> ./HarryPotter_en_get.py：将单个txt文件中的原始数据转为JSON格式的数据
>
> ./gather_and_split.py：将上述得到的多个JSON数据集合并成哈利波特故事续写数据集StoryContinuation_HP，并划分训练集和测试集

由于书本对话较多，且分段比较频繁，一段话的平均只有28个词；为了数据集构建的便利，提取txt中每一段话的第一句话作为需要续写的句子，从它开始的连续段落，要求加起来超过300词，作为续写的输出。按照以上思路，进行续写故事数据集的构建。

在六本书一共31683条数据中，划分出30000条作为训练集，其余为验证（测试）集

### filename

validation/test dataset: dev.json

training dataset: train.json

### Implement

通过下面的命令行，运行finetune_hf.py文件，“..THUDM/chatglm3-6b”是需要被微调的模型的路径，输出文件的位置在lora.yaml文件中设置，设置为./output_StoryContinuation_HP

> **lora.yaml settings**
>
> train_batch_size: 1; gradient_accumulation_steps: 16; real_batch_size: 16
>
> max_steps: 5675; epoch: 3

```python
cd finetune_demo
python finetune_hf.py  ../HarryPotterEnglish/datasets_and_processing_code  ../THUDM/chatglm3-6b  configs/lora.yaml
```

使用自己获取并且构建的StoryContinuation_HP数据集进行大模型chatglm3-6b的微调，令其获取哈利波特世界下的故事续写能力。

微调过程中的详细命令行输出过程和GPU情况，进行了截图，放在路径Screenshot/finetuning_2下

### Result



## Merge the model

在微调输出中，得到的只是微调的lora权重部分，这与基础模型部分是分开保存的，inference_hf.py文件进行推理时，也并没有这两部分真正意义上合并成一个模型；通过代码将微调部分与原基础模型合并，使其可以像原模型一样进行部署。

code path: ./finetune_demo/merge_model.py

--model-dir: 微调输出的权重路径

--out-dir: 合并模型输出路径

```
cd finetune_demo
python merge_model.py --model-dir ./output_StoryContinuation_HP/checkpoint-3750 --out-dir ./output_merged
```

