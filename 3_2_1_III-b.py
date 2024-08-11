year = 1900
if year % 4:
    leap_or_common = "common"
elif year % 100:
    leap_or_common = "leap"
elif year % 400:
    leap_or_common = "common"
else:
    leap_or_common = "leap"

print(f"# {year} is a {leap_or_common} year.")
# 1900 is a common year.
