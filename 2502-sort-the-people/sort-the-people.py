class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        students=dict(zip(heights,names))
        ans=[]
        for value in sorted(students.keys(),reverse=True):
            ans.append(students[value])
        return ans