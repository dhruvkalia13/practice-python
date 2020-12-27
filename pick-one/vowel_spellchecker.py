class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        output = []
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        words_vow_masked = []
        for word in wordlist:
            a = ""
            for char in word:
                a = a + ("*" if char in vowels else char)
            words_vow_masked.append(a)
        lower_wordlist = [word.lower() for word in wordlist]
        lower_word_masked = [word.lower() for word in words_vow_masked]
        query_vow_masked = []
        for query in queries:
            a = ""
            for char in query:
                a = a + ("*" if char in vowels else char)
            query_vow_masked.append(a)

        for query in queries:
            query_dict = {}
            if query in wordlist:
                output.append(query)
                continue
            lower_query = query.lower()
            if lower_query in lower_wordlist:
                output.append(wordlist[lower_wordlist.index(lower_query)])
                continue
            i = queries.index(query)
            if query_vow_masked[i].lower() in lower_word_masked:
                j = lower_word_masked.index(query_vow_masked[i].lower())
                output.append(wordlist[j])
                continue
            output.append("")
            # done_outside = False
            # for q in query:
            #     done_inside = False
            #     if q.lower() in vowels:
            #         loc_vow = vowels.index(q.lower())
            #         for vowel in vowels:
            #             if vowels.index(vowel) != loc_vow:
            #                 i = query.index(q)
            #                 if query[:i] + vowel.lower() + query[i+1:] in wordlist:
            #                     output.append(query[:i] + vowel.lower() + query[i+1:])
            #                     done_inside = True
            #                     done_outside = True
            #                     break
            #                 elif query[:i] + vowel.upper() + query[i+1:] in wordlist:
            #                     output.append(query[:i] + vowel.upper() + query[i+1:])
            #                     done_inside = True
            #                     done_outside = True
            #                     break
            #     if done_inside: break
            # if done_outside is False:
            #     output.append("")
        return output
