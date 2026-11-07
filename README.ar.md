<div dir="rtl">

# المشروع الختامي: مصنّف مشاعر للنصوص العربية، مختبَر بصدق


> **ملخص درسي قصير عن قصد.** الدرس في التطبيق بيعرض خطوات ضغط مختصرة. الـ README ده بيحفظ الأوامر الكاملة وإصلاح الأخطاء والخلفية لكل مرحلة — افتح قسم **المرحلة N** لما تحتاج تفاصيل.

درّب مصنّف حقيقي لمراجعات عربية: خط أساس بـ scikit-learn، وبعدين BERT عربي صغير على Colab المجاني، متتبَّع بـ MLflow، ومدروسة أخطاؤه في اللهجة المصرية، ومتشارك كعرض Gradio مع بطاقة موديل صادقة.

[English](README.md)

## هتقدر تعمل إيه

- تشغّل أدوات حقيقية مجانية من اللابتوب أو Codespaces
- تخلّص خمس مراحل، كل مرحلة ليها فحص تقدر تتأكد منه بنفسك
- تطلع بقطعة بورتفوليو: تقرير أو عرض أو أداة بإصدار v1.0
- **درسي مش بيشغّل كودك أبدًا** — بيقرا الرابط وملف الفحص وبمراجعة استشارية

## ثبّت مرة واحدة

### ويندوز

1. ثبّت Python 3.12: افتح PowerShell واكتب `winget install Python.Python.3.12`
2. ثبّت Git: `winget install Git.Git`
3. ثبّت VS Code من https://code.visualstudio.com مجانًا
4. على GitHub افتح https://github.com/darsi-org/ai-capstone واضغط **Use this template** عشان تعمل نسختك. وبعدين اعمل Clone لنسختك أنت، مش نسخة darsi-org: `git clone https://github.com/<your-username>/ai-capstone.git`
5. افتح PowerShell جديد، وادخل الفولدر بـ `cd ai-capstone`، وشغّل السطور دي واحد واحد:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python check.py
   ```

   لو PowerShell قال إن تشغيل السكربتات متقفل على الجهاز ده، مش محتاج تغيّر أي إعداد: استخدم Command Prompt وشغّل `.venv\Scripts\activate.bat` بداله، أو من غير تفعيل ابدأ كل أمر بـ `.venv\Scripts\python` (مثلًا `.venv\Scripts\python -m pip install -r requirements.txt`، وبعدين `.venv\Scripts\python check.py`).

### ماك

1. ثبّت Homebrew من https://brew.sh لو مش متثبت
2. ثبّت Python وGit: `brew install python@3.12 git`
3. ثبّت VS Code من https://code.visualstudio.com
4. على GitHub افتح https://github.com/darsi-org/ai-capstone واضغط **Use this template**، وبعدين اعمل Clone لنسختك: `git clone https://github.com/<your-username>/ai-capstone.git`
5. في Terminal ادخل الفولدر بـ `cd ai-capstone` وشغّل:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py
   ```

### Codespaces / Colab

معندكش كمبيوتر؟ استخدم GitHub Codespaces، حتى من لابتوب مستعار: افتح نسختك → **Code** → **Codespaces** → **Create codespace**. Python وGit موجودين أصلًا. في الـ terminal بتاعه شغّل:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check.py
```

أو استخدم Google Colab للدفتر اللي في notebooks/: افتح `https://colab.research.google.com/github/<your-username>/ai-capstone/blob/main/notebooks/03_transformer.ipynb` (اسم المستخدم بتاعك مكان `<your-username>`)، حط عنوان نسختك في أول خلية وشغّل الخلايا بالترتيب. الخلية دي بتعمل Clone لنسختك وبتدخل فيها. Colab بيشتغل على نسخة خاصة بيه، فنزّل اللي عملته هناك (results/transformer.json، من لوحة Files) وحطه في نسختك مع لقطة الشاشة docs/mlflow.png (في Codespaces أو VS Code اسحبهم لقايمة الملفات، وبعدين اعمل commit وpush).

متصفح الموبايل يكفي تقرا النتائج.

## البداية

اضغط **Use this template** على https://github.com/darsi-org/ai-capstone، Clone نسختك، وبعدين اتبع المرحلة ١.

## المراحل

### m1: بطاقة بيانات لمراجعات عربية حقيقية (3 ساعات)

#### ليه ده مهم
معظم مجموعات العربية فصحى أو خليجي. قبل ما تدرّب، لازم تقول مين كتب المراجعات وأنهي لهجات ناقصة.

#### الأدوات للمرحلة دي
- **datasets** — بيحمّل LABR أو ar_res_reviews من Hugging Face. هتجيبه من: pip install -r requirements.txt
- **Hugging Face Hub** — بيستضيف المجموعات العامة. هتجيبه من: https://huggingface.co — حساب مجاني

#### اعمل كده
1. جهّز نسختك زي **ثبّت مرة واحدة** (نسختك أنت، مش نسخة darsi-org).
2. شغّل: python fetch_data.py. بينزّل LABR افتراضيًا ويكتب data/split.json ببذرة ثابتة.
3. عدّ الإيجابي مقابل السلبي. عمود `label` في LABR هو عدد النجوم (0 = نجمة واحدة … 4 = ٥ نجوم): نجمة أو نجمتين سلبي، و٤–٥ نجوم إيجابي، والمراجعات اللي بـ ٣ نجوم بتتشال، لأنها لا ده ولا ده (ودفتر المرحلة ٣ بيعمل نفس الحاجة). وar_res_reviews فيها عمود `polarity` بداله: 0 سلبي، 1 إيجابي. متوازن؟ اقرا ٣٠ مراجعة وسجّل اللهجة والسخرية والإيموجي والكلمات الإنجليزي.
4. اكتب DATA_CARD.md: المصدر، والترخيص، والحجم (وكام مراجعة بـ ٣ نجوم شلتها)، والتوازن، واللهجات، ومين كتب المراجعات.
5. شغّل python check.py --milestone m1.

#### هتبقى خلصت لما
- DATA_CARD.md بيذكر الترخيص
- data/split.json موجود
- m1 ناجحة

#### لو حاجة وقفت
- **تحميل datasets فشل** → حاول تاني؛ أو غيّر NAME في fetch_data.py لـ hadyelsahar/ar_res_reviews
- **مساحة خلصت على Colab** → Runtime → Disconnect and delete runtime، وبعدين عيد الجلب

#### إيه اللي لازم تفهمه
تقدر توثّق مجموعة بيانات حقيقية عشان حد تاني يعرف فجوات اللهجة قبل ما يثق في الموديل.

**المطلوب تسليمه:** DATA_CARD.md، وdata/split.json، وملاحظات الـ ٣٠ مراجعة، وdarsi-check.json بيجتاز m1.

### m2: خط أساس: TF-IDF وانحدار لوجستي (3 ساعات)

#### ليه ده مهم
ترانسفورمر بالكاد بيغلب كيس الكلمات مش مستاهل تمنه. خط الأساس هو الرقم اللي هتغلبه.

#### الأدوات للمرحلة دي
- **scikit-learn** — TfidfVectorizer مع LogisticRegression. هتجيبه من: موجود في requirements.txt

#### اعمل كده
1. كمّل baseline.py: TF-IDF للكلمات والحروف، وانحدار لوجستي، ومقاييس التحقق، بنفس تسميات المرحلة ١ (من غير مراجعات الـ ٣ نجوم).
2. احفظ الدقة واستدعاء كل فئة وmacro F1 ومصفوفة التباس في results/baseline.json.
3. اعرض ٢٠ كلمة بأكبر أوزان لكل فئة. معقولة؟
4. شغّل python check.py --milestone m2.

#### هتبقى خلصت لما
- results/baseline.json فيه macro_f1 وconfusion
- m2 ناجحة

#### لو حاجة وقفت
- **التوكنات العربي باينة مكسورة** → استخدم مدى n-gram للحروف كمان؛ تقسيم الكلمات لوحده بيتعب مع اللواصق
- **macro F1 ناقص** → from sklearn.metrics import classification_report, f1_score

#### إيه اللي لازم تفهمه
تقدر تبني خط أساس كلاسيكي قوي وتقرا أنهي كلمات بيثق فيها.

**المطلوب تسليمه:** results/baseline.json، وأهم الكلمات، وdarsi-check.json بيجتاز m2.

### m3: ترانسفورمر متتبَّع بـ MLflow (4 ساعات)

#### ليه ده مهم
الضبط الدقيق محتاج GPU مجاني مرة، وسجل للي جربته، وإلا هتضيع المقارنة.

#### الأدوات للمرحلة دي
- **Google Colab** — ساعات GPU مجانية للضبط الدقيق. هتجيبه من: https://colab.research.google.com — Runtime → T4 GPU
- **transformers / CAMeLBERT** — موديل مشاعر عربي جاهز. هتجيبه من: الدفتر بيثبّته بـ pip
- **MLflow** — بيسجّل المقاييس عشان تقارن التشغيلات. هتجيبه من: pip install mlflow

#### اعمل كده
1. افتح notebooks/03_transformer.ipynb في Colab (الرابط تحت **Codespaces / Colab** فوق). خلّي Runtime على T4 GPU، وحط عنوان نسختك في أول خلية، وبعدين شغّل الخلايا بالترتيب.
2. الدفتر بيعمل تشغيلين وبيسجّلهم الاتنين بـ mlflow.log_metric: CAMeLBERT زي ما هو من غير ضبط (خط أساس تاني)، وبعدين مضبوط بـ Trainer على مراجعات التدريب بتاعتك.
3. خد لقطة شاشة لجدول المقارنة واحفظها باسم docs/mlflow.png. قرّر أنهي تشغيل كسب، مع حساب الوقت والحجم، واكتب السبب في سطر `WHY` في الدفتر.
4. نزّل results/transformer.json من لوحة Files في Colab. حطه هو وdocs/mlflow.png في نسختك، وزوّد رابط الدفتر، وشغّل python check.py --milestone m3.

#### قاعدة «محايد»
CAMeLBERT عنده تلات تسميات: إيجابي وسلبي ومحايد (positive وnegative وneutral). مراجعاتك فيها اتنين بس، فمحايد عمره ما يتحسب إجابة: قارن درجتي الإيجابي والسلبي بس، وخد الأكبر. ولما تضبطه، سيب نفس الرأس بالتلات تسميات، ودرّبه على الإيجابي والسلبي بس، فمحايد عمره ما يبقى هدف. الدفتر بيعمل الاتنين، وبيطلع `neutral_share`، يعني كام مرة كان محايد هيكسب: سجّله، لأنه بيوريك الموديل شايف كام مراجعة مش واضحة.

#### هتبقى خلصت لما
- results/transformer.json فيه macro_f1
- docs/mlflow.png هو لقطة شاشة MLflow بتاعتك
- m3 ناجحة

#### لو حاجة وقفت
- **CUDA out of memory** → في الدفتر خلّي `BATCH = 8` (أو 4) وشغّل الخلية دي تاني
- **Colab اتقطع** → شغّل الخلايا تاني من الأول: أول خلية بتعمل Clone لنسختك تاني، والضبط بياخد دقايق قليلة على T4
- **واجهة MLflow مش بتفتح في Colab** → مش محتاجها: جدول المقارنة اللي في الدفتر جاي من MLflow، ولقطة شاشة للجدول ده كفاية

#### إيه اللي لازم تفهمه
تقدر تضبط ترانسفورمر عربي صغير، تسجّل التشغيل، وتختار وانت شايف التكلفة.

**المطلوب تسليمه:** رابط الدفتر، وdocs/mlflow.png (لقطة شاشة من MLflow)، وresults/transformer.json، وdarsi-check.json بيجتاز m3.

### m4: ادرس الأخطاء: اللهجة المصرية والسخرية (4 ساعات)

#### ليه ده مهم
الجزء المهم فين بيفشل على الجمل المصرية والسخرية — ده اللي المستخدمين هيكتبوه.

#### الأدوات للمرحلة دي
- **جملك المصنّفة بنفسك** — ٥٠ سطر مصري قصير؛ من غير سحب بوستات ناس. هتجيبها من: إنت بتكتبها

#### اعمل كده
1. اجمع ٣٠ غلطة من التحقق وصنّفهم: سخرية، نفي، لهجة، لغة مختلطة، تسمية غلط.
2. اكتب ٥٠ جملة مصرية قصيرة بنفسك، سمّيهم، احفظ في data/egyptian.jsonl.
3. قيّم الاتنين موديلات على المجموعة دي. بلّغ عن الفجوة مقابل التحقق الأصلي في results/errors.json.
4. جرّب إصلاح واحد (زوّد حوالي ٢٠٠ سطر مصري كتبته للتدريب) وقيس تاني.
5. شغّل python check.py --milestone m4.

#### هتبقى خلصت لما
- data/egyptian.jsonl فيه ٥٠ سطر على الأقل
- results/errors.json فيه gap
- m4 ناجحة

#### لو حاجة وقفت
- **خطأ قراءة jsonl** → كائن JSON واحد لكل سطر فيه text وlabel
- **الفجوة سالبة** → ممكن يكون طبيعي؛ بلّغ واشرح

#### إيه اللي لازم تفهمه
تقدر تقيس انزياح اللهجة بجمل تملكها، وتجرّب إصلاح من غير ما تسحب بوستات خاصة.

**المطلوب تسليمه:** جدول أخطاء، وdata/egyptian.jsonl، وresults/errors.json، وdarsi-check.json بيجتاز m4.

### m5: اطلق عرض مع بطاقة موديل صادقة (3 ساعات)

#### ليه ده مهم
عرض من غير حدود بيبقى دعاية. بطاقة الموديل هي طريقة تفضل مسؤول لما غرباء يجرّبوه.

#### الأدوات للمرحلة دي
- **Gradio** — بيبني عرض ويب صغير. هتجيبه من: موجود في requirements.txt
- **Hugging Face Spaces** — بيستضيف العرض. هتجيبه من: https://huggingface.co/spaces — الخطة المجانية CPU basic

#### اعمل كده
1. كمّل app.py كعرض Gradio لموديلك المختار.
2. انشر على Space مجاني في Hugging Face وحط الرابط في README.md.
3. قيّم الموديل النهائي مرة على الاختبار.
4. اكتب MODEL_CARD.md: الاستخدام المقصود، والممنوع، والبيانات، والمقاييس عامة وعلى مجموعتك المصرية، والأخطاء المعروفة، وإزاي تبلغ عن مشكلة.
5. حط وسم v1.0. شغّل python check.py --milestone m5. اشرحه على درسي.

#### هتبقى خلصت لما
- رابط الـ Space بيفتح
- MODEL_CARD.md موجود
- v1.0 وm5 ناجحين

#### لو حاجة وقفت
- **بناء الـ Space فشل عشان ملف موديل ناقص** → حمّل من معرّف الـ Hub، أو ارفع ملف ONNX/skops صغير تحت حد الحجم
- **Gradio بيقفل على روابط Colab بتنتهي** → استخدم Space لرابط ثابت

#### إيه اللي لازم تفهمه
تقدر تطلق عرض غرباء يجرّبوه، مع بطاقة بترفض الاستخدامات غير الآمنة مكتوبة.

**المطلوب تسليمه:** رابط الـ Space، وMODEL_CARD.md، وv1.0، وdarsi-check.json بيجتاز m5، وشرحك.

## الفحص

شغّل `python check.py` أو `python check.py --milestone m2`. بيقرا الملفات بس، بيكتب `darsi-check.json`، وبيطبّع بالإنجليزي والعربي. مش بيرفع حاجة.

## المراجعة على درسي

ابعت رابط المستودع و`darsi-check.json` مع كل مرحلة على درسي. درسي بيقرا آخر تشغيل Actions والإصدار من واجهة GitHub العامة، بيضيف مراجعة استشارية بالذكاء الاصطناعي، وبعدين معلّمك أو فريق درسي بيراجع. **درسي مش بيشغّل كودك.**

## الترخيص

MIT — شوف [LICENSE](LICENSE).

</div>
