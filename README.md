# Capstone: an Arabic sentiment classifier, honestly tested


> **Darsi briefs are short on purpose.** The in-app lesson shows tight numbered clicks. This README keeps the full commands, error fixes, and background for each milestone — open the matching **Milestone N** section when you need detail.

Train a real classifier for Arabic reviews: a scikit-learn baseline, then a small Arabic BERT on free Colab, tracked with MLflow, studied for Egyptian-dialect mistakes, and shared as a Gradio demo with an honest model card.

[العربية](README.ar.md)

## What you will be able to do

- Run real free tools from a laptop or Codespaces
- Finish five milestones, each with checks you can self-verify
- Leave with a portfolio piece: a report, demo or tool tagged v1.0
- **Darsi never runs your code** — it reads your link and check file, then an advisory review

## Install once

### Windows

1. Install Python 3.12: open PowerShell and run `winget install Python.Python.3.12`
2. Install Git: `winget install Git.Git`
3. Install VS Code from https://code.visualstudio.com (free)
4. On GitHub, open https://github.com/darsi-org/ai-capstone and press **Use this template** to make your own copy. Then clone your copy, not darsi-org's: `git clone https://github.com/<your-username>/ai-capstone.git`
5. Open a new PowerShell, go into the folder with `cd ai-capstone`, and run these lines one at a time:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python check.py
   ```

   If PowerShell says running scripts is disabled on this system, you don't need to change any setting: use Command Prompt and run `.venv\Scripts\activate.bat` instead, or skip activating and start every command with `.venv\Scripts\python` (for example `.venv\Scripts\python -m pip install -r requirements.txt`, then `.venv\Scripts\python check.py`).

### Mac

1. Install Homebrew from https://brew.sh if you don't have it
2. Install Python and Git: `brew install python@3.12 git`
3. Install VS Code from https://code.visualstudio.com
4. On GitHub, open https://github.com/darsi-org/ai-capstone, press **Use this template**, then clone your copy: `git clone https://github.com/<your-username>/ai-capstone.git`
5. In Terminal, go into the folder with `cd ai-capstone` and run:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py
   ```

### Codespaces / Colab

No computer of your own? Use GitHub Codespaces, from a borrowed laptop too: open your copy → **Code** → **Codespaces** → **Create codespace**. Python and Git are already there. In its terminal, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check.py
```

Or use Google Colab for the notebook in notebooks/: open `https://colab.research.google.com/github/<your-username>/ai-capstone/blob/main/notebooks/03_transformer.ipynb` (your username in place of `<your-username>`), put your copy's address in the first cell and run the cells in order. That cell clones your copy and moves into it. Colab works on its own copy, so download what you made there (results/transformer.json, from the Files panel) and add it to your copy with your screenshot docs/mlflow.png (in Codespaces or VS Code, drag them into the file list, then commit and push).

A phone browser is enough to read the results.

## Start

Press **Use this template** on https://github.com/darsi-org/ai-capstone, clone your copy, then follow milestone 1.

## Milestones

### m1: A data card for real Arabic reviews (3 hours)

#### Why this matters
Most Arabic datasets are MSA or Gulf. Before you train, you must say who wrote the reviews and which dialects are missing.

#### Tools for this milestone
- **datasets** — loads LABR or ar_res_reviews from Hugging Face. Get it: pip install -r requirements.txt
- **Hugging Face Hub** — hosts the public datasets. Get it: https://huggingface.co — free account

#### Do this
1. Set up your copy as in **Install once** (your copy, not darsi-org's).
2. Run: python fetch_data.py. It downloads LABR by default and writes data/split.json with a fixed seed.
3. Count positive vs negative. LABR's `label` is the star rating (0 = 1 star … 4 = 5 stars): 1–2 stars are negative, 4–5 stars are positive, and 3-star reviews are dropped, because they are neither (the m3 notebook does the same). ar_res_reviews has a `polarity` column instead: 0 negative, 1 positive. Is it balanced? Read 30 reviews and note dialect, sarcasm, emojis, English words.
4. Write DATA_CARD.md: source, licence, size (and how many 3-star reviews you dropped), balance, dialects, who wrote these reviews.
5. Run python check.py --milestone m1.

#### You know you're done when
- DATA_CARD.md names the licence
- data/split.json exists
- m1 passes

#### If something goes wrong
- **datasets download fails** → Retry; or set NAME in fetch_data.py to hadyelsahar/ar_res_reviews
- **Out of disk on Colab** → Runtime → Disconnect and delete runtime, then rerun fetch

#### What you should understand
You can document a real dataset so someone else knows its dialect gaps before trusting the model.

**Hand in:** DATA_CARD.md, data/split.json, your 30-review notes, and darsi-check.json that passes m1.

### m2: A baseline: TF-IDF and logistic regression (3 hours)

#### Why this matters
A transformer that barely beats bag-of-words is not worth its cost. The baseline is the number to beat.

#### Tools for this milestone
- **scikit-learn** — TfidfVectorizer + LogisticRegression. Get it: in requirements.txt

#### Do this
1. Complete baseline.py: word and character TF-IDF, logistic regression, validation metrics, with the same labels as m1 (3-star reviews dropped).
2. Save accuracy, per-class recall, macro F1 and a confusion matrix into results/baseline.json.
3. List the 20 words with the biggest weights per class. Do they make sense?
4. Run python check.py --milestone m2.

#### You know you're done when
- results/baseline.json has macro_f1 and confusion
- m2 passes

#### If something goes wrong
- **Arabic tokens look broken** → Use a character n-gram range too; word splits alone struggle with clitics
- **Macro F1 missing** → from sklearn.metrics import classification_report, f1_score

#### What you should understand
You can build a strong classical baseline and read which words it trusts.

**Hand in:** results/baseline.json, top words, and darsi-check.json that passes m2.

### m3: A transformer, tracked with MLflow (4 hours)

#### Why this matters
Fine-tuning needs a free GPU once, and a log of what you tried, or you will lose the comparison.

#### Tools for this milestone
- **Google Colab** — free GPU hours for fine-tuning. Get it: https://colab.research.google.com — Runtime → T4 GPU
- **transformers / CAMeLBERT** — CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment. Get it: pip in the notebook
- **MLflow** — logs metrics so you can compare runs. Get it: pip install mlflow

#### Do this
1. Open notebooks/03_transformer.ipynb in Colab (the link is under **Codespaces / Colab** above). Set Runtime to T4 GPU, put your copy's address in the first cell, then run the cells in order.
2. The notebook makes two runs and logs both with mlflow.log_metric: CAMeLBERT scored as it is (a second baseline), then fine-tuned with Trainer on your training reviews.
3. Take a screenshot of its comparison table and save it as docs/mlflow.png. Decide which run wins, counting time and size too, and write why in the notebook's `WHY` line.
4. Download results/transformer.json from Colab's Files panel. Add it and docs/mlflow.png to your copy, add the notebook link, and run python check.py --milestone m3.

#### The neutral rule
CAMeLBERT has three labels: positive, negative and neutral. Your reviews have two, so neutral never counts as an answer: compare only the positive and negative scores and pick the larger. Fine-tune with the same three-label head, training only on positive and negative, so neutral is never a target. The notebook does both, and reports `neutral_share`, how often neutral would have won: note it, because it shows how many reviews the model finds unclear.

#### You know you're done when
- results/transformer.json has macro_f1
- docs/mlflow.png is your MLflow screenshot
- m3 passes

#### If something goes wrong
- **CUDA out of memory** → In the notebook, set `BATCH = 8` (or 4) and run that cell again
- **Colab disconnected** → Run the cells again from the top: the first cell clones your copy again, and fine-tuning takes only a few minutes on a T4
- **MLflow UI won't open in Colab** → You don't need it: the notebook's comparison table comes from MLflow, and a screenshot of that table is enough

#### What you should understand
You can fine-tune a small Arabic transformer, log the run, and choose with cost in mind.

**Hand in:** Notebook link, docs/mlflow.png (MLflow screenshot), results/transformer.json, and darsi-check.json that passes m3.

### m4: Study the mistakes: Egyptian dialect and sarcasm (4 hours)

#### Why this matters
The interesting part is where it fails on Egyptian sentences and sarcasm — that is what your users will write.

#### Tools for this milestone
- **Your own labelled sentences** — 50 short Egyptian lines; no scraping real people's posts. Get it: you write them

#### Do this
1. Collect 30 validation mistakes and sort them: sarcasm, negation, dialect, mixed language, wrong label.
2. Write 50 short Egyptian sentences yourself, label them, save as data/egyptian.jsonl.
3. Score both models on that set. Report the gap vs the original validation set in results/errors.json.
4. Try one fix (add ~200 Egyptian lines you wrote to training) and measure again.
5. Run python check.py --milestone m4.

#### You know you're done when
- data/egyptian.jsonl has at least 50 lines
- results/errors.json has gap
- m4 passes

#### If something goes wrong
- **jsonl parse error** → One JSON object per line with text and label fields
- **Gap is negative** → That can be fine; report it and explain

#### What you should understand
You can measure dialect shift with sentences you own, and try one fix without scraping private posts.

**Hand in:** Error table, data/egyptian.jsonl, results/errors.json, and darsi-check.json that passes m4.

### m5: Ship a demo with an honest model card (3 hours)

#### Why this matters
A demo without limits becomes marketing. A model card is how you stay responsible when strangers try it.

#### Tools for this milestone
- **Gradio** — builds a small web demo. Get it: in requirements.txt
- **Hugging Face Spaces** — hosts the demo. Get it: https://huggingface.co/spaces — free CPU basic

#### Do this
1. Finish app.py as a Gradio demo of your chosen model.
2. Deploy to a free Hugging Face Space and put the link in README.md.
3. Score the final model once on the test set.
4. Write MODEL_CARD.md: intended use, not intended use, data, metrics overall and on your Egyptian set, known failures, how to report a problem.
5. Tag v1.0. Run python check.py --milestone m5. Explain it on Darsi.

#### You know you're done when
- Space link opens
- MODEL_CARD.md exists
- v1.0 and m5 pass

#### If something goes wrong
- **Space build fails on missing model file** → Load from the Hub id, or commit a small ONNX/skops file under size limits
- **Gradio blocks on Colab share links that expire** → Use a Space for a stable link

#### What you should understand
You can ship a demo strangers can try, with a card that refuses unsafe uses in writing.

**Hand in:** Space link, MODEL_CARD.md, v1.0, darsi-check.json that passes m5, and your explanation.

## The check

Run `python check.py` or `python check.py --milestone m2`. It only reads files, writes `darsi-check.json`, and prints English and Arabic. It uploads nothing.

## Review on Darsi

Send your repository link and `darsi-check.json` with each milestone on Darsi. Darsi reads your latest Actions run and release from GitHub's public API, adds an advisory AI review, then your teacher or the Darsi team reviews it. **Darsi never runs your code.**

## Licence

MIT — see [LICENSE](LICENSE).
