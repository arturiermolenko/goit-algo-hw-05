import timeit

with open("stat_1.txt", "r", encoding="windows-1251") as f:
    article_1 = f.read()
with open("stat_2.txt", "r", encoding="UTF-8-SIG") as f:
    article_2 = f.read()

existing_sub_1 = "Алгоритми"
non_existing_sub_1 = "Хешування"
existing_sub_2 = "рекомендаційні системи"
non_existing_sub_2 = "Графові бази"

def boyer_moore_unicode(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    shifts = 0
    while shifts <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shifts + j]:
            j -= 1
        if j < 0:
            return shifts
        else:
            shifts += max(1, j - bad_char.get(text[shifts + j], -1))
    return -1

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern, q=101):
    m = len(pattern)
    n = len(text)
    hpattern = 0
    htext = 0
    h = 1
    d = 256
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        hpattern = (d * hpattern + ord(pattern[i])) % q
        htext = (d * htext + ord(text[i])) % q
    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            htext = (d * (htext - ord(text[i]) * h) + ord(text[i + m])) % q
            if htext < 0:
                htext += q
    return -1

times = {
    'Boyer-Moore': {
        'article_1_existing': timeit.timeit(lambda: boyer_moore_unicode(article_1, existing_sub_1), number=1000),
        'article_1_non_existing': timeit.timeit(lambda: boyer_moore_unicode(article_1, non_existing_sub_1), number=1000),
        'article_2_existing': timeit.timeit(lambda: boyer_moore_unicode(article_2, existing_sub_2), number=1000),
        'article_2_non_existing': timeit.timeit(lambda: boyer_moore_unicode(article_2, non_existing_sub_2), number=1000)
    },
    'Knuth-Morris-Pratt': {
        'article_1_existing': timeit.timeit(lambda: kmp_search(article_1, existing_sub_1), number=1000),
        'article_1_non_existing': timeit.timeit(lambda: kmp_search(article_1, non_existing_sub_1), number=1000),
        'article_2_existing': timeit.timeit(lambda: kmp_search(article_2, existing_sub_2), number=1000),
        'article_2_non_existing': timeit.timeit(lambda: kmp_search(article_2, non_existing_sub_2), number=1000)
    },
    'Rabin-Karp': {
        'article_1_existing': timeit.timeit(lambda: rabin_karp(article_1, existing_sub_1), number=1000),
        'article_1_non_existing': timeit.timeit(lambda: rabin_karp(article_1, non_existing_sub_1), number=1000),
        'article_2_existing': timeit.timeit(lambda: rabin_karp(article_2, existing_sub_2), number=1000),
        'article_2_non_existing': timeit.timeit(lambda: rabin_karp(article_2, non_existing_sub_2), number=1000)
    }
}

print(times)

