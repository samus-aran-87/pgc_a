import re

params = {
    "file_path" : "/Users/alexander/Code/Playground/regex/",
    "file_name" : "dump.txt",
    "file_result" : "result.txt",
}

input_file = open(params['file_name'], mode='r', encoding='utf-8')
output_file = open(params['file_result'], mode='w', encoding='utf-8')
mytext = input_file.read()

regex = r"[\w.-]+@(?!intel.com)[\w.-]+" #[\w.-]+@[\w.-]+ #[\w.-]+@[A-Za-z-]+\.[\w.]+  #[\w.-]+@(?!intel.com)[\w.-]+
results = re.findall(regex, mytext)
# print(len(results)) # 100 - 2 (intel.com)

for n, i in enumerate(results, 1):
    print(n, i)
    output_file.write(i+'\n')
