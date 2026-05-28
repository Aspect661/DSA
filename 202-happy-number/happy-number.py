class Solution:
    def isHappy(self, n: int) -> bool:

        def square(num):
            
            sum = 0
            while num!=0:
                x = num%10
                sum += x**2
                num = num // 10
            
            return sum
        
        # store_num = []
        # store_num.append(square(n))

        # while 1 not in store_num:
        #     num = square(store_num[-1])
        #     if num == 1:
        #         return True
        #     elif num in store_num: 
        #         return False
        #     else:
        #         store_num.append(num)
        
        # return square(n) == 1
            
        slow = square(n)
        fast = square(square(n))

        while(slow!=fast):
            if slow == 1 or fast == 1:
                return True
            slow = square(slow)
            fast = square(square(fast))
        
        return slow == 1