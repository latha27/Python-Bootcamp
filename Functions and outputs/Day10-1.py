
f_name=input("Enter the first name:")
l_name=input("Enter the last name:")
def format_name(ff_name,ll_name):
    ff_name=f_name.title()
    ll_name=l_name.title()
    return f"{ff_name} {ll_name}"
print(format_name(f_name,l_name))

