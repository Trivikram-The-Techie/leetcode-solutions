class Solution:

    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        n = len(s)
        s_list = list(s)

        # tree[node] = [leftChar, rightChar, maxLen, prefixLen, suffixLen, segLen]
        tree = [None] * (4 * n)

        def merge(left, right):
            lc, rc = left[0], right[1]
            segLen = left[5] + right[5]

            # Base max length is the max of both subtrees
            maxLen = max(left[2], right[2])

            # Merge prefix length
            prefixLen = left[3]
            if left[3] == left[5] and left[1] == right[0]:
                prefixLen = left[5] + right[3]

            # Merge suffix length
            suffixLen = right[4]
            if right[4] == right[5] and left[1] == right[0]:
                suffixLen = right[5] + left[4]

            # If characters across the boundary match, consider the combined middle block
            if left[1] == right[0]:
                maxLen = max(maxLen, left[4] + right[3])

            maxLen = max(maxLen, prefixLen, suffixLen)

            return [lc, rc, maxLen, prefixLen, suffixLen, segLen]

        def build(node, start, end):
            if start == end:
                c = s_list[start]
                tree[node] = [c, c, 1, 1, 1, 1]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, val):
            if start == end:
                s_list[idx] = val
                tree[node] = [val, val, 1, 1, 1, 1]
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)

        result = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            result.append(tree[1][2])  # tree[1][2] is maxLen at root

        return result