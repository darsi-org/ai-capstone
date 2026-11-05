<div dir="rtl">

# المشروع الختامي: مصنّف مشاعر للنصوص العربية، مختبَر بصدق


> **ملخص درسي قصير عن قصد.** الدرس في التطبيق بيعرض خطوات ضغط مختصرة. الـ README ده بيحفظ الأوامر الكاملة وإصلاح الأخطاء والخلفية لكل مرحلة — افتح قسم **المرحلة N** لما تحتاج تفاصيل.

درّب مصنّف حقيقي لمراجعات عربية: خط أساس بـ scikit-learn، وبعدين BERT عربي صغير على Colab المجاني، متتتبَّع بـ MLflow، ومتدروس على أخطاء اللهجة المصرية، ومتشارك كعرض Gradio مع بطاقة موديل صادقة.

[English](README.md)

## هتقدر تعمل إيه

- تشغّل أدوات حقيقية مجانية من اللابتوب أو Codespaces
- تخلّص خمس مراحل، كل مرحلة ليها فحص تقدر تتأكد منه بنفسك
- تطلع بقطعة بورتفوليو: تقرير أو عرض أو أداة بإصدار v1.0
- **درسي مش بيشغّل كودك أبدًا** — بيقرا الرابط وملف الفحص وبمراجعة استشارية

## ثبّت مرة واحدة

### ويندوز

١. ثبّت Python 3.12: افتح PowerShell واكتب winget install Python.Python.3.12
٢. ثبّت Git: winget install Git.Git
٣. ثبّت VS Code من https://code.visualstudio.com مجانًا
٤. على GitHub افتح https://github.com/darsi-org/ai-capstone واضغط Use this template، وبعدين Clone نسختك
٥. جوّه فولدر المشروع شغّل:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python check.py

### ماك

١. ثبّت Homebrew من https://brew.sh لو مش متثبت
٢. brew install python@3.12 git
٣. ثبّت VS Code من https://code.visualstudio.com
٤. على GitHub افتح https://github.com/darsi-org/ai-capstone → Use this template → Clone نسختك
٥. جوّه فولدر المشروع شغّل:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py

### Codespaces / Colab

معندكش كمبيوتر؟ استخدم GitHub Codespaces: افتح نسختك → Code → Codespaces → Create codespace. كل حاجة هتتثبت هناك. أو افتح دفتر في Google Colab، شغّل أول خلية بتنسخ الريبو، وبعدين python check.py. الاتنين بيشتغلوا من لابتوب مستعار؛ ومتصفح الموبايل يكفي تقرا النتائج.

## البداية

اضغط **Use this template** على https://github.com/darsi-org/ai-capstone، Clone نسختك، وبعدين اتبع المرحلة ١.

## المراحل

### m1: بطاقة بيانات لمراجعات عربية حقيقية (3 ساعات)

## ليه ده مهم
معظم مجموعات العربية فصحى أو خليجي. قبل ما تدرّب، لازم تقول مين كتب المراجعات وأنهي لهجات ناقصة.

## الأدوات للمرحلة دي
- **datasets** — بيحمّل LABR أو ar_res_reviews من Hugging Face. هتجيبه من: pip install -r requirements.txt
- **Hugging Face Hub** — بيستضيف المجموعات العامة. هتجيبه من: https://huggingface.co — free account

## اعمل كده
1. Clone https://github.com/darsi-org/ai-capstone وجهّز الـ venv.
2. شغّل: python fetch_data.py. بينزّل LABR افتراضيًا ويكتب data/split.json ببذرة ثابتة.
3. عدّ الإيجابي مقابل السلبي. متوازن؟ اقرا ٣٠ مراجعة وسجّل اللهجة والسخرية والإيموجي والكلمات الإنجليزي.
4. اكتب DATA_CARD.md: المصدر، والترخيص، والحجم، والتوازن، واللهجات، ومين كتب المراجعات.
5. شغّل python check.py --milestone m1.

## هتبقى خلصت لما
- DATA_CARD.md بيذكر الترخيص
- data/split.json موجود
- m1 ناجحة

## لو حاجة وقفت
- **تحميل datasets فشل** → حاول تاني؛ أو غيّر NAME في fetch_data.py لـ hadyelsahar/ar_res_reviews
- **مساحة خلصت على Colab** → Runtime → Disconnect and delete runtime، وبعدين عيد الجلب

## إيه اللي لازم تفهمه
تقدر توثّق مجموعة بيانات حقيقية عشان حد تاني يعرف فجوات اللهجة قبل ما يثق في الموديل.

**المطلوب تسليمه:** DATA_CARD.md، وdata/split.json، وملاحظات الـ ٣٠ مراجعة، وdarsi-check.json بيجتاز m1.

### m2: خط أساس: TF-IDF وانحدار لوجستي (3 ساعات)

## ليه ده مهم
ترانسفورمر بالكاد بيغلب كيس الكلمات مش مستاهل تمنه. خط الأساس هو الرقم اللي هتغلبه.

## الأدوات للمرحلة دي
- **scikit-learn** — TfidfVectorizer مع LogisticRegression. هتجيبه من: in requirements.txt

## اعمل كده
1. كمّل baseline.py: TF-IDF للكلمات والحروف، وانحدار لوجستي، ومقاييس التحقق.
2. احفظ الدقة واستدعاء كل فئة وmacro F1 ومصفوفة التباس في results/baseline.json.
3. اعرض ٢٠ كلمة بأكبر أوزان لكل فئة. معقولة؟
4. شغّل python check.py --milestone m2.

## هتبقى خلصت لما
- results/baseline.json فيه macro_f1 وconfusion
- m2 ناجحة

## لو حاجة وقفت
- **التوكنات العربي باينة مكسورة** → استخدم مدى n-gram للحروف كمان؛ تقسيم الكلمات لوحده بيتعب مع اللواصق
- **macro F1 ناقص** → from sklearn.metrics import classification_report, f1_score

## إيه اللي لازم تفهمه
تقدر تبني خط أساس كلاسيكي قوي وتقرا أنهي كلمات بيثق فيها.

**المطلوب تسليمه:** results/baseline.json، وأهم الكلمات، وdarsi-check.json بيجتاز m2.

### m3: ترانسفورمر متتتبَّع بـ MLflow (4 ساعات)

## ليه ده مهم
الضبط الدقيق محتاج GPU مجاني مرة، وسجل للي جربته، وإلا هتضيع المقارنة.

## الأدوات للمرحلة دي
- **Google Colab** — ساعات GPU مجانية للضبط الدقيق. هتجيبه من: https://colab.research.google.com — Runtime → T4 GPU
- **transformers / CAMeLBERT** — موديل مشاعر عربي جاهز. هتجيبه من: pip in the notebook
- **MLflow** — بيسجّل المقاييس عشان تقارن التشغيلات. هتجيبه من: pip install mlflow

## اعمل كده
1. افتح notebooks/03_transformer.ipynb في Colab. خلّي Runtime على T4 GPU.
2. اضبط CAMeLBERT، أو قيّمه من غير ضبط كخط أساس تاني. سجّل التشغيلين بـ mlflow.log_metric.
3. خد سكرين للمقارنة في docs/. قرّر مين كسب، مع حساب الوقت والحجم.
4. زوّد رابط الدفتر. احفظ results/transformer.json. شغّل python check.py --milestone m3.

## هتبقى خلصت لما
- results/transformer.json فيه macro_f1
- docs/ فيه سكرين MLflow
- m3 ناجحة

## لو حاجة وقفت
- **CUDA out of memory** → صغّر الـ batch لـ ٨ أو ٤، أو اضبط على جزء الأول
- **Colab اتقطع** → احفظ نقاط الحفظ على Drive؛ كمّل من آخر خطوة
- **واجهة MLflow مش بتفتح في Colab** → استخدم mlflow.log_metric وصدّر جدول مقاييس؛ سكرين للجدول يكفي

## إيه اللي لازم تفهمه
تقدر تضبط ترانسفورمر عربي صغير، تسجّل التشغيل، وتختار وانت شايف التكلفة.

**المطلوب تسليمه:** رابط الدفتر، وسكرين MLflow، وresults/transformer.json، وdarsi-check.json بيجتاز m3.

### m4: ادرس الأخطاء: اللهجة المصرية والسخرية (4 ساعات)

## ليه ده مهم
الجزء المهم فين بيفشل على الجمل المصرية والسخرية — ده اللي المستخدمين هيكتبوه.

## الأدوات للمرحلة دي
- **Your own labelled sentences** — ٥٠ سطر مصري قصير؛ من غير سحب بوستات ناس. هتجيبه من: you write them

## اعمل كده
1. اجمع ٣٠ غلطة من التحقق وصنّفهم: سخرية، نفي، لهجة، لغة مختلطة، تسمية غلط.
2. اكتب ٥٠ جملة مصرية قصيرة بنفسك، سمّيهم، احفظ في data/egyptian.jsonl.
3. قيّم الاتنين موديلات على المجموعة دي. بلّغ عن الفجوة مقابل التحقق الأصلي في results/errors.json.
4. جرّب إصلاح واحد (زوّد حوالي ٢٠٠ سطر مصري كتبته للتدريب) وقيس تاني.
5. شغّل python check.py --milestone m4.

## هتبقى خلصت لما
- data/egyptian.jsonl فيه ٥٠ سطر على الأقل
- results/errors.json فيه gap
- m4 ناجحة

## لو حاجة وقفت
- **خطأ قراءة jsonl** → كائن JSON واحد لكل سطر فيه text وlabel
- **الفجوة سالبة** → ممكن يكون طبيعي؛ بلّغ واشرح

## إيه اللي لازم تفهمه
تقدر تقيس انزياح اللهجة بجمل تملكها، وتجرّب إصلاح من غير ما تسحب بوستات خاصة.

**المطلوب تسليمه:** جدول أخطاء، وdata/egyptian.jsonl، وresults/errors.json، وdarsi-check.json بيجتاز m4.

### m5: اطلق عرض مع بطاقة موديل صادقة (3 ساعات)

## ليه ده مهم
عرض من غير حدود بيبقى دعاية. بطاقة الموديل هي طريقة تفضل مسؤول لما غرباء يجرّبوه.

## الأدوات للمرحلة دي
- **Gradio** — بيبني عرض ويب صغير. هتجيبه من: in requirements.txt
- **Hugging Face Spaces** — بيستضيف العرض. هتجيبه من: https://huggingface.co/spaces — free CPU basic

## اعمل كده
1. كمّل app.py كعرض Gradio لموديلك المختار.
2. انشر على Space مجاني في Hugging Face وحط الرابط في README.md.
3. قيّم الموديل النهائي مرة على الاختبار.
4. اكتب MODEL_CARD.md: الاستخدام المقصود، والممنوع، والبيانات، والمقاييس عامة وعلى مجموعتك المصرية، والأخطاء المعروفة، وإزاي تبلغ عن مشكلة.
5. حط وسم v1.0. شغّل python check.py --milestone m5. اشرحه على درسي.

## هتبقى خلصت لما
- رابط الـ Space بيفتح
- MODEL_CARD.md موجود
- v1.0 وm5 ناجحين

## لو حاجة وقفت
- **بناء الـ Space فشل عشان ملف موديل ناقص** → حمّل من معرّف الـ Hub، أو ارفع ملف ONNX/skops صغير تحت حد الحجم
- **Gradio بيقفل على روابط Colab بتنتهي** → استخدم Space لرابط ثابت

## إيه اللي لازم تفهمه
تقدر تطلق عرض غرباء يجرّبوه، مع بطاقة بترفض الاستخدامات غير الآمنة مكتوبة.

**المطلوب تسليمه:** رابط الـ Space، وMODEL_CARD.md، وv1.0، وdarsi-check.json بيجتاز m5، وشرحك.

## الفحص

شغّل `python check.py` أو `python check.py --milestone m2`. بيقرا الملفات بس، بيكتب `darsi-check.json`، وبيطبّع بالإنجليزي والعربي. مش بيرفع حاجة.

## المراجعة على درسي

ابعت رابط الريبو و`darsi-check.json` مع كل مرحلة على درسي. درسي بيقرا آخر تشغيل Actions والإصدار من واجهة GitHub العامة، بيضيف مراجعة استشارية بالذكاء الاصطناعي، وبعدين معلّمك أو فريق درسي بيراجع. **درسي مش بيشغّل كودك.**

## الترخيص

MIT — شوف [LICENSE](LICENSE).

</div>
