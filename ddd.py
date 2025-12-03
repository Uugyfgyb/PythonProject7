from manim import *
import numpy as np


class IntegralTheoremNoLaTeX(Scene):
    def construct(self):
        # 标题
        title = Text("Integral Theorems", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 问题描述
        problem = Text(
            "Evaluate the line integral:",
            font_size=32
        )
        problem.next_to(title, DOWN, buff=0.5)

        integral_text = Text(
            "∮_C x³ dx - x³ dy + xyz dz",
            font_size=32
        )
        integral_text.next_to(problem, DOWN, buff=0.3)

        self.play(Write(problem))
        self.play(Write(integral_text))
        self.wait(2)

        # 曲线C的描述
        curve_desc = Text(
            "Where C is the intersection curve of:",
            font_size=28
        )
        curve_desc.next_to(integral_text, DOWN, buff=0.5)

        surface1 = Text(
            "x² + y² = z² + 3",
            font_size=28
        )
        surface1.next_to(curve_desc, DOWN, buff=0.3)

        surface2 = Text(
            "z = 3 - √(x² + y²)",
            font_size=28
        )
        surface2.next_to(surface1, DOWN, buff=0.3)

        self.play(Write(curve_desc))
        self.wait(1)
        self.play(Write(surface1))
        self.wait(1)
        self.play(Write(surface2))
        self.wait(2)

        # 交线方程
        intersection = Text(
            "The intersection C is: x² + y² = 4, z = 1",
            font_size=28, color=RED
        )
        intersection.next_to(surface2, DOWN, buff=0.5)

        self.play(Write(intersection))
        self.wait(2)

        # 清除所有，开始讲解斯托克斯定理
        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(integral_text),
            FadeOut(curve_desc),
            FadeOut(surface1),
            FadeOut(surface2),
            FadeOut(intersection)
        )

        # 斯托克斯定理标题
        stokes_title = Text("Stokes' Theorem", font_size=48, color=BLUE)
        stokes_title.to_edge(UP)

        stokes_formula = Text(
            "∮_C F·dr = ∬_S (curl F)·dS",
            font_size=36, color=BLUE
        )
        stokes_formula.next_to(stokes_title, DOWN, buff=0.5)

        self.play(Write(stokes_title))
        self.play(Write(stokes_formula))
        self.wait(2)

        # 定义向量场F
        F_title = Text("Vector field F = ", font_size=32)
        F_components = Text("(x³, -x³, xyz)", font_size=32)
        F_group = VGroup(F_title, F_components).arrange(RIGHT)
        F_group.next_to(stokes_formula, DOWN, buff=0.8)

        self.play(Write(F_title))
        self.play(Write(F_components))
        self.wait(2)

        # 计算旋度
        curl_title = Text("Curl of F:", font_size=32)
        curl_title.next_to(F_group, DOWN, buff=0.8)

        curl_result = Text("curl F = (xz, -yz, -3x²)", font_size=32)
        curl_result.next_to(curl_title, DOWN, buff=0.3)

        self.play(Write(curl_title))
        self.play(Write(curl_result))
        self.wait(2)

        # 选择曲面S
        surface_choice = Text(
            "Choose surface S: disk at z=1 (radius 2)",
            font_size=28, color=GREEN
        )
        surface_choice.next_to(curl_result, DOWN, buff=0.8)

        normal_vector = Text("Normal vector n = (0, 0, 1)", font_size=28, color=ORANGE)
        normal_vector.next_to(surface_choice, DOWN, buff=0.3)

        self.play(Write(surface_choice))
        self.wait(1)
        self.play(Write(normal_vector))
        self.wait(2)

        # 计算点积
        dot_product = Text(
            "(curl F)·n = (xz, -yz, -3x²)·(0,0,1) = -3x²",
            font_size=28
        )
        dot_product.next_to(normal_vector, DOWN, buff=0.5)

        self.play(Write(dot_product))
        self.wait(2)

        # 曲面积分
        surface_integral = Text(
            "∬_S (curl F)·dS = ∬_D -3x² dA",
            font_size=32
        )
        surface_integral.next_to(dot_product, DOWN, buff=0.5)

        self.play(Write(surface_integral))
        self.wait(2)

        # 转换为极坐标
        polar_title = Text("Convert to polar coordinates:", font_size=28)
        polar_title.next_to(surface_integral, DOWN, buff=0.8)

        polar_integral = Text(
            "x = r cosθ, y = r sinθ, dA = r dr dθ",
            font_size=28
        )
        polar_integral.next_to(polar_title, DOWN, buff=0.3)

        polar_result = Text(
            "∬_D -3x² dA = ∫₀²π ∫₀² -3(r cosθ)² · r dr dθ",
            font_size=28
        )
        polar_result.next_to(polar_integral, DOWN, buff=0.3)

        self.play(Write(polar_title))
        self.play(Write(polar_integral))
        self.play(Write(polar_result))
        self.wait(2)

        # 简化积分
        simplified = Text(
            "= -3 ∫₀²π cos²θ dθ · ∫₀² r³ dr",
            font_size=28
        )
        simplified.next_to(polar_result, DOWN, buff=0.5)

        self.play(Write(simplified))
        self.wait(2)

        # 计算积分
        calculation1 = Text("∫₀²π cos²θ dθ = π", font_size=28)
        calculation1.next_to(simplified, DOWN, buff=0.3)

        calculation2 = Text("∫₀² r³ dr = 4", font_size=28)
        calculation2.next_to(calculation1, DOWN, buff=0.3)

        self.play(Write(calculation1))
        self.wait(1)
        self.play(Write(calculation2))
        self.wait(2)

        # 最终结果
        final_result = Text("= -3 × π × 4 = -12π", font_size=36, color=GREEN)
        final_result.next_to(calculation2, DOWN, buff=0.8)

        self.play(Write(final_result))
        self.wait(2)

        # 最终答案框
        answer_box = SurroundingRectangle(final_result, color=GREEN, buff=0.2)
        answer_text = Text("Final Answer", font_size=32, color=GREEN)
        answer_text.next_to(answer_box, UP, buff=0.1)

        self.play(Create(answer_box))
        self.play(Write(answer_text))
        self.wait(3)


class VisualExplanation(Scene):
    """带简单图形的可视化解释"""

    def construct(self):
        # 标题
        title = Text("Visualizing the Problem", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 创建一个圆表示交线C
        circle = Circle(radius=2, color=RED)
        circle_label = Text("C: x² + y² = 4", color=RED, font_size=24)
        circle_label.next_to(circle, DOWN)

        self.play(Create(circle))
        self.play(Write(circle_label))
        self.wait(2)

        # 在圆上添加方向箭头（顺时针）
        arrow1 = Arrow(
            start=[2, 0, 0],
            end=[1, -1, 0],
            color=RED,
            buff=0,
            stroke_width=4
        )

        arrow2 = Arrow(
            start=[1, -1, 0],
            end=[0, -2, 0],
            color=RED,
            buff=0,
            stroke_width=4
        )

        arrow3 = Arrow(
            start=[0, -2, 0],
            end=[-1, -1, 0],
            color=RED,
            buff=0,
            stroke_width=4
        )

        direction_text = Text("Clockwise direction", color=RED, font_size=20)
        direction_text.next_to(circle, RIGHT)

        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.play(GrowArrow(arrow3))
        self.play(Write(direction_text))
        self.wait(2)

        # 显示曲面S（圆盘）
        disk = Circle(radius=2, color=BLUE, fill_opacity=0.3)
        disk.move_to(circle.get_center())

        disk_label = Text("Surface S (disk at z=1)", color=BLUE, font_size=24)
        disk_label.next_to(disk, UP)

        self.play(FadeIn(disk))
        self.play(Write(disk_label))
        self.wait(2)

        # 显示法向量
        normal_arrow = Arrow(
            start=[0, 0, 0],
            end=[0, 1, 0],  # 简化表示，实际是(0,0,1)
            color=GREEN,
            buff=0,
            stroke_width=6
        )

        normal_text = Text("Normal vector n", color=GREEN, font_size=20)
        normal_text.next_to(normal_arrow, RIGHT)

        self.play(GrowArrow(normal_arrow))
        self.play(Write(normal_text))
        self.wait(2)

        # 清除图形，显示计算过程
        self.play(
            FadeOut(title),
            FadeOut(circle),
            FadeOut(circle_label),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(direction_text),
            FadeOut(disk),
            FadeOut(disk_label),
            FadeOut(normal_arrow),
            FadeOut(normal_text)
        )

        # 显示计算步骤
        steps = VGroup(
            Text("Step 1: Apply Stokes' Theorem", font_size=32, color=BLUE),
            Text("∮_C F·dr = ∬_S (curl F)·dS", font_size=28),
            Text("Step 2: Compute curl F", font_size=32, color=BLUE),
            Text("curl F = (xz, -yz, -3x²)", font_size=28),
            Text("Step 3: Choose surface S", font_size=32, color=BLUE),
            Text("S: disk at z=1 with n = (0,0,1)", font_size=28),
            Text("Step 4: Compute dot product", font_size=32, color=BLUE),
            Text("(curl F)·n = -3x²", font_size=28),
            Text("Step 5: Convert to polar coordinates", font_size=32, color=BLUE),
            Text("x = r cosθ, dA = r dr dθ", font_size=28),
            Text("Step 6: Evaluate integrals", font_size=32, color=BLUE),
            Text("∫∫ -3(r cosθ)² r dr dθ = -12π", font_size=28, color=GREEN)
        )

        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.scale(0.8)

        self.play(Write(steps[0]))
        self.play(Write(steps[1]))
        self.wait(1)
        self.play(Write(steps[2]))
        self.play(Write(steps[3]))
        self.wait(1)
        self.play(Write(steps[4]))
        self.play(Write(steps[5]))
        self.wait(1)
        self.play(Write(steps[6]))
        self.play(Write(steps[7]))
        self.wait(1)
        self.play(Write(steps[8]))
        self.play(Write(steps[9]))
        self.wait(1)
        self.play(Write(steps[10]))
        self.play(Write(steps[11]))
        self.wait(3)


class CompleteExplanation(Scene):
    """完整的讲解，结合文本和简单图形"""

    def construct(self):
        # 第一部分：问题陈述
        section1 = Text("Problem Statement", font_size=48, color=BLUE)
        section1.to_edge(UP)

        problem = VGroup(
            Text("Evaluate the line integral:", font_size=32),
            Text("∮_C x³ dx - x³ dy + xyz dz", font_size=36),
            Text("where C is the intersection of:", font_size=28),
            Text("1) x² + y² = z² + 3", font_size=28),
            Text("2) z = 3 - √(x² + y²)", font_size=28)
        )

        problem.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem.next_to(section1, DOWN, buff=0.8)

        self.play(Write(section1))
        self.wait(1)
        for item in problem:
            self.play(Write(item))
            self.wait(0.5)
        self.wait(2)

        # 找到交线
        intersection = Text("Intersection C: x² + y² = 4, z = 1",
                            font_size=32, color=RED)
        intersection.next_to(problem, DOWN, buff=0.8)

        self.play(Write(intersection))
        self.wait(2)

        # 清除第一部分
        self.play(
            FadeOut(section1),
            FadeOut(problem),
            FadeOut(intersection)
        )

        # 第二部分：斯托克斯定理
        section2 = Text("Solution using Stokes' Theorem", font_size=48, color=BLUE)
        section2.to_edge(UP)

        # 创建一个简单的示意图
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )
        axes.next_to(section2, DOWN, buff=0.5)

        circle = Circle(radius=2, color=RED, stroke_width=4)
        circle.move_to(axes.c2p(0, 0))

        self.play(Write(section2))
        self.play(Create(axes))
        self.play(Create(circle))
        self.wait(2)

        # 显示向量场F
        F_text = Text("F = (x³, -x³, xyz)", font_size=32)
        F_text.next_to(axes, DOWN, buff=0.8)

        self.play(Write(F_text))
        self.wait(2)

        # 斯托克斯定理公式
        stokes = Text("Stokes' Theorem:", font_size=32, color=GREEN)
        stokes.next_to(F_text, DOWN, buff=0.5)

        stokes_eq = Text("∮_C F·dr = ∬_S (curl F)·dS", font_size=32)
        stokes_eq.next_to(stokes, DOWN, buff=0.3)

        self.play(Write(stokes))
        self.play(Write(stokes_eq))
        self.wait(2)

        # 计算旋度
        curl_text = Text("curl F = (xz, -yz, -3x²)", font_size=32)
        curl_text.next_to(stokes_eq, DOWN, buff=0.8)

        self.play(Write(curl_text))
        self.wait(2)

        # 选择曲面
        surface_text = Text("Choose S as the disk at z=1", font_size=28, color=YELLOW)
        surface_text.next_to(curl_text, DOWN, buff=0.5)

        normal_text = Text("with normal n = (0, 0, 1)", font_size=28, color=YELLOW)
        normal_text.next_to(surface_text, DOWN, buff=0.3)

        self.play(Write(surface_text))
        self.play(Write(normal_text))
        self.wait(2)

        # 计算点积
        dot_text = Text("(curl F)·n = -3x²", font_size=32)
        dot_text.next_to(normal_text, DOWN, buff=0.8)

        self.play(Write(dot_text))
        self.wait(2)

        # 转换为极坐标
        polar_title = Text("In polar coordinates:", font_size=28)
        polar_title.next_to(dot_text, DOWN, buff=0.8)

        polar_eq = Text("-3x² = -3(r cosθ)²", font_size=32)
        polar_eq.next_to(polar_title, DOWN, buff=0.3)

        self.play(Write(polar_title))
        self.play(Write(polar_eq))
        self.wait(2)

        # 积分计算
        integral_title = Text("Surface integral becomes:", font_size=28)
        integral_title.next_to(polar_eq, DOWN, buff=0.8)

        integral = Text("∬ -3(r cosθ)² r dr dθ", font_size=32)
        integral.next_to(integral_title, DOWN, buff=0.3)

        limits = Text("r: 0 to 2, θ: 0 to 2π", font_size=24)
        limits.next_to(integral, DOWN, buff=0.3)

        self.play(Write(integral_title))
        self.play(Write(integral))
        self.play(Write(limits))
        self.wait(2)

        # 计算结果
        result_text = Text("= -3 × ∫₀²π cos²θ dθ × ∫₀² r³ dr", font_size=32)
        result_text.next_to(limits, DOWN, buff=0.8)

        final_calc = Text("= -3 × π × 4 = -12π", font_size=36, color=GREEN)
        final_calc.next_to(result_text, DOWN, buff=0.5)

        self.play(Write(result_text))
        self.play(Write(final_calc))
        self.wait(2)

        # 最终答案
        answer_box = SurroundingRectangle(final_calc, color=GREEN, buff=0.2)
        answer_label = Text("Final Answer", font_size=32, color=GREEN)
        answer_label.next_to(answer_box, UP, buff=0.1)

        self.play(Create(answer_box))
        self.play(Write(answer_label))
        self.wait(3)

# 运行命令：
# manim -pql integral_theorem.py CompleteExplanation
# manim -pql integral_theorem.py IntegralTheoremNoLaTeX
# manim -pql integral_theorem.py VisualExplanation