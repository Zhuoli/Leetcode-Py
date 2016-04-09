class Solution(object):
    def longestIncreasingPath(self, matrix):
        if matrix == None or len(matrix) == 0:
            return 0
        longestPath = 0
        pathDic={}
        Width = len(matrix[0])
        Height = len(matrix)

        for row in range(0,Height):
            for col in range(0, Width):
                #Longest path start from this point
                length = self.travel(matrix, row, col, pathDic)
                #Record
                pathDic[str(row)+ ',' +str(col)] = length
                if longestPath < length:
                    longestPath = length

        return longestPath

    def travel(self, matrix, row, col, pathDic):
        Width = len(matrix[0])
        Height = len(matrix)
        pathLength = 1
        if row-1>=0 and matrix[row-1][col]>matrix[row][col]:
            subpathLength = self.helper(pathDic, row-1, col,matrix)
            if subpathLength + 1 > pathLength:
                pathLength = subpathLength + 1
        if row+1<Height and matrix[row+1][col]>matrix[row][col]:
            subpathLength = self.helper(pathDic, row+1, col,matrix)
            if subpathLength + 1 > pathLength:
                pathLength = subpathLength + 1
        if col-1>=0 and matrix[row][col-1]>matrix[row][col]:
            subpathLength = self.helper(pathDic, row, col-1,matrix)
            if subpathLength + 1 > pathLength:
                pathLength = subpathLength + 1
        if col+1<Width and matrix[row][col+1]>matrix[row][col]:
            subpathLength = self.helper(pathDic, row, col+1,matrix)
            if subpathLength + 1 > pathLength:
                pathLength = subpathLength + 1
        return pathLength

    def helper(self,pathDic, neighborRow, neighborCol, matrix):
        key = str(neighborRow) + ',' + str(neighborCol)
        if not key in pathDic:
            subPathLength = self.travel(matrix, neighborRow, neighborCol, pathDic)
            pathDic[key] = subPathLength
        neighborPath = pathDic[key]
        return neighborPath
matrix = []
solution = Solution()
p = solution.longestIncreasingPath(matrix)
print(p)