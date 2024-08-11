year = 1900
leap_or_common = 'common' if year % 4 or (not year % 100 and year % 400) \
    else 'leap'
print(f"# {year} is a {leap_or_common} year.")
# 1900 is a common year.
