# -*- coding: utf-8 -*-
"""
Reflektion & Rotation
"""

from manim import *
import numpy as np
import math

class RefRot(Scene):
    def construct(self):
        title = [
            Tex("Reflektion \& Rotation").scale(2),
            Tex("Reflektion").to_corner(UP + LEFT),
            Tex("Rotation").to_corner(UP + LEFT)
            ]
        self.play(Write(title[0]))
        self.wait(1)
        self.play(Transform(title[0], title[1]))
        self.wait(1)

        plane = NumberPlane()
        frame = Rectangle(height = 10.0, width = 7.0, fill_color=BLACK,fill_opacity=1,color=WHITE,buff = .1).to_corner(UP + LEFT).shift(LEFT + UP)

        self.add_foreground_mobject(title[1])
        self.play(Write(plane))
        self.play(Write(frame))
        vec_v = Arrow(ORIGIN, [3, 1, 0], color = ORANGE, buff = 0)
        vec_vTex = MathTex(r"v").move_to(vec_v.tip).shift(RIGHT*0.4)
        vec_u = Arrow(ORIGIN, [4, 3, 0], color = BLUE, buff = 0)
        vec_uTex = MathTex(r"u").move_to(vec_u.tip).shift(RIGHT*0.4)
        vec_v2 = Arrow(ORIGIN, [1.8,2.6,0], color = ORANGE, buff = 0)
        vec_v2Tex = MathTex(r"v'").move_to(vec_v2.tip).shift(UP * 0.3 + RIGHT*0.4)
        vec_vp1 = Arrow([2.4,1.8,0], [3,1,0], color = ORANGE, buff = 0.1, backgound_stroke_opacity = 0.5)
        vec_vp2 = Arrow([1.8,2.6,0], [2.4,1.8,0], color = ORANGE, buff = 0.1, backgound_stroke_opacity = 0.5)
        self.play(Write(vec_v), Write(vec_u), Write(vec_v2), Write(vec_vTex), Write(vec_v2Tex), Write(vec_uTex))
        self.play(Write(vec_vp1), Write(vec_vp2))

        linAlg = MathTex(r"\text{In LinAlg: \enspace}", *"v^{'} = v - 2 * v_{\perp}".split()).scale(0.65).to_corner(UP + LEFT).shift(DOWN)
        self.play(Write(linAlg))

        GA = [
            MathTex(r"\text{In GA: \qquad}", *"v^{'} = u v u^{-1}".split(), "\Leftarrow u^{-1} = \dfrac{u}{||u||^2}").scale(0.65).to_corner(UP + LEFT).shift(2*DOWN),
            MathTex("v' =", "\dfrac{( 3e_1 + 4e_2 )( 3e_1 - 1e_2 )( 3e_1 + 4e_2 )}{5^2}").scale(0.65).to_corner(UP + LEFT).shift(3*DOWN),
            MathTex("v' =", "\dfrac{27e_1^3 + 36e_2e_1^2 + (-9)e_1e_2e_1 + 36e_1^2e_2 + ... + (-16)e_2^3}{5^2}").scale(0.45).to_corner(UP + LEFT).shift(4*DOWN),
            MathTex("v' =", "\dfrac{27e_1 + 36e_2 + (-9)e_2*(-1) + 36e_2 + ... + (-16)e_2}{5^2}").scale(0.45).to_corner(UP + LEFT).shift(5*DOWN),
            MathTex("v' =", "1.8e_1 + 2.6e_2").scale(0.65).to_corner(UP + LEFT).shift(6*DOWN)
            ]

        self.play(Write(GA[0][:6]))
        self.play(Write(GA[0][6]))
        self.play(Write(GA[1]))
        self.play(Write(GA[2]))
        self.play(Write(GA[3]))
        self.play(Write(GA[4]))

        self.play(
            FadeOut(linAlg), FadeOut(GA[0]), FadeOut(GA[1]), FadeOut(GA[2]), FadeOut(GA[3]),FadeOut(GA[4]),
            FadeOut(vec_vp1), FadeOut(vec_vp2),
            Transform(title[1], title[2])
            )

        vec_w = Arrow(ORIGIN, [2, 0, 0], color = GREEN, buff = 0)
        vec_wTex = MathTex(r"w").move_to(vec_w.tip).shift(RIGHT*0.4)
        vec_v3 = Arrow(ORIGIN, [1.8,-2.6,0], color = ORANGE, buff = 0)
        vec_v3Tex = MathTex(r"v''").move_to(vec_v3.tip).shift(RIGHT*0.4)
        alpha = Angle(vec_v, vec_v3, radius = 0.75, other_angle=False, color = RED)
        alphaTex = MathTex(r"\alpha", color = RED).move_to(alpha).shift(0.4 * UP + 0.25 * LEFT)

        linAlg = MathTex(r"\text{In LinAlg: \enspace}", r"v^{''} = v \begin{pmatrix} cos(\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(\alpha) \end{pmatrix}").scale(0.65).to_corner(UP + LEFT).shift(DOWN)
        self.play(Write(linAlg), Write(vec_w), Write(vec_wTex), Write(vec_v3), Write(vec_v3Tex), Write(alpha), Write(alphaTex))

        ges = [
            MathTex(r"\rightarrow 2 * \text{Reflektion} = \text{Rotation}").scale(0.65).to_corner(UP + LEFT).shift(2*DOWN),
            MathTex(r"\rightarrow 2*\phi = \alpha").scale(0.65).to_corner(UP + LEFT).shift(2.5*DOWN),
            ]

        phi = Angle(vec_w, vec_u, radius = 1, other_angle=False, color = YELLOW)
        phiTex = MathTex(r"\phi", color = YELLOW).move_to(phi).shift(0.2 * RIGHT + 0.3*UP)
        alpha2 = Angle(vec_v3, vec_v, radius = 1.25, other_angle=False, color = RED)
        alphaTex2 = MathTex(r"\alpha", color=RED).move_to(alpha2).shift(0.4 * DOWN + 0.4 * RIGHT)

        self.play(Write(ges[0]), Write(ges[1]))
        self.play(Transform(alpha, alpha2), Transform(alphaTex, alphaTex2))
        self.play(Write(phi), Write(phiTex))

        GA = [
            MathTex(r"\text{In GA: \qquad}", *"v^{'} = u v u^{-1}".split()).scale(0.65).to_corner(UP + LEFT).shift(3.5*DOWN),
            MathTex(r"\text{In GA: \qquad}", *"v^{''} = w ( u v u^{-1} ) w^{-1}".split()).scale(0.65).to_corner(UP + LEFT).shift(3.5*DOWN),
            MathTex(r"\text{In GA: \qquad}", *"v^{''} = (wu) v (uw)^{-1}".split()).scale(0.65).to_corner(UP + LEFT).shift(3.5*DOWN),
            MathTex(r"v^{''} = (wu) v (uw)^{-1}").scale(0.65).to_corner(UP + LEFT).shift(6*DOWN),
            MathTex(r"v^{''} = |wu| e^{-\phi e_1e_2} v \dfrac{1}{|uw|} e^{\phi e_1e_2}").scale(0.65).to_corner(UP + LEFT).shift(6*DOWN),
            MathTex(r"v^{''} = v e^{2 \phi e_1e_2} = v e^{\alpha e_1 e_2}").scale(0.65).to_corner(UP + LEFT).shift(6*DOWN)
            ]

        self.play(Write(GA[0]))
        self.play(ReplacementTransform(GA[0][1:], GA[1][1:]))
        self.play(ReplacementTransform(GA[1][3:6], GA[2][3]), ReplacementTransform(GA[1][8:11], GA[2][5]))

        brace = Brace(GA[2][3])
        reminder = [
            MathTex(r"\text{Produkt der Vektoren } wu = \text{Scalar} + \text{Bivektor}").scale(0.5).to_corner(UP + LEFT).shift(4.5*DOWN),
            MathTex(r"\Rightarrow \text{ebenfalls in Exponentialsschreibweise darstellbar:}").scale(0.5).to_corner(UP + LEFT).shift(4.75*DOWN),
            MathTex(r"\Rightarrow uw = |u|e^{\phi_u e_1e_2}|w|e^{\phi_w e_1e_2}").scale(0.5).to_corner(UP + LEFT).shift(5*DOWN),
            MathTex(r"\Rightarrow uw = |uw|e^{\phi e_1e_2}").scale(0.5).to_corner(UP + LEFT).shift(5*DOWN),
            MathTex(r"\Rightarrow \text{Nur } \phi \text{ von Bedeutung. Länge und Position nicht}").scale(0.5).to_corner(UP + LEFT).shift(7*DOWN)
            ]
        self.play(Write(brace), Write(reminder[0]))
        self.play(Write(reminder[1]))
        self.play(Write(reminder[2]))
        self.play(ReplacementTransform(reminder[2], reminder[3]))

        self.play(Write(GA[3]))
        self.play(ReplacementTransform(GA[3], GA[4]))
        self.play(ReplacementTransform(GA[4], GA[5]))
        self.play(Write(reminder[4]))

        self.wait(10)

        # uEq = MathTex(*"u = a e_1 + b e_2".split()).shift(UP).shift(UP)
        # vEq = MathTex(*"v = c e_1 + d e_2".split()).shift(UP)
        # uvEq = [
        #     MathTex(*"u v = ( a e_1 + b e_2 )( c e_1 + d e_2 )".split()),
        #     MathTex(*"u v = a c e_1 e_1 + b d e_2 e_2 + a d e_1 e_2 + b c e_2 e_1".split()).shift(DOWN),
        #     MathTex(*"u v = a c \cdot 1 + b d \cdot 1 + a d e_1 e_2 - b c e_1 e_2".split()).shift(DOWN),
        #     MathTex(*"u v = ( a c + b d ) + ( a d - c d ) e_1 e_2".split()).shift(DOWN),
        #     MathTex(*"u v = ( a c + b d ) + ( a d - c d ) e_1 e_2".split()).to_corner(UP + LEFT).shift(0.5*DOWN + LEFT*0.5).scale(0.75),
        #     MathTex(*r"u v = ( |u| |v| cos( \varphi )) + ( |u| |v| sin( \varphi ) ) e_1 e_2".split()).to_corner(UP + LEFT).shift(2*DOWN + LEFT).scale(0.75)
        #     ]

        # self.play(Write(uEq), Write(vEq))
        # self.wait(1)
        # self.play(ReplacementTransform(uEq[0].copy(), uvEq[0][0]), ReplacementTransform(vEq[0].copy(), uvEq[0][1]))
        # self.play(
        #     Write(uvEq[0][2:4]),
        #     ReplacementTransform(uEq[2:].copy(), uvEq[0][4:9]),
        #     Write(uvEq[0][9]),
        #     ReplacementTransform(vEq[2:].copy(), uvEq[0][10:15]),
        #     Write(uvEq[0][15])
        #     )
        # self.wait(2)
        # self.play(Write(uvEq[1][:3]), Write(uvEq[1][7::5]))


        # self.remove(uvEq[1])
        # self.play(
        #     ReplacementTransform(uvEq[0][4:6].copy(), uvEq[1][3:7]),
        #     ReplacementTransform(uvEq[0][10:12].copy(), uvEq[1][3:7])
        #     )
        # self.play(
        #     ReplacementTransform(uvEq[0][7:9].copy(), uvEq[1][8:12]),
        #     ReplacementTransform(uvEq[0][13:15].copy(), uvEq[1][8:12])
        #     )
        # self.play(
        #     ReplacementTransform(uvEq[0][4:6].copy(), uvEq[1][13:17]),
        #     ReplacementTransform(uvEq[0][13:15].copy(), uvEq[1][13:17])
        #     )
        # self.play(
        #     ReplacementTransform(uvEq[0][7:9].copy(), uvEq[1][18:]),
        #     ReplacementTransform(uvEq[0][10:12].copy(), uvEq[1][18:])
        #     )
        # self.wait(2)
        # self.play(
        #     TransformMatchingTex(uvEq[1], uvEq[2])
        #     )
        # self.wait(2)
        # self.play(
        #     TransformMatchingTex(uvEq[2], uvEq[3])
        #     )
        # self.wait(2)
        # brace1 = Brace(uvEq[3][3:10])
        # brace2 = Brace(uvEq[3][11:18])
        # brace1_text = brace1.get_text("Dot-Product").shift(LEFT*0.5)
        # brace2_text = brace2.get_text("Parallelogramm").shift(RIGHT*0.5)
        # braces = VGroup(brace1,brace2,brace1_text,brace2_text)
        # self.play(Write(braces))

        # #Transfer to numberplane
        # self.play(
        #     FadeOut(braces),
        #     FadeOut(uEq),
        #     FadeOut(vEq),
        #     FadeOut(uvEq[0])
        #     )
        # self.play(
        #     Transform(uvEq[3], uvEq[4])
        #     )

        # vGroup = VGroup(uvEq[4],title[1])
        # self.add_foreground_mobjects(vGroup)
        # frame = SurroundingRectangle(vGroup,fill_color=BLACK,fill_opacity=1,color=WHITE,buff = .1)
        # numberplane = NumberPlane()
        # self.play(Write(frame))
        # self.add_foreground_mobjects(frame)
        # self.add_foreground_mobjects(vGroup)
        # self.play(Write(numberplane))

        # u_vec_val = np.array([4/3,2,0])
        # v_vec_val = np.array([2.25,0.75,0])
        # u_vec = Arrow(ORIGIN,u_vec_val,buff=0)
        # u_vec_text = Tex('({{a}}, {{b}})').next_to(u_vec.get_end(), LEFT*0.9).scale(0.75)
        # v_vec = Arrow(ORIGIN,v_vec_val,buff=0)
        # v_vec_text = Tex('({{c}}, {{d}})').next_to(v_vec.get_end(), DOWN).scale(0.75)
        # self.play(Create(v_vec),Create(u_vec_text),Create(u_vec),Create(v_vec_text))
        # self.wait(1)
        # #DOTPRODUCT

        # ortho = np.dot(u_vec_val,v_vec_val)/np.dot(v_vec_val,v_vec_val)

        # line = DashedLine(v_vec_val * ortho
        #                   ,u_vec_val)
        # orto_vec = Arrow(ORIGIN,
        #                  v_vec_val* ortho,buff=0)
        # dotProd =  Arrow(ORIGIN,
        #                  v_vec_val*math.sqrt(np.dot(u_vec_val,v_vec_val)),
        #                  buff=0)
        # b1 = Brace(dotProd,direction=(dotProd.copy().rotate(-math.pi/2).get_unit_vector()),buff=0)
        # b1_text = b1.get_tex("|...| = ac + bd").shift(0.5*DOWN)
        # b2_text = b1.get_tex(r"ac + bd = |u||v|cos( \varphi )").shift(0.5*DOWN)
        # angleBetween = Angle(v_vec, u_vec, radius=0.8, other_angle=False)
        # angleTex = MathTex(r"\varphi").move_to(angleBetween).shift(0.2*UP+0.2*RIGHT)
        # dotProd_G = VGroup(line,dotProd,b1,b1_text,angleBetween,angleTex,b2_text)
        # frame2 = SurroundingRectangle(uvEq[5],fill_color=BLACK,fill_opacity=1,color=WHITE,buff = .1)
        # self.play(Create(line))
        # self.play(Create(orto_vec))
        # self.play(ReplacementTransform(orto_vec,dotProd))
        # self.play(Create(b1),
        #           Create(b1_text))
        # self.play(Create(angleBetween),
        #           Create(angleTex))
        # self.play(Unwrite(b1_text))
        # self.play(Write(b2_text))
        # self.play(Write(frame2),
        #           Write(uvEq[5][0:3]))
        # self.play(ReplacementTransform(b2_text.copy(),uvEq[5][3:9]))
        # self.play(Unwrite(dotProd_G))

        # #PARALLELOGRAM
        # parallel = Polygon(ORIGIN,u_vec_val,u_vec_val + v_vec_val,v_vec_val,color=WHITE,fill_color=WHITE,fill_opacity=0.5)
        # flaecheText = Tex(r" Fläche = ad-cb").next_to(v_vec).shift(DOWN+4*LEFT)
        # flaecheText2 = Tex(r" {{Fläche}} = |u||v| sin($\varphi$)").next_to(v_vec).shift(DOWN+4*LEFT)
        # self.play(Write(parallel))
        # self.play(Write(flaecheText))
        # self.play(TransformMatchingTex(flaecheText,flaecheText2))
        # self.play(ReplacementTransform(flaecheText2.copy(),uvEq[5][9:17]))
        # self.play(ReplacementTransform(uvEq[4][19:].copy(),uvEq[5][17:]))
        # self.wait(2)

