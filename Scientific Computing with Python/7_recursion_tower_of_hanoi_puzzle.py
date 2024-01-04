# Recursion is a programming approach that allows you to solve complicated computational
# problems with just a little code.

# In this project, you'll start with a loop-based approach to solving the tower of Hanoi
# mathematical puzzle. Then you'll learn how to implement a recursive solution.

NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []


def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)

    # move the nth disk from source to target
    target.append(source.pop())

    # display our progress
    print(A, B, C, "\n")

    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)


# Ensure the code won't run when imported as a module
if __name__ == "__main__":
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, A, B, C)
