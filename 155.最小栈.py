#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (47.24%)
# Total Accepted:    21.2K
# Total Submissions: 44K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
#
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#

# @lc code=start

class MinStack(object):
    """使用两个栈, 一个记录值, 一个记录当前最小值"""

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, x: int):
        if not self.stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# @lc code=end

if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(3)
    obj.push(2)
    print(obj.getMin())
    print(obj.pop())
    print(obj.getMin())

