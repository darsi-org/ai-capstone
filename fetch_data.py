"""Download one public Arabic review dataset and make a fixed train/validation/test split (seed 42)."""
import json
import pathlib

from datasets import load_dataset

NAME = "mohamedadaly/labr"  # or "hadyelsahar/ar_res_reviews"
ds = load_dataset(NAME, split="train").shuffle(seed=42)
n = len(ds)
split = {"dataset": NAME, "seed": 42, "train": [0, int(n * 0.8)], "validation": [int(n * 0.8), int(n * 0.9)], "test": [int(n * 0.9), n]}
pathlib.Path("data").mkdir(exist_ok=True)
pathlib.Path("data/split.json").write_text(json.dumps(split, indent=2), encoding="utf-8")
ds.to_csv("data/reviews.csv")
print(split)
