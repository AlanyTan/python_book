float_1 = 3.5
fraction_1 = float_1.as_integer_ratio()
match fraction_1:
    case (9|7|5|3|1) as numerator, _ as denominator:
        print(f"# {numerator=} / {denominator=}")
        # numerator=7 / denominator=2
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")

float_2 = 2.25
match float_2.as_integer_ratio():
    case (9|7|5|3|1) as numerator, denominator:
        print(f"# {numerator=} / {denominator=}")
        # numerator=9 / denominator=4
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
        
float_3 = 1
match float_3.as_integer_ratio() * 2:
    case (9|7|5|3|1) as numerator, denominator:
        print(f"# {numerator=} / {denominator=}")
    case nomatch:
        print(f"# no pattern matched {nomatch}")
        # no pattern matched (1, 1, 1, 1)
