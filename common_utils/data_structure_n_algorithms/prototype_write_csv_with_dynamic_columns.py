import csv

headers = ['Username', 'Date', 'Status', 'provider.cnbc', 
            'provider.xfinity', 'provider.zyx']
rows = [{'Username':'testuser', 'Date':'6/11/2014', 'Status':'active', 
           'provider.cnbc':'1234567890', 'provider.xfinity':'asdfhagsdfah'},
        {'Username':'testuser2', 'Date':'9/17/2013', 'Status':'active',
           'provider.xfinity':'asdfhagsdfah', 'provider.zyx':'xyz987654'},
        {'Username':'testuser3', 'Date':'2/11/2012', 'Status':'inactive',
           'provider.zyx':'xyz987654'},
       ]

# we figure out the headers after looping through all rows

with open('members_dynamic_columns.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
