import itertools


class Solution:
    def compressString(self, S: str) -> str:
        # ans=[]
        # cnt=0

        # for i,val in enumerate(s):
        #     if i != 0 and s[i]!=s[i-1]:
        #         ans.append(s[i-1]+str(cnt))
        #         cnt=0
        #     cnt +=1

        # if cnt:
        #     ans.append(s[-1]+str(cnt))

        # return min(s, "".join(ans),key=len)
        return min(S, "".join(k + str(len(list(v))) for k, v in itertools.groupby(S)), key=len)
        # return min(S, re.sub(r"(?P<dup>.)\1*",
        #                      lambda x: x.group("dup") + str(len(x.group())), S))


print(Solution().compressString(S="aabcccccaaa"))
