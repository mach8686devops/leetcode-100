class Solution:
    """
    @param to: The target of everyone will throw the handkerchief to.
    @return: Return the number of turns the game will stop.
    """

    def gameTurns(self, to):
        n = len(to)
        min_turn = n

        for i in range(n):
            position = i
            turn_count = 0
            visited = set()

            position = to[position]
            turn_count += 1
            while position != i:
                position = to[position]
                turn_count += 1
                # 如果到了已访问过的点，代表这个手绢进入了死循环，到不了出发点
                if position in visited:
                    break
                visited.add(position)

            # 只有回到出发点的，才算作有效的值
            if position == i:
                min_turn = min(min_turn, turn_count)

        return min_turn
