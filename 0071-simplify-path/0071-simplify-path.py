class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Split the path by '/'
        components = path.split('/')
        stack = []
        
        for portion in components:
            # If it's '..', we go up one directory level if possible
            if portion == "..":
                if stack:
                    stack.pop()
            # If it's empty or '.', we do nothing
            elif portion == "." or portion == "":
                continue
            # For any valid directory name, push it to the stack
            else:
                stack.append(portion)
                
        # Reconstruct the canonical path
        return "/" + "/".join(stack)