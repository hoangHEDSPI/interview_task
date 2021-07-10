class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count_map = {}
        
        for cp_domain in cpdomains:
            count, domains = cp_domain.split()
            count = int(count)
            domains = domains.split('.')
            for i in range(len(domains)):
                sub_domain = '.'.join(domains[i:])
                if sub_domain in domain_count_map:
                    domain_count_map[sub_domain] += count
                else:
                    domain_count_map[sub_domain] = count
            
        return [str(domain_count_map[key]) + " " + key for key in domain_count_map]
        
