import sys
f = open('vote.txt')
mylist = list(f)
Democrats = set()
for i in range(len(mylist)):
	mylist[i] = mylist[i].split(' ')
	if mylist[i][1] == 'D':
		Democrats.add(mylist[i][0])
#print(mylist)
#print(Democrats)
vote_list = [[0 for j in range(len(mylist[0])-3)] for i in range(len(mylist))]
#print(len(vote_list[0]))
for i in range(len(mylist)):
	for j in range(len(mylist[i])-3):
		vote_list[i][j] = int(mylist[i][j+3])
#print(vote_list)
dic = {}
for i in range(len(mylist)):
	dic[mylist[i][0]] = vote_list[i]

def policy_compare(sen_a,sen_b,voting_dict):
	sen_a_list = voting_dict[sen_a]
	sen_b_list = voting_dict[sen_b]
	simi = 0
	for i in range(len(sen_a_list)):
		simi += sen_a_list[i]*sen_b_list[i]
	return simi

print('Task2: dot_product is '+ str(policy_compare('Akaka','Alexander',dic)))
def most_similar(sen,voting_dict):
	comp_dic = {}
	for key in dic.keys():
		comp_dic[key] = policy_compare(key,sen,dic)
	del comp_dic[sen]
	msimi = max(comp_dic, key = comp_dic.get)
	return msimi

print('Task3: '+ most_similar('Akaka',dic))
def least_similar(sen,voting_dict):
	comp_dic = {}
	for key in dic.keys():
		comp_dic[key] = policy_compare(key,sen,dic)
	del comp_dic[sen]
	msimi = min(comp_dic, key = comp_dic.get)
	return msimi
print('Task4: '+ least_similar('Akaka',dic))
print('Task5: ' + most_similar('Chafee',dic))
print('Task5: ' + least_similar('Santorum',dic))

def find_average_similarity(sen,sen_set,voting_dict):
	sum_ = 0
	sen_set_list = list(sen_set)
	#print(sen_set_list)
	for i in sen_set_list:
		sum_ += policy_compare(sen,i,dic)
	aver = sum_ / len(sen_set_list)
	return aver
print('Task6: dot_product is '+str(find_average_similarity('Akaka',Democrats,dic)))

def find_average_record(sen_set, voting_dict):
	sen_set_list = list(sen_set)
	total_list = [0 for i in range(len(vote_list[0]))]
	for i in range(len(vote_list[0])):
		for j in sen_set_list:
			total_list[i] += dic[j][i]
	for i in range(len(total_list)):
		total_list[i] = total_list[i] / len(sen_set_list)
	return total_list
print('Task6: find_average_record '+ str(find_average_record(Democrats,dic)))

#2.12.7:find the senator who has the greatest average similarity with Democrats
Democrats_comp0 = {}
for key in dic.keys():
	Democrats_comp0[key] = find_average_similarity(key,Democrats,dic)
msimi = max(Democrats_comp0, key = Democrats_comp0.get)
print('2.12.7\n the senator who has the greatest average similarity with the Democrats is ' + msimi)
#2.12.8
average_Democrat_record = find_average_record(Democrats,dic)
dic['Average_D_r'] = average_Democrat_record
#print(dic)
Democrats_comp1 = {}
for key in dic.keys():
	Democrats_comp1[key] = policy_compare(key,'Average_D_r',dic)
del Democrats_comp1['Average_D_r' ]
print( 'Average_D_r' in Democrats_comp1)
msimi0 = max(Democrats_comp1, key = Democrats_comp1.get)

print('2.12.8\n the senator who has the greatest average similarity with the Democrats is ' + msimi0)

#2.12.9 use obvious way (too lazy to write the fast matrix multiplication without third-party modelus)
def dot_p(list_a,list_b):
	dot_p = 0
	for i in range(len(list_a)):
		dot_p += list_a[i]*list_b[i]
	return dot_p
def bitter_rivals(voting_dict):
	obvious_way_dic = {}
	tmp = [[0 for i in range(2)] for j in range(len(mylist))]
	for i in range(len(mylist)):
		tmp[i][0] = mylist[i][0]
		tmp[i][1] = vote_list[i]
	for i in range(len(tmp)-1):
		for j in range(i+1,len(tmp)):
			obvious_way_dic[tmp[i][0] + ' and ' + tmp[j][0]] = dot_p(tmp[i][1],tmp[j][1])
	obvious_way_dic[tmp[-2][0] + ' and ' + tmp[-1][0]] = dot_p(tmp[-2][1],tmp[-1][1])
	mdis = min(obvious_way_dic, key = obvious_way_dic.get)
	return mdis
print('2.12.9\n Im not sure because the lexicographical order sucks but these two senators disagree most according to my program: ',bitter_rivals(dic))
		
	
