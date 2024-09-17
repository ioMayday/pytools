# -*- coding: utf-8 -*-
'''
功能：命令行增删查改地址簿
博客：Python世界：简易地址簿增删查改算法实践
地址：https://blog.csdn.net/qq_17256689/article/details/142264232
'''

import json

# 初始化地址簿，添加默认联系人
address_book_init = {
    "Alice": {"email": "alice@example.com", "phone": "123-456-7890"},
    "Bob": {"email": "bob@example.com", "phone": "234-567-8901"},
    "Charlie": {"email": "charlie@example.com", "phone": "345-678-9012"}
}

# 保存地址簿到文件
def save_address_book(address_book):
    with open('address_book.json', 'w') as file:
        json.dump(address_book, file)

# 从文件读取地址簿
def load_address_book():
    try:
        with open('address_book.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return address_book_init

# 显示地址簿全文
def read_address_book(address_book):
    for name, info in address_book.items():
        print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}")

# 查找联系人
def find_contact(address_book, name):
    if name in address_book:
        info = address_book[name]
        print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}")
    else:
        print(f"Contact {name} not found.")

# 删除联系人
def delete_contact(address_book, name):
    if name in address_book:
        del address_book[name]
        save_address_book(address_book)
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

# 增加联系人
def add_contact(address_book, name, email, phone):
    address_book[name] = {"email": email, "phone": phone}
    save_address_book(address_book)
    print(f"Contact {name} added.")

# 修改联系人
def modify_contact(address_book, name, email, phone):
    if name in address_book:
        address_book[name] = {"email": email, "phone": phone}
        save_address_book(address_book)
        print(f"Contact {name} modified.")
    else:
        print(f"Contact {name} not found.")

# 主函数
def main():
    address_book = load_address_book()
    while True:
        command = input("Enter command (--read, --find, --delete, --add, --modify, --exit): ")
        if command == "--read":
            read_address_book(address_book)
        elif command == "--find":
            name = input("Enter name to find: ")
            find_contact(address_book, name)
        elif command == "--delete":
            name = input("Enter name to delete: ")
            delete_contact(address_book, name)
        elif command == "--add":
            name = input("Enter name to add: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            add_contact(address_book, name, email, phone)
        elif command == "--modify":
            name = input("Enter name to modify: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            modify_contact(address_book, name, email, phone)
        elif command == "--exit":
            save_address_book(address_book)
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

