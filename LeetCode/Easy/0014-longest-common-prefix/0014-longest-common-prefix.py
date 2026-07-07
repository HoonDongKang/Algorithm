class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def buildNode():
            return { 'children': {}, 'is_end': False }
        
        trie = buildNode()
        def buildTrie(word):
            cur = trie
            for char in word:
                if char not in cur['children']:
                    cur['children'][char] = buildNode()

                cur = cur['children'][char]

            cur["is_end"] = True
        
        for word in strs:
            buildTrie(word)

        cur = trie
        result = ""

        while not cur["is_end"] and len(cur["children"]) == 1:
            char, next_node = list(cur["children"].items())[0]
            result += char
            cur = next_node
        
        return result