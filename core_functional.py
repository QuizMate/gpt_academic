# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break


def get_core_functions():
    return {
        "学术润色(英)": {
            # 前言
            "Prefix":   r"Below is a paragraph from an academic paper. Polish the writing to meet the academic style, " +
                        r"improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence. " +
                        r"Furthermore, list all modification and explain the reasons to do so in markdown table." + "\n\n",
            # 后语
            "Suffix":   r"",
            "Color":    r"secondary",    # 按钮颜色
        },
        "学术润色(中)": {
            "Prefix":   r"作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，" +
                        r"同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本" + "\n\n",
            "Suffix":   r"",
        },
        "查找语法错误": {
            "Prefix":   r"Can you help me ensure that the grammar and the spelling is correct? " +
                        r"Do not try to polish the text, if no mistake is found, tell me that this paragraph is good." +
                        r"If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, " +
                        r"put the original text the first column, " +
                        r"put the corrected text in the second column and highlight the key words you fixed.""\n"
                        r"Example:""\n"
                        r"Paragraph: How is you? Do you knows what is it?""\n"
                        r"| Original sentence | Corrected sentence |""\n"
                        r"|--------|--------|""\n"
                        r"| How **is** you? | How **are** you? |""\n"
                        r"| Do you **knows** what **is** **it**? | Do you **know** what **it** **is** ? |""\n"
                        r"Below is a paragraph from an academic paper. "
                        r"You need to report all grammar and spelling mistakes as the example before."
                        + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break,    # 预处理：清除换行符
        },
        # "中译英": {
        #     "Prefix":   r"Please translate following sentence to English:" + "\n\n",
        #     "Suffix":   r"",
        # },
        "中英互译": {
            "Prefix":   r"I want you to act as a scientific English-Chinese translator, " +
                        r"I will provide you with some paragraphs in one language " +
                        r"and your task is to accurately and academically translate the paragraphs only into the other language. " +
                        r"Do not repeat the original provided paragraphs after translation. " +
                        r"You should use artificial intelligence tools, " +
                        r"such as natural language processing, and rhetorical knowledge " +
                        r"and experience about effective writing techniques to reply. " +
                        r"I'll give you my paragraphs as follows, tell me what language it is written in, and then translate:" + "\n\n",
            "Suffix": "",
            "Color": "secondary",
        },
        "引用扩写": {
            "Prefix": r"请根据文章的引用进行扩写:" + "\n\n",
            "Suffix": "",
            "Expand": True,
            "Color": "secondary",
        },
        "摘要扩写": {
            "Prefix":  r"请根据文章的摘要进行扩写:" + "\n\n",
            "Suffix": "",
            "Expand": True,
            "Color": "secondary",
        },
        "内容扩写": {
            "Prefix":   r"请针对文章内容扩写:" + "\n\n",
            "Suffix": "",
            "Expand": True,
            "Color": "secondary",
        },
        "大纲扩写": {
            "Prefix":   r"请针对文章大纲扩写:" + "\n\n",
            "Suffix": "",
            "Expand": True,
            "Color": "secondary",
        },
        "加入案例": {
            "Prefix":   r"请在文章中加入通俗易懂生动的案例:" + "\n\n",
            "Suffix": "",
            "Polishing": True,
            "Color": "secondary",
        },
        "加入文献": {
            "Prefix":   r"请在文章中引入文献，要求在谷歌学术超过一千字的文献:" + "\n\n",
            "Suffix": "",
            "Polishing": True,
            "Color": "secondary",
        },
    }
