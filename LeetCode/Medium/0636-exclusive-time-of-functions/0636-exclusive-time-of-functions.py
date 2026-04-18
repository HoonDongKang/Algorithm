class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exec_time = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            id, flag, time = log.split(":")
            id = int(id)
            time = int(time)

            if flag == "start":
                if stack:
                    exec_time[stack[-1]] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                exec_time[stack[-1]] += time - prev_time + 1
                stack.pop()
                prev_time = time + 1

        return exec_time
