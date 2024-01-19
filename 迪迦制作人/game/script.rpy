# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("陈文昊")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    $ relation = 0 #好感度

    scene bg room
    # bg room.jpg
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。
    show eileen happy with dissolve
    show eileen happy 
    # eileen  happy.png
    # show eileen happy

    # 此处显示各行对话。

    e "欢迎来到迪迦的世界"

    e "培养你自己的迪迦奥特曼吧"
    # hide eileen happy
    e "你想怎么培养我呢?"
    e "有以下几个选项"
    # 此处为游戏结尾。
    menu:
        e "选择一个你觉得可以让我变强选项"
        "谈恋爱":
            e "唉嘿嘿，被发现了~"
            $ relation = relation + 1

        "抛弃我":
            $ relation = relation - 1
    
    if relation == 1:
        jump goodend
    elif relation == -1:
        jump badend
    hide eileen happy
    #show niuzi with dissolve
    return
label goodend:
     e "快来和我谈恋爱~"
     e "唉嘿嘿~"
label badend:
     e "真讨厌"
     e "快嗦我牛子" 
     show niuzi with dissolve
     menu:
        e "你嗦不嗦"
        "嗦一口":
            e "爱死你了~"
            $ relation = relation + 1
        "不嗦，滚":
            e "呜呜呜~"
            $ relation = relation - 1