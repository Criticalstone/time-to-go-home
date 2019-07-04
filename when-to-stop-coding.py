from datetime import timedelta
import sys
from typing import List, Iterator

def main(startTime: str) -> None:
    splitStart: List[int] = list(map(int, startTime.split(":")))
    start: timedelta = timedelta(hours = splitStart[0], minutes = splitStart[1])
    print (start + timedelta(hours = 8, minutes = 42))

if (__name__ == "__main__"):
    main(sys.argv[1])