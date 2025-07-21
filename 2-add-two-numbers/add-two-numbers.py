class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = ""
        s2 = ""
        current1 = l1
        current2 = l2

        while True:
            if current1:
                s1 += str(current1.val)
                current1 = current1.next
            if current2:
                s2 += str(current2.val)
                current2 = current2.next
            if not current1 and not current2:
                break
        total = int(s1[::-1]) + int(s2[::-1])

        dummy = ListNode(0)
        curr = dummy
        for digit in str(total)[::-1]:  # reverse for correct order
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
