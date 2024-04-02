round_robin_rounds = 2
groups = {
    'A':['Argentina', 'Brazil', 'Chile', 'Denmark'],
    'B':['England', 'France','Greece', 'Hungary'],
    'C':['Italy', 'Japan', 'Kuwait', 'Luxembourg']
}
time_field_availability = {
    'day_1_am': ['east',         'north', 'south'],
    'day_1_pm': ['east', 'west', 'north',        ],
    'day_2_am': ['east', 'west', 'north', 'south'],
    'day_2_pm': ['east', 'west', 'north', 'south'],
    'day_3_am': ['east',         'north', 'south'],
    'day_3_pm': ['east', 'west', 'north', 'south'],
    'day_4_am': ['east', 'west', 'north', 'south'],
    'day_4_pm': ['east', 'west',          'south'],
    'day_5_am': ['east', 'west', 'north', 'south'],
    'day_5_pm': ['east', 'west', 'north', 'south'],
}

fields_available = iter(
    [(time, field) for time in time_field_availability
         for field in time_field_availability[time] if field ]
    )

def schedule_matches(groups: dict, fields_available: dict,
                   round_robin_rounds: int = 2) -> dict:
    field = None
    match_schedule = {}
    team_schedule = {team:[] for group in groups.values() for team in group}
    all_teams_by_group = [(team, group_name) for group_name in groups
                            for team in groups[group_name]]
    while any([(len(team_schedule[team]) < (len(group)-1)*round_robin_rounds)
               for group in groups.values() for team in group]):
        teams_sorted_by_round_played = sorted(all_teams_by_group,
                key=lambda x: (len(team_schedule[x[0]]),
                               max(team_schedule[x[0]],['']))
                )
        current_round_paired = []
        for home_team, home_group in teams_sorted_by_round_played:
            if field is None:
                field = next(fields_available)
                
            if home_team in current_round_paired \
               or (field[0] in team_schedule.get(home_team)):
                continue

            sorted_guest_group = sorted(
                filter(lambda x: x!= home_team and x not in current_round_paired,
                       groups[home_group][::-1]),
                key=lambda x: (len(team_schedule[x]), max(team_schedule[x],[''])))
            while sorted_guest_group:
                guest_team = sorted_guest_group.pop(0)
                
                match_= tuple(sorted([guest_team, home_team])) \
                        if round_robin_rounds % 2 \
                            else (guest_team, home_team)
                match_count = [m[0] for m in match_schedule.keys()].count(match_)
                if match_count >= (
                   round_robin_rounds / (2 - round_robin_rounds % 2))
                    # these two teams had already matched.
                   or field[0] in team_schedule.get(guest_team):
                    # there is a conflict of schedule for the guest team
                    continue

                match_schedule[(match_, match_count+1, home_group)] = field
                team_schedule[home_team].append(field[0])
                team_schedule[guest_team].append(field[0])
                current_round_paired.append(home_team)
                current_round_paired.append(guest_team)
                # we had a match, no need to check the rest of the group
                sorted_guest_group = []
                # this field had been used by this match, 
                field = None

        if not current_round_paired:
            # no teams can use this field, skip this field for now...
            field = None
            
    return match_schedule


match_schedule = schedule_matches(groups, fields_available, round_robin_rounds)

fields = sorted({field for fields in time_field_availability.values()
              for field in fields})
group_name_width = max([len(group_name) for group_name in groups])
team_name_width = max([len(t) for group in groups.values() for t in group])
time_width = max([len(time) for time in time_field_availability])
print_column_width = group_name_width + 1 + team_name_width*2 + 1 
print("As time table:")
table_title = ('_'*(time_width+2)+f'{{:_^{print_column_width}}}'*len(fields)
               ).format(*fields)
print(table_title)
for time in time_field_availability:
    print(f"{time:{time_width+2}}", end='')
    for field in fields:
        try:
            pos = list(match_schedule.values()).index((time, field))
            match_ = list(match_schedule.keys())[pos]
            print(f"{match_[2]:>{group_name_width}})"
                  f"{match_[0][0]:>{team_name_width}}"
                  f":{match_[0][1]:<{team_name_width}}", end='')
        except ValueError as e:
            print(f"{'':{print_column_width}}", end='')
    print()

print("\nBy time and field:")
for seq, match_ in enumerate(match_schedule):          
    print(f"{seq:3}, {match_schedule.get(match_)}\t "
          f"{match_[2]:{group_name_width}}"
          f"{match_[0:2]}")
