import nltk
import enchant
import pandas as pd

def is_available_sentence(sentence):
    for w in sentence:
        if d.check(w) == False and w.isdecimal() == False:
            return False
    return True

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

    data = pd.read_csv("src/data/twitter_conversation.csv")
    data = data.dropna(how="any")

    all_sentence_cnt = 0
    ok_sentence_cnt = 0
    out_df = pd.DataFrame(columns=["reply", "context"])
    for _, row in data.iterrows():
        all_sentence_cnt += 1
        is_exist = True
        context = nltk.word_tokenize(row[1])
        if is_available_sentence(context) == False:
            continue
        
        reply = nltk.word_tokenize(row[0])
        if is_available_sentence(reply) == False:
            continue
        
        out_df = out_df.append({"reply": row[0], "context": row[1]}, ignore_index=True)
        ok_sentence_cnt += 1
        
    percent = ok_sentence_cnt/all_sentence_cnt * 100
    print("%d/%d" % (ok_sentence_cnt, all_sentence_cnt))
    print("%d パーセント" % percent)
    
    out_df.to_csv("normalized_conversation.csv", index=False)