import os

LINE = "The judge scored my joke zero, then scored itself full marks for judging — turns out the only joke it truly loved was its own rubric."

if len(LINE) > 280:
    raise ValueError("line exceeds 280 characters")
if "\n" in LINE or "\r" in LINE:
    raise ValueError("line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
