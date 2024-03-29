ROUND_ROBIN_ROUNDS = 2
groups = [
    ['Argentina', 'Brazil', 'Chile', 'Denmark'],
    ['England', 'France','Greece', 'Hungary'],
    ['Italy', 'Japan', 'Kuwait', 'Luxembourg']
]
fields =        ['east', 'west', 'north', 'south']
time_field_availability = {
    'day_1_am': [True,   False,  True,    True   ],
    'day_1_pm': [True,   True,   True,    False  ],
    'day_2_am': [True,   True,   True,    True   ],
    'day_2_pm': [True,   True,   True,    True   ],
    'day_3_am': [True,   False,  True,    True   ],
    'day_3_pm': [True,   True,   True,    True   ],
    'day_4_am': [True,   True,   True,    True   ],
    'day_4_pm': [True,   True,   False,   True   ],
    'day_5_am': [True,   True,   True,    True   ],
    'day_5_pm': [True,   True,   True,    True   ],
}

fields_available = iter(
    [(time, fields[seq]) for time in time_field_availability
         for seq, field in enumerate(time_field_availability[time]) if field ]
    )

field = None
match_schedule = {}
team_schedule = {team:[] for group in groups for team in group}
while any([(len(team_schedule[team]) < (len(group)-1)*ROUND_ROBIN_ROUNDS) \
           for group in groups for team in group]):
    all_teams_by_group = [(team, gid) for gid in range(len(groups))
                          for team in groups[gid]]
    teams_sorted_by_group_and_round_played = sorted(all_teams_by_group,
            key=lambda x: (x[1], len(team_schedule[x[0]]),
                           max(team_schedule[x[0]],['0'])))
    current_round_paired = []
    for home_team, home_group in teams_sorted_by_group_and_round_played:
        if field is None:
            field = next(fields_available)
            
        if home_team in current_round_paired \
           or (field and field[0] in team_schedule.get(home_team)):
            continue

        sorted_guest_group = sorted(
            filter(lambda x: x!= home_team, groups[home_group][::-1]),
                    key=lambda x: (len(team_schedule[x]),
                                    max(team_schedule[x],['0']) ) )
        while sorted_guest_group:
            guest_team = sorted_guest_group.pop(0)
            
            match_= tuple(sorted([guest_team, home_team])) \
                      if ROUND_ROBIN_ROUNDS % 2 \
                        else (guest_team, home_team)
            match_count = [m[0] for m in match_schedule.keys()].count(match_)
            if match_count >= \
               ROUND_ROBIN_ROUNDS / (2 - ROUND_ROBIN_ROUNDS % 2):
                # these two teams had already matched.
                continue
            
                
            if field[0] in team_schedule.get(guest_team):
                # there is a conflict of schedule for the guest team
                continue
            else:
                match_schedule[(match_, match_count+1)] = field
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
        
print_column_width = max([len(t) for group in groups for t in group])*2 + 1
print("As time table:")
print('_'*12+'{0:_^{4}}{1:_^{4}}{2:_^{4}}{3:_^{4}}'.\
      format(*fields, print_column_width))
for time in time_field_availability:
    print(f"{time:12}", end='')
    for field in fields:
        try:
            pos = list(match_schedule.values()).index((time, field))
            match_ = list(match_schedule.keys())[pos]
            half_width = print_column_width // 2
            print(f"{match_[0][0]:>{half_width}}:{match_[0][1]:<{half_width}}",
                  end='')
        except ValueError as e:
            print(f"{'':{print_column_width}}", end='')
    print()

print("\nBy time and field:")
for seq, match in enumerate(match_schedule):          
    print(f"{seq:3}, {match_schedule.get(match)}\t {match}")
