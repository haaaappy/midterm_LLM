import re

def remove_asterisk_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # 使用正则表达式删除 *...* 结构
    cleaned_content = re.sub(r'\*.*?\*', '', content)

    with open(file_path, 'w') as file:
        file.write(cleaned_content)

if __name__ == "__main__":
    file_path = 'story_datasets\\HarryPotterEnglish\\2.Harry Potter and The Chamber Of Secrets.txt'
    remove_asterisk_content(file_path)