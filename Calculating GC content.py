class find_the_highest_GC_content:
    def highest_GC(series_dict):
        for series in series_dict.values():
            Count_A=series.count('A')
            Count_G=series.count('G')
            Count_T=series.count('T')
            Count_C=series.count('C')
            GC_computation= 100 * (Count_C+ Count_G) / (Count_A+Count_C+Count_G +Count_T) 
            for series_key in series_dict.keys():
                if series_dict[series_key]==series:
                   series_dict1[series_key]=GC_computation     
            GC_computation_list.append(GC_computation)
            for k, v in series_dict1.items():
                if v == max(series_dict1.values()):
                   max_tuple=(k,v)
        return max_tuple[1]

if __name__=="__main__":
    #Count(G + C)/Count(A + T + G + C) * 100
    max_tuple=() # to collect (key,value) where value is max
    series_dict1={} # new dict for new values
    GC_computation_list=[] # GC content => new values
    GC_content_dict={
    'Rosalind_6404':'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG',
    'Rosalind_5959':'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
    'Rosalind_0808':'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'}
    print(find_the_highest_GC_content.highest_GC(GC_content_dict))
