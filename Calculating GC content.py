#unt(G + C)/Count(A + T + G + C) ** 100
GC_content= 'AGTCAG'
max_list=()
series_dict1={}
GC_computation_list=[]
dict_gc_max={}
GC_content_dict={
'Rosalind_6404':'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG',
'Rosalind_5959':'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
'Rosalind_0808':'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'}
def highest_GC(series_dict):
    for series in series_dict.values():
       # while len(series)>0:
        Count_A=series.count('A')
        Count_G=series.count('G')
        Count_T=series.count('T')
        Count_C=series.count('C')
        GC_computation= (Count_C+ Count_G) / (Count_A+Count_C+Count_G +Count_T) 
        # series_dict1.update(series=GC_computation)
        for series_key in series_dict.keys():
            series_dict1[series_key]=GC_computation
    
        GC_computation_list.append(GC_computation)
        for k, v in series_dict1.items():
            if v == max(series_dict1.values()):
               max_list=(k,v)
    return GC_computation_list, max_list
print(highest_GC(GC_content_dict))