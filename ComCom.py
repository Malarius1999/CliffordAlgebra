# -*- coding: utf-8 -*-
"""
CompareComplex
"""

from manim import *
import numpy as np
import math


class ComCom(Scene):
    def construct(self):
        eq1 = [
            MathTex(*r"e_1 ( e_1 e_2 )".split()).to_corner(UP + LEFT),
            MathTex(*r"e_2").to_corner(UP + LEFT),
            MathTex(*r"e_1 ( e_1 e_2 ) = e_2".split()).to_corner(UP + LEFT)
            ]
        eq2 = [
            MathTex(*r"( e_1 e_2 )( e_1 e_2 )".split()).to_corner(UP + LEFT).shift(DOWN),
            MathTex(*r"-e_2 e_1 ( e_1 e_2 )".split()).to_corner(UP + LEFT).shift(DOWN),
            MathTex(*r"- e_2 e_2".split()).to_corner(UP + LEFT).shift(DOWN),
            MathTex(*r"-1").to_corner(UP + LEFT).shift(DOWN),
            MathTex(*r"( e_1 e_2 )( e_1 e_2 ) = -1".split()).to_corner(UP + LEFT).shift(DOWN)
            ]
        self.play(Write(eq1[0]), Write(eq2[0]))

        self.play(ReplacementTransform(eq1[0], eq1[1]))
        self.play(ReplacementTransform(eq1[1], eq1[2]))

        self.play(ReplacementTransform(eq2[0], eq2[1]))
        self.play(ReplacementTransform(eq2[1], eq2[2]))
        self.play(ReplacementTransform(eq2[2], eq2[3]))
        self.play(ReplacementTransform(eq2[3], eq2[4]))

        aehnlich = Tex("Ähnlich").shift(3.25 * UP).scale(0.5)
        isEq = MathTex(r"\Leftrightarrow").shift(2.75 * UP).scale(2)
        eq3 = MathTex(*r"1 * ( j ) = j".split()).to_corner(UP + RIGHT)
        eq4 = MathTex(*r"( j ) * ( j ) = -1".split()).to_corner(UP + RIGHT).shift(DOWN)
        self.play(Write(aehnlich), Write(isEq), Write(eq3), Write(eq4))

        teilmenge = MathTex(r"\text{Komplexe Zahlen sind darstellbar durch } G(\mathbb{R}^2): G_2^+ \cong \mathbb{C}").to_corner(UP + LEFT).shift(2*DOWN + 1.5*LEFT).scale(0.75)
        vergleich = MathTex(r"\text{bspw. } c = 2 + 2 e_1 e_2 = 2 + 2 j").to_corner(UP + LEFT).shift(2.75 * DOWN + 0.75 * LEFT).scale(0.75)
        self.play(Write(teilmenge), Write(vergleich))
        reminder = MathTex(r"\text{(Reminder) Komplex -> Polar: } c = |c|*(cos(\alpha)+j*sin(\alpha)) = |c|*e^{j*\alpha}").to_corner(UP + LEFT).shift(3.25 * DOWN + 3.5 * LEFT).scale(0.5)
        reminder2 = MathTex(r"\text{(Reminder 2) Matrizen bspw. } A = e_1e_2 \text{ können mit } e^{Aj} \text{, durch die Reihenentwicklung, verwendet werden").to_corner(UP + LEFT).shift(3.75 * DOWN + 5.25 * LEFT).scale(0.5)
        self.play(Write(reminder))
        eq5 = [
            MathTex(*r"c = 2 + 2 e_1 e_2".split()).to_corner(DOWN + LEFT).shift(1*UP),
            MathTex(*r"c = 4 * (\dfrac{1}{2} + \dfrac{1}{2} e_1 e_2)".split()).to_corner(DOWN + LEFT).shift(1*UP),
            MathTex(*r"c = 4 * (cos(\dfrac{\pi}{4}) + e_1 e_2 sin(\dfrac{\pi}{4})".split()).to_corner(DOWN + LEFT).shift(1*UP),
            MathTex(*r"c = 4 * e^{\pi/4 e_1 e_2}".split()).to_corner(DOWN + LEFT).shift(1*UP)
            ]

        self.play(Write(eq5[0]))
        self.play(ReplacementTransform(eq5[0], eq5[1]))
        self.play(ReplacementTransform(eq5[1], eq5[2]))
        self.play(Write(reminder2))
        self.play(ReplacementTransform(eq5[2], eq5[3]))

        brace = Brace(eq5[3][4])
        brace_text = brace.get_text("Rotor").shift(0.25*UP).scale(0.5)
        self.play(Write(brace), Write(brace_text))

        self.wait(10)
        # title = [
        #     Tex("Reflektion \& Rotation").scale(2),
        #     Tex("Reflektion").to_corner(UP + LEFT),
        #     Tex("Rotation").to_corner(UP + LEFT)
        #     ]
        # self.play(Write(title[0]))
        # self.wait(1)
        # self.play(Transform(title[0], title[1]))
        # self.wait(1)

        # plane = NumberPlane()
        # frame = Rectangle(height = 10.0, width = 7.0, fill_color=BLACK,fill_opacity=1,color=WHITE,buff = .1).to_corner(UP + LEFT).shift(LEFT + UP)

        # self.add_foreground_mobject(title[1])
        # self.play(Write(plane))
        # self.play(Write(frame))
        # vec_v = Arrow(ORIGIN, [3, 1, 0], color = ORANGE, buff = 0)
        # vec_vTex = MathTex(r"v").move_to(vec_v.tip).shift(RIGHT*0.4)
        # vec_u = Arrow(ORIGIN, [4, 3, 0], color = BLUE, buff = 0)
        # vec_uTex = MathTex(r"u").move_to(vec_u.tip).shift(RIGHT*0.4)
        # vec_v2 = Arrow(ORIGIN, [1.8,2.6,0], color = ORANGE, buff = 0)
        # vec_v2Tex = MathTex(r"v'").move_to(vec_v2.tip).shift(UP * 0.3 + RIGHT*0.4)
        # vec_vp1 = Arrow([2.4,1.8,0], [3,1,0], color = ORANGE, buff = 0.1, backgound_stroke_opacity = 0.5)
        # vec_vp2 = Arrow([1.8,2.6,0], [2.4,1.8,0], color = ORANGE, buff = 0.1, backgound_stroke_opacity = 0.5)
        # self.play(Write(vec_v), Write(vec_u), Write(vec_v2), Write(vec_vTex), Write(vec_v2Tex), Write(vec_uTex))
        # self.play(Write(vec_vp1), Write(vec_vp2))

        # linAlg = MathTex(r"\text{In LinAlg: \enspace}", *"v^{'} = v - 2 * v_{\perp}".split()).scale(0.65).to_corner(UP + LEFT).shift(DOWN)
        # self.play(Write(linAlg))

        # GA = [
        #     MathTex(r"\text{In GA: \qquad}", *"v^{'} = u v u^{-1}".split(), "\Leftarrow u^{-1} = \dfrac{u}{||u||^2}").scale(0.65).to_corner(UP + LEFT).shift(2*DOWN),
        #     MathTex("v' =", "\dfrac{( 3e_1 + 4e_2 )( 3e_1 - 1e_2 )( 3e_1 + 4e_2 )}{5^2}").scale(0.65).to_corner(UP + LEFT).shift(3*DOWN),
        #     MathTex("v' =", "\dfrac{27e_1^3 + 36e_2e_1^2 + (-9)e_1e_2e_1 + 36e_1^2e_2 + ... + (-16)e_2^3}{5^2}").scale(0.45).to_corner(UP + LEFT).shift(4*DOWN),
        #     MathTex("v' =", "\dfrac{27e_1 + 36e_2 + (-9)e_2*(-1) + 36e_2 + ... + (-16)e_2}{5^2}").scale(0.45).to_corner(UP + LEFT).shift(5*DOWN),
        #     MathTex("v' =", "1.8e_1 + 2.6e_2").scale(0.65).to_corner(UP + LEFT).shift(6*DOWN)
        #     ]

        # self.play(Write(GA[0][:6]))
        # self.play(Write(GA[0][6]))
        # self.play(Write(GA[1]))
        # self.play(Write(GA[2]))
        # self.play(Write(GA[3]))
        # self.play(Write(GA[4]))

        # self.play(
        #     FadeOut(linAlg), FadeOut(GA[0]), FadeOut(GA[1]), FadeOut(GA[2]), FadeOut(GA[3]),FadeOut(GA[4]),
        #     FadeOut(vec_vp1), FadeOut(vec_vp2), FadeOut(vec_v2Tex),
        #     Transform(title[1], title[2])
        #     )

        # vec_w = Arrow(ORIGIN, [2, 0, 0], color = GREEN, buff = 0)
        # vec_wTex = MathTex(r"w").move_to(vec_w.tip).shift(RIGHT*0.4)
        # vec_v3 = Arrow(ORIGIN, [1.8,-2.6,0], color = ORANGE, buff = 0)
        # vec_v3Tex = MathTex(r"v'").move_to(vec_v3.tip).shift(RIGHT*0.4)
        # alpha = Angle(vec_v, vec_v3, radius = 0.75, other_angle=False)
        # alpha2 = Angle(vec_v, vec_v3, radius = 0.2, other_angle=False)
        # alphaTex = MathTex(r"\alpha").move_to(alpha).shift(0.4 * UP + 0.25 * LEFT)

        # linAlg = MathTex(r"\text{In LinAlg: \enspace}", r"v^{''} = v \begin{pmatrix} cos(\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(\alpha) \end{pmatrix}").scale(0.65).to_corner(UP + LEFT).shift(DOWN)
        # self.play(Write(linAlg), Write(vec_w), Write(vec_wTex), Write(vec_v3), Write(vec_v3Tex), Write(alpha), Write(alphaTex))

        # GA = [
        #     MathTex(r"2 * \text{Reflektion} = \text{Rotation}").scale(0.65).to_corner(UP + LEFT).shift(2*DOWN),
        #     MathTex(r"\phi_1 + \phi_2 = 2*\phi = \alpha").scale(0.65).to_corner(UP + LEFT).shift(2.5*DOWN),
        #     ]
        # self.play(Write(GA[0]), Write(GA[1]))
        # self.play(Transform(alpha, alpha2))

        # self.wait(10)
