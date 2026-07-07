class Solution:
    def longestWord(self, words: list[str]) -> str:
        def buildNode():
            return { 'children': {}, 'is_end': False }
        
        trie = buildNode()

        def buildTrie(word):
            cur = trie
            for char in word:
                if char not in cur['children']:
                    cur['children'][char] = buildNode()

                cur = cur['children'][char]

            cur['is_end'] = True
        
        for word in words:
            buildTrie(word)

        answer = ""

        def dfs(node, word):
            nonlocal answer

            if len(word) > len(answer):
                answer = word

            elif len(word) == len(answer) and word < answer:
                answer = word

            for char in node['children']:
                next_node = node['children'][char]

                if not next_node['is_end']:
                    continue

                dfs(next_node, word + char)
            
        dfs(trie, "")

        return answer