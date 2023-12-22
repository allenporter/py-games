#!/usr/bin/python3

import random
from dataclasses import dataclass, field

LADDERS = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    82: 100,
}
CHUTES = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78,
}
WARPS = {**LADDERS, **CHUTES}

@dataclass
class GameStats:
    rolls: int = 0
    chutes: int = 0
    ladders: int = 0
    positions: list[int] = field(default_factory=list)
    roll_history: list[int] = field(default_factory=list)


def run_game() -> GameStats:
    stats = GameStats()
    pos = 0
    while pos != 100:
        stats.rolls += 1
        #print("Position: ", pos)
        roll = random.randint(1, 6)
        stats.roll_history.append(roll)
        #print("Roll: ", roll)
        new_pos = pos + roll
        if new_pos > 100:
            # At the end, can't roll
            #print("No move")
            continue
        #print("New position: ", new_pos)
        if result := WARPS.get(new_pos):
            if result < new_pos:
                stats.chutes += 1
                #print(f"Chute! ({result})")
            else:
                stats.ladders += 1
                #print(f"Ladder! ({result})")
        else:
            result = new_pos
        pos = result
        stats.positions.append(pos)

    # print("Winner!")
    return stats

def main():
    print("hey there")

    min_game_state = None
    min_rolls = None
    history = []
    for _ in range(0, 1000000):
        stats = run_game()
        history.append(stats)
        #print(stats)
        if min_rolls is None or stats.rolls < min_rolls:
            min_rolls = stats.rolls
            min_game_state = stats
        #print()

    print(f"Minimum rolls: {min_rolls}")
    print(min_game_state)

    total = sum(s.rolls for s in history)
    avg = total / len(history)
    print(f"Average rolls: {avg}")


if __name__ == "__main__":
    main()