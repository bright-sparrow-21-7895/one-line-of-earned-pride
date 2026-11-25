# One Line of Earned Pride — entry design:
# The pride here is quiet, not loud. The first sentence carries the
# achievement itself: a mother's house paid off with money from a job
# nobody believed in. The second sentence lands the emotional proof —
# the shoebox of receipts by the door — showing the pride is mutual:
# she kept every receipt because she was proud too. Two plain sentences,
# no boasting, the detail does the work.
import os

ENTRY = (
    "I paid off my mother's house with money nobody thought my job could make. "
    "She still keeps every receipt in a shoebox by the door."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
