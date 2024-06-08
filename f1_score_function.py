# 1) f1 score function
def calc_f1_score (tp, fp, fn):
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        raise TypeError("Input must be an integer")
    if tp <= 0 or fp <= 0 or fn <= 0:
        raise ValueError("Input must be a positive integer")
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

assert round(calc_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(round(calc_f1_score(tp =2, fp =4, fn =5), 2))