class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDictionary = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            wordDictionary[sortedWord].append(word)
        return list(wordDictionary.values())
