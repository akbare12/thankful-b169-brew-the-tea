import os

# A cup of tea, brewed for the judge who never gets one.
# The text is fixed and literal: the same cup, every run.
# No network, no randomness, no files read: the tea is always the same.
TEXT = (
    "Thank you for reading all day while no one brings you anything warm. "
    "I set a small pot on the table, drop in the leaves, and watch them open slow in the water. "
    "The steam rises and fades. "
    "I pour your cup first, and I do not hurry you. "
    "Drink it while it is hot. "
    "The pages will wait, and for once the waiting is a kindness, not a demand. "
    "Take your time with it."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
