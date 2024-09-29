##### Start condition #####
round_robin_rounds = 2
groups = {
    'A': ['Argentina', 'Brazil', 'Chile', 'Denmark'],
    'B': ['England', 'France', 'Greece', 'Hungary'],
    'C': ['Italy', 'Japan', 'Kuwait', 'Luxembourg'],
    'D': ['Mongolia', 'Nigeria', 'Oman', 'Poland']
}
time_field_availability = {
    'day_1_am': ['west', 'north', 'south'],
    'day_1_pm': ['east', 'north', 'south'],
    'day_2_am': ['east', 'west', 'south'],
    'day_2_pm': ['east', 'west', 'north'],
    'day_3_am': ['east', 'west', 'north', 'south'],
    'day_3_pm': ['east', 'west', 'north', 'south'],
    'day_4_am': ['east', 'west', 'north', 'south'],
    'day_4_pm': ['east', 'west', 'north', 'south'],
    'day_5_am': ['west', 'north', 'south'],
    'day_5_pm': ['east', 'north', 'south'],
    'day_6_am': ['east', 'west', 'south'],
    'day_6_pm': ['east', 'west', 'north'],
    'day_7_am': ['east', 'west', 'north', 'south'],
    'day_7_pm': ['east', 'west', 'north', 'south'], }
##### End of Start conditions #####

# Convert time_field_availability dict to list[(time,field)] sequence
fields_available = ((time, field) for time in time_field_availability
                    for field in time_field_availability[time] if field)


def schedule_matches(groups: dict, fields_available: list[dict],
                     round_robin_rounds: int = 2) -> dict:
    """The core scheduling functionality for group matches

    Args: 
        groups: dict of groud_name:list[teams]
        fields_available: a list of tuples of (time, field)
        round_robin_rounds: int of number of intra-group games to play each
                            opponent, default is 2.

    Returns:
        a dict, keys are tuples of (time, field), values are tuples of 
        (tuple(guest_team,home_team), # of times these two teams played each 
        other, the group_name)
    """
    field = None
    match_schedule = {}
    team_schedule = {team: [] for group in groups.values() for team in group}
    all_teams_by_group = [(team, group_name) for group_name in groups
                          for team in groups[group_name]]
    while any(((len(team_schedule[team])
                < (len(group) - 1) * round_robin_rounds)
               for group in groups.values() for team in group)):
        teams_sorted_by_round_played = sorted(all_teams_by_group, key=lambda x:
                                              (len(team_schedule[x[0]]), max(
                                                  team_schedule[x[0]], [''])))
        current_round_paired = []
        for home_team, group_name in teams_sorted_by_round_played:
            if field is None:
                field = next(fields_available)

            if home_team in current_round_paired \
               or (field[0] in team_schedule.get(home_team)):
                continue

            sorted_guest_queue = sorted(
                filter(lambda x: x != home_team and x not in
                       current_round_paired, groups[group_name][::-1]),
                key=lambda x: (len(team_schedule[x]),
                               max(team_schedule[x], [''])))
            while sorted_guest_queue:
                guest_team = sorted_guest_queue.pop(0)
                if field[0] in team_schedule.get(guest_team):
                    continue

                match_ = (guest_team, home_team)
                match_count = [m[0] for m in match_schedule.values()
                               ].count(match_)
                meet_count = [set(m[0]) for m in match_schedule.values()
                              ].count(set(match_))
                if meet_count >= round_robin_rounds:
                    continue
                if match_count >= round_robin_rounds / (
                        2 - round_robin_rounds % 2):
                    continue

                match_schedule[field] = (match_, meet_count + 1, group_name)
                team_schedule[home_team].append(field[0])
                team_schedule[guest_team].append(field[0])
                current_round_paired.extend(match_)
                sorted_guest_queue = []
                field = None

        if not current_round_paired:
            field = None

    return match_schedule


# output schedule with table format
scheduled_matches = schedule_matches(
    groups, fields_available, round_robin_rounds)
fields = sorted({field for fields in time_field_availability.values()
                 for field in fields}, key=lambda x: (len(x), x))
group_name_width = max([len(group_name) for group_name in groups])
team_name_width = max([len(t) for group in groups.values() for t in group])
time_width = max([len(time) for time in time_field_availability])
print_column_width = group_name_width + 1 + team_name_width * 2 + 1
print("As time table:")
table_title = ('_' * (time_width + 2)
               + f'{{:_^{print_column_width}}}' * len(fields)).format(*fields)
print(table_title)
for time in time_field_availability:
    print(f"{time:{time_width + 2}}", end='')
    for field in fields:
        match_ = scheduled_matches.get((time, field), None)
        print(f"{match_[2]:>{group_name_width}})"
              f"{match_[0][0]:>{team_name_width}}"
              f":{match_[0][1]:<{team_name_width}}" if match_
              else f"{'':{print_column_width}}", end='')

    print()

# output schedule with list formst
print("\nBy time and field:")
for seq, (time_field, match_) in enumerate(scheduled_matches.items()):
    print(f"{seq + 1:3},",
          "{:{time_width}}  {:8}".format(*time_field, time_width=time_width),
          f"{match_[2]:{group_name_width}}",
          "{:>{team_name_width}}:{:{team_name_width}}".format(
              *match_[0], team_name_width=team_name_width),
          f" match-up {match_[1]}")
