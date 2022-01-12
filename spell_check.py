import nltk
import enchant
import re
import pandas as pd

def is_available_sentence(sentence):
    for w in sentence:
        if d.check(w) == False and w.isdecimal() == False:
            return False
    return True

def cleaning(sentence):
    sentence = sentence.lstrip().rstrip()
    sentence = re.sub(r'!+', '.', sentence)
    sentence = re.sub(r'\?+', '?', sentence)
    return sentence
    

if __name__ == "__main__":
    nltk.download("punkt")
    d = enchant.Dict("en_US")
    d.add("n't")
    d.add("'t")
    d.add("'m")
    d.add("'s")
    d.add("'ve")
    d.add("'re")
    d.add("'d")
    d.add("ve")
    d.add("didn")
    d.add("ok")
    d.add("isn")
    d.add("aren")
    d.add("2nd")
    d.add("doesn")

    data = pd.read_csv("scrape_twitter/5row.csv")
    data = data.dropna(how="any")

    all_sentence_cnt = 0
    ok_sentence_cnt = 0
    out_df = pd.DataFrame(columns=["reply", "context1", "context2", "context3", "context4"])
    for _, row in data.iterrows():
        all_sentence_cnt += 1
        is_exist = True
        
        for i in range(5):
            sentence = nltk.word_tokenize(row[i])
            if is_available_sentence(sentence) == False:
                is_exist = False
                continue
            
        if is_exist == False:
            continue
        
        out_df = out_df.append(
            {
                "reply": cleaning(row[0]), 
                "context1": cleaning(row[1]), 
                "context2": cleaning(row[2]), 
                "context3": cleaning(row[3]), 
                "context4": cleaning(row[4]), 
            }, 
            ignore_index=True
            )
        ok_sentence_cnt += 1
        
    percent = ok_sentence_cnt/all_sentence_cnt * 100
    print("%d/%d" % (ok_sentence_cnt, all_sentence_cnt))
    print("%d パーセント" % percent)
    
    out_df.to_csv("normalized_conversation.csv", index=False)