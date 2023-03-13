from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: heappop(live)
            if negH: heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
        return res[1:]


class Solution:
    def getSkyline(self, buildings):
        # 对于一个 building, 他由 (l, r, h) 三元组组成, 我们可以将其分解为两种事件: 
        #     1. 在 left position, 高度从 0 增加到 h(并且这个高度将持续到 right position); 
        #     2. 在 right position, 高度从 h 降低到 0. 
        # 由此引出了 event 的结构: 在某一个 position p, 它引入了一个高度为 h 的 skyline, 
        # 将一直持续到另一 end postion
        
        # 对于在 right position 高度降为 0 的 event, 它的持续长度时无效的
        # 只保留一个 right position event, 就可以同时触发不同的两个 building 在同一 
        # right position 从各自的 h 降为 0 的 event, 所以对 right position events 
        # 做集合操作会减少计算量
        
        # 由于需要从左到右触发 event, 所以按 postion 对 events 进行排序
        # 并且, 对于同一 positon, 我们需要先触发更高 h 的事件, 先触发更高 h 的事件后, 那么
        # 高的 h 相比于低的 h 会占据更高的 skyline, 低 h 的 `key point` 就一定不会产生; 
        # 相反, 可能会从低到高连续产生冗余的 `key point`
        # 所以, event 不仅需要按第一个元素 position 排序, 在 position 相同时, 第二个元素 
        # h 也是必须有序的
        events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))
        
        # res 记录了 `key point` 的结果: [x, h]; 同时 res[-1] 处的 `key point` 
        # 代表了在下一个 event 触发之前, 一直保持的最高的 skyline
        
        # hp 记录了对于一条高为 h 的 skyline, 他将持续到什么 position 才结束: 
        # [h, endposition] 在同时有多条 skyline 的时候, h 最高的那条 skyline 会掩盖 h 
        # 低的 skyline, 因此在 event 触发时, 需要得到当前最高的 skyline 所以利用 heap 结构
        # 存储 hp, 它的第一个值永远为列表中的最小值: 因此在 event 中记录的是-h, heap 结构就
        # 会返回最高的 skyline. 同时, h 必须在 endposition 之前, 因为它按第一个元素排序
        res, hp = [[0, 0]], [(0, float('inf'))]

        for l, neg_h, r in events:
            # 触发 event 时, 首先要做的就是清除已经到 endposition 的 skyline
            # hp: [h, endposition]
            # 如果当前 position 大于等于了 hp 中的 endposition, 那么该 skyline 会被清除掉
            # 由于在有 high skyline 的情况下, low skyline 不会有影响, 因此, 只需要按从高
            # 到低的方式清除 skyline, 直到剩下一个最高的 skyline 并且它的 endposition 大
            # 于当前 position
            while l >= hp[0][1]: 
                heapq.heappop(hp)
            
            # 对于高度增加到 h 的时间(neg_h < 0), 我们需要添加一个 skyline, 他将持续到 r 
            # 即 endposition
            if neg_h:
                heapq.heappush(hp, (neg_h, r))
            
            # 由于 res[-1][1] 记录了在当前事件触发之前一直保持的 skyline
            # 如果当前事件触发后 skyline 发生了改变
            #     1. 来了一条新的高度大于 h 的 skyline
            #     2. res[-1] 中记录的 skyline 到达了 endposition
            # 这两种事件都会导致刚才持续的 skyline 与现在最高的 skyline 不同; 同时, 
            # `key point` 产生了, 他将被记录在 res 中 
            if res[-1][1] != -hp[0][0]:
                res.append([l, -hp[0][0]])
        
        return res[1:]


from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        # 不难发现这些关键点的特征是：竖直线上轮廓升高或者降低的终点
        # 所以核心思路是：从左至右遍历建筑物，记录当前的最高轮廓，如果产生变化则记录一个关键点
        
        # 首先记录构造一个建筑物的两种关键事件
        # 第一种是轮廓升高事件(L, -H)、第二种是轮廓降低事件(R, 0)
        # 轮廓升高事件(L, -H, R)中的R用于后面的最小堆
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})

        # 先根据L从小到大排序、再根据H从大到小排序(记录为-H的原因)
        # 这是因为我们要维护一个堆保存当前最高的轮廓
        events.sort()

        # 保存返回结果
        res = [[0, 0]]
        
        # 最小堆，保存当前最高的轮廓(-H, R)，用-H转换为最大堆，R的作用是记录该轮廓的有效长度
        live = [(0, float("inf"))]

        # 从左至右遍历关键事件
        for L, negH, R in events:
            
            # 如果是轮廓升高事件，记录到最小堆中
            if negH: heappush(live, (negH, R))
            
            # 获取当前最高轮廓
            # 根据当前遍历的位置L，判断最高轮廓是否有效
            # 如果无效则剔除，让次高的轮廓浮到堆顶，继续判断
            while live[0][1] <= L: 
                heappop(live)
            
            # 如果当前的最高轮廓发生了变化，则记录一个关键点
            if res[-1][1] != -live[0][0]:
                res += [ [L, -live[0][0]] ]
        return res[1:]


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]

class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        """
        Divide-and-conquer algorithm to solve skyline problem,
        which is similar with the merge sort algorithm.
        """
        n = len(buildings)
        # The base cases
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        # If there is more than one building,
        # recursively divide the input into two subproblems.
        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2 :])

        # Merge the results of subproblem together.
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):
        """
        Merge two skylines together.
        """
        def update_output(x, y):
            """
            Update the final output with the new element.
            """
            # if skyline change is not vertical -
            # add the new point
            if not output or output[-1][0] != x:
                output.append([x, y])
            # if skyline change is vertical -
            # update the last point
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):
            """
            Append the rest of the skyline elements with indice (p, n)
            to the final output.
            """
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        p_l = p_r = 0
        curr_y  = left_y = right_y = 0
        output = []

        # while we're in the region where both skylines are present
        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            # pick up the smallest x
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            # max height (i.e. y) between both skylines
            max_y = max(left_y, right_y)
            # if there is a skyline change
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # there is only left skyline
        append_skyline(p_l, left, n_l, left_y, curr_y)

        # there is only right skyline
        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output