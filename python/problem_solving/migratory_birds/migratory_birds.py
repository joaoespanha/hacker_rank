from collections import Counter


def migratoryBirds(arr):
    bird_count = Counter(arr)
    top_counts = bird_count.most_common(2)

    if top_counts[0][0] > top_counts[1][0] and top_counts[0][1] == top_counts[1][1]:
        return top_counts[1][0]
    else:
        return top_counts[0][0]
