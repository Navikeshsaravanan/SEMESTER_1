# Question_5 Unique Web Crawler Links
def update_visited_links(visited_links_set,new_link_list):
    count = 0
    for i in new_link_list:
        if i not in visited_links_set:
            count+=1
    j = visited_links_set.union(set(new_link_list))
    print((j,count))
visi = eval(input("enter the visited links in set:"))
new = eval(input("enter the newly visited links in lists:"))
update_visited_links(visi,new)