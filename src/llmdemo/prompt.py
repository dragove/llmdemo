from llmdemo import model, tokenizer
import time


def chat(prompt):
    return model.chat(tokenizer, prompt)[0]


def promptchat(prompt):
    print(f"Q: {prompt}\n")
    response = chat(prompt)
    print(f"A: {response}\n")


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
    promptchat(f'帮我把被三个双引号覆盖的句子总结成一句"""{text}"""')


# 告诉gpt生成的数据格式
def prompt2():
    promptchat("生成三本书，要求包含书名、作者姓名、体裁，将结果输出成json格式，要求包含 \
    bookId、title、authorName、genre 字段")


# 告诉gpt输出的内容的样式
def prompt3():
    text = """
    编辑并运行C语言代码有这样几步：\n
    1. 通过包管理器安装 gcc 编译器\n\
    2. 使用 `gcc ${filename}.c -o ${executablename}` 命令来编译代码; \n\
    3. 在终端中输入 `./${executablename}` 来执行代码
    """
    promptchat(f"""
    提供给你一段使用```包裹的文段。如果这段话包含了一系列的步骤，请将它重写成如下格式：
    步骤1：……
    步骤2：……
    ……
    步骤N：……
    如果这段话不包含一系列步骤，则回答我：“文段无任何步骤”
    ```{text}```
    """)


# 告诉gpt回复的方式
def prompt4():
    promptchat("""
    你的任务是使用统一的格式回答问题

    学生：教我什么是耐心

    老师：耐心是一种重要的品质，指在面对困难、挑战或不确定性时，保持冷静、坚定和持久的态度。\
耐心意味着愿意承受压力和不确定性，并保持冷静和专注。这意味着可以在面对困难和挑战时，保持耐心和毅力，不轻易放弃或失去信心。\
以下是一些可以培养耐心的方法：\
1. 挑战自己：尝试去接受一些挑战，无论是学习新技能、完成一个任务、解决一个难题，都可以让你更加有耐心。\
2. 坚持锻炼：锻炼可以增强你的耐心和毅力。你可以通过定期锻炼来培养耐心，例如每天进行一定的有氧运动或力量训练。\
3. 培养良好的习惯：良好的习惯可以帮助你培养耐心。例如，坚持规律的作息时间、保持良好的饮食习惯、定期休息等等。\
4. 与他人交流：与他人交流可以帮助你培养耐心。与亲朋好友分享你的困难，寻求他们的建议和支持，可以让你更加有耐心。\
5. 学会放松：放松可以帮助你保持冷静和耐心。你可以通过冥想、瑜伽、听音乐等方式来放松自己，这可以帮助你更好地应对压力和不确定性。\
通过以上方法，你可以培养自己的耐心和毅力，更好地应对生活中的挑战和不确定性。

    学生：教我什么是诚信
    """)


# 告诉gpt有哪些任务
def prompt5():
    promptchat("""
    阅读以下文章并回答问题：

    小石潭记
    从小丘西行百二十步，隔篁竹，闻水声，如鸣珮环，心乐之。伐竹取道，下见小潭，水尤清冽。全石以为底，近岸，卷石底以出，为坻，为屿，为嵁，为岩。青树翠蔓，蒙络摇缀，参差披拂。
潭中鱼可百许头，皆若空游无所依。日光下彻，影布石上，佁然不动；俶尔远逝，往来翕忽。似与游者相乐。
潭西南而望，斗折蛇行，明灭可见。其岸势犬牙差互，不可知其源。
坐潭上，四面竹树环合，寂寥无人，凄神寒骨，悄怆幽邃。以其境过清，不可久居，乃记之而去。
同游者：吴武陵，龚古，余弟宗玄。隶而从者，崔氏二小生：曰恕己，曰奉壹。

    1、用“/”标出如下面句子的朗读节奏。
    一、潭中鱼可百许头 二、其岸势犬牙差互
    2、作者通过写小石潭人迹罕至、凄清幽静的环境，意在表现怎样的思想感情？
    3、请从文中找出你最喜欢的句子，并说明理由。
    """)


def summarize():
    promptchat("""你的任务是从电子商务网站上生成一个产品评论的简短摘要。
请对三个反引号之间的评论文本进行概括，最多30个字。
评论:```这个熊猫公仔是我给女儿的生日礼物，她很喜欢，去哪都带着。
公仔很软，超级可爱，面部表情也很和善。但是相比于价钱来说，
它有点小，我感觉在别的地方用同样的价钱能买到更大的。
快递比预期提前了一天到货，所以在送给女儿之前，我自己玩了会。
```
    """)


lamp_review = """
我需要一盏漂亮的卧室灯，这款灯具有额外的储物功能，价格也不算太高。\
我很快就收到了它。在运输过程中，我们的灯绳断了，但是公司很乐意寄送了一个新的。\
几天后就收到了。这款灯很容易组装。我发现少了一个零件，于是联系了他们的客服，他们很快就给我寄来了缺失的零件！\
在我看来，Lumina 是一家非常关心顾客和产品的优秀公司！
"""


def infer():
    promptchat(f"""
    以下用三个反引号分隔的产品评论的情感是什么？\
评论文本: ```{lamp_review}```
    """)


def infer2():
    promptchat(f"""以下用三个反引号分隔的产品评论的情感是什么？\
用一个单词回答：「正面」或「负面」。\
评论文本: ```{lamp_review}```""")


def infer3():
    promptchat(f"""
使用包含不超过5个词汇识别以下评论的作者表达的情感。将答案格式化为以逗号分隔的单词列表。\
评论文本: ```{lamp_review}```\
""")


def infer4():
    promptchat(f"""
以下评论的作者是否表达了愤怒？评论用三个反引号分隔。给出是或否的答案。\
评论文本: ```{lamp_review}```\
""")


def infer5():
    promptchat(f"""从评论文本中识别以下项目：
- 情绪（正面或负面）
- 审稿人是否表达了愤怒？（是或否）
- 评论者购买的物品
- 制造该物品的公司

评论用三个反引号分隔。将您的响应格式化为 JSON 对象，以 “Sentiment”、“Anger”、“Item” 和 “Brand” 作为键。
如果信息不存在，请使用 “未知” 作为值。
让你的回应尽可能简短。
将 Anger 值格式化为布尔值。

评论文本: ```{lamp_review}```""")


def infer6():
    promptchat("""c++ 中如何分离模板的声明和定义？""")


def trans1():
    prompt = """
将以下中文翻译成英文:
```您好，我想订购一个搅拌机。```
"""
    response = promptchat(prompt)
    print(response)


def trans2():
    prompt = """
请告诉我以下文本是什么语种:
```Combien coûte le lampadaire?```
"""
    response = promptchat(prompt)
    print(response)


def trans3():
    prompt = """
请将以下文本翻译成中文，分别展示成正式与非正式两种语气:
```Would you like to order a pillow?```
"""
    response = promptchat(prompt)
    print(response)


def trans4():
    user_messages = [
        # System performance is slower than normal
        "La performance du système est plus lente que d'habitude.",
        # My monitor has pixels that are not lighting
        "Mi monitor tiene píxeles que no se iluminan.",
        # My mouse is not working
        "Il mio mouse non funziona",
        # My keyboard has a broken control key
        "Mój klawisz Ctrl jest zepsuty",
        # My screen is flashing
        "我的屏幕在闪烁"
    ]
    for issue in user_messages:
        time.sleep(20)
        prompt = f"告诉我以下文本是什么语种，直接输出语种，如法语，无需输出标点符号: ```{issue}```"
        lang = promptchat(prompt)
        print(f"原始消息 ({lang}): {issue}\n")

        prompt = f"""
        将以下消息分别翻译成英文和中文，并写成
        中文翻译：xxx
        英文翻译：yyy
        的格式：
        ```{issue}```
        """
        response = promptchat(prompt)
        print(response, "\n=========================================")


def expand1():
    pass

