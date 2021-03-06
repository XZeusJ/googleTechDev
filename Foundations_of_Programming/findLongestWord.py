# Qusetion Describe
'''
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
'''

'''
1. brute-force algorithm
use S to generate all 2**len(S) possible subsequences. 
then we go through D to find the longest word in D and strSET
 A slight optimization is to at least ensure the dictionary is represented 
 by a hash table or prefix tree (tries) so that lookups are efficient.
this algorithm cost O(2**len(S)) ?!..
'''

S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}


def getSET(s, strSet=[]):
    if len(s) == 0:
        return strSet

    if len(strSet) == 0:
        strSet.append(s[0])
    else:
        for st in strSet[:]:
            strSet.append(st + s[0])
        strSet.append(s[0])
    return getSET(s[1:], strSet)


def longestWord(S, D):
    strSet = getSET(S)
    lw = ""
    for s in D:
        if s in strSet and len(s) > len(lw):
            lw = s
    return lw


# print(longestWord(S, D))

'''
2. cancellation algorithm :?
for each character in S, we go through every string in D to see
whether the first character in that string is as same as the current character
in S. If so, delete the character of string in D
finally check if there some word deleted complete in D, and the result is 
the longest word in these removed string.
O(len(S)*len(D))
'''


def longestWord2(S, D=set()):
    D = list(D)
    cpD = D.copy()
    for char in S:
        for i in range(len(cpD)):
            if len(cpD[i]) > 0 and char == cpD[i][0]:
                cpD[i] = cpD[i][1:]  # delete first character of str in D if matches

    lw = ""
    for i in range(len(cpD)):
        if len(cpD[i]) == 0 and len(D[i]) > len(lw):
            lw = D[i]

    return lw


# print(longestWord2(S, D))

'''
3. Greedy algorithm
for each str in D, we match the string with S using indexOf.
which is if we can find first character of str in S, then we continue 
finding second character of str in S that is left part starting from the first character index
if we can completely go through whole word, we can assure that word is in S
worst-case: O()
'''


def isInS(word, S=""):
    # for c in word:
    #     index = S.find(c)
    #     if index == -1: return False
    #     S = S[index + 1:]
    # return True

    # it is far from optimal in a worst-case scenario where S may be
    # long and the dictionary strings quite short.
    i = 0
    for c in S:
        if word[i] == c:
            i += 1
        if i == len(word):
            return True
    return False


def longestWord3(S, D):
    lw = ""
    for word in D:
        if isInS(word, S) and len(word) > len(lw):
            lw = word
    return lw


# print(longestWord3(S, D))

'''
4. sort + greedy
first we sort the D, start from longest word to see if it's in S
O(N*W) where W is the number of words in D and N is the number of characters in S.
'''


def longestWord4(S, D):
    D = list(D)
    D.sort(key=lambda x: len(x), reverse=True)
    return longestWord3(S, D)


print(longestWord4(S, D))
D = ["ba", "ab", "a", "b"]

sorted(D, key=lambda x: len(x))
reversed(D)
print(longestWord4("bab", ["ba", "ab", "a", "b"]))

'''
5. improving the greedy approach
because the S is ordered, so maybe we can find some way use binary search
so we preprocess S to find such indices where letter occurs
first we map each character in S into ordered number

'''

import collections


def longestWord5(letters, words):
    # preprocess letters
    letter_positions = collections.defaultdict(list)
    # For each letter in 'letters', collect all the indices at which it appears.
    # O(#letters) space and speed.
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
    # For words, in descending order by length...
    # Bails out early on first matched word, and within word on
    # impossible letter/position combinations, but worst case is
    # O(#words # avg-len) * O(#letters / 26) time; constant space.
    # With some work, could be O(#W * avg-len) * log2(#letters/26)
    # But since binary search has more overhead
    # than simple iteration, log2(#letters) is about as
    # expensive as simple iterations as long as
    # the length of the arrays for each letter is
    # “small”.  If letters are randomly present in the
    # search string, the log2 is about equal in speed to simple traversal
    # up to lengths of a few hundred characters.
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
        # Find any remaining valid positions in search string where this
        # letter appears.  It would be better to do this with binary search,
        # but this is very Python-ic.
        possible_positions = [p for p in letter_positions[letter] if p >= pos]
        if not possible_positions:
            break
        pos = possible_positions[0] + 1
        if possible_positions:
            # We didn't break out of the loop, so all letters have valid positions
            return word


print(longestWord5(S, D))
