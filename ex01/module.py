


def do():
    print("Welcome to ex01")
    teams = _create_team()

    # Print the created teams
    print("Created teams:", teams)

    match_schedule = _schedule(teams)

    # Print the generated schedule
    print("Generated Schedule:")
    i = 0
    for match in match_schedule:
        i = i+1
        print(f"game{i}:{match[0]} vs {match[1]}")

# --------------------------------------------------------------------------------
# internal function 
# --------------------------------------------------------------------------------
    
def _create_team():
    try:
        # Prompt the user to enter the number of teams to create
        num_teams = int(input("Enter the number of teams to create: "))
        
        # Check if the number of teams is a positive integer
        if num_teams <= 0:
            print("Please enter a positive integer for the number of teams.")
            return

        # Create an array of team names with prefixes 'team' + uppercase letters (starting from 'A')
        teams = ['team' + chr(ord('A') + i) for i in range(num_teams)]

        return teams

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

def _schedule(teams):
    try:
        # Check if there are at least two teams to create a schedule
        if len(teams) < 2:
            print("At least two teams are required to create a schedule.")
            return

        # Generate the schedule by pairing each team with every other team
        num_teams = len(teams)
        match_schedule = []

        for i in range(num_teams - 1):
            for j in range(i + 1, num_teams):
                match_schedule.append((teams[i], teams[j]))

        return match_schedule

    except Exception as e:
        print(f"Error occurred: {e}")