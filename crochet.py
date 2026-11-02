# crochet.py —— 钩织小管家 V0.1
from pathlib import Path
import json

class Yarn:
    """一卷毛线"""
    def __init__(self, brand, series, material, weight_g, length_m, price,
                 color="", color_code=""):
        self.brand = brand          # 品牌
        self.series = series        # 系列
        self.material = material    # 材质
        self.weight_g = weight_g    # 克重
        self.length_m = length_m    # 长度
        self.price = price          # 价格
        self.color = color          # 颜色
        self.color_code = color_code  # 色号

    def show(self):
        return (f"{self.brand}·{self.series} | {self.material} | "
                f"{self.color} | {self.weight_g}g/{self.length_m}m | ¥{self.price}")

class Project:
    """一个钩织项目"""
    def __init__(self, name, needle, yarns=None, link="",
                 current=0, total=0, unit="圈"):
        self.name = name
        self.needle = needle        # 针号
        self.yarns = yarns or []    # 用到的线（先放 Yarn 对象）
        self.link = link            # 教程/图解
        self.current = current      # 当前进度
        self.total = total          # 总进度
        self.unit = unit            # 圈 / 行

    def show(self):
        yarn_txt = "、".join(y.show() for y in self.yarns) if self.yarns else "（未登记）"
        return (f"🧶 {self.name}｜针 {self.needle}｜进度 {self.current}/{self.total}{self.unit}\n"
                f"   用料：{yarn_txt}\n"
                f"   图解：{self.link}")