from datetime import timedelta
import sys
from typing import List, Iterator

WORKING_DAY_HOURS = 8
WORKING_DAY_MINUTES = 42

def main(startTime: str) -> None:
    splitStart: List[int] = list(map(int, startTime.split(":")))
    start: timedelta = timedelta(hours = splitStart[0], minutes = splitStart[1])
    print (start + timedelta(hours = WORKING_DAY_HOURS, minutes = WORKING_DAY_MINUTES))

if (__name__ == "__main__"):
    main(sys.argv[1])