import re
import random
import json

def extract_lines_and_word_counts(file_path):
    lines = []  # 存储每一行的字符串
    lines_word_count = []  # 存储每一行的词数

    with open(file_path, 'r') as file:
        for line in file:
            # 去除行尾的换行符和特殊字符
            cleaned_line = line.rstrip().replace('\u3000', '')
            # 只添加非空行
            if cleaned_line:
                lines.append(cleaned_line)
                # 计算并记录每一行的词数
                word_count = len(cleaned_line.split())
                lines_word_count.append(word_count)

    return lines, lines_word_count

path = ["story_datasets\\HarryPotterEnglish\\1.Harry Potter and the Sorcerer's Stone.txt", "story_datasets\\HarryPotterEnglish\\2.Harry Potter and The Chamber Of Secrets.txt","story_datasets\\HarryPotterEnglish\\3.Harry Potter and the Prisoner of Azkaban.txt","story_datasets\\HarryPotterEnglish\\4.Harry Potter and the Goblet of Fire.txt","story_datasets\\HarryPotterEnglish\\5.Harry Potter and the Order of the Phoenix.txt","story_datasets\\HarryPotterEnglish\\6.Harry Potter and The Half-Blood Prince.txt","story_datasets\\HarryPotterEnglish\\7.Harry Potter and the Deathly Hallows.txt"]
# 实际的文件路径
index = 4
file_path = path[index]
# 调用函数并获取结果
lines, lines_word_count = extract_lines_and_word_counts(file_path)

# 提取每一行的第一句话 以及第一句话的词数
first_sentences = []
first_sentences_word_count = []
for line in lines:
    first_sentence = re.split(r'(?<!Mr)(?<!Mrs)\. ', line)[0] + '.'
    first_sentences.append(first_sentence)
    first_sentence_word_count = len(first_sentence.split())
    first_sentences_word_count.append(first_sentence_word_count)

# 删除first_sentences中的前置空格
first_sentences = [sentence.lstrip() for sentence in first_sentences]
# 删除lines中的前置空格
lines = [line.lstrip() for line in lines]

# 制作数据集，json格式的
dataset = []
answer_word_counts = []

#续写的提示语
prompts = ["Please continue writing a coherent and logical story based on the following sentence.",
           "I request that you craft a continuous, logical narrative following this sentence.",
           "Kindly develop a consistent and rational tale from the sentence provided below.",
           "Please proceed to create a story that flows logically from the sentence here.",
           "I invite you to continue the story in a coherent and logical manner from this sentence.",
           "Could you please elaborate on a story that is coherent and logical, starting with the following sentence?",
           "Write a sequel that is coherent and logical, beginning with the sentence below, please.",
           "Continue the narrative in a way that makes sense, starting with the sentence given.",
           "Extend the story logically from the sentence presented here.",
           "Please weave a story that follows logically from the sentence provided."]

for i, first_sentence in enumerate(first_sentences):
    if first_sentence.startswith("CHAPTER") or first_sentence.startswith("Chapter") or first_sentence.isupper() or (i>0 and "CHAPTER" in first_sentences[i-1]) or (i>0 and "Chapter" in first_sentences[i-1]):
        continue
    
    content = first_sentence
    answer = lines[i]
    total_word_count = lines_word_count[i]
    
    j = i + 1
    while total_word_count <= 300 and j < len(lines):
        answer += " " + lines[j]
        total_word_count += lines_word_count[j]
        j += 1
    
    answer_word_count = total_word_count
    answer_word_counts.append(answer_word_count)

    #随便挑一条指令，告诉模型现在是要续写
    prompt = random.choice(prompts)
    dataset.append({"conversations": [{"role":"user", "content": f'{prompt} "{content}"'}, {"role":"assistant", "content": answer}]})

print(f"Dataset size: {len(dataset)}")
i = 0
for data in dataset[:5]:  # Print first 5 entries for verification
    print(data, answer_word_counts[i], '\n')
    i += 1

print(len(lines))

output_file_path = f"dataset_output_{index+1}.json"

with open(output_file_path, 'w') as output_file:
    for entry in dataset:
        json.dump(entry, output_file)
        output_file.write(',\n')

# 随机选择5个索引
random_indices = random.sample(range(len(first_sentences)), 5)

# 打印随机选择的结果
for i in random_indices:
    print(f"First Sentence {i+1}: {first_sentences[i]}  Word Count: {first_sentences_word_count[i]}")
    print(f"Line {i+1}: {lines[i]}  Word Count: {lines_word_count[i]}\n")