# Generated by Haxe 3.3.0

import pandas as Pandas


class Script:
    __slots__ = ()

    @staticmethod
    def main():
        food_info = Pandas.read_csv("../food_info.csv")
        print(str(type(food_info)))



Script.main()