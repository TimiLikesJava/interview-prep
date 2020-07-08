class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if(color != newColor):
            self.callDFS(image , sr , sc , color , newColor)
        return image
    
    def callDFS(self , image , sr , sc , color , newColor):
        if(sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] == newColor):
            return
        if(image[sr][sc] == color):
            image[sr][sc] = newColor
            self.callDFS(image , sr -1 , sc , color ,newColor) #up
            self.callDFS(image , sr + 1 , sc , color ,newColor) #down
            self.callDFS(image , sr , sc - 1 , color , newColor) #left
            self.callDFS(image , sr , sc + 1 , color , newColor) #right
