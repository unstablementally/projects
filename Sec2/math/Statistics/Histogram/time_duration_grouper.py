#this is histogram grouping based on per hour
from collections import Counter
set_of_duration = input("Pls input the durations to be grouped, put extra 0 for minutes, and leave every duration with a space")
listed_sets = [duration + 'm' for duration in set_of_duration.split("m") if duration]
#adds back the m after splitting for the func to work
def remove_min_hr():
  global listed_sets
  edited_durations = []
  for duration in listed_sets:
    if duration:
      hours = duration.strip().split('h')[0]
      #splits and take only the hours
    try:
      edited_durations.append(int(hours))
    except ValueError:
      print(f"A duration you typed has a typo at {duration} Ending...")
      return
  listed_sets = edited_durations
remove_min_hr()
occurence = Counter(listed_sets)
for hour, count in sorted(occurence.items()):
  hour_word = "hour" if hour in [1] else "hours"
  count_word = "time" if count == 1 else "times"
  #grammar
  print(f"{hour} {hour_word} occurs {count} {count_word}")