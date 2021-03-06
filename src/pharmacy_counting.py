from collections import defaultdict


drug_num_cost = defaultdict(dict)
sucriber_dict = defaultdict(set)

input_test = "/Users/mingleizhao/Git_projects/pharmacy_counting/input/itcont.txt"

with open(input_test,'r') as f:
    inputs = f.readlines()
    

def quick_update(drug_num_cost, subcriber_dict, line):
    """Return dictionary drug_num_cost and dictionary subscriber_dict of information about all drugs."""
    fields = line.split(",")
    drug_name = fields[-2]
    drug_cost = int(fields[-1].rstrip('\n'))
    subscriber_id = fields[0]
    if subscriber_id not in subcriber_dict[drug_name]:
        drug_num_cost[drug_name]['count'] = drug_num_cost[drug_name].get('count',0)+1
        subcriber_dict[drug_name].add(subscriber_id)
    drug_num_cost[drug_name]['cost']  = drug_num_cost[drug_name].get('cost', 0)+drug_cost
    return drug_num_cost, subcriber_dict

for line in inputs[1:]:
    drug_num_cost, subcriber_dict = quick_update(drug_num_cost, sucriber_dict, line)


class OutputTuple():
    """A simple attempt to store the required fields in output."""
    
    def __init__(self, name, cost, count):
        """Initialize attributes of the OutputTuple class."""
        self.name = name
        self.cost = cost
        self.count = count

tuple_list_unsorted = [OutputTuple(k,v['cost'],v['count']) for k,v in drug_num_cost.items()]

tuple_list_sorted = sorted(tuple_list_unsorted, key = lambda tuple_: (-tuple_.cost, tuple_.name))

output_file = "/Users/mingleizhao/Git_projects/pharmacy_counting/output/top_cost_drug.txt"

with open(output_file, 'w') as f:
    f.write('drug_name,num_prescriber,total_cost\n')
    for tuple_ in tuple_list_sorted:
        f.write(str(tuple_.name)+','+str(tuple_.count)+','+str(tuple_.cost)+'\n')

