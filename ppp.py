from manim import *
import numpy as np


class TorontoUniversityComplete(Scene):
    def construct(self):
        # 添加背景音乐
        try:
            self.add_sound("C:/Users/fujia/Desktop/Zeta.mp3")
        except:
            print("注意：背景音乐文件未找到，请检查路径")

        # ========== 第一部分：标题介绍 ==========
        self.section1_title_intro()

        # ========== 第二部分：数据网格 ==========
        self.section2_data_grid()

        # ========== 第三部分：学生构成饼图 ==========
        self.section3_pie_chart()

        # ========== 第四部分：热门专业条形图 ==========
        self.section4_bar_chart()

        # ========== 第五部分：校园设施 ==========
        self.section5_campus_facilities()

        # ========== 第六部分：最终总结 ==========
        self.section6_conclusion()

    def section1_title_intro(self):
        """第一部分：标题介绍"""
        # 创建背景
        bg = Rectangle(
            width=config.frame_width * 1.5,
            height=config.frame_height * 1.5,
            fill_color=[DARK_BLUE, BLUE_E],
            fill_opacity=1,
            stroke_width=0
        )
        self.play(FadeIn(bg))

        # 主标题
        title = Text("多伦多大学生活数据", font_size=72, color=WHITE, weight=BOLD)
        title.shift(UP * 1)

        # 副标题
        subtitle = Text("University of Toronto - Campus Life Statistics",
                        font_size=36, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.5)

        # 动画
        self.play(Write(title, run_time=2))
        self.play(Write(subtitle, run_time=1.5))
        self.wait(1)

        # 转场效果
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(bg)
        )

    def section2_data_grid(self):
        """第二部分：数据网格"""
        # 标题
        section_title = Text("关键数据概览", font_size=60, color=BLUE_C)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # 数据卡片
        data_items = [
            {"label": "学生总数", "value": "90,000+", "icon": "👨‍🎓", "color": BLUE},
            {"label": "国际生比例", "value": "25%", "icon": "🌍", "color": GREEN},
            {"label": "本科专业", "value": "700+", "icon": "📚", "color": PURPLE},
            {"label": "图书馆数量", "value": "44个", "icon": "📖", "color": ORANGE},
            {"label": "校园面积", "value": "180英亩", "icon": "🏛️", "color": TEAL},
            {"label": "研究经费", "value": "$1.4B+", "icon": "💰", "color": GOLD},
        ]

        # 创建网格
        grid = VGroup()
        for i, item in enumerate(data_items):
            card = self.create_data_card(item)
            row = i // 3
            col = i % 3
            card.shift(RIGHT * (col - 1) * 4.5 + DOWN * (row - 0.5) * 2.5)
            grid.add(card)

        # 动画：卡片逐个出现
        for card in grid:
            self.play(
                card.animate.scale(1.2).set_opacity(1),
                run_time=0.5
            )
            self.play(
                card.animate.scale(1 / 1.2),
                run_time=0.3
            )

        self.wait(2)

        # 转场
        self.play(
            FadeOut(section_title),
            FadeOut(grid)
        )

    def create_data_card(self, item):
        """创建数据卡片"""
        card = VGroup()

        # 背景
        bg = RoundedRectangle(
            width=4, height=2.5,
            corner_radius=0.3,
            fill_color=item["color"],
            fill_opacity=0.2,
            stroke_color=item["color"],
            stroke_width=3
        )

        # 图标
        icon = Text(item["icon"], font_size=48)
        icon.move_to(bg.get_center() + UP * 0.5)

        # 数值
        value = Text(item["value"], font_size=42, color=YELLOW, weight=BOLD)
        value.move_to(bg.get_center() + DOWN * 0.2)

        # 标签
        label = Text(item["label"], font_size=24, color=WHITE)
        label.move_to(bg.get_bottom() + UP * 0.4)

        card.add(bg, icon, value, label)
        return card

    def section3_pie_chart(self):
        """第三部分：学生构成饼图"""
        # 标题
        title = Text("学生构成分析", font_size=60, color=BLUE_C)
        title.to_edge(UP)
        self.play(Write(title))

        # 饼图数据
        data = [
            {"label": "本科生", "value": 65, "color": BLUE},
            {"label": "研究生", "value": 25, "color": GREEN},
            {"label": "国际生", "value": 25, "color": GOLD},
            {"label": "height(0)

            # 标签
            label = Text(major["name"], font_size=20, color=WHITE)
            label.next_to(bar, DOWN, buff=0.2)

            # 数值
            value = Text(f"{major['value'] * 100:.0f}%",
                         font_size=24, color=YELLOW)
            value.next_to(bar, UP, buff=0.1)

            bars.add(bar)
            labels.add(label)
            values.add(value)

        # 创建坐标轴
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 100, 20],
            x_length=8,
            y_length=5,
            axis_config={"color": GRAY}
        )
        axes.shift(DOWN * 1)

        self.play(Create(axes))

        # 条形生长动画
        for bar, label, value in zip(bars, labels, values):
            target_height = bar.height  # 保存目标高度
            bar.stretch_to_fit_height(0)  # 重置为0

            self.play(
                bar.animate.stretch_to_fit_height(target_height),
                run_time=1.5
            )
            self.play(
                FadeIn(label),
                FadeIn(value),
                run_time=0.5
            )

        self.wait(2)

        # 转场
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(bars),
            FadeOut(labels),
            FadeOut(values)
        )

    def section5_campus_facilities(self):
        """第五部分：校园设施"""
        # 标题
        title = Text("校园设施概览", font_size=60, color=BLUE_C)
        title.to_edge(UP)
        self.play(Write(title))

        # 设施数据
        facilities = [
            {"icon": "🏛️", "name": "历史建筑", "desc": "百年历史的哥特式建筑"},
            {"icon": "📚", "name": "图书馆", "desc": "44个图书馆，千万藏书"},
            {"icon": "🔬", "name": "实验室", "desc": "世界级研究设施"},
            {"icon": "🏟️", "name": "体育中心", "desc": "奥运标准设施"},
            {"icon": "🎭", "name": "艺术中心", "desc": "剧院与画廊"},
            {"icon": "🌳", "name": "校园绿地", "desc": "180英亩绿色空间"},
        ]

        # 创建设施图标
        icons = VGroup()
        for i, facility in enumerate(facilities):
            # 创建图标组
            icon_group = VGroup()

            # 背景圆
            circle = Circle(
                radius=0.8,
                fill_color=BLUE_E,
                fill_opacity=0.2,
                stroke_color=WHITE,
                stroke_width=2
            )

            # 图标
            icon = Text(facility["icon"], font_size=48)

            # 名称
            name = Text(facility["name"], font_size=20, color=YELLOW)
            name.next_to(icon, DOWN, buff=0.1)

            icon_group.add(circle, icon, name)

            # 排列成网格
            row = i // 3
            col = i % 3
            icon_group.shift(
                RIGHT * (col - 1) * 2.5 +
                DOWN * (row - 0.5) * 2
            )

            icons.add(icon_group)

        # 动画：图标逐个出现
        for icon in icons:
            self.play(FadeIn(icon, scale=0.5, run_time=0.5))

        # 旋转效果
        self.play(
            icons.animate.rotate(PI / 6),
            run_time=2,
            rate_func=smooth
        )
        self.play(
            icons.animate.rotate(-PI / 6),
            run_time=2,
            rate_func=smooth
        )

        self.wait(2)

        # 转场
        self.play(
            FadeOut(title),
            FadeOut(icons)
        )

    def section6_conclusion(self):
        """第六部分：最终总结"""
        # 创建渐变背景
        bg_gradient = Rectangle(
            width=config.frame_width * 1.5,
            height=config.frame_height * 1.5,
            fill_color=[DARK_BLUE, "#000033", BLACK],
            fill_opacity=1,
            stroke_width=0
        )
        self.play(FadeIn(bg_gradient))

        # 主标题
        main_title = Text("多伦多大学",
                          font_size=80,
                          color=GOLD,
                          weight=BOLD)

        # 英文标题
        eng_title = Text("University of Toronto",
                         font_size=48,
                         color=WHITE)
        eng_title.next_to(main_title, DOWN, buff=0.5)

        # 动画
        self.play(
            Write(main_title, run_time=2),
            Write(eng_title, run_time=1.5)
        )
        self.wait(1)

        # 成就列表
        achievements = [
            "• 加拿大顶尖研究型大学",
            "• 全球排名前20",
            "• 多元文化校园",
            "• 诺贝尔奖得主母校",
            "• 创新与领导力的摇篮"
        ]

        achievements_group = VGroup()
        for i, text in enumerate(achievements):
            line = Text(text, font_size=32, color=WHITE)
            line.shift(DOWN * i * 0.8)
            achievements_group.add(line)

        achievements_group.next_to(eng_title, DOWN, buff=1)

        # 逐条显示成就
        for line in achievements_group:
            line.set_opacity(0)
            self.add(line)
            self.play(
                line.animate.set_opacity(1).set_color(YELLOW),
                run_time=0.5
            )
            self.play(
                line.animate.set_color(WHITE),
                run_time=0.3
            )

        self.wait(1)

        # 最终口号
        slogan = Text("欢迎来到多伦多大学！",
                      font_size=54,
                      color=GOLD,
                      weight=BOLD)
        slogan.to_edge(DOWN).shift(UP * 1)

        self.play(Write(slogan, run_time=2))

        # 闪烁效果
        for _ in range(3):
            self.play(
                slogan.animate.scale(1.1).set_color(YELLOW),
                rate_func=there_and_back,
                run_time=0.5
            )

        # 淡出结束
        self.wait(3)
        self.play(
            FadeOut(main_title),
            FadeOut(eng_title),
            FadeOut(achievements_group),
            FadeOut(slogan),
            FadeOut(bg_gradient)
        )

# ========== 渲染配置 ==========
# 如果你想要更高的质量，可以在命令行中指定参数
# 或者创建一个配置文件