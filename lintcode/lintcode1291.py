class Solution:
    """
    @param Events: the start and end time
    @return: if there has a solution return 1, otherwise return -1.
    """

    def CheerAll(self, Events):
        # write your code here
        order_events = []
        num = len(Events)
        now = 1

        for i in range(num):
            leave = Events[i][1] - int((Events[i][1] - Events[i][0]) / 2) - 1
            order_events += [[leave, i]]
        order_events.sort()
        for i in range(num):
            index = order_events[i][1]
            start = Events[index][0]
            end = Events[index][1]
            leave = order_events[i][0]
            now = int(max(now, start))
            if now > leave:
                return -1
            now += ((end - start) // 2) + 1
        return 1
