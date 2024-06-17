#this is histogram grouping based on per hour
from collections import Counter
set_of_duration = input("Pls input the amount of durations to be grouped as follows: 00h00m (Don't need to put extra 0 for hours but needed for minutes) and leave every duration with a space")
listed_sets = set_of_duration.split()
def remove_min_hr():
  global listed_sets
  edited_durations = []
  for duration in range(len(listed_sets)):
    hours = listed_sets[duration][:-4]
    #checks whether the resulting text is only integers for hours
    try:
      edited_durations.append(int(hours))
    except ValueError:
      print(f"A duration you typed has a typo at {listed_sets[duration]} Ending...")
      return
  listed_sets = edited_durations
remove_min_hr()
occurence = Counter(listed_sets)
for hour, count in sorted(occurence.items()):
  hour_word = "hour" if hour in [0,1] else "hours"
  count_word = "time" if count == 1 else "times"
  print(f"{hour} {hour_word} occurs {count} {count_word}")