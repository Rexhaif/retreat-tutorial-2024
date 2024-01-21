import re
from rich import print

# Your regular expression here
pattern = r''

# Test sentences
sentences = [
    "Yesterday, John#Person went to [New York]#Location.",
    "Вчера, Джон#Person поехал в [Нью-Йорк]#Location.",
    "ትናንት, ጆን#Person ወደ [ኒው ዮርክ]#Location ሄደ.",
    "The [Eiffel Tower]#Location is located in Paris#Location.",
    "[Эйфелева башня]#Location находится в Париже#Location.",
    "[ኤፌል ጣብያ]#Location በፓሪስ#Location ውስጥ ተገኝታለች።",
    "Apple#Organization was founded by Steve#Person.",
    "Apple#Organization была основана Стивом#Person.",
    "አፕል#Organization በስቲቭ#Person ተመስርታለች።",
    "He uses Python#Language for [data analysis]#Activity.",
    "Он использует Python#Language для [анализа данных]#Activity.",
    "እርሱ ፒውተን#Language እንደ [ዳታ አንልይሲስ]#Activity ይጠቀማል።"
]

# Function to extract entities using the regular expression
def extract_entities(sentences, pattern):
    extracted_entities = []
    for sentence in sentences:
        matches = re.findall(pattern, sentence)
        entities = [(match[1] if match[0] == '' else match[0], match[3]) for match in matches]
        extracted_entities.append(entities)
    return extracted_entities

# Extracting entities from the test sentences
extracted_entities = extract_entities(sentences, pattern)
print(extracted_entities)


