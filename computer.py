import random
import math

FIELD_OF_VIEW = 180
RANGE = 1000
LOCK_ON_TIME = 3

def generate_target():
    angle = random.uniform(-FIELD_OF_VIEW/2, FIELD_OF_VIEW/2)
    distance = random.uniform(0, RANGE)
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    return x, y

def detect_target(target):
    x, y = target
    distance = math.sqrt(x**2 + y**2)
    return distance <= RANGE

def select_target(targets):
    closest_target = None
    min_distance = float('inf')
    for target in targets:
        x, y = target
        distance = math.sqrt(x**2 + y**2)
        if distance < min_distance:
            min_distance = distance
            closest_target = target
    return closest_target

def lock_on_target(target):
    print(f"Locking onto target at position {target}...")
    for i in range(LOCK_ON_TIME):
        print(f"Locking... {i+1}")
    print("Target locked!")

def targeting_computer():
    while True:
        targets = [generate_target() for _ in range(5)]
        print("Targets detected:", targets)

        in_range_targets = list(filter(detect_target, targets))

        if not in_range_targets:
            print("No targets within range.")
            continue

        target = select_target(in_range_targets)
        print(f"Closest target selected at position {target}")

        lock_on_target(target)

        break

if __name__ == "__main__":
    targeting_computer()
