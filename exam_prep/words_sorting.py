
def words_sorting(*words):
    words_dict = {w: sum(map(ord, w)) for w in words}

    if sum(words_dict.values()) % 2 == 0:
        return "\n".join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: x[0])])

    return "\n".join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: -x[1])])

