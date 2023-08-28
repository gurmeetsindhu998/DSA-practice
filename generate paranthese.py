def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []

        def traverse(left, right, s):

            if left+right == n*2:
                res.append(s)
                return

            if left < n:
                traverse(left+1,right,s+"(")

            if right <left:
                traverse(left,right+1,s+")")

        traverse(1,0,"(")

        return res

generateParenthesis(3)