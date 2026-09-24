"""
This exercise request to sort the strings in a list.
1. from shortest length to longest
2. Same length: alphabetical order, comparing letters case-sensitive
3. Still tied; fewer vowels first (ignore non-letters when counting vowels)
4. Still tied: Keep the original relative order (stable sort)
5. Handle empty labels and empty lists
 NO sorted() or list.sort()
"""


def vowel_counter(label) -> int:
    counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for ch in label:
        if ch.lower() in vowels:
            counter += 1
    return counter


def comes_before(a, b) -> bool:
    if len(a) != len(b):
        return len(a) < len(b)
    if a.lower() != b.lower():
        return a.lower() < b.lower()
    if vowel_counter(a) != vowel_counter(b):
        return vowel_counter(a) < vowel_counter(b)
    return False


def find_first(labels: list[str]) -> int:
    best = 0
    for i in range(1, len(labels)):
        if comes_before(labels[i], labels[best]):
            best = i
    return best


def seed_packet_sort(labels: list[str]) -> list[str]:
    copy_labels = labels.copy()
    new_label: list[str] = []
    while len(copy_labels) > 0:
        pos = find_first(copy_labels)
        new_label.append(copy_labels[pos])
        copy_labels.pop(pos)
    return new_label


if __name__ == "__main__":
    the_list = ["shit", "dog", "bat", "cat", "rat", "skunk", "elephant", "lion"]
    print(comes_before("bbb", "aaa"))   # False (rule 2 decides: aaa first)
    print(comes_before("ab", "AB"))     # False (full tie)
    print(comes_before("Bb", "bb"))     # False (full tie)
    print(comes_before("hi", "test"))   # True  (rule 1)
    print(seed_packet_sort(the_list))
