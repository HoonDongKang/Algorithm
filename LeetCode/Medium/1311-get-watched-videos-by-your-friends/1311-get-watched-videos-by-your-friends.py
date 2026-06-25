from collections import deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        queue = deque([(id, 0)])
        visited = [False] * len(friends)
        visited[id] = True
        find_friend = set()
        videos_frequency = {}

        while queue:
            idx, cur_count = queue.popleft()
            for edge in friends[idx]:
                if visited[edge]:
                    continue

                now_count = cur_count + 1
                visited[edge] = True

                if now_count == level:
                    find_friend.add(edge)
                elif now_count < level:
                    queue.append((edge,now_count))
    
        for idx in find_friend:
            videos = watchedVideos[idx]

            for vid in videos:
                videos_frequency[vid] = videos_frequency.get(vid, 0) + 1
        
        return sorted(videos_frequency.keys(), key=lambda video: (videos_frequency[video], video))