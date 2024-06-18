day_of_week = 6
match day_of_week:
    case 0|6|"Sunday"|"Saturday"|"Weekend":
        print(f"# It's Weekend!")
    case 0:
        print(f"# It's Sunday, The week starts .")
    case 1|"Monday":
        print(f"# I's Monday, 4 more days to weekend.")
    case 2|"Tuesday":
        print(f"# It's Tuesday, 3 more days to weekend.")
    case 3|"Wednesday":
        print(f"# It's Wednesday, 2 more days to weekend.")
    case 4|"Thursday":
        print(f"# It's Thursday, 1 more day to Weekend.")
    case 5|"Friday":
        print(f"# It's Friday, tomorrow is weekend!")
    case 6:
        print(f"# It's Saturday, one more day of weekend.")
    case _:
        print(f"# Error: {day_of_week} cannot be recognized as a day of week.")
# It's Weekend!
