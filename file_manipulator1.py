import sys

# ファイル内容を逆にする
def reverse_file(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        contents = f.read()
    
    reverse_contents = contents[::-1]
    with open(outputpath, 'w') as f:
        f.write(reverse_contents + "\n")

# ファイルをコピー
def copy_file(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        contents = f.read()
    
    with open(outputpath, 'w') as f:
        f.write(contents)

# ファイル内容を複製
def replication(inputpath, num_replications):
    with open(inputpath, 'r') as f:
        contents = f.read()
    
    with open(inputpath, 'a') as f:
        for i in range(num_replications):
            f.write(contents)

# ファイル内文字列置換
def replace(inputpath, replace_from, replace_to):
    with open(inputpath, 'r') as f:
        contents = f.read()
    
    replaced_contents = contents.replace(replace_from, replace_to)
    with open(inputpath, 'w') as f:
        f.write(replaced_contents)

if sys.argv[1] == "reverse":
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]
    reverse_file(inputpath, outputpath)
elif sys.argv[1] == "copy":
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]
    copy_file(inputpath, outputpath)
elif sys.argv[1] == "duplicate-contents":
    inputpath = sys.argv[2]
    num_replications = int(sys.argv[3])
    replication(inputpath, num_replications)
elif sys.argv[1] == "replace-string":
    inputpath = sys.argv[2]
    replace_from = sys.argv[3]
    replace_to = sys.argv[4]
    replace(inputpath, replace_from, replace_to)
else:
    print("第一引数は reverse, copy, duplicate-contents, replace-string のいずれかを入力してください")