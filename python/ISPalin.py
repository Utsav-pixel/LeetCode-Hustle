import math

















# class Solution:
#     def isPalin(self,N):
#         if N == 0:
#             return True
#         x= math.floor(math.log10(abs(N)))
#         if N//10**x == N%10:
#             N = N%10**x  # Trim from start
#             N = N//10    # Trim from end

#             if not self.isPalin(N):
#                 return False
            
#         else:
#             return False
#         return True

# Sol = Solution()
# print(Sol.isPalin(10041))