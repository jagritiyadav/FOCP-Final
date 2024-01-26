# def read_log_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#         return lines
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return []

# def analyze_log(lines):
#     if not lines:
#         print("No data to analyze.")
#         return

#     cat_visits = 0
#     other_cats = 0
#     total_time = 0
#     visit_lengths = []

#     for line in lines:
#         if "Cat Visit" in line:
#             cat_visits += 1
#             visit_time = int(line.split(":")[-1].strip().split()[0])
#             visit_lengths.append(visit_time)
#         elif "Other Cats" in line:
#             other_cats = int(line.split(":")[-1].strip())
#         elif "Total Time in House" in line:
#             time_str = line.split(":")[-1].strip().split(',')
#             hours = int(time_str[0].split()[0])
#             minutes = int(time_str[1].split()[0])
#             total_time = hours * 60 + minutes

#     if cat_visits > 0:
#         average_visit_length = sum(visit_lengths) / len(visit_lengths)
#         longest_visit = max(visit_lengths)
#         shortest_visit = min(visit_lengths)
#     else:
#         average_visit_length = 0
#         longest_visit = 0
#         shortest_visit = 0

#     print("Log File Analysis")
#     print("==================")
#     print(f"Cat Visits: {cat_visits}")
#     print(f"Other Cats: {other_cats}")
#     print(f"Total Time in House: {total_time // 60} Hours, {total_time % 60} Minutes")
#     print(f"Average Visit Length: {average_visit_length:.2f} Minutes")
#     print(f"Longest Visit: {longest_visit} Minutes")
#     print(f"Shortest Visit: {shortest_visit} Minutes")

# # Usage
# filename = 'filename'
# lines = read_log_file(filename)
# analyze_log(lines)

import sys

def read_log_file(file_path):
    """
    Read the log file and return a list of tuples containing cat activities.
    Each tuple is of the form (cat_type, entry_time, exit_time).
    """
    activities = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == 'END':
                    break
                cat_type, entry_time, exit_time = line.strip().split(',')
                activities.append((cat_type, int(entry_time), int(exit_time)))
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

    return activities

def analyze_cat_shelter(activities):
    """
    Analyze the cat shelter activities and print the required output.
    """
    correct_cat_visits = 0
    intruding_cats_doused = 0
    total_time_in_house = 0
    visit_lengths = []

    for cat_type, entry_time, exit_time in activities:
        if cat_type == 'OURS':
            correct_cat_visits += 1
            total_time_in_house += exit_time - entry_time
            visit_lengths.append(exit_time - entry_time)
        elif cat_type == 'THEIRS':
            intruding_cats_doused += 1

    if correct_cat_visits == 0:
        avg_visit_length = longest_visit = shortest_visit = 0
    else:
        avg_visit_length = sum(visit_lengths) // correct_cat_visits
        longest_visit = max(visit_lengths)
        shortest_visit = min(visit_lengths)

    print("\nLog File Analysis\n==================\n")
    print(f'Cat Visits: {correct_cat_visits}')
    print(f'Other Cats: {intruding_cats_doused}\n')
    print(f'Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes\n')
    print(f'Average Visit Length: {avg_visit_length} Minutes')
    print(f'Longest Visit:        {longest_visit} Minutes')
    print(f'Shortest Visit:       {shortest_visit} Minutes')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Missing command line argument!')
        sys.exit(1)

    log_file_path = sys.argv[1]
    cat_activities = read_log_file(log_file_path)
    analyze_cat_shelter(cat_activities)
