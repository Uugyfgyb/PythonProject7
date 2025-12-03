from manim import *

class LoveLetterScene(Scene):
    def construct(self):
        # 创建情书文本
        love_letter = Text("""
        我爱你，付骏怡。
        你是我的阳光，  
        我的温暖。  
        每一个思念的瞬间，都想和你一起走过。
        你是我生命中的最美好。
        """, font_size=36)

        # 将情书放置到屏幕中间
        love_letter.to_edge(UP)

        # 创建红色爱心
        heart = SVGMobject("heart.svg")  # 假设你有一个SVG格式的爱心文件
        heart.set_color(RED)
        heart.scale(0.5)  # 缩放爱心大小
        heart.to_edge(DOWN + RIGHT)

        # 添加情书和爱心到场景
        self.play(Write(love_letter))
        self.play(FadeIn(heart))

        # 让情书慢慢消失
        self.wait(2)
        self.play(FadeOut(love_letter))

        # 让爱心持续展示
        self.wait(2)
