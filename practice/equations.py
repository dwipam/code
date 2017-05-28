class Solution(object):
    def calcEquation(self, equations, values, queries):
        un = set(reduce(lambda x,y:x+y,z)
        dic = self.compute_coef(values,map(lambda x:tuple(x),equations))
        import pdb;pdb.set_trace()
        return map(lambda x: dic[tuple(x)] if tuple(x) in dic.keys() else -1.0,queries) 
    def compute_coef(self,values,equations):
        print equations
        dic = {}
        for i in range(len(equations)):
             dic[equations[i]] = values[i]
             dic[equations[i][::-1]] = 1/values[i]
        for i in range(len(equations)-1):
            l = i+1
            dic[(equations[i][0],equations[l][1])] = values[i]*values[l]
            dic[(equations[i][0],equations[l][1])[::-1]] = 1/(values[i]*values[l])
        return dic

s = Solution()
print(s.calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
