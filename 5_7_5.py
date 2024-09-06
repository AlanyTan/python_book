##### Start condition #####
round_robin_rounds = 2
groups = {
    'A': ['Argentina', 'Brazil', 'Chile', 'Denmark'],
    'B': ['England', 'France', 'Greece', 'Hungary'],
    'C': ['Italy', 'Japan', 'Kuwait', 'Luxembourg'],
    'D': ['Mongolia', 'Nigeria', 'Oman', 'Poland']
}
time_field_availability = {
    'day_1_am': ['east', 'north', 'south'],
    'day_1_pm': ['east', 'west', 'north',],
    'day_2_am': ['east', 'west', 'south'],
    'day_2_pm': ['west', 'north', 'south'],
    'day_3_am': ['east', 'west', 'north', 'south'],
    'day_3_pm': ['east', 'west', 'north', 'south'],
    'day_4_am': ['east', 'west', 'north', 'south'],
    'day_4_pm': ['east', 'north', 'south'],
    'day_5_am': ['east', 'west', 'north',],
    'day_5_pm': ['east', 'west', 'south'],
    'day_6_am': ['west', 'north', 'south'],
    'day_6_pm': ['east', 'west', 'north', 'south'],
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
        a dict, keys are tuples of (tuple(guest_team,host_team), # of times 
        these two teams played each other, the group_name); the value is the
        field these two teams will be playing
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
        for home_team, home_group in teams_sorted_by_round_played:
            if field is None:
                field = next(fields_available)

            if home_team in current_round_paired \
               or (field[0] in team_schedule.get(home_team)):
                continue

            sorted_guest_group = sorted(
                filter(lambda x: x != home_team and x not in
                       current_round_paired, groups[home_group][::-1]),
                key=lambda x: (len(team_schedule[x]),
                               max(team_schedule[x], [''])))
            while sorted_guest_group:
                guest_team = sorted_guest_group.pop(0)

                match_ = tuple(sorted([guest_team, home_team])
                               ) if round_robin_rounds % 2 else (
                                   guest_team, home_team)
                match_count = [m[0] for m in match_schedule.keys()
                               ].count(match_)
                if (match_count >= (round_robin_rounds /
                                    (2 - round_robin_rounds % 2))
                    ) or field[0] in team_schedule.get(guest_team):
                    continue

                match_schedule[(match_, match_count + 1, home_group)] = field
                team_schedule[home_team].append(field[0])
                team_schedule[guest_team].append(field[0])
                current_round_paired.extend(match_)
                # we had a match, no need to check the rest of the group
                sorted_guest_group = []
                # this field had been used by this match,
                field = None

        if not current_round_paired:
            # no teams can use this field, skip this field for now...
            field = None

    return match_schedule


# call the schedule_matches function
match_schedule = schedule_matches(groups, fields_available, round_robin_rounds)

# output schedule with table format
scheduled_match = {match_schedule[k]: k for k in match_schedule}
fields = sorted({field for fields in time_field_availability.values()
                 for field in fields})
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
        match_ = scheduled_match.get((time, field), None)
        print(f"{match_[2]:>{group_name_width}})"
              f"{match_[0][0]:>{team_name_width}}"
              f":{match_[0][1]:<{team_name_width}}" if match_
              else f"{'':{print_column_width}}", end='')

    print()

# output schedule with list formst
print("\nBy time and field:")
for seq, match_ in enumerate(match_schedule):
    print(f"{seq:3}, {match_schedule.get(match_)}\t "
          f"{match_[2]:{group_name_width}}"
          f"{match_[0:2]}")
