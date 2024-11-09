#!/usr/bin/env python
# coding: utf-8

# In[2]:


from ibm_watsonx_ai.foundation_models import Model
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.foundation_models import ModelInference
from langchain_core.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
import os
import getpass


# In[3]:


def get_credentials():
	return {
		"url" : "https://eu-de.ml.cloud.ibm.com",
		"apikey" : "Jq8P15FmG-lxwhWU0Zm5mGLVkREuDH4mqTCvy6_UHTg1"
	}


# In[4]:


model_id = "sdaia/allam-1-13b-instruct"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 900,
    "repetition_penalty": 1
}
project_id = "9c0b7793-7781-4139-8205-44ba471b2f82"
space_id = os.getenv("SPACE_ID")


# In[5]:


model = Model(
	model_id = model_id,
	params = parameters,
	credentials = get_credentials(),
	project_id = project_id,
	space_id = space_id
	)
# ده الكود الي هتضيفة 
# WCKVEXBu_aF-FqplNg7W3VxhWn3GT8DaAce0LPWHU6LC


# In[6]:


watsonx_llm = WatsonxLLM(watsonx_model=model)


# In[7]:


examples = [
    {
        "query": "أحب القراءة والكتابة في الليل ولاكن أحتاج إلى الضوء.",
        "answer": """التصحيح:
 "أحب القراءة والكتابة في الليل ولكن أحتاج إلى الضوء."

الإعراب:

أحب: فعل مضارع مرفوع وعلامة رفعه الضمة الظاهرة على آخره. والفاعل ضمير مستتر تقديره "أنا".
القراءة: مفعول به منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
والكتابة: الواو حرف عطف، "الكتابة" مفعول به منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
في: حرف جر.
الليل: اسم مجرور بـ "في" وعلامة جره الكسرة الظاهرة على آخره.
ولكن: حرف عطف مبني على السكون لا محل له من الإعراب.
أحتاج: فعل مضارع مرفوع وعلامة رفعه الضمة الظاهرة على آخره. والفاعل ضمير مستتر تقديره "أنا".
إلى: حرف جر.
الضوء: اسم مجرور بـ "إلى" وعلامة جره الكسرة الظاهرة على آخره."""
    }, {
        "query": " ذهبوا الولد إلى المدرسة.",
        "answer": """التصحيح:
ذهبَ الولدُ إلى المدرسة.

الإعراب:

ذهبَ: فعل ماضٍ مبني على الفتح.
الولدُ: فاعل مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
إلى: حرف جر.
المدرسةِ: اسم مجرور بحرف الجر "إلى" وعلامة جره الكسرة الظاهرة على آخره.
"""
    }, {
        "query":" الطلاب في المدرسة يلعبون الكرة في الساحة الكبيرة صباحا قبل بدأ الحصص الدراسية.",
        "answer":""" التصحيح:

الطلابُ في المدرسةِ يلعبون الكرةَ في الساحةِ الكبيرةِ صباحًا قبلَ بدءِ الحصصِ الدراسية.

الإعراب:

الطلابُ: مبتدأ مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
في: حرف جر.
المدرسةِ: اسم مجرور بحرف الجر "في" وعلامة جره الكسرة الظاهرة على آخره.
يلعبون: فعل مضارع مرفوع بثبوت النون لأنه من الأفعال الخمسة، والواو ضمير متصل في محل رفع فاعل.
الكرةَ: مفعول به منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
في: حرف جر.
الساحةِ: اسم مجرور بحرف الجر "في" وعلامة جره الكسرة الظاهرة على آخره.
الكبيرةِ: صفة للساحة مجرورة وعلامة جرها الكسرة الظاهرة على آخرها.
صباحًا: ظرف زمان منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
قبلَ: ظرف زمان منصوب وعلامة نصبه الفتحة الظاهرة على آخره، وهو مضاف.
بدءِ: مضاف إليه مجرور وعلامة جره الكسرة الظاهرة على آخره.
الحصصِ: مضاف إليه مجرور وعلامة جره الكسرة الظاهرة على آخره.
الدراسيةِ: صفة للحصص مجرورة وعلامة جرها الكسرة الظاهرة على آخرها."""
    },{
         "query":" إذا الريح يهدي الغصون تارةً و تعصف الأوراق كأنها طيرا.",
        "answer":"""التصحيح:
إذا الريحُ تهدي الغصونَ تارةً وتَعصفُ الأوراقُ كأنها طيرٌ.

الإعراب:

إذا: ظرف لما يُستقبل من الزمان خافض لشرطه، متضمن معنى الشرط.
الريحُ: مبتدأ مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
تهدي: فعل مضارع مرفوع وعلامة رفعه الضمة المقدرة، والفاعل ضمير مستتر تقديره هي (يعود على الريح).
الغصونَ: مفعول به منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
تارةً: ظرف زمان منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
وتعصفُ: الواو حرف عطف، تَعصفُ: فعل مضارع مرفوع وعلامة رفعه الضمة الظاهرة، والفاعل ضمير مستتر تقديره هي (يعود على الريح).
الأوراقُ: فاعل مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
كأنَّ: حرف تشبيه ونصب.
ها: ضمير متصل في محل نصب اسم كأنّ (يعود على الأوراق).
طيرٌ: خبر كأنّ مرفوع وعلامة رفعه الضمة الظاهرة على آخره."""
    },{
        "query":" البحر يعانق السماء كأنه رمالها تتلألأ في ضوء القمر.",
        "answer":"""التصحيح:
البحرُ يعانقُ السماءَ كأنها رمالٌ تتلألأ في ضوء القمر.

الإعراب:

البحرُ: مبتدأ مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
يعانقُ: فعل مضارع مرفوع وعلامة رفعه الضمة الظاهرة على آخره، والفاعل ضمير مستتر تقديره هو (يعود على البحر)، والجملة من الفعل والفاعل في محل رفع خبر المبتدأ.
السماءَ: مفعول به منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
كأنَّ: حرف تشبيه ونصب.
ها: ضمير متصل في محل نصب اسم كأنّ (يعود على السماء).
رمالٌ: خبر كأنّ مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
تتلألأ: فعل مضارع مرفوع وعلامة رفعه الضمة الظاهرة، والفاعل ضمير مستتر تقديره هي (يعود على الرمال)، والجملة الفعلية في محل رفع صفة لرمال.
في: حرف جر.
ضوءِ: اسم مجرور بحرف الجر "في" وعلامة جره الكسرة الظاهرة على آخره، وهو مضاف.
القمرِ: مضاف إليه مجرور وعلامة جره الكسرة الظاهرة على آخره.
"""
    }
]


# In[12]:


example_template = """
User: {query}
AI: {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)

prefix = """[INST]المهمة: أنت خبير في اللغة العربية وقواعد النحو.

التوجيه: قم بإعراب الجملة التالية بتفصيل دقيق لكل عنصر نحوي، مع تقديم الشرح بشكل مختصر وواضح.

يرجى تصحيح  الجملة لغويا ونحويا مع الحفاظ علي المعنى.

"""
# and the suffix our user input and output indicator
suffix = """
User: {query}
AI:[/INST] """

# now create the few shot prompt template
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n\n"
)


# In[14]:


def output_function(question):
    prompt=few_shot_prompt_template.format(query=question)
    return model.generate_text(prompt=prompt, guardrails=False)

