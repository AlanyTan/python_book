float_1 = 3.5
fraction_1 = float_1.as_integer_ratio()
match fraction_1:
    case (9|7|5|3|1) as numerator, _ as denominator:
        print(f"# {numerator=} / {denominator=}")
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
# numerator=7 / denominator=2

float_2 = 2.25
match float_2.as_integer_ratio():
    case (9|7|5|3|1) as numerator, denominator:
        print(f"# {numerator=} / {denominator=}")
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
# numerator=9 / denominator=4
        
float_3 = 0.5
match float_3.as_integer_ratio() * 3:
    case (9|7|5|3|1) as numerator, denominator:
        print(f"# {numerator=} / {denominator=}")
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
# no pattern matched (1, 2, 1, 2, 1, 2)
