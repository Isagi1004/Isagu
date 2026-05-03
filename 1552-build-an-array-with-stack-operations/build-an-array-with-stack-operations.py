class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        a=[]
        m=[]
        for i in range(1,n+1):
            if a!=target:
                if i in target:
                    a.append(i)
                    m.append("Push")
                if i not in target:
                    m.append("Push")
                    m.append("Pop")
        return m