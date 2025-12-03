# University of Toronto at Scarborough
# Jiasheng Fu
# Time ( )
from manim import *

class LetterToFuJunyi(Scene):
    def construct(self):
        # 情书内容（每一行一个句子）
        lines = [
            "我爱你。",
            "在这么大的宇宙里，遇见你，像在无穷集合里选中了唯一的特别解。",
            "如果把我对你的喜欢写成函数 f(t)，那它在时间轴上永远单调递增。",
            "你的笑像是我生命里的常数项。",
            "只要想到你，所有噪声都变成了背景。",
            "我想和你一起走很远很远的路，从现在这个初始条件一直积分到未来无穷远。",
            "愿我所有的温柔与努力，都刚好收敛到一句简单的话：",
            "—— 我真的真的，很喜欢你。"
        ]

        # 使用 Paragraph 来排版多行中文
        love_letter = Paragraph(
            *lines,
            line_spacing=1.1,
            font_size=30,
            font="KaiTi",  # 你可以换成本机支持中文的字体
            color="#0000FF"
        )

        # 把情书放在屏幕偏左中间，给右下角留位置放爱心
        love_letter.to_edge(LEFT).shift(UP * 0.5)

        # 右下角的红色爱心（用文字实现）
        heart = Text(
            "❤",
            font_size=88,
            color=RED,
            font="Microsoft YaHei"
        )
        heart.to_corner(DR).shift(UP * 0.3 + LEFT * 0.3)

        # 动画：逐行出现情书
        # 先把每一行取出来（Paragraph 的 submobjects 就是每一行）
        lines_mobs = love_letter.submobjects

        self.play(FadeIn(heart, shift=UP * 0.3), run_time=0.8)  # 先让小爱心出现
        self.play(heart.animate.scale(1.1), run_time=0.4)
        self.play(heart.animate.scale(1 / 1.1), run_time=0.4)

        # 逐行写出情书
        for line in lines_mobs:
            self.play(Write(line), run_time=2.5)
            self.wait(1.0)

        # 最后整体稍微停留一会儿
        self.wait(5)
        self.embed()

