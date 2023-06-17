from llmdemo import model, tokenizer


# 告诉gpt读取哪一部分内容做处理
def prompt1():
    text = """
    在公众场合对他人非隐私部位拍摄或录影，无论被拍摄者是否同意，拍摄者都不违反任何法律，纯拍摄行为也没有侵害肖像权的问题 \
    但若是在公众场合拍摄他人(无论是否为隐私部位)，然后发视频上网说被拍摄的人是色狼或是做出任何有损他社会评价的评论，\
    那么这就是真正侵害了被拍摄者的肖像权的行为 \
    此外，在公众场合拍摄他人并且将视频上网造谣诽谤侮辱被拍摄的人，或是捏造事实诽谤的，轻者行政拘留，罚款，重者则有刑事责任 \
    还有一点，那就是任何路人(非警察)或地铁保安或小区保安，都无权查看你的手机内存 \
    《刑法》第二百四十六条 \
    以暴力或者其他方法公然侮辱他人或者捏造事实诽谤他人，情节严重的，处三年以下有期徒刑 \
    、拘役、管制或者剥夺政治权利。
    """
    prompt = f'帮我把被三个双引号覆盖的句子总结成一句"""{text}"""'
    print(f"Q: {prompt}\n")
    response, history = model.chat(tokenizer, prompt, [])
    print(f"A: {response}\n")


# 告诉gpt生成的数据格式
def prompt2():
    prompt = "生成三本书，要求包含书名、作者姓名、体裁，将结果输出成json格式，要求包含 \
    bookId、title、authorName、genre 字段"
    print(f"Q: {prompt}\n")
    response, history = model.chat(tokenizer, prompt, [])
    print(f"A: {response}\n")


# 告诉gpt输出的内容的样式
def prompt3():
    text = """
    编辑并运行C语言代码有这样几步：\n
    1. 通过包管理器安装 gcc 编译器\n\
    2. 使用 `gcc ${filename}.c -o ${executablename}` 命令来编译代码; \n\
    3. 在终端中输入 `./${executablename}` 来执行代码
    """
    prompt = f"""
    提供给你一段使用```包裹的文段。如果这段话包含了一系列的步骤，请将它重写成如下格式：
    步骤1：……
    步骤2：……
    ……
    步骤N：……
    如果这段话不包含一系列步骤，则回答我：“文段无任何步骤”
    ```{text}```
    """
    print(f"Q: {prompt}\n")
    response, history = model.chat(tokenizer, prompt, [])
    print(f"A: {response}\n")
