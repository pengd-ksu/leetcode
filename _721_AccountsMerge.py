class Solution:
    def dfs(self, node, graph, visited, component):
        if visited[node]:
            return
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited, component)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        visited = {}
        email_to_account = {}

        # set up graph, visited 
        for account in accounts:
            emails = account[1:]
            first_email = emails[0] # could've been last or any other
            for email in emails:
                # add undirected edges b/w first node and other nodes
                graph.setdefault(email, set()).add(first_email)
                graph.setdefault(first_email, set()).add(email)
                visited[email] = False
                email_to_account[email] = account[0] # name
        
        output = []
        for email,account in email_to_account.items():
            if visited[email]:
                continue
            # visited dict ensures that DFS gets called for every component
            # and NOT on every node
            nodes = [] # to fill all nodes (emails) in the component
            self.dfs(email, graph, visited, nodes)
            output.append([account] + sorted(nodes))
            
        return output

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = defaultdict(str)
        visited = set()
        result = []
        
        def dfs(email, merged_emails):
            visited.add(email)
            merged_emails.append(email)
            for email_to_merge in graph[email]:
                if email_to_merge not in visited:
                    dfs(email_to_merge, merged_emails)
        
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            
            first_email = emails[0]
            email_to_name[first_email] = name
            
            for em in emails[1:]:
                graph[first_email].append(em)
                graph[em].append(first_email)
                email_to_name[em] = name
                
        for email, name in email_to_name.items():
            if email not in visited:
                merged_emails = []
                dfs(email, merged_emails)
                result.append([name] + sorted(merged_emails))
                
        return result


class UnionFind:
    def __init__(self, num):
        self.parent = list(range(num))
        self.rank = [0 for _ in range(num)]
    
    def find_set(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find_set(self.parent[u])
        return self.parent[u]

    def union(self, set1, set2):
        if set1 == set2:
            return
        rank1, rank2 = self.rank[set1], self.rank[set2]
        if rank1 > rank2:
            self.parent[set2] = set1
        else:
            self.parent[set1] = set2
            if rank1 == rank2:
                self.rank[set2] += 1
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #create idx-to-address dictionary and address-to-idx dictionary
        address_set = set()
        for account in accounts:
            for address in account[1:]:
                address_set.add(address)
                
        N, M = len(accounts), len(address_set)
        addresses = sorted(list(address_set))
        idx_address_dict = {(idx + N) : address for idx, address in enumerate(addresses)}
        address_idx_dict = {address : (idx + N) for idx, address in enumerate(addresses)}
        
        #create union find object
        uf = UnionFind(N + M)
        
        #union all pairs of (person, address)
        for i, account in enumerate(accounts):
            for address in account[1:]:
                address_idx = address_idx_dict[address]
                uf.union(uf.find_set(i), uf.find_set(address_idx))
        
        #get the parent for all elements (it can be person's name or address)
        #note that for idx = 0, 1, 2, ..., N - 1, N, N + 1, ...., N + M - 2, N + M - 1,
        #0 <= idx < N      => name
        #N <= idx < N + M  => address
        parent_dict = collections.defaultdict(list)
        for i in range(N + M):
            parent = uf.find_set(i)
            parent_dict[parent].append(i)
        
        #for each group (=account), output the result
        #Note that the accounts themselves can be returned in any order
        #note: each group always contains exactly one person's name. Also, the smallest number is person's name
        res = []
        for group in parent_dict.values():
            person_idx = group[0]
            person = accounts[person_idx][0]
            data = [person]
            for address_idx in group[1:]:
                if address_idx >= N:
                    data.append(idx_address_dict[address_idx])
            res.append(data)
        
        return res


class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                em_graph[acc[1]].add(email)
                
                #connect 2nd to 1st email
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
        # here we use loop to traverse all unconnected
        # components of the graph
        for email in em_graph:
            if email not in seen:
                seen.add(email)
                 q = [email]
                component = []
                
                # this loop give us the all conneted path as here
                # all common gmail as a list in comonent
                while q:
                    edge = q.pop(0)
                    component.append(edge)
                    for nei in em_graph[edge]:
                        if nei not in seen:
                            seen.add(nei)
                           q.append(nei)
                            
                # after geting all connect comonent we sorted the as 
                # question and search the owner of the starting email
                # append in the ans
                ans.append([em_to_name[email]] + sorted(component))
        return ans        