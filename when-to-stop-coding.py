from datetime import timedelta
import sys
from typing import List, Iterator

WORKING_DAY_HOURS = 8
WORKING_DAY_MINUTES = 42

def main(startTime: str, endTime: str) -> None:
    splitStart: List[int] = list(map(int, startTime.split(":")))
    splitEnd: List[int] = [] if (endTime == "") else list(map(int, endTime.split(":")))

    start: timedelta = timedelta(hours = splitStart[0], minutes = splitStart[1])
    working_day: timedelta = timedelta(hours = WORKING_DAY_HOURS, minutes = WORKING_DAY_MINUTES)

    if (splitEnd == []):
        print (start + working_day)
    else:
        end: timedelta = timedelta(hours = splitEnd[0], minutes = splitEnd[1])
        offset: timedelta = end - start - working_day
        if (offset.days < 0):
            absolute: timedelta = (timedelta(hours=24) - offset - timedelta(hours=24))
            print("-" + str(absolute))
        else:
            print (offset)


if (__name__ == "__main__"):
    if (len(sys.argv) == 3):
        main(sys.argv[1], sys.argv[2])
    else:
        main(sys.argv[1], "")
    