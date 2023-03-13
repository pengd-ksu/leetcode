class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        for i in range(len(recipes)):
            graph[recipes[i]].extend(ingredients[i])
        sup = set(supplies)    
        res = []
        path = dict()

        def dfs(rec):
            if rec in path:
                return path[rec]
            path[rec] = False # Cycle detection
            for ing in graph[rec]:
                if ing in graph.keys():# ing is a recipe
                    if not dfs(ing):
                        return False
                else: # ing is not a recipe
                    if ing not in sup: # check if it's original supply
                        path[ing] = False
                        return False
            path[rec] = True
            return True
        
        for rec in recipes:
            if dfs(rec):
                res.append(rec)
                
        return res

["ju","fzjnm","x","e","zpmcz","h","q"]

[["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],
["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],
["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]

["f","hveml","cpivl","d"]