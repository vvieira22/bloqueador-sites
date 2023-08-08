def all_websites() -> list:
    a = int(input("how many websites? "))
    website_list = []
    for i in range(a):
        website_list.append(str(input("Enter the website URL: ")))

    return website_list

def blocker():
    ip = "127.0.0.1"
    with open(r"C:/windows/System32/drivers/etc/hosts", "r+") as host:
        content = host.read()
        for i in all_websites():
            if i in content:
                print(i + " is already blocked")
                pass
            else:
                what_to_write = "\n" + ip + "       " + i + "\n"
                host.write(what_to_write)

def unblocker():
    with open(r"C:/Windows/System32/drivers/etc/hosts", "r+") as host:
        content = host.read()
        my_websites = all_websites()
        for i in range(len(my_websites)):
            if my_websites[i] in content:
                new_content = content.replace(my_websites[i], "")
                host.truncate(0)
                host.write(new_content)
            else:
                print(i + " has not been blocked")

if __name__ == "__main__":
    menu_driven = int(input("1. Block a website, 2. Unblock a Website: "))
    if menu_driven == 1:
        blocker()
    elif menu_driven == 2:
        unblocker()
    else:
        print("Enter")